# An end-to-end analysis: evidence to conditional choice

**Cross-course pathway:** All six Phase 3 courses. Use as a capstone orientation.

## Build the decision chain rather than six unrelated reports

Consider a fictional shuttle service facing a choice between two dispatch policies and fleet sizes 2–4. The MBSE course specifies needs, operational scenarios, functions, interfaces and parameter constraints. Metrics analysis defines the measured wait-time distribution, demand uncertainty, reliability and suitable test design. Foundations of Simulation builds an event calendar with correct resource contention. Advanced Simulation adds battery energy, temperature and time synchronization where these mechanisms materially affect the decision. Systems Dynamics asks how demand, service reputation, maintenance backlog and investment respond over months. Decision Science compares feasible alternatives and evaluates the value of an additional pilot.

A coherent artifact chain might be:

`NEED-SVC-01 → REQ-WAIT-01 → SCN-PEAK-RAIN → MODEL-DES-v2 + MODEL-THERM-v1 → DATA-WAIT-2026 → MEAS-P95 → DEC-FLEET-03`.

Every arrow needs ownership and a tested interpretation. In particular, simulated 95th-percentile wait is not measured qualification evidence.

## A deliberately adversarial review

A simulation yields estimated p95 wait of 11.4 min, apparently within a 12-min requirement. But the demand model omits a peak scenario, correlated rain increases boarding delay, and a charging change is not reflected in the model configuration. The data did not include accessibility trips. The correct engineering response is not “pass.” Narrow the claim, repair missing assumptions, design a discriminating test and record a conditional decision.

## Capstone minimum data package

Preserve scenario manifest, input datasets (synthetic clearly labeled), model and solver versions, seeds, design matrix, results, sensitivity and uncertainty, experiment plans, visualizations, source code, tests, decision thresholds, reviewer notes, and a list of prohibited interpretations. A second student should be able to rerun one pivotal result without guessing hidden settings.

**Cross-course challenge:** Identify one original course deliverable from each of the six courses that contributes evidence to this chain. Then explain which evidence must come from real-world tests rather than simulation.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
