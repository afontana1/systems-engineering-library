## Step 04 integrated case — estimation, pairing, and absence-of-failure claims

In NS-QSE4.1, the estimand must be stated before computing any confidence interval. Three different targets appear: the **mean conditional arrival rate**, the **difference in per-day mean wait between two policies**, and the **chance of an unacceptable event**. A large number of synthetic requests cannot make these targets interchangeable. The observation units in the demand file are 24 one-hour windows, not independent per-request samples.

### A hierarchical-rate estimate

The controlled Gamma–Poisson calculation produces posterior means \(122/12.2=10\) requests/hour in clear conditions and \(218/12.2\approx17.869\) in storm conditions. Its sampled 95% interval assumes the prior family, constant conditional rate, complete counts, and independent increments. If thunderstorms share a latent demand driver across successive hours, treating twelve storm windows as conditionally independent overstates the information in those observations. Longer time-series records and residual checks would be needed before assigning operational confidence.

### A paired interval for comparing dispatch configurations

The simulator reuses the **same generated arrival stream** for each policy and each synthetic day. On storm days, the baseline policy has two servers, each requiring 10 minutes/request; the combined design has three servers at 8 minutes/request. Their sample mean of *daily mean waits* is approximately **16.880** versus **2.346 minutes**. The paired change is therefore about **14.533 minutes/day**, baseline minus combined. For paired day \(i\), define \(D_i=\bar W_{i,\mathrm{baseline}}-\bar W_{i,\mathrm{combined}}\). A nonparametric paired bootstrap resamples the twelve \(D_i\) values as whole blocks, not separate individual requests. With the controlled seed and 2,500 resamples, the percentile interval is approximately **[10.86, 18.01] minutes**.

This is a *synthetic conditional bootstrap interval*. It quantifies across-day variability under the chosen generator and small set of invented cases; it is not a confidence interval for genuine emergency operations. Reusing arrival streams is helpful because random variability from separate streams does not mask the policy contrast. But it does not remove structural bias, omitted staff breaks, dispatch priority, or weather-correlated travel time.

### A zero-event sample is not proof of zero risk

If zero failures are observed in \(n\) independent Bernoulli trials with constant failure probability \(p\), then \(P(0\mid p)=(1-p)^n\). Equating this probability with \(\alpha=0.05\) yields the one-sided 95% upper bound \(p_U=1-0.05^{1/n}\). For 20 independent zero-failure trials, \(p_U\approx0.1391\); for 100, \(p_U\approx0.0295\). This calculation cannot be applied naïvely to 100 trips sharing one grid supply: common-cause failure breaks the independent-trial assumption. Nor does it license a safety claim from the *absence of recorded* incidents when incident detection is incomplete.

### Reproducible engineering record

The report records the actual bootstrap method, policy definitions, number of paired days, and input hash. Report the request-weighted mean wait separately from the equal-day mean; heavy-demand days receive larger weight in the former. A review must identify missing data, censoring at the observation-window boundary, whether over-time completions count, and whether the target population is the same as the sample.

<details><summary>Worked exercises and interpretation</summary>

1. **One-sided upper bound.** Compute the upper failure bound for \(n=20\): \(1-0.05^{1/20}\approx0.1391\). Explain that *zero observed* and *zero possible* failures are not equivalent.
2. **Pairing.** For synthetic daily mean waits baseline [12, 18, 15] and improved [6, 10, 8], paired differences are [6, 8, 7], mean **7 minutes**. Independently resampling baseline and improved lists destroys the shared-day covariance and changes the estimand's uncertainty.
3. **Missingness.** If four high-demand storm windows are unrecorded, what fails? An interval based on the remaining hours can be narrow yet biased, because missingness is associated with the operating condition being estimated.

</details>

**Boundary:** Statistical precision is not model validation. Book 8's assurance logic and the advanced Architecture collection still require credible operational measurements and configuration-specific evidence.
