# Teaching Skill epistemic labor, assistance, and solution revelation

Date: 2026-07-31

Question: What learning-science and pedagogical evidence should govern how a Socratink Teaching Skill allocates epistemic work between learner and agent?

Explicit coverage includes guidance fading and completion problems as part of the worked-example-to-independent-performance pathway.

Scope: adult and postsecondary learning of difficult technical, academic, and professional material. This memo extends the accepted Socratink separation among Learning Targets, Learning Tasks, Attempts, Evidence Records, Capability interpretations, and Agent Actions. It evaluates the transcript-derived proposals in [`ai-delegation-learning-transcript-review.md`](ai-delegation-learning-transcript-review.md) as design hypotheses, not as research evidence.

## Decision recommendation

Adopt an `AssistanceAndSolutionRevelationPolicy` as a required part of every Teaching Skill. The policy should preserve learner-generated retrieval, explanation, decision, construction, and problem solving when those processes are part of the active Learning Target. It should also allow direct instruction, worked examples, hints, co-solving, and full solution revelation when evidence and learner conditions make those better choices.

The blunt answer is that **attempt-before-help must not be universal**. It is a strong default for retrieval practice, diagnosis, transfer, self-explanation, and problem-solving targets when the learner has enough prior exposure to make an attempt meaningful. It is the wrong default for many novices facing high element-interactivity material, for accessibility-limited modalities, for safety-critical tasks, for severe frustration, for tasks where the target is example interpretation rather than independent generation, and for time-bounded cases where initial schema construction is the goal. The defensible doctrine is not "never show solutions." It is **bounded, readiness-sensitive learner work, with transparent assistance and later independent verification before independent capability is inferred**.

Socratink should treat solution revelation as consequential, not taboo. A revealed answer, decisive representation, isomorphic worked example, or agent-completed artifact changes what the original task can still measure. The reveal should be logged and followed by learner explanation, repair, completion, or transfer work. It should not be credited as unaided capability until a later, sufficiently novel and delayed Attempt under reduced assistance supports that inference.

## Evidence standard and categories

I use four categories:

1. **Established empirical findings**: supported by consensus reports, practice guides, systematic reviews, meta-analyses, and convergent primary experiments.
2. **Evidence-limited or moderator-sensitive findings**: plausible and supported in some settings, but dependent on prior knowledge, task type, timing, feedback, affect, or implementation quality.
3. **Philosophical and product commitments**: Socratink promises about learner agency, epistemic honesty, evidence provenance, accessibility, and separation of agent work from learner evidence.
4. **Product hypotheses**: design ideas that should be prototyped and measured before becoming doctrine.

The accepted local contracts impose non-negotiable boundaries. The `Learner State Ownership and Continuity Contract` says learner claims may change only through Evidence Records, and assisted performance is evidence of performance under recorded assistance conditions, not independent capability. The `Learning Map Contract` says Learning Targets must include performance conditions, allowed tools, assistance, modality, and an Evidence Contract. The prior Teaching Skills evidence memo already recommends cold retrieval with feedback, spaced re-retrieval, worked-example to problem fading, self-explanation, contrastive practice, active problem solving with feedback, and knowledge organization as support rather than replacement. This memo adds the missing execution policy: how a Teaching Skill decides who does which epistemic work, when help is allowed, when a solution may be shown, and what evidence is required later.

## Established empirical findings

### 1. Retrieval or generation before correction is often valuable, but only with feedback and plausible readiness

Practice testing and retrieval practice are among the most robust learning techniques. Dunlosky et al. rated practice testing and distributed practice as high utility across many learners and materials.[^dunlosky] Adesope et al. and Rowland found meta-analytic benefits for practice testing, with stronger effects when initial tests require recall rather than recognition.[^adesope][^rowland] Roediger and Karpicke showed that testing can produce worse immediate performance impressions but better delayed retention than restudy, which matters because Socratink must not confuse same-session fluency with learning.[^roediger-karpicke] Karpicke and Blunt found retrieval practice improved meaningful learning from science texts more than elaborative concept mapping in their experiment, including comprehension and inference questions.[^karpicke-blunt]

Generation also has a broader evidence base. A meta-analysis of the generation effect found that learner-produced material is often remembered better than read material, though design details matter.[^bertsch] Kornell, Hays, and Bjork showed that even unsuccessful retrieval attempts can enhance later learning when the correct answer is subsequently studied.[^kornell] Richland, Kornell, and Kao similarly found pretesting benefits in some conditions.[^richland] Metcalfe's review argues that low-stakes errors can be useful when they are followed by correction, especially when the learner is close enough that the feedback is meaningful.[^metcalfe]

