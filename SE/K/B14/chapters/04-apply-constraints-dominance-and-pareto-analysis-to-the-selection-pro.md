# Chapter 04 — Apply constraints, dominance, and Pareto analysis to the selection problem

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 4 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 4](../labs/lab-04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md) → attempt the [original Week 4 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w04.md) remains available for a quick recap.

## The decision behind the theory

Rankings can conceal that some options are simply worse on every relevant dimension, while other options represent real tradeoffs. **Essential question:** What can be concluded before stakeholder preferences are aggregated?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Validate units, missing values, direction of preference, and evidence comparability before computing dominance.

Feasibility precedes preference. A constraint violation can exclude an alternative, trigger a waiver decision, or require redesign; do not silently assign a bad score.

Alternative X dominates Y if X is no worse on all considered objectives and better on at least one, under the stated direction and data. Uncertainty can make dominance indeterminate.

The Pareto set contains non-dominated alternatives for the included objectives and dataset. It does not prove completeness, fairness, or stakeholder preference.

Show the effect of adding/removing objectives and of measurement uncertainty on frontier membership.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Model decisions, uncertainties, evidence, constraints, and alternatives**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Converge on a preferred selection using transparent value and decision methods**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Pareto analysis identifies alternatives for which no objective can improve without worsening another.

### Distinguishing related ideas

A dominated option can be eliminated without knowing preferences, but the Pareto frontier does not itself identify a winner.

### Interpretation and boundary conditions

Hard feasibility rules must precede preference comparison; a slightly safer unsafe design is still unacceptable.

## Graduate depth: feasibility, dominance, and uncertainty in trade spaces

### Constraints define eligibility before preferences rank it

Multiobjective analysis starts with a feasible set, not with a weighted score. Let design vector `x` represent resources, architecture choices, and operating rules. The feasible region is `X = {x : g_i(x) <= 0, h_j(x) = 0}` under stated assumptions. Requirements involving safety, regulatory limits, interoperability, and physically achievable performance should not be converted into small score penalties merely to preserve an appealing alternative. By contrast, preferences about cost or convenience may be traded among eligible designs when the decision authority permits it.

A candidate `a` Pareto-dominates `b` for objectives to be minimized if `f_i(a) <= f_i(b)` for every objective and `<` for at least one, assuming comparable scales, identical scenarios, and established directions of preference. Nondominated alternatives form a Pareto set. The Pareto frontier does not identify a unique best design; it reveals where improving one objective requires a sacrifice in another. Furthermore, dominance in a deterministic model does not imply dominance under uncertain parameters or changing operational contexts.

### Treat uncertainty in constraints explicitly

Suppose a charging system must support daily energy demand `D` within available energy `E(x,omega)`. Checking only `E[E(x,omega)] >= D` ignores the probability of shortfall. A chance constraint might instead require `P[E(x,omega) >= D(omega)] >= 0.99`. This is meaningful only if the joint uncertainty model for energy, demand, and outages is supported. Distribution-free worst-case constraints can be conservative, while chance constraints can hide severe tail consequences. When failures are safety-critical, an estimated 99% success probability may be insufficient and must not be treated as an authorization threshold by default.

Robust dominance can be defined across a scenario set: design `a` is no worse than `b` in each required scenario and strictly better somewhere. That criterion is demanding; few alternatives survive when scenarios conflict. A more informative presentation can display conditional frontiers by scenario, constraint margins, and where the relative order changes. Monte Carlo output alone does not justify averaging away stakeholder differences or regulatory obligations.

### Numerical illustration and model integrity

Consider three fictional feasible Northstar designs, evaluated for normalized cost and mean response time: A `(100, 14)`, B `(110, 12)`, C `(120, 13)`, with lower preferred for both. B dominates C because it is cheaper and faster; A and B are nondominated. But suppose B lacks required accessible-trip coverage during a battery outage. B then fails a hard scenario requirement; it should be excluded before constructing the relevant frontier. Alternatively, if B's response time has a large uncertainty interval, the dominance conclusion may not be statistically established. Report scenario definitions, measurement error, model error, and practical effect sizes.

Constraint boundaries are engineering hypotheses, too. A new interface design may expand the feasible region; a supplier delay may shrink it. Recompute the frontier after changes rather than carrying forward a frozen rank. The decision artifact should preserve why each design was ruled out, what remains uncertain, and which requirements are truly nonnegotiable. Pareto analysis improves transparency precisely because it refuses to conceal values inside an apparently objective single number.

## Worked engineering example from the course

Alternative D has lower wait, higher accessible coverage, higher availability, and lower emissions than C, but costs more and deploys later. Neither dominates the other. Alternative F may be dominated once cost is treated over five years rather than only pilot purchase price; the conclusion must state the cost boundary.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

If A has cost $300k and wait 15 min while B has cost $320k and wait 12 min, neither dominates: A is cheaper and B faster. An option C costing $350k with wait 17 min is dominated by both.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A design succeeds with probability 0.8 for benefit $500k, otherwise loses $100k. What is expected value before acquisition cost?

<details><summary>Show a reasoned solution</summary>

EV=0.8×500k+0.2×(−100k)=$380k. A risk-averse or budget-constrained decision maker may still reject it.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Maximize/minimize directions are inconsistent.
* An infeasible option is scored as though feasible without waiver.
* Pareto efficiency is called optimal or best.
* A changed objective set is not reflected in the interpretation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. Does a Pareto frontier require weights?
2. Can a dominated option be chosen?
3. What is weak dominance?
4. Why audit cost boundaries?

<details><summary>Explain the answers</summary>

**1. Does a Pareto frontier require weights?** No. It depends on objectives, directions, feasibility, and performance values.

**2. Can a dominated option be chosen?** Only with an explicit reason such as omitted objectives, uncertainty, constraints, or strategic considerations; the dominance result itself must not be hidden.

**3. What is weak dominance?** No worse on all objectives, with definitions varying on whether strict improvement is required.

**4. Why audit cost boundaries?** Different lifecycle boundaries can reverse comparisons.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 4](../labs/lab-04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[03 — Previous chapter](03-model-decisions-uncertainties-evidence-constraints-and-alternatives.md) · [05 — Next chapter](05-converge-on-a-preferred-selection-using-transparent-value-and-decisi.md) · [Book index](../README.md)
