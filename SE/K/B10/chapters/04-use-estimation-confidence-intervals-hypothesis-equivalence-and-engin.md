# Chapter 04 — Use estimation, confidence intervals, hypothesis, equivalence, and engineering significance

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 4 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 4](../labs/lab-04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md) → attempt the [original Week 4 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w04.md) remains available for a quick recap.

## The decision behind the theory

Decision makers often ask whether performance is 'different,' 'good enough,' or 'within margin.' These are not the same question. **Essential question:** Which inferential claim matches the engineering decision, and what precision is required?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Define the estimand before selecting the test. Examples include the difference in 90th-percentile wait under two policies, the accessible-trip success probability in winter, or the maintenance-rate ratio between configurations.

Confidence intervals quantify uncertainty under a sampling and model procedure; they do not assign a simple probability to a fixed parameter under the usual frequentist interpretation. Communicate the engineering range and decision consequence rather than ritual wording.

A superiority test asks whether a difference is supported. Equivalence asks whether performance lies within a predeclared region that is small enough to be operationally unimportant. Noninferiority asks whether a candidate is not worse by more than an accepted margin.

Large samples can make trivial differences statistically significant. Small samples can leave consequential differences uncertain. Always report effect size, interval, threshold or equivalence margin, and decision consequence.

Predeclare primary outcomes and subgroup analyses where possible. If exploration produces a promising claim, label it and seek confirmation rather than presenting it as prespecified evidence.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Establish data provenance, sampling validity, exploratory analysis, and measurement uncertainty**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Design efficient experiments with factors, responses, noise, power, randomization, and blocking**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Inference requires specifying an estimand, a sampling model and a decision threshold before interpreting a confidence interval or test result.

### Distinguishing related ideas

Statistical significance reports incompatibility with a hypothesis under assumptions; it is not a direct measure of engineering importance.

### Interpretation and boundary conditions

A tiny travel-time improvement may be statistically detectable yet operationally irrelevant, while a rare severe failure may demand action despite weak statistical power.


## Deeper theory — statistical inference as a conditional engineering argument

### Estimation is not certification

Statistical methods are often presented as procedures that turn observations into a number and a decision. Their deeper role is to make explicit what can be inferred from incomplete, variable measurements. An observed average is a property of the sample. A confidence interval is produced by a procedure whose long-run coverage has a specified interpretation under a particular sampling model. A test statistic evaluates compatibility of observations with a defined model. None alone proves that the system will perform acceptably in a different population, a degraded configuration or an unrepresented operating condition.

Suppose 30 Northstar trips were completed and their mean waiting time was 8.4 minutes. Does that establish that the service meets a “mean wait below ten minutes” requirement? Not yet. We need to know which trips were sampled, whether cancellations were excluded, whether there were repeated measurements on the same vehicle or route, and how variability enters. A confidence interval for the mean might be narrow if all observations are highly correlated; treating them as independent would create false precision. More decimal places are not more evidence.

### Sampling models are engineering assumptions

A standard interval for a mean with independent observations and approximately appropriate distributional assumptions has the form estimate ± critical value × standard error. The standard error decreases roughly with the square root of sample size. That familiar result can lead to the mistaken belief that simply collecting more data always makes the conclusion reliable. If data are selected only from easy routes, increasing sample size improves precision for the wrong population. If the sensor has a stable calibration bias, repeated measurements make the biased estimate look extremely certain. If failures cluster during rare weather events, independent-trial formulas understate tail uncertainty.

Two uncertainty classes should be distinguished. **Aleatory variability** represents variation in phenomena such as demand, weather and service times. **Epistemic uncertainty** reflects limited knowledge of model structure, parameters, calibration or operating scenarios. More representative data may reduce epistemic uncertainty about a parameter, but it does not abolish intrinsic variability. A design can have precise estimates of its own unreliability. Statistical inference informs decisions only when both types of uncertainty are appropriately acknowledged.

### Null-hypothesis tests answer narrower questions than engineers ask

A p-value is the probability, *under the specified null model*, of an outcome at least as extreme as the observed one according to the chosen statistic. It is not the probability the null hypothesis is true. Failure to reject a difference is not evidence of equivalence. A small p-value can accompany a practically trivial effect when the sample is huge, and a consequential difference may be statistically inconclusive when the sample is small.

