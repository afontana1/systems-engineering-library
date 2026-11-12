# Chapter 02 — Translate stakeholder values into objectives, measures, and value structure

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 2 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 2](../labs/lab-02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md) → attempt the [original Week 2 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w02.md) remains available for a quick recap.

## The decision behind the theory

Stakeholder statements often mix desired outcomes, proposed means, thresholds, and slogans. **Essential question:** How can the analyst represent what stakeholders value without confusing ends, means, requirements, and convenient metrics?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Fundamental objectives describe why the decision matters; means objectives describe how a fundamental objective might be achieved. Means can become design assumptions if not challenged.

An objectives hierarchy should be collectively exhaustive enough for the decision and minimally redundant. Perfect independence is rare, but double counting must be diagnosed.

Constraints define infeasible or unacceptable regions. Tradeable objectives express preference among feasible alternatives. A threshold may be a requirement, policy, or stakeholder preference; label the authority.

Measures need definition, unit, scale, direction, range, source, uncertainty, timing, and owner. Proxy measures require an explicit causal rationale.

Value functions translate performance into preference for one objective. Nonlinearity represents diminishing returns, thresholds, or aversion—not physical behavior.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Frame the decision, distinguish problem types, and expose decision-process risk**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Model decisions, uncertainties, evidence, constraints, and alternatives**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Objectives and metrics encode a value model

An objective describes what the decision maker values; a metric is an imperfect observation or proxy for that value. “Accessible transportation” may be represented by average wait, service area coverage, reliability for disabled riders, or proportion of missed essential trips. These metrics are related but not interchangeable. Selecting one without examining what it omits can lead to a mathematically optimized yet socially undesirable result.

Value modeling requires explicit tradeoffs and attention to nonlinear preferences. Reducing a wait from 60 to 45 minutes may matter much more than reducing one from five to zero. A score that treats both as equal absolute improvements may misrepresent stakeholder preference. Constraints should also be separated from preferences: the obligation not to violate a safety rule is not simply a criterion to be outweighed by cost. Decision science clarifies whose value function is being represented and which outcomes cannot legitimately be traded away.

## Graduate depth: constructing value functions without hiding preferences

### From stakeholder language to measurable consequences

An objective hierarchy translates expressions such as 'safe, affordable, accessible service' into consequences that can be distinguished and compared. A *fundamental objective* describes a reason for caring about a decision; a *means objective* describes an action or intermediate mechanism that might help achieve it. 'Reduce preventable harm' is fundamental; 'add a second dispatch console' is a means that can succeed or fail. Mixing the two allows the proposed solution to become its own justification. A good hierarchy first asks what outcome is valued, then what attributes demonstrate that outcome, and only then which designs can affect those attributes.

Measures must have explicit direction, unit, population, time horizon, and observability. An average wait of ten minutes can coexist with unacceptable long waits for remote users; availability measured during routine hours may miss crisis-period failure. Define operational measures and, when necessary, distributions rather than averages. A measure is a proxy for value, not value itself. Choosing it is a substantive modeling decision that warrants stakeholder review.

### Utility, scaling, and independence assumptions

To combine consequences, one may transform each attribute `x_i` into a scaled value `v_i(x_i)` and consider an additive score `V(x) = sum(w_i * v_i(x_i))`. This is not justified merely because weighted sums are easy to calculate. Its interpretability depends on conditions about preferences over tradeoffs and, for uncertain outcomes, utility independence. If a small increase in cost becomes unacceptable when safety is poor, preferences involve an interaction that an additive expression cannot capture. The scale endpoints and elicitation procedure matter as much as the weights.

Weights are not intrinsic importance percentages. In a swing-weight procedure, they refer to the value of moving an attribute from its defined worst to best reference level. If the reference range for wait time changes, an elicited weight may change even though stakeholders' underlying values have not. A statement that 'safety is 40%' is meaningless without specified consequence ranges and a model for tradeoffs. Hard safety or accessibility obligations should remain constraints, not merely terms that can be offset with enough convenience or cost benefit.

### Preference uncertainty and stakeholder disagreement

An engineering team can estimate travel time, maintenance cost, and reliability; it cannot infer a legitimate community's tradeoffs solely from technical data. Elicitation often reveals incompatible stakeholder perspectives rather than a single hidden 'true' preference. One approach represents weight ranges or distinct stakeholder value functions and reports where alternatives are preferred under each. Another uses outranking or deliberative approaches that allow non-compensatory concerns. A decision-support model helps expose disagreement; it does not eliminate questions of representation, authority, or fairness.

Sensitivity analysis should probe structural preferences, not only shift weights by arbitrary percentages. Ask whether a nonlinear penalty for waits over thirty minutes reverses the choice. Ask whether cost is an annual budget constraint or a long-term present-value outcome. Ask whether the most vulnerable population is considered through its own attribute rather than diluted into an overall average. If rankings change substantially, the next step may be stakeholder deliberation, not another decimal place of performance simulation.

### Example: what a Northstar score conceals

Imagine two fictional service concepts: A has lower mean wait and higher operating cost; B has a slightly longer mean wait but markedly fewer extreme waits for remote users. A weighted mean-wait/cost score could prefer A, while a distribution-sensitive, equity-constrained assessment prefers B. Neither result is mathematically contradictory: they encode different objective structures. The engineering task is to identify which structure corresponds to authorized stakeholder values and which consequences are backed by data.

