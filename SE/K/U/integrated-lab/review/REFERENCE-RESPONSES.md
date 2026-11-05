# Reference responses — review after completing exercises

These are **illustrative solution arguments**, not a unique answer key. Engineering alternatives may be stronger if their assumptions are explicit and evidence is reproducible.

## L01 — Context

An adequate boundary statement says the SOI *models scheduling on synthetic inputs* and excludes real dispatch; a sketch shows passenger representatives and dispatch operators outside the software. Proposed real validation measures could include actual missed pickups, accessible boarding completion and user-reported service usability, all requiring separate ethical and operational study.

## L02 — Requirements

A credible `REQ-09` might specify a future assisted-boarding workflow with accessible user testing, dispatch escalation and documented response criteria. No present code supports it. Tightening the p90 fixture threshold to 15 minutes changes the reference verdict to fail because the measured nearest-rank p90 remains 20 minutes.

## L03 — Architecture

`Request` parsing requires nonnegative finite time, one passenger and distinct stops. Deduplication preserves only equal repeats; conflicting reuse raises error. Scheduler uses each vehicle's next-free time; the non-overlap invariant is guaranteed only for the single-threaded simulated schedule. Supporting a group booking requires more than changing one parser condition.

## L04 — Trade study

One vehicle fails the fixed completion requirement (6/12); two vehicles pass it (12/12, p90=20). A 3-vehicle option should be compared on cost and performance, not assumed optimal; all costs are invented. Under a hard completion criterion, option A is infeasible even if inexpensive.

## L05 — Software

Test examples should include duplicate and conflicting event IDs, positive vehicle count, zero or nonfinite arrival time, end-horizon edge, and overlapping assignment detection. An in-memory digest is not a signed audit log or cyber assurance mechanism.

## L06 — Simulation

The teaching runner uses `seed=20261101`, 200 replications and exponential gaps of mean 4 minutes. Its exact output is stored in `outputs/results.json` and must be recomputed. The confidence band is **Monte Carlo uncertainty of the simulated replication mean**, not real-world reliability or model bias. Reducing this interval with more replications does not validate the data-generating mechanism.

## L07 — Evidence

A test of a deliberately degraded system can pass when it *correctly detects* a requirements failure. A requirement-to-test link is insufficient to claim verification; one must see valid configuration-specific results and a suitable method.

## L08 — Safety / human factors

Possible unsafe controls: issuing an assignment to an unavailable vehicle, leaving an unserved rider without escalation, or ignoring an accessibility requirement. A suitable preliminary investigation includes stakeholders, operators and safety specialists and cannot be replaced by unit tests.

## L09 — Change

Allowing two passengers changes parsing, scheduling occupancy, likely service duration, interface schemas, tests and hazards. Changing only `REQ-07` or one line of code leaves the rest of the assurance chain stale. A hash captures file changes but does not authenticate author or test environment.

## L10 — Review

A defensible conclusion is **research-only continuation**. The fixed fixture's passing results cannot support a real deployment decision in light of synthetic demand, missing physical operation, absent human/accessibility evidence, security gaps and unvalidated recovery behavior.
