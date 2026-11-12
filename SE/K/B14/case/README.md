# NS-DA14.1 — Campus Mobility Selection and Scalable Service Decision Laboratory

**Course:** EN.645.784 · **Book 14** · **Status:** controlled instructional model, **HOLD** for real selection/qualification. This *synthetic* model is a worked decision-science example, **not** campus data, a validated service forecast, a calibrated fleet simulation, or independent accessibility/safety evidence.

## Scope and source boundaries

The course's six 18-month pilot packages A–F and their seven numeric measures are transcribed **unchanged** from Section 7 of the EN.645.784 course guide. Their five-year costs do **not** establish the separate pilot-authorization budget. All added screening limits, scaling anchors, weights, conditional payoffs, probabilities, diagnostic likelihoods, parametric design equations, and environmental stresses are **invented for instructional transparency**. The six-alternative pilot selection and the scalable-service design are separate decisions. The original Book 11 event-queue analysis, Book 12 physical simulation, and Book 13 feedback model are not substitutes for validation of this decision model.

## Editable, reproducible evidence

- [Controlled decision JSON](decision-inputs.json) — pilot measurements, declared thresholds, value preferences, design factors, and Bayesian teaching beliefs
- [Standard-library Python analyzer](../tools/step03_book14_decision.py) — input validation, hard screening, additive value, dominance/Pareto enumeration, DOE, least-squares surrogate, and Bayesian EVPI/EVSI
- [Pilot screening and value scores](pilot-screening.csv) — all six original alternatives retained with rejection reasons and conditional preference result
- [All 1,440 design candidates](design-candidates.csv) — including infeasible configurations and reasons
- [Five sampled nondominated designs](efficient-designs.csv) — finite subset, not a global or physical frontier
- [Eight-run factorial experiment](factorial-doe.csv) — intentionally deterministic model; no statistical replication or Monte Carlo intervals
- [Independent surrogate holdout rows](surrogate-holdout.csv) — 36 training and 16 held-out in-domain synthetic points
- [Computed summary including EVPI and EVSI](summary.json) — numerical cross-check
- [Editable architecture morphology](morphology.csv) — complete course option classes versus the smaller sampled computational subset
- [Decision evidence and credibility register](evidence-register.csv) — evidence owner, assumption status, open review gate
- [Selection/design evidence chain diagram](decision-evidence.svg) — editable vector artifact

Reproduce the derived records using Python's standard library, from repository root:

```bash
python3 SE/K/B14/tools/step03_book14_decision.py --write
python3 scripts/check_step03_book14.py
```

The script is deterministic. `--write` regenerates the five CSV outputs and `summary.json` from the controlled JSON. Do not modify the original course guide's pilot values to force a preferred answer.

## Stage 1 — Pilot selection and preference reversal

For demonstration, require five-year cost ≤$10.4M, deployment ≤12 months, accessible-trip coverage ≥0.95, availability ≥0.95, and integration-risk category ≤3. These are **illustrative policy gates, not verified campus requirements**. Only **C and D** pass. C has lower cost, higher modeled access coverage and faster deployment; D has lower modeled wait, higher availability and lower annual emissions. Neither dominates the other.

With the declared six-attribute value anchors and weights, the conditional values are **C = 0.708571** and **D = 0.724524**. Shift approximately **0.07251** weight from waiting-time value to accessible coverage and the preference ties; a larger shift favors C. The difference is preference-sensitive and cannot be interpreted as observed service superiority. The positive-test Bayesian exercise has **EVPI = 3.00** and **EVSI = 1.77** synthetic utility points; after 0.50 point of test burden, net value is **1.27**. These points cannot be treated as dollars without separate valuation.

## Stage 2 — Bounded scalable-service search

The actual course morphology is larger than the evaluated computational subset. NS-DA14.1 enumerates **1,440** tuples over two architectures, five fleet counts, three charger counts, three reserve values, two dispatch policies, two automation types, two zone counts and two speed settings. The synthetic response equations produce **10 nominally feasible** candidates and **five nondominated** candidates across cost, wait, emissions and accessible-coverage gap. Exhaustive enumeration establishes the finite-grid result only. The distinct course-final example of a 14-vehicle/6-charger, 15% reserve pilot is retained in the original guide and not overwritten; the model here does not validate or refute it.

A nondominated teaching candidate with hybrid service, 18 vehicles, 8 chargers, 10% reserve, priority dispatch, human operation, four zones, and 18 mph gives synthetic cost **$13.156M**, wait **14.0136 minutes**, coverage **0.998**, availability **0.9544**, emissions **126.6 tCO2e/year**. Under `high_demand` it fails the wait gate (**17.736 minutes**). Under `charger_loss` it fails wait (**15.9576 minutes**) and availability (**0.9424**). **HOLD** rather than procurement approval.

## Verification boundaries and critical open issues

The model checks formal input ranges, screening, output and Pareto calculations, DOE reconstruction, surrogate holdouts, positive/negative Bayesian branches, tests for invalid inputs, and publication consistency. **No real passenger datasets, cost estimates, autonomy hazard controls, field validation, accessibility co-design, external legal review, supplier commitments, or procurement approval were performed.** The deterministic surrogates can reproduce the invented response function but cannot certify real service behavior. A decision authority must separately approve thresholds, measure definitions, preferences and governance and must obtain independent model validation and safety/accessibility review before action.
