# Simulation calibration and rare-event analysis

## 1. The decisions this method supports

When an engineering model predicts a deadline violation, two questions are easy to confuse: **How well have we estimated its inputs from data?** and **How accurately have we simulated a rare outcome conditional on those inputs?** More simulation draws reduce random Monte Carlo error, but cannot remove calibration error, incorrect model structure, biased instrumentation or a shifted operating population.

This guide adds an end-to-end quantitative example to [simulation output and credibility](simulation-output-and-credibility.md), [correlated uncertainty](correlated-uncertainty-propagation.md) and [experimental design](statistical-inference-and-experiments.md). The examples are deliberately separate: a Poisson arrival-rate model illustrates calibration, and an extreme normal-tail event illustrates variance reduction. **They are not observations of a real shuttle or claims about a real system's rare-event rate.**

## 2. Define the estimand and separate types of uncertainty

Let \(\theta\) denote parameters inferred from operational observations \(D\), \(U\) denote simulation random numbers and \(Y=g(\theta,U)\) denote the reported outcome. At least four uncertainties can matter:

1. *Stochastic variability:* different service or weather realizations even with known parameters.
2. *Parameter estimation:* different plausible \(\theta\) given finite calibration observations.
3. *Model-form discrepancy:* the chosen Poisson, independence or queue discipline assumptions may omit causal mechanisms.
4. *Monte Carlo error:* randomness of the numerical estimator conditional on the specified inputs and model.

The law of total variance clarifies why simulating at only one estimated parameter value is not a full predictive uncertainty analysis:

\[
\operatorname{Var}(Y\mid D)
=\mathbb E_{\theta\mid D}[\operatorname{Var}(Y\mid \theta,D)]
+\operatorname{Var}_{\theta\mid D}\{\mathbb E(Y\mid\theta,D)\}.
\]

This expression presumes a parameter uncertainty distribution; a classical interval or likelihood analysis need not assign a posterior. A complete study states its inferential framework rather than treating a confidence interval as a posterior probability.

## 3. Calibrate a rate to observed counts

Assume independent arrivals follow a stationary Poisson process with rate \(\lambda\) arrivals/hour. Given exposures \(t_i\) and observed counts \(n_i\), the likelihood up to a parameter-independent constant is

\[
L(\lambda)\propto \lambda^{N}e^{-\lambda T},\quad
\ell(\lambda)=N\ln\lambda-\lambda T+C,
\quad N=\sum_i n_i,\;T=\sum_i t_i.
\]

Setting the derivative \(N/\lambda-T=0\) gives \(\hat\lambda=N/T\). The [synthetic calibration dataset](data/calibration_counts.csv) has 39 arrivals in five hours and 51 in another five. Thus \(N=90\), \(T=10\) hours, and

\[
\boxed{\hat\lambda=90/10=9\;\mathrm{arrivals/hour}.}
\]

The observed counts are not necessarily evidence of a stationary Poisson process; they are an exercise **under that model**. To quantify finite-data uncertainty, define the likelihood-ratio deviance

\[
D(\lambda)=2\left[N\ln\left(\frac{\hat\lambda}{\lambda}\right)
-T(\hat\lambda-\lambda)\right].
\]

An approximate 95% profile-likelihood interval consists of positive rates with \(D(\lambda)\le3.84146\), using an asymptotic one-degree-of-freedom chi-squared cutoff. Numerically this is approximately **[7.2664, 10.9896] arrivals/hour**. This is not an exact Poisson confidence interval and can perform poorly for tiny counts or nonstationarity.

### Hold out data instead of grading calibration on its training set

A third *synthetic*, deliberately withheld one-hour interval recorded 14 arrivals. Under the fitted \(\lambda=9\) process, the probability of at least 14 arrivals is

\[
P(N_{1h}\ge14)=1-\sum_{k=0}^{13}e^{-9}\frac{9^k}{k!}\approx 0.0739.
\]

One 7.39% tail outcome does not automatically reject the model; it provides a specific discrepancy to inspect. Repeated unusually high counts, daily seasonality, overdispersion, bursts or correlated arrivals would motivate a richer model and held-out validation. Never use the same count observations both to tune parameters and to advertise an independent confirmation of fit.

## 4. Why brute-force Monte Carlo fails for small probabilities

Suppose the quantity of interest is \(p=P(Z>4)\) where \(Z\sim N(0,1)\). This is a **toy threshold model** chosen because its exact probability is known:

\[
p=\tfrac12\operatorname{erfc}(4/\sqrt2)
\approx 3.167124\times10^{-5}.
\]

A direct estimator with \(n\) independent draws is \(\hat p_{\rm direct}=\frac1n\sum_{i=1}^n\mathbf 1(Z_i>4)\). Its variance is \(p(1-p)/n\). With 50,000 draws the expected number of exceedances is only 1.58. A result of zero, one or two observed events is entirely plausible; the associated relative uncertainty is huge. **Zero exceedances must never be reported as proof that the true event probability is zero.**

