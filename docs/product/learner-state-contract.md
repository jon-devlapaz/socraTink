# Learner State Ownership and Continuity Contract

Status: Accepted baseline for Wayfinder issue #7.

This contract defines the minimum durable-state guarantees that make one Learner Agent continuous across changing models, harnesses, tools, skills, personas, and service deployments.

## Ownership

The learner owns every durable record required to reconstruct the continuity of their Learner Agent. Socratink is a custodian of that state, not its owner.

Learner-owned state includes:

- learner identity and declared preferences;
- Learning Goals and Goal Interpretations;
- authorized Source manifests and provenance;
- Knowledge Ontology additions and goal-scoped Learning Maps;
- Learning Tasks, Attempts, Evidence Records, and Capability interpretations;
- permissions, overrides, corrections, and consent history;
- installed skill and persona manifests;
- Persona Relationship State;
- version, audit, and migration history required to explain how current state arose.

Learner ownership does not transfer ownership of model weights, platform code, shared packages, or source payloads that cannot legally be redistributed. When a payload cannot be exported, its stable identity, authorization status, provenance, and any portability limitation must remain explicit in the export.

## Evidence mutation

Learner claims may change only through Evidence Records. Declared Learning Tasks are the default mechanism for producing Attempts and durable evidence, but a separate pre-authored task interface is not scientifically required.

A bounded segment of conversation, speech, tool use, or process data may become opportunistic evidence only when it is promoted into a task-equivalent Evidence Record before any learner claim changes. The record must identify:

- the versioned Learning Target or Capability being informed;
- the preserved learner work product and observation provenance;
- modality and relevant environmental conditions;
- allowed tools, assistance source, timing, amount, and adaptivity;
- the interpretation or scoring rule and its assumptions;
- uncertainty, counterevidence, and maximum claim scope;
- the intended use and consequence of the update.

Raw chat, content exposure, time-on-task, model agreement, agent work, or tool output remains context or a hypothesis when this contract cannot be satisfied. Assisted performance is evidence of performance under the recorded assistance conditions, not independent capability. Spoken performance is valid evidence when its modality and construct-irrelevant threats are represented explicitly.

This rule follows the assessment-triangle separation of cognition, observation, and interpretation and the evidence-centered-design requirement that claims, work products, conditions, and inference rules form a coherent validity argument. See [`../research/learner-evidence-mutation-validity.md`](../research/learner-evidence-mutation-validity.md).

## Inspection and correction

The learner may inspect all durable learner-owned state in a human-readable form, including the evidence trail, provenance, conditions, uncertainty, and interpretation rule supporting every current learner claim.

The learner may directly correct declared facts, preferences, permissions, and Source metadata. They may challenge an Evidence Record or Capability interpretation, attach context or counterevidence, mark it disputed, or exclude it from future inference.

Historical Attempts and prior interpretations are not silently overwritten. Corrections are appended and versioned, preserve what changed and why, and trigger recomputation of every affected current claim. The interface must distinguish the original observation, the agent's interpretation, the learner's correction, and the current operative state.

## Deletion and forgetting

Learner ownership includes permanent deletion of learner-owned state. The learner may delete raw artifacts, conversations, audio, Attempts, Evidence Records, Persona Relationship State, Learning Projects, or the complete account.

Deletion removes the selected content from active and recoverable product storage and triggers recomputation or removal of every dependent current claim. It must not be implemented as merely hiding data from the learner-facing interface.

Socratink may retain only non-reconstructive deletion tombstones and narrowly required legal, billing, abuse-prevention, or security records. Every exception must disclose its purpose, scope, and retention period and must not preserve the deleted learning content or permit reconstruction of it.

## Export and import

The learner may obtain a complete, self-describing, versioned export of the durable state required to reconstruct Learner Agent continuity. The export contains:

- canonical learner state and stable identifiers;
- raw learner work and Source payloads where legally exportable;
- provenance, content hashes, and schema versions;
- Learning Projects, maps, Attempts, Evidence Records, corrections, disputes, deletions, and current derived claims;
- installed Thinking Skill, Teaching Skill, Tool, and Persona Package manifests;
- Persona Relationship State, preferences, permissions, and consent history;
- migration and audit history required to explain current state;
- explicit declarations for every omitted, externally referenced, or legally non-exportable payload.

Exports exclude platform credentials, service secrets, proprietary model weights, and shared package payloads the learner does not own. Their stable identities and compatibility requirements remain represented where continuity depends on them.

Import into a compatible Socratink runtime must reconstruct the same Learner Agent identity, projects, preserved evidence history, current claims, permissions, and persona relationships. Portability guarantees data continuity and verifiable omissions. It does not yet promise that the export can execute in every third-party harness or recreate identical model behavior.

