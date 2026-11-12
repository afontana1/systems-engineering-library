# Chapter 08 — Analyze transient and steady-state output with defensible run controls

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 8 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 8](../labs/lab-08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md) → attempt the [original Week 8 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w08.md) remains available for a quick recap.

## The decision behind the theory

Simulation produces observations, not answers. **Essential question:** How should warm-up, run length, replications, dependence, intervals, and stopping rules be chosen for the decision claim?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

A terminating simulation has a natural start and end, such as one operating day. A steady-state study estimates long-run behavior after initialization effects decay.

Warm-up removes initial transient observations but also discards data. Choose it from system behavior, plots, multiple runs, and sensitivity—not a convenient fraction.

Independent replications are often the clearest analysis unit. Observations within a run are usually dependent and should not be treated as independent samples.

Quantiles and rare-event measures may require more runs, bootstrapping, specialized estimators, or scenario-based bounds. A narrow mean interval does not validate tail claims.

Precision conditional on the model does not address input, model-form, or scenario uncertainty. Report these separately.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Use simulation for concept exploration, alternatives, and scenario analysis**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Apply simulation in design and development using selection, ranking, and design of experiments**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Simulation output is dependent time-series evidence

A simulation run generates observations whose statistical properties depend on how the model was started and how long it was observed. A queue beginning empty may show artificially low waiting times compared with a real service operating in equilibrium. Discarding an initial warm-up period can reduce initialization bias, but it is inappropriate if the decision concerns an actual service startup. The evaluation horizon must match intended use.

Observations within a run are often correlated; treating every passenger event as an independent replication makes confidence intervals too narrow. Independent replications or appropriately constructed batches address this dependence under explicit assumptions. Longer runs reduce sampling uncertainty about the *modeled* process, not structural uncertainty about whether its rules represent reality. Report run length, initialization, seeds, failure scenarios, and response distributions. A narrow interval around a biased simulation model is not strong evidence about field performance.

## Deeper theory: simulation output is a stochastic process, not a single number

A simulation trace can look precise while containing very little evidence about a long-run service. A reported waiting-time average of 14.2 minutes is the output of a particular initialization, sequence of random events, run length, and observation rule. To interpret it, one must understand **what quantity is being estimated** and the dependence structure of the generated observations. A transient evacuation simulation asks about a finite mission window; a continuously operating dispatch center might ask about long-run performance after initial conditions cease to dominate. These are different statistical objects.

### Initial conditions and the distinction between transient and steady state

Let \(Y(t)\) denote a time-varying performance measure, such as the number of waiting requests. The transient expectation \(E[Y(t)]\) may depend strongly on the initial state. A long-run time average, when it exists, concerns the behavior after sufficient time and under stable operating assumptions. Starting Northstar with an empty queue creates an artificially favorable opening period. Starting with a backlog inherited from the previous shift may create the opposite bias. Discarding a warm-up period can reduce initialization bias for a steady-state study, but doing so in a morning-commute study may remove the actual phenomenon of interest.

A stable long-run regime is not guaranteed. If arrival demand systematically exceeds service capacity, queue length tends to grow rather than settle into a stationary distribution. In an M/M/1 example the utilization ratio is \(\rho=\lambda/\mu\). The familiar steady-state formulas require \(\rho<1\). An analyst who computes a steady-state waiting time at \(\lambda\ge\mu\) is not making a minor numerical error; the assumed stationary operating state does not exist under that model.

### Why many events are not many independent observations

Consecutive waiting times share the same queue history. A long delay leaves work behind, which can cause later delays, so observations within a run are generally serially correlated. The standard error of an average cannot be justified by dividing its raw standard deviation by the square root of the number of events as though events were independent. One remedy is to run multiple **independent replications**, each using a distinct random stream and the same experimental definition. For \(R\) independent replication means \(\bar Y_1,\ldots,\bar Y_R\), uncertainty in the grand mean can be estimated from the variability *between replication means*.

Under the usual approximately normal replication-mean conditions, a two-sided confidence interval is

\[\bar Y\ \pm\ t_{R-1,1-\alpha/2}\frac{s_{\bar Y}}{\sqrt R}.\]

Here \(s_{\bar Y}\) is the sample standard deviation of the replication means, not of every event pooled across runs. The approximation requires enough independent replications and a well-behaved replication-mean distribution. In very rare-event or heavy-tailed settings, specialized methods may be necessary.

### The numerator, denominator, and survival of a metric

