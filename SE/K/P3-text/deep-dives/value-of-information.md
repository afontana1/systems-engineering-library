# When learning first is worth more than choosing now

**Cross-course pathways:** Decision Science 3 and 11; Metrics 11; Simulation Foundations 7.

## A two-state decision tree

Suppose a flexible fleet policy A pays +$50k in high-demand conditions and -$20k in low demand. A conservative policy B pays +$25k in both states. With equal probability of high and low demand, `EV(A)=0.5(50)+0.5(-20)=15` thousand and `EV(B)=25` thousand. Without new information, choose B under risk-neutral expected value.

Perfect information would reveal the state *before* choice: choose A in high demand and B in low, yielding `0.5(50)+0.5(25)=37.5` thousand. **Expected value of perfect information** `EVPI=37.5-25=12.5` thousand. This is an upper bound on the expected value of any information about the state for the specified model, before information cost; real tests are imperfect and may arrive too late.

Call `expected_value_and_evpi([[50,-20],[25,25]],[0.5,0.5])` to reproduce the calculation.

## Imperfect signals require Bayes' rule

If a demand forecast has sensitivity 80% for high demand and specificity 70% for low demand, with prior 50/50, then `P(high | positive) = .8×.5/(.8×.5 + .3×.5) ≈ .727`. Do *not* use the model's accuracy as the posterior probability of high demand. Evaluate the best action conditional on each signal, then average signal-specific values to compute expected value of sample information (EVSI). An experimental program has value only if it could change a decision enough to offset its own cost and delay.

## A robust alternative

Expected value is not the only rational criterion. A risk-averse authority may minimize the worst regret; an irreversible investment may value downside protection. Compute the regret of choosing A or B relative to the state-specific optimal action, and report different decision criteria separately. Explain trade-offs to stakeholders rather than silently choosing a criterion.

**Exercise:** If the probability of high demand is p, A has expected `70p-20` (thousands), B remains 25. They tie at `p=45/70≈0.643`. A forecast with posterior p below that threshold cannot alter a risk-neutral decision to choose B.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
