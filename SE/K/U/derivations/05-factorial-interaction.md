# D05 · Deriving a factorial interaction without hiding uncertainty

**Skill:** Compute a two-factor contrast and distinguish it from evidence of statistical significance.

## A complete 2×2 illustrative design

Let factor A be dispatch policy (old `−1`, new `+1`), and B demand (low `−1`, high `+1`). Observed cell means (minutes of wait) are:

| Policy | Demand | Mean wait |
|---|---|---:|
| Old | Low | 7 |
| New | Low | 5 |
| Old | High | 15 |
| New | High | 10 |

For coded factors, model `y = β0 + βA A + βB B + βAB A B + ε`. The grand mean is `(7+5+15+10)/4 = 9.25`. The main effect of A (new minus old) is `(5+10)/2 − (7+15)/2 = −3.5`. The B effect is `(15+10)/2 − (7+5)/2 = 6.5`.

Policy improvement at low demand is `5−7 = −2`; improvement at high demand is `10−15 = −5`. The **difference of differences** is `−5−(−2)=−3`. This is the factorial interaction *effect* contrast; the regression coefficient in ±1 coding is `βAB = −3/4 = −0.75`. The other coefficients are `βA = −1.75`, `βB=3.25` and `β0=9.25`.

Check a prediction: new/high (`A=+1`, `B=+1`) gives `9.25−1.75+3.25−0.75=10`, matching the table.

## This is not yet a statistical finding

The four means alone do not estimate cell variance. Add independent randomized replications, or blocking for time-of-day or weather, before constructing confidence intervals or p-values. If the same stochastic simulation stream is reused across conditions deliberately (common random numbers), analyze the paired dependence rather than pretending all observations are independent.

Factorial effects are conditional on factor levels. A two-level “high demand” range may not generalize to extreme festival demand, nonlinear saturation or emergency modes.

## Design choices

Randomize run order; balance exposure; predeclare response variables; log failed or aborted runs; reserve a confirmatory experiment if screening many factors. Examine interaction before interpreting a global main effect as a universal policy improvement.

## Practice

**Question:** Is the new policy guaranteed to reduce waits by 3.5 minutes for every demand scenario?

<details><summary>Solution</summary>

No. The −3.5 minute main effect is an average over the two selected demand levels. The policy effect is −2 minutes under low demand and −5 under high demand in the illustrative table, demonstrating interaction.

</details>

**Transfer artifact:** Design matrix, randomization plan, raw replicate dataset, model with interaction, residual diagnostic, and scenario-limited conclusion. See [design of experiments](../../encyclopedia/design-of-experiments.md).

<!-- STEP04-FLAGSHIP-U1-START -->
### D05 extension · Two-factor contrast as an interaction, not a causal proof

Consider a balanced synthetic $2\times2$ table of mean waits (minutes): base $y_{00}=18$, capacity-only $y_{10}=15$, process-only $y_{01}=14$, both $y_{11}=8$. The interaction on the raw response scale is $I=y_{11}-y_{10}-y_{01}+y_{00}=8-15-14+18=-3$ minutes. The joint intervention saves 3 more minutes than the sum of separately estimated reductions predicts. An interaction depends on the response scale and design; repeated randomization, controlled scenario blocks and a standard error are required before inferring a population effect.

**Exercise and solution.** If $y_{11}$ were 11 instead of 8, $I=0$ and the table would be additive on this scale. A single noiseless synthetic table cannot certify additivity outside its assumed domain. [Case data](../flagship-integration/data/ns-u4.1-case.json).
<!-- STEP04-FLAGSHIP-U1-END -->
