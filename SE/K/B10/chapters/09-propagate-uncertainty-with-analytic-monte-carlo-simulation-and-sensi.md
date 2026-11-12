# Chapter 09 — Propagate uncertainty with analytic Monte Carlo simulation and sensitivity analysis

*Book 10 · EN.645.756 · Metrics, Modeling and Simulation for Systems Engineering · Week 9 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 9](../labs/lab-09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md) → attempt the [original Week 9 assessment](../../../C/P3/EN645756.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-756-w09.md) remains available for a quick recap.

## The decision behind the theory

Performance models combine uncertain demand, weather, component behavior, measurement, parameters, and future conditions. **Essential question:** What distribution of system outcomes follows from the controlled uncertainty model, and which inputs drive the result?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the metrics, modeling and simulation for systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Write the analytic model as a traceable set of equations or functions before running it. Each input must map to a measure, model, source, unit, and uncertainty type.

Avoid double counting. Parameter uncertainty about a distribution, operational variability drawn from that distribution, and measurement error on observed data are distinct layers.

Model dependence explicitly through conditional models, common drivers, copulas, or empirical joint sampling. Verify that generated samples reproduce intended marginal and joint behavior.

Monte Carlo error is not system uncertainty. Quantify numerical precision with repeated batches, standard errors, interval estimates, or convergence plots for the actual output statistic, especially quantiles and small probabilities.

Local sensitivity asks how output changes near one point; global sensitivity apportions variation over an input space and can capture interactions. Sensitivity depends on the specified ranges and distributions and is not a universal property of the system.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Analyze reliability, availability, maintainability, degradation, and censored evidence**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Quantify requirement compliance, technical margin, allocation risk, and design options**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Uncertainty propagation carries distributions and dependencies through an engineering model; it cannot repair missing causal mechanisms.

### Distinguishing related ideas

Assuming independent battery, weather and demand factors may understate tail risk when bad conditions occur together.

### Interpretation and boundary conditions

Sensitivity should distinguish variation intrinsic to operations from uncertainty due to incomplete knowledge; they support different remedies.

## Deeper theory: uncertainty propagation is about the decision, not the histogram

### Separate random variation from uncertainty about the model

Aleatory uncertainty represents variability in the modeled operating process, such as passenger arrivals under defined conditions. Epistemic uncertainty represents imperfect knowledge of parameters, structure, or applicability; it may be reduced through better observations or modeling. The distinction depends on the chosen representation and decision horizon. A fixed but unknown battery degradation rate may be epistemically uncertain even when future passenger demand is treated as aleatory. Mixing them into one distribution can hide whether more data or a design change could resolve the issue.

For output `Y=f(X)`, a first-order uncertainty approximation is `Var(Y) ≈ J Σ Jᵀ`, where `J` is the gradient of `f` with respect to the inputs and `Σ` is their covariance matrix. The off-diagonal terms matter: shared demand surges can increase both energy use and service delay. This approximation assumes the local linearization is adequate. Near a capacity threshold or mode switch, a small input change may cause an abrupt output change; direct simulation across modes may be needed to characterize the decision risk.

### Monte Carlo precision is not model credibility

Monte Carlo draws uncertain inputs, runs the model, and summarizes the resulting output distribution. It is attractive because nonlinear and coupled models can be used without analytic integration. Yet a million simulation runs only reduce numerical sampling error around the distribution implied by the assumed inputs and model. They do not correct a missing failure mechanism, erroneous covariance, or a workload profile that excludes stressful operating conditions. For an estimated probability `p` from `N` independent Bernoulli trials, the approximate standard error is `sqrt(p(1−p)/N)`; this numerical uncertainty differs from uncertainty about the true probability.

Rare adverse events are particularly costly to estimate by naive random sampling. If failure probability is on the order of one in a million, a million trials may observe only about one event on average, giving a highly unstable estimate. Importance sampling or targeted stress scenarios can improve efficiency if probability weights are constructed correctly and validated. Reporting “no failures in the simulation” is not a safety argument when the sampled event is rarer than the simulation can resolve.

### Global sensitivity and decision sensitivity answer different questions

A local derivative describes near-baseline influence; variance-based global sensitivity quantifies contribution to output variability over a declared input space and distribution. Both can be misleading if parameters are dependent and the method assumes independence. A variable can contribute little to average output variance yet dominate the probability of crossing a critical safety threshold. Therefore, analyze quantities tied to the decision: `P(response > limit)`, expected service shortfall, worst credible consequence, or probability of one concept outperforming another.

Northstar might find that routine energy demand uncertainty changes the median battery reserve only slightly, while cold-weather heating uncertainty determines whether the minimum reserve constraint is violated. The responsible report separates numerical error, parameter uncertainty, structural model discrepancy, and scenario applicability; it shows which new evidence would alter the recommended design. Sensitivity analysis matters when it directs attention to assumptions worth resolving, not when it merely ranks inputs in a visually attractive bar chart.

## Worked engineering example from the course

The analytic model predicts 90th-percentile wait, energy use, availability, and accessible-trip fulfillment from demand, weather, fleet configuration, boarding distributions, charging behavior, and failure/repair models. Independent sampling estimates 4% probability of wait noncompliance; dependent weather-demand sampling raises it to 13%. Sobol analysis identifies demand-weather interaction and cold charging time as dominant, while vehicle-count uncertainty dominates only near the capacity threshold. Replicate batches show that 100,000 runs are adequate for the compliance probability but not for an extremely rare safety-event estimate.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

