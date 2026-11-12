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

## In-depth method: a complete Bayesian test-purchase decision

The [Bayesian decision and value-of-information guide](../methods/bayesian-decision-handbook.md) develops the test-purchase example from prior beliefs to optimal actions, imperfect evidence, sensitivity, and the value ceiling for buying a test. Its [Python calculator](../methods/code/decision_test_value.py) reproduces the calculations without external packages.

For a component with a 20% prior fault probability, shipping produces an assumed loss of 100 k$ if faulty and 0 k$ otherwise. Redesign costs 15 k$ and is assumed to eliminate that fault. The no-test expected losses are 20 k$ to ship and 15 k$ to redesign, so redesign is the risk-neutral baseline decision.

Suppose test sensitivity is 90% and specificity is 95%. A positive test occurs with probability \(0.9(0.2)+0.05(0.8)=0.22\). The posterior fault probabilities are

\[
P(F\mid +)=\frac{0.18}{0.22}\approx0.8182,\qquad
P(F\mid -)=\frac{0.02}{0.78}\approx0.02564.
\]

Shipping is preferable only if fault probability is below the redesign-versus-shipping break-even value \(15/100=0.15\). Consequently, the optimal test-conditioned policy is **redesign after positive; ship after negative**. The loss before test fee is \(0.22(15)+0.02(100)=5.3\) k$; EVSI is \(15-5.3=9.7\) k$. Perfect information would cost \(0.2(15)+0.8(0)=3\) k$, so EVPI is \(15-3=12\) k$. A 5 k$ test yields 4.7 k$ expected net benefit *if* its test accuracy, cost, timing and modeled consequences are credible.

A critical qualification is that no one can interpret those numbers as real defect risk without data supporting the prior, conditional test performance, redesign effectiveness and loss estimates. The mathematics is exact *under the invented model*. Decision quality still depends on the model's connection to reality.




## Step 02 review studio — an imperfect test can still change a decision

Suppose a synthetic subsystem has prior failure probability `P(F)=0.20`. A perfect mitigation costs 25 units and eliminates this modeled loss; an unmitigated failure costs 100 units. Without a test, expected failure loss is 20, so **do not mitigate** under a risk-neutral cost rule. Now add an imperfect test with sensitivity `P(+|F)=0.80` and false-positive rate `P(+|not F)=0.10`.

The positive probability is `P(+)=0.8(0.2)+0.1(0.8)=0.24`; posterior failure probability after a positive is `0.16/0.24=2/3`. After a negative it is `0.04/0.76≈0.05263`. Choose mitigation if posterior failure cost exceeds 25: mitigate after positive, do not mitigate after negative. Expected cost **after test, before test fee** is `0.24(25)+0.76(0.05263×100)=6+4=10`. Thus sample information is worth `20−10=10` units before costs, under the simplified model. A test fee of 6 leaves net value 4.

**Solved challenge:** if the fee rises to 12, does the test remain worthwhile for cost minimization? **No:** net value is −2. This example assumes the mitigation eliminates the modeled loss, no time penalty, accurate test characteristics, and risk neutrality. Safety obligations may invalidate a pure expected-cost decision.

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
