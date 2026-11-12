# Statistical inference and design of engineering experiments

*Technical method guide · Estimation, inference, factorial experiments, interactions, and confirmation · Phase 2 expansion*

**What this guide enables.** Formulate a population claim, choose and interpret an interval or test, construct a small factorial experiment, calculate main and interaction effects, and evaluate whether the study can support a system-level decision. The examples are synthetic, not observations from an operating system.

**Before starting:** [Probability and dependence](../encyclopedia/probability-and-dependence.md), [statistical acceptance](../encyclopedia/statistical-acceptance-and-confidence.md), [design of experiments](../encyclopedia/design-of-experiments.md), and [measurement traceability](../encyclopedia/measurement-traceability-and-calibration.md).

## 1. Define the estimand before collecting numbers

Suppose the Northstar dispatch team is evaluating two settings: **A** is a revised queue scheduler and **B** is a replicated dispatch worker. The team wants to reduce *mean processing latency in milliseconds for eligible requests during a predeclared load profile*. That italicized phrase is the **estimand**: the target quantity in a specific population and condition. It is different from the maximum observed latency, 99th percentile, service-availability probability, or causal effect of the scheduler in other traffic conditions.

A statistical question needs a six-part declaration: population, response and units, factor settings, sampling or randomization unit, uncertainty source, and decision threshold. A traceable request identifier is an observation identifier, but it does not automatically define an independent experimental unit. If thousands of requests share one deployment and one outage, treating all requests as independent treatment replications creates pseudoreplication.

Measurements also have instrument and sampling errors. Clock drift can shift all observed times, while random request variation makes individual observations fluctuate. An interval derived from request variation does not automatically include clock-calibration uncertainty. Keep an uncertainty budget for each mechanism, and avoid describing an interval for the *mean* as an interval for *individual future requests*.

## 2. Confidence intervals, tests, and effect sizes answer different questions

Let independent observations be \(Y_1,\ldots,Y_n\), with sample mean \(\bar Y\) and sample standard deviation \(s\). For an approximately normal independent sample with unknown variance, a two-sided \(100(1-\alpha)\%\) confidence interval for the population mean is

\[
\bar Y\;\pm\;t_{1-\alpha/2,n-1}\,\frac{s}{\sqrt n}.
\]

The \(t\) multiplier is a quantile of Student's distribution, and \(s/\sqrt n\) estimates the standard deviation of the **sample mean**, not of a future individual event. The coverage interpretation concerns repeated applications of the procedure under its assumptions. It is not a posterior probability for an already fixed parameter.

For example, four hypothetical independent latency observations of 9, 10, 11, and 10 milliseconds have \(\bar Y=10\), sample variance \(s^2=2/3\), and standard error \(0.40825\) ms. With \(t_{0.975,3}=3.18245\), the 95% confidence interval is approximately \([8.70,11.30]\) ms. It is extremely wide for a performance acceptance claim. Larger, independent, representative samples and a model appropriate to the required percentile would be needed for tail-service requirements.

A test of \(H_0:\mu=\mu_0\) evaluates compatibility of observations with a specified null model. It does **not** measure the probability that \(H_0\) is true, and a large p-value is not proof of equivalence. If the engineering question is whether two implementations are sufficiently similar, establish a practical equivalence margin \(\Delta\) *before* looking at the result and use an appropriate equivalence interval/test. Always report the effect estimate and uncertainty, not only a significance flag.

For binary outcomes with \(k\) successes among \(n\) independent Bernoulli trials, an illustrative alternative to the naive \(\hat p\pm z\sqrt{\hat p(1-\hat p)/n}\) interval is the **Wilson score interval**, which remains well behaved at \(k=0\) and \(k=n\):

\[
\frac{\hat p+\frac{z^2}{2n}\pm z\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}}}{1+\frac{z^2}{n}}.
\]

This is a two-sided *approximate confidence interval*, not an acceptance rule or a substitute for the one-sided exact binomial bounds described in the [verification handbook](requirements-verification-handbook.md). The [example calculator](code/factorial_doe.py) computes Wilson bounds for independent attribute data as a separate demonstration.

## 3. Why a factorial experiment is more informative than one-factor-at-a-time trials

In a \(2^2\) full factorial, the scheduler setting \(A\in\{-1,+1\}\) and replication setting \(B\in\{-1,+1\}\) are crossed. Every combination is run, allowing estimation of the main effects *and* their interaction. In contrast, changing one factor while freezing the other can miss a scheduler whose benefit depends on replication.

A common coded model is

\[
Y=\beta_0+\beta_A A+\beta_B B+\beta_{AB}AB+\varepsilon.
\]

For balanced observations, \(\beta_A\) is **half** the difference between the mean response at \(A=+1\) and at \(A=-1\); likewise for \(B\). The interaction effect is the difference between the mean of the two same-sign treatment combinations and the mean of the opposite-sign combinations. Thus the coded interaction coefficient is one-half the interaction effect:

