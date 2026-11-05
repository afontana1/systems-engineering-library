# 07 · Experimental design, uncertainty, and defensible evidence

**Concept dossier · system test & evaluation / metrics / applied analytics**

## Separate observation, inference, and assurance

A measured quantity is not automatically a population property. An **estimate** summarizes a sample under a model; a **confidence interval** describes performance of a statistical procedure under repeated sampling; a **compliance claim** requires alignment with a specific acceptance rule and operational envelope. Each inference depends on how the sample was collected, what was excluded, measurement uncertainty and whether trials are dependent.

## Design the experiment around a question

Suppose engineers want to know whether a new dispatch rule improves pickup wait times during congestion. They can run a randomized A/B trial across comparable periods, but randomization must account for time-of-day and demand waves. If two systems share a fleet, treatment may contaminate control; if weather changes between test days, a before/after comparison may confound the intervention with weather.

A minimal protocol states:

1. Objective and decision threshold before seeing the results.
2. Unit of randomization, target population, nuisance factors and exclusions.
3. Measurement system, calibration, timestamps, data-loss rules and blinding when possible.
4. Replications, blocking, power or precision analysis, and a stop rule.
5. Statistical method, diagnostics, uncertainty interval, configuration and review authority.

## Worked two-factor example

Let factors be dispatch policy `A` (old −1 vs new +1) and demand `B` (low −1 vs high +1). Simulated average waits for four cells are:

| A | B | Mean wait (min) |
|---|---|---:|
| −1 | −1 | 7 |
| +1 | −1 | 5 |
| −1 | +1 | 15 |
| +1 | +1 | 10 |

The main effect of A is average at A=+1 minus average at A=−1: `(5+10)/2 − (7+15)/2 = −3.5 min`. The main effect of B is `(15+10)/2 − (7+5)/2 = +6.5 min`. The new policy reduces wait by 2 minutes under low demand and 5 under high demand: the effect **interacts** with demand. The factorial interaction contrast is `(10 − 15) − (5 − 7) = −3 min`, or its regression coefficient is −0.75 under the coded `A×B` model. Without independent replicates these four cells do not provide an estimate of experimental error; do not quote a p-value from this table.

## Zero failures do not equal zero risk

For `n` independent identical Bernoulli trials and zero failures, the exact one-sided 95% confidence upper bound for failure probability is `1 - 0.05^(1/n)`. With `n=300`, it is approximately 0.00994 (0.994%). However, repeated tests against nearly identical scenarios are not independent coverage of a diverse real-world environment. Confidence calculations never rescue a poor test design.

**Measurement uncertainty** is distinct: if timestamp error can be ±0.3 s per clock and clocks are unsynchronized, a 0.2 s timing margin is not trustworthy. Document uncertainty sources and propagation assumptions rather than quoting a false number of significant digits.

## A realistic decision

Suppose mean wait improves but the highest-demand subgroup experiences more abandoned trips. The aggregate mean is insufficient: operational validation asks whether the system improves the intended outcome for important scenarios and groups. Use both statistics and engineering judgment, record untested conditions, and challenge the alternative explanation.

## Practice

**A.** Why block a test by demand level? **Answer:** to reduce nuisance variation and identify a policy-by-demand interaction that an aggregate comparison may miss.

**B.** Can a narrow confidence interval compensate for biased sampling? **Answer:** no; precision about a biased estimand is not correctness for the target population.

**C.** What does “zero failures in 100 trials” support? **Answer:** under independent identical Bernoulli assumptions, a 95% one-sided upper bound near 2.95%, not zero failure probability.

**Transfer artifact:** a 2×2 experiment plan, simulated cell means with replicate variability, uncertainty budget, explicit decision rule and limitations table.

## Connections

[Traceability and assurance](02-requirements-evidence.md) · [Trade studies](05-trades-uncertainty.md) · [Model credibility](08-model-credibility.md) · [Interventions](14-causal-interventions.md).  
**Existing primer:** [Design of experiments](../../encyclopedia/design-of-experiments.md).
