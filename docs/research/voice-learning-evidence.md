# Learner speech as an evidence-bearing learning modality

Issue: [jon-devlapaz/socraTink#4](https://github.com/jon-devlapaz/socraTink/issues/4)
Branch: `research/voice-learning-evidence`
Date: 2026-07-31

## Executive answer

Spoken explanation can be useful evidence in a learning loop, but it is not a privileged window into understanding. Speech can reveal a learner's retrievable content, explanatory structure, vocabulary, misconceptions, metacognitive monitoring, fluency under a task, and sometimes affective or interactional cues. It cannot, by itself, establish durable learning, general transfer, motivation, intelligence, mental state, disability status, honesty, or mastery independent of the task, prompt, language, speech context, microphone, ASR model, and scoring rubric.

The best-supported mechanism is not “speaking” itself. It is active retrieval plus generative explanation. Retrieval practice has high-utility evidence across learning conditions, and self-explanation has moderate-to-strong evidence depending on domain and implementation. Oral explanation can add useful affordances: low-friction production, time-stamped hesitation and revision traces, conversational repair, and teach-back-style checks. Writing can be equally or more appropriate when the target construct is formal composition, precision, notation, reflection, accessibility, or auditable evidence. The report therefore supports a voice-first option only if SocraTink treats speech as one input modality among several, validates transcripts before inference, provides non-speech alternatives, and separates evidence from interpretation.

## Practical conclusion for a voice-first reconstruction loop

A defensible loop is:

1. Ask the learner to retrieve and explain from memory, not merely reread or repeat.
2. Capture audio only after explicit consent and with an obvious recording indicator.
3. Transcribe, then show the learner the transcript or extracted claims for correction.
4. Score the explanation against a task-specific rubric grounded in target knowledge, not against generic fluency, accent, confidence, or prosody.
5. Use speech signals as prompts for follow-up questions, not as final labels.
6. Offer equivalent written, typed, AAC, captioned, and quiet-environment alternatives.
7. Retain the minimum audio/transcript data required for the learning purpose.
8. Validate ASR and scoring separately by subgroup, accent, dialect, age, disability, language, device, environment, and domain vocabulary.

## What speech can reveal

Speech can provide evidence about the following, when the task and scoring rule are explicit.

| Evidence channel | What it can support | Guardrail |
| --- | --- | --- |
| Free recall or prompted explanation | Retrieval of facts, relationships, procedures, examples, and misconceptions at the moment of the task | Do not infer long-term retention unless later delayed retrieval confirms it. |
| Self-explanation | Whether the learner can connect steps, causes, constraints, and principles | Requires rubrics for causal and conceptual quality. Talk quantity alone is not evidence. |
| Teach-back or explaining to a peer | Whether the learner can reorganize content for an audience and expose gaps through clarification | Strongest when there is feedback or a check for receiver understanding. |
| Revisions, repairs, and “wait, no” moments | Metacognitive monitoring and error correction | Can indicate monitoring, but not necessarily deeper knowledge. |
| Timing, pauses, fillers, prosody | Possible cognitive load, formulation difficulty, uncertainty, interaction management, or emotion cues | These cues are multiply determined. They should trigger follow-up, not scoring by themselves. |
| ASR transcript | A convenient textual artifact for retrieval and explanation scoring | Transcript errors can erase, invent, or bias evidence. Learner review is required for high-stakes use. |

## What cannot be inferred from speech alone

Do not infer these directly from audio, transcript, or prosody:

- Durable mastery or transfer without delayed, varied retrieval.
- General intelligence, aptitude, or “learning style.”
- Motivation, confidence, boredom, anxiety, or deception as labels.
- English proficiency, disability, or neurodivergence unless the assessment was designed and validated for that construct.
- Knowledge absence from silence, pauses, accent, low volume, stuttering, code-switching, or ASR failure.
- Superiority of speaking over writing for all learners or all topics.
- Fairness across dialects, accents, ages, genders, disabilities, microphones, or environments without subgroup validation.

## Evidence by topic

### 1. Retrieval is the strongest learning mechanism to preserve

Retrieval practice is strongly supported. Roediger and Karpicke found that taking memory tests improved long-term retention of prose passages compared with restudying, even though restudying could improve short-term performance and confidence. Karpicke and Roediger later found that repeated testing after initial correct recall produced a large delayed-recall benefit for vocabulary learning, while repeated studying after learning did not. Dunlosky and colleagues rated practice testing and distributed practice as high-utility learning techniques because their benefits generalize across learner characteristics, materials, and criterion tasks more than many common study strategies.

Implication for SocraTink: speech is valuable when it operationalizes retrieval. A voice prompt like “explain without looking” is aligned with this evidence. A voice prompt that merely asks the learner to narrate while reading is weaker.

Sources: Roediger & Karpicke (2006), Karpicke & Roediger (2008), Dunlosky et al. (2013).

### 2. Self-explanation and oral explanation can reveal conceptual organization

Self-explanation research supports asking learners to generate explanations of steps, principles, and relationships. Bisra and colleagues' meta-analysis found self-explanation benefits across many studies, while Dunlosky et al. treated self-explanation as promising but not as broadly generalizable as practice testing. This distinction matters: explanation is useful, but its effectiveness depends on domain, prior knowledge, prompt design, feedback, and outcome measure.

Oral explanation may be especially useful when the product is a spontaneous explanation rather than a polished essay. It can reveal the order in which concepts are retrieved, where a learner repairs an error, and which explanatory links are missing. But a transcript is still a performance sample, not the learner's full knowledge state.

Implication for SocraTink: prompt for causal links, contrasts, examples, and failure cases. Score the structure and correctness of claims, not verbosity or eloquence.

Sources: Bisra et al. (2018), Dunlosky et al. (2013), Chi et al. (1989).

### 3. Teach-back is useful as a comprehension check, not a magic proof of mastery

Teach-back asks a learner or patient to explain material back in their own words so the educator can check comprehension and repair gaps. Talevski and colleagues' systematic review of health-care teach-back found mostly positive effects across heterogeneous settings, with 19 of 20 studies reporting effectiveness across outcomes such as knowledge recall, retention, and health outcomes. The review also emphasized implementation heterogeneity and limited reporting of implementation strategies.

Learning-by-teaching research is related but not identical. Ribosa and Duran's meta-analysis on students generating teaching materials found evidence for learning-by-teaching effects, but the effect depends on task design and the teaching artifact.

Implication for SocraTink: teach-back should be used as a loop: learner explanation, system or human detection of gaps, targeted follow-up, and re-explanation. A single fluent explanation should not be treated as final mastery.

Sources: Talevski et al. (2020), Ribosa & Duran (2022), Fiorella & Mayer (2013).

### 4. Speaking versus writing is a design trade-off, not a hierarchy

The evidence does not justify a universal claim that speaking is better than writing. Research comparing oral and written explanation suggests modality interacts with text complexity, task demands, and whether the learner is self-explaining or explaining to a fictitious student. Jacob, Lachner, and Scheiter's Learning and Instruction article is explicitly titled “Learning by explaining orally or in written form? Text complexity matters.” Lachner, Sibley, and Hoogerheide's work on written explanations found that written self-explaining can outperform written instructional explaining in some conditions, and their cumulative analysis suggested only a small effect for instructional explaining, moderated by modality.

Writing has distinct strengths. It slows production, supports editing, produces easier audit trails, enables formal notation, helps learners externalize complex structures, and can be more accessible for learners who cannot or do not want to speak. Speaking has distinct strengths. It can lower friction, capture spontaneous retrieval, encourage elaboration, and support conversational repair. The right choice depends on the target construct and learner context.

Implication for SocraTink: offer speech and writing as parallel evidence modes. Prefer speech for low-friction retrieval and conversational reconstruction. Prefer writing for precision, formulas, long-form argument, revision history, accessibility needs, and high-stakes records.

Sources: Jacob et al. (2020), Lachner et al. (2021), Hoogerheide et al. (2016), Dunlosky et al. (2013).

### 5. Hesitation, pauses, and prosody are signals with many causes

Disfluencies are real linguistic phenomena, not mere noise. Clark and Fox Tree argued that “uh” and “um” function in spontaneous speaking and can manage listener expectations. Scherer's review of vocal emotion research shows that voice carries affect-relevant information, but it also highlights the complexity of research paradigms and interpretation.

For learning assessment, this means hesitation and prosody are weak standalone evidence. Pauses may reflect retrieval difficulty, planning, unfamiliar vocabulary, second-language production, speech impairment, anxiety, microphone delay, turn-taking norms, or simply careful thought. Prosody may reflect emotion, culture, disability, environment, or task format. These signals are useful for adaptive UX, such as “would you like a hint?” or “take your time,” but not for latent labels such as “confused,” “unmotivated,” or “low mastery” without validation.

Implication for SocraTink: use hesitation and prosody as uncertainty indicators that route to follow-up questions. Do not use them as direct grading features unless the construct is explicitly speech fluency and the measure is validated for the population.

Sources: Clark & Fox Tree (2002), Scherer (2003), AERA/APA/NCME Standards (2014).

### 6. ASR and transcription error can distort evidence

ASR is not neutral measurement. Koenecke and colleagues evaluated five major ASR systems on structured interviews and found substantial racial disparities, with average word error rate of 0.35 for Black speakers versus 0.19 for White speakers. Tatman found gender and dialect differences in YouTube automatic captions, with lower accuracy for women and Scottish speakers in that dataset. NIST's Speech Recognition Scoring Toolkit is a standard toolkit for scoring recognition outputs, including alignment-based scoring through `sclite`.

ASR errors matter more in learning than in casual dictation because a single domain term, negation, formula, or causal connector can change the assessment. “Does not increase” versus “does increase” is a validity failure, not just a typo. Error rates also vary by device, background noise, language, code-switching, age, disability, accent, dialect, and domain vocabulary.

Implication for SocraTink: never treat raw ASR transcripts as ground truth. Store audio only if needed. Show transcripts to learners for correction. Track ASR confidence and word alternatives. Validate word error rate, concept error rate, and downstream scoring error by subgroup and domain.

Sources: Koenecke et al. (2020), Tatman (2017), NIST SCTK.

### 7. Accessibility requires equivalent non-speech paths

WCAG 2.2 covers accessibility for auditory, physical, speech, cognitive, language, learning, and neurological disabilities, and notes that its criteria are testable but do not cover every need. A voice-first system must not become speech-only. Learners may be deaf or hard of hearing, nonspeaking, have speech disabilities, use augmentative and alternative communication, be in noisy or public spaces, have trauma or anxiety around being recorded, or be using a device without a microphone.

Voice can also be an accessibility benefit for learners with dysgraphia, motor impairments, low vision, fatigue, or limited keyboard access. The design requirement is modality choice and equivalent learning value, not mandatory speech.

Implication for SocraTink: provide typed responses, pasted notes, AAC-compatible input, captions, transcript editing, keyboard access, visible recording state, pause/resume, and the ability to opt out of audio while still completing the learning loop.

Sources: W3C WCAG 2.2, W3C Web Speech API.

### 8. Privacy and consent are central because voice is sensitive personal data

The Web Speech API security and privacy section requires explicit, informed user consent before speech input sessions and an obvious indication when audio is being recorded. It also warns that speech input could be used for eavesdropping and that malicious pages could mislead users about recording state.

In education contexts, FERPA governs privacy of education records for covered educational agencies and institutions. The U.S. Department of Education's FERPA page points to 34 CFR Part 99 and the statutory rights around student records. COPPA applies to online collection of personal information from children under 13 in covered contexts, and the FTC's COPPA guidance describes operator duties around notice and verifiable parental consent. GDPR treats biometric data used for uniquely identifying a person as a special category of personal data under Article 9, and voice recordings are at least personal data when they identify or relate to an identifiable person. NIST's Privacy Framework provides a risk-management approach to identify and manage privacy risks.

Implication for SocraTink: define whether audio, transcript, embeddings, rubric scores, and derived misconceptions are education records or personal data in each deployment. Use purpose limitation, data minimization, retention limits, encryption, access control, deletion/export, consent records, vendor agreements, and separate controls for minors.

Sources: W3C Web Speech API, U.S. Department of Education FERPA page, FTC COPPA FAQ, GDPR Article 9, NIST Privacy Framework.

### 9. Evidence validity must be designed, not assumed

The Standards for Educational and Psychological Testing define validity around evidence and theory supporting interpretations of scores for proposed uses. This is the key assessment principle for SocraTink: a voice transcript is not automatically a valid measure of learning. The interpretation must be warranted.

A validity argument for a voice-first reconstruction loop should specify:

- Construct: what learning target is being inferred.
- Task: why the prompt elicits relevant evidence.
- Observation: what is captured, such as audio, transcript, concepts, errors, timing, or self-corrections.
- Scoring: how evidence maps to feedback or mastery claims.
- Generalization: whether the inference holds across prompts and contexts.
- Fairness: whether subgroup performance differences reflect the construct rather than ASR, accent, disability, or access.
- Consequences: whether the feedback helps learners and avoids harmful labels or exclusion.

NIST's AI RMF is not education-specific, but its framing is useful: trustworthy AI requires risk management across design, development, use, and evaluation. For SocraTink, that means ASR, extraction, scoring, feedback generation, and data retention each need separate evidence and monitoring.

Sources: AERA/APA/NCME Standards (2014), NIST AI RMF 1.0.

## Design recommendations

### Evidence model

Use a layered model:

1. **Audio layer:** raw speech with consent metadata, device/environment metadata where appropriate, and short retention.
2. **Transcript layer:** ASR output with confidence, alternatives, timestamps, and learner corrections.
3. **Claim layer:** extracted propositions, examples, causal links, definitions, procedures, and misconceptions.
4. **Rubric layer:** domain-specific scoring against target knowledge.
5. **Feedback layer:** generated questions, hints, retrieval prompts, and reconstruction tasks.
6. **Evidence log:** what was inferred, from which source, with what confidence, and whether the learner corrected it.

### Product guardrails

- Phrase feedback as “your explanation did not mention X” rather than “you do not know X.”
- Prefer “the transcript may have missed this” when confidence is low.
- Keep audio optional unless the learning goal is explicitly oral communication.
- Keep writing available as a first-class path.
- Make transcript correction part of the learning activity, not an error-recovery afterthought.
- Do not infer emotion or confidence from voice for grading.
- Do not use accent, dialect, speaking rate, pause length, or filler frequency as mastery features.
- Separate formative feedback from summative assessment.
- Require human review for high-stakes claims.

### Evaluation plan

Before relying on speech-derived evidence, run these checks:

1. **Learning efficacy:** randomized comparison of voice retrieval, written retrieval, and non-retrieval control with delayed tests.
2. **Construct validity:** expert review of whether extracted claims match target concepts.
3. **Transcript accuracy:** WER and domain concept error rate by subgroup and environment.
4. **Downstream scoring accuracy:** compare rubric scores from human transcript, ASR transcript, learner-corrected transcript, and audio-informed human scoring.
5. **Fairness:** inspect error and feedback rates across dialect, accent, language background, disability, gender, age, microphone type, and noise level.
6. **Accessibility:** test with screen readers, keyboard-only users, captions, AAC workflows, low-vision settings, and no-microphone environments.
7. **Privacy:** document data inventory, lawful basis or consent flow, retention schedule, deletion path, vendor processing, and minor protections.
8. **User consequence:** measure whether feedback improves reconstruction without increasing shame, surveillance concerns, or opt-out penalties.

## Major evidence gaps

1. **Direct comparisons of speech and writing for reconstruction loops are thin.** There is evidence on retrieval, self-explanation, oral versus written explanation, and learning-by-teaching, but less evidence on AI-mediated voice-first reconstruction systems with transcript correction and adaptive feedback.
2. **Most modality studies are narrow.** They often use specific domains, short interventions, undergraduates or school samples, and limited outcome measures. They do not establish universal superiority of speech.
3. **Prosody and hesitation validity is weak for learning inference.** These signals are meaningful in speech science, but not sufficiently construct-valid for mastery, motivation, or affect labels in general learners.
4. **ASR fairness evidence changes quickly.** Koenecke et al. and Tatman show serious disparities, but commercial ASR systems evolve. SocraTink needs current, deployment-specific audits.
5. **Domain vocabulary errors are under-measured.** Standard WER can miss the educational cost of misrecognizing a key concept, negation, symbol, named entity, or causal connector.
6. **Accessibility research for voice-first learning tools is sparse.** General WCAG guidance is strong, but product-specific evidence is needed for learners using AAC, speech disabilities, hearing loss, multilingual speech, or quiet-space constraints.
7. **Privacy expectations for learner voice are context-sensitive.** FERPA, COPPA, GDPR, and state privacy laws may apply differently by deployment. Product evidence must include legal review and user trust research.
8. **Validity evidence for AI-generated feedback is separate from validity evidence for ASR.** A good transcript can still produce invalid feedback if extraction or scoring is wrong.

## References

- AERA, APA, & NCME. (2014). *Standards for Educational and Psychological Testing*. Official AERA page: https://www.aera.net/Publications/Books/Standards-for-Educational-Psychological-Testing-2014-Edition
- Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*, 703-725. https://doi.org/10.1007/s10648-018-9434-x
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science, 13*(2), 145-182. https://doi.org/10.1207/s15516709cog1302_1
- Clark, H. H., & Fox Tree, J. E. (2002). Using uh and um in spontaneous speaking. *Cognition, 84*(1), 73-111. https://doi.org/10.1016/S0010-0277(02)00017-3
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4-58. https://doi.org/10.1177/1529100612453266
- European Parliament and Council. (2016). Regulation (EU) 2016/679, General Data Protection Regulation. EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679
- Federal Trade Commission. (2026). Complying with COPPA: Frequently Asked Questions. https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- Fiorella, L., & Mayer, R. E. (2013). The relative benefits of learning by teaching and teaching expectancy. *Contemporary Educational Psychology, 38*(4), 281-288. https://doi.org/10.1016/j.cedpsych.2013.06.001
- Hoogerheide, V., Deijkers, L., Loyens, S. M. M., Heijltjes, A., & van Gog, T. (2016). Gaining from explaining: Learning improves from explaining to fictitious others on video, not from writing to them. *Contemporary Educational Psychology, 44-45*, 95-106. https://doi.org/10.1016/j.cedpsych.2016.02.005
- Jacob, L., Lachner, A., & Scheiter, K. (2020). Learning by explaining orally or in written form? Text complexity matters. *Learning and Instruction, 68*, 101344. https://doi.org/10.1016/j.learninstruc.2020.101344
- Karpicke, J. D., & Roediger, H. L. III. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966-968. https://doi.org/10.1126/science.1152408
- Koenecke, A., Nam, A., Lake, E., Nudell, J., Quartey, M., Mengesha, Z., Toups, C., Rickford, J. R., Jurafsky, D., & Goel, S. (2020). Racial disparities in automated speech recognition. *Proceedings of the National Academy of Sciences, 117*(14), 7684-7689. https://doi.org/10.1073/pnas.1915768117
- Lachner, A., Sibley, L., & Hoogerheide, V. (2021). Learning by writing explanations: Is explaining to a fictitious student more effective than self-explaining? *Learning and Instruction*. https://doi.org/10.1016/j.learninstruc.2020.101438
- National Institute of Standards and Technology. (2023). Artificial Intelligence Risk Management Framework. https://www.nist.gov/itl/ai-risk-management-framework
- National Institute of Standards and Technology. (2025). Privacy Framework. https://www.nist.gov/privacy-framework
- National Institute of Standards and Technology. (2021). SCTK, the NIST Scoring Toolkit. https://github.com/usnistgov/SCTK
- Ribosa, J., & Duran, D. (2022). Do students learn what they teach when generating teaching materials for others? A meta-analysis through the lens of learning by teaching. *Educational Research Review, 37*, 100475. https://doi.org/10.1016/j.edurev.2022.100475
- Roediger, H. L. III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249-255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Scherer, K. R. (2003). Vocal communication of emotion: A review of research paradigms. *Speech Communication, 40*(1-2), 227-256. https://doi.org/10.1016/S0167-6393(02)00084-5
- Talevski, J., Wong Shee, A., Rasmussen, B., Kemp, G., & Beauchamp, A. (2020). Teach-back: A systematic review of implementation and impacts. *PLOS ONE, 15*(4), e0231350. https://doi.org/10.1371/journal.pone.0231350
- Tatman, R. (2017). Gender and dialect bias in YouTube's automatic captions. *Proceedings of the First ACL Workshop on Ethics in Natural Language Processing*, 53-59. https://doi.org/10.18653/v1/W17-1606
- U.S. Department of Education, Student Privacy Policy Office. FERPA regulations and guidance. https://studentprivacy.ed.gov/ferpa
- W3C. (2024). Web Content Accessibility Guidelines (WCAG) 2.2. W3C Recommendation. https://www.w3.org/TR/WCAG22/
- W3C Web Speech API Community Group. (2026). Web Speech API, Security and privacy considerations. https://webaudio.github.io/web-speech-api/#security-and-privacy-considerations
