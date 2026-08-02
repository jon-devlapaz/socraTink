# MemoHarness agent-harness experience alpha review

Date: 2026-08-02

Primary source: Yue Huang, Wenjie Wang, Han Bao, Yuchen Ma, Xiaonan Luo, Yi Nian, Haomin Zhuang, Zheyuan Liu, Yue Zhao, and Xiangliang Zhang, *MemoHarness: Agent Harnesses That Learn from Experience*, arXiv:2607.14159v1, submitted 2026-07-14. <https://arxiv.org/abs/2607.14159>

Evidence status for Socratink: **alpha**. This is an important early signal about adaptive agent harnesses, not settled product doctrine.

## Paper identity and status

- **Title:** *MemoHarness: Agent Harnesses That Learn from Experience*.
- **Authors:** Yue Huang, Wenjie Wang, Han Bao, Yuchen Ma, Xiaonan Luo, Yi Nian, Haomin Zhuang, Zheyuan Liu, Yue Zhao, and Xiangliang Zhang.
- **Institutions:** University of Notre Dame, LMU Munich, and University of Southern California.
- **Version:** arXiv:2607.14159v1.
- **Submission date:** 2026-07-14, per the arXiv metadata page.
- **Review status:** the PDF marks the work as "Preprint. Under review" on page 1. The arXiv page lists it as a submitted cs.AI and cs.CL preprint, not as an accepted peer-reviewed publication.
- **Code link listed in paper:** <https://github.com/HowieHwong/MemoHarness>, shown on page 1.
- **Primary links:** arXiv abstract page <https://arxiv.org/abs/2607.14159>, PDF <https://arxiv.org/pdf/2607.14159>, DOI record <https://doi.org/10.48550/arXiv.2607.14159>.

## Research question

The paper asks whether an LLM agent's surrounding harness can improve by learning from prior executions rather than relying on one fixed global prompt, tool policy, workflow, memory policy, and output handler. More specifically, it tests whether a structured, experience-backed harness can adapt to each new case at test time without test-time labels, feedback, gradient updates, or additional search. The authors frame this as a gap between prompt or workflow optimization and full harness-level adaptation, especially because harness choices interact across context construction, tools, decoding, orchestration, memory, and output handling (Introduction, pages 1-2; Section 2, pages 3-7).

## Methods

MemoHarness decomposes the agent harness into six editable control surfaces: context assembly, tool interaction, generation control, orchestration, memory management, and output processing (Section 2.3 and Table 1, page 5). It then stores execution experience in a dual-layer bank containing per-case execution entries and distilled global patterns (Section 2.4, pages 5-6). During training-time search, the controller proposes harness configurations, executes them on labeled search cases, records trajectories, scores reward and token cost, diagnoses failures into coarse harness dimensions, and periodically distills repeated patterns (Section 2.5, pages 6-7; Appendix B, page 15).

The selection rule is correctness-first. Mean task reward is optimized first, and token usage is used only as a secondary tiebreaker among equal-reward candidates (Equation 16, Section 2.5, page 7). At evaluation time, the system freezes the experience bank, retrieves similar successes, similar failures, and relevant global patterns, then emits a case-specific harness for the visible test case without using the hidden answer or running a new feedback loop (Section 2.6 and Equations 17-20, pages 7-8). Figure 1 summarizes this two-phase pipeline: training-time guided harness search followed by test-time case adaptation (Figure 1, page 3).

## Population, data, and setting

There is no human learner population. The study evaluates agent systems on benchmark tasks. The three main task families are Terminal-Bench for long-horizon shell agency, LiveCodeBench for single-shot code generation, and FinanceAgent for multi-step financial reasoning (Section 3.1, page 8; Appendix C, page 16). Terminal-Bench uses an 80/20 train/evaluation split of the 89-task suite, yielding an 18-task held-out evaluation split for absolute performance and cost reporting (Appendix C, page 16).