## Model-swap continuity

A model swap is a read-path change by default. It cannot mutate, reinterpret, migrate, or recompute canonical Learner Agent State merely because a different Model is selected.

The Model receives a projected view of state and may propose actions, but it does not write directly to canonical state. Every durable write passes through typed, inspectable state-transition interfaces that enforce evidence, permission, constitutional, versioning, and audit contracts.

At the moment of a swap, these remain invariant:

- Learner Agent identity and stable identifiers;
- Learning Projects, Goals, Sources, Ontology, Maps, and revisions;
- Attempts, Evidence Records, corrections, disputes, and current claims;
- permissions, preferences, installed-package manifests, and consent history;
- Persona Relationship State and its ownership boundaries;
- provenance, audit, and migration history.

Ephemeral context projections, caches, embeddings, and model-specific summaries may be rebuilt or discarded. They must be tagged as derived runtime artifacts and cannot serve as the sole source of canonical continuity.

A model may produce different language, reasoning traces, or Next Learning Action proposals. The contract preserves identity, truth, evidence, and governance, not identical model behavior. Any required schema or state migration is a separate, versioned, reversible operation with an inspectable diff and cannot be hidden inside the model swap.

### Minimum model-swap proof

1. Hash or otherwise fingerprint a representative canonical-state fixture.
2. Run Model A, switch to Model B, and switch back.
3. Verify that swapping alone never changes the canonical fingerprint.
4. Verify that both Models can read the same projects, provenance, evidence, permissions, and persona relationships.
5. Compare their proposed Next Learning Actions without requiring identical outputs.
6. Verify that only a separately valid learner, evidence, permission, or migration event can cross the durable write gate.
7. Delete and rebuild all model-specific caches and projections without losing continuity.

## Persona-switch continuity

Switching the Active Persona may change voice, framing, motivational approach, and proposed teaching behavior. The switch itself cannot mutate the Knowledge Ontology, Learner Evidence Model, Capability claims, permissions, or any Persona Relationship State.

Each Persona Relationship State remains a separate learner-owned record associated with its Persona Package. One persona cannot read or inherit another persona's relationship state by default. Cross-persona memory sharing requires an explicit learner grant that identifies the shared fields, purpose, recipients, and duration and remains inspectable and revocable.

Persona Packages and Active Personas remain subordinate to the Learning Constitution and the same evidence and durable-write gates as every other runtime component.

## Cross-project evidence

Evidence Records are canonical learner-level objects. They retain their original Learning Targets, conditions, provenance, and Learning Project context and are not copied into another project as independent evidence.

Another Learning Project may reference an existing Evidence Record and propose a new, bounded interpretation of its relevance. It cannot rewrite the record, detach it from its origin, or silently treat success in one context as universal transfer. Broader Capability claims require evidence across relevant targets, tasks, contexts, modalities, or times.

## State-transition acceptance matrix

| Transition | Required authority or observation | Canonical effect |
| --- | --- | --- |
| Change a Goal, preference, permission, or relationship convention | Explicit learner action or previously granted scoped authority | Append a versioned state change; do not create learner evidence |
| Add a Source | Learner authorization | Preserve the Source and provenance; propose rather than silently activate material Map changes |
| Activate a material Map Revision | Learner confirmation | Version the Learning Map; preserve earlier versions and evidence links |
| Create an Attempt | Observable learner work with preserved conditions | Append an observation; do not directly create a Capability claim |
| Create an Evidence Record | Valid evidence contract connecting observation to a target and use | Append bounded support, counterevidence, or unresolved evidence |
| Change a current Capability interpretation | Recompute from eligible Evidence Records under a versioned inference rule | Preserve prior interpretation and make the new basis inspectable |
| Correct or dispute state | Learner correction, challenge, or counterevidence | Append the correction and recompute affected current state |
| Delete learner-owned state | Explicit learner deletion request | Permanently remove selected content and recompute dependents, subject only to disclosed narrow retention exceptions |
| Swap a Model, harness, Tool, Skill, or Active Persona | Runtime configuration change | No canonical state mutation from the swap alone |
| Migrate canonical schema or state | Explicit versioned migration with rationale, diff, validation, and rollback treatment | Preserve auditability and never hide migration inside a runtime swap |
| Reuse evidence across projects | Reference the original Evidence Record with a bounded relevance interpretation | Do not duplicate, rewrite, or infer universal transfer |

## Minimum continuity claim

Socratink may claim that Learner Agent continuity is real only when export/import reconstruction, model-swap invariance, deletion, correction, evidence-gated mutation, and cross-project reference behavior pass executable acceptance tests against representative state fixtures. Until then, continuity is a product hypothesis rather than an established capability.
