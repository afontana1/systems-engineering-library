# Robust optimization and technical margins: good decisions across plausible futures

**Canonical reference · Analytics, modeling, simulation and decisions · Expanded reference · Internal editorial review; independent peer review not performed**

## Why optimizing the nominal scenario is insufficient

Conventional optimization asks for an alternative that minimizes a cost or maximizes a value under a specified set of constraints. In real engineering, loads, demand, regulations, weather, interfaces and cost estimates are not fully known. A design optimized for a point estimate can be fragile: a small parameter shift may violate its key constraint. **Robust optimization** evaluates decisions against an explicit uncertainty set; **stochastic optimization** uses probability distributions and an objective such as expected cost or a risk measure. They answer different questions and neither can make a poor uncertainty model trustworthy.

Technical *margin* is the difference between a requirement boundary and predicted or measured capability, stated in compatible units and under defined conditions. A 20% average throughput margin is not a 20% safety margin for peak loading if the distributions and failure mechanisms differ. The direction of “good” matters: for latency, lower is better, so margin may be `allowable latency − predicted latency`; for available payload, it may be `capacity − demand`.

## Three decision rules

For alternative `a` and scenario `s` with cost `C(a,s)`: an expected-cost rule minimizes `Σ p(s)C(a,s)`, conditional on a defensible probability model; a worst-case rule minimizes `max_s C(a,s)`, conditional on a justifiable uncertainty set; minimax regret minimizes `max_s[C(a,s) − min_b C(b,s)]`. Different rules capture different preferences and tolerances. A decision team should not describe one as universally optimal when stakeholders have not agreed on the objective.

Constrained designs also need feasibility across scenarios, not just low cost. A *chance constraint* such as `P(latency ≤ 2 seconds) ≥ 0.99` relies on a probability model and correct interpretation of the target population. A robust constraint such as `latency(a,s) ≤ 2 seconds for all s∈S` relies on the completeness and relevance of the set `S`. Both can fail if a hidden operational mode is excluded.

## Worked comparison: expected cost versus regret

Suppose two shuttle fleet designs face **normal** and **severe** operating scenarios. Illustrative lifecycle costs in thousands are:

| Alternative | Normal | Severe |
|---|---:|---:|
| A: lean fleet | 120 | 250 |
| B: reserve capacity | 160 | 190 |

If the normal scenario has probability 0.8 and severe 0.2, expected costs are `E[C_A]=0.8×120+0.2×250=146` and `E[C_B]=0.8×160+0.2×190=166` (thousands). An expected-cost decision chooses **A**. Worst-case costs are 250 for A and 190 for B, so a worst-case rule chooses **B**. Scenario-optimal costs are 120 for normal and 190 for severe; regret for A is `(0,60)` and for B `(40,0)`. Maximum regrets are 60 and 40, so minimax regret also chooses **B**.

No calculation is wrong: the rules embody different risk attitudes. The 0.8 scenario weight is itself contestable and should not be silently treated as an observed frequency. A/B service quality, safety, equity and regulatory compliance may impose non-negotiable constraints before any cost comparison.

## Margins, sensitivity and decision value

Suppose a proposed server has a measured peak demand envelope of 150 requests/s and tested sustained capacity of 180 requests/s. Nominal headroom is `180−150=30 requests/s`, or 20% relative to demand. This does **not** guarantee 20% headroom under a storm scenario that doubles authentication overhead or changes the work mix. Sensitivity analysis should rank influential uncertain variables, test dependency assumptions, and evaluate discontinuities such as queue saturation. Decisions should distinguish adaptable capacity, physical margin, spare capacity and statistical confidence in demand forecasts.

A robust decision may be deliberately reversible: reserve a later expansion interface, run a pilot that informs demand uncertainty, or pay for a modular fleet. Such flexibility has cost and can be evaluated using value-of-information and real-option thinking. It is not automatically worth purchasing; the option must be exercisable before a critical constraint is violated.

## Common modeling failures

- Optimizing a weighted score before ruling out designs that violate absolute safety or legal constraints.
- Using independent parameter ranges that create impossible scenario combinations, or omitting a credible joint adverse scenario.
- Reporting expected cost without showing the tails or who bears the downside.
- Treating model prediction margin as demonstrated physical margin on a released configuration.

Document objectives, decision rights, scenario rationale, uncertainty provenance, sensitivity, feasibility, and an explicit re-evaluation trigger. Decision robustness is evidence about *specified futures*, not protection against every unforeseen event.

## Selected source-to-claim references

- **O1 · Multidisciplinary technical trades and sensitivity:** [NASA Systems Engineering Handbook, section 4.0 — design solution definition and trade context](https://www.nasa.gov/reference/4-0-system-design-processes/).
- **O2 · Model/data credibility limits and technical evidence:** [NASA Systems Engineering Handbook, section 2.0 — systems engineering fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/). These are methodological anchors, not an endorsement of the original cost matrix.

## Follow the knowledge

- **Prerequisites:** [Engineering trades](engineering-trades.md), [Probability and dependence](probability-and-dependence.md).
- **Related concepts:** [Pareto and value](pareto-and-value.md), [Bayesian value of information](bayesian-value-of-information.md), [Model credibility](model-vv-and-credibility.md).
- **Go deeper:** [Book 14, Chapter 11 — Robustness, regret and uncertainty](../B14/chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md); [Book 6, Chapter 10 — DOE and uncertain down-select](../B6/chapters/10-doe-parametric-analysis-uncertainty-sensitivity-and-dow.md).
