# Learning Map epistemology and primary routing unit

Date: 2026-07-31

Scope: architecture research for Socratink's Knowledge Ontology, goal-scoped Learning Map, and Learner Evidence overlay. This is not a database selection or final implementation schema.

## Question

How should Socratink structure knowledge epistemically for a goal-scoped Learning Map, and what should be its primary routing unit? In particular, should the map route over a general concept or knowledge graph, a claim graph, a capability graph, or a target-centric map?

## Central conclusion

Socratink should adopt the proposed rule:

> **Learning Targets are the primary routable map nodes. Knowledge Components, Source Claims, exact provenance, and learner evidence should remain referenced layers rather than peer map nodes.**

This rule is the best fit with formal knowledge representation, evidence-centered assessment design, knowledge-space and prerequisite models, cognitive diagnosis, and Socratink's existing continuity contract. It preserves the distinction between:

- what the world or sources assert;
- what concepts, rules, relations, and instances mean;
- what the learner is trying to become able to do;
- what the learner has actually demonstrated under recorded conditions.

A Learning Map should be a goal-scoped, versioned route through **evidence-evaluable Learning Targets**, not a single all-purpose graph where concepts, source claims, tasks, evidence records, embeddings, and learner capability claims are interchangeable nodes. The map may traverse all those layers to choose and explain a route, but the learner-facing routing state should remain target-centric.

The practical routing unit should be:

> **A versioned Learning Target: a goal-scoped, evidence-evaluable claim that the learner can perform a stated action on specified knowledge under stated conditions.**

A Next Learning Action then instantiates the route as a target plus teaching skill plus task or interaction mode plus expected evidence.

## Why the target-centric rule is recommended

### 1. Formal ontology separates concepts, propositions, relations, and instances

Formal ontology and knowledge representation do not treat all graph nodes as the same kind of thing. Gruber's classic definition treats an ontology as an explicit specification of a conceptualization, and later ontology engineering work distinguishes domain concepts/classes, relations/properties, individuals/instances, axioms, and annotations. W3C RDF supplies a graph data model for statements as subject-predicate-object triples. OWL 2 adds formally interpreted classes, properties, individuals, data values, axioms, and versioning constructs. SKOS supplies a lighter model for concept schemes, labels, broader/narrower/related relations, mappings, examples, and notes.

For Socratink, this implies that the Knowledge Ontology should represent multiple epistemic types, not collapse them:

- **Concepts and Knowledge Components**: semantic units, rules, procedures, relationships, or skills hypothesized to support targets.
- **Propositions and Source Claims**: assertions attributable to a source, model, learner, curator, or extraction activity.
- **Relations**: typed links with semantics, for example `isA`, `partOf`, `causes`, `contrastsWith`, `equivalentTo`, `supports`, `attacks`, `exemplifies`, `requires`, or `assesses`.
- **Instances and examples**: particular cases, data points, worked examples, artifacts, or source spans.
- **Learning Targets**: goal-scoped performative claims about learner action under conditions.
- **Evidence Records**: observations and interpretations about learner performance, not knowledge itself.

A generic graph UI can display all of these. A routing system should not make them peers. Routing to "Bayes' theorem" as a concept, "the textbook says priors update likelihoods" as a source claim, "can solve base-rate problems unaided" as a target, and "learner solved item 7 with a hint" as evidence are different acts.

### 2. Source claims need provenance and argument structure, not route ownership

Socratink's source-ingestion provenance architecture already argues that original sources are immutable, source claims are interpretations, and every derivative assertion needs exact anchors and transformation provenance. W3C PROV-DM and PROV-O are a strong standards basis because they model entities, activities, agents, derivation, attribution, bundles, invalidation, and provenance of provenance. W3C Web Annotation is a strong basis for exact selectors over source spans, media intervals, byte ranges, regions, and derived representations.

Source Claims should therefore remain canonical in the Knowledge Ontology and provenance layers. They can justify Learning Targets and map edges. They can conflict, support, attack, supersede, or exemplify. But they should not be primary route stops because learning is not the same as accepting a source assertion. A source claim may be false, contested, irrelevant to the learner goal, too fine-grained, too broad, or pedagogically useless as the next action.

Argumentation theory reinforces this boundary. Toulmin-style argument structure distinguishes claim, data, warrant, backing, qualifier, and rebuttal. Dung's abstract argumentation frameworks model attack relations and acceptability among arguments. These structures help Socratink explain why a target or prerequisite edge is warranted. They do not by themselves decide which learner capability should be elicited next.

### 3. Evidence-centered design routes around claims to be made about performance

The National Research Council's assessment triangle separates cognition, observation, and interpretation. Evidence-centered design similarly asks what claims are to be made, what evidence would support them, what tasks can elicit that evidence, and what inference model connects work products to claims. This directly supports Learning Targets as route nodes.

