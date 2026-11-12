# Enterprise portfolio decisions under constraints

**Reference entry · Enterprise engineering, affordability and decision analysis**

## The portfolio is a system, not a ranked wish list

An enterprise portfolio allocates scarce capital, personnel, schedule and risk capacity among interventions whose benefits, dependencies and consequences may interact. Selecting projects independently by benefit-cost ratio can be wrong when projects are indivisible, share enabling infrastructure, or create conflicting constraints. Define the boundary—programs, operating units, suppliers, workforce, external stakeholders—before choosing a value model.

For binary investment choices \(x_i\in\{0,1\}\), a simple first model is

\[
\max_x\sum_i v_i x_i\quad\text{subject to}\quad\sum_i c_i x_i\le B.
\]

Here \(v_i\) is an explicitly defined benefit score (not automatically a dollar value), \(c_i\) is a compatible resource quantity, and \(B\) is the resource limit. A project dependence such as “B requires A” becomes \(x_B\le x_A\). A mutually exclusive architecture choice uses \(x_A+x_B\le1\). A complete investment decision also needs timing, uncertainty, operational effects, equity and safety constraints; a linear sum is a useful starting approximation, not a universal objective.

## Worked enumeration

Consider three *indivisible* proposed improvements: A costs 4 units and yields value 7; B costs 3 and yields 5; C costs 5 and yields 9. A budget of 8 allows the singletons, A+B (cost 7, value 12), and B+C (cost 8, value 14), but not A+C (cost 9) or all three. **B+C is the feasible maximum at value 14** if benefits are additive and there are no dependencies. Ratios \(7/4=1.75\), \(5/3\approx1.67\), \(9/5=1.80\) would rank C then A then B, but greedy ranking can fail on constrained, indivisible selections; enumeration or integer optimization gives the defensible optimum for the stated model.

Now assume C needs an enabling A subsystem. The extra constraint \(x_C\le x_A\) makes C infeasible under the budget because A+C costs 9; A+B, value 12, becomes the winner. The requirements architecture—not merely the budget spreadsheet—changes the decision.

## Risk, resource conflict and stage gates

A scenario-based alternative replaces fixed \(v_i\) with \(v_{is}\) for plausible states \(s\). Compute expected value only after defining justified probabilities; otherwise use scenario regret, robust feasibility, explicit qualitative comparisons or value-of-information reasoning. Workforce hours and integration-slot availability often bind before nominal funding does. Model them as additional constraints instead of inventing shadow prices without an economic basis.

An evidence-based stage gate records the objective, budget version, candidate set, assumptions, exclusions, decision authority, dissent, sensitivity, and next evidence trigger. A portfolio should be reassessed after an interface change, supplier failure or new operating objective. An approved project is not a proven benefit until the relevant outcomes have been measured.

## Exercise with check

For the unconstrained example, decrease the budget from 8 to 7. The optimum becomes A+B with value 12; neither C+B nor A+C is affordable. Then introduce a workforce limit allowing at most one of A and B. Re-enumerate feasible options and state which constraint causes the new selection. Explain why a positive net-present value alone is insufficient when a mandatory safety obligation is unmet.

## Limits and sources

Benefit scores require stakeholder-approved scales; adding unlike units without justification is invalid. Project interactions can defeat additivity. A purely financial optimization can exclude accessibility or resilience unless these are encoded as constraints or separately governed criteria. Related: [enterprise as system](enterprise-as-system.md), [Pareto value](pareto-and-value.md), [Bayesian information](bayesian-value-of-information.md), and [authority and governance](authority-and-governance.md).

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — trade study, technical decision analysis and lifecycle perspective.
- [SEBoK enterprise systems engineering](https://sebokwiki.org/wiki/Enterprise_Systems_Engineering) — enterprise scope and governance context.

*Scope:* Values and costs are synthetic abstract units. No actual portfolio is appraised.
