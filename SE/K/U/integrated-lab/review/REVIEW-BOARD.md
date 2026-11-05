# Northstar · Integrated preliminary review board

## Decision to make

**Question:** Is this *synthetic software model* ready for further controlled research? **Not:** Is a real regional transportation service safe to operate? The latter cannot be supported by these artifacts.

**Recommended reference disposition:** continue sandbox research; do **not** authorize operational dispatch, real passenger scheduling, vehicle control, or safety-critical use.

## Evidence ledger for the review

| Claim / concern | Evidence available | Strongest warranted interpretation | Known limitation |
|---|---|---|---|
| Exact duplicate handling | `tests/test_lab.py`; `outputs/results.json` | Exact repeated request payload processed once within one run | No durable storage, concurrency, authentication or network failures |
| Non-overlap invariant | `src/northstar.py`; tests; assignment CSV | No overlapping scheduled intervals in reference toy allocator | Fixed trip time; not physical fleet safety |
| Fixture service target | 12/12 completions; 20-minute p90 | Passes chosen narrow fixture thresholds | Input demand intentionally invented |
| Vehicle loss | One-vehicle variant serves 6/12 | Critical model sensitivity to resource degradation | Not a failure probability or outage frequency |
| Stochastic arrivals | 200 seeded synthetic replications | Performance changes under assumed arrival law | No field validation of distribution or process |
| Trace completeness | `src/assurance.py`; matrices | Required IDs link without dangling references | Links do not prove evidence sufficiency |
| Hazard treatment | `data/hazards.csv`; human-factors lesson | Preliminary identification of selected model hazards | Critical real operational hazards uncontrolled |
| Reproducibility | `outputs/input-hashes.json`; committed sources | Inputs can be tracked and runs repeated | Hashes not externally authenticated |

## Questions the board should challenge

1. Are service targets connected to actual user outcomes or just fixture convenience?
2. Why should twelve artificial requests stand for a regional mobility service?
3. What is the policy if a request is unserved, a rider requires assistance, or communications fail?
4. Is an exact duplicate replay the same problem as concurrent writes or a malicious replay? Why not?
5. Which requirements are linked to **passing evidence** and which only have a test reference?
6. What are the uncertainties behind the stochastic model and its confidence interval?
7. Which changed inputs would make the earlier results stale?
8. What real-world evidence and independent authority are required before any pilot?

## Required board package

- Boundaries, stakeholder needs, concept of operations, and explicitly excluded real systems.
- Baseline requirements, design and interface rationale, alternative evaluation.
- Source and tests, input hashes, result summaries and one deliberate negative test.
- Experiment plan, sensitivity results, model-credibility claims and limitations.
- Hazard register, open findings and action owners, including accessibility and information security.
- Change-impact matrix and configuration state.
- **Decision statement** with scope, evidence, residual uncertainty, conditions and next review trigger.

## Reference decision wording

> The software-only Northstar teaching prototype exhibits the specified deterministic scheduling and structural traceability behaviors for a synthetic reference fixture. A deliberate degradation test and invented stochastic-arrival sensitivity analysis show the service results are conditional. The package does not justify any operational transport, accessibility, cybersecurity, or safety assertion. The review accepts continued research within a controlled sandbox only, with unresolved findings and validation work assigned before reconsideration.