A Learning Target is the unit that can connect:

- a cognition model: which Knowledge Components and prerequisite structures matter;
- an observation model: which task or dialogue can elicit relevant learner work;
- an interpretation model: how the Attempt would support, weaken, or leave unresolved a learner claim;
- a product action: what Socratink should ask the learner to do next.

A concept graph lacks the observation and interpretation part. A claim graph has epistemic content but not learner performance conditions. A capability graph is closer, but capabilities are usually broader current interpretations over evidence, not atomic route opportunities. A target-centric map is the smallest unit that can be both epistemically grounded and actionably assessed.

### 4. Knowledge-space theory and cognitive diagnosis support target-like observable states, not raw concepts

Knowledge-space theory models a domain as a set of problems or items and represents feasible knowledge states under prerequisite closure. It shows that adaptation depends on states and prerequisite structure, not just semantic relatedness among topics. Cognitive diagnosis models and Q-matrices map items to latent attributes or skills. They force a distinction between observed tasks, latent Knowledge Components, and claims about what a learner knows.

For Socratink, the useful adaptation is not "visit the next nearby concept." It is "choose the next target whose prerequisite target set is plausible, whose evidence value is high, and whose task can discriminate likely learner states." Knowledge Components and Q-matrix-like mappings belong behind the target and task design. They should inform routing, but they are not themselves the map route node.

### 5. Learning progressions and concept maps support structured routes, but need goal and evidence boundaries

Learning progressions represent hypothesized paths through increasingly sophisticated understanding over time. Concept maps represent meaningful relations among concepts and have empirical support as learning and assessment aids. Curriculum and prerequisite graphs can encode sequencing constraints. These sources support structured maps, but they do not imply that a general concept graph is the right runtime route.

A concept map can show that photosynthesis involves light energy, carbon dioxide, chlorophyll, glucose, and oxygen. A Learning Map needs routable targets such as "predict how limiting carbon dioxide affects glucose production in a simple plant-growth scenario, given a graph of inputs and outputs." The latter can be assessed, connected to evidence, decomposed into prerequisites, and used to choose a task.

### 6. Semantic similarity and embeddings are useful projections, not epistemic authority

Vector search, semantic similarity, and graph embeddings are valuable retrieval and clustering tools. But they are lossy, model-specific, version-dependent projections. They infer proximity from distributional or graph patterns, not truth, prerequisite necessity, conceptual identity, or evidence validity. Embeddings also encode corpus bias and can be brittle under domain shift. They should help Socratink find candidate Source Claims, Knowledge Components, examples, or possible target alignments. They should not decide canonical equivalence, prerequisite edges, learner mastery, or active route order without typed evidence and review.

## Comparison of candidate primary route structures

| Candidate | What it routes over | Strengths | Main failure mode | Recommendation |
| --- | --- | --- | --- | --- |
| General concept or knowledge graph | Concepts, relations, instances, facts, topics, examples | Good for semantic navigation, explanation, retrieval, concept maps, prerequisite discovery | Turns high-degree concepts into route stops. Conflates knowing about a concept with being able to do something. Cannot by itself specify evidence or task conditions. | Keep as Knowledge Ontology. Use to support and explain Learning Targets, not as primary route. |
| Claim graph | Source Claims, arguments, support/attack/conflict, provenance | Excellent for epistemic honesty, contested knowledge, source-backed explanation, correction and retraction | Routes through propositions instead of learner performances. May optimize source reconciliation rather than learning. Source granularity is unstable and source dependent. | Keep as claim/provenance/argument layer in the Knowledge Ontology. Use to warrant targets and edges. |
| Capability graph | Broad learner capabilities and subcapabilities | Closer to learner outcomes. Useful for summaries across projects and long-term transfer | Capabilities are evidence-derived interpretations, often too broad for next action. Making them route nodes risks circular mutation from inferred state to route state. | Keep in Learner Evidence overlay as current interpretations. Use to summarize and constrain routes. Do not make them atomic route nodes. |
| Target-centric Learning Map | Versioned Learning Targets with prerequisite, decomposition, equivalence, transfer, and assessment links | Aligns ontology, instruction, evidence, routing, and learner agency. Supports versioning and correction. Keeps mastery outside the map. | Requires disciplined target authoring. Poor targets can be vague, over-fragmented, or biased by available tasks. | Adopt. Learning Targets are primary routable nodes. |

## Separation of commitments

### Philosophical commitments

These are normative Socratink choices, not empirical discoveries:

1. **Epistemic humility**: sources, models, teachers, and learners can be wrong. Socratink should preserve uncertainty and conflict instead of forcing consensus.
2. **Learner agency**: the learner owns goals, authorizes sources, confirms material map revisions, and may inspect or challenge evidence.
3. **Layer separation**: truth-tracing, route planning, and learner evidence are different responsibilities.
4. **No mastery from exposure**: seeing content, receiving an explanation, or being semantically near a concept is not evidence that the learner can perform.
5. **Interpretability over opaque optimization**: routing should be explainable as target, rationale, evidence gap, source support, uncertainty, and next task.

