# Chapter 02 — Characterize probability distributions, tails, dependence, and stochastic performance

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 2 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 2](../labs/lab-02-characterize-probability-distributions-tails-dependence-and-stochast.md) → attempt the [original Week 2 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w02.md) remains available for a quick recap.

## The decision behind the theory

A system is used across variable demand, weather, human behavior, component condition, and mission scenarios. **Essential question:** What probability model represents performance and dependence well enough for the intended engineering decision?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Distribution choice begins with the generating process and support. Counts, proportions, positive durations, bounded capacities, and time-to-event observations require different candidate families.

Fit is not proved by one goodness-of-fit p-value. Use empirical distributions, Q-Q or P-P plots, tail behavior, parameter stability, mechanism, and intended-use consequences.

Mixtures appear when data combine zones, vehicle types, weather regimes, passenger classes, or configurations. A single fitted distribution can hide multimodality and subgroup failure.

Dependence matters in uncertainty propagation. Demand, precipitation, traffic, and charging delay may rise together. Independent sampling can materially understate extreme wait time or energy demand.

Create an uncertainty taxonomy. Aleatory variability may be irreducible for the decision horizon; epistemic uncertainty may be reduced; measurement uncertainty affects observed values; model-form uncertainty reflects alternative plausible representations.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Define the lifecycle technical-measurement strategy and decision chain**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Establish data provenance, sampling validity, exploratory analysis, and measurement uncertainty**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Probability models encode mechanisms and dependence

Selecting a distribution is not a matter of picking a familiar curve. A count of requests over an interval, time until equipment failure, and measurement error arise from different mechanisms. Their supports, tails, and dependence patterns matter. A normal approximation may assign impossible negative values to a nonnegative duration; a Poisson model may be inappropriate when demand arrives in correlated bursts. The analyst should first ask what events generate the variable and what invariants its distribution must respect.

Dependence is often more consequential than marginal distributions. If two service nodes fail during the same network outage, multiplying their independent reliability estimates exaggerates redundancy. If requests arrive together after a public event, average arrival rate can conceal long queues. Probability models are arguments about variability, and their credibility depends on measurement context and exposure conditions. A parameter estimate is not a universal property of a system; it is a property under the sampling and operational assumptions used to infer it.

## Deeper theory: probabilistic performance depends on mechanisms and joint behavior

### A distribution is a scientific hypothesis, not merely a fitted curve

Selecting a probability distribution asserts something about how outcomes arise. A normal model may be reasonable for the sum of many small influences under suitable conditions, but can be inappropriate for nonnegative repair times with heavy right tails. A lognormal model may fit multiplicative effects yet poorly represent a physical upper bound. A mixture model can represent different operational modes whose responses have different mechanisms. The distribution family should be justified by physics, process knowledge, and diagnostic evidence—not only by a high numerical goodness-of-fit score.

If demand has two modes, nominal and peak, a response-time distribution may be written as `F(t) = p F_nominal(t) + (1-p) F_peak(t)`. Its overall average may look acceptable while the peak-mode tail violates an operational requirement. The mixture weight p is itself sensitive to season, class schedules, and policy. Predictions outside the observed operating mix require a credible model of how that mix may change.

### Dependence controls system-level tail risk

Engineering quantities often share drivers: temperature affects battery output and cooling load; congestion affects both packet delay and retry rates; a supplier defect affects multiple components. If X and Y are random delays, `Var(X+Y) = Var(X) + Var(Y) + 2 Cov(X,Y)`. Ignoring positive covariance understates variability of total delay. But covariance alone does not fully describe the chance of joint extreme events. Tail dependence and common-cause scenarios may matter much more for rare mission failures than ordinary correlation coefficients suggest.

Monte Carlo simulation is useful only if joint samples preserve plausible dependence. Independently sampling every marginal distribution can generate an unrealistic world in which shared failures never occur. A common-environment variable, scenario-based sampling, or an explicit dependency model may be needed. Results should expose the assumed dependence structure and test sensitivity to alternatives.

### Rare events demand disproportionate evidence

If a failure probability is 0.001 per mission and trials are independent, the probability of seeing zero failures in 100 trials is approximately `(1 - 0.001)^100`, or 90.5%. Thus a modest clean test campaign provides little evidence that the rare-event probability is truly low. Tail claims need large or strategically chosen data sets, mechanistic analysis, stress testing, and transparent uncertainty bounds. The absence of observed failures is not evidence of impossibility.

The same caution applies to extrapolation. A parametric tail fitted to ordinary delays may predict very rare events, but small model errors can dominate that prediction. Physical bounds, change points, operating modes, and failure mechanisms must be investigated before treating a fitted 99.99th percentile as engineering fact.

### Separate randomness from lack of knowledge

Aleatory variability describes variation expected to remain among operations; epistemic uncertainty describes limited knowledge of parameters, mechanisms, or model form. The distinction matters for interventions. Additional field data may reduce uncertainty about a demand distribution but cannot eliminate natural variation in arrivals. Redesigning capacity or policy can change the operational variability itself. An uncertainty analysis should identify which sources are reducible, which are design-controllable, and which require robust operation.

A useful probabilistic result reports its conditioning: population, mission duration, environment, configuration, and model assumptions. Without this, a numerical failure probability appears portable when it is actually specific to a particular scenario. The most rigorous probabilistic engineering begins by asking what process could generate the observed data and which decisions that process model can safely support.

