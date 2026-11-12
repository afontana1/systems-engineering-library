# Simulation output analysis, warm-up, and model credibility

*Engineering method guide · Stochastic simulation, independent replications, comparison experiments, V&V, and intended-use decisions · Phase 3*

**Learning outcome.** Given a stochastic simulation and a proposed engineering decision, distinguish transient from steady-state claims, form a valid uncertainty interval for an output measure, compare alternatives with controlled randomness, and construct a credible-use argument that does not confuse computer-code correctness with real-world validation. The queue example is **synthetic** and deliberately limited to a single-server system.

**Prerequisites:** [Discrete-event simulation](../encyclopedia/discrete-event-simulation.md), [probability and dependence](../encyclopedia/probability-and-dependence.md), [model V&V and credibility](../encyclopedia/model-vv-and-credibility.md), and [statistical inference](statistical-inference-and-experiments.md).

## 1. Define the output claim and the time regime

A simulation output is meaningful only when attached to an **estimand**: the metric, population, time regime, stochastic mechanisms, and operating conditions. “Average delay is 20 minutes” is ambiguous. Is it mean queue wait or mean total time in the system? A steady-state mean or the mean over the first two hours after startup? One shift, a randomly chosen passenger, or the average of independent daily replications?

There are two major study designs:

- **Terminating simulations** have a natural endpoint, for example a 12-hour maintenance shift. Starting from an empty queue may be an accurate representation of that shift; deleting early observations would *remove* part of the estimand. Replicate the whole shift independently.
- **Steady-state/nonterminating simulations** investigate long-run behavior under approximately time-invariant inputs. Starting empty can bias measurements downward. Choose a justified initialization policy, evaluate warm-up sensitivity, and measure over a sufficiently long post-warm-up horizon.

An apparent steady state can still be seasonal or a mixture of different regimes. If arrivals peak every afternoon, it may be more defensible to model the daily cycle as a terminating or periodic system rather than discard data until a deceptively stable average emerges.

## 2. A queue model with a known analytic benchmark

For an M/M/1 first-come first-served queue, assume independent Poisson arrivals at rate \(\lambda\), independent exponentially distributed service times at rate \(\mu\), one server, no balking or abandonment, and \(0 < \lambda < \mu\). Under *stationary* conditions, the expected **total time in system** is

\[
E[W]=\frac{1}{\mu-\lambda}; \qquad \rho=\frac{\lambda}{\mu}.
\]

At \(\lambda=9\) jobs/hour and \(\mu=12\) jobs/hour, \(\rho=0.75\) and \(E[W]=1/3\) hour = **20 minutes**. At \(\mu=13\), the corresponding analytic mean is **15 minutes**. These results are analytic benchmarks for a simulator implementing the assumptions—not evidence that a real dispatch system actually has exponential service or stationary demand.

An efficient single-server simulation uses arrival times \(A_i\), departure times \(D_i\), and service times \(S_i\):

\[
D_i=\max(A_i,D_{i-1})+S_i, \qquad W_i=D_i-A_i.
\]

This recurrence enforces first-come first-served service and gives a small model that can be traced by hand. For example, if arrivals occur at 0, 1, and 1.5 minutes and respective services take 2, 2, and 1 minute, departures are 2, 4, and 5 minutes; times in system are 2, 3, and 3.5 minutes. A correct event-calendar implementation should reproduce this deterministic trace before stochastic runs are trusted.

## 3. Replication means, autocorrelation, and uncertainty

Successive \(W_i\) from the **same queue run** are dependent because today's backlog affects tomorrow's wait. An ordinary standard error \(s_W/\sqrt{N}\) over all individual customers is generally invalid if it assumes independent customers. The safer first teaching design is \(R\) independently seeded replications. Let \(\bar W_r\) be the average output for retained customers in replication \(r\). Compute:

\[
\bar{\bar W}=\frac1R\sum_{r=1}^{R}\bar W_r,\qquad
s_R^2=\frac{1}{R-1}\sum_{r=1}^{R}(\bar W_r-\bar{\bar W})^2,
\]

\[
CI_{95\%}=\bar{\bar W}\pm t_{0.975,R-1}\frac{s_R}{\sqrt R}.
\]

Here the independent **replication means** are sampling units. The interval estimates a mean under the declared model and initialization policy; its nominal coverage relies on the t approximation and independent runs. It does not cover model error, input uncertainty, or the distribution of an individual customer's delay. A percentile such as 99th-percentile delay needs its own estimator and uncertainty assessment.

**Reproducible experiment.** [Run the standard-library Python example](code/queue_replications.py). It conducts 40 independent replications, each with 2,000 initial customers excluded and 6,000 measured customers. Its seed policy is fixed solely for reproducibility. The code computes two service-rate cases with shared within-replication random inputs but different seeds **across** replications. The script's 95% intervals use \(t_{0.975,39}\approx2.02269\), not an unannounced normal approximation.

For this exact configuration, the simulated estimates are:

| Quantity | Estimated mean (minutes) | 95% t interval | Analytic expectation |
|---|---:|---:|---:|
| Baseline, \(\mu=12\) | 20.347 | [19.748, 20.945] | 20.000 |
| Upgrade, \(\mu=13\) | 15.198 | [14.841, 15.556] | 15.000 |
| Paired upgrade minus baseline | −5.149 | [−5.411, −4.887] | −5.000 |

