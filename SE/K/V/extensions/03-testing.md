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
