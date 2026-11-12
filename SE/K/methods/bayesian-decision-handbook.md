# Bayesian decisions, imperfect tests, and value of information

*Technical method guide · Decision science, statistical evidence, and system trades · Phase 1 expansion*

**What this chapter enables.** Given uncertain technical states, competing actions, a noisy diagnostic test, and an explicit loss model, calculate prior and posterior decisions, expected value of perfect information (EVPI), expected value of sample information (EVSI), net information value, and the assumptions that could reverse the recommendation.

**Prerequisites:** [Probability and dependence](../encyclopedia/probability-and-dependence.md), [engineering trades](../encyclopedia/engineering-trades.md), and [risk versus issue](../encyclopedia/risk-vs-issue.md). The complete numerical calculation is included; external readings are optional references rather than hidden prerequisites.

## 1. Define a decision, not merely a probability

In a fictional shuttle vehicle controller, a hidden fault may cause an expensive operational loss after release. A hardware redesign can eliminate this particular modeled fault, but costs money and may delay deployment. A diagnostic bench test may indicate whether the fault exists; it is imperfect and has a price. The engineering choice is whether to **ship**, **redesign**, or **buy information before choosing**.

A Bayesian *inference* updates beliefs after observations. A Bayesian *decision* additionally attaches consequences to the actions available after those observations. Let \(\theta\) be the unknown state, \(a\) an action and \(z\) a possible test observation. For losses \(L(a,\theta)\), the action minimizing posterior expected loss is

\[
a^*(z)=\underset{a\in\mathcal A}{\operatorname{arg\,min}}\;\sum_{\theta}L(a,\theta)P(\theta\mid z).
\]

The minimum is over *feasible* actions. A design that violates a non-negotiable safety constraint must not become permissible merely because its expected cost looks attractive.

## 2. Baseline case and units

Use the following **illustrative**, mutually exclusive states and losses. Amounts are **thousands of dollars** (k$), not empirical estimates.

| State | Prior | Ship loss | Redesign loss |
|---|---:|---:|---:|
| Fault present, \(F\) | 0.20 | 100 k$ | 15 k$ |
| Fault absent, \(\neg F\) | 0.80 | 0 k$ | 15 k$ |

The redesign is assumed to eliminate *only this fault* completely and to introduce no new risk. Those assumptions are intentionally simplistic and must be challenged in a real trade study.

Without a test, the expected shipping loss is \(0.20(100)+0.80(0)=20\) k$. The expected redesign loss is \(15\) k$. The rational **risk-neutral** choice under this model is **redesign**, because \(15<20\). This step is an optimization over actions, not a statement that the prior 20% fault probability is accurate.

### The action threshold

If the posterior fault probability is \(q\), shipping costs \(100q\) k$ in expectation while redesign always costs 15 k$. The actions switch when

\[
100q=15 \quad\Longrightarrow\quad q_{\mathrm{switch}}=0.15.
\]

Below 15% ship; above 15% redesign; at exactly 15%, expected losses tie. This makes the value of the diagnostic test easy to interpret: it is useful if plausible test outcomes move the posterior across that boundary.

## 3. Compute what the proposed diagnostic actually tells us

Suppose test sensitivity is \(P(+\mid F)=0.90\), and specificity is \(P(-\mid\neg F)=0.95\). The false-positive rate is 0.05 and the false-negative rate is 0.10. These are assumed conditional probabilities, not asserted performance of any real device.

A convenient frequency interpretation uses 1,000 hypothetical components:

| True state | Positive | Negative | Total |
|---|---:|---:|---:|
| Fault present | 180 | 20 | 200 |
| Fault absent | 40 | 760 | 800 |
| **Total** | **220** | **780** | **1,000** |

Thus

\[
P(+)=0.90(0.20)+0.05(0.80)=0.22,\qquad P(-)=0.78.
\]

Bayes' theorem produces two different posteriors:

\[
P(F\mid +)=\frac{0.90(0.20)}{0.22}=\frac{9}{11}\approx0.81818,
\]

\[
P(F\mid -)=\frac{0.10(0.20)}{0.78}=\frac{1}{39}\approx0.02564.
\]

A positive result moves the fault probability above the 15% decision threshold, so **redesign after positive**. A negative result puts it below the threshold, so **ship after negative**. Notice that “a 90% sensitive test” is not the same as “a positive result implies a 90% chance of fault”; the prior and specificity both matter.

## 4. Evaluate the proposed decision policy before buying the test

After a positive observation the team redesigns, incurring 15 k$. After a negative observation it ships, risking loss only if the test missed an actual fault. Expected loss before paying the test fee can be calculated two equivalent ways.

**By observation branch:**

\[
E[L\mid\text{test policy}]=P(+)(15)+P(-)\,P(F\mid-)(100).
\]

Substitute the numbers: \(0.22(15)+0.78(0.025641)(100)=3.3+2.0=5.3\) k$.

**By joint event:** positive outcomes always trigger redesign (0.22 × 15), while false negatives incur shipping loss (0.02 × 100). This is again 5.3 k$.

Without testing the optimal expected loss is 15 k$, so

\[
\mathrm{EVSI}=15-5.3=9.7\ \mathrm{k\$}.
\]

If the diagnostic costs 5 k$ and creates no other effects, testing yields total expected cost \(5.3+5=10.3\) k$ and a **net expected improvement of 4.7 k$**. The break-even all-in information acquisition cost is 9.7 k$. A 6 k$ direct fee plus a 4 k$ expected delay penalty is therefore *not* worthwhile, even though the test is scientifically useful.

