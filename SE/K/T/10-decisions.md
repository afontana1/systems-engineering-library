# Multiobjective decisions, Pareto tradeoffs, and information value

*Core Concepts · Assurance · T10*

> Defend architecture choices without hiding feasibility constraints or stakeholder preferences.

**Recommended preparation:** [Architecture, interfaces, and design tradeoffs](03-architecture.md), [Uncertainty, statistical evidence, and Bayesian decisions](06-inference.md)

**Related course companions:** [Book 6](../B6/OPEN-BOOK.html), [Book 14](../B14/OPEN-BOOK.html), [Book 19](../B19/OPEN-BOOK.html)

## 1. Screen feasibility before preferences
A decision model needs a feasible set. If an option violates a mandatory braking distance or accessibility constraint, a high score on cost cannot make it acceptable. Start with hard constraints and record which stakeholder or regulation established each one. Soft preferences then rank feasible alternatives, rather than overriding obligations.

For alternative \(j\), weighted utility \(U_j=\sum_iw_i v_i(x_{ij})\) requires more than normalized weights. Value functions \(v_i\) encode how the decision-maker values differences in the criterion; linear value may be inappropriate when crossing a response-time threshold has disproportionate consequences. Weight elicitation should be based on comparable swings, not assigning percentages to labels without scale definitions.

## 2. Pareto dominance precedes arbitrary scoring
Alternative A dominates B if it is no worse on every desired criterion and strictly better on at least one. Dominated options can be removed without choosing weights, assuming the criteria and their directions are agreed. Remaining nondominated alternatives form a Pareto set. The selection among them is a value judgment informed by consequences, not a mathematical discovery of a uniquely best engineering design.

Document changes in stakeholder perspective. A maintenance team may prioritize repair time, while riders prioritize access and speed. The goal is not to erase disagreement but to reveal which tradeoffs cause it.

## 3. Use uncertainty to identify decision thresholds
Suppose a fleet expansion improves expected wait by a model-dependent amount. Instead of displaying only a single estimate, ask which values would reverse the decision. Run sensitivity analysis over demand, maintenance downtime, travel-time variability, and cost. If the ranking is robust over plausible ranges, expensive new data may not be decision-relevant. If choices reverse near a plausible threshold, targeted measurements can have high value.

The expected value of perfect information (EVPI) is the expected payoff if you could choose with full information minus the best payoff from acting now. It is an upper bound on what perfect information is worth under the assumed model and preferences. A real study costs money and yields imperfect observations; its expected value is usually smaller.

## 4. Beware weighted-score theater
Weights can be chosen to justify a favored design after the fact. Ordinal ratings can be treated as interval measurements without justification. Uncertainty can be compressed into expected values that hide low-probability catastrophes. Guard against these by publishing the feasible set, utility construction, weight sensitivity, probabilistic assumptions, and rejected alternatives.

## 5. Turn sensitivity analysis into an information plan
After finding a weight or parameter threshold that reverses an architecture decision, identify the measurement that would most reduce decision uncertainty. If demand growth drives the reversal, collecting better estimates of actual trip requests may matter more than refining the energy model. If all alternatives fail the same safety requirement, better stakeholder utility weights are irrelevant until feasibility is restored.

Apply a three-stage decision process: (1) establish minimum acceptable performance, (2) eliminate dominated feasible options, and (3) apply preferences and uncertainties to the remaining Pareto set. This separates what *must* be achieved from what stakeholders *prefer*. Record disagreements rather than forcing an artificial consensus.

For probabilistic decisions, calculate an expected payoff under each action and each plausible state. Then ask whether tails, irreversibility, or safety obligations make expected payoff an inadequate primary criterion. A conservative threshold or robust optimization rule may be more appropriate, and the change in decision principle should be explicit.

**Check your reasoning:** If an option's expected cost is lowest but its performance violates an accessibility requirement in a low-demand neighborhood, it cannot be rescued by a favorable weighted average. Hard constraints, equity obligations, and risk appetite belong in the decision formulation, not as afterthoughts.

## Guided worked example

### Worked information-value case
Two demand states, high and low, each have probability 0.5. Expanding fleet capacity gives net payoffs \(+120\) and \(-40\) (arbitrary monetary units); not expanding gives 0 in both states. Without more information, expansion has expected payoff 40, so choose it. Perfect knowledge would expand only in high demand, yielding expected payoff 60. Thus \(EVPI=60-40=20\) units. A study costing more than 20 cannot be justified solely by this idealized decision benefit.

## Independent transfer exercise

Create a four-criterion decision matrix for two fleet architectures with one hard constraint. Identify Pareto-dominated options, vary preferences, and calculate EVPI for one uncertain demand input.

[Open the companion hypothetical lab](labs/10-decisions-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

An adequate memo makes the conditional choice explicit and shows what evidence could realistically reverse it.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
