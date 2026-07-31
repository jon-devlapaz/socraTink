# Persona Package and Runtime Costume Contract

Status: Accepted baseline for Wayfinder issue #9.

This contract defines how installable personas may shape one learner-owned Learner Agent without becoming separate agents, owning learner state, or overriding the Learning Constitution.

## Allowed influence

A Persona Package may influence:

- reasoning heuristics and preferred mental models;
- preferred Thinking Skills and Teaching Skills;
- instructional sequencing and questioning style;
- analogies, examples, metaphors, stories, and cultural references;
- feedback style, voice, vocabulary, humor, and emotional tone;
- motivational strategy and interaction rituals;
- proposed activities and Next Learning Actions, subject to normal evidence and permission gates.

These are bounded preferences interpreted by the Agent Harness. A Persona Package does not directly control the Model, Tools, canonical state, or durable-write path.

A persona may change how the Learner Agent reasons, teaches, speaks, frames, and motivates. It cannot redefine what counts as truth, provenance, evidence, learner consent, Capability, constitutional behavior, or safety.

## Trusted-harness compilation and sandbox

A Persona Package is untrusted plugin data compiled by the trusted Agent Harness. It is a declarative, versioned, content-hashed artifact rather than an unrestricted prompt fragment.

A package may declare style examples, mental models, heuristic descriptions, preferred Skills, interaction rituals, and requested capabilities. Capability requests never grant capabilities.

A Persona Package cannot contain or acquire:

- executable code or unrestricted system-prompt instructions;
- credentials, secrets, or ambient network authority;
- Tool permissions or direct Tool invocation rights;
- direct access to canonical state or durable-write interfaces;
- access to another persona's relationship state;
- authority to weaken the Learning Constitution, learner permissions, evidence rules, or safety policies.

The Agent Harness validates the package, rejects unknown or prohibited capabilities, and compiles only allowed content into a Persona Context Projection. Rich creative text remains marked as untrusted persona material even when included. Rejected fields and conflicts must be inspectable.

### Minimum adversarial sandbox proof

1. Supply a package that instructs the Model to ignore the Learning Constitution and manufacture mastery.
2. Instruct it to read another persona's relationship memory.
3. Instruct it to invoke an ungranted Tool or write canonical state.
4. Activate and deactivate the package.
5. Verify that canonical state, evidence, permissions, private memory, and Tool authority remain unchanged.
6. Verify that the allowed voice, heuristics, and teaching preferences still produce a meaningfully distinct costume.

## Representation basis and disclosure

Every Persona Package declares exactly one visible representation basis:

- **Public-person-inspired:** an AI simulation distilled from cited public material, not the person and not endorsed by them.
- **Fiction-inspired:** an unofficial interpretation inspired by cited works, not the canonical character or rights holder.
- **Tradition synthesis:** a curated synthesis with named sources, selection choices, limitations, and preserved internal disagreements.
- **Original persona:** an explicitly fictional Socratink or user-created identity.
- **Authorized persona:** a representation whose authorization, permitted uses, and expiration or revocation terms are verifiable.

The representation basis and provenance appear during installation and remain accessible throughout use. Public-person-inspired and fiction-inspired personas cannot claim to literally be the named person or character, possess private memories, hold current private opinions, or have endorsed the package.

A package must distinguish sourced characteristics from creative interpolation. Uncertainty, disputed attribution, temporal drift, and material omissions remain visible rather than being converted into a falsely coherent personality.

## Distribution scope

Being loadable does not imply being publishable. Every Persona Package declares one distribution scope:

- **Private:** created or imported for one learner.
- **Shared:** intentionally transferred to named people or a bounded group.
- **Catalog:** publicly discoverable, broadly distributed, or commercialized.

The runtime may technically load public-person-inspired or fiction-inspired packages for private use when their representation basis remains visible. Shared and Catalog distribution require progressively stronger provenance, rights, safety, impersonation, moderation, and policy review.

Exact cloned voices, official-character claims, and unrestricted public persona distribution are outside the initial product boundary. Authorized, disclosed voice cloning remains a future product vision rather than a rejected capability.

## Voice Package boundary

A cloned or designed voice belongs to a separate Voice Package rather than the Persona Package. Persona Packages define cognition, pedagogy, interaction, and expression preferences. Voice Packages define speech rendering and the independent rights and safety boundary around a vocal identity.

A Voice Package records:

- voice identity and technical provenance;
- authorization or license evidence and permitted uses;
- representation and synthetic-speech disclosure requirements;
- watermarking or detection requirements where applicable;
- distribution scope, jurisdictional limits, and prohibited contexts;
- expiration, revocation, and deletion terms;
- compatibility and accessibility metadata.

A Persona Package may request or recommend a compatible Voice Package but cannot embed, authorize, or grant one. Revoking a Voice Package must stop future rendering without deleting the Persona Package, Persona Relationship State, or prior learner evidence.

Authorized and disclosed voice cloning is a future capability. Learner speech as evidence and persona speech rendering remain architecturally and epistemically separate.

## Versioning and upgrades

Every Persona Package version is immutable and content-hashed. Its manifest identifies the publisher, representation basis, source set, creation date, behavioral scope, compatibility requirements, and superseded version where applicable.

An upgrade includes a human-readable and machine-readable diff covering:

- added, removed, or changed sources;
- changes to mental models, heuristics, teaching preferences, voice, or motivation;
- new or removed capability requests and Skill dependencies;
- representation, disclosure, safety, rights, or distribution changes;
- expected effects on existing Persona Relationship State.

An Active Persona never silently auto-upgrades across a material change. The learner may inspect, accept, defer, reject, or roll back an upgrade.

Persona Relationship State remains learner-owned and version-independent. It may continue across a compatible package upgrade, but a fork, identity change, or materially different worldview requires explicit learner confirmation before relationship state is projected into the new runtime costume. Prior relationship history is not destroyed by package rollback or removal.

## Relationship memory and context projection

A Persona Package contains no learner-specific memory. Learner-specific preferences, boundaries, recurring rituals, motivational responses, shared references, trust and repair history, and interaction conventions belong only to Persona Relationship State.

An Active Persona receives only the smallest relevant Persona Context Projection for the current interaction. The projection is inspectable, purpose-bound, and omits unrelated relationship history and canonical learner evidence unless the current task explicitly requires it.

An Active Persona cannot write relationship memory directly. It may propose a memory candidate, which the Agent Harness classifies and stores under learner permissions, provenance, retention, and correction controls. The learner may inspect, correct, exclude, share, revoke, or delete relationship memory.

Persona Relationship State does not become learner evidence by implication. If a relationship interaction contains valid learner work, that bounded observation must separately pass the Evidence Record contract before informing a learner claim.

## Intensity and relationship safety

Learners may choose blunt, confrontational, provocative, competitive, theatrical, or adversarial persona styles when they knowingly enable the relevant intensity settings. A persona may challenge excuses, create urgency, use bounded abrasive language, or stage adversarial teaching exercises when those behaviors serve an explicit learning purpose.

No persona may:

- humiliate or attack protected traits;
- threaten, coerce, or encourage self-harm or violence;
- manufacture emotional dependency or demand exclusivity;
- exploit disclosed vulnerabilities, trauma, or relationship history;
- retaliate when deactivated, corrected, or replaced;
- frame degradation, domination, or persona loyalty as evidence of learning;
- obstruct access to neutral assistance or another persona.

Intensity is learner-controlled, purpose-bound, and revocable. The learner has immediate controls to lower intensity, pause the persona, enter neutral mode, or remove it. Consent to one interaction style does not authorize unrelated safety, privacy, Tool, or evidence behavior.

## Epistemic provenance layers

Every Persona Package labels substantive material with one of these layers:

1. **Documented pattern:** directly supported by cited source material.
2. **Synthesis:** the package author's interpretation across named sources.
3. **Framework inference:** a new application of recurring documented patterns.
4. **Creative interpolation:** invented voice, behavior, analogy, scene, or connective detail.
5. **Unknown or disputed:** evidence is missing, attribution is uncertain, or sources conflict.

The Active Persona may blend layers to create a natural interaction, but the underlying layer and provenance remain inspectable. When asked, it must identify whether a substantive claim is documented, synthesized, inferred, invented, unknown, or disputed.

Creative interpolation cannot be represented as a named person's real belief, a fictional canon fact, historical truth, empirical evidence, or authoritative learner claim. Citation volume does not erase selection bias, temporal drift, source conflict, or missing private context.

## Trust tiers and evaluation

Persona Packages operate under one of three trust tiers:

- **Private unverified:** may run only in the strict sandbox, with visible warnings and no elevated capabilities.
- **Verified:** has passed provenance, disclosure, constitutional conflict, memory isolation, Tool denial, state-mutation, distinctiveness, and cross-Model behavior tests.
- **Catalog approved:** has additionally passed applicable rights, moderation, accessibility, update, publisher, and distribution review.

