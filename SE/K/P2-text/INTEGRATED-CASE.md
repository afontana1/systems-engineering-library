# The campus-shuttle case: a controlled chain from mission concept to evidence

> Every system, person, datum and result in this document is fictional. It is a teaching exercise about systems engineering, not a real transit deployment, physical safety case or authorization to operate autonomous vehicles.

## Background and engineering boundaries

A university wants accessible, predictable rides across a large campus. The program may use staffed vehicles and a software dispatch platform. Safety-critical driving and braking are outside the demonstrator software's authority and require independent physical-system engineering and professional assurance. The campus has existing transport arrangements, unknown peak demand and a tentative acquisition budget.

The program's first challenge is not to choose a vehicle. It is to define the mission and collect defensible evidence for what current users experience. The original study guides demand progressively stronger packages; this companion case illustrates how the same IDs flow across courses.

## Stage A — concept-development baseline (`CON-04`)

| ID | Claim or artifact | Status | Important limit |
|---|---|---|---|
| `NEED-04` | Riders need actionable availability information | Stakeholder need | Not yet a testable response-time requirement |
| `SC-05` | Accessible request during service window | Operational scenario | Must include unavailable and offline branches |
| `MOE-02` | Eligible requests fulfilled to agreed time | Mission effectiveness | Requires denominator and time window |
| `REQ-14/C` | Issue status event within 900 ms for p99 under `WL-01` | Hypothetical approved requirement | Applies only to defined dispatch mode/workload |
| `ASM-22` | Average accessible boarding below 90 s | Provisional assumption | Needs representative observation |
| `CON-04` | Select demand-responsive concept | Concept decision | Limited by current staffing and curb evidence |

Capacity illustration: two vehicles × 480 minutes × 0.85 availability ÷ 24-minute cycle = 34 nominal cycles. With three boardings/cycle this suggests 102 boardings/day, not a distribution, lower service guarantee or accessibility proof.

Concept alternatives must be filtered against hard constraints before weighted preference evaluation. A recommendation includes an approved trade model, sensitivity bands, cost/schedule range and explicit conditions to continue design.

## Stage B — design and integration baseline (`DES-1.3`)

| ID | Design element | Testability requirement |
|---|---|---|
| `F-01` | Receive eligible rider request | Trace timestamp at boundary |
| `IF-03/B` | Dispatch event contract | Schema and revision, origin clock, replay/timeout behavior |
| `BUD-08` | Serial timing allocation totaling 650 ms nominal | Validate stage estimates and system p99 separately |
| `ADR-11` | Asynchronous event delivery | Document resilience and consistency tradeoffs |
| `INT-06` | Stepwise integration from stubs to closed lab | Preserve rollback and configuration |
| `HZ-08` | Stale availability can cause incorrect assignment | Mitigate with freshness, revision, human handling |

The gateway's 80 ms, queue's 150 ms, decision's 120 ms, storage's 100 ms and network's 200 ms sum to 650 ms. The 250 ms nominal margin to the 900 ms requirement is not an observed statistical percentile.

Components carry derived constraints and their interface owners. The integration plan tests duplicate/reordered events, network partition, crash/restart and escalation. Every test run records a manifest of versions and environmental assumptions. No dispatch-only lab result demonstrates braking safety.

## Stage C — test and evidence baseline (`EVD-02`)

| ID | Evidence claim | Work product | Status in this fictional scenario |
|---|---|---|---|
| `VT-14` | Verify `REQ-14/C` in `WL-01` | Approved timing plan, instrument review, raw logs | Planned / not field-proven |
| `TST-27` | No duplicate active assignment after replay | Scripted integration fault test | Laboratory-only example |
| `VAL-06` | Rider understands service status | Moderated representative scenario | Partial stakeholder coverage |
| `RUN-38` | One controlled execution on `D-21` | Logs and manifest | Illustrative, not independent actual test |
| `ACT-09` | Improve partition handling | Rework with explicit retest | Open |

The T&E evidence argument distinguishes *test planned*, *test executed*, *criterion met*, and *outcome validated*. In a toy statistical calculation, no failures in 100 independent representative Bernoulli trials provides a one-sided 95% upper failure-probability bound of about 2.95%, not evidence of 0% risk. Those trial assumptions must themselves be supported.

## Change-impact walk-through

At a later concept review, a stakeholder asks for response time reduced from 900 ms to 600 ms:

1. Reassess mission relevance and obtain approval of the revised threshold.
2. Change `REQ-14/C` to a new controlled revision, retaining the older version.
3. Recalculate `BUD-08`: 650 ms nominal already exceeds 600 ms before variance. Investigate alternative allocations or architecture changes.
4. Revisit `IF-03/B`, `ADR-11`, test instrumentation and workload definitions.
5. Update the qualification criterion and decide whether previous evidence remains relevant to any limited claim.
6. Reassess design, cost/schedule and operational effects; record decision authority.

## Three capstone challenges

**Challenge 1 — concept selection:** Build a three-concept morphological matrix, feasibility gates and a weighted value model. Show a weight shift that changes the winner and propose an experiment that could resolve the most decision-sensitive uncertainty.

**Challenge 2 — integration:** Draw the component dependency sequence and define six laboratory integration increments with fault injection, rollback and traceable versions. Explicitly declare unrepresented physical safety mechanisms.

**Challenge 3 — evidence:** Write the strongest defensible final disposition if the dispatch software passes laboratory tests but has never undergone representative campus network-partition testing or inclusive usability validation. Do not state field- or autonomous-operation approval. Provide conditions and authorities for any future evaluation.

## Where to continue

- [Cross-course pathways](KNOWLEDGE-THREADS.md)
- [The 36 weekly lessons](README.md)
- [Editable worksheets](templates/)
- [Standard-library calculation labs](tools/README.md)
- [Original three-course Phase 2 guide](../../C/P2/OVERVIEW.md)