For cross-dataset transfer, the authors also evaluate on six external suites: MMMLU, HumanEvalFix, StrongReject, Reasoning-Gym-Easy, LawBench, and SWE-Bench Pro (Table 2, page 10; Appendix C, page 16). For cross-model transfer, harness search uses GPT-5.3-Codex as the source model and the learned harness is tested without retraining on Claude-Sonnet-4.6, Gemini-3.1-Pro, Qwen3.5-397B-A17B, GLM-5, GPT-4.1, and DeepSeek-V3.2 (Table 3, page 10; Table 5, page 17; Appendix D, page 17).

## Intervention and comparison

The intervention is the MemoHarness framework: a six-dimensional harness search space, dual-layer experience bank, correctness-first training selection, and test-time case adaptation using retrieved execution experience (Sections 2.3-2.6, pages 5-8). The main comparisons are fixed or released harness baselines on Terminal-Bench: Codex, Terminus, Claude Code, and OpenCode (Section 3.1, page 8; Appendix C, page 16). The authors explicitly warn that not all baselines are pure scaffold-only transplants with the same underlying model and runtime surface, so some comparisons are system-level comparisons against the closest reproducible released configuration (Section 3.2, page 8; Appendix A, page 14; Appendix C, page 16).

## Measures

The primary measure is mean task success rate, averaged over repeated runs and reported using the validation-selected harness rather than the in-training peak (Section 3.1, page 8; Figure 3 caption, page 9; Appendix C, page 17). Cross-dataset suites use their native higher-is-better metrics (Table 2, page 10). Search-time secondary cost is total token usage, while dollar cost is computed offline from token counts and public list prices for reporting (Equations 4-6, page 4; Equation 16, page 7; Appendix B, page 15). Cost reporting on Terminal-Bench includes input tokens, cached input tokens, non-cached input tokens, output tokens, and dollars (Table 4, page 11).

## Results

### Demonstrated findings under the paper's protocol

- On Terminal-Bench, MemoHarness reaches mean task success 0.806, compared with 0.722 for the strongest baseline reported, Codex. The authors report a +0.084 gain over Codex and +0.250 to +0.445 over the other baselines (RQ1, Section 3.2, page 8; Figure 2, page 8).
- Across the three main benchmarks, the final selected harness improves over the base harness on all three: Terminal-Bench 0.722 to 0.806, LiveCodeBench 0.900 to 0.967, and FinanceAgent 0.600 to 0.767 (RQ2, Section 3.2, pages 8-9; Figure 3, page 9).
- Search trajectories differ by task family. FinanceAgent continues improving across rounds and reaches a 65.0% peak around iterations 8 and 9, while LiveCodeBench remains in a narrow 91.2% to 95.0% band, which the authors interpret as lower headroom near a base-model ceiling (RQ2, Section 3.2, page 9; Figure 4, page 9).
- Cross-dataset transfer is positive but selective. The Terminal-Bench-learned harness improves MMMLU by +0.030, StrongReject by +0.030, and SWE-Bench Pro by +0.059, while saturated suites such as HumanEvalFix and Reasoning-Gym-Easy do not move (RQ3, Section 3.2, page 10; Table 2, page 10).
- Cross-model transfer is positive for every evaluated model in the reported Terminal-Bench study, with mean gain +0.098. Examples include GPT-5.3-Codex 0.722 to 0.806, GLM-5 0.500 to 0.733, and DeepSeek-V3.2 0.333 to 0.444 (RQ4, Section 3.2, pages 10-11; Table 3, page 10).
- MemoHarness uses more raw input tokens than several baselines on the Terminal-Bench cost split, but most of those tokens are cached in the authors' evaluation. The reported dollar cost is $6.89, lower than Codex at $10.28 and Claude Code at $9.51, while Terminus and OpenCode remain cheaper at lower reported success (RQ5, Section 3.2, page 11; Table 4, page 11).
- The operation-level diagnostic appendix reports that certain newly added shell operations are associated with reward-improving transitions, such as `cat`, `sed`, `which`, and `test`, while others are weakly or negatively associated in that analysis. The authors present this as an example of diagnostic value from storing execution traces alongside scalar scores (Appendix G and Table 6, pages 19-20).