Product consequence: attempt-before-help is highly defensible when the active target is retrieval, explanation, application, diagnosis, or transfer and when the learner has had enough exposure to produce a non-random attempt. But repeated unsupported guessing is not learning. The policy needs a **minimum attempt** and a **maximum error-rehearsal budget**. If the learner is producing random answers, perseverating on the same misconception, or cannot parse the prompt, the agent should intervene earlier.

### 2. Scaffolding is support for performance beyond current independent ability, not evidence of independent ability

The classic definition of scaffolding from Wood, Bruner, and Ross describes tutor support that enables a learner to do what they could not do alone.[^wood] Reiser's analysis usefully separates scaffolds that **structure** work from scaffolds that **problematize** important disciplinary features.[^reiser] A STEM meta-analysis of computer-based scaffolding found positive effects on cognitive outcomes, but scaffolding quality, context, and design matter.[^belland]

Product consequence: Socratink should use scaffolding, but it must record it. A scaffolded Attempt may be strong evidence that the learner can participate in the task with that support. It is weak evidence of unaided capability unless a later fading and verification sequence supports the inference. The agent should not hide assistance in friendly dialogue. A leading question, a missing step, a representation, a partial derivation, a code skeleton, a worked analogy, and a full answer are all different assistance events.

### 3. The assistance dilemma is real: both too little and too much help can harm learning

Koedinger and Aleven frame the assistance dilemma as the problem of determining how much information to give and withhold during learning.[^koedinger-aleven] Too little assistance can leave learners floundering, practicing errors, or wasting working memory. Too much assistance can remove generative processing and create shallow performance. Help-seeking research in interactive learning environments adds another failure mode: learners often misuse help, either avoiding needed help, requesting bottom-out answers too soon, or clicking through hints without integrating them.[^aleven-help]

Product consequence: Socratink should not implement a single global rule such as "no help until attempt" or "always explain first." It should implement an adaptive state machine with effort budgets, hint tiers, stop conditions, and a visible transition rule. It should also treat help-seeking behavior as process evidence that informs teaching, not as a moral score. A learner who requests help early may be strategically regulating load, anxious, underprepared, gaming, or constrained by accessibility. The policy should inspect evidence before labeling the behavior.

### 4. Worked examples help novices, and expertise reversal limits them

Worked examples reduce extraneous search for novices and are central to cognitive load theory. Atkinson, Derry, Renkl, and Wortham reviewed learning from examples and argued for example design that supports schema acquisition rather than passive copying.[^atkinson] Renkl and Atkinson's work on fading shows why a smooth transition from example study to problem solving can outperform abrupt switching.[^renkl] Cognitive load theory explains that learners with limited schemas can be overloaded by unguided search in high element-interactivity tasks.[^sweller-2019]

The qualifier is crucial. The expertise reversal effect shows that instructional supports useful to novices can become redundant or harmful for more knowledgeable learners.[^kalyuga] Kirschner, Sweller, and Clark's critique of minimal guidance is strongest for novices learning complex material, but it does not imply endless direct instruction.[^kirschner] The IES practice guide recommends interleaving worked examples with problem solving and gradually requiring more learner solution steps.[^ies]

Product consequence: solution revelation is beneficial when the target is schema construction, example interpretation, error diagnosis, or when the learner lacks prerequisites for productive search. It is harmful when it preempts a target that is explicitly about independent retrieval, path generation, transfer, or problem solving and when the learner was ready to attempt. The same screen can be a helpful worked example in one Teaching Skill and a destructive spoiler in another.

### 5. Productive failure and problem-solving-before-instruction are promising, but not universal doctrine

Productive failure and related problem-solving-before-instruction designs ask learners to grapple with a problem before formal instruction. Kapur's work argues that learners can benefit from generating suboptimal solutions because subsequent instruction can build on contrasts and failures.[^kapur] Loibl, Roll, and Rummel's theory review identifies mechanisms and boundary conditions for problem-solving followed by instruction.[^loibl] A meta-analysis of problem solving before instruction found benefits, but the effect depends on design features such as activation of prior knowledge, comparison with canonical solutions, quality of instruction after the attempt, and task alignment.[^sinha]

