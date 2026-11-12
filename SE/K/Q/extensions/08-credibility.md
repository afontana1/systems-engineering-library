## Step 04 integrated case — an auditable quantitative argument, not a qualification claim

The NS-QSE4.1 release closes an eight-chapter chain: declared observations and conditioning assumptions → parameter inference → paired experiments → verified event scheduling → numerical ODE benchmarking → feedback stability analysis → constrained choice → a bounded evidence decision. It is a model-based argument whose conclusions are **conditional on explicitly synthetic inputs**. It does not constitute evidence that an actual regional transportation or battery system is safe or fit for use.

### Distinguish three credibility questions

**Code verification:** Does the implemented model solve its specified mathematical problem? The queue tests verify nonnegative ordered waits and service conservation. The thermal solver is compared against an analytical solution: the exact two-hour value is **37.6444°C**, Euler at one-hour step gives **38.5600°C**, and at quarter-hour steps gives **37.8377°C**. Convergence in this benchmark demonstrates the expected numerical behavior for this case, not the correctness of thermal physics.

**Model validation:** Is the model adequate for an explicit intended use? No independent regional dispatch measurements, validated arrival process, observed service-time distribution, route disruptions, accessibility-priority mechanisms, calibrated heat generation, or actual actuator data were supplied. A deliberately withheld **synthetic generator** comparison has mean error (model minus synthetic reference) **−1.375 minutes** and root-mean-square error \(\sqrt{\sum_{i=1}^8 e_i^2/8}\approx1.904\) minutes. This exercises discrepancy calculations but **cannot be labeled field validation**. It comes from an invented comparator, not independent observed behavior.

**Decision authorization:** Even a verified and validated model does not grant permission to deploy. The controlled configuration records `false` for operator, accessible-stakeholder, safety and data-governance approval. The case therefore returns **HOLD**, irrespective of the lowest illustrative cost score. Numeric optimization cannot set those Boolean approvals to true.

### Credibility arguments must cite configurations and claims

A source-specific evidence register should record claim ID, intended operational context, input revision or SHA-256, formula or software revision, test method, expected range, observed discrepancy, reviewer, and expiry/refresh conditions. The JSON output embeds a SHA-256 hash of its precise input file. Editing the input and rerunning yields new output and a new hash; editing the input without recomputing must be treated as stale evidence. This proves *provenance continuity for the local file*, not authenticity of real measurements or external approvals.

| Claim | Evidence presently available | Boundary / missing evidence |
|---|---|---|
| Demand uncertainty is regime-dependent | Gamma–Poisson worked estimates and mixture identity | No operational sampling frame or missingness study |
| Queue implementation conserves requests | Deterministic trace tests and per-day counts | No shared fleet-state or real dispatch trace |
| Combined policy reduces synthetic storm waits | Paired common-stream comparison and bootstrap | Conditional model effects; no field causal identification |
| Thermal integration solves the chosen ODE | Analytic benchmark, step-size comparison | No experimentally calibrated thermal constants |
| Combined policy is deployable | **No qualifying evidence** | Compound timely fraction below 90% and approvals absent |

### Independent-review protocol

A reviewer should: (1) check the declared units and observation definitions; (2) regenerate [`ns-qse4-results.json`](../outputs/ns-qse4-results.json) and the daily CSV from the source; (3) run `python3 -m unittest discover -s SE/K/Q/code -p 'test_*.py'`; (4) perturb inputs using valid and intentionally invalid files; (5) verify the eight linked chapters and unchanged original labs; and (6) independently test claims against an agreed real-world reference if authorized. Sensitivity results and passing code checks are necessary but insufficient for a strong external credibility claim.

<details><summary>Worked exercises and engineering interpretation</summary>

1. **Quantitative discrepancy.** For model values [9, 10] minutes and synthetic comparator [10, 12], the signed errors are [−1, −2], bias is −1.5 minutes and RMSE is \(\sqrt{(1+4)/2}=\sqrt{2.5}\approx1.581\) minutes. This remains a toy consistency check.
2. **Stale evidence.** The input JSON is edited to increase compound demand, but the results file is not regenerated. The prior output hash no longer matches the controlled input; previous screening claims must be marked stale.
3. **Approval gate.** A revised simulation meets 90% timely requests in every synthetic scenario. Can it be deployed? **No.** It has not established operational model validation, safety case acceptance, stakeholder rights or data authority.

</details>

**Review verdict:** NS-QSE4.1 is suitable for a bounded teaching demonstration and independent computational examination. It is **not** calibrated, validated or authorized for dispatch, fleet procurement, safety certification or battery management. Further Step 05 editorial and source-to-claim review remains required.