### Author interpretation

The authors claim that execution experience is a practical substrate for adaptive harnesses and that the control layer around an LLM can be improved as a complement to model scaling and manual harness engineering (Abstract, page 1; Conclusion, page 11). They interpret the gains as evidence that one fixed harness is brittle when cases differ in domain, ambiguity, reasoning depth, retrieval needs, and output format (Section 2.1, pages 3-4). They also emphasize selective rather than universal transfer, noting that learned harnesses are not universally dominant prompt templates and that component attribution remains incomplete (RQ3, page 10; Appendix A, page 14).

### Socratink product inference

For Socratink, the paper strengthens the product intuition that the **Agent Harness** is a first-class adaptive control plane rather than a thin prompt wrapper. It supports treating harness policies, retrieved execution experience, and case-specific adaptation as product surfaces that can improve task performance. It does **not** demonstrate that a learner learned more, that motivation improved, that persona or voice works better, or that learner evidence can be inferred from agent success. The Socratink inference is architectural and operational, not pedagogical.

## Limitations

The paper's own limitations are material:

1. The primary Terminal-Bench evaluation uses an 18-task held-out split and reports point estimates rather than confidence intervals or significance tests (Appendix A, page 14).
2. Not every baseline is a pure harness transplant with the same underlying model and runtime surface. Some comparisons are system-level comparisons to closest reproducible released configurations (Appendix A, page 14; Appendix C, page 16).
3. The current experiments do not fully isolate the experience bank, global patterns, and case-specific test-time adaptation in all settings (Appendix A, page 14).
4. Cost findings depend on observed cacheability of retrieved experience. Deployments with lower cache reuse may have a different cost profile (RQ5, page 11; Appendix A, page 14).
5. The controller and diagnostic operators are instantiated with practical heuristics, and future work is needed for learned or more general controllers, larger held-out splits, and online experience accumulation (Appendix A, page 14; Appendix B, page 15).

Additional Socratink-specific limitations:

- The benchmarks are agent execution benchmarks, not education studies.
- The tasks measure system output success, not human learning, motivation, trust, or willingness to pay.
- The paper's experience bank stores agent execution traces and diagnostics. Socratink must not confuse those with learner Attempts or Evidence Records.
- The paper does not validate fairness, privacy, accessibility, learner consent, deletion, persona safety, or voice evidence requirements.
- The paper does not establish that harness adaptation should silently mutate canonical learner state. Socratink's accepted durable-write gates remain necessary.

## Fit against current Socratink doctrine

### Learner Agent OS

**Strengthens:** The paper strengthens the Learner Agent OS distinction between Model and Agent Harness. It treats the harness as the external control layer managing context, tools, orchestration, memory, decoding, and output handling, which aligns with Socratink's definition of Agent Harness as the replaceable runtime that interprets learner state and coordinates Models, Tools, Thinking Skills, Teaching Skills, and Persona Packages. The cross-model transfer results especially support Socratink's commitment that model behavior and harness behavior should be separable concerns (Table 3, page 10; Learner State Ownership and Continuity Contract).

**Challenges:** It challenges any implementation plan that treats the harness as mostly static configuration. If Socratink wants adaptive teaching, retrieval, evidence capture, and tool policies, the harness should likely learn from validated operational traces. This is a design pressure, not a doctrine change.

**Leaves unchanged:** The paper leaves unchanged Socratink's claim that one learner-owned Learner Agent persists across models, harnesses, tools, skills, personas, and deployments. Harness adaptation can propose runtime policies, but it must not own learner identity, evidence, or continuity.

### Learning Map

**Strengthens:** MemoHarness's case-specific adaptation resembles Socratink's need to select different instructional control policies for different goal, target, source, readiness, and modality conditions. It supports the idea that one global route or one global teaching behavior will be brittle when cases differ.

**Leaves unchanged:** The paper does not justify changing Learning Maps into generic experience banks. A Learning Map remains a goal-scoped route through evidence-evaluable Learning Targets, not a cache of past executions. Retrieved execution experience may help propose a Next Learning Action or Teaching Skill policy, but it cannot establish target identity, prerequisite edges, mastery, or route order.

