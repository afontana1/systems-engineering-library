# 05 · Trade studies, multiobjective decisions, and information value

**Concept dossier · conceptual design / optimization / decision analytics**

## A score is not a decision

A trade study chooses among feasible alternatives under multiple objectives, hard constraints, uncertain facts and stakeholder preferences. It must distinguish **constraints** (unacceptable to violate), **objectives** (desirable to improve) and **assumptions** (possible sources of changed results). A weighted score is only one possible decision aid. Without clear normalization and stakeholder-accepted weights, a score can disguise a preferred answer.

## Worked deterministic trade

Consider three illustrative shuttle concepts:

| Concept | Annualized cost (k$) | 95th-percentile wait (min) | Accessible-trip completion (%) |
|---|---:|---:|---:|
| A: smaller fleet | 420 | 18 | 94 |
| B: larger fleet | 560 | 11 | 97 |
| C: dispatch redesign | 470 | 13 | 98 |

If the hard accessibility threshold is at least 97%, A is infeasible. B and C are both feasible. C is cheaper and achieves higher accessible completion than B, but B has lower wait time. Neither dominates the other because one improves one criterion while worsening another. They are **Pareto-nondominated** among feasible alternatives. The numbers are fictional assumptions, not evidence about real shuttle services.

Suppose a stakeholder utility function normalizes cost and waiting time to a common 0–1 preference scale and applies elicited weights. Document the mapping, not just the final totals. A 1% accessibility change may not be legitimately interchangeable with one minute of waiting; critical minima should remain hard constraints.

## Sensitivity is part of the conclusion

A decision should be presented with a **switching analysis**: under which plausible changes in input values, weights or constraints does the preferred alternative change? For this example, if C's wait-time estimate worsens from 13 to 17 minutes under rainy-day conditions, the comparison could change sharply. Report distributions or scenarios rather than a single falsely precise “best” answer.

If uncertain variables include common causes—e.g., bad weather affects both operating speed and boarding delay—model their dependence. Independently sampling correlated inputs can understate tail risk or yield physically impossible combinations.

## Learn first, or choose now?

The **expected value of perfect information** (EVPI) is the difference between (i) the expected best action if the uncertain state were revealed before choosing and (ii) the best expected value under current information. Let payoff `U(a,s)` depend on action `a` and state `s` with probabilities `P(s)`:

`EVPI = Σ_s P(s) max_a U(a,s) - max_a Σ_s P(s) U(a,s)`.

Example: dry and wet conditions are equally likely. Design A yields utilities (100,20); design B yields (65,65). Without further information, B yields 65 versus A's 60, so choose B. Perfect foreknowledge permits A in dry weather (100) and B in wet (65), yielding expected 82.5; EVPI is 17.5 utility units. This is an upper bound on what information is worth *in that payoff model*; actual sensors or pilot studies yield imperfect information and have costs.

## Decision discipline

Record alternative-generation rules, exclusions, stakeholder objectives, constraints, data provenance, scenario weights, dependence assumptions, method choice, switching thresholds and decision authority. A model is an aid to accountable reasoning, not a substitute for governance.

## Exercises with answers

**A.** Why is a dominated alternative not always deleted immediately? **Answer:** dominance may disappear under uncertainty, missing objectives or changed constraints. Check whether the comparison used defensible data and all relevant criteria.

**B.** Can EVPI be negative? **Answer:** not for a correctly calculated perfect-information decision problem with the same actions and payoff model; you can always ignore the information. The value of a specific experiment net of its cost can be negative.

**C.** What should accompany a weighted score? **Answer:** scales, weights, evidence, threshold constraints, uncertainty ranges and sensitivity/switching conditions.

**Transfer artifact:** a Pareto table, scenario matrix, one EVPI calculation and a decision record that names a responsible owner.

## Connections

[Outcome definitions](01-outcomes-boundaries.md) · [Experiments](07-experimental-evidence.md) · [Model credibility](08-model-credibility.md) · [Enterprise governance](13-sos-enterprise-governance.md).  
**Legacy primers:** [Engineering trades](../../encyclopedia/engineering-trades.md), [Bayesian value of information](../../encyclopedia/bayesian-value-of-information.md).
