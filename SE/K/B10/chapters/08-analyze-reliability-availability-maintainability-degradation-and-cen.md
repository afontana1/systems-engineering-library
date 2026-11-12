# Chapter 08 — Analyze reliability, availability, maintainability, degradation, and censored evidence

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 8 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 8](../labs/lab-08-analyze-reliability-availability-maintainability-degradation-and-cen.md) → attempt the [original Week 8 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w08.md) remains available for a quick recap.

## The decision behind the theory

Failures, repairs, degradation, and downtime often occur sparsely and under changing exposure. **Essential question:** What reliability and availability claims are supported by the event, exposure, censoring, and maintenance data?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Define the event and exposure. 'Failure rate' is meaningless without what counts as failure, the population, operating state, environment, configuration, and exposure unit.

Reliability concerns successful operation for a duration or mission; availability concerns readiness or uptime and includes restoration. High repairability can improve availability without improving reliability.

Right-censored units contribute survival information. Recurrent failures, repairable systems, and competing failure modes require structures different from simple first-failure life data.

Zero failures provide a bound dependent on exposure and confidence or credibility level, not proof of perfect reliability. Rare-event decisions often need precursor, physics, simulation, or structured prior evidence as well as direct events.

Reliability growth claims require stable definitions, configuration history, test intensity, and evidence that improvements—not reporting changes or easier conditions—explain the trend.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Build and validate performance response models across use and environment**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Propagate uncertainty with analytic Monte Carlo simulation and sensitivity analysis**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Availability joins failure mechanisms to restoration capability

Reliability concerns the probability of performing a required function over a stated duration; availability additionally depends on restoration. A component with frequent but very brief failures may have higher steady-state availability than one with rare, prolonged repairs. The familiar ratio of mean time between failures to the sum of mean time between failures and mean repair time is a special-case long-run model, not a universal guarantee of mission success.

Restoration may require spare parts, trained staff, access permissions, and communications. Those dependencies can be shared across nominally redundant components. A single unavailable technician can create correlated downtime despite independent hardware failures. Reliability and maintainability should therefore be interpreted at mission level and with explicit repair logistics. Censored test evidence, changing operating conditions, and aging can invalidate simple constant-rate assumptions. Engineering analysis needs to distinguish the mathematical model from the actual restoration process it purports to describe.

## Deeper theory: reliability data are observations of survival under exposure

### Censoring is information, not a missing zero

Suppose ten components are tested for 1,000 hours, and only two fail while the other eight remain functional when the test ends. The unfailed units are *right-censored*: their failure times exceed their observed exposure, but their eventual failure times are unknown. Treating them as failures at 1,000 hours understates life; dropping them entirely wastes exposure and can overstate failure risk. Survival analysis uses both observed failures and censored observation intervals while stating the assumptions that make this valid, including whether censoring is independent of the underlying failure mechanism.

The survival function `S(t) = P(T > t)` gives the probability a unit's lifetime exceeds `t` under specified conditions. The hazard `h(t)` describes an instantaneous conditional failure rate among units still surviving, not the probability of failure in one arbitrary interval. For a constant hazard `λ`, `S(t) = exp(−λt)` and mean life equals `1/λ`, but many real degradation mechanisms have increasing or decreasing hazards. A Weibull model can represent several shapes, yet fitting a flexible distribution to sparse failures does not create information that was never measured.

### Exposure definitions and competing failure modes matter

A vehicle operated 1,000 calendar hours may accumulate only 100 powered motion hours. A motor failure rate per operating hour and an electronics aging rate per calendar time have different exposure bases. Combining them without conversion produces incoherent reliability estimates. Duty-cycle differences, temperature, load, maintenance actions, and manufacturing batches also create heterogeneous populations. The correct analysis may stratify or explicitly model these covariates instead of pooling all observations into one average curve.

Competing risks occur when different failure types can terminate observation. A battery might be replaced for preventive maintenance before a thermal failure can occur; that event changes which failure mechanisms remain observable. Treating such replacement as innocuous censoring without checking assumptions can bias the estimate. Similarly, repairable systems need recurring-event or renewal models rather than a single time-to-first-failure distribution. Reliability, maintainability, and operational availability require linked but distinct representations.

### Design and decision implications are conditional

Consider a nominal constant-failure model with `λ = 0.001` failures per operating hour. It predicts `S(100) ≈ exp(−0.1) ≈ 0.905` over 100 operating hours. That prediction is only for the defined population and conditions; it says nothing directly about safe outcome probability, repair logistics, or mission completion after a fault. Estimating availability from the same failure data requires repair and support information, including detection delay, spares, and return-to-service authorization.

A reliability claim should display confidence bounds, data provenance, censoring rules, exposure normalization, model diagnostics, and possible common causes. Sparse field data sometimes cannot discriminate between an early manufacturing defect regime and wear-out behavior. The appropriate action may be a bounded design decision and targeted monitoring rather than a falsely precise lifetime forecast. Northstar's evidence should make the distinction between observed failures, modeled survival, mission consequences, and accepted operational risk explicit.

