# Goal-Scoped Learning Map Contract

Status: In progress for Wayfinder issue #6.

This contract defines how Socratink represents a learner's route through a Learning Goal without collapsing knowledge, source claims, learner evidence, or semantic similarity into one undifferentiated graph.

Its epistemic basis is documented in [`../research/learning-map-epistemology.md`](../research/learning-map-epistemology.md). Source identity, extraction, claims, and provenance remain governed by [`../research/source-ingestion-provenance.md`](../research/source-ingestion-provenance.md). Learner evidence remains governed by [`learner-state-contract.md`](learner-state-contract.md).

## Primary routing unit

The Learning Map is a goal-scoped, versioned route through **Learning Targets**. It is not the general Knowledge Ontology and it does not store learner mastery.

A Learning Target is:

> A versioned, goal-scoped, evidence-evaluable claim that the learner can perform a stated action on specified knowledge under stated conditions.

Learning Targets are the primary routable map nodes because they can connect all four requirements of an adaptive learning decision:

- the learner's interpreted goal;
- the knowledge and prerequisite hypotheses relevant to that goal;
- an action or task capable of eliciting observable learner work;
- an interpretation rule describing what that work may demonstrate.

A routable Learning Target must identify at minimum:

- a stable target ID and target version;
- the Learning Map and Goal Interpretation that give it scope;
- a learner-performable statement and action verb;
- references to relevant Concepts or Knowledge Components;
- performance conditions, including modality, allowed tools, assistance, and context;
- an Evidence Contract or rubric capable of interpreting an Attempt;
- supporting Source Claims, warrants, or standards where available;
- lifecycle status and provenance.

## Referenced epistemic layers

The following objects inform and justify routing but are not peer route nodes:

- **Concepts and Knowledge Components** belong to the Knowledge Ontology. They describe domain meaning and hypothesized cognitive structure.
- **Source Claims and Argument or Warrant records** belong to the knowledge and provenance layers. They preserve what a source or transformation asserts, why it may be trusted, and where it may conflict.
- **Attempts, Evidence Records, Learner Target Interpretations, and Capability Interpretations** belong to the Learner Evidence overlay. They describe what the learner did and the bounded conclusions currently supported by that work.
- **Chunks, embeddings, vector indexes, summaries, and model-specific representations** are disposable projections. They may retrieve or propose candidates but cannot establish canonical identity, truth, prerequisite structure, target equivalence, mastery, or route order.

The Learning Map references these objects by stable ID and version. It does not copy them into a flattened graph or silently reinterpret them.

## Container and presentation objects

A `LearningMap` is the versioned route container for one Goal Interpretation. A `MapRevision` is a proposed, inspectable change to that route. Target clusters, modules, and milestones may organize or present Learning Targets, but they are not atomic evidence units and are not routable by default.

## Typed route edges

Learning Map edges must have explicit routing semantics. A generic relationship, source ordering, concept hierarchy, semantic similarity score, or generated association cannot silently become a route constraint.

The initial target-to-target edge vocabulary includes:

- **`requiresTarget`**: the source target should normally be demonstrated before the destination target under this Goal Interpretation. This is the only edge type that may act as a hard progression gate.
- **`supportsTarget`**: the source target is expected to help performance on the destination target but is not necessary. It may affect recommendation weight but cannot block progression.
- **`subtargetOf`**: the source target decomposes or refines a broader destination target. This expresses target structure, not prerequisite order. Completing one child does not imply completion of its parent.

Every proposed `requiresTarget` edge must remain an inspectable, versioned map hypothesis with rationale, provenance, confidence, and scope. It cannot be inferred as canonical merely because:

- two targets, concepts, or source passages are semantically similar;
- one item appears earlier in a source or curriculum;
- one Knowledge Component is broader, narrower, or related to another;
- an embedding, language model, persona, or extraction pipeline proposes the relationship;
- the learner has completed a neighboring or supporting target.

Non-gating route relationships may influence explanation, candidate generation, and recommendation ranking. They must never be interpreted as unmet prerequisites.

## Prerequisite cycle policy

The active `requiresTarget` projection for one Learning Map revision and Goal Interpretation must be a directed acyclic graph. This is a narrow executable routing invariant, not a claim that knowledge, cognition, or learning is inherently acyclic.

A strict `requiresTarget(A, B)` edge means that B is ineligible until A satisfies the declared prerequisite condition. Reciprocal or longer hard-gate cycles provide no valid route entry point, so a revision containing one cannot be activated.

Every proposed Map Revision must run a topological validation over its active hard-gate projection. When validation finds a cycle, it must:

- reject activation of the revision;
- return an intelligible trace containing the involved targets and edges;
- preserve the provenance, rationale, confidence, and scope of every disputed edge;
- require an explicit revision rather than selecting an arbitrary order.

The revision may resolve the cycle by:

1. downgrading an overstated `requiresTarget` edge to `supportsTarget`;
2. splitting or refining a target whose bundled performance created the cycle;
3. narrowing an edge to the context, modality, task, source, or Goal Interpretation where it applies;
4. recording mutual development without internal hard ordering;
5. leaving the relationship unresolved and using exploratory tasks rather than inventing a gate.

Knowledge Ontology, argument, association, support, transfer, and co-development structures may contain cycles according to their own typed semantics. Learners may revisit earlier targets, follow spiral teaching sequences, and strengthen earlier performance through later work without violating the routing invariant.

Hard gates should initially be rare, explainable, challengeable, and supported more strongly than soft recommendations. Acyclicity proves that a route is navigable. It does not prove that its prerequisite hypotheses are pedagogically correct.

