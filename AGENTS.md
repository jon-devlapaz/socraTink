# Socratink learning harness

Socratink is the product. The repository uses a Flue-derived TypeScript harness
as its foundation.

## Ownership

- `apps/socratink/` owns the Socratink application and learner-facing interface.
- `packages/` owns the inherited harness framework.
- Product changes belong in `apps/socratink/` unless a verified framework
  requirement proves that a package must change.
- Keep Flue attribution, Apache licensing, and `@flue/*` package names intact.

Do not turn product work into a framework rewrite. Make the smallest complete
change that produces observable Socratink behavior.

## Harness terminology

An agent is a capitalized exported function in a module beginning with
`'use agent'`. Flue hooks attach its model, tools, skills, state, and other
capabilities. The function's return value is its instruction.

Routing is explicit in `app.ts`: mount an HTTP-reachable agent with
`createAgentRouter`. Registration comes from the `'use agent'` scan, not from
mounting.

The model layer uses Pi's provider protocol through the inherited Flue runtime.

## Project structure

- `apps/socratink/` — Socratink chat app and web UI
- `packages/runtime/` — agent runtime, sessions, tools, and harness plumbing
- `packages/vite/` — Vite integration and generated server bootstraps
- `packages/cli/` — Flue command-line tooling
- `apps/www/` — inherited framework documentation
- `examples/` — inherited framework integration examples
- `demo/` — inherited standalone demonstration client

## Verification

For Socratink-only changes, run:

```sh
pnpm --dir apps/socratink check:types
pnpm --dir apps/socratink build
```

Use broader workspace checks only when shared framework packages change.
