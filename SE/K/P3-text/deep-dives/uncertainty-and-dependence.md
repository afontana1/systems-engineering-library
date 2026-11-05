# Uncertainty is not just a standard deviation

**Cross-course pathways:** Metrics 2, 3 and 9; Foundations M&S 3 and 8; Decision Science 11.

## Four different reasons a number is uncertain

A waiting-time estimate can vary because different riders experience genuinely different trips (**aleatory** variation), because arrival-rate parameters were estimated from limited data (**epistemic** uncertainty), because the timestamp device has bias (**measurement** uncertainty), or because the simulator omits a relevant mechanism (**model-form** uncertainty). One error bar does not make these sources interchangeable. Some can be reduced by measurement or improved model design; others characterize the system under its operating scenarios.

The law of total variance helps separate scenarios: `Var(Y) = E[Var(Y | S)] + Var(E[Y | S])`. The first term is variation *within* scenarios and the second is the effect of having different scenario means. If dry-day and rainy-day mean waits differ significantly, a single pooled distribution can conceal the scenario risk even when its overall mean looks acceptable.

## A derivation for correlated time components

Suppose trip time `T = A + B`, where `A` is travel time and `B` is boarding time. From expansion of `E[(T-E[T])²]`,

`Var(T) = Var(A) + Var(B) + 2 Cov(A,B)`.

For standard deviations 2 and 1 minute, and correlation `ρ=0.6`, variance is `4 + 1 + 2(0.6)(2)(1) = 7.4 min²`; standard deviation is `√7.4 = 2.72 min`. With false independence, the result would be `√5 = 2.24 min`, understating the spread by about 18%. Under a **joint normal assumption**, the corresponding approximate 95th percentile is `mean + 1.645 SD`; with mean 15, it is 19.47 min versus 18.68 min. Real trip times may not be normal, so test support and tail behavior.

## What a Monte Carlo run can and cannot do

`tools/phase3_lab.py` implements `correlated_sum_mc`. Fix a seed to reproduce a run; change seeds to measure Monte Carlo error; vary the correlation assumption to estimate model sensitivity. A million runs of a poorly chosen distribution do not validate it. The Monte Carlo standard error of an estimated probability `p` is approximately `sqrt(p(1-p)/N)` for independent draws; correlated replications require more care. For a rare p=0.001 and N=10,000, the expected count is only ten events—often inadequate for a confident tail estimate.

## Practice and explanation

**Problem:** A and B have SDs 3 and 4 with correlation -0.5. What is the sum SD? **Solution:** `Var(A+B)=9+16+2(-0.5)(3)(4)=13`; SD `√13≈3.606`. Negative correlation reduces spread, though it does not guarantee small tails in nonnormal models.

**Transfer:** Draw a shared-weather driver upstream of arrivals, travel and boarding. Explain which correlations can be measured from data and which remain structural hypotheses.

**Credibility boundary:** This is a mathematical teaching model, not empirical evidence about autonomous vehicle operations.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
