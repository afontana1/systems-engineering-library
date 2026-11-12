# Chapter 05 — Converge on a preferred selection using transparent value and decision methods

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 5 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 5](../labs/lab-05-converge-on-a-preferred-selection-using-transparent-value-and-decisi.md) → attempt the [original Week 5 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w05.md) remains available for a quick recap.

## The decision behind the theory

Once the efficient set is known, stakeholders still must express values and accept tradeoffs. **Essential question:** How can the analyst combine performance and preference without hiding compensation, scale effects, or disagreement?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

An additive value model is transparent but assumes preferential conditions and compensability that must be examined.

Weights reflect importance over specified performance ranges, not abstract importance. Swing weighting asks about the value of moving from worst to best on each attribute.

Noncompensable thresholds, veto conditions, lexicographic priorities, or outranking logic may be appropriate for safety, rights, policy, or mission-critical outcomes.

Compare methods to learn whether the recommendation is method-dependent. A disagreement is evidence, not a nuisance to be removed.

Sensitivity includes break-even values: the weight, threshold, cost, or performance at which the preferred alternative changes.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Apply constraints, dominance, and Pareto analysis to the selection problem**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Visualize, communicate, and defend the pilot selection decision**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### A preferred alternative depends on both evidence and preference

A decision method combines descriptions of uncertain consequences with judgments about desirability. Expected value is appropriate only under its assumptions about probabilities and the decision maker's utility. A risk-averse organization may prefer a somewhat lower expected payoff if an adverse tail outcome threatens continuity of service. Conversely, treating any uncertainty as intolerable can prevent valuable learning or investment.

Transparent selection separates *prediction*, *value*, and *authority*. Engineers can estimate costs and performance, but stakeholder governance determines how competing outcomes are valued. Sensitivity analysis reveals which preferences or uncertain parameters drive the ranking. A robust recommendation does not suppress those dependencies; it identifies when another alternative would become preferable. The decision remains a justified choice under stated conditions, not a theorem proving that one design is universally superior.

## Graduate depth: preference aggregation and the conditions for a defensible choice

### Value functions express judgments, not physics

Once a decision-maker has defined a feasible set, selecting among nondominated designs requires an explicit preference structure. A common additive model is `V(x) = sum_i w_i v_i(x_i)`, with weights `w_i` nonnegative and summing to one. This expression is interpretable only when individual value functions, scaling conventions, and the required preference-independence assumptions are justified. A weight is not simply the percentage importance of an objective in everyday language; it encodes the relative value of specified *swings* over specified ranges.

If response time varies from 10 to 20 minutes and annual cost from 5 to 8 million dollars, the weight elicitation must refer to those ranges. Replacing the cost range with 5 to 20 million while retaining the old weights changes the implied tradeoff. An additive model can also fail when objectives interact. For example, improved response time may have far more value for accessible emergency trips than for routine trips; treating average time and accessibility as separable can obscure this complementarity. Multiplicative value models or explicit conditional preferences may better represent the judgment, though they require harder elicitation and validation.

### Risk, uncertainty, and expected utility

The value of an outcome and a choice under risk are not identical concepts. If `x` produces uncertain consequence `z`, expected utility evaluates `E[U(z) | x]` given a credible probability model and a utility function representing attitudes to risk. It is generally wrong to calculate `U(E[z])` and treat it as equivalent: for nonlinear utility, Jensen's inequality shows they can differ. A stakeholder who is highly averse to catastrophic failure may prefer a design with lower average payoff and a much safer lower tail. Regulatory and ethical constraints still sit outside any discretionary utility trade.

Different stakeholders may also have incommensurable concerns. An operator values dispatch workload, passengers value timely access, budget owners value affordability, and safety authorities impose independent approval obligations. A combined score is legitimate only after the decision process states whose preferences count, who can veto an option, and how conflicts are resolved. Averaging scores from unauthorised respondents is not technical consensus. Sensitivity analysis over plausible weights should reveal whether the choice is robust or contested.

### A conditional recommendation, not an artificial winner

Suppose Northstar has two eligible alternatives. Design A has normalized travel-time value 0.9 and cost value 0.5; B has 0.7 and 0.8. With time weight 0.6 and cost weight 0.4, the additive scores are `V(A)=0.74` and `V(B)=0.74`. This is a tie *under these numbers*, not evidence the systems are identical. If the decision is sensitive to a small weight shift, the proper output is a conditional preference, a negotiation about value, or a request for targeted information—not extra decimals.

A good selection record therefore contains eligibility tests, objective ranges, value-function shapes, elicitation participants, decision authority, sensitivity to disputed parameters, and a plan to revisit the choice when evidence changes. It should connect back to Pareto screening and forward to pilot validation. The most important distinction is between an analysis that exposes the consequences of preferences and a calculation that quietly decides those preferences for the stakeholders.