Consider two service policies. Policy A completes 95 of 100 requests with a 25-minute average completed-trip wait. Policy B completes 60 of 100 with a 10-minute average among completed trips. It is incorrect to conclude that B is better for riders solely from the smaller mean. The wait statistic conditions on having been served; the 40 unsuccessful requests have vanished from its denominator. A meaningful performance description needs completion fraction, censored and abandoned requests, delay distribution, and potentially subgroup experience. **A metric is an estimand**, a particular quantity defined for a specified population and observation procedure.

The same issue arises with percentiles. A 95th percentile is not a hard maximum, and a 95% confidence interval on the mean is not a 95th-percentile interval. The former describes a tail of the outcome distribution; the latter describes uncertainty about an estimated parameter. Precision about which object is being reported is essential for a credible engineering claim.

### Comparing designs without paying for unnecessary noise

When comparing two fleet designs under uncertain demand, use a common set of sampled demand scenarios for both designs. The paired difference \(D_i=Y_{B,i}-Y_{A,i}\) removes much of the noise contributed by the shared scenario, if the model coupling is implemented correctly. Its variance is

\[\operatorname{Var}(D)=\operatorname{Var}(Y_B)+\operatorname{Var}(Y_A)-2\operatorname{Cov}(Y_A,Y_B).\]

Positive correlation can make paired comparisons more precise. But the pairing must be meaningful: mismatched random-number consumption between event-driven models can inadvertently compare different underlying cases. Common random numbers are a variance-reduction design, not a guarantee of causally matched sample paths.

Finally, **more runs address Monte Carlo uncertainty, not model invalidity**. A highly precise estimate from a model that omits maintenance downtime can be less useful than a less precise estimate from a model representing the important mechanisms. Output analysis is therefore part of an evidence argument: it identifies the parameter being estimated, the population to which it applies, the computational sampling error, and the remaining uncertainty about whether the simulated world matches the real one.

## Worked engineering example from the course

Ten replications produce a tight interval for mean wait but an unstable 90th percentile. Increasing run length does not solve the problem because each day has few tail observations. The analysis uses more independent day replications and bootstrap intervals, and labels rare disruption claims as low confidence.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

If each replication lasts 8 hours and begins empty, initial low congestion biases a long-run steady-state estimate downward. Choose a warm-up based on diagnostics—or explicitly study a finite 8-hour terminating day instead.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A simulation delivers 12, 14, 16, 18, 20 and 22 completed requests in six independent runs. Calculate sample mean.

<details><summary>Show a reasoned solution</summary>

The mean is (12+14+16+18+20+22)/6=17 completed requests. Six replications are insufficient to claim a rare-event guarantee.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Phase 3 technical reference: Independent replication means and a paired queue comparison

For an M/M/1 queue with nine arrivals and twelve services per hour, stationary mean total time is \(60/(12-9)=20\) minutes. A simulation starting empty has transient behavior, so steady-state estimation must justify warm-up and observation length. The reproducible companion executes **40 independent runs**, removes 2,000 customers as a declared initial transient, and averages the following 6,000 per run. Let \(Y_r\) be each replication mean. The estimate is \(\bar Y\pm t_{.975,39}s_Y/\sqrt{40}\), producing approximately **20.347 ± 0.599 minutes**, not a naive standard error over 240,000 correlated customer observations. A service upgrade to 13/hour produces approximately 15.198 ± 0.357 minutes; paired differences on common random streams estimate −5.149 ± 0.262 minutes. Interpret these intervals as sampling error *conditional on the queue assumptions*, not as physical field evidence. The [complete output-analysis method](../../methods/simulation-output-and-credibility.md) derives the formulas, warm-up caveats and experiment design.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Within-run observations are treated as independent replications.
* Warm-up or replication counts are arbitrary.
* A narrow interval is presented as proof the model is valid.
* Tail requirements are evaluated using only mean performance.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is initialization bias?
2. Why use independent replications?
3. What does a confidence interval quantify?
4. Why can quantiles need more data?

<details><summary>Explain the answers</summary>

**1. What is initialization bias?** Distortion caused by starting the simulation in an artificial state that differs from the process of interest.

**2. Why use independent replications?** They provide independent run-level observations suitable for many interval and comparison methods.

**3. What does a confidence interval quantify?** Uncertainty in an estimator under the model, sampling, and analysis assumptions—not all real-world uncertainty.