## Worked engineering example from the course

Trip demand is initially modeled as Poisson and boarding time as lognormal. Diagnostics show strong overdispersion in counts and two boarding-time regimes associated with mobility-device use. Demand and precipitation are dependent. The revised model uses a negative-binomial demand model, a conditional boarding-time model, and a joint resampling or copula approach for demand and weather. The 95th-percentile wait estimate increases because the original independent, single-population model understated concurrent stress.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Suppose a dispatch-time distribution has mean 4 minutes, but 5% of requests wait 25 minutes. The mean is poor evidence for a 95th-percentile target. A second scenario with the same mean can have a different tail; specify quantiles and conditional populations.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** An event occurs 0 times in n=30 independent Bernoulli trials. Compute the exact one-sided 95% upper failure-probability bound.

<details><summary>Show a reasoned solution</summary>

p_upper = 1−0.05^(1/30) ≈ 0.0950. The result does not demonstrate failure probability below 1%.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Phase 3 technical reference: Specify the joint distribution and its physical mechanism

A pair of normally distributed inputs is not fully specified by two marginal means and standard deviations. For illustrative correlation \(\rho\), form \(D=120+6Z_1\) and \(V=12+1.2(\rho Z_1+\sqrt{1-\rho^2}Z_2)\) from independent standard normals. Then \(\operatorname{Cov}(D,V)=\rho(6)(1.2)\), and \(T=D/V\) is nonlinear and may have an asymmetric tail. The [derivation and synthetic results](../../methods/correlated-uncertainty-propagation.md) reveal why the mean of the ratio exceeds the nominal ratio, and why negative correlation pushes the 95th percentile above the independent-input estimate. A normal speed with theoretical nonpositive tail is physically unrealistic and must be assessed or replaced before operational use.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A normal distribution assigns material probability to impossible negative values without treatment.
* A single distribution is fitted across known configurations or populations without checking mixtures.
* Inputs with a common driver are sampled independently despite consequential tail effects.
* Parameter estimates are reported as exact known constants.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a random variable?
2. What is a percentile?
3. What is overdispersion?
4. Why condition a distribution?

<details><summary>Explain the answers</summary>

**1. What is a random variable?** A numerical representation of an uncertain outcome defined on a probability space.

**2. What is a percentile?** A value below which a specified proportion of the modeled or observed population lies.

**3. What is overdispersion?** Variance greater than expected under a reference count model such as Poisson, often indicating heterogeneity or dependence.

**4. Why condition a distribution?** Performance may differ systematically by environment, use, subgroup, or configuration; conditioning avoids mixing distinct regimes.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 2](../labs/lab-02-characterize-probability-distributions-tails-dependence-and-stochast.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[01 — Previous chapter](01-define-the-lifecycle-technical-measurement-strategy-and-decision-cha.md) · [03 — Next chapter](03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md) · [Book index](../README.md)

## Step 03 integrated quantitative case: distributions, mixtures, and tails

The [NS-QA10.1 dossier](../case/INDEX.html) tests command latency under both **mild/cold** operating conditions and **baseline/optimized** controllers. The 24 rows in [factorial-trials.csv](../case/factorial-trials.csv) are balanced experimental illustrations, not an operational population survey.

### Why averages do not define the engineering risk

For a random latency \(T\), a percentile is \(q_p=\inf\{t:F_T(t)\ge p\}\). The 95th percentile is a statement about a cumulative distribution within a defined conditioning set. A two-regime mixture is \(F_T(t)=\pi F_{\rm cold}(t)+(1-\pi)F_{\rm mild}(t)\); **the mixture percentile is generally not the average of the two regime percentiles**. Changing the fraction of cold operations can alter fleet-wide tail behavior even if the conditional distributions remain unchanged.

The synthetic cell means are 440 and 390 ms in mild weather, and 520 and 490 ms in cold weather for baseline and optimized control respectively. These values describe central tendency *within the designed experiment*. They cannot demonstrate `QA-01` because the cold peak sample size is six and the factorial test does not reproduce all field stressors.

### Dependence is part of the model, not an optional embellishment

Route distance and heating hours may share a cold-weather cause. If energy use is linear in those inputs, its variance contains a covariance term: \(\operatorname{Var}(aD+bH)=a^2\sigma_D^2+b^2\sigma_H^2+2ab\rho\sigma_D\sigma_H\). Omitting that term is equivalent to *asserting zero correlation*, not being conservative. In Chapter 9, this changes the modeled energy p95 from 28.29 to 29.13 kWh, across a 29 kWh limit.

### A rare-event calculation

If individual peak-condition exceedances were independent with probability 1%, the probability of zero exceedances in six trials would be \((.99)^6\approx94.15\%\). Observing none would therefore be unsurprising even if the underlying exceedance rate were precisely at the limit. To establish a small risk with confidence, one needs a much larger or differently structured demonstration and careful scrutiny of independence.

**Exercise and answer.** Why should one not pool all 24 factorial runs to estimate the cold optimized p95? Because 18 runs are drawn from *different conditional populations*. The p95 requirement is conditional on cold peak operations, so pooling changes the estimand. State the population, estimand, and sampling assumptions before calculating a percentile.
