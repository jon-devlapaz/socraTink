# Teaching Skill Contract

Status: Accepted baseline for Wayfinder issue #8.

This contract defines the governed instructional procedures that one learner-owned Learner Agent may use to select, conduct, evaluate, and adapt learning activity without confusing agent assistance with learner capability.

Its pedagogical and architectural basis is documented in [`../research/teaching-skills-evidence.md`](../research/teaching-skills-evidence.md), [`../research/teaching-skill-epistemic-labor.md`](../research/teaching-skill-epistemic-labor.md), [`../research/teaching-skill-evaluator-system-design.md`](../research/teaching-skill-evaluator-system-design.md), and [`../research/teaching-skill-voice-system-design.md`](../research/teaching-skill-voice-system-design.md). Learning Targets and route selection remain governed by [`learning-map-contract.md`](learning-map-contract.md). Learner claims and Evidence Records remain governed by [`learner-state-contract.md`](learner-state-contract.md). Persona influence and Voice Package authority remain governed by [`persona-package-contract.md`](persona-package-contract.md).

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

## Interaction mode and cognitive-labor declaration

Every `TeachingContext` and proposed Learning Task must declare one interaction mode and the exact division of cognitive labor:

| Mode | Primary purpose | Evidence consequence |
| --- | --- | --- |
| `learning` | Develop or test learner capability. Target-relevant epistemic actions remain reserved for the learner except where declared assistance is instructionally justified. | Evidence is bounded by every Agent Action, Tool use, assistance event, and reveal. Independent capability requires fresh qualifying learner work. |
| `execution` | Accomplish an external task using agent capability. | Agent-produced work may be useful output, but it is not learner-capability evidence. Review, agreement, or delivery does not change that status. |
| `hybrid` | Divide a real task between learner and agent while developing selected capabilities. | Only the explicitly learner-reserved and observed work may support a learner claim. The task must state the claim ceiling created by the division. |

The declaration must identify which retrieval, explanation, decision, construction, debugging, comparison, verification, and problem-solving actions belong to the learner; which the agent may perform; what Tools may do; and which outputs require learner inspection or transformation. A conversational phrase such as “we built this” cannot replace that attribution.

A mode change is an explicit, append-preserved event. If a learner asks the agent to perform work that was reserved for the learner, the Harness must either refuse within the current task, record an allowed assistance or reveal event and narrow the claim, or close the evidence-eligible task and continue in execution or hybrid mode. It must not retroactively relabel delegated work as learner work.

When AI output is used inside learning or hybrid mode, the Teaching Skill should require construct-relevant critical engagement where appropriate. This may include prediction before output, questioning assumptions, locating evidence, editing or annotating the output, testing it against observable consequences, comparing alternatives, explaining discrepancies, or revising a learner-authored artifact. These actions are instructional procedures, not automatic proof of understanding.

The Teaching Skill must preserve a route to fresh performance under reduced or declared assistance whenever it claims movement toward independence. The appropriate delay, novelty, modality, Tools, and assistance conditions remain governed by the Evidence Contract and `AssistanceAndSolutionRevelationPolicy`.

## Teaching Skill selection authority

Teaching Skill selection is a governed decision by the Agent Harness, not an unconstrained Model choice, Persona preference, engagement optimization, or fixed learner-type assignment. Selection proceeds in three ordered stages: deterministic eligibility, evidence-informed ranking, and learner choice among eligible procedures.

### Deterministic eligibility

The Harness must first exclude every Teaching Skill version that cannot validly execute for the current `TeachingContext`. Eligibility must check at minimum:

- active Learning Target, Evidence Contract, Learning Goal, and Map Revision compatibility;
- declared interaction mode and the learner-reserved epistemic work required by that mode;
- prerequisite and readiness floors, including whether the learner has enough representation for the proposed attempt;
- assistance, reveal, evaluator, consequence-tier, modality, accessibility, Tool, environment, permission, consent, time, and safety requirements;
- exact Teaching Skill version, dependency closure, validation status, lifecycle status, and Agent Harness compatibility;
- whether the procedure can preserve the required learner artifact, provenance, evaluation boundary, fresh-verification path, and stop controls.

