# Teaching Skill epistemic labor: pedagogy and learning-science grounding

Date: 2026-07-31

Scope: focused research for Wayfinder issue #8 on how a governed Teaching Skill should allocate cognitive work between learner and agent. This review evaluates attempt-before-help, productive struggle, scaffolding, hints, worked examples, solution revelation, guidance fading, feedback, and later independent verification. It does not select a database, UI, model provider, or universal tutoring algorithm.

## Question

What learning-science and pedagogical evidence should govern how a Socratink Teaching Skill decides:

- what the learner must attempt or generate;
- what the agent may explain, hint, demonstrate, or perform;
- when struggle is productive or unproductive;
- when a worked example or full solution should be revealed;
- how assistance should fade;
- what later evidence is required before independent capability is inferred?

## Central conclusion

Socratink should adopt an explicit `AssistanceAndSolutionRevelationPolicy` for every Teaching Skill, but it should **reject a universal attempt-before-help or never-reveal-solutions rule**.

The defensible rule is:

> Preserve learner-generated cognitive work when it is relevant to the active Learning Target, while adapting guidance to prior knowledge, task complexity, affect, accessibility, time, and evidence. Assistance must be purposeful, recorded, and faded when independent performance is the target. A solution may be revealed when it is instructionally justified, but the reveal changes what later performance can demonstrate and therefore requires a new learner action and, when independence matters, a later unassisted verification task.

This conclusion follows from a converging but moderator-sensitive evidence base:

- retrieval and generation before correction often improve retention and reveal gaps;
- problem solving before instruction can improve conceptual learning and transfer when designed as Productive Failure, especially for older learners and appropriate domains;
- unguided or minimally guided discovery is unreliable, particularly for novices and high-element-interactivity tasks;
- worked examples reduce unnecessary search and support schema acquisition for novices;
- the expertise-reversal effect means support that helps novices can become redundant or harmful for advanced learners;
- scaffolding should be contingent, faded, and transferred to learner responsibility;
- hints and help can improve learning, but learners often misuse, avoid, or game help, creating an assistance dilemma;
- feedback quality and task alignment matter more than a simplistic immediate-versus-delayed rule;
- assisted success is evidence of assisted performance unless later evidence supports transfer to independent performance.

The product implication is not “make learning hard.” It is **protect the right cognitive work, prevent avoidable overload and repeated error rehearsal, and preserve an inspectable path from supported performance to independent reconstruction and transfer.**

## Evidence standard

Priority was given to:

1. systematic reviews and meta-analyses;
2. authoritative practice guides and consensus reports;
3. major theoretical reviews with empirical programs;
4. primary experiments that clarify timing, moderators, or implementation.

The evidence is strongest for retrieval practice, feedback, worked examples for novices, guided active learning, and the need to condition learner claims on assistance. Evidence is promising but more context-sensitive for Productive Failure, exact hint policies, adaptive struggle budgets, and AI-mediated fading in adult self-directed learning.

The video transcript reviewed in [`ai-delegation-learning-transcript-review.md`](ai-delegation-learning-transcript-review.md) is treated as a design provocation, not research evidence.

## Separation of commitments

### Established or strongly convergent findings

1. Active retrieval, generation, explanation, and problem solving can produce stronger learning than passive restudy when prompts and feedback match the desired outcome.
2. Prior knowledge and task complexity moderate the value of guidance.
3. Novices commonly benefit from worked examples and structured guidance in complex domains.
4. Guidance should adapt and often fade as competence increases.
5. Assistance conditions change what a successful performance demonstrates.
6. Exposure to an explanation or solution is not evidence of independent capability.
7. Feedback should address the task, process, or self-regulation needed for improvement rather than merely praise, punish, or announce correctness.
8. Inquiry and exploration are more reliable when guidance is present.

### Moderator-sensitive findings

1. Problem solving before instruction can outperform instruction before problem solving, but benefits depend on fidelity to Productive Failure design, learner age, domain, task, and subsequent consolidation.
2. Unsuccessful retrieval or generation can support later learning when corrective feedback follows and errors are not repeatedly rehearsed without correction.
3. The best timing and granularity of hints depend on the learner, task, knowledge component, and intended evidence.
4. Immediate feedback is not universally superior to delayed feedback or vice versa. The function of feedback and target outcome matter.
5. The optimal rate of fading and threshold for revealing a solution are not universal.