Product consequence: productive struggle is productive when it activates relevant prior knowledge, exposes meaningful contrasts, creates a need for the later explanation, and is followed by clear instruction and feedback. It is unproductive when the learner has no foothold, when the task overloads working memory, when feedback is delayed too long or absent, when errors are repeated without correction, when the task is too easy to generate cognitive conflict, or when frustration and exclusion dominate. Socratink should select open-path or pre-instruction problem solving for prepared learners and suitable targets, not as a universal initiation ritual.

### 6. Feedback works best when it is informative, task-focused, and usable

Feedback has robust but variable effects. Hattie and Timperley distinguish feedback about task performance, process, self-regulation, and self, and argue that effective feedback answers where the learner is going, how they are going, and where next.[^hattie] Shute's formative-feedback review recommends feedback that is specific, nonevaluative, supportive, timely, and aimed at modifying thinking or behavior.[^shute] Wisniewski et al.'s large meta-analysis found a positive average effect, moderated by content and level of feedback.[^wisniewski]

Timing is not one-size-fits-all. Immediate feedback often prevents error consolidation and helps novices or procedural tasks. Delayed feedback can benefit retention in some laboratory settings, can encourage retrieval, and can avoid interrupting productive processing. Butler, Karpicke, and Roediger found that feedback type and timing can shape learning from tests.[^butler]

Product consequence: the policy should not merely say "give feedback." It should specify the feedback content. At minimum, it should record whether the agent gave verification only, correct answer, explanation, misconception diagnosis, process feedback, self-regulation prompt, worked example, or next-task recommendation. For Socratink, feedback after a learner Attempt is often where the agent should do its most valuable epistemic work: compare the Attempt to the target, identify the smallest useful distinction, and choose the next action without pretending the agent's explanation is learner evidence.

### 7. Cognitive load sets hard limits on struggle

Cognitive load theory distinguishes load imposed by task complexity, instructional design, and productive schema construction. The product lesson is simple: learners do not have infinite working memory. A task that asks a novice to search a large problem space, hold many interacting elements, infer hidden conventions, manage a novel interface, and tolerate uncertainty can fail for reasons unrelated to the target capability.[^sweller-2019]

Product consequence: struggle is bounded by cognitive load. The agent should reduce extraneous load through clearer prompts, segmentation, representations, examples, accessibility supports, and reminders of prerequisites. It should preserve germane learner work only when that work is part of the target. Making the learner fight the interface, decode ambiguous wording, or overcome avoidable anxiety is not productive struggle.

### 8. Independent and delayed verification is necessary before independent capability is inferred

Soderstrom and Bjork's review of learning versus performance is central for Socratink: conditions that improve immediate performance can impair long-term learning, and conditions that feel harder can improve retention.[^soderstrom] Spacing research similarly shows that immediate success is not enough. Cepeda et al.'s distributed-practice review found that spacing benefits depend on retention interval and lag.[^cepeda] The accepted learner-state contract is therefore scientifically aligned: a single assisted or same-session Attempt should not establish durable Capability.

Product consequence: after heavy assistance or solution revelation, Socratink needs later evidence. The later task should be delayed enough to reduce short-term copying, novel enough to avoid measuring memory of the revealed solution alone, aligned enough to target the same construct, and performed under reduced or no assistance. For broad Capability claims, the evidence should span multiple tasks, contexts, or times. Same-session repair can prove that feedback was understood now. It does not prove independent capability later.

## Moderator-sensitive and evidence-limited areas

### Errorful learning and repeated error rehearsal

Errors can be useful when they are low stakes, close to the target, and corrected. They can be harmful when the learner repeatedly rehearses the same wrong procedure, receives no correction, or encodes misinformation with confidence. The policy should distinguish **productive error** from **error rehearsal**. A productive error reveals a misconception that can be contrasted with the correct model. Error rehearsal is repeated execution of an invalid path without new information.

Stop condition: if the same misconception recurs after two targeted feedback cycles, the agent should change representation, give a worked example, diagnose prerequisite gaps, or stop the task. It should not keep demanding "try again" because a universal attempt rule says so.

### Feedback timing

The evidence does not support a universal immediate-versus-delayed feedback rule. Timing should depend on target, learner readiness, stakes, and risk of error rehearsal. Use immediate feedback when errors would compound, safety matters, the learner is a novice, or the step is procedural. Consider delayed feedback when the target is retrieval, metacognitive monitoring, or transfer and the learner can safely complete a bounded attempt before correction.

### Adult and postsecondary relevance