### Learner Evidence Model

**Strengthens:** The paper's diagnostic trace design indirectly reinforces Socratink's separation of observation, diagnosis, and interpretation. MemoHarness records trajectories, verifier outcomes, failures, costs, and coarse diagnoses before distilling patterns (Sections 2.4-2.5, pages 5-7; Appendix B, page 15). Socratink can analogously store observations and assistance events before evaluation.

**Challenges:** It creates a temptation to treat repeated agent success as evidence about a learner. That would violate current doctrine. MemoHarness success is evidence about a harness under benchmark conditions, not evidence that a learner can retrieve, explain, solve, or verify a Learning Target.

**Leaves unchanged:** Learner claims may change only through Evidence Records with preserved learner work, conditions, assistance, tools, scoring rule, uncertainty, and maximum claim scope. Agent Actions and harness traces remain context unless promoted through Socratink's evidence contract.

### Teaching Skill and cognitive-labor doctrine

**Strengthens:** The six-dimensional harness space gives useful implementation vocabulary for Teaching Skill execution: context assembly, tool exposure, generation budget, orchestration topology, memory policy, and output validation (Table 1, page 5). This can help implement `TeachingContext` construction, assistance-tier policies, solution-reveal handling, evaluator sealing, and typed `TeachingSkillResult` boundaries.

**Challenges:** Test-time adaptation must be constrained before learner work begins. A Teaching Skill cannot adapt the rubric, hidden evaluation material, assistance boundary, or claim ceiling after seeing the learner's Attempt merely because similar past cases suggest a better policy. MemoHarness adapts a system harness for output success. Socratink must adapt an instructional procedure while preserving learner-reserved cognitive labor.

**Leaves unchanged:** The Assistance and Solution-Revelation Policy remains required. Delegated agent work cannot be laundered into independent learner capability, even if an adaptive harness improves final task success.

### Motivation

**Strengthens:** Only weakly. The paper supports operational adaptivity, which could help Socratink avoid generic support and choose better-fit tasks or scaffolds. Better fit may support motivation, but the paper does not measure learner desire, return behavior, confidence repair, trust, or willingness to pay.

**Leaves unchanged:** Motivation remains a Socratink product responsibility, but it must be tested with learner behavior and affective safety measures, not inferred from benchmark gains.

### Persona

**Strengthens:** The paper supports compiling persona preferences through a trusted harness rather than treating a Persona Package as direct unrestricted prompt control. If persona behavior affects context, examples, challenge style, or orchestration, those choices can be represented as harness policy dimensions subject to validation.

**Leaves unchanged:** A Persona Package remains untrusted declarative package data compiled by the Agent Harness. It cannot own Tools, canonical state, learner evidence, permissions, or durable writes. MemoHarness does not change persona authority.

### Voice

**Mostly leaves unchanged:** The paper has no direct evidence about voice learning, ASR, TTS, speech modality, consent, accessibility, or Voice Package rights. The only relevant inference is that voice capture, transcript correction, ASR confidence, evaluator sealing, and TTS rendering should be harness-controlled surfaces rather than provider-owned hidden behavior. Socratink's voice doctrine remains governed by the voice evidence and voice system design notes.

## What this strengthens, challenges, or leaves unchanged

### Strengthens

- Treat Agent Harness as a first-class adaptive control plane.
- Store execution traces, diagnostics, costs, and policy versions as reusable operational experience.
- Use typed harness dimensions rather than one monolithic prompt when analyzing failures.
- Prefer correctness-first selection where lower cost is a tiebreaker, not the primary learning objective.
- Keep Models replaceable and evaluate whether harness policies transfer across model families.

### Challenges

- Static, one-size-fits-all harness configuration for all learning tasks.
- Any plan that lacks operational trace capture for failed Teaching Skill executions.
- Any plan that optimizes local cost or short completions before task validity and learner evidence quality.
- Any plan that cannot explain which control surface changed when an adaptive policy improves or fails.

### Leaves unchanged