## Worked engineering example from the course

Twelve vehicles accumulate 18,000 operating hours with three propulsion interruptions and many censored vehicle histories. A naive estimate divides failures by calendar days. The corrected analysis uses operating exposure, configuration and temperature strata, recurrent-event records, and confidence bounds. Availability is analyzed separately using downtime duration and logistics delay. The evidence supports a charger-interface redesign and spares change but is insufficient to claim the propulsion requirement is met in severe cold.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

If mean time between failure is 200 hours and mean repair time is 10 hours under ideal renewal assumptions, inherent availability is 200/210 ≈ 95.24%. It is not operational availability when logistics delays, shared outages, or planned service are excluded.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** An event occurs 0 times in n=30 independent Bernoulli trials. Compute the exact one-sided 95% upper failure-probability bound.

<details><summary>Show a reasoned solution</summary>

p_upper = 1−0.05^(1/30) ≈ 0.0950. The result does not demonstrate failure probability below 1%.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Censoring changes the likelihood, not just the spreadsheet denominator

A power-module life test has eight units: three failures at 20, 50 and 80 h and five units that have not failed by 100 h. Under an independent, noninformative-censoring exponential model, the likelihood is \(L(\lambda)=\lambda^3e^{-650\lambda}\). Its maximum yields \(\widehat\lambda=3/650\,\mathrm{h}^{-1}\) and \(\widehat R(50)=e^{-150/650}\approx0.7939\). The nonparametric Kaplan–Meier estimator instead gives \(\widehat S(50)=0.75\), with observed risk sets eight then seven units.

Those estimates are conditional on the stated model and exposure accounting. Only three failures occurred, so a strong reliability requirement cannot be certified from a narrow point estimate. Replicate the calculations using [the data and censored-survival method](../../methods/reliability-and-censored-evidence.md), and audit whether censoring is related to deteriorating condition.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Censored units are discarded or treated as failures at study end.
* Calendar time, operating exposure, missions, and fleet population are mixed without definition.
* Zero failures are described as zero risk or complete requirement compliance.
* Reliability and availability are treated as interchangeable.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is reliability?
2. What is availability?
3. What is right censoring?
4. What is hazard?

<details><summary>Explain the answers</summary>

**1. What is reliability?** The probability of performing required functions without failure for a specified time or mission under stated conditions.

**2. What is availability?** The probability or proportion of time a system is in an operable and committable state under stated support conditions.

**3. What is right censoring?** Knowing that an item survived at least to a time without observing its failure time.

**4. What is hazard?** The instantaneous failure tendency conditional on survival to that point.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 8](../labs/lab-08-analyze-reliability-availability-maintainability-degradation-and-cen.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[07 — Previous chapter](07-build-and-validate-performance-response-models-across-use-and-enviro.md) · [09 — Next chapter](09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md) · [Book index](../README.md)


## Extended worked problems and lab

Study the [worked problem workshop on common-cause availability](../practice/availability.md), then complete the [extended laboratory](../practice/lab-availability.md). The exercises are separate from the original assessed coursework.

## Step 03 integrated quantitative case: censored reliability and mission time

The [life-test dataset](../case/reliability-life.csv) records eight synthetic modules. Three fail at 120, 190, and 300 operating hours; the other five remain functioning through 360 hours and are **right-censored**, not successful infinite-life observations.

### Derive the constant-hazard likelihood

Under an exponential lifetime model with independent non-informative censoring, a unit with failure time \(t_i\) contributes \(\lambda e^{-\lambda t_i}\), while a unit censored at \(c_j\) contributes \(e^{-\lambda c_j}\). Thus, up to terms not involving \(\lambda\), \(L(\lambda)\propto\lambda^d e^{-\lambda E}\), where \(d\) is the number of failures and \(E\) is total observed exposure. Differentiating \(\ell=d\log\lambda-\lambda E\) gives \(\widehat\lambda=d/E\).

Here \(E=120+190+300+5(360)=2410\) module-hours and \(d=3\). So \(\widehat\lambda=3/2410=0.0012448\) failures/hour. The modeled 50-hour reliability is

\[
\widehat R(50)=e^{-\widehat\lambda 50}=0.93966.
\]

This is below the hypothetical 0.95 requirement `QA-03`. It is a point estimate under a constant-hazard assumption, **not a measured population reliability** or a precision-certified failure probability.

### Test the censoring and hazard assumptions

Right-censored units must not be counted as failed at 360 hours, nor treated as proof they survive indefinitely. Examine whether the stopped tests were administrative or related to imminent deterioration. A constant hazard assumes memorylessness; wear-out, early-life failures, and fleet heterogeneity can invalidate it. Before using the model in an approval decision, inspect survival curves, failure mechanisms, competing risks, repair histories, and uncertainty intervals, and collect a larger representative sample.

**Exercise and answer.** A student computes \(3/(8\cdot360)=0.0010417\) failures/hour. Why is this wrong? It includes hours that the three failed units did not survive. Only actual observed time at risk belongs in the exposure denominator. Replacing 2410 with 2880 biases the hazard estimate downward.