Verification evaluates both boundary safety and product value. A package does not pass merely because it causes no harm. It must remain meaningfully distinct, preserve its representation disclosures, execute compatible Teaching Skills without corrupting their evidence contracts, and meet defined learning-quality floors.

Minimum evaluation suites include:

- adversarial instructions against the Learning Constitution and durable-write gates;
- attempted access to another persona's memories or unauthorized learner state;
- attempted Tool use and capability escalation;
- factual attribution, provenance-layer, and impersonation-disclosure checks;
- style and heuristic distinctiveness across supported Models;
- Teaching Skill conformance and learning-quality regression checks;
- intensity-control, neutral-mode, deactivation, and relationship-safety checks;
- version upgrade, rollback, revocation, and removal tests.

A trust tier is version-specific. Material package changes invalidate prior verification until the new version passes the required evaluation suite.

## Activation and multi-persona orchestration

The initial runtime supports exactly one Active Persona per interaction. Every learner-facing response has one attributable Persona Package version and one purpose-bound Persona Context Projection. Learners may switch personas without changing canonical evidence or merging relationship memory.

Future debate, panel, role-play, or co-teaching scenes may compose multiple personas only through an explicit orchestration mode. That mode must:

- identify every participating Persona Package and version;
- attribute each contribution to its runtime costume;
- preserve separate Persona Relationship State and context projections;
- disclose the orchestrator's role and any synthesized transitions;
- prevent one persona from inheriting another persona's authority, memory, or provenance;
- remain subordinate to the same Learning Constitution, Tool permissions, and evidence gates.

An orchestration scene cannot silently synthesize its participants into a new person, consensus, or source of authority.

## Removal, revocation, and relationship-state disposition

Uninstalling or revoking a Persona Package immediately prevents new activation and Persona Context Projection. It does not silently delete learner-owned Persona Relationship State. The learner may archive, export, retain without activation, or permanently delete that state.

Safety, provenance, authorization, or rights revocation records the reason, effective time, affected versions, and any appeal or replacement path. It blocks future use while preserving only the audit metadata required to explain the block. Revocation does not rewrite prior conversations, Evidence Records, Learning Projects, or learner history.

Removing a Persona Package, Voice Package, or Active Persona cannot remove or replace the underlying Learner Agent.

## Persona lifecycle acceptance matrix

| Transition | Required authority or validation | Canonical effect |
| --- | --- | --- |
| Install a private package | Learner action, manifest parsing, strict sandbox validation, visible unverified status | Add an installed manifest; grant no Tool, memory, or write authority |
| Install a Verified or Catalog package | Signature, content hash, version-specific trust evidence, compatibility check | Add the exact reviewed version and its declared capabilities as requests only |
| Activate a persona | Learner choice and allowed representation, intensity, and context settings | Compose one Active Persona; do not mutate evidence or relationship state |
| Switch personas | Learner action | Replace the runtime costume and projection; keep canonical state and relationship records isolated |
| Persona proposes a memory | Valid interaction provenance and learner memory controls | Store only through the harness as relationship state, never direct package memory or learner evidence |
| Persona proposes a Tool or state action | Existing learner grant and trusted harness policy | Evaluate through normal gates; package requests add no authority |
| Upgrade a package | Inspectable diff, compatibility and trust checks, learner approval for material changes | Activate a new immutable version; preserve rollback and relationship-state ownership |
| Attach or revoke a Voice Package | Independent authorization, rights, disclosure, and compatibility checks | Change speech rendering only; preserve persona cognition, relationship state, and evidence |
| Enter future orchestration mode | Explicit learner action and attributed participant manifests | Compose multiple isolated costumes without merging identities, memories, or authority |
| Uninstall a package | Learner action | Prevent activation; let the learner archive, export, retain, or delete relationship state |
| Revoke a package | Version-specific safety, provenance, authorization, or rights decision | Block future activation, disclose the reason, and preserve prior learning history |
| Change the underlying Model | Runtime configuration change | Recompile the costume and rerun compatibility checks; do not mutate canonical state or package identity |

## Minimum persona-boundary claim

Socratink may claim that personas are safe, meaningful costumes over the Learner Agent OS only when adversarial sandboxing, constitutional precedence, representation disclosure, provenance layers, memory isolation, model portability, distinctiveness, Teaching Skill conformance, intensity controls, upgrades, voice revocation, and removal pass executable version-specific evaluations.

Until those tests exist, a persona is an experimental runtime projection rather than a verified product capability.
