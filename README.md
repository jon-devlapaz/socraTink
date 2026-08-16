# Socratink

Socratink is a minimal, model-backed conversation surface built with
[Flue](https://github.com/withastro/flue).

This baseline intentionally does one thing: it connects the Socratink web
interface to one model-backed chat agent. Learning behavior comes later, after
the foundation works reliably.

## Run the current app

Requirements: Node.js 22+, pnpm 11, and an OpenAI-compatible model endpoint.

```sh
pnpm install
pnpm dev
```

The app reads these local environment settings without committing their values:

- `JON_LOCAL_BASE_URL` — the model endpoint; defaults to
  `http://127.0.0.1:3001/v1`
- `JON_LOCAL_API_KEY` — the endpoint's API key when required

## Verify the app

```sh
pnpm check:types
pnpm build
```

The product source lives in `src/`. The default Vite build generates the
Node application in `dist/`, and the UI build writes its static assets to
`dist/client/`.

## Foundation and attribution

Socratink began as a product application inside the Flue open-source
TypeScript agent harness repository. The standalone product consumes the
published `@flue/*` packages and keeps those names, this provenance statement,
and the original [Apache License 2.0](LICENSE) so its upstream lineage remains
explicit.