### Philosophical and product commitments

1. Learner effort is not intrinsically valuable. Effort is valuable when it performs cognitive work relevant to the target or produces evidence needed for adaptation.
2. Socratink should not optimize away learner retrieval, explanation, decision, construction, or problem solving when those actions are the target.
3. The agent may perform peripheral work that is not the learning target, provided the division of labor is explicit.
4. Accessibility, dignity, consent, and learner agency constrain every struggle or assistance policy.
5. The learner may request more or less help, but the system must explain what that changes about evidence and route interpretation.

### Product hypotheses requiring validation

1. A machine-readable assistance policy will reduce accidental over-helping and false independent-capability claims.
2. Recording solution exposure will improve later task selection and transfer validity.
3. A transparent hint ladder will help adults regulate assistance without increasing gaming or frustration.
4. Repeated success across decreasing assistance tiers may predict transition toward independence.
5. An Open-Path Problem Lab can improve path generation and strategy evaluation on novel technical problems.

## Finding 1: attempt before help should be conditional, not universal

Retrieval-practice research supports asking learners to reconstruct, solve, or explain before correction. Practice testing has robust benefits over restudy, and generative retrieval usually offers more diagnostic information than recognition. Failed retrieval attempts can also improve subsequent learning when followed by corrective feedback.

However, the evidence does not justify requiring a cold attempt in every interaction:

- A learner with insufficient prerequisite knowledge may have no productive representation from which to begin.
- High-element-interactivity tasks can overwhelm working memory before schemas exist.
- Repeated guessing can rehearse errors or produce frustration without useful diagnostic value.
- A worked example may be the appropriate first instructional move for a novice procedural target.
- Accessibility, anxiety, language burden, fatigue, time limits, or high-stakes safety can justify earlier support.
- Some targets concern comprehension of a new representation or procedure rather than unaided discovery.

Therefore, `attemptBeforeHelp` should be a policy field with conditions, not a constitutional absolute.

Recommended values include:

- `required`: the learner must produce a bounded initial attempt before help;
- `preferred`: ask for an attempt unless readiness, accessibility, or stop conditions justify support;
- `optional`: learner may choose attempt or example-first;
- `not_applicable`: the task begins with instruction, modeling, or exposure by design.

When an attempt is required, the policy must define what counts as a sufficient attempt. Time alone is not enough. A sufficient attempt might be a proposed answer with rationale, a partial derivation, a diagram, candidate approaches, a prediction, or a statement of the exact unknown.

Evidence basis: Dunlosky et al.; Adesope et al.; Rowland; Kornell, Hays, and Bjork; Pashler et al.; the Socratink Teaching Skills evidence review.

## Finding 2: productive struggle is designed, bounded, and followed by consolidation

Productive Failure research provides the strongest correction to both “tell first always” and “never reveal.” Sinha and Kapur's meta-analysis of 53 studies and 166 comparisons found a moderate advantage for problem solving followed by instruction, with stronger effects when implementation matched Productive Failure principles. The same review reports moderators and contrasting trends for younger learners and domain-general skills.

Loibl, Roll, and Rummel argue that problem solving before instruction can activate prior knowledge, make gaps visible, and prepare learners to notice and integrate canonical explanations. Productive failure is not simply leaving someone alone until they succeed. Common design features include:

- a problem that activates relevant prior knowledge but is not readily solvable by the learner's current methods;
- opportunities to generate and compare multiple representations or solution approaches;
- preservation of errors and partial solutions as contrasts for later instruction;
- affective and motivational support;
- a subsequent consolidation phase that explicitly connects learner productions to canonical concepts, methods, and distinctions.

Struggle becomes unproductive when:

- prerequisites are too weak to generate meaningful approaches;
- the task is poorly aligned to the target;
- the learner repeats the same error without informative feedback;
- cognitive load comes from interface, notation, language, or irrelevant search rather than the target construct;
- the learner cannot tell what progress or failure means;
- frustration, shame, fatigue, or accessibility barriers dominate;
- no consolidation or corrective instruction follows;
- the system treats time spent or persistence as mastery.

