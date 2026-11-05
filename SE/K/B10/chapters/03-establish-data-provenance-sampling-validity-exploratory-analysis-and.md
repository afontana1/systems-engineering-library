# Chapter 03 — Establish data provenance, sampling validity, exploratory analysis, and measurement uncertainty

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 3 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 3](../labs/lab-03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md) → attempt the [original Week 3 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w03.md) remains available for a quick recap.

## The decision behind the theory

Operational datasets are rarely designed for the analyst's later question. **Essential question:** Which data are fit for the intended analysis, and what bias or uncertainty remains after cleaning?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Data cleaning is an analytic decision. Preserve raw data, create immutable identifiers, and log every transformation, exclusion, unit conversion, merge, and imputation.

Missing completely at random, missing at random conditional on observed information, and missing not at random imply different risks. In engineering operations, missingness often reflects sensor dropout, maintenance, severe conditions, or human reporting behavior and is therefore informative.

Censoring records partial information: a component may still be operating at study end, or an event may be detected only above a threshold. Deleting censored records biases reliability and duration estimates.

Measurement uncertainty begins with a measurement model that relates the reported quantity to sensor, calibration, environmental, resolution, processing, and sampling contributions. Do not mix this uncertainty automatically with population variability.

Exploratory analysis should be reproducible and labeled exploratory. Pre-specify confirmatory analyses after exploration or validate them on held-out or new data.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Characterize probability distributions, tails, dependence, and stochastic performance**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Use estimation, confidence intervals, hypothesis, equivalence, and engineering significance**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Statistical data quality begins before analysis with sampling design, measurement bias, missingness and provenance.

### Distinguishing related ideas

A large dataset is not necessarily representative if it systematically excludes night operations or canceled trips.

### Interpretation and boundary conditions

An elegant confidence interval can precisely quantify variation around a biased sample, which is not the same as uncertainty about the mission population.

## Worked engineering example from the course

A charger log records 41-minute median turnaround. Examination finds that failed sessions were excluded, cold-weather sessions have 18% sensor dropout, and two charger firmware versions use different end-of-charge definitions. A measurement model adds timestamp synchronization, current-sensor calibration, and event-detection uncertainty. Reconstructing failed sessions and stratifying by firmware changes the 95th percentile from 55 to 67 minutes and invalidates the original threshold claim.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

With 15 invalid records among 300 logs, the apparent invalid rate is 5%. But if missing logs occur mainly during outages, excluding them biases failure estimates downward. Record the missingness mechanism before treating 285 records as representative.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A sample of 25 independent results has mean 14 min and sample standard deviation 5 min. Estimate a 95% t interval for the population mean using t(24)≈2.064.

<details><summary>Show a reasoned solution</summary>

Standard error = 5/√25=1; interval ≈ 14±2.064, or [11.936,16.064] minutes, under the sampling assumptions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Raw data are overwritten or transformations cannot be replayed.
* Failed sessions, censored lives, or difficult cases are deleted without bias analysis.
* Firmware or configuration changes are combined as if measurements were identical.
* An imputed dataset is reported without uncertainty or sensitivity analysis.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is censoring?
2. What is selection bias?
3. What is a measurement model?
4. Why preserve raw data?

<details><summary>Explain the answers</summary>

**1. What is censoring?** Partial observation of an outcome, such as knowing a component survived at least until study end.

**2. What is selection bias?** Systematic difference between observed and target populations caused by the observation or inclusion process.

**3. What is a measurement model?** A functional relationship linking the measurand to input quantities and corrections used to evaluate the reported value.

**4. Why preserve raw data?** To maintain auditability, permit reprocessing, and distinguish observations from analyst transformations.

</details>


## Deeper theory: sampling, selection bias, and evidence provenance

### Observed data are filtered versions of the world

Statistical analysis starts before the first formula: it starts with the process that makes an observation available. Define the target population, sampling frame, selection mechanism, measurement procedure, and intended inference. For a mobility service, completed rides are not a representative sample of all attempted journeys if riders abandon requests during long waits. Using only completed rides to estimate wait time excludes precisely the difficult cases. The observed distribution is conditional on being observed; it need not equal the operational distribution a decision maker cares about.

Missingness can be broadly classified as missing completely at random (MCAR), missing at random conditional on observed covariates (MAR), or missing not at random (MNAR). If telemetry fails more often during severe weather or network congestion, the missingness may depend on the outcome of interest. Merely deleting missing records can bias a reliability estimate upward. Imputation methods require assumptions, and no procedure can identify unobserved values from data alone without sufficient structure or external information. Sensitivity analysis should show how conclusions change under plausible missing-data mechanisms.

### Precision and validity answer different questions

A large sample can estimate the wrong quantity very precisely. Suppose 10,000 successful bookings are logged, but 2,000 failed attempts are omitted. The observed completion proportion among logged records is 100%; the actual proportion among attempted bookings is `10,000/12,000 ≈ 83.3%` under this simplified accounting. A narrow confidence interval around the logged proportion would not repair the selection error. Statistical precision describes random variability under a model; validity concerns whether the model and data-generating process support the intended claim.

Dependence also alters uncertainty. Requests from the same rider, route, software build, or weather episode may be correlated. Treating each as independent can make standard errors artificially small. Clustered analyses, stratification, hierarchical models, or block bootstrap methods may better reflect the sampling process, but they require enough independent clusters and credible assumptions. If only two storm events are observed, thousands of within-storm records do not establish broad storm-condition reliability.

### Provenance and reproducibility are part of the evidence claim

An engineering dataset needs data dictionary, unit and timestamp conventions, extraction period, raw-source identifiers, transformation steps, software environment, exclusions, and access-control constraints. A derived metric should be reproducible from an identified source configuration. A dashboard screenshot without a query, denominator, and version cannot be independently audited. Transformations such as joining tables, filtering anomalies, and replacing missing values can change results as much as a new physical measurement.

An evidence review should ask which observations could be missing, what measurement errors are plausible, which assumptions connect the sample to the target population, and whether the conclusion survives reasonable alternative analyses. For Northstar, a trustworthy assessment of pickup wait would include unserved requests, cancellations, demand peaks, accessibility groups, and communication outages, with privacy-preserving aggregation where appropriate. No single cleaning rule or statistical test establishes truth; credible analysis is a chain of bounded inferences from documented observations to a decision.

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 3](../labs/lab-03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[02 — Previous chapter](02-characterize-probability-distributions-tails-dependence-and-stochast.md) · [04 — Next chapter](04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md) · [Book index](../README.md)