**4. Why can quantiles need more data?** They depend on fewer observations in distribution tails and can be unstable, especially for rare events.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 8](../labs/lab-08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[07 — Previous chapter](07-use-simulation-for-concept-exploration-alternatives-and-scenario-ana.md) · [09 — Next chapter](09-apply-simulation-in-design-and-development-using-selection-ranking-a.md) · [Book index](../README.md)

## Phase 5 technical reading: Why run length cannot solve uncertain inputs

A calibrated stationary Poisson arrival rate from synthetic counts is \(\hat\lambda=N/T=90/10=9\) arrivals/hour. The approximate 95% profile-LR interval [7.2664, 10.9896]/hour concerns parameter uncertainty before simulation. Increasing replication count reduces sampling variability of a queue statistic conditional on a fixed rate, but not the uncertainty of the rate itself. For rare conditions, brute-force Monte Carlo may observe zero failures even when the true model probability is nonzero. The [calibration and importance-sampling guide](../../methods/simulation-calibration-and-rare-events.md) derives likelihood estimation, a held-out count diagnostic, an unbiased weighted estimator and independent error checks.

## Step 03 integrated mobility simulation case: output inference and replication discipline

### Choose a terminating-system estimand

The modeled campus day starts at 06:00 and ends at 18:00, with time-dependent rates. It is a **terminating** system. The initial condition (vehicles fully charged and initially idle) is part of the claimed experiment, not startup bias to discard. A warm-up deletion would erase genuine morning peak behavior. In a separate *nonterminating* station or continuous-horizon model, one might diagnose steady state and remove initialization effects, but no automatic rule transfers across these cases.

There are two distinct percentile quantities. First compute a day-specific p90 \(Q_{0.9,r}\) across standard requests in replication \(r\), then estimate \(E[Q_{0.9,r}]\) by averaging across independent days. Alternatively pool requests across all replications to estimate a request-weighted p90. These have different weights and answer different questions when daily counts vary. The release reports the **mean of per-day nearest-rank p90 values**, plus a confidence interval across day replications. It must not be mislabeled as a 95% confidence interval for the real system's pooled 90th percentile.

### Derive uncertainty intervals for the mean daily p90

For \(R\) independent replications with daily percentile results \(q_1,\ldots,q_R\), calculate

\[\bar q=\frac1R\sum_{r=1}^{R}q_r,\qquad s_q^2=\frac1{R-1}\sum_{r=1}^R(q_r-\bar q)^2,\quad SE(\bar q)=\frac{s_q}{\sqrt R}.\]

A nominal two-sided 95% Student interval for the **mean** replication-level percentile is

\[\bar q\pm t_{0.975,R-1}\frac{s_q}{\sqrt R}.\]

For 30 replications, \(t_{0.975,29}\approx2.04523\). The [calculation code](../tools/step03_book11_mobility.py) uses this critical value for 30 seeds; for other replication counts its simplified demonstration uses a normal critical value and requires a more careful analyst review. The 14-vehicle baseline standard-trip p90 mean is about **36.4 min**; inspect [summary.json](../case/summary.json) for the exact computed interval. An interval for simulation noise cannot certify tail accuracy of an uncalibrated input distribution.

### Paired comparisons exploit common random numbers

For each seed \(r\), compute \(d_r=q_{14,r}-q_{12,r}\), then form \(\bar d\pm t_{0.975,29}s_d/\sqrt{30}\). This construction preserves useful within-day covariance. The controlled run yields approximately **-32.67 min** difference in mean daily standard p90, with a model-based 95% interval **[-36.05, -29.29] min** for 14 versus 12. An *unpaired* interval would fail to use that covariance and may give a different precision. The paired method still assumes independent replication seeds, a stable estimator, and interpretable shared exogenous streams; the endogenous charging draws are not strictly identical after policy divergence.

Check more than the interval: plot replication-level results by seed, inspect unusually long queues, observe whether accessible request samples are small, and test a larger replication count. The daily percentage not picked up by close is a finite-day ratio, and its mean across days differs from a pooled requests-weighted ratio. At least one adverse scenario and extreme sample trace should accompany a report. Do not stop replications opportunistically when a favorable confidence interval first appears; predeclare a precision or resource rule.

**Exercise and worked answer.** Given daily p90 values 10, 14 and 24 minutes, find their mean and sample variance. **Solution:** \(\bar q=(10+14+24)/3=16\); squared deviations are 36, 4 and 64, so \(s_q^2=(36+4+64)/(3-1)=52\ \mathrm{min}^2\). The standard error is \(\sqrt{52/3}\approx4.16\) minutes. With only three days, a normal 1.96 multiplier is not defensible; the Student critical value with two degrees of freedom is much larger, and data representativeness remains unresolved.

[Replications and summary](../case/INDEX.html) · [Chapter 9](09-apply-simulation-in-design-and-development-using-selection-ranking-a.md).