### Established empirical findings

These are broadly supported by learning-science and assessment literature:

1. Assessment validity concerns interpretations and uses, not raw observations alone.
2. Claims about learner knowledge require coherence among cognition, observation, and interpretation.
3. Task design, assistance, modality, and context affect what was demonstrated.
4. Concept maps can support meaningful learning and assessment, but concept relation diagrams are not enough to infer performance.
5. Learning progressions and prerequisite structures are useful hypotheses that need empirical validation and revision.
6. Cognitive diagnosis requires explicit mappings between tasks/items and latent attributes or skills.
7. Similarity and embeddings are useful for retrieval and candidate generation, but they do not establish truth, prerequisite, or learner mastery.

### Formal and mathematical models

These are useful abstractions that Socratink can adapt:

1. **RDF graph model**: triples and datasets for representing statements and named graphs.
2. **OWL 2 ontology model**: classes, properties, individuals, axioms, annotations, imports, and version IRIs.
3. **SKOS concept schemes**: lightweight concept labels, broader/narrower/related links, mappings, examples, and notes.
4. **PROV**: entities, activities, agents, derivation, attribution, bundles, invalidation, specialization, alternate, and collections.
5. **Argumentation frameworks**: support, attack, rebuttal, qualifier, and acceptability structures around claims.
6. **Knowledge-space theory**: feasible learner knowledge states and prerequisite closure over a set of tasks or problems.
7. **Cognitive diagnosis and Q-matrix models**: mappings from observed items/tasks to latent attributes or Knowledge Components.
8. **Learning progressions**: ordered hypotheses about increasingly sophisticated understanding.

### Standards choices

Recommended standards profile:

1. Use **W3C PROV-DM/PROV-O** for provenance concepts and export vocabulary.
2. Use **W3C Web Annotation** selectors for exact source and derivative anchors.
3. Use **RDF/JSON-LD compatibility** for exportable graph statements and named provenance bundles, but do not require a triple store as the first storage engine.
4. Use **OWL 2 and SKOS selectively**: OWL where formal class/property/individual semantics and version IRIs help, SKOS where labels, concept schemes, broader/narrower, examples, and mappings are enough.
5. Treat embeddings, graph indexes, and vector stores as **disposable projections** that point back to canonical IDs, versions, and provenance.

### Product hypotheses

These need product validation:

1. Learners will understand and trust target-centric routes more than concept maps if each target has a clear action, rationale, and evidence condition.
2. A Learning Target can be made small enough for routing but large enough to avoid atomizing every micro-fact.
3. Source-claim provenance can be hidden by default but inspected when learners ask "why this target?" or "where did this come from?"
4. Target-centered routing will reduce false mastery compared with concept completion or exposure-based progress.
5. Cross-project evidence reuse can improve personalization if every transfer remains conditional and inspectable.

## Canonical placement of nodes and edges

### Knowledge Ontology

The Knowledge Ontology should own domain semantics, source assertions, provenance references, and uncertainty about knowledge structure. It represents available knowledge, not what this learner has mastered.

Canonical node types:

| Node type | Meaning | Notes |
| --- | --- | --- |
| `Concept` | A domain idea, term, category, variable, object, or phenomenon | SKOS-style labels, definitions, broader/narrower, related, examples, mappings are appropriate. |
| `KnowledgeComponent` | A concept, rule, relation, procedure, strategy, misconception, or skill hypothesized to support targets | Can be aligned to cognitive diagnosis attributes or KLI-style knowledge components. |
| `RelationType` | A defined edge semantics such as `causes`, `partOf`, `equivalentTo`, `requires`, `contrastsWith` | Relation definitions need direction, transitivity, symmetry, cycle policy, and scope. |
| `InstanceOrExample` | Particular case, worked example, source example, dataset row, problem, artifact, or counterexample | Should point to provenance or task records when sourced. |
| `SourceIdentity`, `Capture`, `Blob`, `Representation`, `Selector`, `Activity`, `Derivative` | Source/provenance entities | As already recommended in source-ingestion provenance architecture. |
| `SourceClaim` | Addressable interpretation of what a source asserts, with attribution, exact support, extraction method, confidence, and scope | Source Claims from different sources remain distinct even when equivalent. |
| `ArgumentOrWarrant` | Structured support, attack, rebuttal, backing, qualifier, or rationale over Source Claims and map hypotheses | Useful when provenance alone is not enough to justify a target or edge. |
| `EpistemicConflict` | Explicit disagreement or incompatibility among Source Claims or extracted structures | Never silently resolved by majority vote or embedding similarity. |