A defensible value analysis documents the hierarchy, attribute definitions, scale transformations, reference ranges, elicited judgments, feasible-set constraints, and results under competing preference models. It reports *conditional preference*, not an allegedly objective winner. This perspective connects requirements engineering to decision theory: requirements declare eligibility and outcomes, while a value model explains comparisons among eligible choices when objectives conflict.

## Worked engineering example from the course

“Improve accessibility” becomes the fundamental objective “Provide equitable independent mobility.” Means objectives include low-floor vehicles and reservable spaces. Measures include accessible-trip coverage, 90th-percentile accessible wait, failed boarding rate, and user-reported independence. “Use low-floor vehicles” is not retained as a fundamental objective because it prejudges the design.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A value hierarchy maps ends (accessible reliable trips) to means (capacity, availability) and measurable attributes. A cost metric is not a value function: $100k saved may be negligible or decisive depending on budgets and thresholds.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A design succeeds with probability 0.8 for benefit $500k, otherwise loses $100k. What is expected value before acquisition cost?

<details><summary>Show a reasoned solution</summary>

EV=0.8×500k+0.2×(−100k)=$380k. A risk-averse or budget-constrained decision maker may still reject it.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A design feature is treated as a fundamental objective.
* A critical stakeholder outcome has no measure or reason for omission.
* Double-counted measures are aggregated without disclosure.
* Threshold authority is unknown.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a means objective?
2. What is an attribute?
3. Why use a nonlinear value function?
4. What is double counting?

<details><summary>Explain the answers</summary>

**1. What is a means objective?** An objective valued because it contributes to another, more fundamental objective.

**2. What is an attribute?** A scale used to measure achievement of an objective.

**3. Why use a nonlinear value function?** To represent preference that changes nonlinearly over the performance range.

**4. What is double counting?** Giving the same underlying value influence multiple times through redundant measures.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 2](../labs/lab-02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[01 — Previous chapter](01-frame-the-decision-distinguish-problem-types-and-expose-decision-pro.md) · [03 — Next chapter](03-model-decisions-uncertainties-evidence-constraints-and-alternatives.md) · [Book index](../README.md)

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 02

### Elicit fundamental ends before assigning convenient numbers

The fundamental objectives are reliable **on-time movement**, equitable accessible-trip coverage, total resource stewardship, operational safety, environmental consequence, and reversible learning. Fleet size, charger count and autonomy level are **means**—variables that may help attain ends but should not be granted intrinsic utility. A measure dictionary connects each end to an operational definition: 90th-percentile wait has units of minutes and an observation window; accessible-trip coverage is completed eligible accessible trips divided by eligible demand; availability requires a fleet-time denominator; five-year cost is in millions of dollars with a declared boundary; annual emissions must specify an inventory methodology. These course-supplied columns lack an independently verified measurement process. Their appearance in a spreadsheet does not make them field observations.

### Anchored single-attribute value functions

For a cost-type metric with desirable low value \(L\) and adverse high value \(H\), define \(v_\downarrow(x)=\operatorname{clip}((H-x)/(H-L),0,1)\). For beneficial coverage use \(v_\uparrow(x)=\operatorname{clip}((x-L)/(H-L),0,1)\). The [controlled value specification](../case/decision-inputs.json) fixes cost anchors $6M and $12M, wait anchors 7 and 22 minutes, coverage anchors 0.85 and 1.00, deployment anchors 4 and 18 months, availability anchors 0.90 and 0.99, and annual emissions anchors 80 and 220 tCO2e. These are **declared policy anchors**, not fitted sample minima or maxima. Clipping maps out-of-range values to 0 or 1, deliberately hiding extrapolated differences; a real decision study should reconsider anchors when new alternatives lie outside them.

The weight vector \(w=(0.18,0.30,0.28,0.08,0.06,0.10)\) sums to one for the ordered attributes cost, wait, coverage, deployment, availability and emissions. These weights are an *invented* swing-weight illustration, not reported campus stakeholder preferences. In authentic swing weighting, reviewers first compare a full range improvement for each attribute, not arbitrary percentages attached to different units. A simple additive value function \(V=\sum_i w_i v_i\) is defensible only with suitable preferential independence and acceptable compensability. A hard accessibility minimum belongs to the feasible-set definition, not as a score deduction.

**Worked value example.** For pilot C, value contributions for cost, wait and coverage are \(0.18(12-9.4)/6=0.078\), \(0.30(22-11.2)/15=0.216\), and \(0.28(0.99-0.85)/0.15=0.26133\), respectively. Add the other three contributions 0.06286, 0.03467 and 0.05571 to obtain **\(V(C)=0.70857\)**. Compare D's vector and obtain **\(V(D)=0.72452\)**. Neither raw dollars nor minutes should be summed directly with fractions; their dimensionless value functions provide the common scale.

**Worked exercise.** A team proposes to add a “number of chargers” bonus to the score without changing the stakeholder hierarchy. **Solution:** Reject the unexamined addition. Chargers are means to service availability and energy feasibility; scoring chargers *and* measured wait or availability risks double-counting one mechanism. If the team values grid resilience independently, define the additional fundamental objective and an interpretable resilience measure before assigning a defensible weight. The decision authority should approve that change before seeing updated rankings.

**Use limitation.** Accessible coverage in the source table is a forecasted attribute, not an equity audit. The model cannot represent the severity, distribution or rights implications of particular denied trips. Treat accessibility and safety as noncompensatory review requirements, and retain stakeholder dissent as evidence, not numerical noise.