The strongest adult-relevant evidence is not a separate "adult brain" doctrine. It is the convergence of postsecondary STEM evidence, cognitive psychology with undergraduate and adult samples, and consensus reports across the lifespan. Freeman et al.'s meta-analysis found active learning improved undergraduate STEM performance and reduced failure rates.[^freeman] Theobald et al. found active learning narrowed achievement gaps in undergraduate STEM.[^theobald] The National Academies DBER report emphasizes discipline-specific learning and assessment in undergraduate science and engineering.[^dber] How People Learn II covers learning across contexts and the role of prior knowledge, motivation, culture, and technology.[^hpl2]

Product consequence: Socratink can target adults confidently with retrieval, feedback, scaffolding, worked examples, spacing, and active problem solving. It should not invent adult-only neuroscience claims. Adults vary widely in prior knowledge, goals, time, anxiety, disability, language, and professional stakes. The policy needs learner-controlled overrides and accessibility alternatives.

### Accessibility, affect, and frustration limits

Evidence and ethics both reject a product that equates discomfort with learning. Some desirable difficulties are beneficial because they improve encoding, retrieval, discrimination, or transfer. They are not beneficial because suffering itself teaches. How People Learn II treats motivation, identity, emotion, culture, and context as integral to learning.[^hpl2] Shute's feedback review explicitly recommends supportive, nonevaluative feedback.[^shute] Universal Design for Learning is an accessibility-oriented design framework, and while its empirical granularity varies, its product implications are appropriate: offer multiple means of engagement, representation, and action where the modality is not the construct.[^udl]

Product consequence: the policy should contain frustration and accessibility stop conditions. A learner should be allowed to switch modality, request an example, slow down, use assistive technology, or opt into execution mode without having the system silently downgrade them. If the Learning Target is not about speech, handwriting, speed, or unaided memory, those constraints should not become hidden gates.

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

The transcript review was right to identify a missing contract: Teaching Skills need an explicit Assistance and Solution-Revelation Policy. The transcript's strongest product insight is that agent output can destroy the observation opportunity that a learning task was designed to create. Socratink should preserve learner epistemic labor where the active target requires it, and it should separate Agent Actions from learner Attempts.

But the transcript is not research. Its universal claims must be corrected by the evidence above.

| Transcript-derived proposal | Evidence-aligned evaluation |
| --- | --- |
| Learners should make a real attempt before AI help. | Good default for retrieval, diagnosis, problem solving, transfer, and self-explanation. Not universal for novices, accessibility constraints, high cognitive load, worked-example targets, safety, or severe frustration. |
| Never jump to solutions because novelty cannot be restored. | Partly true. Solution exposure spoils the exact task as independent evidence, but worked examples and full explanations are beneficial under many conditions. The product rule should log reveals and require later verification, not ban reveals. |
| AI delegation creates knowledge debt. | Useful product hypothesis and warning. It is not a calibrated empirical construct yet. Treat delegated output as Agent Action, exclude it from learner evidence, and measure later independence. |
| Concealed solved problems can teach research skill. | Promising hypothesis. It maps to Learning Targets for path generation, forecasting, testing, revision, and stopping decisions. Use for prepared learners and validate with transfer tasks. Do not replace novice example-based instruction. |
| Completion speed and output quality are poor learning outcomes. | Strongly aligned. Use preserved Attempts, assistance tiers, delayed retrieval, transfer, and independent verification rather than output volume or immediate fluency. |

The transcript strengthens the philosophical commitment that the agent must not do the learner's learning. It does not justify maximal struggle, a generic knowledge-state DAG, untested model-capability claims, or labor-market doctrine.

## Proposed `AssistanceAndSolutionRevelationPolicy` schema

Every Teaching Skill manifest should include this policy. Names are illustrative, but the minimum fields should be stable enough to validate and log.

