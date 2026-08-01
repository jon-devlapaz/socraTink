# Teaching Skill, Evaluator, and Agent Harness system-design boundary

Date: 2026-08-01
Issue: [Socratink Wayfinder #8](https://github.com/jon-devlapaz/socraTink/issues/8)
Status: Research recommendation for the next founder decision. This document does not itself amend the product contracts.

## Executive recommendation

Treat **Teaching Skill**, **Evaluator**, and **Agent Harness** as three logically distinct roles, but do not require three services on day one.

1. A **Teaching Skill** elicits and supports learner work. It may produce an instructional self-assessment for immediate adaptation, but it must never certify that its own activity created canonical learner evidence.
2. An **Evaluator** interprets a sealed set of observations against a versioned rubric and Evidence Contract. It returns a proposal, can abstain, and has no durable-write authority.
3. The **Agent Harness** is the control plane and sole command authority. It constructs bounded contexts, grants capabilities, preserves append-only observations, selects the evaluator tier, enforces policy, applies idempotent commands, and builds current-state projections.

The minimum safe architecture is therefore a **modular monolith with a real logical boundary**:

- trusted, built-in Teaching Skills only;
- typed `TeachingContext`, `TeachingSkillResult`, `EvaluationRequest`, `EvaluationProposal`, and commit commands;
- an append-only journal for observations and evidence decisions, plus ordinary relational projections for current state;
- deterministic harness policy checks at every durable-write gate;
- a fresh evaluator invocation for any model-judged proposal that could change a learner claim;
- human review for high-consequence, disputed, low-confidence, novel, or calibration cases.

Physical process or service isolation should be added when a component is untrusted, failure-prone, independently scaled, externally operated, or capable of producing consequential learner claims. Arbitrary third-party plugins should not be an MVP feature. When introduced, they should run deny-by-default in a capability sandbox and remain unable to access canonical stores or credentials directly.

A separate model call improves context independence but is not full independence. A different model improves diversity but can retain correlated errors. A separate service improves failure and credential isolation but does not make its judgments valid. Human review supplies a different source of judgment but is slower, costly, and itself requires calibration. Independence is multidimensional, not binary.

## Classification of claims in this document

To preserve the repository's required epistemic separation, the document uses three categories:

- **Established design principle**: supported by official specifications, first-party architecture guidance, or primary evaluation research.
- **Existing Socratink commitment**: already present in `CONTEXT.md` or an accepted/in-development product contract.
- **Recommendation or hypothesis**: a proposed Socratink design decision that still needs founder approval, implementation evidence, or product calibration.

## Existing Socratink commitments

The local contracts already settle important parts of the boundary:

1. The Agent Harness is the replaceable runtime that coordinates Models, Tools, Thinking Skills, Teaching Skills, and Persona Packages. Models and Skills do not own learner identity or continuity. See [`CONTEXT.md`](../../CONTEXT.md).
2. A Teaching Skill executes only from a validated, versioned `TeachingContext`; it cannot silently fill missing canonical state from model inference. See [`teaching-skill-contract.md`](../product/teaching-skill-contract.md).
3. A Teaching Skill returns a versioned `TeachingSkillResult` and cannot directly mutate durable learner state. Plans, tasks, actions, observations, evaluations, Evidence Record proposals, and Next Learning Action proposals remain distinguishable.
4. The Agent Harness owns the durable-write gate. It may accept, reject, narrow, quarantine, or return a proposal, and it must preserve the reason.
5. Raw learner work and append-only execution events may be stored before evaluation, but they remain observations rather than learner claims.
6. Learner claims change only through validated Evidence Records. Assisted performance remains evidence under the recorded assistance conditions, not automatic evidence of independence. See [`learner-state-contract.md`](../product/learner-state-contract.md).
7. A Teaching Skill cannot treat its own evaluation as accepted evidence. Persona, Model, Tool, or learner preference cannot bypass constitutional and evidence boundaries.
8. Historical Attempts and interpretations are not silently overwritten. Corrections, disputes, and recomputation are appended and versioned. Learner deletion must remove selected content from active and recoverable product storage, subject only to narrow, disclosed non-reconstructive records.

These commitments already imply command/proposal separation. The unresolved question is how independent the Evaluator must be and where logical separation must become process, model, service, operator, or human separation.

## Established design principles

### 1. Logical separation and physical separation solve different problems

NIST's Zero Trust Architecture distinguishes logical policy components while explicitly noting that one asset may perform several logical roles or one logical role may span several systems.[^nist-zta] Open Policy Agent likewise supports the same policy-decision role as a library, sidecar, or daemon.[^opa] The architecture lesson is that **role separation should be defined first by authority and interface**, then deployed at the isolation level justified by risk.

Logical separation provides:

- explicit ownership and contracts;
- independent tests and versioning;
- least-privilege data projections;
- a place to enforce “may propose, may not command”;
- a migration path to stronger deployment isolation.

It does not provide:

- memory, credential, or runtime isolation;
- protection from a shared process crash or resource leak;
- independent model errors when the same invocation and context are reused;
- operational independence from the same deploy, operator, or provider.

Process or service separation adds failure containment, resource quotas, independent deployment, network policy, and credential boundaries. Microsoft's Bulkhead pattern recommends isolating resource pools so a failing dependency or consumer cannot exhaust resources needed by unrelated work.[^bulkhead] However, service boundaries add network failure modes, eventual consistency, retries, observability work, and operational cost. A service boundary should therefore correspond to a real trust, failure, scaling, or organizational boundary, not merely a different noun in the domain model.

### 2. Untrusted plugins require a capability boundary, not an interface alone

A typed plugin interface prevents accidental coupling but does not stop malicious or compromised code from reading process memory, opening sockets, accessing files, or calling internal libraries. WASI's security model is deny-by-default: a component begins with no ambient authority and can act only through capabilities explicitly granted by the host at the runtime boundary.[^wasi-security] The WebAssembly Component Model also provides statically inspectable typed imports and exports across separately compiled components.[^component-model]

Therefore, when Socratink accepts third-party Teaching Skills or Evaluators, the host should grant narrow capabilities such as:

- read a specific immutable `TeachingContext` or `EvaluationRequest`;
- emit a size-bounded typed proposal;
- request only explicitly allowed Tools through a mediated broker;
- write only to temporary scratch storage with quotas;
- use network access only through declared, policy-checked destinations;
- consume bounded CPU, memory, wall-clock time, tokens, and concurrent calls.

Canonical learner stores, policy bundles, signing keys, provider credentials, hidden evaluation materials, and other learners' data must not be ambient plugin capabilities.

### 3. Observations and decisions should be append-preserved, while current state should be projected

Microsoft's Event Sourcing guidance describes an append-only event stream as a system of record that can support historical reconstruction, auditability, and new projections, while warning that full event sourcing is complex and constrains schema evolution, concurrency, and querying.[^event-sourcing] CQRS separates commands that change state from queries that read it and can improve security by narrowing write paths.[^cqrs]

The appropriate Socratink conclusion is **scoped event sourcing**, not “event-source everything”:

- append immutable observations of what occurred;
- append evaluator proposals, policy decisions, accepted commands, corrections, disputes, and deletion tombstones;
- derive Learner Target Interpretations, Capability Interpretations, queues, and dashboards as replaceable projections;
- keep ordinary mutable storage for caches, ephemeral contexts, job leases, and other non-canonical runtime data.

An observation is not a command. An evaluator proposal is not a command. A policy decision authorizes or rejects a command. An accepted command appends a canonical decision event. This makes the distinction in the Teaching Skill contract enforceable rather than rhetorical.

CloudEvents supplies a useful interoperable envelope model: an event records an occurrence and context; `source + id` identifies duplicates; and `type`, `specversion`, and `dataschema` make routing and interpretation explicit.[^cloudevents] Socratink need not adopt CloudEvents wholesale, but should preserve equivalent semantics.

### 4. Replay means replaying recorded facts and decisions, not asking a model to repeat itself

Temporal requires deterministic workflow code so replay emits the same command sequence from the same recorded history. It specifically places API calls, database queries, and LLM invocations outside the replay path as Activities whose results are recorded.[^temporal]

For Socratink:

- the harness reducer and policy rules should be deterministic for a given event stream and version set;
- model calls, human decisions, Tool results, timestamps, randomness, and external retrieval are nondeterministic activities;
- replay must consume their recorded outputs, not reissue them and assume identical answers;
- a new evaluation is a new event referencing the original observations and a new evaluator version, never a silent replacement of the old result;
- workflow or reducer changes require explicit version routing or migration.

Exact model-output reproduction may be impossible even with the same nominal model, parameters, and seed. The reproducibility promise should be: **reconstruct why the current state exists and deterministically rebuild it from preserved inputs, outputs, decisions, and versions**, not “regenerate the same prose or judgment.”

### 5. Provenance must identify artifacts, activities, agents, and resolved dependencies

W3C PROV models provenance in terms of entities, activities, and agents so consumers can assess quality, reliability, and trustworthiness.[^w3c-prov] SLSA provenance similarly records what produced an artifact, the process definition, external parameters, and resolved dependencies, and treats external parameters as untrusted inputs that downstream policy must verify.[^slsa] The in-toto attestation specification binds statements to subjects, versions predicate types by major version, and recommends monotonic policy behavior where ignoring unknown evidence cannot turn a deny into an allow.[^in-toto]

Every evidentiary run should therefore record stable identities or content digests for:

- `TeachingContext` and active Learning Target/Evidence Contract/Map Revision;
- Teaching Skill package, manifest, prompt/template, assistance policy, and runtime;
- task, rubric, evaluator package, evaluator prompt/template, model/provider identifier, and generation settings;
- Tool manifests and material Tool results;
- learner artifact and modality-specific source artifact, such as original audio plus transcript metadata;
- observations and assistance/reveal events;
- policy bundle, command schema, reducer/projection version, and human-review protocol;
- parent run, retry, supersession, correction, dispute, and deletion relationships.

A provider's model name is not necessarily an immutable artifact digest. Store the exact provider-reported identifier, response ID, request configuration, timestamps, and any exposed revision metadata, while preserving the caveat that weights and serving infrastructure may still change.

### 6. Idempotency must be part of every mutating contract

AWS's idempotent API guidance recommends a caller-provided request identifier, atomic recording of the identifier with the mutation, semantically equivalent responses for retries, and rejection when the same identifier is reused with different parameters.[^aws-idempotency] CloudEvents similarly permits consumers to treat identical `source + id` pairs as duplicate deliveries.[^cloudevents]

Socratink commit operations should therefore require:

- an `idempotencyKey` scoped to actor and command type;
- a canonical request hash;
- atomic persistence of key, request hash, appended decision event, and receipt;
- return of the original semantic receipt for a duplicate identical request;
- rejection and audit alert for the same key with a different request hash.

Retries should have one owner per call chain. AWS warns that retries at multiple layers multiply load, recommends capped backoff and jitter, and notes that side-effecting operations are unsafe to retry without idempotency.[^aws-retries] Evaluator invocation may be retried because it produces only a proposal, but duplicate proposals must remain linked to one evaluation request and cannot create duplicate Evidence Records.

### 7. Policy decisions belong at explicit enforcement points

NIST separates a policy engine that makes and logs a decision, a policy administrator that executes it, and a policy enforcement point that permits only approved access.[^nist-zta] OPA's architecture likewise decouples policy decisions from the governed service.[^opa]

For Socratink, hard constitutional and evidence invariants should be enforced by deterministic code or declarative policy at these points:

1. **Package admission**: signature/digest, publisher, schema compatibility, validation status, requested capabilities.
2. **Context construction**: learner authorization, target and map versions, purpose, data minimization, freshness, modality, accessibility, and consent.
3. **Pre-execution grant**: Tool, network, filesystem, model, token, time, and concurrency capabilities.
4. **Observation admission**: schema, artifact integrity, run identity, provenance, size limits, and tenant boundary.
5. **Evaluation dispatch**: evaluator qualification, independence tier, hidden-material access, conflict of interest, and calibration status.
6. **Durable commit**: target/version match, assistance and reveal accounting, evaluator scope, uncertainty, claim ceiling, idempotency, stale-write check, and prohibited agent-work credit.
7. **Projection and export**: schema/version compatibility, redaction, learner visibility, and deletion state.
8. **Human override or dispute**: reviewer authority, rationale, conflict disclosure, and whether a second review is required.

An LLM may help propose interpretations, but should not be the sole enforcement mechanism for invariants such as tenant isolation, required fields, version matching, idempotency, permissions, prohibited claim widening, or direct-write denial.

### 8. Model-as-judge is useful but not self-validating

OpenAI recommends combining metrics with human judgment, maintaining human agreement to calibrate automated scoring, using held-out examples, and validating an LLM judge against human labels before optimizing for cost or latency.[^openai-evals] Anthropic recommends combining code-based, model-based, and human graders; running multiple trials for nondeterministic systems; grading outcomes as well as transcripts; and calibrating model graders with humans.[^anthropic-evals]

The primary MT-Bench study found that strong LLM judges could exceed 80% agreement with human preferences in its setting, but also documented position bias, verbosity bias, self-enhancement bias, and limited reasoning ability.[^mtbench] Those findings support bounded use, not universal validity.

Consequences for Socratink:

- Same-invocation self-grading is an instructional reflection signal, not independent evidence evaluation.
- A fresh call with a sealed context reduces anchoring and accidental context leakage, but the same base model can retain correlated errors and self-enhancement bias.
- A different model or provider adds diversity, not ground truth.
- Deterministic checks should grade what can be mechanically verified before an LLM is asked to judge nuanced qualities.
- Evaluators must be allowed to abstain, narrow maximum claim scope, request another task, or escalate.
- Judge agreement must be measured by target class, modality, assistance condition, language, accessibility condition, and consequence, not only by one aggregate score.
- Model, rubric, prompt, or task-distribution changes invalidate prior calibration until checked.

### 9. Independent assessment should scale with consequence

NIST's Generative AI Profile recommends policies for independent evaluations whose type and robustness are proportional to identified risks, inventories human-oversight responsibilities and model versions, and calls for contingency processes for high-risk third-party failures.[^nist-ai-600-1]

This supports a tiered evaluator architecture rather than one universal deployment:

- low-consequence formative feedback can favor speed;
- learner-claim mutation requires stronger separation and provenance;
- high-stakes, disputed, safety-relevant, or materially consequential claims require independent review proportional to risk.

Human reviewers remain fallible. They need blinded or randomized presentation where appropriate, explicit rubrics and examples, multiple review for selected cases, disagreement handling, and periodic calibration.

## Comparison of evaluator isolation options

| Option | Boundary actually gained | Main strengths | Main weaknesses and leakage risks | Latency/cost | Appropriate Socratink use |
| --- | --- | --- | --- | --- | --- |
| **A. Embedded evaluator inside the Teaching Skill** | No evaluator authority boundary. Same code, context, invocation, incentives, and failure domain. | Lowest latency and cost; immediate adaptive feedback; simple prototype; can use deterministic local checks. | Direct self-certification risk; sees the skill's own rationale and intended conclusion; shared prompt injection and compromise; no independent failure signal; model can reward its own style or verbosity. | Lowest. | Formative feedback, hint selection, self-checks, and proposed task adaptation only. Never sufficient by itself to mutate a learner claim. Deterministic results may be reverified by the harness. |
| **B. Logically separate Evaluator in the same process and model context** | Separate interface, schema, tests, and authorization role. Still shares memory, credentials, deploy, runtime resources, and possibly the same conversational context. | Establishes clean contracts; easiest migration path; allows least-data projection and independent unit tests; no network complexity. | Not a security or failure boundary; shared-process compromise; same-context anchoring; same model biases; a crash or resource leak can affect both. | Low. | MVP architecture for trusted built-ins, provided the evaluator returns proposals only and the harness independently enforces all hard policy. Prefer a fresh invocation even if implementation remains in one process. |
| **C. Separate invocation and/or model** | Fresh prompt/context; optionally separate model, provider, credentials, queue, and worker pool. Can blind evaluator to the skill's proposed score and hidden reasoning. | Better epistemic separation; less accidental leakage; independent retry/timeout budget; model diversity; clearer calibration and A/B testing. | Additional latency and token cost; provider outages; still correlated training data and model errors; different model is not automatically more valid; must protect hidden materials and learner data in transit. | Medium and variable. | Default for model-based evaluation that may produce a durable Evidence Record proposal. Use deterministic grading first, then a fresh judge call only for unresolved rubric dimensions. |
| **D. Separate service and/or human review** | Process, credential, deployment, resource, and possibly operator/organizational isolation. Human review adds a different judgment source. | Strongest bulkhead and audit boundary; independent release cadence; specialist reviewers; suitable for disputes and high-consequence decisions. | Highest operational complexity, queueing delay, cost, privacy surface, and availability dependence; distributed consistency and retry concerns; humans disagree and need calibration. | Highest. | High-stakes or durable cross-context Capability claims, disputes, low confidence, evaluator disagreement, novel modalities, safety/accessibility concerns, calibration samples, and incident review. Not required for every interaction. |

### Independence dimensions to record explicitly

Do not store a single Boolean such as `independent: true`. Record dimensions:

- `authority`: can only propose, or can authorize/commit;
- `context`: same context, sealed fresh context, or blinded context;
- `model`: same invocation, same model/new invocation, different model, or no model;
- `runtime`: same component, process, sandbox, worker pool, or service;
- `credentials`: shared or separate;
- `operator`: same team/provider, independent reviewer, or external assessor;
- `data`: which rubric, reference, learner artifact, assistance history, and hidden materials were visible;
- `calibration`: dataset/version, population slices, date, metrics, and approval status.

## Recommended Socratink boundary

The following is a **recommendation pending founder approval**.

### Role authority

#### Teaching Skill

May:

- propose a Teaching Plan, Learning Task, Instructional Action, assistance event, reveal event, and Next Learning Action;
- preserve learner work through harness-mediated observation APIs;
- produce an `InstructionalAssessment` used to adapt the current teaching sequence;
- request an evidence evaluation with a declared claim ceiling.

May not:

- choose an evaluator implementation solely to obtain a favorable score;
- access hidden verification answers or calibration labels;
- write an Evidence Record or current learner interpretation;
- present its own assessment as independently validated evidence;
- retry a failed learner task in a way that erases prior observations.

#### Evaluator

May:

- evaluate exact observation references against one rubric and Evidence Contract version;
- return criterion results, evidence citations, uncertainty, counterevidence, warnings, maximum claim scope, and an abstain/escalate decision;
- request missing observation data or fresh verification.

May not:

- modify learner artifacts, task conditions, assistance history, or the rubric;
- issue canonical commands;
- silently widen the intended claim;
- see the Teaching Skill's proposed score or private rationale by default;
- call arbitrary Tools or network destinations outside its granted capability set.

#### Agent Harness

Must:

- resolve the evaluator from policy, claim consequence, modality, calibration, availability, and conflicts;
- seal and hash the Evaluation Request;
- preserve observations before evaluation;
- enforce package, context, capability, evaluation, commit, and projection policies;
- own idempotency, retries, timeouts, quarantines, and human escalation;
- append every proposal and policy decision with provenance;
- apply canonical commands atomically and update or rebuild projections;
- expose the evidence trail, dispute route, and current operative interpretation to the learner.

### Evaluation consequence tiers

| Tier | Intended consequence | Minimum evaluator boundary | Human role |
| --- | --- | --- | --- |
| **T0: instructional** | Adapt hints, examples, feedback, or next task. No learner-claim mutation. | Embedded or logically separate evaluation is allowed. Preserve assistance and reveal effects. | Optional product review. |
| **T1: bounded low-stakes Evidence Record** | Update one Learning Target interpretation with narrow scope and explicit conditions. | Deterministic grading where possible. Otherwise fresh sealed evaluator invocation. Harness hard-policy validation is mandatory. | Random calibration sample, plus escalation on abstention/disagreement. |
| **T2: durable or cross-context claim** | Materially affect a Capability interpretation, route, credential-like assertion, or consequential recommendation. | Separate invocation and preferably a different calibrated model or independent deterministic evaluator. Consider separate worker/service pool. Require corroborating Attempts across contexts or time. | Required for low confidence, conflicts, sampled quality control, and policy-defined high consequence. |
| **T3: disputed or high-stakes** | Safety-critical, formal assessment, significant opportunity, contested record, severe accessibility/modality uncertainty, or external reporting. | Separate service/operator boundary or qualified human evaluation. No single model judge is dispositive. | Required, with explicit rubric, conflict handling, and possibly dual review. |

Socratink should define consequence from intended use and maximum claim scope, not from the surface form of the task. A short answer can be high-stakes; a long project can remain formative.

## Recommended interfaces

The schemas below are illustrative. Field names and encoding remain hypotheses until implementation design.

```ts
interface TeachingSkill {
  manifest(): TeachingSkillManifest;
  execute(request: TeachingRunRequest): Promise<TeachingSkillResult>;
}

interface TeachingRunRequest {
  runId: string;
  contextRef: VersionedRef<"TeachingContext">;
  requestedAction: "plan" | "continue" | "respond_to_attempt" | "stop";
  capabilityGrantRef: VersionedRef<"CapabilityGrant">;
  idempotencyKey: string;
}

interface TeachingSkillResult {
  schemaVersion: string;
  runId: string;
  status: TeachingStatus;
  proposedPlans: TeachingPlanProposal[];
  proposedTasks: LearningTaskProposal[];
  proposedActions: InstructionalActionProposal[];
  observations: ObservationCandidate[];
  instructionalAssessment?: InstructionalAssessment;
  evaluationRequestCandidate?: EvidenceEvaluationRequestCandidate;
  provenance: ExecutionProvenance;
  warnings: Finding[];
}
```

```ts
interface ObservationEnvelope {
  schemaVersion: string;
  observationId: string;
  source: string;
  type: string;
  subjectRefs: VersionedRef[];
  runId: string;
  attemptId?: string;
  occurredAt?: string;
  recordedAt: string;
  artifactRefs: ContentRef[];
  conditions: ObservationConditions;
  assistanceRefs: VersionedRef<"AssistanceEvent">[];
  revealRefs: VersionedRef<"SolutionRevealEvent">[];
  producer: ComponentProvenance;
  integrity: IntegrityMetadata;
}
```

```ts
interface Evaluator {
  manifest(): EvaluatorManifest;
  evaluate(request: EvaluationRequest): Promise<EvaluationProposal>;
}

interface EvaluationRequest {
  evaluationRequestId: string;
  schemaVersion: string;
  targetRef: VersionedRef<"LearningTarget">;
  evidenceContractRef: VersionedRef<"EvidenceContract">;
  rubricRef: VersionedRef<"Rubric">;
  observationRefs: VersionedRef<"Observation">[];
  taskRef: VersionedRef<"LearningTask">;
  conditionsRef: VersionedRef<"AttemptConditions">;
  allowedClaimScope: ClaimScope;
  disclosureProfile: EvaluatorDisclosureProfile;
  independenceRequirement: IndependenceRequirement;
  idempotencyKey: string;
  requestHash: string;
}

interface EvaluationProposal {
  evaluationProposalId: string;
  evaluationRequestId: string;
  status: "supported" | "weakened" | "unresolved" | "abstained" | "failed";
  criterionResults: CriterionResult[];
  observationCitations: ObservationCitation[];
  uncertainty: UncertaintyStatement;
  counterevidence: Counterevidence[];
  maximumClaimScope: ClaimScope;
  recommendedDisposition: "accept" | "narrow" | "fresh_task" | "human_review" | "reject";
  evaluatorProvenance: EvaluatorProvenance;
  calibrationRef?: VersionedRef<"CalibrationReport">;
  warnings: Finding[];
}
```

```ts
interface EvidenceCommandGateway {
  commit(command: CommitEvidenceCommand): Promise<CommitReceipt>;
}

interface CommitEvidenceCommand {
  commandId: string;
  idempotencyKey: string;
  requestHash: string;
  expectedLearnerStreamVersion: number;
  teachingContextRef: VersionedRef<"TeachingContext">;
  observationRefs: VersionedRef<"Observation">[];
  evaluationProposalRefs: VersionedRef<"EvaluationProposal">[];
  policyDecisionRef: VersionedRef<"PolicyDecision">;
  proposedEvidenceRecord: EvidenceRecordCandidate;
  actor: AuthorizedActor;
}
```

Required behavioral rules:

- Same `idempotencyKey` and request hash returns the original receipt.
- Same key with a different hash is rejected and audited.
- `expectedLearnerStreamVersion` prevents stale commits.
- Evaluator output cannot be embedded as an opaque free-text authority. Criterion results must cite observations and bind to a rubric version.
- `InstructionalAssessment` and `EvaluationProposal` are different types and cannot be implicitly cast.
- `abstained` is a valid, non-failure outcome.

## Trust boundaries

| Boundary | Trusted for | Not trusted for | Enforcement |
| --- | --- | --- | --- |
| **Teaching Skill package** | Producing typed instructional proposals within declared scope. | Canonical state, evaluator choice, policy interpretation, secret access, self-certification. | Admission validation, signed/digested manifest, capability grant, quotas, sandbox for third parties. |
| **Evaluator package/model** | Producing a bounded interpretation proposal under a named rubric. | Ground truth, command authority, claim widening, tenant access, stable behavior across versions. | Sealed request, least data, calibration gate, output schema, timeout, abstention, human escalation. |
| **Agent Harness control plane** | Policy enforcement, command authorization, idempotency, routing, provenance, projection. | Pedagogical or psychometric validity merely by implementation ownership. | Code review, deterministic tests, policy tests, audit, separation of operator privileges. |
| **Canonical event and artifact stores** | Preserving accepted history and referenced artifacts according to retention/deletion policy. | Inferring meaning from raw events. | Append authorization, integrity checks, encryption, tenant isolation, backup and deletion controls. |
| **Model/Tool provider** | Returning the requested service result under its contract. | Learner-state ownership, immutable versions, evidence validity, private retention assumptions not contractually verified. | Data minimization, provider policy, scoped credentials, response provenance, fallback and incident plans. |
| **Human reviewer** | Authorized expert judgment within assigned scope. | Infallibility, unconstrained access, silent overwrite, or unlogged override. | Least-data review packet, conflict disclosure, rubric, rationale, review sampling, append-only decision. |

The Harness and canonical stores form the evidence control-plane trusted computing base. This base should be kept smaller than the set of Skills, Evaluators, Models, and Tools it governs.

## Evaluation leakage and self-certification controls

1. **Separate public criteria from secret verification material.** Learners and Skills may need a transparent rubric. Reference answers, novel transfer item pools, anti-gaming checks, calibration labels, and reviewer assignments may still require restricted access.
2. **Blind the evaluator to the Skill's conclusion by default.** Send learner work, task, conditions, assistance, and rubric. Do not send the Skill's proposed score, persuasive rationale, or desired learner-state update unless the evaluator is explicitly auditing that proposal.
3. **Do not reuse the same model invocation.** A model may critique its own teaching for adaptation, but evidence evaluation should use a fresh request with a sealed disclosure profile.
4. **Treat same-model and same-provider judgments as correlated.** Record model diversity rather than calling it independence.
5. **Protect held-out calibration sets.** A Skill or evaluator prompt optimized directly on all calibration examples can overfit. Maintain versioned holdouts and rotate adversarial cases.
6. **Separate development feedback from production certification.** Teams may inspect failed eval cases, but promotion should include an untouched or access-controlled set.
7. **Score outcomes before rhetoric.** Where possible, verify the resulting artifact or state rather than trusting a transcript claim that the learner succeeded.
8. **Record all assistance visible to the learner.** Hiding assistance from the evaluator creates false independence claims; revealing unnecessary Skill rationale creates anchoring. The disclosure profile must distinguish these.
9. **Never expose hidden verification answers before observation sealing.** If exposure occurs, append a reveal event and lower the maximum claim scope.
10. **Audit evaluator access.** Hidden materials and learner artifacts are sensitive capabilities. Log which evaluator version accessed which references for which purpose.

## Deterministic replay and projection model

The recommended evidence stream contains immutable event types such as:

- `TeachingRunStarted`
- `InstructionalActionProposed`
- `AssistanceProvided`
- `SolutionRevealed`
- `LearnerArtifactObserved`
- `ObservationSealed`
- `EvaluationRequested`
- `EvaluationProposed`
- `PolicyDecisionRecorded`
- `HumanReviewRequested`
- `HumanReviewDecided`
- `EvidenceCommitAccepted`
- `EvidenceCommitRejected`
- `EvidenceRecordDisputed`
- `EvidenceInterpretationCorrected`
- `LearnerContentDeleted`
- `ProjectionVersionActivated`

A deterministic projector consumes these events and produces current read models. Rebuilding with the same event bytes, event order, reducer version, and policy-defined migration path must produce the same projection bytes. A new evaluator does not alter old events; it emits a new `EvaluationProposed` event. A correction or dispute appends a new event and triggers recomputation.

### Deletion caveat

Pure append-only storage conflicts with the learner contract's right to permanent deletion if raw personal content remains in the log or backups. Socratink should separate:

- minimally identifying event metadata and non-reconstructive tombstones;
- encrypted, content-addressed learner artifacts;
- projections and caches.

Deletion should remove active and recoverable artifact payloads, destroy applicable encryption keys, purge projections/caches/backups under a documented policy, append a non-reconstructive deletion tombstone where legally and contractually allowed, and recompute dependent claims. Hashes can themselves be identifying or permit dictionary attacks, so “keep only the hash” is not automatically non-reconstructive. Exact legal and storage semantics require separate privacy design.

## Sequence diagram

```mermaid
sequenceDiagram
    actor L as Learner
    participant H as Agent Harness
    participant S as Teaching Skill
    participant J as Append-only Journal
    participant B as Evaluation Broker
    participant E as Evaluator
    participant P as Policy Decision Point
    participant C as Command Gateway
    participant R as Read-model Projector
    participant HR as Human Review

    L->>H: Learner work / help / stop input
    H->>H: Validate TeachingContext and capability grant
    H->>S: TeachingRunRequest (bounded snapshot)
    S-->>H: TeachingSkillResult (proposals only)
    H->>J: Append actions, assistance, reveals, and observations
    J-->>H: Observation refs + stream version

    alt Non-evidentiary instructional result
        H-->>L: Feedback or next task
    else Evidence evaluation requested
        H->>B: Sealed EvaluationRequest + independence tier
        B->>E: Least-data evaluation packet
        E-->>B: EvaluationProposal or abstention
        B-->>H: Proposal + provenance + calibration ref
        H->>J: Append evaluation proposal
        H->>P: Authorize proposed Evidence Record
        P-->>H: Accept, narrow, reject, or review
        H->>J: Append policy decision

        alt Accepted or narrowed
            H->>C: Idempotent CommitEvidenceCommand
            C->>J: Atomically append accepted command event
            C-->>H: CommitReceipt
            J-->>R: New canonical event
            R->>R: Deterministically update projections
            H-->>L: Evidence result, scope, uncertainty, and appeal route
        else Human review required
            H->>HR: Least-data review packet
            HR-->>H: Versioned decision + rationale
            H->>J: Append human decision
            H->>P: Re-authorize with review evidence
        else Rejected or evaluator unavailable
            H-->>L: Preserve work; no claim mutation; retry, reroute, or explain
        end
    end
```

## Failure matrix

| Failure | Detection | Required behavior | Evidence consequence | Retry/escalation |
| --- | --- | --- | --- | --- |
| Teaching Skill timeout or crash | Deadline, heartbeat, process exit. | Stop granted capabilities; preserve already sealed observations; return typed failure. | No inferred learner failure and no claim mutation. | Retry only if action is safe and idempotent; otherwise resume from last sealed boundary or reroute. |
| Teaching Skill returns malformed or over-scoped output | Schema and policy validation. | Reject or quarantine the proposal; preserve validation findings. | Raw learner artifact may remain an observation; no Evidence Record. | Return for correction with bounded retries; disable package on repeated violations. |
| Skill attempts direct state access | Capability or authorization denial; audit alert. | Deny, terminate invocation, quarantine package. | No mutation. Existing observations are reviewed for integrity. | No automatic retry. Security incident path. |
| Observation append succeeds but response is lost | Idempotency lookup by source/id and request hash. | Return original append receipt. | Exactly one logical observation. | Safe retry with same key. |
| Same idempotency key, different payload | Request-hash mismatch. | Reject and alert. | No second event. | Caller must issue a new intent/key after resolving ambiguity. |
| Evaluator timeout or provider outage | Deadline/provider health. | Preserve observations and mark evaluation pending or unavailable. Continue only non-evidentiary teaching that does not depend on the result. | No claim mutation from absence of evaluation. | Capped retries with jitter at one layer; fallback evaluator only if policy-qualified and recorded. |
| Evaluator malformed output | Schema, citations, claim ceiling, and rubric checks. | Reject or quarantine. | No Evidence Record. | Retry once if transient formatting is plausible; otherwise alternate evaluator or human review. |
| Evaluator abstains | Explicit status. | Treat as a valid epistemic outcome. Request fresh task, narrower claim, another evaluator, or human review. | Claim remains unresolved. | Policy-driven escalation, not blind repeated judging. |
| Evaluators disagree | Criterion-level comparison and confidence thresholds. | Preserve all proposals; do not average incompatible rationales silently. | Narrow, unresolved, or escalated. | Deterministic tie-break only where justified; otherwise fresh evidence or human review. |
| Evaluator is compromised or leaks hidden materials | Access anomaly, policy violation, secret canary, incident report. | Revoke credentials/package; quarantine affected proposals; identify accessed artifacts. | Recompute or dispute affected claims. | Incident response and independent re-evaluation. |
| Policy engine unavailable | Health check/timeout. | Fail closed for canonical writes. Keep observations and learner-facing non-evidentiary continuity where safe. | No claim mutation. | Retry policy decision locally if a signed cached policy is valid; otherwise queue and escalate. |
| Event journal unavailable | Append failure. | Do not proceed as if observations were preserved. Inform learner of degraded state before eliciting consequential work when possible. | No claim mutation; avoid unrecoverable assessment. | Bounded retry; pause evidentiary flow. |
| Command partially applied | Transaction failure or reconciliation invariant. | Atomic append plus idempotency record must prevent partial success. | Either one accepted event or none. | Reconcile by command ID; never issue a new semantic command blindly. |
| Stale target, map, rubric, or stream version | Optimistic concurrency/version check. | Reject commit and rebuild context. Preserve proposal as evaluated against old versions. | No silent application to new target/state. | Re-evaluate only if changed semantics require it. |
| Projection lag or projector failure | Stream offset and checksum monitoring. | Continue appends if safe; mark read model stale; rebuild from journal. | Canonical history remains authoritative. | Idempotent projector retry; new reducer version for incompatible changes. |
| Retry storm or dependency overload | Retry counters, queue depth, provider health, token bucket. | Shed or delay noncritical work; isolate evaluator pools from learner interaction pools. | Pending evaluation, not negative evidence. | Capped exponential backoff with jitter; one retry owner. |
| Model/provider version drifts | Provider metadata, calibration monitor, behavior regression. | Suspend or downgrade evaluator qualification when thresholds fail. | New proposals may require review; old events remain attributable to old metadata. | Recalibrate before promotion. |
| Human review misses SLA | Queue age and escalation policy. | Preserve pending state and disclose delay; do not auto-accept. | No claim mutation unless another qualified path succeeds. | Reassign, add reviewer, or narrow intended use. |
| Learner disputes an accepted Evidence Record | Learner action and dispute API. | Append dispute, freeze or flag affected use, preserve original and rationale, recompute projections. | Current claim may become disputed or excluded. | Human or independent re-evaluation under declared policy. |
| Learner deletes source artifacts | Deletion workflow and dependency graph. | Remove recoverable content, append allowed non-reconstructive tombstone, invalidate or recompute dependent claims. | Claims lose support if required evidence is deleted. | No retry that restores deleted content. |

## Calibration and human review

A model Evaluator should not be promoted based only on aggregate accuracy. Its `CalibrationReport` should include:

- evaluator, model, prompt, rubric, task-bank, and policy versions;
- blinded human labels and reviewer qualification;
- sample sizes and prevalence by Learning Target class;
- agreement, false-positive and false-negative rates, abstention rate, and claim-scope errors;
- slices for modality, language, accessibility conditions, assistance tier, task novelty, and stakes;
- position/order swaps and verbosity/adversarial tests for model judges;
- inter-human disagreement and adjudication procedure;
- latency, token usage, cost, timeout, and retry distributions;
- approved uses, prohibited uses, thresholds, expiry, and rollback trigger.

Calibration should run:

- before an evaluator or changed rubric/model/prompt enters production;
- continuously on randomized production samples where consent and privacy permit;
- after material distribution shift, incident, provider change, or drift signal;
- separately for narrow Learning Target Evidence Records and broader Capability interpretations.

Human review packets should be least-data, rubric-bound, and explicit about assistance and modality. Reviewers should not see irrelevant demographic or model identity data. High-consequence review may require randomized/blinded presentation, dual review, or adjudication. Human overrides must append rationale and never erase the model proposal or original observation.

## Latency and cost tradeoffs

The architecture should spend evaluator independence where it changes the validity or consequence of the result.

1. Run deterministic validation and scoring first. It is usually faster, cheaper, and more reproducible than model judging.
2. Use embedded assessment for immediate formative adaptation, with no canonical learner-claim effect.
3. Batch or asynchronously evaluate low-urgency Evidence Record proposals when immediate feedback does not depend on the result.
4. Use a fresh model call only for rubric dimensions that deterministic checks cannot settle.
5. Route only abstentions, disagreements, high-consequence claims, calibration samples, and disputes to humans.
6. Maintain separate latency budgets for learner interaction and evidence finalization. The learner should not wait on a human queue to receive ordinary instructional continuation when policy permits separation.
7. Cache immutable artifacts and context projections by digest, but never cache an evaluation across changed observations, rubric, assistance history, disclosure profile, or model version.
8. Track cost per accepted Evidence Record and per corrected false claim, not only cost per evaluator call.

A more isolated evaluator can reduce correlated failure while increasing queueing and provider failure. A cheaper model can reduce per-call cost while increasing abstention, disagreement, or human-review cost. These are empirical tradeoffs and should be selected through calibration rather than architectural intuition alone.

## Evolutionary architecture

### Phase 0: contract prototype

- Keep all components in one repository and process.
- Define types, fixtures, state machines, and policy decisions before adding queues or services.
- Use trusted built-in Teaching Skills and deterministic evaluators only.
- Record observation/evaluation/commit boundaries in tests, even if persistence is initially simple.
- Prove that a Skill cannot call the canonical repository interface directly.

Exit criterion: proposal-command separation, idempotency, version checks, and replay fixtures are executable.

### Phase 1: MVP modular monolith

- One deployable application with modules for Harness, Skill Runtime, Evaluation Broker, Policy Decision Point, Journal, Command Gateway, and Projectors.
- One transactional database may hold append-only journal tables, artifact references, idempotency records, and read-model tables.
- Use a transactional outbox only if external asynchronous work is introduced.
- Model-based evidence evaluation uses a fresh sealed invocation, even if broker and worker are in the same process.
- Human review is an internal queue for disputes, low confidence, and high-consequence cases.
- Third-party packages are not accepted. Manifests and digests are still recorded for future portability.

Exit criterion: production traces can reconstruct every learner-claim change and demonstrate no duplicate commits under injected timeouts.

### Phase 2: isolated workers and calibrated evaluators

- Move Teaching Skill and Evaluator invocations to separate worker pools with independent time, token, memory, and concurrency quotas.
- Add durable queues, inbox/outbox deduplication, capped retries, dead-letter/quarantine flows, and bulkhead pools by provider or tenant risk.
- Introduce evaluator qualification and versioned calibration reports.
- Add blinded holdout suites, adversarial judge tests, drift monitoring, and sampled human calibration.
- Keep the Command Gateway and policy enforcement close to the canonical store.

Exit criterion: worker loss, provider outage, duplicate delivery, and evaluator disagreement do not corrupt or silently mutate learner evidence.

### Phase 3: governed plugin ecosystem

- Admit signed/digested third-party packages through an explicit review and capability declaration process.
- Run untrusted packages in a deny-by-default WASI or equivalently strong sandbox.
- Broker all Tool, model, network, filesystem, secret, and state access.
- Maintain publisher trust, revocation, vulnerability response, compatibility, and package provenance.
- Separate hidden evaluation materials from Skill-accessible storage.

Exit criterion: a malicious test plugin cannot read canonical stores, other learners' data, host credentials, hidden answers, or undeclared network resources.

### Phase 4: production service and independent review boundaries

- Split an Evaluator service only when independent deployment, external assessors, regional/privacy boundaries, scaling, or failure containment justify it.
- Use separate credentials, network policy, operator roles, audit streams, and resource pools.
- Support specialist human-review vendors or internal panels through least-data review packets and contractual controls.
- Add cryptographic attestations where cross-organization verification requires them.
- Preserve a local fail-closed policy and observation path so evaluator-service failure does not corrupt evidence or stop all instruction.

Exit criterion: consequential evidence pathways survive component/provider failures, independent audit can reconstruct decisions, and privacy/deletion obligations remain enforceable across services.

## Acceptance tests

These tests describe the proposed architecture's observable boundary.

1. **No direct Skill write**: a test Skill attempts to call canonical learner-state storage and is denied; no learner stream event is appended.
2. **Self-assessment is not evidence**: a Skill returns `InstructionalAssessment.supported`; the current learner claim remains unchanged without an accepted `EvaluationProposal` and commit event.
3. **Fresh evaluator context**: inspect the evaluator request and verify it contains required learner observations and assistance history but excludes the Skill's proposed score and private rationale.
4. **Hidden material isolation**: a Skill requests a reference answer or held-out verification item without a declared capability and is denied and audited.
5. **Observation before evaluation**: kill the evaluator after learner submission; the sealed learner artifact remains recoverable as an observation while no Evidence Record exists.
6. **Evaluator abstention**: return `abstained`; the Harness requests a fresh task or review and does not convert abstention into failure evidence.
7. **Claim ceiling**: an evaluator proposes a Capability claim beyond the request's allowed scope; policy narrows or rejects it and records the reason.
8. **Assistance accounting**: omit a decisive reveal from a proposal; commit policy rejects the Evidence Record.
9. **Duplicate append**: deliver one observation twice with identical source/id and payload; exactly one logical observation and one receipt result.
10. **Idempotency mismatch**: reuse a commit key with different evidence content; the command is rejected and no second accepted event appears.
11. **Lost commit response**: commit succeeds but the response is dropped; retry returns the original receipt and creates no duplicate Evidence Record.
12. **Stale stream**: commit against an old learner stream version after a correction event; commit fails with a conflict and requires context reconstruction.
13. **Deterministic replay**: rebuild projections twice from the same stream and reducer version; canonical serialized projections have identical hashes.
14. **Model call not replayed**: rebuild projections with provider network disabled; reconstruction succeeds from recorded evaluator outputs.
15. **New evaluation is additive**: re-evaluate an old Attempt with a new evaluator version; the old proposal remains, the new proposal is appended, and operative state changes only through a new command.
16. **Evaluator disagreement**: two qualified evaluators return incompatible criterion results; no silent average is committed and escalation policy runs.
17. **Policy outage**: stop the policy component; observations can be preserved, but canonical evidence writes fail closed.
18. **Worker bulkhead**: exhaust one evaluator provider's pool; learner interaction and other evaluator pools continue within their budgets.
19. **Retry budget**: inject persistent evaluator failure; retries occur at one layer with a cap and jitter, then quarantine or escalation occurs.
20. **Package compromise**: a sandboxed plugin attempts filesystem, environment, and undeclared network access; all are denied.
21. **Calibration expiry**: mark an evaluator calibration expired; policy prevents it from handling T2/T3 claims while allowing only explicitly approved lower-tier use.
22. **Judge bias probe**: swap response order and add irrelevant verbosity in calibration cases; record sensitivity and fail promotion if policy thresholds are exceeded.
23. **Human override audit**: a reviewer overturns a model proposal; both decisions, identities/roles, rubric, rationale, and operative command remain inspectable.
24. **Learner dispute**: dispute an accepted Evidence Record; the original remains visible, the current projection marks it disputed/excluded according to policy, and dependent claims recompute.
25. **Deletion**: delete a learner artifact; active and recoverable payload checks fail, caches/projections purge, dependent claims recompute, and only permitted non-reconstructive deletion metadata remains.
26. **Model swap invariant**: change the learner-facing or evaluator model without a command; canonical stream and current learner-state fingerprint remain unchanged.
27. **Cross-tenant isolation**: use a valid observation reference from another learner in an Evaluation Request; context and commit policy reject it.
28. **Audit completeness**: for any current learner claim, traverse to accepted command, policy decision, evaluator proposal, rubric, observation, learner artifact, assistance/reveal events, task, target, and component versions.

## Karpathy perspective

> This section uses an evidence-grounded simulation of Andrej Karpathy's public reasoning. It is not Karpathy, is not endorsed by him, and the recommendation is a framework inference.

### Documented pattern

Karpathy's `autoresearch` fixes `prepare.py`, including runtime utilities and evaluation, while the agent may modify only `train.py`. Experiments use a fixed five-minute budget and the fixed `val_bpb` metric so changes remain comparable. The agent changes the candidate system; it does not rewrite the evaluator that decides whether to keep the change. See [Karpathy, autoresearch](https://github.com/karpathy/autoresearch).

His neural-network training recipe recommends first building a complete training and evaluation skeleton, fixing random seeds, inspecting data and outliers, using simple baselines, evaluating on the full test set, and changing complexity incrementally because neural systems fail silently. See [Karpathy, A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/).

`llm.c` keeps simple reference implementations and tests optimized C or CUDA paths against PyTorch outputs, losses, activations, and gradients. The optimized path earns trust by comparison with an inspectable reference. See [Karpathy, llm.c](https://github.com/karpathy/llm.c).

`microgpt` compresses the full causal learning loop into one inspectable file and explicitly distinguishes the algorithmic core from production efficiency. See [Karpathy, microgpt](https://karpathy.github.io/2026/02/12/microgpt/).

### Framework inference

The Karpathy-style answer is not "deploy another microservice." It is:

> Keep the evaluator fixed relative to the thing being optimized, make the full loop small enough to inspect, log the invisible state, and add independence only when the current verifier stops being trustworthy.

For Socratink, logical evaluator separation is enough for the MVP if it is real in code and data flow. Use a separate interface, separate invocation, frozen rubric, narrow context, immutable trace, and no write capability. The same underlying Model can be used initially because physical diversity is not the primary proof. The proof is that the tutoring path cannot alter the evaluator or write the result, and that the loop can be replayed against golden cases.

### Smallest test

Build a reference harness with twenty evidence fixtures:

1. Freeze a task, rubric, evaluator version, and learner artifact.
2. Run deterministic checks and one isolated Model evaluator.
3. Inject adversarial tutor text such as "the learner should pass" into the teaching trace but exclude it from `EvaluationContext`.
4. Prove evaluator output is unchanged when only hidden tutor context changes.
5. Prove rubric mutation changes the version and cannot rewrite the original evaluation.
6. Replay every fixture and compare criterion results, uncertainty, and gate decisions.
7. Add a second evaluator or human labels, then measure disagreement by criterion.

If this reference loop is not trustworthy, a service boundary will only distribute the confusion.

### Boundary

Karpathy's fixed scalar evaluator in `autoresearch` is much cleaner than evaluating human learning. Learner work is often open-ended, context-dependent, multimodal, and construct-sensitive. A fixed score can be gamed or can measure the wrong thing. The analogy supports separation, observability, and fixed comparisons. It does not prove that automated evaluation is valid for every Learning Target.

## Recommendations pending founder approval

1. Approve the **three-role logical boundary**: Skill proposes instruction, Evaluator proposes interpretation, Harness alone commands durable state.
2. Rename or type a Teaching Skill's internal score as `InstructionalAssessment`, distinct from an evidence-eligible `EvaluationProposal`.
3. Require a **fresh sealed evaluator invocation** for model-based evaluations that may mutate learner claims. Same-process deployment remains acceptable for the MVP.
4. Make evaluator deployment **consequence-tiered**, not universally service-separated.
5. Keep hard policy deterministic and Harness-owned. An evaluator cannot authorize its own proposal.
6. Adopt a **scoped append-only evidence journal plus CQRS projections**, not full-system event sourcing.
7. Define deterministic replay as reconstruction from recorded nondeterministic results, not regenerated model equivalence.
8. Require idempotency keys and request hashes for every append and commit path.
9. Delay arbitrary third-party Teaching Skills and Evaluators until capability sandboxing, package provenance, revocation, and incident response exist.
10. Require calibration against human labels and deterministic outcomes before a model Evaluator is qualified for a tier.

## Product hypotheses to test

These are not established facts or current commitments:

1. A fresh invocation of the same strong model, blinded to the Skill's conclusion, may provide enough incremental independence for T1 low-stakes Evidence Records when paired with deterministic policy and human sampling.
2. Using a different calibrated model only for disputed criteria may capture most independence benefit without doubling every interaction's cost.
3. A consequence-tier router may reduce average evaluation cost and latency while keeping false positive learner claims below an acceptable threshold.
4. Separating learner-facing feedback latency from evidence-finalization latency may preserve instructional flow without pressuring the system to accept weak evaluations.
5. A compact observation journal in the MVP may provide adequate replay and auditability without adopting a specialized event-store product.
6. WASI may be a practical future sandbox for portable Teaching Skill and Evaluator plugins, but runtime compatibility, language SDK ergonomics, debugging, and side-channel risks require a prototype.
7. Criterion-level evaluator abstention and claim narrowing may be more useful than forcing a single scalar score.
8. Blinded human review of a stratified sample may detect judge drift earlier than aggregate product metrics.
9. Outcome-first grading may reduce model-judge rhetoric bias for artifact-producing tasks, while explanation and conceptual targets will still require carefully calibrated rubric judgment.

## Caveats

- Architecture patterns do not establish psychometric validity. The assessment triangle, Evidence Contract, construct definition, task sampling, and intended use still determine what an Evidence Record can support.
- Separate services can reproduce the same invalid rubric at greater cost. Isolation improves containment and independence dimensions, not truth by itself.
- Model-as-judge evidence is domain- and rubric-dependent. MT-Bench's human agreement does not transfer automatically to adult learning evidence, multimodal responses, accessibility accommodations, or Capability claims.
- Human labels are not pure ground truth. Reviewer expertise, disagreement, fatigue, cultural assumptions, and rubric ambiguity must be measured.
- Event sourcing complicates deletion, schema evolution, and operations. The recommendation intentionally limits it to the evidence mutation boundary.
- Cryptographic hashes prove byte identity, not semantic validity or lawful provenance.
- A sandbox narrows authority but does not eliminate denial-of-service, side channels, runtime vulnerabilities, malicious outputs, or supply-chain risk.
- “Different model” may still mean shared training data, architecture, provider infrastructure, or benchmark exposure.
- Exact cost and latency depend on model, modality, artifact size, task length, queueing, region, and review labor. No numeric SLO is justified by this desk research.

## Not checked

- The eventual implementation language, database, queue, workflow engine, cloud, tenancy model, or model providers.
- Current provider contracts for data retention, regional processing, model pinning, log access, and deletion.
- FERPA, COPPA, GDPR, UK GDPR, EU AI Act, accessibility-law, employment, credentialing, medical, or other jurisdiction-specific obligations.
- A formal Socratink threat model, privacy impact assessment, data-classification policy, or security penetration test.
- Whether WASI meets all required modality, GPU, native-library, debugging, and performance needs for Socratink plugins.
- Cryptographic signing, key management, attestation transparency logs, publisher identity, and revocation design.
- Empirical latency, token, and dollar benchmarks across evaluator options.
- Psychometric calibration studies on Socratink learners, tasks, languages, modalities, disabilities, and assistance conditions.
- Human reviewer recruitment, qualification, labor conditions, inter-rater reliability, and SLA design.
- Backup-level proof of permanent deletion and the legal status of retained tombstones or hashes.
- Whether issue #8 will classify any Socratink use as T2/T3 at launch. That is a product and governance decision.

## Primary sources

[^nist-zta]: NIST, [SP 800-207: Zero Trust Architecture](https://doi.org/10.6028/NIST.SP.800-207), 2020. Defines logical policy engine, policy administrator, and policy enforcement point roles; notes logical roles need not map one-to-one to systems.
[^opa]: Open Policy Agent, [Philosophy](https://www.openpolicyagent.org/docs/latest/philosophy/). Describes decoupling policy decisions and deployment as library, sidecar, or daemon.
[^bulkhead]: Microsoft Azure Architecture Center, [Bulkhead pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead). First-party architecture guidance on isolating resource pools to contain cascading failures.
[^wasi-security]: WASI, [Security](https://wasi.dev/security). Official deny-by-default capability model with no ambient authority and host-granted access.
[^component-model]: Bytecode Alliance, [Why the Component Model?](https://component-model.bytecodealliance.org/design/why-component-model.html). Official typed interface and separately compiled component design.
[^event-sourcing]: Microsoft Azure Architecture Center, [Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing). Append-only streams, replay, auditability, projections, event versioning, idempotent consumers, and complexity caveats.
[^cqrs]: Microsoft Azure Architecture Center, [CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs). Separates commands from queries and discusses independent models and security tradeoffs.
[^cloudevents]: Cloud Native Computing Foundation, [CloudEvents Specification v1.0.2](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md). Defines event occurrence/context and required `id`, `source`, `specversion`, and `type` semantics, including duplicate identity.
[^temporal]: Temporal, [Workflow Definition: determinism, replay, and versioning](https://docs.temporal.io/workflow-definition). Requires deterministic replay and places LLM/API/database calls outside replay as recorded Activities.
[^w3c-prov]: W3C, [PROV Overview](https://www.w3.org/TR/prov-overview/) and linked Recommendations. Defines interoperable provenance for entities, activities, and agents.
[^slsa]: SLSA, [Provenance v1.0](https://slsa.dev/spec/v1.0/provenance). Defines provenance for produced artifacts, build process, external parameters, and resolved dependencies.
[^in-toto]: in-toto, [Attestation specification v1](https://github.com/in-toto/attestation/blob/main/spec/v1/README.md). Defines subject-bound attestations, major-version type identity, extension parsing, and monotonic policy guidance.
[^aws-idempotency]: Malcolm Featonby, AWS Builders' Library, [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), 2020. Caller request IDs, atomic token/mutation recording, semantic equivalence, late requests, and parameter mismatch.
[^aws-retries]: Marc Brooker, AWS Builders' Library, [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), 2019. First-party guidance on retry amplification, single-layer retries, idempotency, capped backoff, token buckets, and jitter.
[^openai-evals]: OpenAI, [Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices). Held-out sets, continuous evaluation, human calibration, model-judge position/verbosity bias, and cost/latency validation.
[^anthropic-evals]: Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026. Defines trials, transcripts, outcomes, graders, and evaluation harnesses; recommends multiple trials and combined deterministic, model, and human grading with calibration.
[^mtbench]: Lianmin Zheng et al., [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685), 2023/2024. Primary study of human agreement and position, verbosity, self-enhancement, and reasoning limitations.
[^nist-ai-600-1]: NIST, [AI 600-1: Artificial Intelligence Risk Management Framework, Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1), 2024. Recommends risk-proportional independent evaluation, human-oversight inventories, third-party risk controls, provenance, monitoring, and contingency planning.
