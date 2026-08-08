---
type: product-doctrine
doctrine_id: socratink-learner-agent-os-north-star
status: accepted-baseline
doctrine_version: 1
accepted_at: 2026-08-02
founder_direction_confirmed_at: 2026-08-02
wayfinder_map: https://github.com/jon-devlapaz/socraTink/issues/1
acceptance_ticket: https://github.com/jon-devlapaz/socraTink/issues/13
review_trigger: "Review when credible learning, safety, trust, feasibility, economic, legal, market, or model-capability evidence materially challenges a classified claim or the first proof disconfirms a product hypothesis. Do not treat engagement growth, one anecdote, one benchmark, or unscoped preference as doctrine proof."
---

# Socratink north star

## North star

Socratink is designed to give each supported learner a persistent Learner Agent that can grow with them across subjects, goals, models, skills, and personas.

The Learner Agent maintains an explicit, revisable account of what the learner is trying to become capable of, preserves evidence-grounded interpretations of what they have actually demonstrated, and recommends learning experiences that can help them grow without doing the learning for them.

Models, Tools, Teaching Skills, and persona costumes may change. The learner's continuity, agency, evidence, and relationship remain.

## Human belief

Learning is a beautifully human endeavor. It is the act of becoming more capable through curiosity, effort, explanation, creation, error, revision, and return.

AI performing a task does not make human understanding obsolete. It makes judgment, problem solving, formal reasoning, creativity, verification, and the ability to direct powerful tools more important. Socratink begins from a founder commitment: the learner can become smarter and should not be encouraged to surrender that growth because a Model can produce an answer.

The product must help learners grow alongside AI, not become spectators to it.

## Core promise

> Your agent grows with you, remembers what you have actually demonstrated, and finds a better way to help you learn across subjects without doing the learning for you.

The Learner Agent does not merely answer questions correctly. It maintains enough inspectable context about where the learner is, where they are trying to go, and what has helped before to recommend challenges, explanations, examples, personas, and moments of assistance that may help the learner keep becoming more capable.

## Doctrine authority and delegation

This document is Socratink's canonical product doctrine. It owns the product's human purpose, core promise, non-negotiable boundaries, durable product unit, first-proof direction, decision filter, and epistemic governance.

| Artifact | Owns | Must not do |
| --- | --- | --- |
| `north-star.md` | Product doctrine, strategic direction, constitutional product boundaries, and claim classification | Pretend to be research, a detailed runtime contract, an implementation plan, or a record of observed results |
| [`../../CONTEXT.md`](../../CONTEXT.md) | Canonical domain language and relationships | Store implementation design, product rhetoric, or unresolved hypotheses |
| Product contracts | Binding operational elaboration of doctrine for learner state, Learning Maps, Teaching Skills, Personas, motivation, and later governed domains | Weaken doctrine, silently redefine canonical terms, or promote hypotheses into truth |
| Research notes | Sources, methods, findings, limitations, and evidence calibration | Set founder values, product authority, or runtime policy by themselves |
| Wayfinder decisions and roadmap artifacts | Decision history, dependencies, scope, and execution order | Replace doctrine or hide unresolved decisions inside implementation tasks |
| `README.md` and other summaries | Derived orientation for contributors and readers | Contradict or outrank the canonical doctrine and contracts |

A narrower contract may make doctrine operational but cannot override it. When doctrine, canonical language, research, and a product contract appear to conflict, work pauses until the owning artifacts are reconciled explicitly. Apparent precedence is not permission to conceal a contradiction.

## Motivation is a primary product responsibility

Correct pedagogy is not sufficient when a learner lacks the desire, confidence, curiosity, or perceived purpose required to continue. Motivation, curiosity, and the experience of consistent support directed toward the learner's growth are part of the product's job.

Socratink should:

- communicate that the learner's growth still matters in a world of increasingly capable AI;
- select challenges and examples that can awaken curiosity because they fit the learner's current understanding and direction;
- help the learner see why foundational work connects to something they care about creating or becoming;
- use continuity, persona, voice, and remembered interaction preferences to make support feel personal rather than generic;
- respond when the learner reports, requests help with, or confirms a permitted observation of discouragement, overload, uncertainty, or loss of purpose, rather than silently inferring a hidden emotional state;
- celebrate learner-authored effort, insight, correction, persistence, and creation without manufacturing evidence or praise;
- recommend human teachers, peers, mentors, or communities when human connection is the better intervention.

