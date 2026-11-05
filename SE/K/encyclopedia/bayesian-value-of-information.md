# Decision uncertainty and value of information

**Reference entry · Analytics, modeling, simulation and decisions · Expanded reference**

## Definition and diagnostic distinction

**Bayesian decision analysis** combines prior beliefs, evidence likelihoods, and consequences to choose actions under uncertainty. **Value of information (VOI)** measures how much better a decision could become after observing information, not how much information is scientifically interesting. A precise measurement of something unrelated to the decision can have almost no decision value; imperfect evidence about a pivotal uncertainty can be very valuable.

## Theory: updating beliefs and evaluating decisions

For hypothesis `H` and evidence `E`, `P(H|E) = P(E|H)P(H) / P(E)` when the probabilities are well defined. Updating requires a likelihood model: how likely is the observation if the hypothesis is true versus false? With decision `d` and state `θ`, choose the action maximizing expected utility `E[U(d,θ)|E]`, subject to noncompensable constraints. The **expected value of perfect information** (EVPI) is the difference between expected utility with perfect state knowledge and the best expected utility without it. **Expected value of sample information** (EVSI) uses a realistic noisy test and cannot exceed EVPI under consistent assumptions, before costs.

A test may be statistically informative but too late to influence architecture, or it may require substantial operational risk. Information value is conditional on available actions, time to act, test cost, and decision authority.

## Worked example: whether to purchase a field test

A component has a 20% prior probability of a costly hidden fault. Shipping without redesign costs `$0` if sound and `$100k` if faulty, for an expected loss of `$20k`. Redesign costs `$15k` and eliminates that particular fault. Without further information, redesign is preferable. Perfect knowledge would permit redesign only in the faulty 20% of cases, for an expected `$3k` cost. Thus the **EVPI is `$15k - $3k = $12k`**. A proposed test costing `$5k` is worth considering, but not automatically justified: its sensitivity, false-positive rate, delay, and resulting conditional actions determine EVSI.

## Engineering use and evidence

Specify states, priors and their basis, available actions, test likelihoods, consequences, constraints, and timing. Build a decision tree or influence diagram showing information arriving before the action it can affect. Stress priors and utilities; compare expected results with minimax-regret or robust strategies where probability knowledge is weak. Explicitly calculate net VOI after test costs and schedule effects.

## Limitations and connections

Bayes' theorem cannot rescue an untrustworthy likelihood or an incoherent loss model. Treat expert priors as revisable judgments, not measured frequencies. Connect VOI to **trade studies**, **risk**, **experimental design**, **model credibility**, and **enterprise investment**.

## Technical analysis: calculate sample information, not just perfect information

The perfect-information calculation above is a useful *upper bound*, but a purchasing decision needs a measurement model. Suppose the proposed test has **90% sensitivity** for the hidden fault and **95% specificity** for a sound component. With prior fault probability 0.20, the probability of a positive result is `0.90(0.20) + 0.05(0.80) = 0.22`. The posterior fault probability following a positive is `0.18 / 0.22 ≈ 0.8182`; following a negative it is `0.02 / 0.78 ≈ 0.02564`.

If a redesign costs `$15k` and eliminates only this fault, the optimal policy is **redesign after positive** (`$15k < $81.82k` expected shipping loss) and **ship after negative** (`$2.564k < $15k`). Expected loss *before paying for the test* is `P(+)(15k) + P(fault and negative)(100k) = 0.22(15k) + 0.02(100k) = $5.3k`. The no-test optimal loss was `$15k`, so **EVSI = $9.7k**. With a `$5k` test price and no schedule consequences, the expected net gain is `$4.7k`. As a consistency check, `0 ≤ EVSI ($9.7k) ≤ EVPI ($12k)`.

The apparent precision here is mathematical, not empirical. A different prevalence, specificity, or cost of redesign changes the optimal policy and test value. Check the posterior after *each* observation and ensure that evidence arrives **before** the action it can change; testing after a binding production decision has no operational decision value even if the data are informative.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.
- [NASA · NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263) — Credibility practices for modeling and simulation used in decisions.

## Follow the knowledge

**Related concepts**

- [Probability, dependence, and technical uncertainty](probability-and-dependence.md)
- [Risk, issue, uncertainty, and opportunity](risk-vs-issue.md)
- [Engineering trade studies: making preferences and uncertainty inspectable](engineering-trades.md)
- [Design of experiments and sensitivity](design-of-experiments.md)

**Go deeper in the 240-chapter textbooks**

- [Book 14, Chapter 03: Book 14 · Chapter 03 — Model decisions, uncertainties, evidence, constraints, and alternatives](../B14/chapters/03-model-decisions-uncertainties-evidence-constraints-and-alternatives.md)
- [Book 14, Chapter 11: Book 14 · Chapter 11 — Analyze uncertainty, sensitivity, robustness, regret, and value of information](../B14/chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md)
- [Book 18, Chapter 07: Week 07 · System of Systems Engineering · Chapter 07 — Bayesian networks, causality, and decision uncertainty](../B18/chapters/07.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
