# Teaching Skill Contract

Status: In development for Wayfinder issue #8. The foundational epistemic-labor boundary is founder-approved.

This contract defines the governed instructional procedures that one learner-owned Learner Agent may use to select, conduct, evaluate, and adapt learning activity without confusing agent assistance with learner capability.

Its pedagogical basis is documented in [`../research/teaching-skills-evidence.md`](../research/teaching-skills-evidence.md) and [`../research/teaching-skill-epistemic-labor.md`](../research/teaching-skill-epistemic-labor.md). Learning Targets and route selection remain governed by [`learning-map-contract.md`](learning-map-contract.md). Learner claims and Evidence Records remain governed by [`learner-state-contract.md`](learner-state-contract.md). Persona influence remains governed by [`persona-package-contract.md`](persona-package-contract.md).

## Teaching Skill identity

A Teaching Skill is:

> A versioned instructional procedure that declares how the Learner Agent will elicit, support, observe, evaluate, and adapt learner work for a specified class of Learning Targets and learner conditions.

A Teaching Skill is not a Persona, Model, prompt fragment, content format, motivational style, or claim that one pedagogy is universally best. It is a governed procedure executed by the Agent Harness under the Learning Constitution.

## Foundational epistemic-labor boundary

Every Teaching Skill must declare a versioned `AssistanceAndSolutionRevelationPolicy`.

The policy must preserve learner-generated retrieval, explanation, decision, construction, debugging, comparison, verification, and problem solving when those actions are part of the active Learning Target. It may allow direct instruction, worked examples, hints, partial representations, co-solving, tool use, and full solution revelation when the learner's readiness, the target, accessibility, safety, cognitive load, affect, time, or instructional design justify them.

Assistance is legitimate, but it changes what performance demonstrates. Agent-performed or agent-revealed work remains explicit Agent Action or assistance provenance. It cannot be credited as independent learner capability merely because the learner saw it, agreed with it, repeated it, or completed the assisted task.

A decisive reveal changes what the current task can still measure. It must be recorded, followed by an appropriate learner action, and excluded from independent-capability inference for that task. When independence matters, the Learner Agent must obtain fresh evidence from a sufficiently novel, appropriately delayed task under reduced or declared assistance.

## Adaptive guidance, not ritualized struggle

No universal rule may:

- require an unaided attempt before all instruction or help;
- forbid worked examples or full solutions;
- treat persistence, time spent, frustration, or repeated failure as learning;
- force discovery when the learner lacks a meaningful foothold;
- continue struggle after accessibility, safety, prerequisite, cognitive-load, affective, or learner-stop conditions invalidate it.

Attempt-before-help is a conditional instructional choice. It is often appropriate for retrieval, diagnosis, self-explanation, application, path generation, and transfer when the learner has enough prior knowledge to make the attempt meaningful. Example-first or more direct guidance may be preferable for novice schema construction, high-element-interactivity material, inaccessible modalities, safety-critical activity, severe frustration, or missing prerequisites.

Productive struggle must be designed, bounded, and followed by feedback or consolidation. The goal is not to maximize difficulty. It is to protect the cognitive work relevant to the target while preventing avoidable overload, hidden delegation, and repeated error rehearsal.

## Minimum assistance-policy obligations

The versioned policy must declare at minimum:

- the epistemic actions reserved for the learner and the actions the agent may perform;
- readiness and prerequisite conditions;
- whether an attempt is required, preferred, conditional, optional, or not applicable;
- what constitutes a meaningful attempt and which bypass conditions apply;
- struggle budgets, error limits, stop conditions, and learner override behavior;
- assistance tiers and the observable rules for increasing or fading support;
- what counts as decisive information or solution revelation;
- required learner work after assistance or revelation;
- feedback purpose, content, timing, and required next action;
- accessibility and modality adaptations;
- independent-verification conditions, including novelty, delay, assistance, and evidence scope;
- the Attempts, assistance events, reveal events, Agent Actions, and Evidence Records that must be preserved;
- policy identity, version, provenance, evidence basis, and validation status.

Numeric thresholds are not universal doctrine. A Teaching Skill must justify and version task-specific thresholds, and the Learner Agent must preserve the evidence required to evaluate and revise them.

## Required Teaching Context input

A Teaching Skill must not execute from a raw prompt, transcript fragment, Persona preference, or model-inferred context alone. The Agent Harness must provide a validated, versioned `TeachingContext` envelope.

The envelope must identify at minimum:

- the active Learning Target, its Evidence Contract, the interpreted Learning Goal, and the active Map Revision;
- the intended evidence claim and whether the interaction is in learning, execution, or hybrid mode;
- relevant Learner Target Interpretations, Capability Interpretations, Attempts, Evidence Records, uncertainty, counterevidence, prerequisite state, and prior assistance history;
- modality, accessibility requirements, permitted accommodations, allowed Tools, environment, time constraints, and stakes;
- relevant Source Claims, Knowledge Components, ontology references, and provenance when they inform the target or task;
- the selected Teaching Skill and assistance-policy versions;
- active Persona Package, Model, Tool, rubric, evaluator, and task-generator versions when they may affect execution or interpretation;
- learner help preferences, consent or permission conditions, and pause, override, and stop controls;
- context-envelope identity, creation time, provenance, and validation status.