\[
E_{AB}=\frac{\bar Y_{--}+\bar Y_{++}}2-\frac{\bar Y_{+-}+\bar Y_{-+}}2,\qquad \beta_{AB}=E_{AB}/2.
\]

Using four *synthetic* independent runs at each combination, the experiment records:

| A: scheduler | B: replication | Four latency runs (ms) | Cell mean (ms) |
|---|---|---|---:|
| −1 | −1 | 10.5, 10.8, 10.3, 10.6 | 10.55 |
| +1 | −1 | 8.9, 9.0, 9.2, 8.8 | 8.975 |
| −1 | +1 | 7.9, 8.1, 8.0, 7.8 | 7.95 |
| +1 | +1 | 6.8, 6.7, 6.9, 6.6 | 6.75 |

The estimated scheduler main effect is

\[
E_A=\frac{8.975+6.75}{2}-\frac{10.55+7.95}{2}=\boxed{-1.3875\;\mathrm{ms}}.
\]

Likewise, \(E_B=-2.4125\) ms and \(E_{AB}=+0.1875\) ms. In this setting, either modification reduces the mean latency; a small positive interaction means their combined improvement is slightly *less* than the sum of separate improvements on the chosen effect scale. This is not evidence that future large deployments behave similarly.

A difference of 2.4 ms might be statistically discernible but operationally irrelevant if the actual service objective concerns a four-second tail. Conversely, a small change in a low-probability tail can be crucial. The **measure of effectiveness** must motivate the response variable; the analysis cannot repair a poorly chosen measure.

## 4. Quantifying experimental uncertainty honestly

Under independent normal residuals with common variance across the four cells, the pooled within-cell mean-square error is

\[
MSE=\frac{\sum_{a,b}\sum_{j=1}^{r}(Y_{abj}-\bar Y_{ab})^2}{4(r-1)}.
\]

For \(r=4\), there are 12 residual degrees of freedom. Each main effect contrasts two groups of eight observations, so

\[
SE(E_A)=SE(E_B)=SE(E_{AB})=\sqrt{MSE/4}.
\]

A nominal 95% effect interval uses \(t_{0.975,12}\approx2.1788\). In small experiments, normality, independence, constant variance, and honest randomization matter. Check residual patterns and treatment order; a drift in demand over the test period can masquerade as a treatment effect. This example has only four independent replicates per combination. It illustrates analysis, not a general-purpose power guarantee.

**Randomization:** choose treatment order independently of time-of-day changes. **Blocking:** if the study necessarily spans mornings and evenings, include each treatment in each block and model the block. **Replication:** repeat the *whole treatment under independently reset or independent conditions*—not four measurements from one uninterrupted run misrepresented as four independent experiments. **Confirmation:** freeze the chosen settings and conduct a new representative run whose data did not influence model selection.

The [data file](data/dispatch-factorial.csv) contains synthetic test values with a nominal randomized run order, and [the standard-library analyzer](code/factorial_doe.py) calculates cell means, effects, pooled residual uncertainty, and a normal-equation effect report. It does not produce a causal claim unless its experimental-unit and randomization assumptions are established.

## 5. Power, stopping rules, and the distinction between inference and acceptance

The sensitivity of a test depends on actual effect size, residual variability, \(\alpha\), and sample size. A common planning error is to assume that a positive result can be guaranteed by choosing a small enough significance threshold; that makes detection *harder*. Predeclare a minimally important reduction \(\delta\), plausible residual standard deviation \(\sigma\), false-positive risk, desired power, and the model that converts them into run counts. For a simple two-group approximate planning formula with equal group sizes,

\[
n_{\text{per group}}\approx \frac{2\sigma^2(z_{1-\alpha/2}+z_{1-\beta})^2}{\delta^2}.
\]

This does not automatically apply to blocked, sequential, clustered, factorial, non-normal, or adaptive studies. For the actual analysis use the appropriate design matrix and variance structure. Do not peek at an ordinary fixed-sample p-value after every few observations and stop as soon as it looks favorable without an approved sequential design. Distinguish **inference** about an effect from **acceptance** of a system claim: a measured improvement does not itself demonstrate satisfaction of a system-level limit.

## 6. Engineering interpretation and review checklist

A reviewer should be able to answer: Was the factor order randomized? Were test runs independent? Is the observed effect large enough to matter? Does the model predict an engineering-relevant measure? Are noise, environmental changes, missing observations, and response transformations documented? Was a hold-out confirmation run made? Does the conclusion hold only for the tested load and configuration?

**Typical failure patterns:** mistaking repeated measurements for independent samples; confusing confidence with probability of compliance; assuming non-significance means equivalence; ignoring interactions; selecting factors after reading results; unreported exclusions; declaring the best cell without a confirmation trial; extrapolating outside the tested factor range.