Socratink should use a bounded `struggleBudget`, not maximize struggle. The budget may include attempt count, time range, error pattern, hint requests, affective self-report, prerequisite evidence, and progress signals. These are routing and instructional features, not direct knowledge sensors.

Evidence basis: Sinha and Kapur 2021; Loibl, Roll, and Rummel 2017; Kapur 2008, 2010, 2014, 2016; Kapur and Bielaczyc 2012; Lazonder and Harmsen 2016; Kirschner, Sweller, and Clark 2006.

## Finding 3: scaffolding requires contingency, fading, and transfer of responsibility

Wood, Bruner, and Ross introduced tutoring as support that enables performance beyond what the learner can currently complete alone. Later scaffolding reviews emphasize three connected properties:

- **contingency**: support responds to the learner's current performance rather than following a fixed script blindly;
- **fading**: support decreases as competence or control increases;
- **transfer of responsibility**: the learner increasingly owns the process.

These properties directly support Socratink's epistemic labor boundary. The goal is not to avoid help. The goal is to use help to make otherwise inaccessible cognitive work possible while preserving a path toward learner control.

Contingency also creates a validity obligation. A model-generated hint is not automatically appropriate because it sounds plausible. The skill needs an observable trigger, an allowed assistance move, and a reason that the move addresses the present obstacle without unnecessarily revealing later steps.

A fixed hint ladder can provide safe bounds, but selection within it should consider:

- target and Knowledge Components;
- learner's prior Attempts and assistance history;
- current error or impasse classification;
- modality and accessibility needs;
- risk of revealing the decisive path;
- time and frustration constraints;
- whether independence, tool use, collaboration, or comprehension is the target construct.

Evidence basis: Wood, Bruner, and Ross 1976; van de Pol, Volman, and Beishuizen 2010; Reiser 2004; Koedinger and Aleven 2007.

## Finding 4: the assistance dilemma is real

Koedinger and Aleven frame the assistance dilemma as deciding how much information or assistance to give versus how much problem solving to require. Cognitive-tutor research shows that both over-assistance and under-assistance can undermine learning. Learners may:

- avoid help when it is needed;
- request help too quickly;
- click through hints to reach an answer;
- game the system;
- fail to apply a hint;
- persist without progress;
- mistake assisted fluency for independent competence.

This means a learner-controlled “show answer” button is not a complete pedagogy, and a system-controlled withholding rule is not a complete pedagogy either.

A Teaching Skill should distinguish:

- `help_request`: learner asks for support;
- `help_offer`: system offers support based on a declared trigger;
- `help_acceptance_or_refusal`: learner choice;
- `help_level`: type and amount of support;
- `help_use`: evidence that the learner incorporated, ignored, or copied the support;
- `post_help_generation`: learner explains, completes, contrasts, or applies after help;
- `help_dependency`: repeated need for the same level on structurally similar tasks.

These events are process traces. They may inform instruction and uncertainty, but cannot become capability claims without a valid Evidence Record and interpretation rule.

Evidence basis: Koedinger and Aleven 2007; Aleven et al. 2003; Aleven et al. 2006; Baker et al. on gaming; the Socratink learner-evidence validity review.

## Finding 5: worked examples and solution revelation are often beneficial

Worked-example research strongly rejects the idea that seeing a solution is inherently anti-learning. For novices in structured domains, worked examples can reduce ineffective means-ends search and focus attention on problem structure, principles, and step rationale. Alternating examples with problems and prompting self-explanation can improve schema acquisition.

The expertise-reversal effect supplies the opposing boundary. Guidance that reduces load for novices can become redundant for more knowledgeable learners, consume attention, and reduce productive problem solving. Teaching Skills therefore need learner- and target-specific example policies.

A solution reveal can be beneficial when:

- the target is initial schema acquisition rather than discovery;
- prerequisite evidence is weak;
- the task has high element interactivity;
- search is consuming effort unrelated to the target;
- errors are repeating without progress;
- a safety, accessibility, time, or affective constraint requires intervention;
- the reveal is followed by explanation, completion, fading, comparison, or a new problem.

A solution reveal can be harmful when:

- the decisive path generation is itself the target;
- the learner has sufficient readiness for a productive attempt;
- help arrives before meaningful generation or diagnosis;
- the learner can copy without processing;
- the same revealed item is later treated as independent evidence;
- the reveal eliminates the novelty required by a later research-like or transfer task.