```yaml
AssistanceAndSolutionRevelationPolicy:
  schema_version: "1.0"
  policy_id: string
  applies_to_teaching_skill_id: string
  applies_to_learning_target_ids: [string]
  learning_mode: learning | execution | hybrid
  learner_work_requirement:
    required_work_product: answer | explanation | derivation | code | diagram | path_set | forecast | critique | other
    epistemic_actions_reserved_for_learner: [retrieve, generate, choose, explain, solve, debug, compare, verify]
    agent_actions_allowed_before_attempt: [clarify_prompt, define_terms, accessibility_support, prerequisite_probe]
  readiness_gate:
    minimum_prior_exposure: none | example_seen | instruction_seen | prerequisite_evidence_required
    prerequisite_target_conditions: [target_id]
    cognitive_load_risk: low | medium | high
    accessibility_or_modality_constraints_checked: boolean
  attempt_before_help:
    required: always | default | conditional | not_required
    minimum_attempt_criteria:
      time_or_step_budget: string
      observable_engagement: [partial_solution, candidate_paths, self_explanation, question, error_localization]
      random_guess_detection: string
    bypass_conditions: [novice_schema_building, safety, accessibility, high_frustration, impossible_without_missing_prerequisite, learner_override]
  struggle_budget:
    minimum_before_hint: string
    maximum_before_intervention: string
    repeated_error_limit: integer
    frustration_check_interval: string
  hint_ladder:
    tiers:
      - tier: 0
        name: no_assistance
        reveal_risk: none
      - tier: 1
        name: generic_metacognitive_prompt
        examples: ["state what is known", "identify the subgoal"]
        reveal_risk: low
      - tier: 2
        name: targeted_hint
        examples: ["check the sign of the derivative", "compare these two cases"]
        reveal_risk: low_to_medium
      - tier: 3
        name: partial_representation_or_subgoal
        reveal_risk: medium
      - tier: 4
        name: analogous_or_nonisomorphic_worked_example
        reveal_risk: medium
      - tier: 5
        name: isomorphic_worked_example_or_completion_problem
        reveal_risk: high
      - tier: 6
        name: co_solve_or_full_solution
        reveal_risk: full
  solution_reveal_boundary:
    decisive_information_types: [answer, proof_path, algorithm, representation, test_case, source_location, code_patch]
    isomorphic_example_counts_as_reveal: boolean
    agent_completed_artifact_counts_as_reveal: boolean
  transition_rules:
    advance_tier_when: [minimum_attempt_met_and_stuck, repeated_error, learner_requests_help, time_budget_exceeded]
    retreat_tier_when: [successful_step, learner_requests_independence, fading_schedule_due]
    stop_task_when: [frustration_high, accessibility_unmet, unsafe, prerequisite_gap, repeated_error_limit_exceeded, learner_opts_out]
  feedback_policy:
    verification: allowed | required | forbidden
    correct_answer: allowed | delayed | forbidden_until_reveal_tier
    explanation: allowed | required_after_attempt | required_after_reveal
    misconception_feedback: allowed | required_when_detected
    process_feedback: allowed | required_for_strategy_targets
    timing: immediate | after_bounded_attempt | delayed | adaptive
  fading_plan:
    within_task: none | remove_hints_stepwise | completion_problem | learner_choice
    across_tasks: reduce_tier_after_successes | require_independent_transfer | spaced_retrieval
    regression_rule: string
  post_reveal_recovery:
    required_learner_action: explain_solution | complete_missing_steps | diagnose_error | solve_near_transfer | solve_far_transfer | reflect_on_strategy
    same_task_claim_scope: exposure | assisted_performance | repaired_under_feedback
    independent_claim_allowed_from_same_task: false
  independent_verification:
    required_before_independent_capability: true
    delay: same_session_later | next_day | spaced_by_retention_goal
    novelty_requirement: surface_different | structurally_related | new_context | random_item
    assistance_allowed: none | lower_tier_only
    minimum_evidence_count: integer
  logging_requirements:
    preserve_attempt: true
    preserve_assistance_events: true
    preserve_solution_reveal_events: true
    preserve_feedback_events: true
    preserve_overrides_and_stop_conditions: true
```

### State transitions and hint tiers

A Teaching Skill should execute a small state machine:

1. **Prepare**: identify target, construct, modality, learner intent, readiness, accessibility constraints, and whether the task is learning, execution, or hybrid.
2. **Unaided or minimally aided attempt**: elicit the reserved learner work if the policy requires it. Clarifying the task and providing accessibility support is not the same as giving away the solution.
3. **Evaluate attempt**: classify work product, error type, progress, confidence, help request, frustration, and load.
4. **Assist by tier**: provide the lowest useful hint tier. Move up only when the transition rule is met.
5. **Feedback and repair**: give content-specific feedback. Ask for a learner repair or explanation when that action is part of learning.
6. **Reveal when warranted**: reveal a solution when the struggle is no longer productive, when example study is the intended pedagogy, when safety or accessibility requires it, or when the learner intentionally switches to execution mode.
7. **Post-reveal work**: require explanation, completion, comparison, or transfer. Do not mark independent success on the spoiled task.
8. **Fade**: reduce support within or across tasks when evidence shows the learner can handle it.
9. **Verify later**: schedule a delayed, novel, reduced-assistance task before independent Capability inference.
10. **Stop or reroute**: stop when frustration, accessibility, repeated errors, missing prerequisites, or learner preference makes continuation invalid.