## 7. Contrast three kinds of uncertainty interval

It is easy to use a mathematically correct interval for the wrong question. A **confidence interval for a mean** asks what range of mean values is compatible with the observed sample under a model. A **prediction interval** asks what values a *future observation* could take and must include both uncertainty in the mean and the intrinsic observation-to-observation variation. Under independent normal observations, one new observation has an illustrative two-sided prediction interval

\[
\bar Y\pm t_{1-\alpha/2,n-1}s\sqrt{1+\frac1n}.
\]

A **statistical tolerance interval** instead seeks bounds that cover at least a specified proportion of the *population* with a specified confidence level. Its construction is different from both formulas above and generally needs a tolerance factor that depends on sample size, coverage proportion and confidence. In systems engineering this matters because a requirement such as “99% of requests within four seconds” concerns a population tail. A narrow confidence interval for the *mean* is not evidence of sufficient tail coverage.

With the illustrative observations 9, 10, 11 and 10 ms, the confidence interval for the mean is \([8.70,11.30]\) ms. The prediction interval for one independent future reading is much wider:

\[
10\pm3.18245\sqrt{\tfrac23}\sqrt{1+\tfrac14}
\approx [7.095,12.905]\;\mathrm{ms}.
\]

Neither is a 99%-population-content tolerance bound. The exercise is not to memorize three names, but to identify which uncertainty statement matches the decision-maker's actual claim.

## 8. Interactions, aliasing, and experimental extrapolation

Full factorials become expensive as factors multiply: \(2^k\) treatment combinations for \(k\) two-level factors, before replication. A **fractional factorial** samples fewer combinations by introducing a declared *alias structure*. For example, with a generator \(C=AB\), the observed factor-C column equals the AB interaction column, so the experiment cannot distinguish a genuine C main effect from an AB interaction. Calling one of those effects “significant” does not establish which physical mechanism caused it.

A screening study may intentionally accept such confounding when higher-order interactions are judged unlikely; that assumption should be documented and challenged in follow-up experiments. Once influential factors are identified, a response-surface design may add center points and intermediate values to investigate curvature and locate a useful operating region. A two-level linear model cannot justify optimum behavior outside the observed range, nor can it detect all nonlinearities.

An experiment's hierarchy of explanations is therefore **mechanism → planned contrast → observations → uncertainty model → independent confirmation**. The causal inference comes from randomization and controlled conditions, not from the apparent precision of a regression output. If a deployment changes software, hardware and demand simultaneously, a statistical comparison cannot uniquely attribute the effect to one engineering change without further design or assumptions.

## 9. An uncertainty-aware decision worksheet

Before publishing a result, complete the following record, then keep the underlying data and code with the test configuration:

| Question | Example answer for the synthetic factorial |
|---|---|
| Target population | Eligible requests during the fixed simulated load profile |
| Response and unit | Processing latency in milliseconds; a mean, not a percentile |
| Independent unit | One separately initialized and run experimental trial |
| Factor contrasts | Scheduler A and replication B, each at two declared settings |
| Blocking/randomization | Run order recorded; actual real-world order would need independent randomization and block control |
| Reported effect | \(E_A=-1.3875\) ms; \(E_B=-2.4125\) ms; \(E_{AB}=0.1875\) ms |
| Uncertainty model | Equal residual variance, normal independent errors; four replications per cell |
| Unsupported extrapolation | 99th-percentile response, unseen peak-load profiles, lifecycle energy and outage behavior |
| Confirmation | New randomized runs under a frozen treatment decision and a prespecified acceptance rule |

A review should reject a claim whose study target changes after seeing the data. If the team genuinely needs percentile performance, redesign the measurement campaign for tail inference and representative traffic conditions rather than stretching the mean-latency confidence interval.


### Sources and curriculum connections

- [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook): engineering-oriented inference, measurement, and experimental design.
- [NIST e-Handbook, Process/Product Improvement](https://www.itl.nist.gov/div898/handbook/pri/pri.htm): factorial and response-surface methods, assumptions, and study organization.
- [Book 10, Chapter 4 — Estimation and inference](../B10/chapters/04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md), [Chapters 5–6 — Experimental design and interactions](../B10/chapters/05-design-efficient-experiments-with-factors-responses-noise-power-rand.md), [Book 8, Chapter 4 — Test statistics and DOE](../B8/chapters/04-apply-measurement-science-statistics-doe-and-sample-rat.md).
- **Curriculum:** EN.645.756 (weeks 3–7), EN.645.769 (statistical evidence design), EN.645.757 (simulation experiments). Reproduce the factorial analysis, then explain why the experiment does not alone support a 99th-percentile acceptance claim.

**Exercise:** change the final \(A=+1,B=+1\) observation from 6.6 to 8.6 ms; recompute the interaction estimate and pooled variance. Explain why the mean changes and why an unusually variable cell calls the common-variance model into question.
