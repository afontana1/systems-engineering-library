# Workshop 5 · What does zero observed failure prove?

*Companion to Book VIII, Chapter 4 · Statistical confidence and sample rationale*

## The seduction of a flawless demonstration

Northstar's test team reports 30 successful emergency-stop trials and no observed failures. The briefing slide calls the system “100% reliable.” That conclusion does not follow. The experiment observed 0 failures in a finite sample. Inference about an *unknown underlying failure probability* requires a statistical model and an explicit confidence procedure; inference about operational safety also requires conditions that represent the real mission.

Assume each trial is an independent Bernoulli opportunity with the same unknown failure probability \(p\). The probability of observing no failures in \(n\) trials is \((1-p)^n\). To form a one-sided \(100(1-\alpha)\%\) upper confidence bound after zero failures, solve \((1-p_U)^n=\alpha\). Thus

\[
p_U=1-\alpha^{1/n}.
\]

This is an **exact frequentist upper bound conditional on the Bernoulli assumptions**, not a probability that the true \(p\) is below the bound given these observations. It also does not prove performance beyond the tested conditions.

## Worked example: 30 trials

For \(\alpha=0.05\), \(n=30\),

\[
p_U=1-0.05^{1/30}\approx0.0950.
\]

Even with no failures, failure rates as high as approximately **9.5% per independent trial** are not excluded by this 95% confidence procedure. If the acceptance claim is \(p\le0.01\), 30 trials are insufficient to support it with the same procedure. The minimum sample size to achieve a zero-failure upper bound of 1% satisfies

\[
n\ge\frac{\log(0.05)}{\log(1-0.01)}\approx298.1,
\]

so **299 failure-free trials** are required under the assumptions. That is a sample-size calculation, not a recommendation to ignore consequence, dependence, test coverage, or design evidence.

## Why the assumptions matter

**Independent trials:** Repeating the same physical setup may reproduce the same hidden defect or common-cause failure. **Constant failure probability:** Different routes, temperatures, load states and maintenance conditions can have different risks. **Representative opportunities:** A failure opportunity must be defined before computing a per-trial probability. **No hidden censoring:** Trials that were aborted or declared “not evaluable” require accounting. **Stable configuration:** A software change during the campaign means earlier executions may not apply to the final release. Ignoring these conditions creates false precision.

When several failure modes are assessed together, the experiment's result may not support each mode independently. For safety-critical decisions, combine test evidence with hazard analyses, analysis of coverage, fault injection, review of controls and justified operational limitations. Statistical confidence is one component of an assurance argument.

## Worked problems

**Problem 1.** For 10 failure-free independent trials, compute the one-sided 95% upper bound.

<details><summary>Worked solution 1</summary>

\(1-0.05^{1/10}\approx0.2589\), or 25.9%. A small zero-failure sample is weak evidence for very low failure probability.
</details>

**Problem 2.** What minimum number of failure-free trials is needed for a one-sided 95% upper bound of 5%?

<details><summary>Worked solution 2</summary>

\(n\ge\log(0.05)/\log(0.95)\approx58.4\), so 59 independent failure-free trials.
</details>

**Problem 3.** Is a 95% upper confidence bound the same as saying “there is a 95% probability that \(p\) is below the bound”?

<details><summary>Worked solution 3</summary>

Not in frequentist inference. The 95% describes the long-run coverage of the procedure across repeated datasets. A probability statement about \(p\) given the data requires an explicitly chosen Bayesian prior and posterior model.
</details>

**Problem 4.** An engineering team reruns the same simulator seed 299 times. Can it use the formula to claim 1% reliability?

<details><summary>Worked solution 4</summary>

No. Replaying an identical deterministic realization does not produce independent failure opportunities. Even genuinely different simulated seeds require a credibility argument that the simulator represents the relevant failure mechanism.
</details>

## Transfer to engineering work

Use the supplied Python evidence tool to calculate confidence bounds and sample sizes. Then design a test matrix with operational domains, environmental factors and configuration control. Write two sentences your sponsor could safely publish: one describing observed outcomes, the other describing the **limited inference** supported by the model. Critique an alternative plan that merely increases sample size without improving test representativeness.