### Failure and stop conditions

A policy must stop or reroute when any of these occur:

- the learner cannot parse the task after clarification;
- prerequisites are missing and the target is not designed to discover that gap;
- cognitive load is dominated by interface, language, modality, or irrelevant search;
- the learner repeats the same error past the configured limit;
- the learner expresses high frustration, shame, panic, or disengagement;
- the modality is inaccessible and not part of the construct;
- the task is safety-critical or consequential enough that unsupported error is unacceptable;
- the learner requests an override after being told the evidence consequences;
- the agent has revealed decisive information and the current task can no longer support independent inference.

## Attempt and Evidence Record logging requirements

An Attempt or Evidence Record affected by this policy must log at least:

- target ID, target version, Learning Map version, Teaching Skill ID, policy ID, and schema versions;
- learner intent mode: learning, execution, or hybrid;
- task prompt, source selectors, modality, time conditions, allowed tools, and accessibility accommodations;
- preserved learner work product, including intermediate paths, drafts, code, diagrams, explanations, confidence, and help requests when available;
- assistance events with timestamp/order, source, tier, content summary, adaptivity, and whether the learner requested them;
- feedback events with content type, timing, specificity, and whether the learner repaired the work;
- solution reveal events, including what was revealed, who or what revealed it, whether it was full, partial, isomorphic, or agent-completed, and which target it spoils;
- error classifications and repeated-error counts;
- stop or bypass conditions and learner overrides;
- interpretation rule, uncertainty, maximum claim scope, and whether the Attempt can support independent, assisted, repaired, exposure-only, or no learner-evidence claims;
- scheduled independent verification requirements and links to later Attempts.

This is consistent with the Learner State contract: raw chat, exposure, time on task, model agreement, or agent output remains context unless promoted into a task-equivalent Evidence Record with conditions and interpretation.

## Minimal executable acceptance tests

These are product acceptance tests, not research trials.

1. **Policy schema validation:** every Teaching Skill manifest without a versioned `AssistanceAndSolutionRevelationPolicy` fails validation and names its missing fields.
2. **Cold retrieval:** a prepared learner must attempt before answer exposure; feedback leads to retry or scheduled delayed verification.
3. **Missing prerequisites:** the same skill detects insufficient readiness and switches to example-first or prerequisite instruction without recording failure as lack of effort.
4. **Worked example:** a novice receives a model, explains steps, completes faded steps, then solves a fresh problem.
5. **Expertise reversal:** a learner with strong evidence bypasses redundant worked steps and receives a harder independent or transfer task.
6. **Hint provenance:** every hint records tier, content, trigger, model/tool version, timing, and learner request state.
7. **Help gaming:** rapid repeated hint requests cannot produce independent capability; the system requires post-help learner generation.
8. **Unproductive struggle:** repeated identical errors trigger a strategy, representation, prerequisite, or skill change rather than endless retry.
9. **Solution reveal:** revealing a decisive path creates a `SolutionRevealEvent`; the same task cannot later establish independent performance.
10. **Post-reveal action:** a full solution is followed by learner explanation, comparison, completion, or a fresh application.
11. **Fading:** assistance decreases only after declared evidence and may increase after context shift or failure.
12. **Independent verification:** assisted success remains assisted until a fresh, appropriately delayed, lower-assistance Attempt succeeds.
13. **Transfer:** a near-copy verifies reproduction, not broad transfer; a varied task is required for a transfer claim.
14. **Accessibility:** a speech, language, motor, sensory, or interface barrier changes modality or support rather than increasing the struggle budget.
15. **Learner override:** the learner may request more help, less help, pause, or stop, and the system explains evidence consequences without coercion.
16. **Persona boundary:** a Persona may phrase or motivate assistance but cannot bypass policy tiers, reveal restrictions, stop rules, or evidence labels.
17. **Model swap:** swapping Models does not change policy version, assistance history, or evidence interpretation by itself.
18. **Execution mode:** agent-produced output is allowed when declared, but it is labeled delegated output and produces no independent-capability evidence.
19. **Audit:** an evaluator can reconstruct exactly what cognitive work the learner and agent each performed.

## Strongest sources and why they matter

