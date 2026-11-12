### F03 extension · Sampling precision, subgroup performance, and diagnostic evidence

**Define the estimand.** In NS-U4.1 the measured dispatch success fraction $\hat p=k/n$ is 72/80 under the nominal 8-second rule, not the probability of safe arrival or a 90% confidence statement. If, purely for teaching, observations were independent and identically distributed Bernoulli trials, a two-sided 95% Wilson interval uses $z=1.96$:

$$\frac{\hat p+z^2/(2n)\pm z\sqrt{\hat p(1-\hat p)/n+z^2/(4n^2)}}{1+z^2/n}.$$

The lower Wilson endpoint for $72/80$ is below 90%: the observed threshold is not statistically established. Clustering by incident, vehicle, radio network, or operating shift invalidates the simple i.i.d. interpretation. The conservative timing count is only 67/80. The accessible group has 10 guarded successes among 16 requests; one cannot infer that its population service level is 85%.

**Diagnostic example.** For a route blockage, set prior $P(B)=0.15$, alarm sensitivity $P(+|B)=0.80$, and false-positive rate $P(+|\neg B)=0.10$. Bayes gives

$$P(B|+)=\frac{0.80(0.15)}{0.80(0.15)+0.10(0.85)}=0.58537.$$

If a second alarm were independent *conditional on blockage state*, another positive produces approximately 0.91866. If the alarms share a sensor or weather source, this second posterior overstates the gain; repeat observations do not automatically supply independent evidence.

**Credibility gate.** Measurement definition, calibration, population coverage, experiment power, and external validation are distinct. Explicitly document a decision threshold before observing the data, retain excluded cases, and report subgroup denominators; otherwise the analysis can silently select for success.

**Worked exercise and solution.** Change the alarm's false-positive rate to 0.20 while retaining the prior and sensitivity. The posterior becomes $0.12/(0.12+0.17)\approx0.4138$, a substantial decrease. The posterior is an *uncertain belief* about blockage, not an instruction to override a route closure; authorization must be checked separately.

**Reproduce:** [D03](../derivations/03-bayesian-test-and-information.md), [D04](../derivations/04-binomial-confidence-and-test-coverage.md), [runner](../flagship-integration/code/ns_u_case.py).