The intervals here are **Monte Carlo sampling uncertainty under the idealized model**. That both analytic values lie inside the reported intervals is a useful benchmark check, not proof of correctness for every future model or scenario. Change the warm-up length to 0 and then change the measured horizon to 600; compare initialization bias and interval width. Do not tune warm-up after seeing a desired engineering answer.

## 4. Comparing systems: use pairs before pooling

For alternatives A and B, generating paired outputs \((Y_{A,r},Y_{B,r})\) using **common random numbers** can reduce variance when responses react similarly to shared input streams. Define each replication's difference \(D_r=Y_{B,r}-Y_{A,r}\). Then estimate the mean improvement and uncertainty from the \(D_r\), not from the formula for two unrelated samples.

\[
\operatorname{Var}(\bar D)=\frac{1}{R}\bigl(\operatorname{Var}(Y_B)+\operatorname{Var}(Y_A)-2\operatorname{Cov}(Y_A,Y_B)\bigr).
\]

Positive paired covariance reduces comparison variance; negative covariance can do the opposite. To make the coupling valid, explicitly state how random numbers are allocated (for example arrival stream separate from service stream), preserve the same workload scenario, and compare the differences across independent replications. A programming change that shifts random-number consumption can destroy the intended pairing.

A decision about service upgrades should also address cost and capacity constraints. A statistically significant five-minute simulated difference is not automatically economically or operationally significant. The queue may cease to resemble an M/M/1 system under shift changes, priorities, or correlated arrivals.

## 5. Batch means and the limits of warm-up removal

When independent runs are expensive, one long stationary series can be divided into batches and batch means treated as approximately independent **only after demonstrating that batch lengths are adequate for the series' dependence**. Short batches retain serial correlation; overly long batches leave too few batches for reliable variance estimation. Visual checks of moving means and multiple candidate warm-up lengths are diagnostics, not proofs. Do not select deletion length and final confidence interval by cherry-picking whichever makes a design pass.

A reproducible report records: conceptual model revision; code commit; input distributions and parameter sources; random-stream policy; initial conditions; run length and warm-up choice; independent replication count; output estimand and units; uncertainty method; stopping criterion; and sensitivity to workload assumptions. A fixed seed alone does not make a model validated.

## 6. Credibility evidence is a chain of distinct claims

| Claim | Evidence that could support it | What it **does not** prove |
|---|---|---|
| **Code verification** | Unit tests, conservation invariants, deterministic traces, queue benchmark | That the conceptual assumptions match operations |
| **Solution verification** | Convergence/sampling error studies; stable numerical approximations | That missing mechanisms are harmless |
| **Conceptual validation** | Subject-matter review of flows, resources, priorities, time horizon | That all input parameters were calibrated correctly |
| **Outcome validation** | Held-out, configuration-matched observed delay and throughput distributions | That a model remains credible in every future regime |
| **Intended-use acceptance** | Scoped claim, consequences, margin, limitations, accountable authority | That model outputs constitute independent physical test evidence |

A model-versus-test discrepancy may combine stochastic sampling error, measurement error, parameter uncertainty, implementation defects, structural model inadequacy, and environmental mismatch. These must not be collapsed into one unqualified “accuracy” value. Where a validation sample was also used to fit parameters, disclose the dependence; hold out another sample or use an explicitly limited validation claim.

NASA-STD-7009B (2024) and the NASA-HDBK-7009B (2026) distinguish credible modeling-and-simulation practices and their communication from an automatic blanket endorsement. They do not make this synthetic queue a qualified decision tool.

## 7. Complete the analysis as a decision artifact

1. State an intended use: “Compare policies to reduce **mean steady-state time in system** at nine jobs per hour while maintaining an upgrade-cost limit.”
2. Trace the deterministic three-customer event example by hand, and reproduce the M/M/1 analytic benchmark.
3. Run 40 seeded replications; report each configuration's independent-replication interval and the **paired** interval for the difference.
4. Challenge warm-up deletion and run length; investigate autocorrelation rather than hiding it by pooling observations.
5. Repeat at \(\lambda=11\) and discuss why the utilization change might alter the economic decision.
6. Write a credibility table identifying independent empirical data that would be required before applying this model to Northstar operations.

**Teaching prompt:** Compare a terminating two-hour emergency shift to steady-state operations. Why does removing the first 2,000 arrivals change the question rather than simply “improve accuracy” in the terminating case?

**Curriculum crosswalk:** [EN.645.757](../../C/P3/EN645757.md), [EN.645.758](../../C/P3/EN645758.md), [Book 11 ch 8](../B11/chapters/08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md), [Book 11 ch 11](../B11/chapters/11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md), and [Book 12 ch 1](../B12/chapters/01-frame-the-advanced-m-s-decision-intended-use-architecture-and-credib.md).

## Primary technical references

- [NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263). Credibility, intended use, assessments, and disciplined communication.
- [NASA-HDBK-7009B, Models and Simulations Implementation Guide (2026)](https://standards.nasa.gov/standard/NASA/NASA-HDBK-7009). Methods and explanatory practices for implementation.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook). Experimental design and statistical uncertainty practices.

*Source pointers support the general methods; the hypothetical data and results were authored and tested for this library. No standards body has approved this example.*