Motivation is not engagement optimization. Socratink must not create dependency, demand loyalty, manipulate emotion, hide difficulty, provide false praise, inflate progress, or perform the learner's work to keep a session going. A successful outcome may be continued work, later return, a changed strategy, human help, useful action outside Socratink, or departure after the learner accomplishes or revises their purpose. Product retention alone does not establish motivation or growth.

These responsibilities are governed by the [`Motivation, Curiosity, and Human Connection Contract`](motivation-contract.md). Its approved vocabulary does not imply nine separate product subsystems. The first proof uses one learner-visible Motivation Recovery Loop with bounded observation, learner choice, minimal approved retention, separated outcomes, and explicit safety stop gates. Contextual inspiration, Persona continuity, motivation memory, and proactive interpretation remain product hypotheses that must demonstrate incremental value over excellent pedagogy and transparent learner choice.

Revenue, growth, notification, retention, analytics, access, and success decisions are governed by the [`Growth-Incentive Compatibility Contract`](growth-incentive-contract.md). Socratink may earn from capability-building, trustworthy continuity, and transparent access, but not from attention, unnecessary assistance, emotional attachment, prevented exit, or learner-state exploitation. Learner success outside the product, human referral, pause, export, and goal-complete departure remain legitimate outcomes.

## The Learner Agent OS

The durable product entity is one learner-owned Learner Agent, not a chatbot session or Model account.

The Learner Agent:

- builds and revises a provenance-aware Knowledge Ontology from learner-authorized Sources;
- creates goal-scoped Learning Maps around demonstrable Learning Targets;
- maintains a separate Learner Evidence Model grounded in preserved Attempts and explicit conditions;
- invokes versioned Teaching Skills to create, support, observe, and evaluate learner work;
- uses learner-chosen Persona Packages as bounded cognitive, pedagogical, motivational, and expressive costumes;
- preserves continuity across Model, Tool, Skill, persona, project, and deployment changes;
- recommends one explainable Next Learning Action while preserving learner override.

The ontology represents available knowledge structure. The evidence model represents bounded claims about learner performance. The Learning Map connects them without turning either into a decorative mastery graph.

## Foundations before invisible dependence

Socratink does not interpret “learn the foundations” as memorizing every command or performing every rote operation without tools. Foundations are the concepts, representations, decomposition habits, causal models, verification practices, and judgment required to understand a domain and recognize when an answer is wrong.

The Learner Agent should distinguish:

- knowledge that must become independently retrievable or usable;
- procedures that should be understood but may be tool-assisted;
- details that may safely remain externally retrievable;
- higher-order judgment that becomes more important as AI handles lower-level production.

The intended progression is not “learn without AI forever.” It is:

1. establish enough conceptual and problem-solving foundation to direct and verify work;
2. preserve learner-generated reasoning and creation where those actions are the learning target;
3. introduce AI-assisted execution with explicit provenance and assistance conditions;
4. teach the learner to frame valuable problems, direct tools, inspect architecture, test outputs, diagnose failure, and retain the ability to act when automation is wrong.

The Learner Agent must make the current division of cognitive labor visible. An interaction may be primarily **learning**, where target-relevant reasoning and creation remain learner work; **execution**, where the agent performs work to accomplish an external goal; or **hybrid**, where the learner and agent divide the work explicitly. These modes are all legitimate, but they do not produce equivalent evidence. Switching modes must be deliberate, assistance must remain attributable, and delegated work cannot be laundered into a claim of independent capability.

Learning with AI should develop critical engagement rather than passive acceptance. Where relevant to the target, the learner should predict, question, inspect, edit, test, challenge, explain, or revise model output. The product must preserve a practical route back to fresh performance under reduced or declared assistance.

## Creation and falsifiable feedback

Learners become capable by doing more than discussing capability. Socratink should help them explain, solve, build, decide, teach, test, and create things that matter to them.

The product should prefer tasks with observable consequences and useful feedback loops. A prototype that runs, an explanation that survives challenge, a proof that closes, a prediction that can be checked, or a design that encounters a real constraint can reveal more than passive exposure or fluent conversation.

Agent output, content exposure, completion, time spent, and apparent confidence are not learner capability. The product preserves who performed the work and what the result can actually prove.

## Teaching and relationship

Conversation maintains continuity and relationship. Purpose-built Teaching Skills create the learning work.

A Persona Package may influence mental models, examples, humor, challenge style, motivational strategy, and voice. It is a costume over the Learner Agent OS, not a separate agent and not an authority over truth, evidence, permissions, or safety.

The relationship should make the learner feel known and supported without pretending the simulation is a human, exploiting vulnerability, or replacing human relationships. Persona continuity earns its place when it helps the learner attempt, persist, reflect, create, and return.