- Learner Agent State owns continuity, not the Model or harness.
- Learning Maps route through Learning Targets, not generic memory traces.
- Learner Evidence Records require learner work and bounded interpretation.
- Teaching Skills must preserve cognitive-labor attribution and evidence claim ceilings.
- Persona and Voice Packages remain subordinate to the Agent Harness, permissions, and evidence gates.
- Product doctrine should not change from this alpha preprint alone.

## Bounded product hypotheses

1. **Harness-dimension logging hypothesis:** If Socratink logs Teaching Skill failures by context, tool, generation, orchestration, memory, output, assistance tier, and evaluation-boundary dimensions, then debugging and policy improvement will become faster than reviewing raw transcripts alone.
   - **Falsifiable test:** Run a set of repeated Teaching Skill failure reviews. Compare time-to-actionable-fix and reviewer agreement between raw-transcript review and dimension-coded review.

2. **Case-specific Teaching Skill policy hypothesis:** If the harness retrieves similar prior successes and failures before issuing a Learning Task, then it will select more appropriate assistance tiers and task formats without reducing evidence validity.
   - **Falsifiable test:** In a controlled prototype, randomize tasks to static policy versus retrieved-experience policy. Measure valid Attempt rate, evaluator abstention rate, post-task learner correction rate, and delayed transfer performance.

3. **Correctness-first evidence-quality hypothesis:** If Socratink ranks instructional policies by evidence validity and learner target performance before cost, then it will avoid cheap interactions that feel efficient but produce unusable Evidence Records.
   - **Falsifiable test:** Compare a cost-minimizing route selector against a validity-first selector on the same goals. Measure Evidence Record acceptance rate, claim-ceiling violations, learner-rated usefulness, and token cost.

4. **Cross-model continuity hypothesis:** If harness policies are typed, versioned, and separated from model-specific caches, then Socratink can swap Models without corrupting canonical learner state while preserving comparable Teaching Skill behavior.
   - **Falsifiable test:** Use a canonical learner-state fixture, run the same TeachingContext under two Models with one harness policy, and verify that state hashes remain unchanged except through validated Evidence Records or explicit migrations.

5. **Adaptive retrieval safety hypothesis:** If operational experience retrieval is restricted to policy guidance and not canonical learner evidence, then it can improve instruction without leaking hidden solutions or overwriting learner-specific state.
   - **Falsifiable test:** Seed the experience bank with cases containing hidden solutions and unrelated learner artifacts. Verify that retrieved content cannot enter learner prompts, rubrics, Persona Relationship State, or Evidence Records unless explicitly permitted and provenance-labeled.

## Overgeneralization warnings

- Do not infer human learning gains from agent benchmark success.
- Do not treat MemoHarness as proof that memory always helps. The gains depend on task type, retrieval quality, cacheability, and validation protocol.
- Do not treat the six dimensions as Socratink's final harness ontology. They are a useful starting taxonomy, not a complete education architecture.
- Do not assume cost competitiveness if cache hit rates fall, if voice/media artifacts are involved, or if privacy constraints prevent broad experience reuse.
- Do not use adaptive harness success to justify hidden state mutation. Socratink still needs explicit learner permission, provenance, versioning, and durable-write gates.
- Do not let a controller adapt evidence rules after seeing learner work. In education, adaptation can improve teaching, but evidence interpretation must remain sealed enough to avoid moving the goalposts.

## Bottom-line verdict

This paper is **alpha-positive for Socratink's Agent Harness architecture**. It provides early, concrete evidence that harness-level experience, typed control surfaces, and test-time case adaptation can improve agent task success across several benchmark regimes. It most strengthens Socratink's commitment to a serious Agent Harness rather than a thin chatbot wrapper.

It is **not evidence for changing accepted learning doctrine**. It does not prove learner learning, motivation, persona efficacy, voice efficacy, or learner-evidence validity. The right product response is to prototype typed harness experience logging and constrained policy adaptation around Teaching Skills, then test whether they improve valid learner work and delayed performance without violating cognitive-labor attribution.
