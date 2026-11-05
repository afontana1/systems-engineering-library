# Robust optimization: feasibility before preference

*Core Concepts · Quantitative methods · T18*

> Compare alternatives across constraints, uncertainty sets, Pareto fronts, and regret.

**Recommended preparation:** [10 Decisions](10-decisions.md), [08 Dynamics](08-dynamics.md)

**Related companion books:** [Book 6](../B6/OPEN-BOOK.html), [Book 12](../B12/OPEN-BOOK.html), [Book 14](../B14/OPEN-BOOK.html)

## 1. Separate feasible solutions from attractive ones
Weighted scoring is useful only after rejecting choices that violate hard constraints. A shuttle that has the highest nominal mobility score but cannot meet its minimum charging reserve is not an acceptable solution simply because its low cost compensates for the failure. Formulate engineering choices as

\[
\max_{x\in X} f(x)\quad \text{subject to }g_j(x)\leq0,\ j=1,\ldots,m.
\]

The feasible set $X$ and constraints express what is allowed. The objective expresses what is preferred *among allowed choices*. Stakeholders should approve both. Changing the preference weights must not quietly change minimum safety or legal requirements.

## 2. Make units and relationships explicit
Suppose a route policy selects the number of active vehicles $x$, with $x\in\{1,2,3\}$. Nominal service capacity is $6x$ requests per hour. Energy use is $12x$ kWh per hour, and the charging contract limits continuous energy consumption to 30 kWh per hour. Under those exact assumptions, $x=3$ violates the 30-kWh cap even though it serves the greatest nominal demand; $x=2$ is the largest feasible choice.

A model should label whether the energy limit is an instantaneous power cap, an hourly energy budget, or a battery inventory constraint. Mixing kWh and kW without specifying time is a dimensional error, not a policy disagreement.

## 3. Add uncertainty without hiding it
Demand, journey time, and available energy fluctuate. An expected-value calculation may treat average demand as representative even when the system must provide service during a severe demand surge. **Robust optimization** requires constraints to hold for all scenarios in a specified uncertainty set; a **chance constraint** permits a bounded probability of violation under an explicitly modeled distribution.

A robust constraint might be $6x\geq d$ for every $d\in[8,12]$, requiring at least two vehicles. A chance constraint might require $P(6x\geq D)\geq0.95$. The answers depend heavily on the chosen uncertainty distribution, which must be supported by data or clearly labeled an assumption. A broader uncertainty set produces a more conservative design, but may also be expensive or infeasible.

## 4. Trade Pareto efficiency against stakeholder value
When cost, emissions, service completion, and resilience conflict, there is often no single design that dominates every other. A design is **Pareto dominated** if another is at least as good in every criterion and strictly better in at least one. Eliminate dominated designs before discussing subjective weights. Even then, a Pareto-efficient design may be socially unacceptable if it fails a minimum access requirement for a vulnerable population.

A normalized weighted sum can conceal extreme disadvantages; normalization choices change rankings. Use sensitivity analysis to identify weight regions where the recommended alternative switches. Ask stakeholders to review those switch thresholds instead of showing one convenient ranking.

## 5. Minimax regret as an alternative decision lens
When credible futures are very different and probabilities are unreliable, compare regret. For each scenario, define the best feasible outcome, then compute how much is lost by each alternative relative to that scenario's best decision. Minimax regret chooses the alternative whose worst regret is smallest. It does not assert that the worst case is most likely; it protects against severe relative underperformance when future conditions cannot be trusted probabilistically.

For example, compare two fleet investments over calm and emergency weeks. A fixed high-capacity fleet may be costly in calm weeks but resilient in surges; an on-demand contract may do the reverse. A robust decision report should show the scenario outcomes, constraints, cost of protection, and what new information would change the choice.

## 6. Worked example: why ranking is not enough
Take three alternatives with nominal service (requests/hour), energy requirement (kWh/hour), and cost index:

| Alternative | Service | Energy | Cost index |
|---|---:|---:|---:|
| A | 6 | 12 | 2 |
| B | 12 | 24 | 4 |
| C | 18 | 36 | 5 |

The hard requirements are service at least 10 and energy no more than 30. Only B is feasible. No amount of normalized scoring should select C until the energy constraint changes or a justified alternative energy arrangement is designed. Now add uncertainty: if one vehicle can serve anywhere from 4 to 6 requests/hour, B could serve only 8 in the stressed case and fails the robust service threshold. The honest result is **no currently feasible choice** under the stated conditions; engineers must redesign, relax a requirement with authority, or procure additional capacity.

## 7. From optimization result to design authorization
Record configuration assumptions, constraint owners, demand characterization, the solver or enumeration method, sensitivity cases, and how infeasibility is handled. A solver returning an optimum does not certify the model is correct. A valid optimization workflow includes a unit audit, boundary cases, an independent enumeration on small examples, and a decision review with stakeholders who own the constraints.

## Practice questions
**A.** Identify the feasible options in the table. **B.** Explain how an uncertainty set can make every option infeasible. **C.** Compare the meaning of robust satisfaction versus a 95% chance constraint.

<details><summary>Answer check</summary>

B alone satisfies both nominal hard constraints. Under stressed service of 4 per vehicle, B supplies only 8; C supplies 12 but violates energy. Thus no option meets both requirements. Robust feasibility covers every declared scenario; chance constraints rely on a probability model and tolerate a specified violation probability.

</details>

## Further connections
[Decision tradeoffs](10-decisions.md), [simulation credibility](19-simulation-credibility.md), and [requirements](02-requirements.md) help distinguish stakeholder value from nonnegotiable engineering constraints.

## Guided laboratory

[Open the corresponding case-based lab](labs/18-robust-optimization-workshop.md)
