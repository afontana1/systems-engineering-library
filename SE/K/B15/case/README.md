# NS-ASE15.1 — Northstar Agile Systems Engineering operating-model laboratory

**Status:** controlled synthetic educational case. **Decision:** GO only for a bounded, independently reviewed measurement-and-integration experiment; HOLD any inference of operational release suitability, safety acceptance, or enterprise-wide benefit.

[Book 15 reader](../OPEN-BOOK.html) · [Course guide](../../../C/P4/EN645780.html) · [Source chapters](../README.html)

## Intended use and relationship to previous books

This is a synthetic transformation experiment for Northstar Mobility Systems' campus mobility program. It continues the fictional evidence-centered Northstar cases in Books 7–14 but does **not** assume that Book 11's operational fleet or Book 12's physical vehicle have been qualified. It is deliberately a model of **engineering work and evidence flow**, not a dynamic model of real vehicle behavior or stakeholder benefits.

The authoritative model inputs are [controlled-inputs.json](controlled-inputs.json); the [standard-library Python implementation](../tools/step03_book15_flow.py) uses finite daily stage capacities, fixed service durations, a reproducible arrival sequence, a deterministic supplier-delay rule and a deterministic rework rule. No empirical arrival distribution, cost estimate, human behavior model or physical assurance claim has been validated. A green simulated release means that **the model's limited Boolean predicate** was satisfied, not that a deployment is authorized.

## Reproducibility and outputs

Run from the repository root:

```sh
python3 SE/K/B15/tools/step03_book15_flow.py
python3 scripts/check_step03_book15.py
```

The first command recreates all machine-generated outputs (no external Python libraries):

- [Scenario summary](scenario-summary.csv) — 100-business-day counts, observed lead times, critical backlog and screening status.
- [Daily flow](daily-flow.csv) — arrivals, completed items, admitted WIP, waiting backlog, rework counts, with conservation of changes at every day.
- [Per-change evidence ledger](item-evidence.csv) — 48 items × four scenarios, with configuration, class, gate and release information.
- [Result manifest](model-results.json) — structured summary and conditional probability diagnostic.
- [Engineering decisions](decision-log.csv) — human-authored interpretations and outstanding evidence.
- [Evidence register](evidence-register.csv) — scope, provenance, assumptions, missing independent proof, credibility.

## Controlled flow model

| Parameter | Synthetic rule |
|---|---|
| Demand | 48 changes arriving over synthetic days 0–43, with specified burst duplicates |
| Horizon | 100 business days; unreleased changes are **censored**, not counted as completed |
| Stages | Engineering → independent review → integration → assurance → release |
| Nominal service days | 2, 2, 3, 2, 1; day-end completion is available to the next stage the following day |
| Critical changes | Every seventh sequence ID, solely for repeatable case construction |
| Supplier dependency | Every fifth sequence ID incurs scenario-specific extra integration delay |
| Rework | Every ninth change in baseline/flow-only or every sixteenth change in assured/stress re-enters review once, invalidating previous review/integration/assurance gates |
| WIP | Cap applies to **admitted** changes; unadmitted demand remains visible in the backlog |
| Release | All applicable review, integration, assurance, safety, security and version-key checks must pass |

## Output and interpretation

| Scenario | Releases / 48 | Mean total lead days among releases | Nearest-rank p90 days | Unreleased critical items | Educational screening |
|---|---:|---:|---:|---:|---|
| Status quo | 21 | 44.76 | 76 | 3 | Fails |
| Flow only | 42 | 36.57 | 58 | 0 | Fails mean-latency screen |
| Assured learning | 47 | 31.87 | 50 | 0 | Passes synthetic screen |
| Supplier disruption | 31 | 39.06 | 67 | 2 | Fails |

The "passes" entry refers **only** to the provided hypothetical rule of at least 75% accepted releases within the fixed horizon, mean total lead no more than 35 business days *among observed releases*, and zero unresolved critical items. This rule is **not** a satisfactory operational safety or quality criterion. Mean lead times among released items are affected by right censoring; they are not the mean for all demands and should not be compared causally without a suitable event-history analysis and consistent cohort definitions. Multiple model parameters change at once, so the scenario comparison is not a controlled estimate of one intervention's effect.

**Model limitations:** deterministic arrivals and service times, no vacations or outages except simplified supplier delay, no true time-varying risk, no resource skill network, no defect severity distribution, no real safety testing, no calibrated failure probabilities, no repair/rollout operations and no validated demand-value connection. A second independent implementation and real operational observations would be required before any forecast. The economics example in Chapter 12 intentionally uses a *separate, same-window* 10-week hypothetical count; do not use the 100-day simulation count with the 10-week budget.

## Connection to Book 15's twelve-week outcomes

1. Specify change-response time with a configuration-bound evidence endpoint.
2. Tailor low-consequence, reversible changes separately from safety-critical/physical paths.
3. Measure total and admitted lead time, backlog, throughput, WIP and horizon censoring.
4. Allocate decisions to teams, interface authorities and independent safety reviewers.
5. Plan a learning interval with a falsifiable gate and diagnostic belief update.
6. Construct stakeholder value models without trading away hard assurance constraints.
7. Compare interface/adapter change costs and option value.
8. Query configuration-specific evidence and fail closed on stale results.
9. Carry quality, cybersecurity and safety evidence into every increment.
10. Rehearse an invalidated integration result and qualified recovery.
11. Analyze supplier dependencies and system-level critical paths.
12. Defend the CEO investment proposal, unknowns, comparison design and stop conditions.

These additions supplement rather than replace the [original EN.645.780 course outcomes](../../../C/P4/EN645780.html), assessment criteria, existing chapters and labs. They are part of a coordinated first-pass textbook expansion, not a substitute for independent peer review.