## First product proof

The smallest complete proof serves an adult learner facing a real technical or academic performance demand.

The learner provides a goal and a Source. The Learner Agent builds a provisional Learning Map, wears a chosen persona costume, invokes the first reconstruction Teaching Skill, preserves spoken or written learner work, identifies one consequential gap, and chooses a later action from evidence. If difficulty interrupts the encounter, the learner may invoke or confirm one bounded Motivation Recovery Loop without hidden affect inference or evidence mutation. The learner returns after elapsed time and attempts meaningful work again. Learner continuity survives a Model boundary.

This first proof is not the whole product. It must demonstrate the operating principle from which broader subjects, Teaching Skills, personas, modalities, and learning projects can grow.

## Decision filter

Build a product change when it materially improves one or more of these without violating another:

- the learner's desire and belief that continued growth is worthwhile;
- curiosity about a meaningful problem, idea, or creation;
- reaching learner-generated cognitive work rather than passive consumption;
- preserving foundational understanding and problem-solving judgment;
- selecting the right Teaching Skill, challenge, assistance, or modality for the current learner and goal;
- producing valid, inspectable evidence of what the learner can do;
- helping support fade as independence grows;
- returning for delayed reconstruction, transfer, or creation;
- using AI more powerfully without losing the ability to direct, verify, and recover from it;
- preserving learner ownership, continuity, privacy, dignity, and truthful uncertainty.

Do not prioritize chat volume, session length, streaks, content consumption, output volume, automatic completion, persona attachment, or apparent fluency unless they demonstrably serve learner growth under the product's evidence and relationship contracts.

## Doctrine governance and epistemic status

Every material claim in this doctrine belongs to one of five classes.

| Claim class | Meaning | Revision and falsifiability boundary |
| --- | --- | --- |
| **Founder commitment** | A normative choice about what Socratink exists to protect or pursue | It is not established or falsified by a metric. It changes only through an explicit, versioned founder decision that states the trade-off and migration consequence. |
| **Evidence-grounded principle** | A scoped empirical principle supported by cited research and bounded by population, construct, task, modality, and method | It must narrow or change when stronger evidence, validity failure, boundary conditions, or material counterevidence require it. |
| **Product hypothesis** | A falsifiable belief that a Socratink mechanism will improve a declared learner, learning, trust, safety, or viability outcome | It requires predeclared outcomes, comparison, disconfirming signals, stop gates, and a decision to retain, narrow, redesign, or reject it. |
| **Strategic first-proof constraint** | A current choice about wedge, scope, sequence, or the smallest complete proof | It is not pedagogical truth. It changes when feasibility, cost, risk, learner access, opportunity, or earlier decisions make another proof more informative. |
| **Observation or implementation choice** | A measured result, qualitative signal, architecture, provider, interface, threshold, or other execution decision | It remains outside doctrine unless an explicit governance decision promotes a scoped interpretation into a principle, hypothesis, commitment, or strategic constraint. |

### Current classification

**Founder commitments** include the value of human learning, the learner's capacity to grow, learner ownership, epistemic honesty, motivation without manipulation, human connection when appropriate, and the refusal to confuse Agent output with learner capability.

**Evidence-grounded principles** include active retrieval, explanation, practice with feedback, spacing, readiness-sensitive guidance, explicit assistance conditions, accessibility, metacognitive agency, and bounded interpretation of learner evidence. Their scope and implementation remain subject to the linked research and product contracts. The principal evidence boundaries are maintained in [`../research/teaching-skills-evidence.md`](../research/teaching-skills-evidence.md), [`../research/teaching-skill-epistemic-labor.md`](../research/teaching-skill-epistemic-labor.md), [`../research/learner-evidence-mutation-validity.md`](../research/learner-evidence-mutation-validity.md), and [`../research/voice-learning-evidence.md`](../research/voice-learning-evidence.md).

Socratink should adapt to the target, prior knowledge, accessibility needs, learner preference, observed response, and current conditions. It must not assign fixed visual, auditory, kinesthetic, verbal, or social “learning styles” and treat those labels as scientific learner traits.

**Product hypotheses** include whether a persistent Learner Agent, the Motivation Recovery Loop, contextual inspiration, learner-chosen Personas, voice, relationship continuity, motivation memory, Human Connection Exits, and evidence-informed Teaching Skill selection materially improve agency, meaningful action, learning, safe return behavior, trust, or willingness to pay. Motivation evaluation must keep learner report, meaningful behavior, valid learning evidence, safety and relationship effects, operational context, and commercial viability distinct. Non-returners remain part of the outcome. Willingness to pay may inform viability but cannot validate learning, safety, truth, or the mission.

