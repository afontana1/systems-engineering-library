# Integrated quantitative laboratory — NS-QSE4.1

**Collection:** Quantitative Systems Engineering, Chapters 1–8. **Input status:** synthetic classroom data only. **Intended use:** reproducible engineering-method demonstration; not qualified dispatch, safety, or vehicle control.

## Research question and predeclared evidence boundary

Can a coordinated improvement in parallel dispatch capacity and fixed service time reduce simulated queue delay without concealing performance in compound disrupted conditions? How much uncertainty comes from the demand regime, the finite paired sample, the numerical solver, and the inadequacy of model assumptions? Which further evidence is required before approving any intervention?

The source of record is [`../data/ns-qse4-case.json`](../data/ns-qse4-case.json). This file declares observation units, all 24 synthetic count observations, Gamma-prior parameters, service design, compound stress multipliers, price/value assumptions, thermal parameters, scenario weights, synthetic discrepancy data, and explicit (false) approval gates. Its SHA-256 is embedded in generated results; edits must trigger fresh results.

## Reproduce the controlled calculation

From the **repository root** with Python 3.10+:

```bash
python3 SE/K/Q/code/ns_qse_case.py
python3 -m unittest discover -s SE/K/Q/code -p 'test_*.py'
python3 scripts/check_step04_quantitative.py
```

Generated results are [`../outputs/ns-qse4-results.json`](../outputs/ns-qse4-results.json) and [`../outputs/ns-qse4-policy-days.csv`](../outputs/ns-qse4-policy-days.csv). The run uses Python's standard library and fixed seeds; generated output depends on the Python pseudorandom algorithm as implemented in that interpreter. Use the same interpreter version for byte-for-byte reproduction, or use numerical tolerances for independent implementations.

## Eight-workstream traceability crosswalk

| Chapter | Engineering deliverable | Expected numerical or diagnostic result | Primary weakness to challenge |
|---|---|---|---|
| 01 — probability | Regime-conditioned rate model and mixture moments | 10.000 and 17.869 requests/hour; mixture variance 29.414 | Unmeasured regime dependence and missing counts |
| 02 — estimation | Gamma posterior and day-paired bootstrap | Baseline minus combined 14.533 min, interval ~[10.86, 18.01] | Synthetic replications are not field samples |
| 03 — experiments | Two-factor blocked factorial contrasts | Capacity effect −9.598 min; interaction contrast +3.826 min | Model-only causality, scale dependence |
| 04 — discrete events | Event-calendar trace and conservation | Compound combined timely 82.95%, overtime 26.89% | No route, priority, staffing or carry-over queue |
| 05 — continuous model | Thermal balance and solver comparison | Exact 37.6444°C at 2 h; Euler h=1 gives 38.56°C | Thermal parameters not calibrated |
| 06 — feedback | Sampled recursion stability condition | Multiplier 0.5 at h=0.25 h, −1 at h=1 h | No real actuator or delay validation |
| 07 — decisions | Weighted disutility and hard screen | Combined cost-plus-wait ~ $552.68; all policies fail compound screen | Value weights and costs are hypothetical |
| 08 — credibility | Provenance and adverse approval screen | Synthetic discrepancy RMSE ~1.904 min; permission gates false | No independent real-world validation |

## Challenge experiments

1. **Demand stress:** In a *copy* of the JSON, increase every storm count by 30%. Recompute the posterior rate, the policy comparison, and the hard feasibility check. Identify which differences follow from changing the demand generator and which reflect a changed value judgment.
2. **Preference reversal:** Increase the cost of the combined policy to $1,000 per window and recompute the minimum illustrative disutility. Even if the preferred numeric alternative changes, the compound service screen still applies.
3. **Incorrect assumptions:** Request a queue with zero servers, negative service time, unsorted arrivals, a nonfinite arrival, invalid Gamma prior, and scenario weights that do not sum to one. The model must reject these instead of generating plausible-looking outputs.
4. **Numerical instability:** Derive the discrete multiplier for Euler feedback at a step size above the stability boundary. Compare the numerical linear recursion with the stable continuous plant. Do not substitute an unstable Euler result for measured physical instability.
5. **Governance failure:** Set numeric targets to a trivially easy value, leaving permission gates false. The operational disposition must remain **HOLD**. Approval cannot be inferred from a successful optimization.

## Acceptance and independent review

The exercise passes computational verification when the generated results agree with declared inputs and reference checks, all requests are conserved in the queue, and invalid datasets raise a clear error. It does **not** pass field validation, independent safety assurance, equitable-access review, or operator authorization. Reviewers should inspect the source, rerun the model, register discrepancies with units and tolerances, assess the independence assumptions, and request real dispatch, weather and accessible-service traces before operational interpretation.

**Required learner submission:** a revised configuration JSON, a diff against the baseline, generated outputs, two manually verified equations, one deliberately failing test, a one-page limitations/evidence register, and a decision labeled **HOLD / conditional instructional use** unless independently substantiated permissions and validation are supplied.

[Return to the Quantitative collection](../INDEX.html)
