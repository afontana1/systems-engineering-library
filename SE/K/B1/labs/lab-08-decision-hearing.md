# Hypothetical Lab 8 — The Architecture Decision Hearing

**Course:** EN.645.662 Week 8 · **Reading:** [Chapter 8](../chapters/08-trade-studies-and-sensitivity.md) · **Time:** 100–150 minutes · **Type:** reproducible decision audit.

## Situation

A fictional Northstar board compares three feasible options: central turnkey (T), federated integration (F), and local demonstrator (L). The provisional value scores are given in [`architecture-scores.csv`](../data/architecture-scores.csv). Weight resilience at 0.50, affordability at 0.30 and maintainability at 0.20. All scores are invented judgments on declared 0–100 scales, not market data.

## Work to perform

1. Draft a decision statement. List two noncompensable constraints (for example, an agreed accessible-service requirement and an explicitly approved safe-fallback rule), then separate these from preferences.
2. Reproduce weighted scores for T, F, and L by hand, then run `python tools/decision_audit.py` from the book directory. Compare outputs, including the pairwise F-versus-T weight threshold.
3. Hold maintainability weight at 0.20; let resilience weight vary from 0.30 to 0.60 and assign remaining weight to affordability. Plot or tabulate the scores and identify **the overall winner at each point**, not only the pairwise crossover.
4. Assume F's resilience estimate could instead be 70. Recompute its total at original weights; describe how the recommendation changes and whether the uncertainty is resolvable by testing.
5. Critique a fourth proposed criterion, “general technical quality.” Identify possible overlap and propose a measurable replacement.
6. Prepare a recommendation memo that states limitations, stakeholder ownership of weights, dissent, and a bounded next experiment rather than claiming the spreadsheet determines the truth.

## Deliverables

`LAB08_DecisionMemo.md`, `LAB08_Sensitivity.csv`, and a one-page record of assumptions and authority.

<details><summary>Reference calculations and interpretation</summary>

At (0.50, 0.30, 0.20), T=70.0, F=74.5, L=73.5. Pairwise F=T when resilience weight is 23/55 ≈ 0.41818 with maintainability fixed at 0.20. But include L when naming the preferred option. If F's resilience drops to 70, its score becomes 67.0, so L becomes first at 73.5. A one-point nominal lead is weak when evidence is immature. Weighted value is conditional on feasibility, scale validity and preferences.

</details>

## Transfer

The original Week 8 `662_W08_TradeStudy_v1.0` requires an AHP consistency check, sensitivity analyses and a more complete decision record. Your hypothetical calculations are a rehearsal, not that deliverable.


## Extended worked problems and lab

Study the [worked problem workshop on architecture choice and reversal](../practice/trade.md), then complete the [extended laboratory](../practice/lab-trade.md). The exercises are separate from the original assessed coursework.
