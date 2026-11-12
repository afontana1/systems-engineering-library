# NS-MS11.1 — Campus mobility fleet decision and simulation credibility dossier

*EN.645.757 · Book 11 · fictional Northstar teaching baseline · initial coordinated Step 03 edition*

## Decision and status

The decision owner is considering a **Phase 2 campus mobility pilot**. The original course guide defines 06:00–18:00 demand, four initial fleet candidates, accessible service, charging, and performance criteria. Our case extends those *course-specified synthetic inputs* with explicit, deliberately simplified hypotheses. No real campus measurements have been used. The case supports **early option screening only**.

**Decision: HOLD** on operational pilot readiness under the present model: none of the tested fleets (8, 10, 12 or 14) meets *all* three modeled targets—standard-trip daily p90 ≤12 minutes, accessible-trip daily p90 ≤15 minutes, and fraction awaiting pickup at 18:00 strictly below 1%. The model omits ride pooling, staffing, physical route/charger locations and field validation. A model failure here **does not prove that a real fleet would fail**. It indicates that the existing simplifications and candidate space cannot support an approval claim.

## Controlled evidence chain

[Editable process diagram](simulation-evidence-chain.svg) · [Assumptions and units](model-assumptions.json) · [Requirement trace](requirements.csv) · [Credibility and gap register](credibility-register.csv) · [Replication-level measurements](replication-output.csv) · [Machine-readable summary](summary.json) · [Standard-library executable source](../tools/step03_book11_mobility.py).

The chapter sequence uses one problem at different levels: purpose, conceptual process, input distributions, baseline, discrete-event implementation, verification, alternatives, replication inference, designed experiments, integration/T&E, VV&A and sustainment. The original twelve labs remain authoritative course preparation; the new materials supplement rather than overwrite them.

## Repeatable analysis: interpretation

Run from repository root:

```sh
python SE/K/B11/tools/step03_book11_mobility.py
python scripts/check_step03_book11.py
```

The first command uses Python's standard library only, regenerating both CSV and JSON. Seed sets 1000–1029 create independent synthetic days; identical exogenous requests are replayed across fleets within a given day. A daily standard p90 is calculated from standard-trip waits by the nearest-rank rule. The uncertainty interval estimates the **mean of daily p90 statistics**, not a pooled-request percentile, actual operational p90, or validation accuracy. All waits include late pickup if a request remains queued at close, while *not picked up by close* is a separate 18:00 snapshot. After-close events are processed to avoid dropping waits. A trip is assumed to occupy one vehicle exclusively, regardless of its physical passenger capacity.

| Fleet | Baseline standard daily-p90 mean | Baseline accessible daily-p90 mean | Mean fraction awaiting pickup at close |
|---:|---:|---:|---:|
| 8 | about 349.1 min | about 362.5 min | about 36.0% |
| 10 | about 161.9 min | about 168.4 min | about 21.5% |
| 12 | about 69.1 min | about 80.2 min | about 10.3% |
| 14 | about 36.4 min | about 45.4 min | about 6.0% |

Values above come from the model as shipped; `summary.json` is the exact machine-readable source. They describe simulated service under intentionally restrictive **single-request** vehicle service, not a realistic optimized route or pooled-shuttle design. Stress experiments increase arrival rates by 20% and travel times by 30% simultaneously; there is no estimated real-world stress probability.

## Model boundary and evidence priorities

- **Specified, tested in software:** event times, charger capacity and queue progression, seed control, input validation and structural publishing checks. Internal correctness evidence is narrower than operational validation.
- **Assumed:** Poisson demand, lognormal accessible boarding, triangular service/charge, nominal accessible-fleet fraction and battery depletion; all need independent data and plausible limits.
- **Not represented:** multi-party ride pooling, actual eight-passenger/two-device occupancy, route travel network, people and driver shifts, breakdowns, physical charger access, wheelchair-equipment fitting, weather distributions and regulatory compliance.
- **Needed before a real pilot decision:** independent observed demand/tail distributions, reproducible model-to-referent validation under representative conditions, alternatives with realistic staffing/dispatch/pooling, physical integrated tests, accessibility stakeholder review, and approval by the appropriate decision authority.

The software verifies numerical operations and publishing alignment, not NASA/DoD standards conformance. No accreditation has been requested or granted. The 12-week outcome crosswalk is stored at `audit/book11-weekly-outcomes-step03.csv` in the complete authoring repository (not in the published `SE/` tree).
