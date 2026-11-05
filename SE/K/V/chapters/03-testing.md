# 3 · Statistical assurance is a claim about evidence, not certainty

*Graduate methods companion · System Test and Evaluation (Book VIII)*

Testing is a sampling process performed on a configured system in a defined environment. A passing test means only that an observation satisfied a criterion under the test conditions. It does not logically entail that the system will perform acceptably over every operational context. Graduate-level test engineering therefore connects measurement, experimental design, statistical inference, operational exposure, and the strength of the claim being made.

## 3.1 Define the estimand before choosing a test

An estimand is the quantity we intend to infer: the 90th-percentile response time for all requests during winter peak service, the probability of a critical dispatch failure per mission, or the effect of a new controller on missed trips. Each estimand implies a population, configuration, operating environment, and unit of analysis. A convenient laboratory dataset may fail to represent that population.

Separate **verification** ('the artifact satisfies its specified requirements') from **validation** ('the deployed system addresses the intended stakeholder need'). A scheduler may meet its internal latency contract while unacceptable numbers of requests are rejected. A statistic reported only for successful requests can hide this failure by changing the denominator.

## 3.2 Exact zero-failure inference

Suppose $n$ independent, identically distributed Bernoulli trials all succeed. If $p$ denotes the unknown per-trial failure probability, the likelihood of zero observed failures is $(1-p)^n$. The one-sided exact upper $(1-\alpha)$ confidence bound $p_U$ solves

$$(1-p_U)^n=\alpha\quad\Rightarrow\quad p_U=1-\alpha^{1/n}.$$

At 95% confidence and $n=60$, this is approximately $0.0487$. Zero failures in 60 trials does **not** prove that $p<0.01$; to obtain a 95% upper bound of at most 0.01 under the same assumptions, we need

$$n\geq\frac{\ln(0.05)}{\ln(0.99)},$$

or 299 successful independent trials after rounding up. Even then the conclusion is about the defined Bernoulli trial population—not the entire space of software bugs, common-cause hazards, or future operating changes. Dependence, unequal mission exposure, and biased scenario selection violate the simple calculation.

The 'rule of three' gives $p_U\approx3/n$ for large $n$ and small $p$; the exact expression should be preferred when it is easy to compute.

## 3.3 Measurement error and test uncertainty

Suppose a response-time measurement is formed by subtracting two clocks. If clock errors have standard deviations $\sigma_1$ and $\sigma_2$ with correlation $\rho$, the variance of the difference includes

$$\operatorname{Var}(e_2-e_1)=\sigma_1^2+\sigma_2^2-2\rho\sigma_1\sigma_2.$$

Independent clocks with 2 ms and 3 ms standard deviation give $\sqrt{13}\approx3.61$ ms combined standard deviation. A common timing source may increase or decrease the difference uncertainty depending on how errors correlate. Always specify the measurement chain, calibration, sampling rate, clock synchronization, rounding, and missing-data handling before declaring a narrow pass margin meaningful.

Test procedure fidelity matters too. A performance criterion with a 600-ms cutoff cannot be evaluated credibly from timestamps quantized to whole seconds. A safety constraint involving stale route data cannot be tested if the recorded timestamp is overwritten by a downstream service.

## 3.4 Design experiments to isolate causes

A regression or comparative test is an experiment if it attempts to estimate a treatment effect. Pairing two architectures on the *same simulated demand streams* can sharply reduce variance. If $Y_{Ai}$ and $Y_{Bi}$ are responses under alternatives A and B for matched scenario $i$, define $D_i=Y_{Ai}-Y_{Bi}$. A confidence interval for the paired mean difference under suitable assumptions is

$$\bar D\pm t_{1-\alpha/2,n-1}\frac{s_D}{\sqrt n}.$$

Using differences $[5,9,7,11]$ minutes gives mean 8, sample standard deviation $\sqrt{20/3}\approx2.582$, standard error $1.291$, and a 95% $t$ interval with three degrees of freedom of approximately $[3.89,12.11]$ minutes. With only four paired cases, the interval is broad. It is an illustration, not a robust operational estimate.

Blocking, randomization, treatment definition, experimental independence, and stopping rules matter as much as the formula. If the team keeps running trials until a favorable result appears, the nominal confidence guarantee no longer applies without adjusting for sequential monitoring. If many metrics are screened simultaneously, the chance of at least one spurious significant finding can rise.

