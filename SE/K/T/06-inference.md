# Uncertainty, statistical evidence, and Bayesian decisions

*Core Concepts · Quantitative methods · T06*

> Distinguish uncertainty about outcomes from uncertainty about models and assumptions.

**Recommended preparation:** [Requirements, traceability, and assurance arguments](02-requirements.md)

**Related course companions:** [Book 8](../B8/OPEN-BOOK.html), [Book 10](../B10/OPEN-BOOK.html), [Book 14](../B14/OPEN-BOOK.html), [Book 18](../B18/OPEN-BOOK.html)

## 1. An estimate is a statement about information
A simulation can produce a precise decimal while its input assumptions are poorly known. Separate **aleatory variability** (day-to-day randomness) from **epistemic uncertainty** (limited knowledge about rates, models, or contexts). Running more Monte Carlo trials reduces simulation noise; it does not correct a systematically wrong arrival distribution.

Before selecting a statistic, define the engineering estimand: average wait for which users, under what conditions, including which unsuccessful requests? Reporting the 90th percentile only among served passengers can make an outage appear beneficial when it causes more requests to be rejected. A careful experiment reports service fraction and conditional wait together.

## 2. Confidence bounds have sampling contracts
With zero observed failures in \(n\) independent, identically distributed Bernoulli trials, the exact one-sided \(100(1-\alpha)\%\) upper confidence limit on failure probability is \(p_U=1-\alpha^{1/n}\). With \(n=30\) and \(\alpha=0.05\), \(p_U\approx0.0950\). Zero observed failures is consistent with a failure probability approaching 9.5% at this confidence level under the model assumptions. Correlated trials or changed conditions invalidate that simple calculation.

A confidence bound is not a probability distribution over a fixed physical failure rate. Do not casually say there is a 95% probability the true rate lies within this particular frequentist interval. The construction is calibrated over hypothetical repeated sampling.

## 3. Bayesian updating answers a different question
Suppose a prior failure probability \(p\sim\operatorname{Beta}(1,9)\), with prior mean 0.10. After observing two failures in 20 independent trials, the posterior is \(\operatorname{Beta}(3,27)\), with mean 0.10. The unchanged mean does not mean the evidence contributed nothing: the posterior is more concentrated. The choice of prior must be defendable, and a different operating environment may require a hierarchical model rather than mechanical pooling.

For a hypothesis test or sensor, use Bayes' rule in odds form. Posterior odds equal prior odds times the likelihood ratio. A seemingly accurate sensor may produce many false alarms when the event being detected is rare. Always state the base rate and what “accuracy” means.

## 4. Evidence should change decisions
The value of additional information depends on what action it could change. If all plausible parameter values lead to the same architecture, another simulation may add knowledge without changing the decision. If a small shift crosses a feasibility threshold, information about that parameter can be valuable. A good evidence plan identifies decision thresholds in advance and avoids tuning acceptance criteria after results are seen.

## 5. Design statistical studies backward from an action
Imagine a board is deciding whether to authorize a limited pilot. Its rule is that the observed service-completion rate must be at least 90%, with a prespecified uncertainty bound and no unresolved safety-critical anomalies. Before running a test, define the population, measurement procedure, exclusion policy, and analysis plan. A project that changes its denominator after seeing failures destroys the interpretability of the statistic.

Distinguish a **prediction interval** for a future observation from a confidence interval for a population parameter. A very precise estimate of mean waiting time can coexist with an extremely wide range of individual passenger outcomes. For skewed or heavy-tailed delays, report quantiles and non-completion explicitly; the mean may be a poor description of the rider experience.

In Bayesian modeling, posterior conclusions depend on the prior and likelihood. A sensitivity analysis can vary prior strength and reveal how much the evidence actually dominates the prior. Pooling test campaigns across different hardware revisions or weather conditions also requires a model of exchangeability. Treating heterogenous observations as identical can be worse than having fewer data.

**Check your reasoning:** If a test produces no failures in 300 trials, have you proven that the true failure probability is below 1%? No. Under independent Bernoulli assumptions, the exact one-sided 95% upper bound is just below 1%; the observation is evidence conditional on the tested domain and sampling design, not a proof that the system cannot fail elsewhere.

## Guided worked example

### Worked case: why 30 clean trials are insufficient for a 1% target
To obtain a one-sided 95% bound no greater than 1% after *zero* failures, solve \(1-0.05^{1/n}\leq0.01\). This requires \(n\geq\ln(0.05)/\ln(0.99)\approx298.1\), hence at least **299 independent representative trials**. This only addresses one aspect of the reliability argument; representativeness, common-cause behavior, and measurement validity remain open.

## Independent transfer exercise

Using the included calculator, compare zero-failure bounds for 30, 100, and 300 trials. Then describe two realistic reasons why independence would fail in a shuttle-system campaign.

[Open the companion hypothetical lab](labs/06-inference-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

The answer must calculate conditional confidence bounds, explain the assumptions, and avoid equating trial count with operational proof.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.


<!-- STEP04-T1-START -->

## Step 04 T1 — Evidence-driven correction and worked transfer

### T1 audit finding: the denominator and the inference are different claims

The NS-T4.1 fixture has 40 requests, of which 32 were served, five rejected, and three remain pending. Every served request satisfies the nominal eight-second timing limit, but only 26 of **all 40** are timely after adding the declared 0.8-second clock-uncertainty allowance. Thus the guarded all-request fraction is \(26/40=0.65\), not \(32/32=1\). The accessible subgroup contains eight requests, of which six meet that guard: \(6/8=0.75\). Neither denominator can be inferred from a conditional sample of completed trips.

For *a different experiment* consisting of 300 independent Bernoulli trials and **zero** failures, the exact one-sided 95% upper failure-probability bound is \(1-0.05^{1/300}=0.0099361\), about 0.994%. Do **not** apply that bound to the forty-request fixture: it has unsuccessful outcomes, different observation conditions, and potential within-day dependence. Counting 300 messages from one outage as 300 independent proof trials would be an invalid sampling contract.

**Practice and explained solution.** Recompute the guarded all-request rate with one additional rejected request, holding the number of timely completions at 26: it becomes \(26/41\approx0.6341\). Explain why reporting only completed requests would conceal deterioration. In a real study, define the population, sampling unit, missingness rules, and intended operational configuration *before* applying an interval method. [Run the T1 integrated laboratory](labs/T1-INTEGRATED-CASE.md).

<!-- STEP04-T1-END -->