The correct product object is a `SolutionRevealEvent`, not a moral label. It records what was exposed and limits later inference from that item. When a full solution is revealed, the skill should usually require a post-reveal learner action such as self-explanation, completion of omitted steps, error comparison, reconstruction from memory, or application to a non-isomorphic task.

Evidence basis: Atkinson et al. 2000; Atkinson, Renkl, and Merrill 2003; Renkl and Atkinson 2003; Kalyuga et al. 2003; Sweller 1988; Pashler et al. 2007.

## Finding 6: guidance should fade, but not on a folklore schedule

Completion problems and fading worked-out steps provide an evidence-backed bridge from example study to independent problem solving. Support can move from:

1. complete worked example;
2. worked example with self-explanation;
3. partial example or completion problem;
4. strategic hint;
5. process prompt;
6. independent problem;
7. delayed independent or transfer problem.

This is not a universal linear sequence. A learner may need support to increase again after a context shift, new modality, longer delay, or more complex target. Fading should respond to performance under declared conditions, not to exposure count alone.

A defensible fading rule specifies:

- the evidence required to reduce assistance;
- the evidence or failure pattern that increases assistance;
- the maximum claim supported at each tier;
- whether success must repeat across tasks;
- how novelty and context differ across successive tasks;
- when a delayed verification is scheduled.

Evidence basis: Atkinson, Renkl, and Merrill 2003; Renkl and Atkinson 2003; Koedinger and Aleven 2007; Pashler et al. 2007.

## Finding 7: feedback must produce useful next cognition

Feedback research does not support a single “immediate feedback always” rule. Effective feedback depends on what information it provides, what the learner can do with it, the target, and the task.

For Socratink, corrective feedback should preferably identify:

- the specific missing distinction, step, condition, or misconception;
- what in the learner work supports that diagnosis;
- what remains uncertain or could have an alternative explanation;
- the next learner action: revise, explain, contrast, retry, or schedule delayed retrieval.

Feedback should avoid:

- person-level praise or condemnation as a substitute for task information;
- vague correctness labels without a repair path;
- revealing more of the solution than the policy permits;
- presenting a model interpretation as certain when the transcript, task, or rubric is uncertain;
- closing the target after same-session correction when delayed retention or transfer matters.

Feedback after an error should prevent uncorrected error rehearsal. At the same time, an initial error can be instructionally useful when it makes a misconception or missing distinction available for comparison and correction.

Evidence basis: Hattie and Timperley 2007; Shute 2008; Wisniewski, Zierer, and Hattie 2020; Butler, Karpicke, and Roediger on feedback and repeated testing; Kornell, Hays, and Bjork 2009.

## Finding 8: independent capability requires condition-matched verification

Learning science and assessment validity converge on a critical distinction: instruction and evidence are related but not interchangeable.

A learner who succeeds with a worked example, adaptive hint, co-solving, tool output, or agent solution has produced evidence of performance under that assistance. Independent capability requires an Attempt whose conditions match the independent claim.

When durable retention or transfer matters, the verification should usually include:

- reduced or no assistance;
- a fresh task rather than the revealed item;
- an appropriate delay for the retention claim;
- target-relevant variation in surface features or context;
- preserved work and conditions;
- a declared rubric or interpretation rule;
- uncertainty and counterevidence.

Immediate independent retry can demonstrate same-session repair. It should not automatically establish durable retention. A delayed task is stronger evidence for retention; a structurally related novel task is stronger evidence for transfer. Neither should be generalized beyond its conditions.

Evidence basis: Socratink learner-evidence validity research; National Research Council assessment triangle; Mislevy, Steinberg, and Almond; retrieval and spacing meta-analyses; worked-example fading research.

## Finding 9: accessibility and affect are failure boundaries, not afterthoughts

A struggle policy can exclude learners if it interprets speech burden, disability, language load, interface friction, anxiety, sensory conditions, or time scarcity as desirable difficulty. Construct-irrelevant difficulty should be removed or accommodated rather than protected as epistemic labor.

The learner should have:

- accessible alternative modalities;
- a visible request-more-help path;
- a visible request-less-help path;
- an explanation of what assistance changes about evidence;
- the ability to pause or stop without shame;
- control over whether ordinary interactions become evidence;
- correction paths for transcripts, task interpretations, and inferred obstacles.

Frustration is not proof of productive struggle. Affective data should not be inferred from voice, pause length, facial expression, or typing behavior as though it were a validated internal-state sensor. Direct learner report can inform assistance, but still requires context and should not become a stable trait.

Evidence basis: active-learning and scaffolding research; Socratink voice evidence review; learner-evidence validity contract; accessibility standards and assessment-validity principles.

## Proposed `AssistanceAndSolutionRevelationPolicy`

Every Teaching Skill should expose a versioned policy with at least these fields:

```json
{
  "policyId": "asrp:worked-example-fader-v1",
  "skillVersion": "skill:worked-example-fader-v1",
  "targetVersion": "lt:example-target-v3",
  "intendedConstruct": "independent-procedural-performance",
  "learnerWorkRequirement": {
    "requiredActions": ["predict", "complete", "explain", "solve"],
    "agentMayPerform": ["present-example", "ask-question", "score-with-rubric"],
    "agentMustNotSubstitute": ["final-independent-solution"]
  },
  "attemptBeforeHelp": {
    "mode": "preferred",
    "sufficientAttemptRule": "partial method plus rationale or explicit impasse",
    "exceptions": ["missing-prerequisite", "accessibility", "safety", "time-limit"]
  },
  "struggleBudget": {
    "minAttempts": 1,
    "maxAttemptsWithoutNewInformation": 2,
    "timeRange": "task-specific",
    "progressSignals": ["new-representation", "localized-impasse", "error-revision"],
    "stopSignals": ["repeated-identical-error", "learner-stop", "construct-irrelevant-barrier"]
  },
  "assistanceTiers": [
    "independent",
    "generic-process-prompt",
    "targeted-question",
    "strategic-hint",
    "partial-representation",
    "completion-problem",
    "worked-example",
    "co-solved",
    "full-solution"
  ],
  "tierTransitionRules": {
    "increaseSupportWhen": ["declared-trigger"],
    "fadeSupportWhen": ["declared-evidence"],
    "learnerOverride": "allowed-with-disclosed-evidence-consequence"
  },
  "revealBoundary": {
    "decisiveInformation": ["key-representation", "critical-step", "final-answer"],
    "requiresConfirmation": false,
    "recordSolutionRevealEvent": true
  },
  "postRevealAction": ["self-explain", "contrast-error", "complete-new-step"],
  "independentVerification": {
    "required": true,
    "freshTask": true,
    "delay": "retention-goal-dependent",
    "assistance": "none-or-declared-tools",
    "transferVariation": "target-dependent"
  },
  "feedbackPolicy": {
    "allowedFocus": ["task", "process", "self-regulation"],
    "requiresNextLearnerAction": true,
    "uncertaintyDisclosure": true
  },
  "accessibilityAndStopPolicy": {
    "alternativeModalities": true,
    "learnerStopAlwaysAvailable": true,
    "constructIrrelevantDifficultyMustBeRemoved": true
  },
  "provenance": {
    "evidenceBasis": ["source-ids"],
    "policyAuthor": "agent-or-human",
    "createdByActivity": "activity-id",
    "status": "hypothesized-or-validated"
  }
}
```

Numeric thresholds shown here are illustrative, not doctrine. A skill must justify task-specific thresholds and version them.

## Assistance state transitions

The following states are an available vocabulary, not a mandatory sequence:

```text
independent attempt
  -> generic process prompt
  -> targeted question
  -> strategic hint
  -> partial representation
  -> completion problem
  -> worked example
  -> co-solving
  -> full solution reveal
  -> post-reveal learner generation
  -> faded fresh-task retry
  -> delayed independent verification
```

Rules:

1. A transition must record its trigger, source, time, and assistance content.
2. The system may skip tiers when readiness, accessibility, safety, time, or task structure warrants it.
3. Learners may request a different tier, with the evidence consequence explained.
4. A full solution reveal cannot be undone for that task; later independence needs a fresh task.
5. Successful use of a hint does not prove unaided capability.
6. Repeated failure at one tier should change the instructional plan, not merely repeat the same hint.
7. Assistance may increase after context shift or delay; fading is not monotonically guaranteed across all tasks.