Canonical edge types:

| Edge type | Meaning | Cycle/equivalence treatment |
| --- | --- | --- |
| `isA` / `subClassOf` | Class or type inclusion | Cycles imply equivalence or modeling error, depending on formalism. |
| `partOf` / `hasPart` | Mereological or structural component | Cycles are invalid unless the edge is reinterpreted as mutual dependence. |
| `broader` / `narrower` / `related` | SKOS-style concept organization | Broader/narrower should not automatically imply prerequisite. |
| `equivalentTo`, `closeMatch`, `exactMatch`, `sameAsCandidate` | Identity or mapping between concepts, claims, or targets | Exact equivalence should require stronger review than close match. `sameAsCandidate` from embeddings is not canonical. |
| `supports`, `attacks`, `qualifies`, `rebuts` | Argument relations among claims or warrants | Cycles may occur in argument graphs and should be represented, not linearized. |
| `exemplifies` | Instance/example illustrates a concept, relation, claim, or target | Does not imply assessment or mastery. |
| `assertsPrerequisiteFor` | A Source Claim or model asserts that one component/target supports another | This is not yet an active Learning Map prerequisite edge. It is a claim with provenance and uncertainty. |
| `derivedFrom`, `wasGeneratedBy`, `used`, `wasAttributedTo`, `invalidated` | Provenance relations | Follow PROV constraints and preserve invalidated entities for audit. |

### Goal-scoped Learning Map

The Learning Map should own route structure for a specific Learning Goal and Goal Interpretation. It should not store mastery. It should reference ontology, claims, provenance, and learner evidence by ID and version.

Canonical node types:

| Node type | Meaning | Routable? |
| --- | --- | --- |
| `LearningMap` | A versioned route for one Goal Interpretation | No. Container. |
| `MapRevision` | Proposed change set with provenance, rationale, conflicts, and learner confirmation status | No. Governance object. |
| `LearningTarget` | Goal-scoped, evidence-evaluable claim that the learner can perform an action under conditions | **Yes. Primary routable unit.** |
| `TargetCluster` or `Module` | Convenience grouping of targets for presentation or scheduling | No by default. May summarize routes but should not replace targets. |
| `TargetMilestone` | Larger learner-visible achievement composed of targets | Usually not atomic. May be route checkpoint, not evidence unit. |

Minimum Learning Target fields:

```json
{
  "id": "lt:bayes-base-rate-v2",
  "mapVersion": "map:probability-goal-v4",
  "goalInterpretation": "gi:probability-for-medical-risk-v1",
  "statement": "Can compute and explain a posterior probability in a one-test base-rate scenario.",
  "actionVerb": "compute-and-explain",
  "objectRefs": ["kc:conditional-probability", "kc:base-rate", "kc:likelihood"],
  "conditions": {
    "modality": "text or spoken explanation",
    "allowedTools": "basic calculator",
    "assistance": "none after prompt clarification",
    "context": "single diagnostic-test word problem"
  },
  "evidenceContractRef": "ec:base-rate-posterior-rubric-v1",
  "sourceSupportRefs": ["claim:textbook-ch3-c17", "claim:paper-x-c4"],
  "prerequisiteRationaleRefs": ["claim:prereq-base-rate-to-posterior", "warrant:kst-ordering-v1"],
  "status": "active"
}
```

Canonical Learning Map edge types:

| Edge type | Meaning | Routing policy |
| --- | --- | --- |
| `requiresTarget` | Target A should normally precede target B because A is a prerequisite for B under this goal | Active route edge. Must have confidence, rationale, and source/model support. Hard cycles are invalid unless converted to co-requisite clusters. |
| `supportsTarget` | A helps B but is not a gate | Use for recommendation weighting, not hard blocking. |
| `subtargetOf` / `refines` | Target A decomposes B or makes it more specific | Part-whole cycles invalid. A parent is not automatically achieved by one child. |
| `alternativeTargetFor` | A and B are alternative routes to the same learner goal | Route can choose based on evidence, preference, constraints, or source requirements. |
| `equivalentTargetWithinGoal` | Two targets are treated as equivalent for this map version and goal interpretation | Must preserve original target IDs and evidence links. Equivalence outside the goal is not implied. |
| `transfersTo` | Evidence or performance on A may inform B under specified conditions | Always conditional. Requires transfer rationale and uncertainty. Does not copy evidence. |
| `assessableBy` | Target can be elicited by a task pattern, rubric, or Teaching Skill | Links to task/evidence design. It should not imply evidence exists. |
| `groundedIn` | Target or edge is justified by Source Claims, warrants, standards, or curriculum constraints | Explanatory link to referenced layers. Not a route step. |
| `conflictsWithMapHypothesis` | A proposed edge or target conflicts with a source, learner correction, or prior map version | Blocks silent activation. Requires Map Revision review. |

