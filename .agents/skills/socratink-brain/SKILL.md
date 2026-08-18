---
name: socratink-brain
description: >
  Interface safely with the Socratink Brain from the Socratink application repo:
  orient ontology to the live codebase, retrieve task-scoped canon, trace
  provenance, reconcile new evidence, and validate the vault. Use when implementing
  product/learning behavior, learner evidence, Teaching Skills, experiments, R1,
  or any task that depends on Socratink doctrine rather than software-maintenance
  docs alone.
version: 1.0.0
---

# Socratink Brain Interface

Use this skill when a task depends on Socratink's product doctrine, learning science,
learner-agent architecture, current experiments, founder decisions, or historical
rationale.

The Brain is a **governed knowledge system**, not a folder of interchangeable notes.

## Core rule

> Read by authority, write by permission, and never strengthen a claim beyond its evidence.

The default mode is **read + propose**. Do not mutate governing doctrine merely because
a task would be easier if the doctrine changed.

## Coding-agent default

For product or learning work in the Socratink application repository:

1. Run `python .agents/skills/socratink-brain/scripts/brain.py orient`.
2. Read every existing `read_now` path from `brain_root`.
3. If `tandem` is `mismatch`, say so; do not assume `CURRENT STATE.md` describes this checkout.
4. Run `context "<task>"`, then `show` only the linked IDs required to decide.
5. Fill a Brain Contract before writing code.
6. Do not ingest the whole vault. Do not reconstruct doctrine from this repo's software docs.

Helper commands:

```bash
python .agents/skills/socratink-brain/scripts/brain.py orient
python .agents/skills/socratink-brain/scripts/brain.py context "learner evidence"
python .agents/skills/socratink-brain/scripts/brain.py show EVD-0004
python .agents/skills/socratink-brain/scripts/brain.py validate
```

The helper is lexical discovery only. It does not determine truth or authority.

## Find the Brain

Resolve `BRAIN_ROOT` in this order:

1. explicit path from the user/task;
2. `SOCRATINK_BRAIN_PATH` (local environment only; never commit a machine-specific path);
3. current directory if it contains `CONSTITUTION.md`, `NORTH-STAR.md`, and `CURRENT STATE.md`;
4. a nearby sibling checkout named `socratink-brain`, discovered from the working
   directory, this skill's location, or the Socratink git toplevel.

If the Brain cannot be located, report that clearly. Do not reconstruct doctrine from
memory or old app docs.

The bundled helper is optional:

```bash
python .agents/skills/socratink-brain/scripts/brain.py locate
```

Pass `--brain` with a local path when discovery is ambiguous. Do not commit that path.

## Authority stack

Always interpret the Brain in this order:

1. `CONSTITUTION.md` — invariants.
2. `NORTH-STAR.md` — slowly changing strategic direction.
3. `20 Canon/` — atomic current beliefs, policies, constructs, decisions, outcomes.
4. `CURRENT STATE.md` — what is actually implemented, validated, and active now.
5. `50 Active/` — current milestone, bets, experiments, risks, open questions.
6. `40 Views/` — derived synthesis for humans and agents.
7. `30 Procedures/` — safe operating/change/evaluation procedures.
8. `10 Sources/` — provenance and history; never current truth by default.
9. `90 Archive/` — superseded/rejected canonical material.

When two items conflict, the higher authority governs unless a later accepted canonical
decision explicitly supersedes it.

A polished historical document does not outrank current Canon.

## Default context algorithm

Do **not** ingest the whole vault.

For every task:

1. Read `CONSTITUTION.md`.
2. Read `NORTH-STAR.md`.
3. Read `CURRENT STATE.md`.
4. Identify the task's:
   - outcome;
   - authority;
   - constraints;
   - proof/acceptance boundary.
5. Read only relevant `50 Active/` notes.
6. Read the smallest relevant `40 Views/`.
7. Follow wikilinks/IDs into only the `20 Canon/` objects required to decide or implement.
8. Read the relevant `30 Procedures/`.
9. Open `10 Sources/` only when provenance, contradiction, rationale, or source validation
   is material to the task.

Use `orient` first, then `context` / `show` for the task-specific remainder.

## Canonical object vocabulary

