# Socratink product

This repository owns the standalone Socratink product. It uses published Flue
packages as its agent harness.

## Ownership

- `src/` owns the Socratink application and learner-facing interface.
- Flue framework behavior comes from exact published `@flue/*` dependencies;
  framework source is not vendored here.
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

The model layer uses Pi's provider protocol through the published Flue runtime.

## Project structure

- `src/agents/` — Socratink agents
- `src/server/` — runtime provider configuration
- `src/ui/` — learner-facing web UI
- `src/app.ts` — HTTP routes and static UI delivery

## Verification

```sh
pnpm check:types
pnpm build
```

## Maintainability

Follow the maintainability principles in [ZEN.md](ZEN.md).
