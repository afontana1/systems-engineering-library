# Chapter 09 — Explore the trade space with alternatives, uncertainty, sensitivity, and model-based decision records

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 9 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 9](../labs/lab-09-explore-the-trade-space-with-alternatives-uncertainty-sensitivity-an.md) → attempt the [original Week 9 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w09.md) remains available for a quick recap.

## The decision behind the theory

A deterministic calculation can rank options under one assumption set while hiding reversals across uncertainty, operating conditions, or stakeholder preferences. **Essential question:** Which alternatives are feasible and robust, what drives the result, and what evidence would change the recommendation?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Model alternatives as controlled variation, not copied packages. Separate common content, option points, applicability rules, parameter sets, and alternative-specific rationale.

Define feasibility before preference. Requirements, physical constraints, safety, accessibility, and integration rules can eliminate alternatives before value aggregation.

Run across operating scenarios and uncertainty distributions. Show intervals, probabilities, fronts, and reversal conditions rather than a single ranked score.

Sensitivity analysis should identify important uncertain inputs, model forms, criteria weights, and thresholds. A large local derivative does not automatically mean large decision importance.

Write results back as dated, versioned analysis runs and conclusions. The decision record identifies authority, selected option, conditions, dissent, residual risk, and revisit triggers.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Build executable parametric models with units, provenance, constraints, and linked analytics**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Specify physical architectures, variants, configurations, instances, and lifecycle baselines**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Trade-space exploration separates feasible alternatives from merely attractive parameter combinations.

### Distinguishing related ideas

A parametric model can compute metrics exactly under incorrect assumptions, so optimization must include sensitivity to model discrepancy.

### Interpretation and boundary conditions

Large feasible regions may shrink sharply when common-cause reliability, charging windows or accessibility constraints are included.

## Worked engineering example from the course

Alternatives compare 8/10/12 vehicles, 50/100-kW charging, centralized/federated dispatch, and two accessibility layouts. The deterministic baseline favors 8 vehicles and four 100-kW chargers. Uncertainty analysis shows only a 0.42 probability of meeting winter accessible-wait and availability targets. A 10-vehicle mixed-layout alternative has higher cost but 0.88 joint compliance and lower regret. The ranking reverses if peak demand remains below 102 passengers/hour or if accessible boarding increment falls below 60 seconds. The recommendation becomes a staged 10-vehicle baseline with a demand confirmation gate.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Alternative A has normalized scores (cost 0.8, availability 0.6), B has (0.5, 0.9). With cost weight w, their weighted scores are A = 0.6+0.2w and B = 0.9−0.4w. They tie at w = 0.5. The preferred baseline therefore depends on an explicit stakeholder preference, not model syntax.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A model relation table contains 28 requirements, of which 21 link to at least one test and 18 have both source need and test. Calculate test-link coverage and complete-chain coverage.

<details><summary>Show a reasoned solution</summary>

Test-link coverage = 21/28 = 75%; complete-chain coverage = 18/28 ≈ 64.3%. These are structural metrics, not proof that test quality or need validity is sufficient.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Only one preferred design and cosmetic variations are analyzed.
* A weighted score hides infeasibility or noncompensable constraints.
* Uncertain inputs are fixed without justification.
* The model records the recommendation as an immutable fact without version, authority, or conditions.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is feasibility?
2. What is a decision reversal?
3. What is robustness?
4. Why preserve dissent?

<details><summary>Explain the answers</summary>

**1. What is feasibility?** Satisfaction of mandatory constraints and applicability conditions before preference comparison.

**2. What is a decision reversal?** A change in selected alternative caused by plausible changes in assumptions, evidence, model form, thresholds, or preferences.

**3. What is robustness?** Performance or preference stability across relevant uncertainty, scenarios, and assumptions.

**4. Why preserve dissent?** A minority technical judgment or stakeholder concern may become important when assumptions change.

</details>


## Graduate depth: trade-space decisions as model-dependent inference
### A trade-space model is a map, not the territory

A model-based trade study compares feasible architectures on measures that represent stakeholder objectives. Its apparent precision can hide uncertain definitions, uncertain inputs, and model-form error. Begin by separating variables controlled by the designer, environmental scenarios not controlled by the designer, constraints that cannot be traded away, and objectives that express preferences. For an architecture `x` under scenario `omega`, an outcome model `y = f(x, omega, theta)` depends on parameters `theta` that may be estimated or assumed. The decision is only as trustworthy as the scenario envelope, parameter evidence, and interpretation of each outcome.

Even a perfectly computed Pareto frontier can mislead when essential alternatives are missing. Design-space generation should include plausible architecture families, not only nearby variations of an incumbent concept. Dominance is meaningful only with consistent definitions and scenarios: architecture A dominates B if A is at least as good on all considered objectives and strictly better on at least one, under the chosen comparison convention. An option can dominate on nominal estimates while becoming inferior when uncertainties and tail failures are included.

### Sensitivity analysis must distinguish uncertainty types

Local sensitivity measures how a small change in an input alters an output, often via a derivative such as `partial y / partial theta_i`. Global sensitivity examines variation across a wider input distribution and can capture interactions and nonlinearities. Neither necessarily captures model-form error, such as an omitted common-cause failure or a behavioral response that changes under a new policy. Scenario analysis should therefore challenge the structure of the model, not just perturb the values supplied to it.

In a hypothetical Northstar selection, one concept uses a larger fleet and centralized dispatch; another uses fewer vehicles and local dispatch autonomy. If the demand model assumes independently arriving requests, it may underpredict clustered surges after campus events. A small change in average demand may not reveal that structural error. The correct response is to introduce event-driven demand scenarios, compare model predictions with relevant observations, and disclose how rankings change.

### Decision records should preserve competing rationales

A weighted additive value score `V(x) = sum_i w_i v_i(x)` is interpretable when value scales, independence assumptions, and stakeholder authority are established. Double-counting related measures such as wait time and on-time rate can unintentionally privilege one concern. Hard safety constraints should remain separate from utility. If stakeholder preferences are disputed, report the consequences of plausible weight ranges and seek a governance decision rather than disguising conflict as a single “objective” number.

The trade record should retain model revision, units, scenarios, input provenance, assumption ranges, excluded alternatives, feasibility failures, Pareto reasoning, sensitivity results, and dissent. It should distinguish a robust winner from a fragile favorite that changes with small but credible assumptions. If additional evidence could reverse a consequential decision, the model can guide targeted experiments. Its best outcome is not merely a winner, but a transparent explanation of what makes that winner conditional and what would cause engineers to revisit the choice.

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 9](../labs/lab-09-explore-the-trade-space-with-alternatives-uncertainty-sensitivity-an.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[08 — Previous chapter](08-build-executable-parametric-models-with-units-provenance-constraints.md) · [10 — Next chapter](10-specify-physical-architectures-variants-configurations-instances-and.md) · [Book index](../README.md)
