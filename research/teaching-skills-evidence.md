# Evidence-backed Teaching Skills for SocraTink's first adult wedge

Date: 2026-07-31  
Issue: [jon-devlapaz/socraTink#3](https://github.com/jon-devlapaz/socraTink/issues/3)  
Scope: adults learning difficult technical or academic material, especially postsecondary STEM, professional upskilling, and self-directed study of dense conceptual sources.

## Executive answer

The most defensible first Teaching Skills are not "brain hacks." They are behavioral learning routines with converging support from cognitive psychology, education meta-analyses, and postsecondary STEM evidence:

1. **Cold retrieval with corrective feedback**: ask the learner to reconstruct, solve, or explain from memory before seeing the answer, then give targeted feedback.
2. **Spaced re-retrieval**: schedule later retrieval attempts after meaningful delays, with intervals chosen for the intended retention horizon rather than a fixed folklore rule.
3. **Worked-example to problem fading**: start novices from well-designed worked examples, alternate examples with problems, then progressively remove steps.
4. **Self-explanation and deep-question prompting**: make the learner explain why steps, claims, and mechanisms work, especially when integrating new material with prior knowledge.
5. **Contrastive/interleaved discrimination practice**: mix confusable problem types, concepts, or cases after initial exposure so the learner learns when each idea applies.
6. **Active problem-solving with feedback and inclusive structure**: replace passive exposure with short cycles of prediction, attempt, peer/AI discussion when useful, feedback, and retry.
7. **Knowledge organization as a support skill, not a substitute for retrieval**: concept maps and structural representations can improve organization and transfer, but should feed retrieval and explanation rather than become the whole learning activity.

Methods with weak or overgeneralized evidence should not become first-class doctrine: passive rereading, highlighting, generic summarization, unsupported "learning styles," pure unguided discovery for novices, and fixed neuroscience claims such as "the hippocampus requires X" or "sleep-gated verification proves consolidation." Sleep and consolidation matter biologically, but the product-relevant evidence is stronger for **delayed behavioral retrieval tests** than for any specific mechanistic explanation.

## Evidence standard used

I prioritized sources in this order:

- **Authoritative consensus and practice guidance**: National Academies consensus reports and Institute of Education Sciences / What Works Clearinghouse practice guides.
- **Systematic reviews and meta-analyses**: especially those with broad moderators, classroom/postsecondary samples, or adult-relevant tasks.
- **Landmark primary experiments**: used to clarify mechanisms or product affordances, not to overrule broader syntheses.

Evidence grades in this report:

- **High**: converging meta-analysis/practice-guide/consensus support, adult or postsecondary relevance, and clear product-operational form.
- **Moderate**: credible evidence with narrower materials, populations, or implementation conditions.
- **Promising but constrained**: plausible and supported in some settings, but sensitive to learner expertise, task type, or instructional design.
- **Do not canonize**: evidence is weak, contested, or too context-dependent for product doctrine.

## Source landscape

The most useful consensus documents for SocraTink are:

- The IES/WWC practice guide **Organizing Instruction and Study to Improve Student Learning**, which recommends spacing learning over time, interleaving worked examples with problem solving, combining graphics with verbal descriptions, connecting abstract and concrete representations, quizzing for learning, helping learners allocate study time, and asking deep explanatory questions. It explicitly targets content-heavy subjects including science and mathematics and includes postsecondary in its grade scope.[^pashler-ies]
- The National Academies report **How People Learn II**, a consensus update covering learning across the lifespan, formal and informal settings, cognition, motivation, learning technologies, and learning across domains.[^hpl2]
- The National Academies discipline-based education research report for undergraduate science and engineering, which frames postsecondary STEM learning as domain-specific and practice/assessment dependent rather than reducible to generic study tips.[^dber]

The most important systematic reviews and meta-analyses for this issue are Dunlosky et al.'s review of 10 learning techniques, Adesope et al. and Rowland on practice testing/retrieval, Cepeda et al. on distributed practice, Freeman et al. and Theobald et al. on active learning in undergraduate STEM, Wisniewski et al. on feedback, Bisra et al. on self-explanation, Nesbit and Adesope on concept maps, and Macnamara et al. on the limits of deliberate practice.[^dunlosky][^adesope][^rowland][^cepeda][^freeman][^theobald][^feedback][^bisra][^nesbit][^macnamara]

## Candidate Teaching Skills

### 1. Cold retrieval with corrective feedback

**Recommendation:** make this a first Teaching Skill.

**Operational form**

- Ask the learner to answer, reconstruct, solve, draw, or explain **before** showing the explanation.
- Prefer effortful recall, short-answer generation, explanation, and problem solving over recognition-only prompts when the target is durable conceptual knowledge.
- Give immediate or near-immediate feedback that identifies the specific missing distinction, step, misconception, or condition of use.
- Re-test repaired items later rather than marking them permanently learned inside the same session.

**Outcomes supported**

Retrieval practice improves retention compared with restudy and often improves transfer/comprehension when the retrieval task requires meaningful reconstruction. Dunlosky et al. rated practice testing as **high utility** because benefits generalized across learning conditions, learner characteristics, materials, and criterion tasks.[^dunlosky] Adesope et al.'s meta-analysis found practice tests more beneficial than restudying and other non-testing conditions, with effects moderated by test features, participant/study characteristics, outcomes, and methods.[^adesope] Rowland's meta-analysis found testing benefits over restudy and indicated larger benefits when initial tests require recall rather than recognition.[^rowland]

Karpicke and Blunt's primary experiment is especially relevant to SocraTink because it used science-text learning and found retrieval practice produced better meaningful learning than elaborative studying with concept mapping, including on comprehension and inference questions and even when the final assessment involved creating concept maps.[^karpicke-blunt] This should be read as evidence for retrieval's importance, not as evidence that concept mapping is useless.

**Adult/population/context fit**

- Strong fit for adults learning technical material because the method can be embedded in self-study, AI tutoring, exam preparation, code learning, medical/engineering/science concepts, and professional upskilling.
- Postsecondary relevance is substantial, though many studies include undergraduates rather than mid-career adults.
- Works best when prompts match the desired outcome: recall for facts, explanation for mechanisms, problem solving for procedural/conditional knowledge, and transfer cases for application.

**Limitations and contested claims**

- Retrieval is not magic. A poor prompt can train shallow recall while leaving conditional use or causal understanding weak.
- Recognition quizzes are easier to scale but may underdeliver for generative understanding.
- Retrieval can fail unproductively if prior exposure is too weak, if feedback is absent, or if the learner repeatedly rehearses errors.
- Do not claim that retrieval works because of a specific hippocampal prediction-error mechanism unless the product actually depends on that mechanism and cites neuroscience directly. The defensible product claim is behavioral: delayed successful retrieval predicts and improves durable performance better than passive review.

**Evidence quality:** **High**.

**Teaching Skill shape:** `cold-retrieval-drill`: attempt → inspect failure → targeted feedback → retry → mark for later delayed retrieval.

---

### 2. Spaced re-retrieval and delayed verification

**Recommendation:** make this a first Teaching Skill, but avoid fixed interval dogma.

**Operational form**

- Schedule retrieval attempts across time instead of massing repetitions in one session.
- Tie intervals to the learner's retention goal and item difficulty.
- Use failed or repaired items as high-priority candidates for later tests.
- Treat delayed tests as evidence of behavioral retention, not as proof of a named neural consolidation process.

**Outcomes supported**

Dunlosky et al. rated distributed practice as **high utility**.[^dunlosky] Cepeda et al.'s quantitative synthesis covered 839 assessments from 317 experiments in 184 articles and found that spacing and lag matter, with the optimal interstudy interval increasing as the final retention interval increases.[^cepeda] The IES practice guide recommends arranging delayed review of key course content weeks to months after initial presentation and using quizzes to re-expose students to key content.[^pashler-ies]

**Adult/population/context fit**

- Strong fit for adult self-directed study because adult learners often have fragmented schedules and long-term goals.
- Especially valuable for technical vocabulary, procedures, distinctions, equations, laws, and conceptual dependencies that must remain available after the tutorial ends.
- Works for SocraTink's Stage 4 idea if framed as **delayed retrieval verification** rather than "sleep-gated proof."

**Limitations and contested claims**

- A fixed "24-hour" rule is too coarse. Cepeda et al. show spacing depends on the target retention interval.[^cepeda]
- Most spacing evidence concerns verbal recall, though it generalizes enough to support scheduling. Complex transfer and professional performance need better evidence.
- Sleep may contribute to consolidation, but product policy should not require a biological claim. The measurable requirement is that learners can reconstruct after a delay, under reduced short-term accessibility.

**Evidence quality:** **High** for delayed retrieval/spacing, **moderate** for exact scheduling algorithms in complex adult technical learning.

**Teaching Skill shape:** `spaced-verification-scheduler`: classify item difficulty/outcome → schedule future retrieval → adapt interval based on success/failure → separate same-session repair from delayed verification.

---

### 3. Worked-example to problem fading

**Recommendation:** make this a first Teaching Skill for novices and difficult procedural domains.

**Operational form**

- Show a complete worked example for a problem type.
- Ask the learner to explain the rationale for each step.
- Alternate worked examples with near problems.
- Fade steps progressively until the learner solves independently.
- Move from blocked practice to interleaved practice once basic schemas exist.

**Outcomes supported**

The IES practice guide recommends interleaving worked example solutions with problem-solving exercises, specifically having students alternate between reading worked solutions and solving problems on their own.[^pashler-ies] Atkinson et al.'s review in *Review of Educational Research* summarizes instructional principles from worked-example research and is closely tied to cognitive-load theory and problem-solving instruction.[^atkinson] The broader cognitive-load interpretation is that novices can waste working memory on unguided search before they have schemas, while worked examples focus attention on structure and step rationale.

**Adult/population/context fit**

- Strong for adult learners entering mathematics, statistics, programming, physics, algorithms, accounting, formal logic, lab protocols, and other procedure-heavy domains.
- Also useful for conceptual tasks when the "worked example" is a fully traced causal explanation or annotated solution path.

**Limitations and contested claims**

- Worked examples can become passive if the learner only reads them. The skill must require prediction, self-explanation, or completion.
- Expertise reversal matters: advanced learners may learn more from problem solving than from fully worked examples.
- Worked examples are strongest for well-structured domains. Ill-structured academic argument, design judgment, or research interpretation need examples plus comparison, critique, and feedback.

**Evidence quality:** **High** for novice procedural learning, **moderate** for complex conceptual transfer.

**Teaching Skill shape:** `worked-example-fading`: show annotated model → prompt step rationale → give completion problem → fade support → independent solve → delayed re-solve.

---

### 4. Self-explanation and deep explanatory questions

**Recommendation:** make this a first Teaching Skill, especially for SocraTink's mechanism-first identity.

**Operational form**

- Ask "why does this step follow?", "what mechanism makes this true?", "what would break if this assumption changed?", and "how does this connect to a prior node?"
- Require the learner to generate explanations, not merely endorse them.
- Use prompts to expose missing links, non-distinguishing definitions, and hidden causal assumptions.
- Pair with feedback or model explanations when the learner cannot produce a valid explanation.

**Outcomes supported**

Dunlosky et al. rated self-explanation and elaborative interrogation as **moderate utility**: promising and broadly plausible, but less established across educational contexts than retrieval and spacing.[^dunlosky] The IES practice guide recommends asking deep explanatory questions that prompt students to pose and answer deep-level questions and support understanding of taught material.[^pashler-ies] Bisra et al.'s meta-analysis identifies self-explanation as a systematic instructional target, with meta-analytic evidence but implementation-sensitive effects.[^bisra]

**Adult/population/context fit**

- Strong fit for adults learning theory, science mechanisms, programming semantics, mathematical derivations, legal/academic arguments, and systems thinking.
- Particularly aligned with SocraTink's emphasis on causal architecture and avoiding the "bird-naming" fallacy.

**Limitations and contested claims**

- Self-explanation quality varies. Learners can produce fluent but wrong explanations.
- Novices may need scaffolds, partial explanations, or contrast cases before they can explain effectively.
- Self-explanation is not automatically superior to retrieval. It should often be a retrieval prompt: explain from memory, then compare to a model.

**Evidence quality:** **Moderate to high** as a candidate when combined with feedback and retrieval; lower if implemented as ungraded journaling.

**Teaching Skill shape:** `mechanism-explanation-prompt`: learner explanation → identify missing causal link/distinction → targeted prompt or mini-model → learner restates → add delayed retrieval item.

---

### 5. Contrastive and interleaved discrimination practice

**Recommendation:** make this a first Teaching Skill for confusable concepts and problem types, but not as universal randomization.

**Operational form**

- Identify a set of similar concepts, procedures, cases, or problem types that learners confuse.
- Present mixed examples after initial exposure to each category.
- Ask the learner to choose the applicable concept/procedure and justify the diagnostic cue.
- Include near-miss and counterexample cases.

**Outcomes supported**

Dunlosky et al. rated interleaved practice as **moderate utility** because evidence was promising but less developed across contexts than retrieval and spacing.[^dunlosky] The IES practice guide supports interleaving worked examples with problems.[^pashler-ies] Rohrer argues that interleaving helps learners distinguish among similar concepts, which is exactly the product use case for SocraTink's "non-distinguishing definition" and counterexample moves.[^rohrer]

**Adult/population/context fit**

- Strong for technical classification and conditional use: choosing an algorithm, statistical test, design pattern, proof technique, diagnosis, legal standard, or physics principle.
- Useful after learners have enough initial representation to avoid pure confusion.

**Limitations and contested claims**

- Early learning may require blocked introduction before interleaving.
- Interleaving can feel harder and reduce short-term fluency, which may hurt motivation if not framed.
- Evidence is narrower than retrieval/spacing and often domain-specific.

**Evidence quality:** **Moderate**.

**Teaching Skill shape:** `contrast-case-discriminator`: cluster confusables → generate near cases → learner predicts label/procedure → asks for diagnostic cue → feedback contrasts why alternatives fail.

---

### 6. Active problem-solving with feedback and inclusive structure

**Recommendation:** make this a platform-level pattern and modular Teaching Skill, especially for adults in STEM-like domains.

**Operational form**

- Convert exposition into short cycles: predict → attempt → discuss or reflect → feedback → revise.
- Prefer frequent low-stakes attempts over long lectures followed by a final quiz.
- In group/class contexts, include structure that makes participation equitable and psychologically safe.
- In solo AI contexts, simulate the accountable parts: explicit attempt, wait time, feedback, retry, and progress tracking.

**Outcomes supported**

Freeman et al. meta-analyzed 225 undergraduate STEM studies and found active learning increased exam/concept-inventory performance by 0.47 standard deviations; traditional lecture had an odds ratio for failing of 1.95 versus active learning, and students in lecture were 1.5 times more likely to fail.[^freeman] Effects held across STEM disciplines and class sizes, with largest effects in small classes.[^freeman] Theobald et al. analyzed achievement gaps in undergraduate STEM and found active learning reduced exam-score gaps by 33% and passing-rate gaps by 45% for underrepresented students, with high-intensity active learning important and a hypothesis that durable equity gains require both deliberate practice and inclusive teaching.[^theobald]

**Adult/population/context fit**

- Strong for postsecondary and adult technical learning, especially when adults are doing hard problem solving rather than consuming explanations.
- For SocraTink, the AI analogue is not "make lessons interactive" in a vague way. It is structured, repeated attempts with feedback and retry.

**Limitations and contested claims**

- "Active learning" is an umbrella, not a single treatment. Product doctrine should specify mechanisms: retrieval, problem solving, feedback, peer explanation, deliberate practice, or inclusive participation.
- Classroom results do not transfer automatically to solo AI tutoring. The interaction design has to preserve accountability and feedback.
- Theobald et al. show intensity and inclusive design matter; superficial click-through activities should not count.

**Evidence quality:** **High** for undergraduate STEM classes; **moderate to high** for AI/self-study translations depending on implementation fidelity.

**Teaching Skill shape:** `active-attempt-loop`: micro-goal → learner prediction/solution → feedback → repair → retry → delayed verification.

---

### 7. Feedback as information, not praise

**Recommendation:** make this a cross-cutting component of every Teaching Skill rather than a standalone first module.

**Operational form**

- Feedback should answer: What was the goal? What exactly is wrong or missing? What cue or rule distinguishes the right answer? What should the learner do next?
- Prioritize task/process/self-regulation feedback over generic praise.
- Use feedback to generate the next retrieval or contrast item.

**Outcomes supported**

Wisniewski, Zierer, and Hattie's meta-analysis of 435 studies, 994 effects, and more than 61,000 learners found a medium average effect of feedback on learning (d = 0.48), but also significant heterogeneity. The impact depended substantially on information content, and feedback had higher impact on cognitive and motor-skill outcomes than motivational or behavioral outcomes.[^feedback]

**Adult/population/context fit**

- Strong for adult technical learning because error information can be precise: wrong assumption, skipped step, invalid inference, misclassified case, or failed test.
- Especially useful in programming/math/statistics where feedback can be tied to executable or formal checks.

**Limitations and contested claims**

- Feedback is not one intervention. Praise, grades, hints, explanations, answer keys, and process cues differ.
- Too much feedback too early can reduce productive attempt, while too little can rehearse errors.
- Feedback should not replace retrieval. It should close the loop after retrieval.

**Evidence quality:** **High** as a component, **not meaningful** as an undifferentiated module.

**Teaching Skill shape:** embed `diagnostic-feedback-contract` in every module.

---

### 8. Knowledge organization and concept maps

**Recommendation:** use as a support skill, not as the first proof-of-learning skill.

**Operational form**

- Extract or build a knowledge map that names concepts, dependencies, causal links, and confusables.
- Use the map to select retrieval targets, prerequisite chains, contrast sets, and delayed review items.
- Ask learners to reconstruct parts of the map from memory after study.

**Outcomes supported**

Nesbit and Adesope's meta-analysis supports learning with concept and knowledge maps as an educational strategy.[^nesbit] The IES guide also recommends connecting abstract and concrete representations and combining graphics with verbal descriptions.[^pashler-ies] However, Karpicke and Blunt found retrieval practice outperformed concept mapping for science-text learning even on later concept-map outcomes.[^karpicke-blunt]

**Adult/population/context fit**

- Strong for SocraTink because the existing product architecture depends on knowledge maps.
- Useful for difficult academic material where structure is hidden in prose or lecture rhetoric.

**Limitations and contested claims**

- A polished map can create an illusion of competence if learners recognize structure without reconstructing it.
- Learner-generated maps can be misleading when prior knowledge is weak.
- Map quality is itself a hard instructional-design problem.

**Evidence quality:** **Moderate** as a support for organization and transfer; **insufficient** as a standalone proof of understanding.

**Teaching Skill shape:** `map-to-retrieval-planner`: convert map nodes into retrieval prompts, explanation prompts, contrast cases, and spaced verification schedule.

---

### 9. Deliberate practice: useful but contested as a broad doctrine

**Recommendation:** use the microstructure, avoid the grand claim.

**Operational form**

- Define a specific target skill.
- Give tasks just beyond current competence.
- Provide informative feedback.
- Repeat with increasing difficulty.
- Track performance against explicit criteria.

**Outcomes supported and contested**

The deliberate-practice literature supports the general idea that structured, goal-directed practice with feedback matters. But Macnamara, Hambrick, and Oswald's meta-analysis found deliberate practice explained 26% of variance in games, 21% in music, 18% in sports, 4% in education, and less than 1% in professions, concluding it is important but less determinative than popular accounts claim.[^macnamara] Ericsson and Harwell disputed broad operationalizations and argued that original definitions matter.[^ericsson-harwell]

**Adult/population/context fit**

- Strong as a design pattern for technical skill acquisition.
- Weak as a promise that effortful practice alone can overcome all individual, contextual, or domain constraints.

**Limitations and contested claims**

- Do not use "deliberate practice" as a universal explanation for expertise.
- For SocraTink, the safer product claim is: repeated targeted attempts with feedback improve specific performance, and the system can make those attempts visible.

**Evidence quality:** **Moderate and contested**.

**Teaching Skill shape:** integrate into `active-attempt-loop`, not a standalone ideology.

## Methods to avoid as first Teaching Skills

| Method or claim | Why not first-class doctrine | Safer use |
|---|---|---|
| Passive rereading | Dunlosky et al. rated rereading low utility relative to practice testing and distributed practice.[^dunlosky] | Allow brief review before retrieval, but do not count it as learning proof. |
| Highlighting/underlining | Low utility and often creates recognition fluency without durable performance.[^dunlosky] | Use only as annotation for later questions or map extraction. |
| Generic summarization | Low utility overall; can help skilled learners on some tasks but is implementation-sensitive.[^dunlosky] | Turn summaries into retrieval, critique, or explanation prompts. |
| Pure unguided discovery | Alfieri et al. found discovery effects depend on guidance; unassisted discovery is risky for novices.[^alfieri] Lazonder and Harmsen's inquiry meta-analysis likewise centers guidance as a moderator.[^lazonder] | Use guided inquiry with scaffolds, feedback, and worked examples. |
| Learning styles | Not supported well enough for product architecture. | Offer modality choices for accessibility and preference, not as ability-matched learning doctrine. |
| Fixed neuroscience slogans | The education-facing evidence usually supports behavioral routines, not product-specific neural mechanisms. | Say "delayed retrieval is stronger evidence than immediate familiarity," not "sleep proves consolidation." |

## Product implications for current SocraTink architecture

The existing pipeline already points in a promising direction:

- `learnops-extract` creates a structural knowledge map.
- `learnops-present` segments the map into a study surface.
- `learnops-drill` forces explanation and retrieval.
- Stage 4 is planned as delayed verification.

The evidence suggests tightening the language and contracts:

1. **Keep the map, but make retrieval the proof.** A map is a targeting and scaffolding artifact. It should not be treated as evidence that the learner understands.
2. **Replace mechanistic neuroscience claims with behavioral acceptance criteria.** For example: "A repaired node is not Solid until the learner reconstructs it after a delay without notes." This is stronger and easier to test than "synaptic consolidation requires sleep."
3. **Distinguish same-session repair from durable learning.** Same-session correction can show immediate understanding, but delayed retrieval is the stronger retention signal.
4. **Make prompt types outcome-specific.** Facts need recall, mechanisms need causal explanation, procedures need worked-example fading and problem solving, confusables need contrast cases, and transfer needs novel cases.
5. **Track evidence quality per skill.** Retrieval and spacing can be core doctrine. Self-explanation, interleaving, maps, and deliberate practice should carry implementation notes.

## Suggested first modular Teaching Skills

### Tier 1: ship first

1. **Cold Retrieval Drill**  
   Evidence: high.  
   Outcome: durable recall, conceptual reconstruction, gap detection.  
   Core contract: no answer before attempt; feedback must produce a new attempt or scheduled delayed test.

2. **Spaced Verification Scheduler**  
   Evidence: high for spacing, moderate for exact adaptive scheduling.  
   Outcome: retention over time.  
   Core contract: repaired/learned items require delayed retrieval before durable status.

3. **Worked Example Fader**  
   Evidence: high for novice procedural learning.  
   Outcome: problem-solving schemas.  
   Core contract: example → explanation → completion → independent problem → delayed re-solve.

4. **Mechanism Explanation Drill**  
   Evidence: moderate to high when paired with retrieval/feedback.  
   Outcome: causal understanding and transfer.  
   Core contract: learner explains why/how; system checks missing links and non-distinguishing definitions.

### Tier 2: ship as targeted modules

5. **Contrast Case Discriminator**  
   Evidence: moderate.  
   Outcome: choosing the right concept/procedure under confusability.  
   Core contract: mixed cases with diagnostic-cue justification.

6. **Map-to-Retrieval Planner**  
   Evidence: moderate as support.  
   Outcome: converts a knowledge map into testable prompts and schedules.  
   Core contract: maps create drills; maps do not certify learning.

7. **Active Attempt Loop**  
   Evidence: high in undergraduate STEM classrooms, moderate to high for solo AI translation.  
   Outcome: engagement, performance, reduced passive exposure.  
   Core contract: every learning segment includes an accountable learner attempt and informative feedback.

## Major evidence gaps

1. **Adult self-directed AI tutoring evidence is thinner than classroom and lab evidence.** Many strong studies use undergraduates, classrooms, or controlled lab text learning. SocraTink should instrument outcomes rather than assume direct transfer.
2. **Technical-domain transfer needs careful measurement.** Retrieval and spacing reliably improve retention, but far transfer in programming, advanced math, research reasoning, and professional judgment is harder to prove.
3. **Optimal spacing schedules for heterogeneous concept maps are not settled.** Evidence supports spacing and adapting intervals to retention horizon, but exact scheduling for causal-graph learning is an engineering hypothesis.
4. **Self-explanation and interleaving depend heavily on prompt quality.** These should be implemented with diagnostics and examples, not generic "explain more" prompts.
5. **Knowledge-map learning is promising but can inflate perceived competence.** The map must feed retrieval and reconstruction tasks.
6. **Inclusive active learning evidence is classroom-based.** Solo AI systems need analogues for belonging, confidence, and participation safety, but the direct evidence base is emerging.
7. **Neuroscience mechanisms are not yet product acceptance criteria.** The product can respect memory science without claiming that a given UI step directly causes a named neural event.

## Bottom line

For the first adult wedge, SocraTink should define Teaching Skills around **observable learning behaviors**: attempted retrieval, explanation, problem solving, feedback, spacing, and discrimination among confusable cases. These methods are defensible because they are supported by meta-analyses and practice guidance and can be expressed as testable product contracts. The system should avoid turning plausible neuroscience into doctrine; it should prove learning by whether adults can reconstruct and apply difficult material later, not by whether the product story sounds biologically sophisticated.

## References

[^pashler-ies]: Pashler, H., Bain, P. M., Bottge, B. A., Graesser, A., Koedinger, K., McDaniel, M., & Metcalfe, J. (2007). *Organizing Instruction and Study to Improve Student Learning*. Institute of Education Sciences / What Works Clearinghouse Practice Guide. https://ies.ed.gov/ncee/wwc/PracticeGuide/1

[^hpl2]: National Academies of Sciences, Engineering, and Medicine. (2018). *How People Learn II: Learners, Contexts, and Cultures*. National Academies Press. https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures

[^dber]: National Research Council. (2012). *Discipline-Based Education Research: Understanding and Improving Learning in Undergraduate Science and Engineering*. National Academies Press. https://nap.nationalacademies.org/catalog/13362/discipline-based-education-research-understanding-and-improving-learning-in-undergraduate-science-and-engineering

[^dunlosky]: Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4-58. https://doi.org/10.1177/1529100612453266

[^adesope]: Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. *Review of Educational Research, 87*(3), 659-701. https://doi.org/10.3102/0034654316689306

[^rowland]: Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432-1463. https://doi.org/10.1037/a0037559

[^karpicke-blunt]: Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*(6018), 772-775. https://doi.org/10.1126/science.1199327

[^cepeda]: Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354-380. https://doi.org/10.1037/0033-2909.132.3.354

[^atkinson]: Atkinson, R. K., Derry, S. J., Renkl, A., & Wortham, D. (2000). Learning from examples: Instructional principles from the worked examples research. *Review of Educational Research, 70*(2), 181-214. https://doi.org/10.3102/00346543070002181

[^bisra]: Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*, 703-725. https://doi.org/10.1007/s10648-018-9434-x

[^rohrer]: Rohrer, D. (2012). Interleaving helps students distinguish among similar concepts. *Educational Psychology Review, 24*, 355-367. https://doi.org/10.1007/s10648-012-9201-3

[^freeman]: Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *Proceedings of the National Academy of Sciences, 111*(23), 8410-8415. https://doi.org/10.1073/pnas.1319030111

[^theobald]: Theobald, E. J., Hill, M. J., Tran, E., Agrawal, S., Arroyo, E. N., Behling, S., Chambwe, N., et al. (2020). Active learning narrows achievement gaps for underrepresented students in undergraduate science, technology, engineering, and math. *Proceedings of the National Academy of Sciences, 117*(12), 6476-6483. https://doi.org/10.1073/pnas.1916903117

[^feedback]: Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. *Frontiers in Psychology, 10*, 3087. https://doi.org/10.3389/fpsyg.2019.03087

[^nesbit]: Nesbit, J. C., & Adesope, O. O. (2006). Learning with concept and knowledge maps: A meta-analysis. *Review of Educational Research, 76*(3), 413-448. https://doi.org/10.3102/00346543076003413

[^alfieri]: Alfieri, L., Brooks, P. J., Aldrich, N. J., & Tenenbaum, H. R. (2011). Does discovery-based instruction enhance learning? *Journal of Educational Psychology, 103*(1), 1-18. https://doi.org/10.1037/a0021017

[^lazonder]: Lazonder, A. W., & Harmsen, R. (2016). Meta-analysis of inquiry-based learning: Effects of guidance. *Review of Educational Research, 86*(3), 681-718. https://doi.org/10.3102/0034654315627366

[^macnamara]: Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). Deliberate practice and performance in music, games, sports, education, and professions: A meta-analysis. *Psychological Science, 25*(8), 1608-1618. https://doi.org/10.1177/0956797614535810

[^ericsson-harwell]: Ericsson, K. A., & Harwell, K. W. (2019). Deliberate practice and proposed limits on the effects of practice on the acquisition of expert performance: Why the original definition matters and recommendations for future research. *Frontiers in Psychology, 10*, 2396. https://doi.org/10.3389/fpsyg.2019.02396
