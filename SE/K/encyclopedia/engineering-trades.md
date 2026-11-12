# Engineering trade studies: making preferences and uncertainty inspectable

**Reference entry · Concept selection and decision analysis · Expanded reference**

## Definition

An **engineering trade study** is a structured comparison of feasible alternatives against stated mission objectives, constraints, stakeholder preferences, and uncertainties. It is not an after-the-fact ranking table designed to justify a preferred option. A sound trade makes the option set, constraints, consequence models, scoring assumptions, and sensitivity to uncertainty transparent enough for another engineer to challenge.

A trade study must distinguish **feasibility** from **preference**. A concept that violates a mandatory safety or accessibility threshold is not rescued by scoring high on convenience. A concept that is Pareto-dominated by another feasible concept generally needs a special explanation before further investment.

## Formal structure

Let **X** be candidate architectures, **gⱼ(x) ≤ 0** be constraints, and **fᵢ(x)** be outcomes to maximize or minimize. An alternative is Pareto-dominated if another feasible option is no worse on all relevant objectives and strictly better on at least one. The Pareto frontier identifies efficient tradeoffs; it does **not** determine which efficient point stakeholders should prefer.

A weighted additive score **V(x) = Σ wᵢ vᵢ(fᵢ(x))** may be useful when value-function meaning, scaling, and preference-independence assumptions are justified. If scores are normalized using only the candidates in the current shortlist, adding another candidate can change the scale and reverse rankings without changing any real consequence. More robust methods use externally anchored preference curves where possible.

## Worked numerical comparison

Two feasible shuttle designs have the following illustrative outcomes:

| Attribute | Concept A | Concept B |
|---|---:|---:|
| Average peak wait (minutes, lower better) | 6 | 8 |
| Daily energy use (kWh, lower better) | 420 | 300 |
| Cost per day ($, lower better) | 1,200 | 1,050 |

Suppose stakeholders explicitly accept a simplified value scale over a declared comparison range: wait value **v_w = (12 − wait)/8**, energy value **v_e = (500 − energy)/250**, and cost value **v_c = (1500 − cost)/600**. Let weights be **0.5, 0.2, 0.3**. Then A receives **0.5(0.75) + 0.2(0.32) + 0.3(0.50) = 0.589**; B receives **0.5(0.50) + 0.2(0.80) + 0.3(0.75) = 0.635**. On these assumptions B ranks higher.

But if the weight on wait time increases, the ranking may reverse. The lesson is not that B is objectively superior: it is that the preference structure and measurement assumptions are now visible and challengeable. If there is a hard maximum wait or an accessibility minimum, apply it *before* scoring.

## Engineering decision procedure

1. Establish the decision, boundary, owners, and lifecycle horizon.
2. Generate genuinely different alternatives, including the baseline and potentially reversible pilot options.
3. Define nonnegotiable feasibility constraints and check them independently.
4. Estimate consequences using validated models, experiments, or defensible analogies.
5. Identify correlated outcomes and avoid counting the same benefit twice.
6. Elicit value functions and tradeoff weights with authorized stakeholders.
7. Run sensitivity and scenario analysis; report where rankings change.
8. Select, defer, prototype, or request new information, with a documented rationale.

## Uncertainty, failure modes, and evidence

Costs, demand, operating life, environmental conditions, and mission use are rarely certain. Consider probability distributions and common-cause dependence rather than only one deterministic input table. Use value of information to decide whether another test or prototype is worth its expense. Robust selection may prefer a slightly lower expected score with materially better worst-case performance.

Watch for false precision (scores reported to four decimals from subjective inputs), undisclosed excluded options, incomparable time horizons, and weighted matrices that hide infeasible options. A defensible trade report shows raw outcomes, assumptions, constraints, model credibility, sensitivity, and dissent.

## Connections

Trade studies rely on stakeholder value models, requirements constraints, architecture alternatives, uncertainty propagation, model credibility, and governance. They produce a justified decision record rather than mathematical inevitability.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Reference chapters for lifecycle, needs, requirements, design, technical management, integration and V&V.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Breadth-first conceptual encyclopedia and pointers to further references.


## Technical analysis: independently recompute the trade and its robustness

Recomputing the displayed trade-study table: A's values are `(0.75, 0.32, 0.50)` and B's `(0.50, 0.80, 0.75)` on the *declared* anchored scales. With weights `(0.5,0.2,0.3)`, the exact scores are `V_A=0.589` and `V_B=0.635` as reported. The score difference is `−0.046` in A-minus-B direction, small enough that plausible preference changes may reverse the decision; the scores are **not** measured probabilities of mission success.

Holding the energy weight at `0.2`, transferring weight between waiting and cost as `w_wait=w` and `w_cost=0.8−w`, the score difference is `V_A−V_B = 0.5w−0.296`. The indifference point is `w=0.592`. The baseline waiting weight of `0.50` favors B, whereas `0.65` favors A. A defensible report should draw a *preference-stability region* and state whether weight changes of this size are reasonable, rather than suppressing the reversal.

This check presumes the value functions are meaningful across the mission operating envelope. It does not validate the underlying wait, energy, or cost estimates. Further stress demand scenarios, battery aging, accessibility constraints, and evidence about uncertainty before treating either concept as a chosen baseline.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.



## Step 02 review studio — constraints before preferences

A trade study can create the appearance of objectivity even when it combines incompatible measures. First screen mandatory requirements; then define value functions and weights for legitimate compensatory comparisons. Suppose A costs 100 and yields 12 service units, B costs 110 and yields 14, and C costs 120 and yields 11. If cost should be minimized and service maximized, C is **Pareto dominated by A**, since A is both cheaper and better.

**Solved exercise:** may C win a weighted model with positive weights for low cost and high service on properly monotonic value scales? **Not if only those two criteria matter**, because it is dominated. If someone claims C wins, inspect scoring direction, hidden criteria, normalization, or arithmetic; the problem may be conceptual rather than computational.

**Qualification:** feasible alternatives depend on actual constraints, not a convenient scoring list. Real preferences may include lifecycle uncertainty, accessibility, or operational resilience absent from this two-criterion example. A trade-study result should name the intended decision and the evidence that would change it.

## Follow the knowledge

**Related concepts**

- [Pareto frontiers and multiobjective decisions](pareto-and-value.md)
- [Decision uncertainty and value of information](bayesian-value-of-information.md)
- [Probability, distributions, and dependence](probability-and-dependence.md)
- [Functional, logical, and physical architectures](functional-vs-physical.md)

**Explore in the 240-chapter textbooks**

- [Book 1, Chapter 8: Chapter 8 — A Trade Study Makes Judgment Inspectable](../B1/chapters/08-trade-studies-and-sensitivity.md)
- [Book 6, Chapter 9: Book 6 · Chapter 9: Value functions and double counting](../B6/chapters/09-objectives-value-functions-and-multiattribute-evaluatio.md)
- [Book 14, Chapter 4: Book 14 · Chapter 04 — Apply constraints, dominance, and Pareto analysis to the selection problem](../B14/chapters/04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

