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

<!-- STEP04-FLAGSHIP-U1-START -->
### D02 extension · Feasible-first preference and a reversal equation

Given qualities $q_A,q_B$ and normalized costs $c_A,c_B$, consider $V=wq-(1-w)c$, $0\le w\le1$. The two designs tie when $w(q_A-q_B)=(1-w)(c_A-c_B)$ and, if the denominator is nonzero, $w^{\ast}=(c_A-c_B)/[(q_A-q_B)+(c_A-c_B)]$. A reversal weight is meaningful only when the *hard constraints are already satisfied*. NS-U4.1's integrated candidate passes normal service (99.35% total and 100% accessible) but only 45% of scenario weight. With a 95% robustness screen there are no candidates in the feasible set. Preference weights cannot restore feasibility.

**Exercise and solution.** If A has $q=.8,c=.2$ and B has $q=.9,c=.5$, then $V_A-V_B=-.1w+.3(1-w)=.3-.4w$; A and B tie at $w=.75$. This is a stylized preference comparison, not a safety release decision. [Policy outputs](../flagship-integration/outputs/ns-u4.1-results.json).
<!-- STEP04-FLAGSHIP-U1-END -->
