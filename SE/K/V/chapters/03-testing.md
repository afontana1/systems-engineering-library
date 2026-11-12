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

<!-- STEP04-CONNECTED-EVIDENCE-START -->
## Step 04 integrated case — NS-CE4.1: denominator integrity and acceptance

The case's acceptance claim concerns **all requests received during the defined test window**, not only requests ultimately served. That choice of estimand is an engineering decision. Suppressing rejected or unserved requests from the denominator would make a poorer service look more reliable. The data below are completely synthetic and form a small instructional cohort, not an independent representative field trial.

### Declare outcomes and the intended estimand

Each request is assigned exactly one terminal class: timely, late-but-served, or unserved. The 80 requests are partitioned by accessible versus standard demand:

| Group | Timely | Late | Unserved | All requests |
|---|---:|---:|---:|---:|
| Standard | 55 | 6 | 3 | 64 |
| Accessible | 10 | 3 | 3 | 16 |
| **Total** | **65** | **9** | **6** | **80** |

The marginal timely-service fraction is $\widehat p_T=65/80=0.8125$ (81.25%). Among **served requests only**, it is $65/(65+9)=65/74\approx0.87838$ (87.84%). Accessible timely fulfillment across *all* accessible requests is $10/16=0.625$ (62.5%). Therefore both the course's illustrative 90% all-request threshold and 90% accessible threshold fail. The population-level unserved fraction is $6/80=0.075$. These are descriptive proportions of this constructed dataset, not confidence bounds or population performance estimates.

### Separate failure probability evidence from operational timeliness

A different experiment observes **zero failures in 60 trials**, with exact one-sided 95% upper bound on an i.i.d. Bernoulli failure probability

$$p_U=1-\alpha^{1/n}=1-0.05^{1/60}=0.0487029.$$

The numerical statement is conditional on a fixed failure definition, consistent configuration, representative trial design, and independent identically distributed trials. It **does not** establish a 1% upper bound; the example's screening target of $p\le0.01$ fails. Inverting the formula gives $n\ge\lceil\ln(0.05)/\ln(0.99)\rceil=299$ zero-failure *independent* trials for that bound. But running 299 correlated tests of the same input configuration does not create 299 independent pieces of information.

If requests are clustered by dispatch period, a rough design-effect heuristic $n_{\mathrm{eff}}\approx n/[1+(m-1)\rho]$ can illustrate dependence for mean estimands, where $m$ is cluster size and $\rho$ intracluster correlation. **Do not plug this heuristic into the exact zero-failure formula and call the resulting number an exact bound.** Prefer a sampling and inference method designed for the actual cluster structure, plus fault-injection and requirements-driven evidence for systematic hazards.

### What a statistically interpretable acceptance report needs

The test record must name the target population, operating envelope, treatment/exposure, primary endpoint, missing-outcome policy, performance threshold, one- versus two-sided inference, confidence level, calibration and timestamp resolution, group coverage, and stopping rule. The current 80-request table lacks site and time sampling metadata and does not justify a statistical generalization. In a genuine trial, inspect whether accessible trips disproportionately occur during storms, whether test staff intervene, and whether late outcomes are misclassified due to clock synchronization.

If one independently measures the same metric with a simulation using shared inputs, agreement does not imply independent corroboration. Keep separate the uncertainty of measurement, sampling, model form, and configuration transfer. A passing aggregate can conceal failing subgroup outcomes; the accessible result here is an explicit counterexample to aggregate-only review.

### Reproduce and challenge

Run `python3 SE/K/V/code/ns_evidence_case.py` at the repository root. The structured output separately records all-request timeliness, served-only timeliness, accessible timeliness, unserved counts, and the exact zero-failure upper bound. No green dashboard is produced from a measure that excludes unserved requests.

**Worked exercise 1 — denominator bias.** A report announces 87.84% timely service and omits the six unserved requests. Compute the corrected percentage. **Solution:** $65/80=81.25\%$; the served-only statistic overstates the all-request rate by approximately 6.59 percentage points.

**Worked exercise 2 — sensitivity.** If two accessible requests currently late became timely, with all counts otherwise fixed, would the accessible 90% criterion pass? **Solution:** $12/16=75\%$, still below 90%. Fifteen timely accessible requests would be needed because $\lceil0.9(16)\rceil=15$.

**Worked exercise 3 — stopped tests.** After 60 zero-failure trials, the analyst stops because the dashboard is green. Is the assumed preplanned one-sided confidence procedure still justified? **Solution:** Only if stopping did not depend on the favorable data and assumptions were satisfied. A data-dependent sequential rule needs its own error-rate accounting.

**Adverse case.** Set any trial count negative or remove the accessible group in a copied input. Validation must reject the former; an absent required subgroup must not be silently considered a pass. The current instrument is an instructional acceptance *screen*, not a safety certificate.
<!-- STEP04-CONNECTED-EVIDENCE-END -->