### Learner Evidence overlay

The Learner Evidence overlay should own observed work, Evidence Records, and current interpretations about the learner. It should link to Learning Targets by ID and version. It should never become the map itself.

Canonical node types:

| Node type | Meaning |
| --- | --- |
| `LearningTask` | Activity designed or selected to elicit observable work relevant to targets. |
| `Attempt` | Preserved learner work product under recorded conditions. |
| `EvidenceRecord` | Attempt plus conditions, provenance, interpretation rule, uncertainty, and bounded support or counterevidence for targets. |
| `LearnerTargetInterpretation` | Current computed status for a target under a versioned inference rule, for example insufficient evidence, likely independent, likely assisted, disputed, stale. |
| `CapabilityInterpretation` | Higher-order current claim over multiple targets, tasks, contexts, or times. |
| `CorrectionOrDispute` | Learner or curator challenge, exclusion, correction, or context note. |

Canonical edge types:

| Edge type | Meaning |
| --- | --- |
| `attemptsTask` | Learner produced work for a task. |
| `taskElicitsTarget` | Task was intended to elicit evidence for a target. |
| `evidenceSupportsTarget`, `evidenceWeakensTarget`, `evidenceUnresolvedForTarget` | Evidence interpretation relative to target and conditions. |
| `usesRubricOrInferenceRule` | Scoring or interpretation method. |
| `underConditions` | Modality, assistance, timing, allowed tools, context, accommodations. |
| `interpretedAsCapability` | Capability interpretation derived from eligible Evidence Records. |
| `transferredFromEvidence` | Cross-project or cross-target reuse with bounded relevance, never duplication. |
| `disputes`, `supersedes`, `excludedFromInference` | Correction and governance relations. |

## Handling uncertainty, conflict, versioning, and correction

### Uncertainty

Every non-obvious relation should carry uncertainty appropriate to its layer:

- SourceClaim confidence: extraction confidence, source authority, scope, quote support, and known limitations.
- Prerequisite confidence: empirical support, curriculum source, expert judgment, model inference, or learner-specific evidence.
- Target status uncertainty: inferred from Evidence Records, task validity, recency, assistance, and consistency.
- Transfer uncertainty: distance between contexts, modalities, tasks, and conditions.

Use categorical statuses before false precision: `asserted`, `hypothesized`, `contested`, `low-confidence`, `validated-in-this-domain`, `learner-confirmed`, `deprecated`, `invalidated`.

### Conflicting sources

Conflicting Source Claims remain separate. Socratink should represent:

1. the exact claim text or normalized proposition;
2. source identity and selector;
3. claim scope and qualifiers;
4. extraction or curation activity;
5. support or attack relations;
6. whether the conflict affects a target, map edge, task, or explanation.

A Learning Map should not silently choose one source. If the conflict materially changes a target or prerequisite edge, Socratink should create a Map Revision with a learner-facing explanation.

### Versioning

Version these separately:

- Source captures and derivatives;
- Source Claims and extraction activities;
- Knowledge Ontology schema and relation definitions;
- Goal Interpretation;
- Learning Map and Map Revisions;
- Learning Targets;
- Evidence contracts, rubrics, and inference rules;
- Learner Evidence Records and Capability interpretations.

A new source version or new extraction model should propose a map revision. It should not rewrite active map nodes or detach prior evidence from the target versions it originally informed.

### Correction

Corrections are append-only governance events:

- A learner correction to a goal or preference changes future route constraints, not historical evidence.
- A correction to a Source Claim invalidates or supersedes the claim but preserves provenance of the earlier assertion.
- A correction to a target may create a new target version and a map revision.
- A challenge to an Evidence Record can mark it disputed or excluded from future inference, then recompute current target and capability interpretations.

### Cycles

Cycles are not uniformly good or bad. The edge type decides.

| Cycle type | Treatment |
| --- | --- |
| Concept association cycles | Normal in semantic graphs. |
| Argument attack/support cycles | Normal and should be handled as argument structure. |
| `partOf` cycles | Modeling error unless the relation was misnamed. |
| Hard prerequisite cycles among Learning Targets | Invalid for routing. Collapse into co-requisite cluster, relax to `supportsTarget`, or split targets. |
| Equivalence cycles | Expected, but only if all equivalence links are validated. Candidate equivalence from embeddings should not become transitive identity. |
| Transfer cycles | Acceptable only as conditional relevance, not evidence cloning. |

### Prerequisite claims

Prerequisites should be treated as claims before they become active map edges:

1. A source, curriculum, expert, model, or empirical analysis asserts a prerequisite relation.
2. The assertion is stored as a Source Claim or map hypothesis with provenance and uncertainty.
3. The map builder proposes an active `requiresTarget` or `supportsTarget` edge for a specific goal and target version.
4. Material changes appear in a Map Revision.
5. Learner evidence can later weaken, strengthen, or personalize the edge without rewriting the original claim.