## Required Attempt and Evidence Record fields

When a Teaching Skill elicits learner work, preserve:

- target, skill, task, policy, rubric, and map versions;
- learner work product and relevant process trace;
- modality and accessibility accommodations;
- prior exposure to the task or isomorphic examples;
- whether an attempt preceded help and what counted as the attempt;
- assistance tier, source, content, timing, amount, adaptivity, and learner request state;
- every decisive hint or `SolutionRevealEvent`;
- post-help learner action;
- time and attempt count as conditions, not mastery signals;
- interpretation rule, uncertainty, counterevidence, and maximum claim scope;
- whether the record informs immediate routing, assisted performance, independent performance, retention, or transfer;
- required future verification.

Agent-generated text, code, explanation, or solution remains Agent Action output. It may be attached as assistance provenance but cannot become the learner work product.

## Teaching Skill selection implications

The Learner Agent should not select a Teaching Skill only from content type or learner preference. Selection must consider:

- active Learning Target and intended construct;
- prerequisite and current evidence;
- learner's assistance history on structurally related targets;
- whether the target requires retrieval, schema acquisition, discrimination, procedure, explanation, path generation, or transfer;
- task element interactivity and domain structure;
- modality and accessibility;
- time, stakes, affective self-report, and learner preference;
- availability of a valid task, rubric, and independent-verification path;
- Persona influence only within the same assistance and evidence boundaries.

Examples:

- weak prerequisite evidence plus novice procedural target favors a worked example or completion problem;
- established schema plus stale evidence favors cold retrieval;
- confusable cases favor contrastive discrimination;
- sufficiently prepared learner plus path-generation target may favor an Open-Path Problem Lab;
- repeated hint dependence favors a new representation, prerequisite target, or changed Teaching Skill rather than identical retry;
- a learner-requested full answer may be honored in execution or exploration mode, but it cannot be credited as independent learning evidence.

## Evaluation of transcript-derived proposals

The transcript's strongest claim, that AI can remove the process through which the learner gains knowledge and judgment, is consistent with Socratink's evidence boundaries and active-learning research.

The transcript correctly sharpens these product needs:

- protect learner-generated work when it is the target;
- record solution exposure;
- distinguish agent output from learner capability;
- train path generation and strategy evaluation;
- consider the future cost of dependence.

The transcript overreaches when it implies:

- attempt-before-help should be universal;
- a learner should never see a solution;
- all struggle builds research skill;
- the knowledge structure is a single DAG;
- current model limitations or labor-market forecasts are pedagogical truth.

The corrected principle is productive, bounded, readiness-sensitive learner work with contingent assistance and later verification.

## Decision recommendation

Adopt the following founder decision for issue #8:

> A Teaching Skill is a versioned instructional procedure that declares an explicit division of epistemic labor between learner and agent. It must expose a versioned Assistance and Solution-Revelation Policy specifying learner work, permissible agent support, attempt-before-help conditions, productive-struggle bounds, assistance tiers, reveal boundaries, feedback, fading, accessibility and stop conditions, post-help generation, and independent verification. Assistance is instructionally legitimate but changes what performance demonstrates. Agent-performed or revealed work remains explicit and cannot be credited as independent learner capability.

Important boundary:

> The policy adapts guidance; it does not worship struggle. No universal rule requires an unaided attempt, forbids worked examples, or delays help past the point of useful cognition.

## Minimal executable acceptance tests

