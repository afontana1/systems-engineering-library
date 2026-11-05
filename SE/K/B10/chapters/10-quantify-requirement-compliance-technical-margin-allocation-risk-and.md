# Chapter 10 — Quantify requirement compliance, technical margin, allocation risk, and design options

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 10 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 10](../labs/lab-10-quantify-requirement-compliance-technical-margin-allocation-risk-and.md) → attempt the [original Week 10 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w10.md) remains available for a quick recap.

## The decision behind the theory

Requirements and budgets are often treated as deterministic lines even when performance and conditions are uncertain. **Essential question:** What is the probability of satisfying critical requirements, how much usable margin exists, and which design action most improves the evidence?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Convert requirement text into a measurable event with population, conditions, configuration, time basis, and method. A probability of compliance without these conditions is not reviewable.

Separate outcome variability from uncertainty in the estimated probability. Report both the estimated compliance probability and the precision or credibility of that estimate.

Margin is the difference between requirement limit and predicted or measured performance under a stated convention. Choose whether the comparison uses mean, percentile, confidence bound, worst credible case, or another approved basis and do not mix them.

Subsystem budgets are correlated through common environment, use, architecture, and measurement. Root-sum-square or simple addition is not automatically valid. Model covariance and shared drivers.

Compare options under the same input assumptions and decision measures. An option that improves average performance but worsens accessible-service tails or maintenance risk may not be preferred.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Propagate uncertainty with analytic Monte Carlo simulation and sensitivity analysis**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Update lifecycle evidence and decide among upgrade, replacement, retirement, or more information**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Technical margin is a resource relative to a threshold, and its meaning depends on the distribution and correlation of loads.

### Distinguishing related ideas

Subtracting mean demand from nominal capacity produces a number but not a defensible probability of compliance.

### Interpretation and boundary conditions

Allocate margin with uncertainty and shared dependencies in view, especially when multiple subsystems draw from the same power or timing budget.

## Deeper theory: compliance margins are probabilistic decision boundaries

### A design margin is not the same as confidence

A margin compares a predicted or measured performance value with a requirement limit. If lower response time is better and the upper allowable limit is L, a nominal margin can be written `M = L - y_nominal`. A positive M indicates nominal clearance, but it does not establish that the actual system will comply. Manufacturing variation, operational conditions, parameter uncertainty, measurement error, and model bias may all move the realized value. Confidence is a statement about the evidence and uncertainty model behind the prediction; margin is a difference on a performance scale.

For a random outcome Y, a chance-constrained requirement might be `P(Y <= L) >= 0.99` for a specified operating population. If Y were normal with known mean mu and standard deviation sigma, this condition would require approximately `mu + 2.326 sigma <= L`. The constant has no force when the distribution is nonnormal, parameters are uncertain, or observations are dependent. It is not a universal safety factor. In real engineering, estimates of mu, sigma, and model bias add uncertainty that must also be addressed.

### Allocation can spend margin without spending it wisely

A system response-time limit can be split among sensing, communications, processing, and actuation. This simplifies organizational responsibility, but can cause suboptimal resource use if allocations are treated as unchangeable entitlements. A subsystem may deliver surplus margin cheaply while another cannot meet its budget without a major redesign. System-level optimization may justify reallocation, provided the overall constraint and evidence remain intact.

Allocation also creates hidden dependencies. A controller that meets its time budget under a dedicated processor may exceed it when security logging and diagnostic services share CPU time. Component timing distributions can be correlated by common load, so adding nominal budgets or separate 99th percentiles may understate total failure probability. Sensitivity analysis identifies which factors threaten the whole-system margin, rather than treating every local shortfall as equally important.

### Reliability evidence and compliance are different claims

A demonstration that all observed runs meet a limit supports an inference about the sampled configurations and conditions. It does not guarantee compliance in every possible mission. If the operational requirement concerns a 99th percentile, a statistically justified test plan needs enough independent and representative observations to bound that percentile with stated confidence, or credible analytical support. Test selection, stopping rules, and unobserved failure modes affect that inference.

When system behavior is safety critical, rare catastrophic failure may warrant mechanistic hazard controls rather than reliance on a purely statistical margin. A chance constraint is not a license to accept any outcome at a small probability if the applicable safety requirement forbids it. Decision criteria must distinguish hard constraints, accepted residual risks, and objectives over which tradeoffs are allowed.

### Design options have value under uncertainty

An architecture with slightly higher nominal cost may include a reserved interface, spare computational capacity, or modular component that makes later performance improvement easier. The option is valuable when future evidence could reveal an unfavorable operating condition and the architecture preserves the ability to respond. It is less valuable when the adaptation cannot be completed within the required time or when the reserved flexibility introduces its own failure modes. Comparing options therefore involves expected lifecycle consequences and the cost of switching, not just current margin.

A compliance argument should end with conditional statements: what requirement is addressed, what configuration and workload were examined, what margin exists, how uncertainty was assessed, and which future changes would invalidate the conclusion. This is more informative than marking a requirement green because a calculated number lies on the acceptable side of a threshold.

## Worked engineering example from the course

The wait-time requirement is the 90th percentile ≤ 12 minutes by zone and accessibility class during defined service hours. The simulation estimates 0.87 probability of compliance under the winter demand distribution, with wide uncertainty for one accessibility subgroup. Adding one vehicle raises compliance to 0.95 but increases cost and energy; a dispatch change raises it to 0.93 with lower cost but creates sensitivity to communication latency. The recommended staged option combines dispatch change, targeted vehicle reserve, and additional winter data, with a reopening trigger if subgroup compliance remains below 0.95.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

For an upper-limit requirement L=30 and predicted mean 25 with standard deviation 4, the nominal z margin is (30−25)/4=1.25. If normality and model assumptions hold, the exceedance probability is about 10.6%, not zero simply because the mean is in limit.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** An event occurs 0 times in n=30 independent Bernoulli trials. Compute the exact one-sided 95% upper failure-probability bound.

<details><summary>Show a reasoned solution</summary>

p_upper = 1−0.05^(1/30) ≈ 0.0950. The result does not demonstrate failure probability below 1%.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Mean performance is used to claim a percentile, reliability, or subgroup requirement is met.
* A margin number is reported without defining its statistical and operating basis.
* Subsystem allocations are combined under an unjustified independence assumption.
* A critical subgroup is omitted because its sample or compliance is inconvenient.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is probability of compliance?
2. What is technical margin?
3. Why report conditional compliance?
4. What is allocation risk?

<details><summary>Explain the answers</summary>

**1. What is probability of compliance?** The modeled or estimated probability that a precisely defined requirement event is satisfied under stated populations, conditions, configurations, and uncertainty.

**2. What is technical margin?** A controlled difference between a performance estimate or bound and a requirement or allocation, under a specified calculation convention.

**3. Why report conditional compliance?** Overall compliance can hide failure in zones, weather, configurations, or protected/critical subgroups.

**4. What is allocation risk?** Risk that subsystem budgets, interactions, covariance, or growth cause the system-level requirement to be missed.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 10](../labs/lab-10-quantify-requirement-compliance-technical-margin-allocation-risk-and.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[09 — Previous chapter](09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md) · [11 — Next chapter](11-update-lifecycle-evidence-and-decide-among-upgrade-replacement-retir.md) · [Book index](../README.md)