This avoids the common error of treating `broader/narrower`, textbook order, semantic similarity, or co-occurrence as prerequisite necessity.

### Equivalence

Equivalence must be typed and scoped:

- `exactMatch` between concepts is not the same as target equivalence.
- Source Claims that appear equivalent remain distinct because their provenance, scope, and authority differ.
- Learning Targets may be equivalent only within a Goal Interpretation and map version when they demand the same action, conditions, evidence contract, and knowledge scope.
- Embeddings can suggest `sameAsCandidate`, but a canonical equivalence relation needs symbolic checks or review.

### Part-whole

Part-whole should distinguish:

- conceptual part-whole: mitochondria are part of cells;
- target decomposition: explaining mechanism X has subtargets A, B, C;
- curriculum module containment: unit 2 contains targets A, B, C;
- evidence aggregation: multiple target interpretations support a capability.

These should not share one untyped `partOf` edge.

### Supports, exemplifies, assesses

- `supports` in the claim layer means epistemic support.
- `supportsTarget` in the map means pedagogical or prerequisite support.
- `evidenceSupportsTarget` in the learner overlay means an Evidence Record supports a learner claim.
- `exemplifies` means an instance illustrates a concept, claim, or target. It is not assessment.
- `assesses` or `taskElicitsTarget` links a task pattern to a target under an evidence contract. Completion alone is not mastery.

### Transfer

Transfer should be a conditional edge, not a copying rule. Evidence from one target or project can inform another only when Socratink records:

- source Evidence Record ID and original conditions;
- destination target and version;
- similarity and difference in construct, modality, assistance, task type, and context;
- transfer rationale;
- uncertainty and maximum effect;
- learner correction or opt-out if relevant.

This follows the existing learner-state contract: cross-project evidence is referenced with bounded relevance and cannot silently become universal transfer.

## Concrete routing queries

These are product-level query shapes, not database syntax.

### Query 1: choose the next target

Input:

- active Learning Goal and Goal Interpretation;
- active Learning Map version;
- learner preferences and constraints;
- current target interpretations from the Learner Evidence overlay;
- prerequisite edge statuses and uncertainties;
- available Teaching Skills and task patterns.

Ask:

> Which active Learning Target has unmet or stale evidence, has prerequisites satisfied or intentionally waived, has high expected instructional value, can be elicited by an available task or dialogue, and is within the learner's constraints?

Return:

- target ID and version;
- reason it is next;
- blocked prerequisites, if any;
- source and claim support for the target and edge;
- proposed Teaching Skill and task mode;
- expected Evidence Record contract;
- uncertainty and override options.

### Query 2: explain why a target exists

Ask:

> Why is this target in my map?

Return:

- Goal Interpretation link;
- Knowledge Components referenced;
- Source Claims and exact selectors that warrant inclusion;
- prerequisite or progression rationale;
- known conflicts;
- map revision that introduced it;
- whether it is required, optional, alternative, or learner-requested.

### Query 3: diagnose a failure on a task

Ask:

> Given this Attempt and Evidence Record, which target and supporting Knowledge Components are most likely implicated, and what should change in the route?

Return:

- target evidence status change, if any;
- Knowledge Components implicated by the task's Q-matrix-like mapping;
- confidence and alternative explanations such as modality, assistance, or language load;
- recommended target: retry, prerequisite target, alternative representation, or transfer task;
- no Capability mutation unless evidence contract allows it.

### Query 4: handle a new source

Ask:

> A newly authorized source introduces or changes claims relevant to this goal. What map revision is proposed?

Return:

- new or changed Source Claims with provenance;
- affected targets and map edges;
- conflicts with current map;
- proposed additions, removals, edge confidence changes, or target wording changes;
- learner-facing explanation;
- prior target versions and evidence links preserved.

### Query 5: evaluate transfer

Ask:

> Can evidence from target A in project X inform target B in project Y?

Return:

- original Evidence Record and conditions;
- destination target version;
- construct overlap;
- context and modality differences;
- transfer rule and maximum effect;
- uncertainty;
- whether a confirmatory task is recommended before durable Capability interpretation changes.

### Query 6: detect route pathologies

Ask:

> Does this Learning Map contain invalid hard cycles, unsupported prerequisite edges, target-equivalence overreach, source-conflict suppression, or evidence leakage into map nodes?

Return:

- hard prerequisite cycles;
- map edges without rationale or support;
- targets lacking evidence contracts;
- Source Claims promoted into target nodes;
- Evidence Records embedded as route nodes;
- embedding-generated equivalence accepted without review;
- required Map Revisions.

## Failure cases this architecture should prevent

1. **Concept completion masquerading as learning**: the learner viewed content under the concept "conditional probability," so the system marks conditional probability complete. Target-centric routing blocks this because no Evidence Record supports a versioned target.