**Strategic first-proof constraints** include the 18+ initial wedge, a real technical or academic performance demand, a learner-provided goal and Source, a chosen Persona costume, the reconstruction Teaching Skill, spoken or written learner work, elapsed-time return, and continuity across a Model boundary. These choices define the current proof, not the full product or universal learner need.

Qualitative interviews, transcripts, founder observations, learner reports, benchmark results, and product telemetry are **observations** until interpreted through an explicit claim class. The 2026 Chris Piech interview supplied by the founder, <https://youtu.be/g-CD1d0q01I>, and the founder-supplied transcript about cognitive offloading and purpose-built educational AI, <https://youtu.be/52FiVExXfnU>, strengthened product direction but are not controlled learning evidence. Rhetorical neuroscience, correlational findings, learning-style language, product engagement, and model fluency do not become doctrine through repetition.

### Promotion and anti-cherry-picking rules

- An observation may motivate a hypothesis but cannot silently become a principle or commitment.
- A successful product hypothesis does not become a founder commitment. A failed product hypothesis does not automatically negate a founder commitment.
- An evidence-grounded principle requires traceable sources, construct validity, scope, limitations, and stronger treatment than a qualitative signal or one benchmark.
- Product tests must predeclare the treatment, comparison, outcomes, interpretation rules, stop gates, and population before consequential claims are made.
- Null results, negative results, non-returners, rejected interpretations, correction cost, accessibility failures, and subgroup harms remain part of the record.
- Metrics and claim classes cannot be changed retrospectively to turn an unsuccessful test into success.
- Engagement, retention, affection, Persona attachment, output volume, and willingness to pay cannot substitute for valid learning evidence or learner welfare.

### Review, amendment, and replacement

Doctrine review is required when credible evidence materially challenges a classified claim, the first proof disconfirms a core product hypothesis, recurring learner behavior contradicts the intended experience, safety or validity failures appear, the product cannot remain economically or technically feasible without violating its commitments, law or ethics changes the permissible boundary, or Model and market capability materially changes the problem or wedge.

A clarification or evidence-link correction may amend the current version when it does not change authority, claim class, core promise, first-proof boundary, or a learner protection. A material change creates a new doctrine version with the initiating evidence, founder decision, affected contracts, migration consequences, and superseded version preserved. Negative evidence cannot be deleted merely because the doctrine changes.

## Explicit deferrals

This doctrine does not choose database technology, vector infrastructure, Model provider, deployment topology, authentication system, UI framework, exact evaluator threshold, pricing, go-to-market motion, or general business model. It does not authorize under-18 deployment, unrestricted Persona distribution, cloned or protected Persona voice, hidden affect inference, social matching, universal agent portability, or production implementation beyond the accepted contracts and roadmap.

These are governed by later evidence, contracts, Wayfinder decisions, or explicit scope changes. Deferral is not permission for an implementation to decide them silently.

## Acceptance boundary

This doctrine is accepted only while all of the following remain true:

1. The human belief, core promise, durable Learner Agent unit, and non-negotiable learner protections are explicit.
2. Product doctrine, canonical language, operational contracts, research, roadmap decisions, observations, and derived summaries have named owners.
3. Every material empirical or strategic claim can be assigned to one of the five claim classes.
4. Founder commitments are presented as normative choices rather than scientific findings.
5. Evidence-grounded principles preserve sources, scope, limitations, and counterevidence.
6. Product hypotheses name observable outcome channels and require disconfirming conditions and stop gates before consequential claims.
7. Strategic first-proof constraints are distinguishable from the full vision and from universal learning truth.
8. Agent Actions, assistance, exposure, conversation, engagement, and apparent confidence cannot become learner capability without the independent evidence path.
9. Motivation, Persona continuity, voice, and relationship remain bounded by transparency, consent, learner control, human connection, and anti-dependency rules.
10. Deferred architecture, permanent business-model, market, and implementation choices remain outside doctrine.
11. Revenue, growth, notification, retention, analytics, and access mechanisms remain compatible with learner independence under the Growth-Incentive Compatibility Contract.
12. Null, negative, attrition, correction, accessibility, safety, and subgroup evidence cannot be discarded or reclassified to protect the product story.
13. `README.md`, product contracts, and roadmap artifacts remain aligned with this doctrine or explicitly identify themselves as historical donor material.

If an acceptance condition fails, the conflicting claim or derived artifact must be corrected, narrowed, deferred, or versioned before the doctrine can guide further implementation.