| Prefix | Meaning |
|---|---|
| `SRC-` | source / provenance record |
| `CLM-` | atomic empirical or conceptual claim |
| `MEC-` | causal/explanatory mechanism — why an effect may occur |
| `EVD-` | evidence definition or evidence rule |
| `LST-` | learner-state construct |
| `INT-` | pedagogical intervention / Teaching Skill |
| `POL-` | policy governing eligibility, sequencing, fading, or scheduling |
| `CAP-` | product/software capability |
| `OUT-` | outcome / success criterion |
| `BET-` | product, market, or business hypothesis worth investing in |
| `EXP-` | experiment |
| `DEC-` | accepted decision / governing principle |
| `PROC-` | repeatable operating/change procedure |

Do not invent a new type because a new noun appears. Prefer a property or link unless
the concept needs independent authority and lifecycle.

## Truth boundaries

Never collapse these:

```text
source support
    ≠
domain model
    ≠
learner evidence
    ≠
learner-state inference
    ≠
product claim
```

Also preserve:

```text
AI output quality ≠ learning quality
assisted success ≠ independent capability
exposure ≠ learner evidence
immediate performance ≠ durable learning
engagement ≠ learning
```

For learning research:

- `CLM-*` = what evidence supports;
- `MEC-*` = why an effect might occur;
- `INT-*` = what Socratink does;
- `POL-*` = when/how the intervention is used;
- `OUT-*` = what learner change is measured.

Do not use `MEC` as a synonym for a named learning effect.

## Operating modes

### A. Orient

Use when the agent needs to understand Socratink before planning.

Output:

- current North Star;
- current implementation boundary;
- active milestone/experiment;
- relevant governing Canon;
- material uncertainty.

Do not propose architecture until orientation is complete.

### B. Answer / explain

Use the smallest context that supports the answer.

Distinguish:

- **accepted doctrine**;
- **candidate hypothesis**;
- **historical rationale**;
- **current implementation**;
- **your inference**.

If the answer depends on historical evidence, cite the relevant `SRC-*` or source path.

### C. Plan or implement product work

Before code, create an internal **Brain Contract**:

```text
North-star fit:
Current-state boundary:
Canon relied on:
Active bet/experiment:
Procedure:
Evidence/proof obligation:
Claims this work must NOT make:
```

A feature that conflicts with Canon is not an ordinary implementation task.

If the feature is intended to test a contrary hypothesis, keep the variance inside an
explicit `EXP-*` rather than silently rewriting Canon.

### D. Ingest / reconcile new knowledge

Follow `PROC-0001 Rolling knowledge consolidation`.

At minimum:

1. preserve provenance;
2. inventory the blob;
3. extract atomic candidate items;
4. compare each item with existing Canon;
5. classify it as:
   - new;
   - reinforces;
   - refines;
   - contradicts;
   - supersedes;
   - historical only;
6. do not bulk-promote;
7. preserve conflicts and negative evidence;
8. update affected views only after Canon reconciliation;
9. append a consolidation receipt / ledger entry.

### E. Maintain current execution state

Direct updates to `CURRENT STATE.md` or `50 Active/` are allowed only when:

- the task explicitly changes current implementation/experiment state;
- the change is supported by observable repo or experiment evidence;
- the update does not silently change North Star or Canon.

State what evidence changed the current-state view.

### F. Change Canon

Default: **propose, do not silently accept**.

A Canon mutation must:

1. name the object(s) affected;
2. show supporting evidence/source;
3. state whether the change creates, refines, contests, supersedes, or rejects;
4. preserve the old object's history;
5. state what the new object does **not** establish;
6. update affected links/views;
7. run validation;
8. show the diff.

Agents may create `candidate` objects when explicitly asked to curate the Brain.

Changing an item to `accepted`, `contested`, `superseded`, or `rejected` requires either:

- explicit user/founder authorization in the task; or
- a previously accepted governance procedure that clearly delegates that authority.

When uncertain, leave the proposal as `candidate`.

### G. Change `NORTH-STAR.md` or `CONSTITUTION.md`

These are founder-governed.

Do not edit them as part of normal feature work, research ingestion, refactoring, or
cleanup.

If evidence suggests a change:

1. explain the conflict;
2. propose the exact strategic diff;
3. identify downstream Canon/experiment implications;
4. wait for explicit authorization before applying it.

## Write permissions

Use this matrix unless the user explicitly grants broader authority.

| Area | Default agent authority |
|---|---|
| `10 Sources/` | append provenance; do not rewrite source meaning |
| `20 Canon/` | read; propose; create `candidate` only when asked |
| `30 Procedures/` | propose; update after a repeated/proven operating pattern |
| `40 Views/` | update derived synthesis when underlying authority is unchanged |
| `50 Active/` | update when current execution evidence changed |
| `60 Ledger/` | append reconciliation/change receipts |
| `90 Archive/` | do not move items here without explicit supersession/rejection |
| `CURRENT STATE.md` | update from current evidence |
| `NORTH-STAR.md` | founder approval required |
| `CONSTITUTION.md` | founder approval required |