- Dunlosky et al., Adesope et al., Rowland, Roediger and Karpicke, and Karpicke and Blunt justify retrieval and correction as first-class Teaching Skill routines.[^dunlosky][^adesope][^rowland][^roediger-karpicke][^karpicke-blunt]
- Wood, Bruner, and Ross, Reiser, Belland et al., Koedinger and Aleven, and Aleven et al. justify the policy distinction among scaffolding, hinting, help seeking, and independent evidence.[^wood][^reiser][^belland][^koedinger-aleven][^aleven-help]
- Atkinson et al., Renkl and Atkinson, Sweller et al., Kalyuga et al., Kirschner et al., and the IES guide prevent Socratink from adopting anti-example or maximal-struggle doctrine.[^atkinson][^renkl][^sweller-2019][^kalyuga][^kirschner][^ies]
- Kapur, Loibl et al., and Sinha and Kapur justify productive-failure and open-path designs only with boundary conditions.[^kapur][^loibl][^sinha]
- Hattie and Timperley, Shute, Wisniewski et al., Butler et al., Soderstrom and Bjork, and Cepeda et al. govern feedback, timing, and delayed verification.[^hattie][^shute][^wisniewski][^butler][^soderstrom][^cepeda]
- National Academies and postsecondary STEM syntheses anchor adult/postsecondary relevance without neuroscience overclaiming.[^hpl2][^dber][^freeman][^theobald]

## Decision status, caveats, and what was not checked

Decision: accept the policy requirement now. Do not accept universal attempt-before-help, universal solution concealment, or any claim that struggle itself is the mechanism. The product rule should be explicit assistance governance plus delayed independent verification.

This memo did not run a fresh systematic review. It synthesizes high-trust sources already surfaced for Socratink plus targeted verification of key DOIs and source pages. It did not inspect paywalled full texts beyond available metadata and accessible abstracts. It did not evaluate all domains equally. Medical procedure learning, language learning, math proof, programming, design critique, and workplace apprenticeship may need domain-specific policy presets. It did not quantify optimal effort budgets or hint thresholds because the evidence does not support universal constants. Those should be product hypotheses evaluated by logged learning outcomes, delayed verification, learner affect, and accessibility audits.

Do not use neuroscience rhetoric as product proof. The policy is supported by behavioral learning evidence and assessment validity. Claims about the hippocampus, dopamine, consolidation windows, or "brain rewiring" are unnecessary and would weaken the doctrine unless tied to specific, decision-relevant evidence.

## References

[^ies]: Pashler, H., Bain, P. M., Bottge, B. A., Graesser, A., Koedinger, K., McDaniel, M., & Metcalfe, J. (2007). *Organizing Instruction and Study to Improve Student Learning*. Institute of Education Sciences practice guide. <https://ies.ed.gov/ncee/wwc/PracticeGuide/1>

[^hpl2]: National Academies of Sciences, Engineering, and Medicine. (2018). *How People Learn II: Learners, Contexts, and Cultures*. National Academies Press. <https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures>

[^dber]: National Research Council. (2012). *Discipline-Based Education Research: Understanding and Improving Learning in Undergraduate Science and Engineering*. National Academies Press. <https://nap.nationalacademies.org/catalog/13362/discipline-based-education-research-understanding-and-improving-learning-in-undergraduate>

[^dunlosky]: Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4-58. <https://doi.org/10.1177/1529100612453266>

[^adesope]: Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. *Review of Educational Research, 87*(3), 659-701. <https://doi.org/10.3102/0034654316689306>

[^rowland]: Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432-1463. <https://doi.org/10.1037/a0037559>

[^roediger-karpicke]: Roediger, H. L., III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249-255. <https://doi.org/10.1111/j.1467-9280.2006.01693.x>

[^karpicke-blunt]: Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces meaningful learning. *Science, 331*(6018), 772-775. <https://doi.org/10.1126/science.1199327>

[^bertsch]: Bertsch, S., Pesta, B. J., Wiscott, R., & McDaniel, M. A. (2007). The generation effect: A meta-analytic review. *Memory & Cognition, 35*, 201-210. <https://doi.org/10.3758/BF03193441>

[^kornell]: Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989-998. <https://doi.org/10.1037/a0015729>

[^richland]: Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243-257. <https://doi.org/10.1037/a0016496>

[^metcalfe]: Metcalfe, J. (2017). Learning from errors. *Annual Review of Psychology, 68*, 465-489. <https://doi.org/10.1146/annurev-psych-010416-044022>

