# D02 · Trade studies, Pareto screening, and reversal thresholds

**Skill:** Separate admissibility from preference and demonstrate exactly when a favored design stops winning.

## Define a feasible set before scoring

Suppose two shuttle fleet concepts meet regulatory and accessibility constraints. Concept A is rated service quality 8/10 and cost attractiveness 4/10; B scores 6 and 8 respectively. For service weight `w`, an additive utility illustration is:

`U_A(w) = 8w + 4(1−w) = 4 + 4w`

`U_B(w) = 6w + 8(1−w) = 8 − 2w`.

Set them equal: `4 + 4w = 8 − 2w`; therefore `6w = 4` and `w = 2/3`. A wins only if `w > 0.6667`. If stakeholders cannot defend that preference, the recommendation is fragile. At `w = 0.6`, A scores 6.4 and B scores 6.8. At `w = 0.8`, A scores 7.2 and B scores 6.4.

These scores are ordinal judgments unless there is a defensible cardinal value model. A weighted sum assumes meaningful scale intervals, compensability and often independence among criteria. Calling a point estimate “precise” to two decimals does not fix those assumptions.

## Pareto screen

For cost and delay (both minimized), compare A `(10 cost units, 8 min)`, B `(11, 6)`, C `(12, 9)`. A dominates C because it is cheaper and faster; B is not dominated by A because it is faster despite costing more. After screening, compare A and B through preferences, constraints and uncertainty. Never place an unsafe C back in competition due to a low cost weight.

## Epistemic uncertainty

Suppose A's service score is not 8 but in `[7,9]` and B's is `[6,7]`. The tie point varies. At A service 7 and B service 7, B wins for every `w < 1`; at A service 9 and B service 6 the threshold is `4/(4+3)=4/7≈0.571`. Vary measurements and weights jointly, not just one parameter at a time when they may be correlated.

Use three scenarios: ordinary demand, peak demand and degraded network. A concept that wins on the average may violate mandatory minimum performance in the last scenario. Record reversal conditions and a trigger for reopening the decision.

## Distinguish value and risk

Expected utility is not automatically suitable when safety thresholds, irreversibility or legal constraints are noncompensable. Where feasible, formulate an optimization problem as `maximize utility` **subject to** hard constraints, rather than burying violations in the score.

## Practice

**Question:** At what service weight does A beat B? Would assigning a higher weight of 0.8 prove A is superior?

<details><summary>Solution</summary>

A beats B above two-thirds. Choosing 0.8 yields a ranking under that preference model only; it does not prove the value scale, risk assumptions or compliance requirements are correct.

</details>

**Transfer artifact:** A two-dimensional alternatives table, feasible-set checklist, threshold derivation and sensitivity plot with written decision-reversal rules. See [engineering trades](../../encyclopedia/engineering-trades.md) and [Pareto analysis](../../encyclopedia/pareto-and-value.md).