## 5. Perfect information is an upper bound, not a purchase offer

If the true fault state could be known for free, the decision-maker would ship when sound and redesign when faulty, yielding

\[
E[L\mid\text{perfect information}]=0.20(15)+0.80(0)=3\ \mathrm{k\$}.
\]

The no-test baseline is 15 k$, hence

\[
\mathrm{EVPI}=15-3=12\ \mathrm{k\$}.
\]

For this consistent fixed action/loss model,

\[
0\leq\mathrm{EVSI}=9.7\leq\mathrm{EVPI}=12\ \mathrm{k\$}.
\]

If a calculation produces EVSI greater than EVPI, review the probability normalization, whether the available actions changed between calculations, and whether testing costs were deducted in one case but not the other. A test can appear to create new value by enabling an action that was *not* in the original action set; that is a different decision model and should be stated explicitly.

## 6. Sensitivity: when does the recommendation reverse?

A single expected value can conceal deep uncertainty. Test each input for its *effect on the optimal action*, not merely its effect on one intermediate posterior.

**Prior sensitivity.** The no-test decision is to redesign when \(P(F)>0.15\). If strong new evidence justifies a prior of 0.10, shipping becomes the no-test policy. EVSI must then be recomputed against that *new* optimal baseline.

**Specificity sensitivity.** Increasing false positives increases the frequency of needless redesigns. At a false-positive rate \(f\), the positive-test probability is \(0.2(0.9)+0.8f\). If the positive branch still triggers redesign and the negative branch still ships, the policy cost is \([0.18+0.8f](15)+0.02(100)\). That expression is valid only while both branch decisions remain optimal. The key lesson is to **check the policy thresholds after changing any input**.

**Consequence sensitivity.** If the actual fault loss is not 100 k$ but an uncertain distribution that includes safety or mission-critical effects, expected monetary loss may be an inappropriate sole objective. Model hard constraints and unacceptable outcomes separately.

**Test-dependence sensitivity.** Repeated diagnostic results may be conditionally dependent because they share an instrument calibration, environmental factor, or underlying failure mechanism. Multiplying likelihoods as though repeated tests were independent can create dangerously overconfident posteriors.

## 7. Link decision analysis to design robustness

Value of information asks whether to learn more **before** acting; robustness asks what happens if uncertain inputs shift and the team **must act**. These are complementary questions. An architecture may be attractive on expected loss and fragile to tail outcomes. Specify the risk criterion before ranking options: expected loss, chance constraint, maximum regret, downside quantile, or a non-compensable safety bound.

For an example of transparent scenario mixing, suppose peak demand occurs with probability 0.30. Design H has conditional unacceptable-wait probability 0.60 in peak demand and 0.08 otherwise. Design M has 0.12 and 0.02 respectively. Then by total probability:

\[
P(\text{violation}\mid H)=0.30(0.60)+0.70(0.08)=0.236\approx24\%,
\]

\[
P(\text{violation}\mid M)=0.30(0.12)+0.70(0.02)=0.050=5\%.
\]

This reconstructs the **approximately 24% versus 5%** figures discussed in [Book 14, Chapter 11](../B14/chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md) as explicit *hypothetical inputs*, not as observed performance. The scenario probabilities and conditional violation rates need substantiation before using the figures for a real decision. If peak demand correlates with charging faults, a two-state simplification may understate risk.

## 8. Reproduce the results and try adversarial checks

The [Python decision calculator](code/decision_test_value.py) uses only the Python standard library. It prints the prior choice, posterior branches, EVSI, EVPI, and hypothetical demand-mixture probabilities. Its assertions include the inequalities \(0\leq\mathrm{EVSI}\leq\mathrm{EVPI}\) for the declared case.

**Exercise A.** Recompute EVSI if test specificity drops to 0.80. Do the positive and negative policies remain optimal? State the resulting break-even diagnostic price.

**Exercise B.** Explain why a test with perfect sensitivity might still have low value if it arrives after the redesign decision is irreversible. Which variable in the mathematical decision model encodes the available time to act?

**Exercise C.** The 20% prior comes from a small fleet operating in a different climate. Propose a sensitivity interval, collect evidence for the likelihood model, and explain how you would communicate deep uncertainty rather than presenting 20% as a precise physical truth.

### Worked answer to Exercise A

With specificity 0.80, the false-positive probability is 0.20, so \(P(+)=0.18+0.16=0.34\). The posterior after positive is \(0.18/0.34\approx0.5294\) (redesign), while after negative it is \(0.02/0.66\approx0.0303\) (ship). The expected loss of the policy is \(0.34(15)+0.02(100)=7.1\) k$, and **EVSI = 15−7.1 = 7.9 k$**. At the original 5 k$ test fee, the net expected improvement is 2.9 k$. No physical performance conclusion follows from these made-up likelihoods.

## 9. Evidence and sources

A decision record needs state definitions, prior origins, raw likelihood data, action feasibility, cost bounds, consequence units, event timing, source quality, model version, alternative policies, sensitivity analysis, and the authority accepting residual risk. A posterior probability is a conditional mathematical consequence of assumptions; it is not a license to ignore bad inputs.

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) — inferential and experimental methods for engineering.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — decision making and technical risk in system lifecycles.
- [Book 14, Chapter 11](../B14/chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md), [EN.645.784 course](../../C/P3/EN645784.md), [Bayesian concept reference](../encyclopedia/bayesian-value-of-information.md).

**Scope note:** The decision model, probabilities, costs and scenarios are invented teaching examples. Formal authorization, safety assurance and technical risk management require project-specific evidence.
