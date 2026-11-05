# Enterprise portfolio decisions, real options, and governance constraints

*Graduate study for Book 19 — Enterprise Systems Engineering. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> Why is choosing the highest-NPV set of investments sometimes the wrong enterprise decision?

## Theory and conceptual structure

An enterprise system spans capabilities, organizational processes, incentives, information, people and governance. Its architecture cannot be reduced to a technology portfolio. Projects may share scarce engineering talent, operational disruption budgets and public legitimacy. Investment selection should therefore represent dependency constraints, authority, implementation capacity and stakeholder distribution—not simply sum standalone discounted cash flows.

A portfolio optimization model selects a feasible set of investments. It can use binary decisions and budget, staffing and mission constraints. However, estimated project values may not be additive: deploying a shared digital platform may enable later improvements, while simultaneous implementations can overwhelm the same operations team. The model must distinguish synergy, double-counting and conditional benefits.

Real options recognize the value of deferring an irreversible choice while learning. An early pilot may have negative immediate NPV but create information that prevents an expensive poor deployment. That option value is conditional on the decision rights and ability to act on the signal. A pilot without a genuine stop/go choice is not an option; it is a ceremonial phase in a predetermined rollout.

Enterprise governance should define measurable outcomes and identify who bears cost, risk and disruption. A financially attractive portfolio can still violate accessibility or emergency coverage constraints. Robust portfolio decisions examine multiple states of the world and document conditions under which funding is released. Portfolio reviews should include a mechanism for retiring benefits assumptions when evidence contradicts them.

## Formal model and derivation

\[\max_{x_i\in\{0,1\}}\sum_i v_i x_i\quad\text{subject to}\quad \sum_i c_i x_i\le B,\quad Ax\le b.\]
For discount rate \(r\), \(NPV=-C_0+\sum_{t=1}^{T}CF_t/(1+r)^t\). A real option introduces future branch-specific choices after information arrives.

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

Three investments have (cost,value) pairs: dispatch analytics (3,7), interoperability gateway (4,6), and operator training (2,4), in millions of consistent notional units. With budget 6, the simple additive optimizer chooses analytics plus training (cost 5, value 11) rather than gateway plus training (cost 6, value 10). But if gateway is required to deliver the analytics benefit, the pair is infeasible under budget 6. The revised feasible choice may be gateway plus training (cost 6, value 11). A dependency graph changes the answer more than adjusting decimal precision in the value model.

![Model of the linked reasoning steps](../figures/19-enterprise-portfolios.svg)

## Counterexample and critical review

**Counterexample:** A pilot measures transaction throughput but fails to test whether rural communities obtain faster emergency access. Portfolio value is reported as realized despite shifting benefits away from the population named in the enterprise mission. Introduce segment-specific acceptance constraints.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

With budget 6, identify the best additive portfolio from costs [3,4,2] and values [7,6,4].

<details><summary>Worked answer and engineering interpretation</summary>

Analytics plus training costs 5 and yields value 11, which exceeds gateway plus training’s 10. Enumerate feasible portfolios rather than comparing each candidate with just one alternative.

</details>

### Problem 2

Why can a dependency change the preferred portfolio?

<details><summary>Worked answer and engineering interpretation</summary>

If analytics needs the gateway, analytics alone cannot deliver the claimed value; impose x_analytics ≤ x_gateway and recalculate feasible combinations.

</details>

### Problem 3

Define a real option as an operational decision rule.

<details><summary>Worked answer and engineering interpretation</summary>

Fund a bounded pilot; if measured mission outcomes exceed threshold and safety/equity constraints hold, authorize deployment. Otherwise stop, revise or defer. Identify the authority that can actually choose.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/19-enterprise-portfolios.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 19 and its existing weekly lessons](../../B19/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)