With standard deviations σA=3, σB=4 and correlation ρ=0.6, σ(A+B)=√(9+16+2×0.6×3×4)=√39.4≈6.28. Treating inputs as independent would yield 5 and underestimate aggregate dispersion.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A sample of 25 independent results has mean 14 min and sample standard deviation 5 min. Estimate a 95% t interval for the population mean using t(24)≈2.064.

<details><summary>Show a reasoned solution</summary>

Standard error = 5/√25=1; interval ≈ 14±2.064, or [11.936,16.064] minutes, under the sampling assumptions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Phase 3 technical reference: Derive covariance propagation and verify the tail by simulation

For \(T=D/V\), the gradient at mean \((120,12)\) is \(g=(1/12,-120/12^2)\). Therefore, \(\operatorname{Var}(T)\approx g^\mathsf T\Sigma g\). With input SDs 6 and 1.2 and \(\rho=-0.6\), the distance contribution is 0.25, speed contribution 1.00, and cross term **+0.60 seconds squared**; the resulting \(u_T\approx1.360\) s. Sampling independent marginals would remove the cross term and model a different environment. The [complete Monte Carlo study](../../methods/correlated-uncertainty-propagation.md) draws correlated inputs explicitly and reports \(\hat P(T>12\text{ s})=0.09694\) with Monte Carlo standard error ~0.000936. This numerical SE is not uncertainty about the assumed correlation, distributions, or structural form.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Correlated inputs are sampled independently without consequence analysis.
* The same uncertainty is included twice under different names.
* A large run count is cited without precision or convergence evidence for the target statistic.
* Sensitivity indices are interpreted without stating input ranges and distributions.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does Monte Carlo simulation do?
2. What is Monte Carlo error?
3. Why model dependence?
4. What is global sensitivity?

<details><summary>Explain the answers</summary>

**1. What does Monte Carlo simulation do?** It numerically propagates specified uncertain inputs through a model to estimate a distribution or statistic of outputs.

**2. What is Monte Carlo error?** Numerical sampling uncertainty in the estimated output statistic, distinct from modeled system uncertainty.

**3. Why model dependence?** Joint extremes and common causes can materially change output variance, tails, and compliance probability.

**4. What is global sensitivity?** Analysis of how output variation over a specified input space is associated with individual inputs and interactions.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 9](../labs/lab-09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[08 — Previous chapter](08-analyze-reliability-availability-maintainability-degradation-and-cen.md) · [10 — Next chapter](10-quantify-requirement-compliance-technical-margin-allocation-risk-and.md) · [Book index](../README.md)

## Phase 5 technical reading: Separate input uncertainty from the simulation estimator

For a stochastic output \(Y=g(\theta,U)\), the variability conditional on a fixed calibrated parameter \(\theta\) is not the same as the additional uncertainty about \(\theta\) inferred from finite observations. Under a parameter distribution, total variance decomposes into expected conditional variability plus the variability of the conditional mean. A calibration profile interval for \(\lambda=9\) arrivals/hour demonstrates uncertainty that cannot be eliminated by taking more random simulation seeds. A [worked likelihood and importance-sampling extension](../../methods/simulation-calibration-and-rare-events.md) connects these ideas with statistical intervals, rare-event variance and structural sensitivity.

## Step 03 integrated quantitative case: correlated uncertainty and tail risk

The synthetic winter energy model in [model-assumptions.json](../case/model-assumptions.json) is

\[
E=25+0.4D+0.8H\quad\text{kWh},
\]

where \(D\) is zero-mean route-distance deviation in km and \(H\) is zero-mean heating-hours deviation in hours. Set \(\sigma_D=4\) km, \(\sigma_H=1.5\) hours and \(\rho(D,H)=0.6\). Units of the slopes are kWh/km and kWh/hour respectively; never add unscaled distance to energy.

### Work the covariance, not merely the nominal value

The distance contribution to standard deviation is \(0.4(4)=1.6\) kWh; heating contributes \(0.8(1.5)=1.2\) kWh. Therefore

\[
\operatorname{Var}(E)=1.6^2+1.2^2+2(0.6)(1.6)(1.2)=6.304\;\text{kWh}^2.
\]

The resulting standard deviation is 2.5108 kWh. If the joint input distribution is Gaussian and the linear representation is valid, \(q_{.95}(E)=25+1.64485(2.5108)=29.1299\) kWh, exceeding the `QA-02` cap of 29 kWh. Under a *different assumption* of independent inputs, the standard deviation would be 2.0 kWh and p95 would be 28.2897 kWh. The choice of dependence assumption reverses the model-screen result.

### Monte Carlo cross-check versus model credibility

For a reproducible stochastic check, draw independent standard normal \(Z_1,Z_2\); set \(D=4Z_1\), \(H=1.5(0.6Z_1+0.8Z_2)\), then evaluate \(E\) and compare its empirical p95 with the analytic 29.13 kWh. Report the random seed, number of draws, convergence of the empirical p95, and Monte Carlo sampling error. Agreement between code and algebra checks implementation; it does **not validate the input distribution, its correlation, or physical causation**.

**Exercise and answer.** A team samples \(D\) and \(H\) independently and announces a 0.71 kWh margin to the 29 kWh cap. Explain the flaw. They implicitly fixed correlation to zero. The stated evidence supports positive dependence, making the modeled p95 approximately 0.13 kWh *above* the limit. Quantify correlation sensitivity and gather joint field data before any acceptance claim.