## Worked engineering example from the course

A weighted value model prefers D, but C becomes preferred when deployment urgency receives a high swing weight. A threshold method excludes B because accessible coverage is below 0.90. The decision record reports D as preferred under the sponsor model and C as the robust fallback for accelerated deployment, rather than presenting one universal ranking.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Under additive value, weights need scale meaning: a 0.4 weight on wait and 0.6 on cost is not justified merely by stakeholder rank ordering. Define endpoint ranges and preference tradeoffs; perform switching analysis.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** Alternative A scores 0.8 on cost and 0.6 on reliability, while B scores 0.5 and 0.9. At cost weight w, derive the preference switching point.

<details><summary>Show a reasoned solution</summary>

A=0.6+0.2w; B=0.9−0.4w. Equate them: 0.6w=0.3, so w=0.5. Feasibility and scaling of value scores remain separate questions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Weights are arbitrary or described as objective facts.
* A value model permits compensation across a prohibited threshold.
* Only one method/weight set is shown.
* Stakeholder disagreement is averaged without preserving scenarios.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a swing weight?
2. What is compensability?
3. What is a break-even analysis?
4. Why compare methods?

<details><summary>Explain the answers</summary>

**1. What is a swing weight?** The relative value of moving an attribute across its specified worst-to-best range.

**2. What is compensability?** The assumption that poor performance on one objective can be offset by better performance on another.

**3. What is a break-even analysis?** Finding the parameter or preference value at which the recommended alternative changes.

**4. Why compare methods?** To reveal dependence on method assumptions and decision structure.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 5](../labs/lab-05-converge-on-a-preferred-selection-using-transparent-value-and-decisi.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[04 — Previous chapter](04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md) · [06 — Next chapter](06-visualize-communicate-and-defend-the-pilot-selection-decision.md) · [Book index](../README.md)

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 05

### Transparent additive value with a decision-reversal threshold

After screening, the decision authority must express trade preferences rather than ask the algorithm to invent them. The synthetic weighted-additive value model uses six scaled objectives, explicit fixed anchors, and weights that sum to one; its values have no physical units. Pilot C scores **0.708571**, and pilot D scores **0.724524**, a difference \(\Delta V=0.015952\) in D's favor. That small gap is not a statistical confidence interval, an observed difference, or proof of decision robustness. The [value decomposition](../case/pilot-screening.csv) is reproducible using a single function rather than several inconsistent spreadsheets.

**Worked sensitivity derivation.** Hold the other four weights fixed and shift a preference mass \(\delta\) from waiting-time weight to accessible-coverage weight. The original weights are \(w_{wait}=0.30\) and \(w_{access}=0.28\). D has higher normalized wait value by \((11.2-8.9)/15=0.153333\), but lower accessible-coverage value by \((0.98-0.99)/0.15=-0.066667\). Thus the new difference is
\[
\Delta V(\delta)=0.01595238-\delta(0.153333+0.066667)=0.01595238-0.22\delta.
\]
The scores tie near \(\delta=0.07251\). Shifting only **7.25 percentage points** of weight from waiting time to accessible coverage changes the preference: \(w_{wait}\approx0.22749\), \(w_{access}\approx0.35251\). This reversal is *conditional on the particular value functions, anchors, and feasible alternatives*. It is not a survey result and not a reason to choose whichever weight set favors a sponsor.

### Compensability and outranking checks

An outranking-style review can say “D is preferred on wait, availability and emissions, but C has the stronger accessibility and earlier-deployment case; no final ordering without stakeholder thresholds.” This approach does not demand cardinal trade units for every objective. A veto on insufficient accessible coverage should be enforced before either additive scoring or outranking. Weighted sums may omit supported nondominated points in a nonconvex design frontier; the ranking method is not a replacement for Pareto search in Project 2.

**Exercise and explained solution.** Change only weights to \(w_{wait}=0.20\) and \(w_{access}=0.38\); the remaining weights are unchanged. Which candidate ranks first? **Solution:** This transfers \(\delta=0.10\), so \(\Delta V=0.015952-0.022=-0.006048\). C now outranks D, without any change in hardware, field evidence, or feasibility. A decision report must record the actual approved weights, sensitivity range and any preference disagreements, not merely publish one score.

**When this fails.** Additivity presumes relevant preference independence. If accessible coverage has a discontinuous ethical or legal significance, or if cost includes operational changes already captured by the wait model, a simple sum may be inappropriate. Request a noncompensatory governance decision before merging dimensions. The case includes a [review evidence register](../case/evidence-register.csv) that documents this gap.