## 3.5 Multiple evidence sources do not automatically combine

Design reviews may include analysis, inspection, simulation, bench tests, field demonstrations, and safety arguments. These sources are not interchangeable, and they can share common errors. A simulation and a bench test may use the same flawed input dataset. Treating their agreement as two independent confirmations can exaggerate confidence.

An assurance case should identify the claim, the scope, the supporting evidence, explicit warrants connecting evidence to claim, and known defeaters. A defeater is a condition that would invalidate the inference: undocumented code changes, unrepresentative demand, stale calibration, dependence between trials, or an untested failure state. Bounded conclusions are a professional strength, not an embarrassment.

## 3.6 Readiness decisions must count what is excluded

For Northstar, imagine a trial reports a 14-minute p90 wait among served requests. Before celebrating, ask how many were rejected, timed out, or canceled. If 40% of requests never receive service, the denominator changes the interpretation. A defensible test dashboard reports throughput, rejected requests, elapsed wait over the intended population, adverse events, uncertainty, and evidence coverage by mode and stakeholder group.

A readiness recommendation may be 'conditional approval for a restricted trial' rather than unconditional release. State the approved route set, demand envelope, fallback mode, monitored thresholds, open hazards, responsible signatory, and the event that triggers re-evaluation.

## Worked problems with explained solutions

**A.** Find the exact one-sided 95% failure-probability upper bound after 60 independent zero-failure trials. **Solution:** $1-0.05^{1/60}\approx0.0487$.

**B.** How many zero-failure trials support $p_U\leq0.01$ at 95%? **Solution:** Round $\ln(0.05)/\ln(0.99)$ upward to 299. That does not establish a software-wide safety guarantee.

**C.** Calculate the paired 95% mean-difference interval for $[5,9,7,11]$. **Solution:** $8\pm3.182(2.582/2)\approx[3.89,12.11]$ minutes.

**D.** A test passes with p90 wait 14 minutes, but rejects 40% of requests. Is operational suitability established? **Solution:** Not without a population-level criterion and evidence about excluded requests. The reported p90 is conditional on being served.

## Research challenge

Design a verification argument for a dispatch deadline under correlated network delays and nonstationary demand. Justify trial independence, measurement resolution, scenario selection, and the basis for limiting the released operational envelope.

**Practice:** [Statistical assurance laboratory](../labs/03-testing.html) · [Executable notebook](../notebooks/03-testing.ipynb).

## 3.7 Power and acceptance decisions

Failure to reject a null hypothesis is not evidence that an architecture meets an equivalence or noninferiority criterion. To show two designs are 'close enough,' specify a technically meaningful margin $\delta$ and use an appropriate equivalence or noninferiority analysis. Otherwise a small underpowered study can appear reassuring merely because it detects no difference. Similarly, a statistically significant 0.1-ms improvement may be operationally irrelevant when the decision deadline is 600 ms.

Statistical power depends on effect size, variability, sample size, and the test procedure. It should be planned against the minimum effect worth detecting, not retrofitted after seeing a favorable outcome. Sequential testing requires a predeclared monitoring rule; repeatedly peeking at data and stopping on the first significant result changes the error rate. Test plans should name primary endpoints, secondary diagnostics, subgroup analyses, missing-data handling, and decision thresholds in advance.

## 3.8 Verification evidence as a structured argument

Suppose a 95% upper failure-probability bound is below the numerical requirement. The result remains conditional on the independence and representativeness of the trials. It says nothing directly about systematic design defects triggered by a rare but untested input sequence. Complement statistical acceptance with requirements-based tests, adversarial boundary tests, formal interface checks, fault injection, and independent reviews. Diverse evidence may increase confidence when it addresses distinct failure mechanisms, but a pile of correlated tests is not equivalent to strong independent evidence.

When reporting a test, attach the test case, requirement revision, build hash, environment, calibration status, raw results, analysis code, anomalies, exclusions, and reviewer decision. This information permits another engineer to reproduce both the arithmetic and the claim. If the evidence chain is incomplete, describe the defect explicitly instead of silently converting an observed pass into an unconditional verified status.
