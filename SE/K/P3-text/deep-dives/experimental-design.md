# Experiments: effects, interactions and confounding

**Cross-course pathways:** Metrics 5–7, Simulation Foundations 9, Decision Science 9.

## Why randomized comparisons matter

Suppose dispatch policy A is evaluated only during low demand and B only in rain. Their observed difference combines policy and environment. Randomization aims to break systematic association between treatment and nuisance causes; blocking uses known nuisance regimes (such as dry/rain) so comparisons happen within comparable contexts. Replication provides a measure of residual variation. Neither makes a poorly defined measurement reliable.

## A complete 2×2 calculation

Choose factor A = adaptive dispatch (low/high) and factor B = rainy conditions (dry/wet). Let observed mean wait at the four cells be: `y--=14`, `y+-=12`, `y-+=18`, `y++=11` minutes. Define A effect as the average change on going from A- to A+: `[(12-14)+(11-18)]/2 = -4.5 min`. B effect: `[(18-14)+(11-12)]/2 = +1.5 min`. The A×B interaction is the difference in A effects across B, divided by two: `[(11-18)-(12-14)]/2 = -2.5 min` under effect coding. The policy benefit changes markedly in rain; the main-effect average does not fully convey the operational story.

In a replicated experiment, fit a factorial model, estimate standard errors using independent experimental units, inspect residuals and assess whether assumptions fit. A factorial design is not inherently causal when assignment is nonrandom or hidden interventions differ among cells. If the same vehicle is repeatedly tested, distinguish true experimental unit from repeated measurements to avoid pseudoreplication.

## Replication and power

Choose a minimum difference that matters before running the test. For two independent normally distributed groups with approximate common standard deviation σ and equal sample size per group n, a basic planning approximation for a two-sided test is `n ≈ 2 (z_(1-α/2)+z_(1-β))² σ² / δ²`. This idealized formula is not a guarantee for interactions, heteroscedasticity or serial dependence. Blocking may reduce variance; clustering may increase it.

**Check:** A main effect of -4.5 min means the adaptive policy lowers wait on average across the two specified scenarios. It does *not* prove a 4.5-minute benefit in every environment.

**Lab:** `factorial_2x2(14,12,18,11)` returns effects. Change `y++` from 11 to 17; observe how the interaction and recommendation change.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
