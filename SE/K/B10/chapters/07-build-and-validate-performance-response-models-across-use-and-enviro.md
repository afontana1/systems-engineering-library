# Chapter 07 — Build and validate performance response models across use and environment

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 7 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 7](../labs/lab-07-build-and-validate-performance-response-models-across-use-and-enviro.md) → attempt the [original Week 7 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w07.md) remains available for a quick recap.

## The decision behind the theory

Systems engineers need models that predict performance under varying demand, weather, load, design, and condition. **Essential question:** What statistical response model is accurate, interpretable, and valid over the decision region?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Choose the response distribution and link to match the data: continuous energy, positive skewed duration, binary completion, count failures, or proportions may require different models.

Engineering structure should guide variables and interactions. Blind stepwise selection can remove physically important terms, select noise, and understate model uncertainty.

Training fit is not predictive evidence. Reserve time blocks, vehicles, zones, or experimental conditions for validation, and test critical subgroups and tails.

Collinearity may allow good prediction while making individual coefficient interpretation unstable. Report this distinction and avoid causal language unless design supports it.

Publish a validated-domain table specifying ranges, configurations, populations, environments, and known gaps. Prediction beyond that domain is a separate model-use decision.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Analyze factorial experiments, interactions, diagnostics, and confirmation evidence**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Analyze reliability, availability, maintainability, degradation, and censored evidence**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Response models interpolate or approximate performance over a defined region of operating conditions.

### Distinguishing related ideas

A good fit near observed conditions is not evidence of reliable extrapolation into fault states or extreme demand.

### Interpretation and boundary conditions

Examine residual structure and domain boundaries, not just a high coefficient of determination.

## Worked engineering example from the course

A model predicts charging time from temperature, state of charge, charger power, battery age, and their interactions. A simple linear model fits moderately but shows curved residuals and age-by-temperature interaction. A hierarchical polynomial or spline model improves validation error and interval calibration. The team refuses to predict below -12°C because no validation data exist there; instead it identifies an experiment or conservative bound.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A quadratic response model y = 8 + 0.9x − 0.04x² predicts diminishing returns and eventually nonsensical behavior beyond fitted x. Models are local approximations; validate with residuals, holdout scenarios, and physical plausibility, not R² alone.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A sample of 25 independent results has mean 14 min and sample standard deviation 5 min. Estimate a 95% t interval for the population mean using t(24)≈2.064.

<details><summary>Show a reasoned solution</summary>

Standard error = 5/√25=1; interval ≈ 14±2.064, or [11.936,16.064] minutes, under the sampling assumptions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Training fit or R-squared is used as the only validation evidence.
* A model is extrapolated to an unobserved environmental or design region without warning or uncertainty treatment.
* Coefficient association is described as causal without experimental or causal-design support.
* Critical subgroup or tail calibration is ignored.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a prediction interval?
2. What is extrapolation?
3. Why is R-squared insufficient?
4. What is collinearity?

<details><summary>Explain the answers</summary>

**1. What is a prediction interval?** An interval for a future observation that includes both model-estimation uncertainty and outcome variability under the model.

**2. What is extrapolation?** Using a model outside the input, configuration, population, or environmental region supported by development and validation evidence.

**3. Why is R-squared insufficient?** It does not establish correct form, unbiased prediction, valid assumptions, tail calibration, or external performance.

**4. What is collinearity?** Strong relationship among predictors that can make individual effects unstable even when combined prediction is useful.

</details>


## Graduate depth: response surfaces, generalization, and model-form risk
### A fitted model is a hypothesis about a response mechanism

Performance response modeling summarizes how outputs change with design settings, operating conditions, and disturbances. A regression or surrogate model may fit observed data extremely well and still fail outside the experimental domain. The distinction between interpolation and extrapolation is critical: interpolation relies on patterns within represented conditions; extrapolation asks the model to predict where the governing behavior may change. In systems engineering, transitions in operating mode, control saturation, thermal limits, or human behavior are common reasons an apparently smooth model becomes invalid.

A generic response model can be written `y = f(x, z; beta) + epsilon`, with controllable design factors `x`, environmental variables `z`, estimated parameters `beta`, and residual variation `epsilon`. This expression assumes a particular functional form and a residual structure. If residuals depend on load or have persistent temporal correlation, ordinary independent-error confidence intervals can be misleading. Diagnostics should inspect systematic residual patterns, high-leverage observations, heteroscedasticity, and sensitivity to influential points. In time-series settings, training and test data must be separated by deployment-relevant time or group boundaries to avoid leakage.

### Validation is conditional on intended use

A model built to rank two cooling concepts may be adequate even if it cannot predict absolute peak temperatures to a fraction of a degree. A model intended to certify thermal safety needs stronger calibration and uncertainty bounds. Validation criteria should therefore follow the decision, consequence of error, and operating envelope, not a generic threshold on `R^2`. Cross-validation provides evidence about predictive behavior only when the folds reflect how future cases differ from training cases. Randomly splitting nearly identical readings from the same test run often exaggerates generalization.

Consider a Northstar energy-consumption surrogate trained on moderate temperatures and smooth routes. It may rank drivetrain options accurately there but become unreliable in cold weather when heating loads and battery resistance change sharply. A realistic validation design holds out routes, environmental conditions, or hardware configurations likely to be encountered in deployment. It also compares against a physics-based constraint or independent measurement where possible. Agreement between two models sharing the same mistaken assumption is not independent confirmation.

### Predictions need uncertainty envelopes and decision safeguards

Prediction uncertainty has multiple sources: random variability in outcomes, uncertainty in fitted parameters, measurement error, and structural inadequacy. A narrow fitted confidence band may describe uncertainty in the estimated mean while failing to bound an individual future observation. For decisions near a compliance threshold, the relevant question is often the probability of violation or a conservative prediction bound under the specified environment. These quantities depend on the validity of distributional and dependence assumptions.

Model complexity should be chosen by required fidelity, available data, and ability to diagnose errors. More parameters may improve apparent fit while making physical interpretation and robust extrapolation worse. Active learning can target new experiments where uncertainty affects the decision most, but each new measurement must be collected under a controlled configuration. A response model is useful when it states where it works, where it does not, what it predicts, and how its uncertainty should constrain engineering commitments. Its output should inform, not silently replace, engineering judgment.

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 7](../labs/lab-07-build-and-validate-performance-response-models-across-use-and-enviro.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[06 — Previous chapter](06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md) · [08 — Next chapter](08-analyze-reliability-availability-maintainability-degradation-and-cen.md) · [Book index](../README.md)