An ineligible skill cannot be restored by predicted motivation, engagement, completion speed, Persona affinity, Model confidence, learner preference, or prior popularity. If no skill is eligible, the Harness must clarify missing context, diagnose prerequisites, propose a non-evidentiary exploratory action, recommend an appropriate human or external resource, or stop. It must not silently weaken the target or Evidence Contract to force a selection.

### Evidence-informed ranking

The Harness may rank only the eligible set. Ranking should estimate expected learning value for the declared purpose while preserving uncertainty and avoiding invented stable learner traits. Relevant inputs may include:

- target and evidence fit, prerequisite state, readiness, and the learner's demonstrated response to prior tasks, assistance, feedback, and delayed verification;
- current purpose, stakes, available time, modality and accessibility needs, learner preferences, and explicit constraints;
- discouragement, overload, confidence calibration, curiosity opportunities, desire to create, and opportunities for meaningful human connection;
- instructional evidence quality, validation coverage, known exclusions, novelty needs, and uncertainty about expected benefit.

These signals may alter the next procedure, challenge, example, scaffold, modality, Persona expression, or recommendation for a teacher, peer, mentor, or community. They do not become capability evidence merely because they influenced ranking. The system must not infer or preserve fixed learning styles, personality types, motivation types, or broad ability traits from a preferred modality or short interaction history.

Ranking must never optimize engagement, session length, easy completion, emotional attachment, or retention as ends that outweigh learning validity, learner agency, safety, accessibility, truthfulness, or the declared goal. Motivation is a first-class instructional responsibility, but manufactured progress, hidden delegation, dependency, and agent-completed work are invalid means of producing it.

### Learner choice and bounded Persona influence

The Learner Agent should present a comprehensible default and meaningful alternatives when more than one Teaching Skill is eligible. The learner may choose any eligible option, request another eligible option, ask why an option was included or excluded, or decline and stop. The Harness may limit choice only for an explicit policy, safety, permission, evidence-validity, or feasibility reason that it records and can explain.

A Persona may rerank eligible options and shape their presentation, examples, tone, challenge framing, or motivational expression. It cannot add an ineligible option, conceal a valid alternative, alter the target or evidence meaning, weaken learner-reserved work, raise its own relationship or commercial interest above the learner's purpose, or select a procedure solely to deepen attachment to the Persona.

The Model may propose candidates, ranking features, rationales, and uncertainty. The Harness alone validates eligibility, applies policy, resolves the selected immutable version and dependency closure, and authorizes execution.

### Selection record and explanation

For every selection decision, the Harness must append-preserve a versioned `TeachingSkillSelectionRecord` containing at minimum:

- the `TeachingContext`, target, goal, Map Revision, Evidence Contract, interaction mode, and policy versions used;
- the candidate Teaching Skill versions considered;
- each candidate's eligibility result and explicit exclusion reasons;
- the ranking inputs, evidence basis, uncertainty, known missing information, and ordered eligible set;
- Persona and Model proposals distinguished from Harness decisions;
- the default presented, alternatives exposed, learner choice or override, and any constrained-choice reason;
- the selected immutable version and dependency closure, fallback or reroute path, decision time, and actor authority.

The learner-facing explanation must answer: why this procedure now, what valid alternatives exist, why any requested option is unavailable, what learner work it protects, how assistance may change, and how the learner may override, pause, or stop. Ranking scores are decision aids, not scientific measures of the learner, and must not be presented as such.

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

## Teaching Skill, Evaluator, and Harness authority

Teaching Skill, Evaluator, and Agent Harness are three logically distinct authorities. This separation is defined by typed interfaces, bounded context, capabilities, versioning, and write authority. It does not require three processes or services.

The **Teaching Skill** owns instructional control within its declared scope. It may:

- propose plans, tasks, explanations, questions, hints, examples, feedback, and adaptations;
- preserve observations and request evidence evaluation;
- produce a non-authoritative `InstructionalAssessment` for immediate teaching adaptation.

It may not certify its own instructional success, select a more favorable Evaluator after seeing learner work, alter an evidence-eligible rubric after task issuance, access hidden verification material without a declared capability, or commit learner evidence.

The **Evaluator** owns bounded interpretation. It receives a sealed, versioned `EvaluationRequest` containing only the observations and conditions required by the Evidence Contract. It applies a declared rubric and interpretation rule and returns an `EvaluationProposal` or explicit abstention. It may not teach, widen the allowed claim scope, hide disagreement, access canonical state broadly, or perform durable writes.