## Canon write rules

When creating or modifying a canonical object:

- preserve a stable `id`;
- never reuse an old ID for a different idea;
- use allowed `status` values:
  - `candidate`
  - `accepted`
  - `contested`
  - `superseded`
  - `rejected`;
- keep `status` separate from `confidence`;
- link to sources and related Canon where possible;
- keep one atomic governing idea per object;
- add boundary conditions where applicable;
- add a **What this does not establish** section for consequential claims;
- preserve supersession explicitly;
- prefer links over copied explanations.

Do not silently convert a source summary into an accepted claim.

## Learner-agent-specific invariants

When touching learner-state, evidence, policy, or Teaching Skills:

1. learner-authored work remains distinguishable from model-authored work;
2. assistance/reveal provenance survives evidence-bearing attempts;
3. Evidence Contracts define what observations license which inferences;
4. policy may select an intervention but may not rewrite evidence;
5. learner-state updates link back to licensing evidence;
6. UI language may not strengthen the inference;
7. delayed-verification obligations are not equivalent to completed verification;
8. model/provider/persona changes may not erase evidence semantics;
9. persisted learner-visible state must support correction/deletion as required by product doctrine.

Read `40 Views/Agent/Learner Agent Contract.md` before material changes to these surfaces.

## Research ingestion rules

For research claims:

- prefer primary research and systematic/meta-analytic evidence where available;
- preserve contradictory findings and boundary conditions;
- distinguish empirical effect from proposed mechanism;
- do not turn one study into a universal policy;
- do not infer product superiority from mechanism evidence;
- do not infer durable learning from immediate task performance;
- label time-sensitive market evidence separately from learning science.

## Experiments

An experiment may test a hypothesis that is not Canon.

It must not use the experiment itself as proof before results exist.

Before execution, freeze material acceptance criteria where feasible:

- target;
- evidence contract;
- evaluator/rubric;
- treatment/intervention;
- comparison/baseline when causal claims are intended;
- failure cases;
- kill/stop conditions;
- claims the experiment cannot establish.

After execution, preserve adverse/inconclusive evidence.

## Validation before completion

When writing to the Brain:

```bash
python scripts/validate_brain.py
```

Also inspect the diff:

```bash
git diff --check
git status --short
git diff
```

If the vault is a Git repo and the task authorizes commits, make one atomic commit whose
message describes the knowledge change.

Never claim validation succeeded unless it actually ran.

## Required response contract

When the Brain materially informs a task, end the work with a compact report:

```text
Brain context used:
Authority:
Decision / change:
Evidence:
Uncertainty / non-claims:
Validation:
```

For implementation tasks, also include:

```text
Canon affected:
Experiment affected:
Brain update needed after code proof:
```

## Stop conditions

Stop and surface the conflict instead of improvising when:

- `CONSTITUTION` and requested behavior conflict;
- `NORTH-STAR` and requested product direction conflict;
- two accepted canonical objects materially contradict each other;
- a task requires a learner claim unsupported by the Evidence Contract;
- current implementation cannot be established;
- source provenance is missing for a consequential research claim;
- the requested Canon mutation exceeds delegated authority.

Do not resolve governance conflicts by averaging documents.

## Examples

### “Add voice learning”

Do not assume voice is canonical.

Read the current bet/experiment and determine whether voice improves observation,
intervention, verification, accessibility, continuity, or user value enough to justify
complexity. Treat it as a capability/experiment unless Canon says otherwise.

### “Mark this learner as mastered”

Do not create a universal mastery score by convenience.

Find the target's Evidence Contract and learner evidence. Produce only the bounded
state inference licensed by those conditions.

### “A new paper says retrieval is bad”

Do not rewrite retrieval policy from the abstract.

Add provenance, extract the atomic claim, inspect design/population/outcome/boundary
conditions, reconcile it against current retrieval claims, and mark conflict where
warranted.

### “Implement R1”

Read:

- `CONSTITUTION.md`
- `NORTH-STAR.md`
- `CURRENT STATE.md`
- `40 Views/Agent/Learner Agent Contract.md`
- `20 Canon/Evaluation/Experiments/EXP-0001 R1 evidence-bearing learning loop.md`
- linked Evidence/Policy/Intervention objects
- relevant agent/change procedures

Implement only the smallest complete slice needed to satisfy the frozen proof.
