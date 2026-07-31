# Research note: prerequisite cycles in a goal-scoped Learning Map

Date: 2026-07-31

## Question

Should active hard-prerequisite edges among Learning Targets be required to form a directed acyclic graph, even though human knowledge is interconnected, iterative, and sometimes mutually dependent?

## Conclusion

Yes, but only because of the **operational meaning assigned to a hard route gate**, not because knowledge or learning is inherently a DAG.

A strict `requiresTarget(A, B)` edge means that target A must normally be available or sufficiently demonstrated before the route may unlock target B under a particular Goal Interpretation. If both `requiresTarget(A, B)` and `requiresTarget(B, A)` are active, neither target provides a valid entry point. The routing contract is contradictory even when the underlying concepts genuinely develop together.

Therefore:

- the Knowledge Ontology may contain cycles, reciprocal relationships, cross-links, feedback systems, and mutually explanatory concepts;
- argument, association, transfer, and support graphs may also contain typed cycles;
- the active strict-gating projection over Learning Targets must be acyclic;
- a detected hard-gate cycle is evidence that the edge semantics, target granularity, scope, or confidence needs revision;
- resolving a cycle must not erase the real mutual dependency it revealed.

## Research grounding

### Knowledge structure is not naturally a simple sequence

Concept-map theory distinguishes hierarchical organization from cross-links among different parts of a knowledge structure. Novak and Cañas argue that context matters and that cross-links can reveal important relationships and creative integration. This supports a richly connected Knowledge Ontology, not a universal linear curriculum.

Source: Novak, J. D., & Cañas, A. J. (2008), *The Theory Underlying Concept Maps and How to Construct and Use Them*. <https://cmap.ihmc.us/docs/theory-of-concept-maps>

### Prerequisite structure is a model over feasible learning states

Knowledge-space theory models a domain through feasible states and prerequisite closure rather than semantic proximity. Its importance for Socratink is the separation between the objects or performances being assessed and the hypothesized order constraining feasible states. A prerequisite relation is a formal model used for assessment and adaptation, not proof that cognition itself is globally linear.

Source: Doignon, J.-P., & Falmagne, J.-C. (1985), “Spaces for the Assessment of Knowledge.” <https://doi.org/10.1016/S0020-7373(85)80031-6>

### Learning progressions are hypotheses requiring empirical refinement

The learning-progression literature describes progressions as constructs developed to coordinate curriculum, instruction, and assessment. Duncan and Hmelo-Silver explicitly identify development, validation, and unresolved questions as central concerns. Empirical progression studies describe iterative design and validation rather than discovery of one timeless sequence. Mohan, Chen, and Anderson report an iterative process and plans for further conceptual and empirical validation. Songer, Kelcey, and Gotwals likewise use empirical results to revise progression design.

Sources:

- Duncan, R. G., & Hmelo-Silver, C. E. (2009), “Learning Progressions: Aligning Curriculum, Instruction, and Assessment.” <https://doi.org/10.1002/tea.20316>
- Mohan, L., Chen, J., & Anderson, C. W. (2009), “Developing a Multi-Year Learning Progression for Carbon Cycling in Socio-Ecological Systems.” <https://doi.org/10.1002/tea.20314>
- Songer, N. B., Kelcey, B., & Gotwals, A. W. (2009), “How and When Does Complex Reasoning Occur?” <https://doi.org/10.1002/tea.20313>

This supports treating every prerequisite as a versioned, scoped, falsifiable map hypothesis. Learner evidence may strengthen, weaken, or personalize it without rewriting the original provenance.

### Assessment validity requires the gate to serve a specific claim and use

The assessment triangle and evidence-centered design require coherence among cognition, observation, and interpretation. A hard prerequisite should therefore exist only when it has a defensible relationship to the destination Learning Target, the task conditions, and the intended routing decision. Textbook order, concept hierarchy, model confidence, or semantic similarity alone is insufficient.

Sources:

- National Research Council (2001), *Knowing What Students Know*. <https://doi.org/10.17226/10019>
- Mislevy, R. J., Steinberg, L. S., & Almond, R. G. (2003), “On the Structure of Educational Assessments.” <https://doi.org/10.1207/S15366359MEA0101_02>

## Product interpretation

The DAG requirement should apply only to the **active strict-gating projection** for one Learning Map revision and Goal Interpretation. It must not be generalized into claims that:

- all knowledge has one true total order;
- every learner must follow the same sequence;
- revisiting earlier targets is invalid;
- reciprocal conceptual relationships are modeling errors;
- co-development, spiraling, feedback, or transfer cannot occur.

A learner may revisit any target. Teaching sequences may spiral through targets repeatedly. A later target may strengthen an earlier one. Those behaviors do not require contradictory hard gates.

## Recommended cycle-resolution policy

When an active `requiresTarget` cycle is detected, activation should stop and a `MapRevision` should require one of these explicit resolutions:

1. **Downgrade an overstated edge** to `supportsTarget` when the relationship is helpful but not a true gate.
2. **Split or refine a target** when the cycle was caused by targets that bundle multiple performances at incompatible levels of granularity.
3. **Scope the edge more narrowly** when the prerequisite holds only for a particular context, modality, task, source, or Goal Interpretation.
4. **Represent co-development explicitly** when the targets genuinely reinforce one another. The group has an entry strategy and no internal hard ordering. It is not itself evidence of mastery and does not merge the targets or their Evidence Contracts.
5. **Mark the structure unresolved** when evidence is insufficient. The system may propose exploratory tasks, but it must not invent an arbitrary hard order.

Every resolution preserves the original claims, provenance, confidence, disagreement, and revision history.

## Recommended acceptance rule

> The active `requiresTarget` projection must be acyclic because it encodes strict route eligibility, not because knowledge is acyclic. Cycles elsewhere are governed by their own edge semantics. A hard-gate cycle blocks activation until an inspectable Map Revision downgrades, decomposes, narrows, co-develops, or explicitly leaves the relationship unresolved.

## Limits

This research supports the semantic and governance policy. It does not establish a universal statistical threshold for promoting a prerequisite hypothesis into a hard gate. That threshold should be tested by domain, learner population, consequence, and available evidence. The product should initially make hard gates rare, explainable, and easy to challenge rather than pretending prerequisite discovery is solved.