2. **Embedding false friend**: semantic search equates financial derivatives with calculus derivatives and routes the learner to the wrong examples. Embeddings may propose candidates, but typed Knowledge Components, Source Claims, and target conditions must validate alignment.

3. **Source claim as route stop**: a textbook sentence becomes the next item: "Bayes' theorem updates priors by likelihood." The learner needs to compute, explain, or apply something. The source claim can ground a target but is not itself a learning action.

4. **Capability circularity**: current inferred capability "understands Bayes" becomes a route node, then task success updates the same broad node. Keeping Capability interpretations in the evidence overlay prevents a broad summary from replacing specific targets.

5. **Silent map rewrite after reprocessing**: a new extraction model changes claim clusters and silently changes target order. Versioned Source Claims and Map Revisions require inspection and learner confirmation for material changes.

6. **Prerequisite by textbook order**: chapter order creates hard prerequisites even when later evidence shows the learner can perform the downstream target. Prerequisite claims need warrant, uncertainty, and learner-specific override.

7. **Unbounded transfer**: success explaining a concept orally in biology is copied as evidence for written quantitative use in chemistry. Transfer edges must record conditions and uncertainty, and often should route a confirmatory task.

8. **Conflict erasure**: two sources disagree about a definition, and the system averages them into one canonical fact. Source Claims remain distinct with conflict relations. The map can route a target about distinguishing definitions if relevant.

9. **Over-fragmented target graph**: every vocabulary term becomes a target. A valid Learning Target must specify an action, condition, and evidence contract. Vocabulary concepts stay in the ontology unless they become demonstrable performance requirements.

10. **Untyped part-whole cycles**: a module contains a target, the target is part of a capability, and the capability is shown as part of the module, creating a routing loop. Typed containers, targets, and evidence-derived capabilities prevent this.

## Decision recommendation

Adopt a three-layer epistemic contract:

1. **Knowledge Ontology**: canonical semantic and epistemic structure. It owns concepts, Knowledge Components, Source Claims, source/provenance references, argument/conflict relations, instances/examples, and relation definitions. It can be queried by route generation but is not the learner route.

2. **Goal-scoped Learning Map**: canonical route structure for a Learning Project. It owns Learning Targets as primary routable nodes, plus target-to-target route edges, target groups, map revisions, and references to ontology claims and evidence contracts. It stores no mastery.

3. **Learner Evidence overlay**: canonical learner-performance evidence. It owns Attempts, Evidence Records, current target interpretations, corrections, disputes, and Capability interpretations. It references Learning Targets by version and can inform routing, but it does not rewrite the map.

The proposed rule should be adopted with four refinements:

1. **Learning Targets are primary route nodes, not the only queried entities.** Routing should traverse Knowledge Components, Source Claims, provenance, tasks, and learner evidence to choose and explain targets.
2. **Learning Targets must carry evidence contracts.** A target without action, condition, and assessability becomes a disguised concept node.
3. **Prerequisite edges are map hypotheses with provenance.** They are not inherited automatically from ontology hierarchy, curriculum order, or embeddings.
4. **Capabilities remain evidence-derived summaries.** They may constrain target selection and summarize progress, but they should not be atomic next-route nodes unless converted into specific Learning Targets.

## Minimal product contract

Before Socratink activates a target-centric map, every active Learning Target should satisfy:

- one Goal Interpretation and active map version;
- a performance verb and object of performance;
- explicit conditions, including modality, assistance, tools, and context where relevant;
- referenced Knowledge Components;
- an evidence contract or task pattern that can elicit work;
- source or design rationale;
- versioned prerequisite/support/decomposition edges, if any;
- uncertainty and review status;
- learner-visible explanation and override path.

Every active `requiresTarget` edge should satisfy:

- source, expert, empirical, or model rationale;
- confidence and edge type, hard requirement versus support;
- cycle check;
- affected target versions;
- review status;
- invalidation or correction behavior.

Every route recommendation should be able to answer:

- Why this target now?
- What would count as evidence?
- What sources or map hypotheses support it?
- What uncertainty or conflict exists?
- What happens if the learner disagrees or succeeds in a different way?

## Caveats

1. **Target authoring is the hard part.** The architecture only works if Learning Targets are written at the right grain size with observable actions and conditions. Too broad creates vague mastery. Too narrow creates route noise.
2. **Prerequisite relations are often empirical hypotheses.** Formal graph structure cannot guarantee that A must precede B for a particular learner. Socratink should support overrides and personalization.
3. **Knowledge-space and cognitive-diagnosis models require calibration.** Q-matrices and prerequisite closures are only as good as their task mappings and validation evidence.
4. **Concept maps are still valuable.** Rejecting concept nodes as primary route nodes does not reject concept-map views. Learners may benefit from seeing ontology maps, but routing should remain target-based.
5. **Standards do not solve product semantics.** RDF, OWL, SKOS, PROV, and Web Annotation provide representational tools. Socratink still needs a disciplined application profile and validation gates.
6. **Embeddings remain useful but bounded.** They can retrieve, cluster, and suggest. They should not canonically merge, order, or validate targets without typed evidence.
7. **Transfer is especially risky.** Cross-context generalization is pedagogically valuable but should be treated as uncertain until confirmed by evidence under destination conditions.

