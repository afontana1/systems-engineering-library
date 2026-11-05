# Statistical acceptance: sampling decisions are not proofs of perfection

**Canonical reference · Analytics, modeling, simulation and decisions · Expanded reference · Internal editorial review; independent peer review not performed**

## A decision rule for incomplete evidence

A statistical acceptance plan determines what observation will lead an authorized decision-maker to accept or reject a *defined* lot, process, or performance claim. It is not the same as an estimate of the true defect probability, and a passed sample does not prove the absence of defects. NIST's engineering statistics handbook emphasizes acceptance sampling as a decision about lots and explains how its operating-characteristic (OC) curve depends on the assumed sampling model.

For attribute sampling, define sample size `n`, maximum accepted defective count `c`, and defect probability `p` under the plan's assumptions. With independent Bernoulli observations (or a sufficiently large lot for binomial approximation), the number of defectives is binomial. The probability of accepting a lot with defect fraction `p` is `P_accept(p) = Σ[k=0..c] C(n,k) p^k (1−p)^(n−k)`. For finite-lot sampling without replacement, a hypergeometric model may be required. Mission tests with correlated failures, repeated runs on one unchanged system, and changing environmental modes violate the naive independence picture.

## Worked example: producer and consumer risk

Suppose the plan randomly inspects **100 independent items** and accepts a lot if **at most one** is defective: `n=100, c=1`. If the true fraction defective is `p=0.01`, the probability of acceptance is `0.99^100 + 100×0.01×0.99^99 ≈ 0.7358`. Thus even a lot with only **1%** defectives is rejected about **26.4%** of the time under this plan. For a lot with `p=0.05`, the acceptance probability is `0.95^100 + 100×0.05×0.95^99 ≈ 0.0371`: roughly **3.7%** of such lots pass.

These probabilities characterize a plan's operating behavior, not the quality of any single accepted lot. A team choosing an acceptance-quality level and a rejectable-quality level should specify tolerated producer and consumer risks *at those levels* and then solve for a sampling plan that supports them. Avoid selecting `(n,c)` from habit and only afterward discovering how much risk it assigns to stakeholders.

## Zero observed failures and confidence limits

For **n independent trials**, all with a common unknown failure probability `p`, observing zero failures has probability `(1−p)^n`. Inverting the corresponding exact one-sided 95% binomial test gives an upper confidence bound `p_upper = 1 − 0.05^(1/n)`. For `n=100` and zero failures, `p_upper ≈ 0.02951`, or **2.95%**. The statement “zero failures in 100 tests proves reliability at least 99%” is not supported at 95% confidence; the sample is too small for that claim.

This interval is a frequentist coverage procedure under the sampling model, not a 95% probability that the fixed but unknown `p` lies below the bound. If tests share software, hardware or climate conditions, effective information may be far less than `n` independent replications. Testing a single unit repeatedly also does not necessarily establish a production-lot defect fraction.

## Three acceptance questions that must not be confused

1. **Conformance:** did this *specific configuration* meet a deterministic requirement on the measured trial?
2. **Population performance:** what can these samples support about the true rate or distribution of future outcomes, under a defined population model?
3. **Decision risk:** what are the consequences of accepting a bad lot or rejecting a good one, with what authority and loss function?

Continuous performance metrics require other models: a pass/fail count cannot establish a 99th-percentile latency bound without an appropriate sampling and analysis plan. Rare catastrophic events typically require multiple evidence sources—analysis, architecture controls, formal properties, historical data and operational monitoring—rather than an impractically large test-only demonstration.

## Design and evidence discipline

Predeclare the requirement, lot/population, test selection mechanism, independence assumptions, conditions and exclusions, acceptance threshold, confidence/risk convention, failed-test handling and stop rules. Record exact configurations and instrument limitations. If a team repeats tests until a favorable result appears, the nominal false-accept probability may be invalid. Similarly, if developers tune the product after looking at the sample, subsequent acceptance should use a new controlled plan.

Treat acceptance as a governed decision with documented residual uncertainty; do not use statistical phrases to imply certainty beyond the model.

## Selected source-to-claim references

- **T1 · Acceptance sampling is a lot decision, not quality estimation:** [NIST/SEMATECH e-Handbook, 6.2.1 What is Acceptance Sampling?](https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm).
- **T2 · Binomial OC curve and producer/consumer risk:** [NIST/SEMATECH e-Handbook, 6.2.3.2 Choosing a Sampling Plan with an OC Curve](https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc232.htm).

## Follow the knowledge

- **Prerequisites:** [Probability and dependence](probability-and-dependence.md), [Verification matrix](verification-matrix.md).
- **Related concepts:** [V&V](v-and-v.md), [Model credibility](model-vv-and-credibility.md), [Reliability and maintainability](reliability-availability-maintainability.md).
- **Go deeper:** [Book 8, Chapter 10 — Evidence sufficiency](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md); [Book 10, Chapter 8 — Censored reliability evidence](../B10/chapters/08-analyze-reliability-availability-maintainability-degradation-and-cen.md).