The **Agent Harness** is the control plane and sole command authority. It:

- constructs the `TeachingContext` and sealed `EvaluationRequest`;
- freezes the task, Evidence Contract, rubric, Evaluator, assistance policy, and permitted claim scope before an evidence-eligible Attempt;
- grants least-privilege capabilities and denies ambient access to canonical stores, credentials, hidden materials, and unrelated learner data;
- preserves observations, assistance, reveals, proposals, policy decisions, disputes, corrections, and accepted commands;
- selects the required evaluation consequence tier;
- applies deterministic policy, provenance, version, idempotency, concurrency, and claim-ceiling checks;
- accepts, narrows, rejects, quarantines, or escalates proposals;
- appends validated Evidence Records and rebuilds current-state projections.

Harness ownership of the gate does not itself establish pedagogical or psychometric validity. Evaluators, policies, and uses still require evidence, calibration, monitoring, and correction.

## Sealed evaluation boundary

An evidence-eligible task must declare its target, task, Evidence Contract, rubric, interpretation rule, allowed claim scope, and Evaluator identity and version before the Attempt begins. Adaptive item selection is allowed only through a predeclared versioned procedure.

A fresh evaluator invocation must receive:

- sealed learner artifacts or observation references;
- task, target, Evidence Contract, rubric, and interpretation-rule versions;
- modality, environment, allowed Tools, and relevant accommodations;
- all assistance, feedback, exposure, and reveal events that affect interpretation;
- the maximum claim scope and intended evidence use;
- the required independence tier, provenance, and trace identity.

It must not receive the Teaching Skill's proposed score, private persuasive rationale, desired learner-state update, irrelevant Persona instructions, or mutable criteria created after observing the response. A Persona may shape learner-facing evaluation language after the decision, but it cannot change criterion results, uncertainty, escalation, or claim scope.

The same underlying Model may teach and evaluate in the initial system only through separate invocations with isolated contexts and recorded dependence. The same invocation may provide formative self-critique but cannot create canonical learner evidence. A separate Model, worker, service, operator, panel, or human reviewer strengthens some dimensions of independence but never substitutes for evaluator validity.

Deterministic, executable, exact, or reference-based checks must run before open-ended Model judgment when they can evaluate the intended construct validly. A Model Evaluator must preserve criterion-level results, observation citations, uncertainty, counterevidence, calibration status, and abstention as a valid outcome.

## Evaluation consequence tiers

Evaluation independence scales with the intended use and maximum claim scope, not with the apparent length or difficulty of the task.

| Tier | Consequence | Minimum boundary |
| --- | --- | --- |
| `T0 instructional` | Adapt teaching without changing a learner claim. | Embedded or logically separate formative assessment is allowed. No Evidence Record mutation. |
| `T1 bounded evidence` | Update one Learning Target interpretation under narrow stated conditions. | Deterministic evaluation where valid, otherwise a fresh sealed evaluator invocation plus Harness validation. |
| `T2 durable or cross-context claim` | Materially affect broader Capability, routing, or credential-like interpretation. | Corroborating Attempts and a separately invoked calibrated Evaluator, preferably with different failure characteristics; review on uncertainty or conflict. |
| `T3 disputed or high-stakes` | Affect safety, significant opportunity, formal assessment, external reporting, or a contested record. | Independent service, operator, qualified human, panel, or equivalent governed review. No single Model judgment is dispositive. |

The Harness must preserve which dimensions of independence are present: invocation context, prompt, Model, provider, process, credentials, deployment, operator, rubric author, hidden-material access, and human reviewer. Independence is multidimensional rather than a binary label.

## Modality declaration and first-class voice

Voice is a first-class capture and rendering modality around the semantic teaching system. It is not a separate agent, a privileged window into understanding, or a mandatory interface for targets that another modality can represent validly.

Every proposed Learning Task and every opportunistic evidence capture must include a versioned `ModalityDeclaration`. For each modality relative to each intended claim, the declaration assigns exactly one role:

| Role | Meaning | Evidence consequence |
| --- | --- | --- |
| `construct_relevant` | Features of the modality are part of the Learning Target, such as pronunciation, listening, oral interaction, public speaking, notation, or formal writing. | The Evidence Contract names the relevant features, conditions, accommodations, and validated scoring rule. Substituting another modality changes the task or claim. |
| `evidence_channel` | The modality carries learner work about another construct, such as a spoken conceptual explanation. | Evaluate the target-relevant semantic work, not generic performance in the channel. Equivalent channels should remain available where the construct permits them. |
| `accommodation` | The modality or transformation enables access to the same intended construct. | The accommodation and its effects remain explicit. It cannot reduce the learner claim merely because assistance was needed to access the task. |
| `presentation_only` | The modality renders agent or system content without constituting learner work. | It cannot become learner evidence, alter evaluation, or imply exposure, comprehension, or mastery. |

A modality may hold different roles for different claims, but its role cannot remain ambiguous within one Evidence Contract. When speech, writing, AAC, diagrams, notation, gesture, or another channel changes the construct rather than merely carrying it, the target and evaluation must say so explicitly.

### Voice interaction requirements

A voice-capable Teaching Skill must:

- obtain purpose-bound consent before capture, show an obvious recording state, and provide immediate pause, mute, stop, correction, and revocation controls;
- provide synchronized text for agent speech and provisional text for learner speech, plus keyboard-operable text, writing, AAC, and quiet-mode paths wherever the construct permits them;
- preserve raw audio, normalized audio, ASR partials, ASR final output, learner corrections, extracted claims, evaluation proposals, and generated speech as distinct lineage-linked artifacts rather than silently overwriting one with another;
- treat ASR partials as provisional display artifacts, never as sealed learner evidence;
- expose transcription failure, media gaps, degraded conditions, provider identity, Model and configuration versions, and relevant capture conditions instead of guessing or hiding them;
- keep learner speech evidence, Teaching Skill orchestration, Evaluator authority, Persona behavior, and Voice Package rendering rights logically separate;
- support interruption and cancellation so that unplayed agent speech, late provider output, or a cancelled turn cannot be mistaken for learner exposure or attached to a later turn;
- minimize audio, transcript, timing, and generated-speech retention under explicit learner permissions and the learner-state deletion contract.

For any `T1`, `T2`, or `T3` evidence-bearing voice evaluation, the learner must be able to inspect, correct, and approve the operative transcript revision before the Harness seals the `EvaluationRequest`. A later correction changes the turn seal, invalidates any proposal bound to the previous revision, and requires fresh evaluation before canonical use. `T0` formative feedback may use clearly labeled provisional transcription, but it cannot mutate a learner claim.

The Evaluator receives source audio or audio-derived features only when the Evidence Contract makes them construct-relevant, the learner has consented to that use, and the sealed request names the permitted features. Otherwise it receives the approved transcript and declared conditions, not unrestricted audio, prosody, or hidden provider features.

Accent, dialect, eloquence, assertiveness, speaking rate, pauses, fillers, disfluency, stuttering, volume, microphone quality, apparent confidence, apparent emotion, and ASR confidence are not learner-capability evidence unless the Learning Target explicitly includes the feature and the measure has been validated for the intended population and use. By default, hesitation or transcription uncertainty may trigger clarification or a fresh task, not a learner label or score.

Persona expression may shape wording, rhythm, tone, and delivery after instructional and evaluation decisions. A separately authorized Voice Package may render that expression. Neither a Persona Package nor a Voice Package may alter the learner artifact, modality role, rubric, criterion result, claim scope, or evidence boundary.

## Version identity and lifecycle

Every Teaching Skill release is an immutable, content-hashed `TeachingSkillVersion`. Its identity combines a stable `skill_id`, human-readable semantic version, schema version, and authoritative content hash. The content hash covers the canonical manifest and every declarative or executable artifact that can affect selection, learner work, assistance, evaluation, output, or failure behavior.

The version manifest must declare at minimum:

- publisher, provenance, creation time, status, superseded version, and human-readable and machine-readable change summaries;
- supported Learning Target and Evidence Contract families and versions;
- required `TeachingContext`, `TeachingSkillResult`, `ModalityDeclaration`, assistance-policy, and evaluator interface versions;
- exact built-in dependency versions or permitted dependency ranges that resolve to an exact dependency closure before execution;
- required and optional Tool capabilities, permission classes, runtime features, and minimum compatible Agent Harness version;
- supported learner conditions, modalities, accessibility paths, environments, consequence tiers, and known exclusions;
- validation evidence, calibration status where applicable, unresolved risks, and retirement or revocation conditions.