The envelope is a bounded snapshot for one instructional decision or declared sequence. Durable learner state remains canonical outside the skill. A Teaching Skill may consume the envelope and propose actions or records, but it cannot silently mutate the envelope, learner state, Learning Map, or Evidence Contract.

Unknown, unavailable, disputed, stale, and not-applicable values must remain distinct and explicit. The Model must not fill missing canonical inputs by conversational inference and then treat those guesses as state.

Before execution, the Agent Harness must validate that the context is sufficient for the proposed instructional act. If the Learning Target, Evidence Contract, interaction mode, required permissions, or construct-relevant accessibility conditions cannot be established, the skill must clarify, diagnose, propose a bounded context revision, choose a non-evidentiary exploratory action, or reroute. It must not silently guess and proceed as though the missing condition were known.

Persona preferences and learner preferences are advisory inputs within this envelope. They may influence presentation, examples, modality, assistance, and selection among valid procedures. They cannot alter the target, invent evidence, widen an evidence claim, or bypass constitutional and policy boundaries.

## Typed result and durable-write boundary

A Teaching Skill must return a versioned `TeachingSkillResult`. It must not directly mutate durable learner state, the active Learning Map, the Knowledge Ontology, Source records, permissions, Persona Relationship State, or any other canonical object.

A result must declare one terminal or continuation status, such as:

- `plan_ready`;
- `action_ready`;
- `awaiting_learner_work`;
- `clarification_required`;
- `reroute_proposed`;
- `paused`;
- `stopped`;
- `completed`;
- `failed`.

As applicable, the typed result may contain:

- a `TeachingPlan` that identifies the target, instructional rationale, sequence, assistance policy, evidence intention, adaptation points, and exit conditions;
- one or more proposed Learning Tasks, each with expected learner work, modality, allowed Tools, conditions, rubric, evaluator reference, and evidence eligibility;
- proposed Instructional Actions such as explaining, questioning, demonstrating, prompting, hinting, comparing, modeling, or giving feedback;
- preserved learner artifacts and observation references without silently rewriting the learner's work;
- proposed Assistance Events, `SolutionRevealEvent` records, feedback events, and Agent Actions;
- a proposed evaluation with rubric results, interpretation, uncertainty, counterevidence, and maximum claim scope;
- a proposed Evidence Record that references the exact target, task, learner artifact, conditions, assistance history, evaluator, and interpretation rule;
- proposed Next Learning Actions, clarification questions, context corrections, reroutes, pauses, or stops;
- result identity, status, versions, provenance, execution trace, validation findings, warnings, and errors.

A `TeachingPlan` describes an intended instructional sequence. A Learning Task defines an evidence-eliciting activity and expected learner work. An Instructional Action is one agent act within a plan or task. An observation preserves what occurred. An evaluation proposes how observed learner work should be interpreted. These objects must remain distinguishable even when one interaction produces several of them.

The Agent Harness owns the durable-write gate. It must validate each proposed object against the active `TeachingContext`, schema, permissions, constitutional rules, target and map versions, assistance policy, and evidence contract before committing it. Validation may accept, reject, narrow, quarantine, or return a proposal for correction. Rejection must preserve a reason and must not silently convert the proposal into canonical state.

A proposed Evidence Record is not durable learner evidence until the Agent Harness confirms at minimum:

- the target and Evidence Contract versions;
- the preserved learner work product and observation provenance;
- modality, environment, allowed Tools, and relevant accommodations;
- assistance source, timing, amount, adaptivity, and every decisive reveal;
- the evaluator and interpretation-rule versions;
- uncertainty, counterevidence, intended use, and maximum claim scope;
- that the proposal does not credit Agent Actions as learner work.

The durable-write gate may store raw learner work and append-only execution events before final evaluation when required for continuity or recovery. Such storage remains observation data, not a learner claim. Only a validated Evidence Record may update a Learner Target Interpretation or Capability Interpretation under the learner-state contract.

## Non-negotiable failure boundaries

The system must reject or surface any Teaching Skill that:

- executes without a validated, versioned `TeachingContext` or silently replaces missing canonical inputs with model inference;
- returns untyped output, directly mutates canonical state, or bypasses the Agent Harness durable-write gate;
- treats its own evaluation or Evidence Record proposal as accepted evidence without independent harness validation;
- lacks a versioned `AssistanceAndSolutionRevelationPolicy`;
- hides agent work or decisive assistance inside conversational style;
- treats exposure, agreement, copying, completion, or assisted success as independent capability;
- reveals decisive information without recording its effect on evidence validity;
- continues identical retries after its declared error or struggle boundary;
- treats accessibility accommodation as lower capability when the accommodation is not part of the target construct;
- permits a Persona, Model, Tool, or learner preference to bypass constitutional evidence boundaries;
- cannot identify what cognitive work the learner and agent each performed;
- cannot provide a fresh verification path when it claims movement toward independence.

## Minimum foundational claim

A conforming Teaching Skill may adapt how much help the learner receives. It may not adapt away epistemic honesty about who performed the work or what the resulting evidence can prove.