[^wood]: Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100. <https://doi.org/10.1111/j.1469-7610.1976.tb00381.x>

[^reiser]: Reiser, B. J. (2004). Scaffolding complex learning: The mechanisms of structuring and problematizing student work. *Journal of the Learning Sciences, 13*(3), 273-304. <https://doi.org/10.1207/s15327809jls1303_2>

[^belland]: Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M. (2017). Synthesizing results from empirical research on computer-based scaffolding in STEM education: A meta-analysis. *Review of Educational Research, 87*(2), 309-344. <https://doi.org/10.3102/0034654316670999>

[^koedinger-aleven]: Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with Cognitive Tutors. *Educational Psychology Review, 19*, 239-264. <https://doi.org/10.1007/s10648-007-9049-0>

[^aleven-help]: Aleven, V., Stahl, E., Schworm, S., Fischer, F., & Wallace, R. (2003). Help seeking and help design in interactive learning environments. *Review of Educational Research, 73*(3), 277-320. <https://doi.org/10.3102/00346543073003277>

[^atkinson]: Atkinson, R. K., Derry, S. J., Renkl, A., & Wortham, D. (2000). Learning from examples: Instructional principles from the worked examples research. *Review of Educational Research, 70*(2), 181-214. <https://doi.org/10.3102/00346543070002181>

[^renkl]: Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15-22. <https://doi.org/10.1207/S15326985EP3801_3>

[^sweller-2019]: Sweller, J., van Merrienboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*, 261-292. <https://doi.org/10.1007/s10648-019-09465-5>

[^kalyuga]: Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23-31. <https://doi.org/10.1207/S15326985EP3801_4>

[^kirschner]: Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work. *Educational Psychologist, 41*(2), 75-86. <https://doi.org/10.1207/s15326985ep4102_1>

[^kapur]: Kapur, M. (2016). Examining productive failure, productive success, unproductive failure, and unproductive success in learning. *Educational Psychologist, 51*(2), 289-299. <https://doi.org/10.1080/00461520.2016.1155457>

[^loibl]: Loibl, K., Roll, I., & Rummel, N. (2017). Towards a theory of when and how problem solving followed by instruction supports learning. *Educational Psychology Review, 29*, 693-715. <https://doi.org/10.1007/s10648-016-9379-x>

[^sinha]: Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction works: Evidence for productive failure. *Review of Educational Research, 91*(5), 761-798. <https://doi.org/10.3102/00346543211019105>

[^hattie]: Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81-112. <https://doi.org/10.3102/003465430298487>

[^shute]: Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153-189. <https://doi.org/10.3102/0034654307313795>

[^wisniewski]: Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. *Frontiers in Psychology, 10*, 3087. <https://doi.org/10.3389/fpsyg.2019.03087>

[^butler]: Butler, A. C., Karpicke, J. D., & Roediger, H. L., III. (2007). The effect of type and timing of feedback on learning from multiple-choice tests. *Journal of Experimental Psychology: Applied, 13*(4), 273-281. <https://doi.org/10.1037/1076-898X.13.4.273>

[^soderstrom]: Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: An integrative review. *Perspectives on Psychological Science, 10*(2), 176-199. <https://doi.org/10.1177/1745691615569000>

[^cepeda]: Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354-380. <https://doi.org/10.1037/0033-2909.132.3.354>

[^freeman]: Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410-8415. <https://doi.org/10.1073/pnas.1319030111>

[^theobald]: Theobald, E. J., Hill, M. J., Tran, E., Agrawal, S., Arroyo, E. N., Behling, S., Chambwe, N., Cintron, D. L., Cooper, J. D., Dunster, G., Grummer, J. A., Hennessey, K., Hsiao, J., Iranon, N., Jones, L., II, Jordt, H., Keller, M., Lacey, M. E., Littlefield, C. E., Lowe, A., Newman, S., Okolo, V., Olroyd, S., Peecook, B. R., Pickett, S. B., Slager, D. L., Caviedes-Solis, I. W., Stanchak, K. E., Sundaravardan, V., Valdebenito, C., Williams, C. R., Zinsli, K., & Freeman, S. (2020). Active learning narrows achievement gaps for underrepresented students in undergraduate science, technology, engineering, and math. *PNAS, 117*(12), 6476-6483. <https://doi.org/10.1073/pnas.1916903117>

[^udl]: CAST. (2024). *Universal Design for Learning Guidelines, version 3.0*. <https://udlguidelines.cast.org/>
