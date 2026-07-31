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
