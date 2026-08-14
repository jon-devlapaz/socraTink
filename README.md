# Socratink

Socratink is a minimal, model-backed conversation surface built on a locally
owned learning harness.

This baseline intentionally does one thing: it connects the Socratink web
interface to one model-backed chat agent. Learning behavior comes later, after
the foundation works reliably.

## Run the current app

Requirements: Node.js 22+, pnpm 11, and an OpenAI-compatible model endpoint.

```sh
pnpm install
pnpm --dir apps/socratink dev
```

The app reads these local environment settings without committing their values:

- `JON_LOCAL_BASE_URL` — the model endpoint; defaults to
  `http://127.0.0.1:3001/v1`
- `JON_LOCAL_API_KEY` — the endpoint's API key when required

## Repository shape

- `apps/socratink/` — the Socratink chat application and web interface
- `packages/` — the framework packages that make up the learning harness
- `apps/www/` — inherited framework documentation
- `examples/` — inherited framework integration examples
- `demo/` — inherited framework demonstration client

## Foundation and attribution

The learning harness is derived from
[Flue](https://github.com/withastro/flue), an open-source TypeScript agent
harness. Its framework packages retain their `@flue/*` names so attribution and
upstream lineage stay explicit. The repository remains licensed under the
[Apache License 2.0](LICENSE).
