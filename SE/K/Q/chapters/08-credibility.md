# Model credibility and evidence-based engineering assurance

*Textbook-depth conceptual sequence · EN.645.757 / EN.645.758 / EN.645.769 / EN.645.782 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 11](../../B11/OPEN-BOOK.html), [Book 12](../../B12/OPEN-BOOK.html), [Book 8](../../B8/OPEN-BOOK.html), [Book 16](../../B16/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## Credibility belongs to a claim and its use

An engineering model is not "validated" in the abstract. Credibility is relative to a specific intended use, operating envelope, decision consequence and available evidence. A scheduling simulation might be adequate to compare software queue disciplines under normal demand but inadequate to certify patient transport during a regional outage. The same code can be appropriate for one low-consequence decision and dangerously incomplete for another.

Begin with a claim such as: "Configuration B serves at least 90% of emergency requests within 30 minutes under the specified 2026 winter storm scenario set." Decompose it into assumptions: representative storm demand, correctly implemented dispatcher, credible travel-time model, correct outage and message-delay behavior, appropriate sample size, measurement completeness, and configuration traceability. Each assumption becomes a potential evidence need or limitation. A model-based argument fails when it equates reproducible computation with trustworthy real-world inference.

## Verification, validation and uncertainty

**Code verification** asks whether a numerical method is implemented correctly (for example, event counts and time accounting). **Solution verification** asks whether numerical error is small enough for the calculation. **Model validation** asks whether the representation is adequate relative to external referents for the intended use. **Uncertainty quantification** describes variability and incomplete knowledge in results and inputs. These activities overlap but cannot substitute for each other. Passing every unit test does not establish that a simulator's failure modes resemble field failures.

A structured credibility plan lists: context of use, decision thresholds, model assumptions, data provenance, referent evidence, V&V results, uncertainty budgets, sensitivity experiments, and explicit restrictions on use. For simulation-based acceptance, the plan should be agreed before inspecting favorable results. Otherwise analysts can silently change scenarios, thresholds or treatment of incomplete cases until a preferred answer appears.

## A quantitative error budget

Suppose predicted mean wait differs from reference measurements. A useful decomposition is \(\text{observed discrepancy}=\text{parameter uncertainty}+\text{structural discrepancy}+\text{numerical error}+\text{measurement error}\), understood conceptually rather than as a directly additive identity without further assumptions. Some terms are correlated and not identifiable from the same observations. A convergence test can constrain numerical error. Calibration on historical data may reduce parameter mismatch but risks overfitting; evaluation on genuinely held-out conditions tests transfer. A model trained on normal weekday traffic should not automatically support extreme-event decisions.

For a scalar model \(y=f(x,\theta)\), a first-order variance approximation is \(\mathrm{Var}(y)\approx J\Sigma J^T\), where \(J=\partial f/\partial\theta\) evaluated at nominal parameters and \(\Sigma\) is their covariance matrix. This approximation assumes locally smooth behavior and sufficiently small uncertainties. Near capacity thresholds, discontinuities or phase transitions invalidate simple linearization; scenario-based or stochastic methods are often needed. It is also important not to treat standard deviations from different sources as independent without evidence.

## Discrepancy and falsification

A useful test tries to break a model's assumptions. Northstar should inject a shared communications outage, bursty demand, duplicate requests, unavailable vehicles, and clock skew. The simulator should not silently continue as though all systems have perfect observations. For each stress case record expected behavior, actual model behavior, missing mechanisms, and whether the gap matters to the decision. A discrepancy ledger is evidence of active model governance, not a sign of failure to be hidden.

Stress tests should be selected from physical mechanisms and mission hazards, not only from convenient Gaussian parameter ranges. Counterexamples are especially valuable: if the model predicts lower wait when requests are rejected, that is not necessarily a software bug; it may reveal a metric that conditions on successful service. An assurance argument must include the full denominator and acknowledge incentives created by its metrics.

## The assurance chain and configuration

A defensible digital evidence chain relates the requirement baseline, model version, input dataset and seed, analysis script, execution environment, resulting artifact, review finding, and decision. Reproducibility asks whether the same computation can be rerun. Provenance asks where its inputs and assumptions originated. Validity asks whether that computation measures something real and relevant. These are distinct claims. A cryptographic hash can identify an artifact but cannot prove that its underlying demand assumptions are representative.

When models feed multiple engineering teams, controls are needed for interface semantics and units. A model change that renames a field without changing its meaning may be harmless; a change that silently switches latency units from seconds to milliseconds can invalidate an entire system performance budget. Schema checks, versioning, dimensional tests and explicit change impact should accompany model release.

## A decision-quality review

The reviewer should ask what specific conclusion is supported, which conditions were exercised, which hazards remain unmodeled, and how robust the conclusion is to reasonable alternative assumptions. For high-consequence use, independent confirmation and stronger real-world evidence may be required. An honest outcome may be "conditionally suitable for ranking candidates under normal operations, not suitable for certification." This is a meaningful engineering finding and a clear instruction for additional work.


## Further depth: independent evidence and graded confidence

A credible simulation-based assurance argument combines different evidence types. Unit tests demonstrate implementation properties, analytic benchmark comparisons check solution correctness, field observations test representativeness, and controlled experiments test predictive discrimination between alternatives. All these can share a hidden assumption, so apparent agreement may not imply independence. For example, an analyst may calibrate a traffic simulator using the same historical dataset later called an "independent validation set." That is data reuse, not an external challenge.

A useful validation matrix lists operating conditions against critical behaviors. Rows might include ordinary demand, peak surge, outage, delayed telemetry, route restriction and dispatch override. Columns might include queue behavior, travel duration, vehicle energy, operator intervention, and cross-agency coordination. Each cell indicates whether there is a credible referent, evidence strength, uncertainty, and a planned or completed test. A blank cell is a visible limitation; do not fill it with a green check solely because another cell passed.

Model credibility can be structured by a risk-informed process: define decision consequence, identify failure pathways that could invalidate the model, allocate evidence effort accordingly, and require an independent reviewer where consequences justify it. Some important claims involve human behavior, institutional incentives and ethically contested outcomes that cannot be settled by numerical validation alone. The appropriate evidence may include participatory stakeholder review, qualitative analysis and field pilots, alongside simulations.

### Credibility verdicts should be bounded

The most helpful statement is often neither "validated" nor "invalid" but **fit for a bounded purpose**. For example: "The model is suitable for screening three dispatch policies under measured weekday demand with currently configured vehicles, subject to a ±15% travel-time sensitivity range; it is not suitable to certify emergency evacuation reliability." That verdict tells users exactly what they may do with the result and what evidence would be required to broaden the claim. It also provides a testable change-control criterion when the use case changes.

## Problems — attempt first

1. Give an example of a simulator that passes code tests but is invalid for emergency dispatch decisions.
2. Explain why matching historical data after calibration is not sufficient validation.
3. For \(y=2a+b\) with independent parameter SDs 0.1 and 0.3, calculate first-order output SD.
4. What evidence links must be retained to reproduce a simulation-based design decision after a software revision?

<details><summary>Worked answers and engineering interpretation</summary>

1. A flawless queueing algorithm that ignores road closures and communications loss may be correct code yet unrepresentative of disaster operations.
2. Calibration can fit noise or compensate for omitted mechanisms; held-out conditions and independent referents help assess transfer to the intended use.
3. \(\mathrm{Var}(y)=4(0.1^2)+0.3^2=0.13\), so \(SD(y)=\sqrt{0.13}\approx0.361\), under independence and local linearity.
4. Requirement revision, model/code revision, input dataset and units, seed/configuration, environment/dependency versions, run records, results, review findings and decision rationale.
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/08-credibility.html) · [Download editable Markdown lab](../labs/08-credibility.md) · [Open the associated notebook](../notebooks/08-credibility.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)

<!-- STEP04-QUANTITATIVE-START -->
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
<!-- STEP04-QUANTITATIVE-END -->