## 5. Importance sampling derivation

Choose a sampling distribution \(q(x)=\phi(x-4)\), a normal density shifted toward the event region, while the target remains \(f(x)=\phi(x)\). Then

\[
p=\int\mathbf1(x>4)f(x)\,dx
=\int\mathbf1(x>4)\frac{f(x)}{q(x)}q(x)\,dx.
\]

The likelihood ratio for \(X\sim N(4,1)\) is

\[
w(X)=\frac{\phi(X)}{\phi(X-4)}
=\exp(-4X+8).
\]

Consequently, the unbiased importance-sampling estimator, conditional on the specified densities, is

\[
\hat p_{IS}=\frac1n\sum_{i=1}^n\mathbf1(X_i>4)\exp(-4X_i+8),
\quad X_i\sim N(4,1).
\]

Its Monte Carlo standard error can be computed from the sample variance of **weighted contributions**, rather than from an unweighted count of threshold exceedances. Shifting a distribution without the likelihood-ratio correction estimates a different probability. If the proposal density is zero where the target event has positive probability, the estimator is invalid.

The deterministic 50,000-draw [Python demonstration](code/calibration_rare_events.py) prints:

| Quantity | Reproducible result | Interpretation |
|---|---:|---|
| Exact mathematical benchmark | 0.00003167 | Under \(N(0,1)\), not field risk |
| Direct MC, one fixed seed | 0.00004000 (2 events) | Extremely noisy |
| Shifted importance sampling | about 0.00003166 | Properly weighted estimate |
| Importance-sampling standard error | about 0.00000030 | Numerical precision conditional on chosen distributions |

The point is not that importance sampling *always* works better. A poor proposal or heavy-tailed weight distribution can cause enormous variance and unstable estimates. Diagnose weights, proposal support, effective sample size, sensitivity to proposal choice and independent replicate stability. For real engineered rare events, common-cause mechanisms and rare regimes omitted from the model remain invisible even to a numerically precise estimator.

## 6. An end-to-end model credibility plan

A responsible engineering study can use this sequence:

| Stage | Required output | Failure mode to challenge |
|---|---|---|
| Define intended use | Which design decision, consequence and population | Wrong outcome or time scale |
| Define observation process | Timestamp origin, missingness, clock calibration, selection | Biased or drifting measurements |
| Fit parameters | Likelihood, units, training set and uncertainty | Hidden pooling across nonstationary regimes |
| Challenge model structure | Held-out data, residuals, dependence, high-load scenarios | Fit driven by a convenient but false family |
| Verify implementation | Analytic limiting cases, deterministic seeds, unit tests | Coding or numerical error |
| Estimate rare outcomes | Appropriate importance sampling, splitting or other scheme | Apparent zero from insufficient direct draws |
| Interpret decision | Sensitivity to parameters, proposal and structural alternatives | Numerical precision mistaken for assurance |
| Governance | Version, reviewer, constraints and revalidation triggers | Stale model reused beyond evidence scope |

For the Campus Mobility example, a fitted dispatch arrival rate could inform service-capacity studies, but the independent toy \(P(Z>4)\) tail must **not** be presented as the shuttle's deadline-miss probability. Connecting them would require an explicit causal simulation that maps input arrivals, service resources, buffering, network conditions and software behavior to the chosen missed-deadline event. The end-to-end model would then need calibration and independent challenge data.

## 7. Reproduce and investigate

Run from the project root (no packages required):

```sh
python3 SE/K/methods/code/calibration_rare_events.py
```

**Exercises:** (1) Derive \(\hat\lambda=N/T\) from the likelihood. (2) Solve the profile deviance equation numerically and explain why a 95% likelihood-ratio interval is approximate. (3) With 50,000 direct draws, derive the expected count of \(Z>4\) events: \(50,000p\approx1.584\). (4) Change the proposal shift from 4 to 1 or 7; compare standard errors, not only point estimates. (5) Describe an unmodeled queue burst that would invalidate the original Poisson-calibrated system prediction without affecting the normal-tail program's math.

## 8. Sources and course paths

- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — experimental data analysis, uncertainty and statistical inference.
- [NASA-STD-7009B: Models and Simulations](https://standards.nasa.gov/node/263) — model credibility processes tied to intended use.
- [Book 11, chapter 8](../B11/chapters/08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md) and [chapter 11](../B11/chapters/11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md); [Book 10, chapter 9](../B10/chapters/09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md); courses EN.645.757, EN.645.758 and EN.645.756.

**Scope:** Synthetic data and probability models for instruction. No real-world rare failure probability, operational forecast, model accreditation or safety acceptance is implied.