Semantic version labels communicate intended compatibility, but the content hash is authoritative. A release is classified as:

- **patch** when behavior, evidence meaning, permissions, learner work, and compatibility remain unchanged and the release corrects implementation or documentation without widening scope;
- **minor** when it adds backward-compatible target coverage, presentation, task forms, or capabilities without changing the meaning of existing declared behavior;
- **major** when it changes learner-reserved work, assistance or reveal policy, target or evidence meaning, rubric or evaluator requirements, modality role, claim scope, permissions, required Tools, durable outputs, failure behavior, or compatibility assumptions.

If classification is uncertain, the release is major. A semantic label never permits a consumer to ignore the exact hash, change summary, or validation status.

### Resolution and evidence pinning

Before a Teaching Skill executes, the Agent Harness resolves and records the exact skill version and exact dependency closure. `TeachingContext`, `TeachingSkillResult`, Attempts, Assistance Events, reveal events, evaluation requests, evaluation proposals, Evidence Records, traces, and replay records must reference those exact identities. Floating labels such as `latest`, mutable branches, provider aliases, or unrecorded dependency ranges cannot appear as the operative identity of an evidence-eligible run.

Historical learner work retains the versions under which it was elicited and interpreted. Installing, selecting, upgrading, rolling back, retiring, or revoking a Teaching Skill cannot silently reinterpret prior Attempts or overwrite prior Evidence Records. Applying a new skill, policy, rubric, or Evaluator to historical work creates a new proposal with new provenance and an explicit relationship to the prior interpretation.

### Upgrade and rollback

An active Learning Task or evidence-eligible Attempt remains pinned to its resolved version closure until it completes, pauses for an explicit migration, or is invalidated. No dependency may change in place during the run.

A future run may adopt a compatible version only through a declared upgrade policy that checks the manifest, change classification, validation status, target and Evidence Contract compatibility, required capabilities, learner permissions, and active plan state. Material changes must be inspectable before use. Changes that alter learner expectations, modality, retained data, permissions, safety, or evidence meaning require explicit learner notice or consent as the governing contract requires.

An in-progress Teaching Plan may migrate only through a versioned migration procedure that states preserved state, discarded state, changed behavior, evidence consequences, and rollback path. If equivalence cannot be demonstrated, the Harness closes or invalidates the affected task and starts a fresh task under the new version rather than pretending continuity.

Rollback selects an earlier immutable version for future eligible runs. It does not erase artifacts produced by the newer version or rewrite their provenance. The Harness must reject rollback when the earlier version is incompatible, revoked for safety or security, unavailable with its exact dependencies, or invalid for the intended Evidence Contract.

### Retirement, revocation, and archival replay

Retirement removes a version from normal new-run selection while preserving its manifest, hash, change history, validation record, and references needed to understand prior activity. Revocation additionally blocks new execution because of a security, safety, rights, validity, or integrity failure and applies an explicit policy to active runs.

Retired or revoked code need not remain executable forever. Audit and deterministic replay must remain possible from preserved manifests, events, inputs, recorded nondeterministic outputs, policy decisions, migrations, and non-reconstructive deletion tombstones. If an exact runtime can no longer be safely executed, the system must disclose that limitation rather than substituting a newer implementation and calling it equivalent.

## MVP and evolutionary topology

The MVP is a modular monolith with real logical boundaries:

- one deployable system may host Harness, trusted built-in Teaching Skills, Evaluation Broker, Evaluators, policy gate, evidence journal, command gateway, and projections;
- typed interfaces and capability denial must prove that Skills and Evaluators cannot call canonical repositories directly;
- Model-based evidence evaluation uses a fresh sealed invocation;
- evidence-critical observations and decisions are append-preserved, while current learner state remains a rebuildable projection;
- every mutating command carries an idempotency key, request hash, expected learner-stream version, exact references, and actor authority;
- retries with the same key and request return the original semantic result, while reuse with changed content is rejected and audited;
- replay consumes recorded Model, Tool, human, and external outputs rather than calling them again and assuming identical results;
- applying a new Evaluator to historical work appends a new proposal and never overwrites the old interpretation silently.

Physical isolation increases only when a real trust, failure, scaling, privacy, provider, operator, or consequence boundary requires it. Introduce isolated workers, durable queues, sandboxed third-party packages, separate credentials or services, and independent review incrementally. Do not distribute an unclear or invalid evaluator across services.