Suppose a redesigned dispatcher reduces mean response time by 0.1 seconds with a very small p-value. The change may be irrelevant if the system-level latency budget has two seconds of margin. Conversely, an increase of 1.5 seconds under rare overload may threaten an emergency response requirement even if an underpowered test cannot reject a zero-effect null. Engineering significance requires an independently justified threshold tied to system consequences.

### Equivalence and noninferiority express different claims

A conventional difference test usually considers a null of no difference. **Equivalence testing** asks whether the true difference lies inside a prespecified acceptable interval, for example between -0.5 and +0.5 seconds. It generally uses two one-sided tests, or the corresponding confidence-interval criterion. **Noninferiority** asks whether a new design is no worse than a comparator by more than a specified margin, often relevant when the new design improves cost or maintainability. The margin must be chosen from engineering consequences *before* observing the data. Choosing it afterward to declare success undermines the decision.

For a safety-critical replacement, statistical equivalence of one performance measure is rarely enough. An alternate dispatch algorithm might match average latency but introduce a new failure mode during communication loss. Quantitative comparison must be situated within architecture, hazard analysis and configuration control.

### Exact zero-failure evidence and its limits

If failure probability is a constant \(p\), trials are independent and each trial represents the same population, the probability of observing zero failures in \(n\) trials is \((1-p)^n\). A one-sided 95% upper confidence bound solves \((1-p_U)^n=0.05\), giving

\[
p_U=1-0.05^{1/n}.
\]

For 60 zero-failure trials, the bound is about 4.87%. To make the upper bound no greater than 1% with zero observed failures requires at least

\[
n\geq\frac{\log(0.05)}{\log(0.99)}\approx 298.1,
\]

so 299 independent representative successes. This is a *sample-size calculation under the model*, not a certification recipe for every operating condition. A thousand nominal trials may say little about a failure mode triggered only by stale credentials and simultaneous vehicle outage.

### The real role of statistical evidence

An engineering decision combines an estimate, its uncertainty, a loss or acceptance criterion, and an explicit operational domain. Statistical evidence should be connected to the requirement being evaluated, the configuration tested, the populations represented and the modes excluded. Confidence intervals quantify one form of uncertainty under a sampling procedure. They do not validate the physics, make a biased sample representative or resolve stakeholder disagreement about acceptable risk. The mature question is therefore not “Is the p-value below 0.05?” but “What bounded claim does this evidence support, which assumptions make that claim true, and what decision follows if those assumptions fail?”

## Worked engineering example from the course

An upgraded dispatcher reduces mean wait by 0.4 minutes with p < 0.001 across 24,000 trips. The improvement is statistically clear but below the predeclared 1.0-minute practical threshold, while the 90th-percentile wait in the accessibility subgroup improves by 2.8 minutes with a wider interval. The engineering decision therefore depends on tail and subgroup estimands, not the overall mean p-value.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

An estimated mean reduction of 0.4 minutes with 95% CI [0.1,0.7] can be statistically distinguishable from zero yet below a 1-minute engineering threshold. Failure to reject a difference is not an equivalence test; predefine the equivalence region.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** An event occurs 0 times in n=30 independent Bernoulli trials. Compute the exact one-sided 95% upper failure-probability bound.

<details><summary>Show a reasoned solution</summary>

p_upper = 1−0.05^(1/30) ≈ 0.0950. The result does not demonstrate failure probability below 1%.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Failure to reject a difference is reported as proof of equivalence.
* A p-value is reported without effect size and interval.
* The overall average is allowed to override a critical subgroup or tail requirement.
* Exploratory subgroup findings are presented as prespecified confirmation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is an estimand?
2. What does a confidence interval communicate?
3. Why is p < 0.05 insufficient?
4. What is equivalence testing?

<details><summary>Explain the answers</summary>

**1. What is an estimand?** The precisely defined quantity the analysis seeks to estimate for a target population and condition.

**2. What does a confidence interval communicate?** The range produced by a procedure with stated long-run coverage under its assumptions, used to assess plausible engineering values and precision.

**3. Why is p < 0.05 insufficient?** It does not establish effect importance, model validity, requirement compliance, or decision value.

**4. What is equivalence testing?** Testing whether a difference lies inside a predeclared region of practical equivalence rather than merely failing to find a difference.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 4](../labs/lab-04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[03 — Previous chapter](03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md) · [05 — Next chapter](05-design-efficient-experiments-with-factors-responses-noise-power-rand.md) · [Book index](../README.md)