1. **Cold retrieval:** a prepared learner must attempt before answer exposure; feedback leads to retry or scheduled delayed verification.
2. **Missing prerequisites:** the same skill detects insufficient readiness and switches to example-first or prerequisite instruction without recording failure as lack of effort.
3. **Worked example:** a novice receives a model, explains steps, completes faded steps, then solves a fresh problem.
4. **Expertise reversal:** a learner with strong evidence bypasses redundant worked steps and receives a harder independent or transfer task.
5. **Hint provenance:** every hint records tier, content, trigger, model/tool version, timing, and learner request state.
6. **Help gaming:** rapid repeated hint requests cannot produce independent capability; the system requires post-help learner generation.
7. **Unproductive struggle:** repeated identical errors trigger a strategy, representation, prerequisite, or skill change rather than endless retry.
8. **Solution reveal:** revealing a decisive path creates a `SolutionRevealEvent`; the same task cannot later establish independent performance.
9. **Post-reveal action:** a full solution is followed by learner explanation, comparison, completion, or a fresh application.
10. **Fading:** assistance decreases only after declared evidence and may increase after context shift or failure.
11. **Independent verification:** assisted success remains assisted until a fresh, appropriately delayed, lower-assistance Attempt succeeds.
12. **Transfer:** a near-copy verifies reproduction, not broad transfer; a varied task is required for a transfer claim.
13. **Accessibility:** a speech, language, motor, sensory, or interface barrier changes modality or support rather than increasing the struggle budget.
14. **Learner override:** the learner may request more help, less help, pause, or stop, and the system explains evidence consequences without coercion.
15. **Persona boundary:** a Persona may phrase or motivate assistance but cannot bypass policy tiers, reveal restrictions, stop rules, or evidence labels.
16. **Model swap:** swapping Models does not change policy version, assistance history, or evidence interpretation by itself.
17. **Execution mode:** agent-produced output is allowed when declared, but it is labeled delegated output and produces no independent-capability evidence.
18. **Audit:** an evaluator can reconstruct exactly what cognitive work the learner and agent each performed.

## Major evidence gaps

1. Adult self-directed AI tutoring has less direct evidence than classroom, laboratory, and conventional intelligent-tutoring contexts.
2. Exact struggle budgets and hint thresholds are task- and population-specific.
3. Inferring frustration or readiness from passive traces risks construct error and subgroup bias.
4. Assistance fading models need domain-specific calibration.
5. Far transfer from path-generation practice to real research performance is not established.
6. Persona effects on help seeking, persistence, dependence, and solution requests require direct study.
7. The effect of voice conversation on help timing and perceived pressure is not well established.
8. Delayed independent verification schedules for complex professional tasks are not settled.

## Caveats

- Productive Failure is a designed sequence, not unguided abandonment.
- Worked-example effects are strongest in structured domains and novice learning; complex ill-structured tasks need different supports.
- Meta-analytic averages do not determine the best policy for an individual learner or target.
- Assistance trace data can inform but not read mental state directly.
- A transparent policy can still encode poor pedagogical assumptions; it needs outcome evaluation and revision.
- Learning outcome measures should prioritize delayed reconstruction, appropriate application, and transfer rather than engagement or immediate completion.

## What was not checked

- proprietary tutoring-system datasets and unpublished negative results;
- current commercial AI tutor assistance policies;
- domain-specific pedagogy for every target area;
- minors, special education, clinical remediation, or high-stakes licensure as separate populations;
- real-time affect detection, which should not be presumed valid;
- exact numeric thresholds for time, attempts, hints, fading, or delay;
- production privacy and security architecture for process traces.

## Strongest sources and why they matter