A full append-only design must remain compatible with learner deletion. Raw personal artifacts, projections, caches, backups, and reconstructive identifiers must be deletable under the learner-state contract; any retained tombstone must be non-reconstructive and narrowly justified.

## Non-negotiable failure boundaries

The system must reject or surface any Teaching Skill that:

- executes without a validated, versioned `TeachingContext` or silently replaces missing canonical inputs with model inference;
- returns untyped output, directly mutates canonical state, or bypasses the Agent Harness durable-write gate;
- treats its own evaluation or Evidence Record proposal as accepted evidence without independent harness validation;
- changes the evidence-eligible rubric, Evaluator, interpretation rule, or claim scope after seeing learner work without invalidating the task and creating a new versioned procedure;
- uses the same Model invocation both to teach and to produce canonical learner evidence;
- omits construct-relevant assistance, feedback, exposure, reveal, Tool, modality, or accommodation conditions from the sealed evaluation request;
- bypasses the required consequence tier, evaluator qualification, calibration, abstention, disagreement, or human-review rule;
- commits duplicate, stale, non-idempotent, untraceable, or silently overwritten evidence;
- lacks a versioned `AssistanceAndSolutionRevelationPolicy`;
- hides agent work or decisive assistance inside conversational style;
- omits the interaction mode or exact learner, agent, and Tool labor partition;
- switches from learning to hybrid or execution work without an explicit event and corresponding evidence consequence;
- treats reviewing, editing, explaining, or approving agent-produced work as equivalent to independently producing the target work;
- uses critical-engagement rituals as automatic evidence rather than evaluating the target-relevant learner work they elicit;
- treats exposure, agreement, copying, completion, or assisted success as independent capability;
- reveals decisive information without recording its effect on evidence validity;
- continues identical retries after its declared error or struggle boundary;
- treats accessibility accommodation as lower capability when the accommodation is not part of the target construct;
- permits a Persona, Model, Tool, or learner preference to bypass constitutional evidence boundaries;
- allows ranking, engagement, Persona affinity, Model confidence, or learner preference to resurrect an ineligible Teaching Skill;
- selects a skill before checking interaction mode, learner-reserved epistemic work, Evidence Contract compatibility, accessibility, permissions, exact version closure, or required evaluation boundaries;
- ranks or selects for session length, easy completion, attachment, or retention at the expense of learning validity, learner agency, truthfulness, or safety;
- assigns a fixed learning style, motivation type, personality type, or broad ability trait from modality preference or short interaction history;
- prevents the learner from choosing another eligible procedure, requesting an explanation, declining, pausing, or stopping without an explicit recorded governing reason;
- permits a Persona to introduce an ineligible option, conceal an eligible alternative, alter evidence meaning, or optimize for dependence on the Persona;
- treats a Model proposal as the authoritative eligibility, policy, version-resolution, or execution decision;
- executes without an append-preserved `TeachingSkillSelectionRecord` that distinguishes candidates, exclusions, ranking inputs, uncertainty, Persona and Model proposals, Harness authority, learner choice, and fallback;
- cannot identify what cognitive work the learner and agent each performed;
- cannot provide a fresh verification path when it claims movement toward independence;
- captures voice without purpose-bound consent or an obvious recording state, or continues capture after pause, stop, or revocation;
- uses an ASR partial, hidden transcript, or unapproved operative transcript for evidence-bearing evaluation;
- silently overwrites original audio, ASR output, learner correction, or prior evaluation when a later artifact is created;
- treats presentation-only persona speech, content exposure, accent, fluency, prosody, or transcription confidence as learner capability without an explicit validated construct;
- executes an evidence-eligible run under a floating or mutable Teaching Skill identity or without recording the exact dependency closure;
- changes a Teaching Skill, policy, evaluator dependency, Tool dependency, or modality rule in place under an existing version or content hash;
- silently upgrades an active task, Attempt, or Teaching Plan without preserving version identity and evidence consequences;
- rewrites historical learner work or evidence when a version is upgraded, rolled back, retired, or revoked;
- claims compatibility, migration equivalence, or safe rollback without declared checks and validation evidence.

## Minimum foundational claim

A conforming Teaching Skill may adapt how much help the learner receives. It may not adapt away epistemic honesty about who performed the work or what the resulting evidence can prove.
