# Chapter 08 — Formulate parametric design and conduct multiobjective search

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 8 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 8](../labs/lab-08-formulate-parametric-design-and-conduct-multiobjective-search.md) → attempt the [original Week 8 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w08.md) remains available for a quick recap.

## The decision behind the theory

A feasible design space may contain thousands or millions of combinations and continuous settings. **Essential question:** How should the analyst formulate and search the space without mistaking algorithm output for complete knowledge?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Define variables with type, bounds/options, units, owner, and feasibility logic. Define objectives with direction and computation source.

Mixed-variable design requires careful encoding; integer labels must not imply physical distance among categories.

Weighted sums are useful but can miss nonconvex frontier regions and collapse transparency. Epsilon-constraint and population-based methods expose different regions.

Verify the search with known test functions, repeated seeds, constraint checks, and comparison to enumerated subsets where possible.

Algorithm convergence means the search stabilized under its settings; it does not prove complete exploration, accurate models, or appropriate objectives.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Reframe the engineering design problem and generate alternatives through morphology**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Design computational experiments to learn efficiently from the design space**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Multiobjective design reveals structure in the trade space

An optimization problem is defined by decision variables, feasible constraints, and objectives. When more than one objective matters, there may be no unique best design. One alternative may minimize cost while another maximizes resilience; neither dominates the other if each is superior on at least one important dimension. The nondominated frontier makes this conflict visible without pretending that all stakeholders share a single weighting of outcomes.

The frontier is only as valid as its model. If charging congestion or maintenance outages are omitted, an apparently efficient design may disappear once those constraints are added. Some variables are discrete architectural choices, while others are continuous settings; combining them can create nonconvex trade spaces. Before interpreting solver output, check units, bounds, constraint satisfaction and model validity. A mathematically optimized result is a property of the formulation, not a guarantee about the operational world.

## Deeper theory: multiobjective design searches a feasible world, not a score table

An optimization algorithm does not decide what a system should value. It solves a mathematical problem in which someone has already chosen design variables, constraints, objectives, and the relationship between the variables and system behavior. The central reasoning challenge is therefore formulation. A perfectly implemented solver can reliably select a physically impossible design if the engineering model omits a charging constraint, or a socially unacceptable design if accessibility is left out of the objective and constraints.

### Feasibility precedes preference

Let \(x\) denote design decisions such as fleet size, battery capacity, number of chargers, and dispatch policy. Let \(g_i(x)\leq0\) represent hard constraints and \(f_j(x)\) represent objective measures. The **feasible set** is \(\mathcal F=\{x:g_i(x)\leq0,\ i=1,\ldots,m\}\). Only designs in \(\mathcal F\) should be compared using ordinary preference weights if the constraints are truly mandatory. Putting a life-safety requirement into a weighted average alongside acquisition cost permits a sufficiently cheap unsafe alternative to win, which contradicts the requirement's intended status.

Feasibility may be difficult to determine because constraints are state-dependent. A battery that supports a nominal 100-km duty cycle may be inadequate at low temperature, under degradation, with cabin heating and grade changes. If power use is represented by a model \(E(x,s)\) for scenario \(s\), a robust energy constraint might require \(E(x,s)\leq E_{\rm usable}(x,s)\) for every scenario in a defined uncertainty set. The answer depends critically on which scenarios are included. Robustness against an unlimited uncertainty set may be impossible or prohibitively expensive; robustness against a narrow set can be illusory.

### Pareto efficiency has a precise but limited meaning

A feasible design \(x_a\) dominates another feasible design \(x_b\) for objectives to be minimized when it is no worse in every objective and strictly better in at least one. A design is Pareto efficient when no feasible alternative dominates it. This definition can identify choices worth discussing, but a Pareto-efficient design is not automatically good: an entire frontier may fail stakeholder aspirations, or an ethically unacceptable attribute may have been excluded from the model.