## What was not checked

- No exhaustive review of all intelligent tutoring prerequisite-mining algorithms was completed.
- No domain-specific empirical dataset was analyzed to validate target grain size or prerequisite edges.
- No comparative UX study was checked on learner trust in target-centric maps versus concept maps.
- No full legal review of standards licensing, source rights, or export obligations was performed.
- No storage-engine benchmark was conducted. The recommendation intentionally remains epistemic and schema-level.
- No formal Socratink ontology profile was written in OWL, SHACL, JSON Schema, or TypeScript.
- No review of all IMS Global, CASE, xAPI, or competency-framework standards was completed. These may matter for interoperability but were outside this pass.

## Strongest sources and why they matter

- W3C RDF 1.1 Concepts: establishes graph statements and datasets as representation substrate, not a product-specific epistemic type system. <https://www.w3.org/TR/rdf11-concepts/>
- W3C OWL 2 Structural Specification: distinguishes classes, properties, individuals, axioms, annotations, imports, and ontology versioning. <https://www.w3.org/TR/owl2-syntax/>
- W3C SKOS Reference: supports lightweight concept schemes, labels, broader/narrower, related, mappings, examples, and notes without equating concept hierarchy with prerequisites. <https://www.w3.org/TR/skos-reference/>
- W3C PROV-DM and PROV-O: establish entities, activities, agents, derivation, attribution, bundles, invalidation, and provenance of provenance. <https://www.w3.org/TR/prov-dm/> and <https://www.w3.org/TR/prov-o/>
- W3C Web Annotation Data Model: supports exact source anchors and selectors for text, media, regions, and other resource segments. <https://www.w3.org/TR/annotation-model/>
- Gruber, T. R. (1993). "A Translation Approach to Portable Ontology Specifications." DOI: <https://doi.org/10.1006/knac.1993.1008>
- Guarino, N., Oberle, D., & Staab, S. (2009). "What Is an Ontology?" DOI: <https://doi.org/10.1007/978-3-540-92673-3_0>
- Dung, P. M. (1995). "On the Acceptability of Arguments and Its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games." DOI: <https://doi.org/10.1016/0004-3702(94)00041-X>
- National Research Council. (2001). *Knowing What Students Know: The Science and Design of Educational Assessment.* DOI: <https://doi.org/10.17226/10019>
- Mislevy, R. J., Steinberg, L. S., & Almond, R. G. (2003). "On the Structure of Educational Assessments." DOI: <https://doi.org/10.1207/S15366359MEA0101_02>
- Doignon, J.-P., & Falmagne, J.-C. (1985). "Spaces for the Assessment of Knowledge." DOI: <https://doi.org/10.1016/S0020-7373(85)80031-6>
- Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). "The Knowledge-Learning-Instruction Framework." DOI: <https://doi.org/10.1111/j.1551-6709.2012.01245.x>
- Junker, B. W., & Sijtsma, K. (2001). "Cognitive Assessment Models with Few Assumptions, and Connections with Nonparametric Item Response Theory." DOI: <https://doi.org/10.1177/01466210122032064>
- de la Torre, J. (2009). "DINA Model and Parameter Estimation: A Didactic." DOI: <https://doi.org/10.3102/1076998607309474>
- Duncan, R. G., & Hmelo-Silver, C. E. (2009). "Learning Progressions: Aligning Curriculum, Instruction, and Assessment." DOI: <https://doi.org/10.1002/tea.20316>
- Novak, J. D., & Canas, A. J. (2008). "The Theory Underlying Concept Maps and How to Construct and Use Them." IHMC technical report: <https://cmap.ihmc.us/docs/theory-of-concept-maps>
- Nesbit, J. C., & Adesope, O. O. (2006). "Learning With Concept and Knowledge Maps: A Meta-Analysis." DOI: <https://doi.org/10.3102/00346543076003413>
- Salton, G., Wong, A., & Yang, C. S. (1975). "A Vector Space Model for Automatic Indexing." DOI: <https://doi.org/10.1145/361219.361220>
- Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). "Semantics Derived Automatically from Language Corpora Contain Human-like Biases." DOI: <https://doi.org/10.1126/science.aal4230>
- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). "On the Dangers of Stochastic Parrots." DOI: <https://doi.org/10.1145/3442188.3445922>
