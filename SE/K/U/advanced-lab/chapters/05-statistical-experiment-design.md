# A05 — Paired Monte Carlo, uncertainty and design of experiments

**Competency:** construct a reproducible comparison using common demand streams, calculate sampling uncertainty, and explain the difference between Monte Carlo precision and model credibility.

## Why one fixture is not enough

The 12-request baseline was deliberately chosen to be interpretable. It is not a random representative sample of regional transportation demand. A system may pass this fixture while regularly failing a different arrival pattern. To examine sensitivity, the advanced laboratory generates synthetic exponential interarrival gaps with mean four minutes. For each replication, the identical demand stream is evaluated under baseline and outage configurations.

The observation of interest is `D_i = completion_fraction_outage_i − completion_fraction_baseline_i`. Using the same arrival stream in each pair reduces nuisance variation from demand; it does *not* make successive replications dependent, provided each stream is independently generated. This is **common random numbers** as a variance-reduction principle.

## Derivation: interval for the mean paired difference

For `n` independent replications, compute `d_bar = sum(D_i)/n` and sample standard deviation

` s_D = sqrt(sum((D_i − d_bar)^2)/(n − 1)) `.

The approximate 95% normal interval is `d_bar ± 1.96 × s_D/sqrt(n)`. It is an approximation, especially with small n, bounded/discrete outcomes or strong skew. For small samples, a suitable t-based or bootstrap analysis may be more appropriate. The provided code uses the normal approximation intentionally and labels it.

In 120 seeded, independent synthetic arrival streams, the lab's paired experiment shows a substantial negative mean completion difference under the faulted design. Recompute after editing source assumptions; the saved result is part of a versioned configuration, not a universal fact.

## Credibility has multiple layers

**Code verification:** does the algorithm implement its documented scheduling rules? **Conceptual-model validation:** are those rules adequate representations of the intended decisions? **Input credibility:** are demand, service times, communications and outage distributions justified? **Output interpretation:** are the estimands and constraints reported accurately? More replications shrink Monte Carlo sampling error without repairing an incorrect conceptual model or biased input distribution.

## Sensitivity experiment

Vary mean interarrival time between 2, 4 and 8 minutes, and vary trip duration between 10, 12 and 16 minutes. Keep the same seeds across alternatives. Plot or tabulate paired differences and interaction effects. Compare whether longer trip times hurt more under high arrival rates. Explain the operational meaning of a model interaction before adding more decimal places to the results.

## Practice and deliverable

**Exercise 1.** If `d_bar = −0.15`, `s_D=0.20` and `n=100`, compute the normal interval.

<details><summary>Worked answer</summary>Standard error = `0.20/10=0.02`. Halfwidth `1.96×0.02=0.0392`. Interval = `[−0.1892, −0.1108]`, subject to model validity and normal-approximation assumptions.</details>

**Exercise 2.** Does doubling replications from 100 to 200 halve interval width?

<details><summary>Worked answer</summary>No. Holding the standard deviation fixed, width scales as `1/sqrt(n)`, so it becomes approximately `1/sqrt(2)≈0.707` times as wide.</details>

**Submit:** a written estimand, seed policy, experimental matrix, confidence calculation, and a model-credibility table. Related: [v11 uncertainty chapter](../../integrated-lab/chapters/06-models-and-uncertainty.md).
