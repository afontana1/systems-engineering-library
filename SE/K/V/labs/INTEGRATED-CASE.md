# Integrated laboratory — NS-CE4.1: connected engineering evidence

This laboratory links all six chapters to the same **synthetic**, unqualified Northstar emergency-dispatch evidence chain. It is designed for individual reproduction, peer challenge, and a reasoned release recommendation. The existing six labs and notebooks remain independently available.

## Learning objectives and source of truth

1. Distinguish hard constraints from preference, uncertainty, and approval.
2. Detect a contract revision mismatch, stream gap, repeated event, and stale timestamp.
3. Preserve the all-request and accessible-request denominators during acceptance analysis.
4. State why M/M/1 requires $\lambda<\mu$ and what a paired $t$ interval assumes.
5. Distinguish structurally linked claims from actionable, current, in-scope evidence.
6. Calculate a difference-in-differences comparison without asserting unverified causal identification.

Controlled assumptions: [editable JSON](../data/ns-evidence4-case.json). Reproduction: [standard-library Python model](../code/ns_evidence_case.py), [computed output](../outputs/ns-evidence4-results.json), [unit tests](../code/test_ns_evidence_case.py). The digest in the output binds it to the case JSON bytes; it is not a certified digital signature.

## Reproduction workflow

At the repository root, run:

```bash
python3 SE/K/V/code/ns_evidence_case.py
python3 -m unittest discover -s SE/K/V/code -p 'test_*.py'
python3 scripts/check_step04_connected_evidence.py
```

Record the case revision and SHA-256 input digest in your report. Copy the JSON to a temporary directory for perturbations; do **not** silently overwrite the controlled results. Recompute all derived tables rather than hand-editing numerical outputs.

## Six evidence stations

| Station | Reproduce | Adversarial variation | Required interpretation |
|---|---|---|---|
| Concept | Three nominal/storm screens; resilient passes | Raise resilient storm p90 to 16.1 min | Small margin defeats the modeled pass |
| Interface | Four violations in four-message trace | Repair stream order but leave revision 2.0 | Correct sequencing is not current contract evidence |
| Acceptance | 65/80 total timely; 10/16 accessible | Change two accessible late to timely | 12/16 = 75%, still fails 90% |
| Simulation | 30 min stationary total time; paired interval | Set nominal $\lambda\geq\mu$ | No finite stationary mean; reject formula |
| Provenance | 5 structural / 1 actionable paths | Alter evidence payload only | Digest mismatch reveals change, not authorship |
| Enterprise | -4 min illustrative DiD, -5 accessible DiD | Change comparison post from 18 to 16 | Estimate becomes -2; identification still absent |

## Assurance review and independent challenge

Draw a directed graph from each claim to its requirement, evidence artifact, revision, result, tested scenario, and decision owner. List all known defeaters. Demonstrate that the five paths exist even when four cannot support the current claim. Evaluate the evidence sources' dependence; avoid counting two reports derived from one simulation as independent corroboration.

A valid engineering disposition must explicitly address **all** of these gates: service capacity and wait constraints; accessible timely-service fraction; interface conformance; sample and model credibility; current artifact provenance; stakeholder and organizational approvals; and possible group or time-selection bias. No combination of local PASS flags can grant the missing approvals. Discuss how a real trial could measure the required quantities without exposing participants to inadequately governed risk.

## Suggested review submission and scoring rubric

Submit: (a) an exact copy of the input JSON and its digest, (b) regenerated result JSON, (c) six short numerical derivations, (d) at least four deliberate failures with observed diagnostics, (e) a five-path traceability table, and (f) a signed-by-author *proposal* for a limited evidence-acquisition plan, not an authorization.

| Dimension | Points | Minimum expectation |
|---|---:|---|
| Numerical and formal reasoning | 25 | Correct quantities, units, boundaries and paired comparison |
| Adversarial tests and reproducibility | 25 | Demonstrates rejection of invalid model states |
| Source-to-claim and configuration trace | 20 | Clear versions, digests, scopes and independent review needs |
| Critical interpretation | 20 | Non-independence, model form, unidentified causal assumptions |
| Writing and ethics | 10 | Separate evidence from authority and protect affected groups |

**Disqualifying shortcut:** claiming the synthetic model qualifies an operational system, declaring approval from a single favorable design screen, or discarding unserved requests. Release of this instructional project is not release of the modeled dispatch system.
