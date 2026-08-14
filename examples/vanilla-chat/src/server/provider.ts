import { createProvider } from '@earendil-works/pi-ai';
import { openAICompletionsApi } from '@earendil-works/pi-ai/api/openai-completions.lazy';
import { setProvider } from '@flue/runtime';

setProvider(
	createProvider({
		id: 'jon-local',
		auth: {
			apiKey: {
				name: 'Jon local model API key',
				resolve: async () => ({ auth: { apiKey: process.env.JON_LOCAL_API_KEY } }),
			},
		},
		models: [
			{
				id: 'auto',
				name: 'Auto',
				api: 'openai-completions',
				provider: 'jon-local',
				baseUrl: 'http://100.79.25.11:3001/v1',
				reasoning: false,
				input: ['text'],
				cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
				contextWindow: 1_048_576,
				maxTokens: 1_048_576,
			},
		],
		api: openAICompletionsApi(),
	}),
);
