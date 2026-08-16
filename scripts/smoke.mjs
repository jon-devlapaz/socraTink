import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { createFlueClient } from '@flue/sdk';

const expectedReply = 'Socratink smoke response.';
const sockets = new Set();

function listen(server) {
	return new Promise((resolve, reject) => {
		server.once('error', reject);
		server.listen(0, '127.0.0.1', () => {
			server.off('error', reject);
			resolve(server.address().port);
		});
	});
}

function close(server) {
	return new Promise((resolve, reject) => {
		server.close((error) => (error ? reject(error) : resolve()));
		for (const socket of sockets) socket.destroy();
	});
}

async function waitForServer(url, process, timeoutMs = 10_000) {
	const deadline = Date.now() + timeoutMs;
	while (Date.now() < deadline) {
		if (process.exitCode !== null) throw new Error(`Socratink server exited with code ${process.exitCode}`);
		try {
			const response = await fetch(url);
			if (response.ok) return response;
		} catch {}
		await new Promise((resolve) => setTimeout(resolve, 50));
	}
	throw new Error(`Socratink server did not become ready within ${timeoutMs}ms`);
}

const fakeProvider = createServer(async (request, response) => {
	assert.equal(request.method, 'POST');
	assert.equal(request.url, '/v1/chat/completions');
	assert.equal(request.headers.authorization, 'Bearer smoke-test-key');

	let body = '';
	for await (const chunk of request) body += chunk;
	const payload = JSON.parse(body);
	assert.equal(payload.model, 'auto');
	assert.equal(payload.stream, true);

	response.writeHead(200, {
		'content-type': 'text/event-stream',
		'cache-control': 'no-cache',
		connection: 'keep-alive',
	});
	const chunks = [
		{ id: 'chatcmpl-smoke', object: 'chat.completion.chunk', created: 0, model: 'auto', choices: [{ index: 0, delta: { role: 'assistant' }, finish_reason: null }] },
		{ id: 'chatcmpl-smoke', object: 'chat.completion.chunk', created: 0, model: 'auto', choices: [{ index: 0, delta: { content: expectedReply }, finish_reason: null }] },
		{ id: 'chatcmpl-smoke', object: 'chat.completion.chunk', created: 0, model: 'auto', choices: [{ index: 0, delta: {}, finish_reason: 'stop' }] },
		{ id: 'chatcmpl-smoke', object: 'chat.completion.chunk', created: 0, model: 'auto', choices: [], usage: { prompt_tokens: 4, completion_tokens: 4, total_tokens: 8 } },
	];
	for (const chunk of chunks) response.write(`data: ${JSON.stringify(chunk)}\n\n`);
	response.end('data: [DONE]\n\n');
});
fakeProvider.on('connection', (socket) => {
	sockets.add(socket);
	socket.once('close', () => sockets.delete(socket));
});

let appProcess;
let stderr = '';
try {
	const providerPort = await listen(fakeProvider);
	const portProbe = createServer();
	const appPort = await listen(portProbe);
	await close(portProbe);

	appProcess = spawn(process.execPath, ['dist/server.mjs'], {
		env: {
			...process.env,
			PORT: String(appPort),
			JON_LOCAL_BASE_URL: `http://127.0.0.1:${providerPort}/v1`,
			JON_LOCAL_API_KEY: 'smoke-test-key',
		},
		stdio: ['ignore', 'pipe', 'pipe'],
	});
	appProcess.stderr.on('data', (chunk) => {
		stderr += chunk;
	});

	const origin = `http://127.0.0.1:${appPort}`;
	const root = await waitForServer(`${origin}/`, appProcess);
	const html = await root.text();
	assert.match(html, /<title>Socratink<\/title>/);

	const assetPaths = [...html.matchAll(/(?:src|href)="([^"?#]*assets\/[^"?#]+)"/g)].map((match) => match[1]);
	assert.ok(assetPaths.length >= 2, 'expected built JavaScript and CSS assets');
	for (const path of assetPaths) {
		const asset = await fetch(new URL(path, origin));
		assert.equal(asset.status, 200, `asset ${path} should load`);
		assert.ok((await asset.arrayBuffer()).byteLength > 0, `asset ${path} should not be empty`);
	}

	const client = createFlueClient({ url: `${origin}/api/agents/chat/smoke-conversation` });
	const admission = await client.send({ message: { kind: 'user', body: 'Return the smoke response.' } });
	const reply = await client.read(admission);
	assert.equal(reply.text, expectedReply);

	console.log(`smoke passed: root, ${assetPaths.length} assets, agent route, completed response`);
} catch (error) {
	if (stderr) process.stderr.write(`\nSocratink server stderr:\n${stderr}`);
	throw error;
} finally {
	if (appProcess?.exitCode === null) {
		appProcess.kill('SIGTERM');
		await new Promise((resolve) => appProcess.once('exit', resolve));
	}
	if (fakeProvider.listening) await close(fakeProvider);
}