Weighted sums \(\sum_j w_j f_j(x)\) can generate some efficient designs when weights are nonnegative and objectives are properly scaled. But weighting is sensitive to units; combining dollars with minutes without normalization or a value function makes weights hard to interpret. In a nonconvex feasible-objective region, some efficient points cannot be recovered by any weighted-sum choice. Methods such as the epsilon-constraint approach can reveal those unsupported points by optimizing one objective while bounding the others.

### Why marginal tradeoffs matter

For a smooth single-objective constrained optimization, Karush–Kuhn–Tucker conditions characterize candidate optima under appropriate regularity assumptions. The Lagrangian for inequalities \(g_i(x)\leq0\) can be written \(\mathcal L(x,\lambda)=f(x)+\sum_i\lambda_i g_i(x)\), with \(\lambda_i\geq0\). At a regular local optimum, stationarity and complementary slackness give clues about active constraints and **shadow prices**. A nonzero multiplier can indicate how much objective improvement may be available from a small relaxation of a constraint, locally and under the model's assumptions.

But engineering design spaces are often discrete, discontinuous, and mixed-integer: one cannot purchase 2.4 charging stations. Local derivatives may be unavailable, and KKT conditions do not guarantee a globally best choice. The useful conceptual takeaway is not memorizing an optimizer's equations; it is learning to ask which constraint limits performance, whether the limitation is physical or policy-imposed, and how sensitive the selected design is to that boundary.

### Decision robustness versus model robustness

A design may remain feasible under uncertainty while its preference ranking changes sharply. Consider two vehicles: a low-cost, low-capacity option and a high-cost, higher-capacity option. Both may meet minimum service in every modeled scenario, yet their economic attractiveness can reverse if demand grows by only 10%. This is **decision sensitivity**, distinct from whether the computational solver converged. A robust decision report should show the feasible region, competing objectives, uncertainty assumptions, and conditions under which a different alternative becomes preferred.

Optimization is most valuable when it reveals the structure of disagreement: which constraints are binding, what resources buy the largest improvements, and which choices depend on contested values. It should narrow and clarify engineering judgment, not replace it with an unexplained scalar score.

## Worked engineering example from the course

A design vector includes architecture ID, fleet size, charger count, reserve ratio, zone count, and speed. Objectives minimize lifecycle cost, accessible wait, emissions, and service disruption while meeting safety, coverage, and deployment constraints. Repeated search seeds produce similar core frontier regions but disagree at high-automation designs, triggering more sampling.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Optimize a candidate with cost C(x)=100+12x and expected wait W(x)=35/(1+x), x≥0 fleet equivalents. The marginal cost is +12 per x, wait improvement decreases as x increases. Without an explicit value or constraint, there is no unique best x.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A design succeeds with probability 0.8 for benefit $500k, otherwise loses $100k. What is expected value before acquisition cost?

<details><summary>Show a reasoned solution</summary>

EV=0.8×500k+0.2×(−100k)=$380k. A risk-averse or budget-constrained decision maker may still reject it.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Categorical variables are treated as meaningful numeric distances.
* Constraint violations enter the feasible frontier unnoticed.
* One algorithm run is accepted without checks.
* Convergence is claimed as proof of global or decision optimality.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is Pareto rank 1?
2. Why repeat optimization seeds?
3. What is epsilon-constraint?
4. What is a mixed-variable problem?

<details><summary>Explain the answers</summary>

**1. What is Pareto rank 1?** The non-dominated set; later ranks are obtained by removing earlier fronts and repeating.

**2. Why repeat optimization seeds?** To assess stochastic search variability and coverage stability.

**3. What is epsilon-constraint?** Optimize one objective while bounding others at specified levels.

**4. What is a mixed-variable problem?** A design problem containing combinations of continuous, integer, binary, or categorical variables.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 8](../labs/lab-08-formulate-parametric-design-and-conduct-multiobjective-search.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[07 — Previous chapter](07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md) · [09 — Next chapter](09-design-computational-experiments-to-learn-efficiently-from-the-desig.md) · [Book index](../README.md)