Research basis: [`../research/learning-map-prerequisite-cycles.md`](../research/learning-map-prerequisite-cycles.md).

### Minimum cycle proof

1. Create a representative map with at least ten Learning Targets and a valid hard-gate route.
2. Add one reciprocal or multi-target `requiresTarget` cycle.
3. Verify that activation fails and identifies the complete cycle without changing the previous active revision.
4. Downgrade, split, or narrow one involved edge through an inspectable Map Revision.
5. Verify that the repaired revision passes topological validation and routing resumes.
6. Verify that equivalent cycles in non-gating typed structures do not fail this validator.

## Target equivalence

`equivalentTargetWithinGoal` is a strict, scoped map relation. Two Learning Targets may be treated as equivalent only within a named Goal Interpretation and Learning Map version when they require the same:

- learner action or performance;
- knowledge and construct scope;
- performance conditions, including modality, tools, assistance, and context;
- Evidence Contract and interpretation boundaries.

Equivalence does not assert global identity. The original target IDs, versions, provenance, source support, and evidence links remain distinct and inspectable. Changing the Goal Interpretation, conditions, Evidence Contract, or relevant target version invalidates the equivalence unless a new Map Revision re-establishes it.

The system must reject canonical equivalence based only on:

- similar wording, labels, or nearby concepts;
- embedding proximity, clustering, or model confidence;
- shared source passages or curriculum placement;
- overlapping but non-identical Knowledge Components;
- similar tasks whose assistance, modality, context, or scoring rules differ.

Embeddings and models may propose a `sameAsCandidate` for review. They cannot activate `equivalentTargetWithinGoal` directly.

Equivalence never merges or copies Evidence Records. Any use of evidence associated with one equivalent target must reference the original record and satisfy the learner-state evidence and transfer contracts.

## Alternative routes

Non-equivalent Learning Targets may provide legitimate alternative routes toward the same goal or milestone. They must be grouped in an explicit, versioned Alternative Set rather than mislabeled as equivalent.

Every Alternative Set must declare:

- its stable ID, map version, Goal Interpretation, rationale, and provenance;
- its member target IDs and versions;
- a completion rule such as `one-of`, `k-of-n`, or learner-selected branch;
- any conditions that restrict which alternatives are valid;
- whether later convergence targets or additional evidence are required;
- how a learner may inspect, override, or revisit the selected branch.

Satisfying an Alternative Set means only that its declared route obligation is complete. It does not:

- mark unattempted alternatives as achieved;
- create or copy Evidence Records for those alternatives;
- establish that the targets are equivalent;
- support a broader Capability Interpretation beyond the evidence actually collected.

The router may rank valid alternatives using goal fit, current evidence gaps, expected learning or information value, accessibility needs, learner preference, available tools, time, source requirements, and other declared constraints. The chosen branch and decisive factors must be explainable. The choice remains reversible unless an external requirement makes it irreversible and that requirement is disclosed before selection.

Changing membership, completion rules, constraints, or convergence requirements requires a Map Revision. Existing Attempts and Evidence Records remain attached to their original targets and versions.

## Transfer between targets

`transfersTo` is a conditional map hypothesis about the possible relevance of performance on one Learning Target to another. It is never an instruction to copy evidence or declare destination mastery.

Every transfer proposal must record:

- the source Learning Target, version, Evidence Record IDs, and original performance conditions;
- the destination Learning Target and version;
- relevant similarities and differences in construct, knowledge scope, modality, assistance, task type, context, and time;
- the transfer rationale and its provenance;
- uncertainty, counterevidence, and the maximum allowed effect on routing or interpretation;
- any learner correction, dispute, permission, or opt-out relevant to cross-project reuse.

Eligible source evidence may change recommendation weight, reduce unnecessary repetition, or justify a shorter destination verification task. It cannot by itself mark the destination target achieved. A durable destination Learner Target Interpretation requires destination-relevant evidence collected or validly promoted under the learner-state Evidence Record contract.

Cross-project transfer references the original Evidence Records and preserves their original project, target, conditions, and provenance. It does not duplicate or detach them from their origin. Changing a transfer hypothesis or its maximum effect requires an inspectable Map Revision and cannot rewrite the source evidence.

## Next Learning Action boundary

A Learning Target identifies what capability should be developed or tested. It does not by itself prescribe the complete interaction.

A Next Learning Action instantiates a route decision by combining:

1. a selected versioned Learning Target;
2. a Teaching Skill or instructional policy;
3. a task, prompt, tool, or interaction modality;
4. the expected evidence and interpretation conditions.

This separation allows the Learner Agent to change pedagogy, persona, modality, or model without changing the epistemic identity of the target.

## Non-negotiable failure boundaries

The system must reject or surface any proposal that:

- treats a nearby concept or embedding match as the next route step without a Learning Target;
- treats source agreement as learner capability;
- treats exposure, conversation, or model-generated work as learner evidence without the Evidence Record contract;
- marks a target achieved merely because one child target, example, or related concept was completed;
- allows a model, persona, vector index, or generated summary to become the sole canonical source of map structure;
- loses the versions and provenance required to explain why a target exists or was selected.

## Decisions still to resolve

Wayfinder issue #6 will additionally define:

- typed target-to-target and target-to-reference edge semantics;
- prerequisite, cycle, equivalence, decomposition, alternative-path, and transfer policies;
- provenance, confidence, conflict, and uncertainty requirements;
- map revision, correction, and learner-confirmation paths;
- canonical routing queries and their failure behavior;
- an executable acceptance matrix for the contract.