1. Koedinger, K. R., & Aleven, V. (2007). “Exploring the Assistance Dilemma in Experiments with Cognitive Tutors.” Defines the central help-versus-problem-solving tradeoff and reviews tutor experiments. <https://doi.org/10.1007/s10648-007-9049-0>
2. Aleven, V., Stahl, E., Schworm, S., Fischer, F., & Wallace, R. (2003). “Help Seeking and Help Design in Interactive Learning Environments.” Major review of learner help seeking and system design. <https://doi.org/10.3102/00346543073003277>
3. Wood, D., Bruner, J. S., & Ross, G. (1976). “The Role of Tutoring in Problem Solving.” Foundational scaffolding account. <https://doi.org/10.1111/j.1469-7610.1976.tb00381.x>
4. van de Pol, J., Volman, M., & Beishuizen, J. (2010). “Scaffolding in Teacher-Student Interaction: A Decade of Research.” Review emphasizing contingency, fading, and transfer of responsibility. <https://doi.org/10.1007/s10648-010-9127-6>
5. Sinha, T., & Kapur, M. (2021). “When Problem Solving Followed by Instruction Works: Evidence for Productive Failure.” Meta-analysis of 53 studies and 166 comparisons, including moderators. <https://doi.org/10.3102/00346543211019105>
6. Loibl, K., Roll, I., & Rummel, N. (2017). “Towards a Theory of When and How Problem Solving Followed by Instruction Supports Learning.” Explains preparation and consolidation mechanisms and boundary conditions. <https://doi.org/10.1007/s10648-016-9379-x>
7. Kapur, M. (2008). “Productive Failure.” Foundational empirical formulation. <https://doi.org/10.1080/07370000802212669>
8. Kapur, M. (2016). “Examining Productive Failure, Productive Success, Unproductive Failure, and Unproductive Success in Learning.” Clarifies that failure is not automatically productive. <https://doi.org/10.1080/00461520.2016.1155457>
9. Kapur, M., & Bielaczyc, K. (2012). “Designing for Productive Failure.” Identifies design principles rather than treating struggle as absence of teaching. <https://doi.org/10.1080/10508406.2011.591717>
10. Lazonder, A. W., & Harmsen, R. (2016). “Meta-Analysis of Inquiry-Based Learning: Effects of Guidance.” Shows guidance matters in inquiry learning. <https://doi.org/10.3102/0034654315627366>
11. Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). “Why Minimal Guidance During Instruction Does Not Work.” Important argument and evidence synthesis on novice guidance and cognitive architecture. <https://doi.org/10.1207/s15326985ep4102_1>
12. Atkinson, R. K., Derry, S. J., Renkl, A., & Wortham, D. (2000). “Learning from Examples.” Review of worked-example instructional principles. <https://doi.org/10.3102/00346543070002181>
13. Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). “Transitioning from Studying Examples to Solving Problems.” Tests self-explanation and fading worked-out steps. <https://doi.org/10.1037/0022-0663.95.4.774>
14. Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). “The Expertise Reversal Effect.” Establishes that guidance benefits depend on learner expertise. <https://doi.org/10.1207/S15326985EP3801_4>
15. Hsu, C.-Y., Kalyuga, S., & Sweller, J. (2015). “When Should Guidance Be Presented in Physics Instruction?” Directly tests timing of guidance. <https://doi.org/10.1037/arc0000012>
16. Pashler, H., et al. (2007). *Organizing Instruction and Study to Improve Student Learning.* Authoritative IES practice guide supporting spacing, retrieval, worked examples, and explanatory questions. <https://ies.ed.gov/ncee/wwc/PracticeGuide/1>
17. Dunlosky, J., et al. (2013). “Improving Students' Learning with Effective Learning Techniques.” Broad review grading retrieval and distributed practice highly. <https://doi.org/10.1177/1529100612453266>
18. Adesope, O. O., Trevisan, O. A., & Sundararajan, N. (2017). “Rethinking the Use of Tests.” Meta-analysis of practice testing. <https://doi.org/10.3102/0034654316689306>
19. Rowland, C. A. (2014). “The Effect of Testing Versus Restudy on Retention.” Meta-analysis of the testing effect. <https://doi.org/10.1037/a0037559>
20. Kornell, N., Hays, M. J., & Bjork, R. A. (2009). “Unsuccessful Retrieval Attempts Enhance Subsequent Learning.” Supports errorful generation when followed by correction. <https://doi.org/10.1037/a0015729>
21. Hattie, J., & Timperley, H. (2007). “The Power of Feedback.” Influential synthesis of feedback levels and functions. <https://doi.org/10.3102/003465430298487>
22. Shute, V. J. (2008). “Focus on Formative Feedback.” Review of effective formative feedback characteristics and moderators. <https://doi.org/10.3102/0034654307313795>
23. Wisniewski, B., Zierer, K., & Hattie, J. (2020). “The Power of Feedback Revisited.” Meta-analysis reinforcing that feedback effects depend on information and implementation. <https://doi.org/10.3389/fpsyg.2019.03087>
24. Chi, M. T. H., & Wylie, R. (2014). “The ICAP Framework.” Distinguishes passive, active, constructive, and interactive engagement. <https://doi.org/10.1080/00461520.2014.965823>
25. National Research Council (2001). *Knowing What Students Know.* Establishes cognition-observation-interpretation coherence for evidence claims. <https://doi.org/10.17226/10019>
26. Mislevy, R. J., Steinberg, L. S., & Almond, R. G. (2003). “On the Structure of Educational Assessments.” Supports explicit claims, tasks, evidence, and inference rules. <https://doi.org/10.1207/S15366359MEA0101_02>
