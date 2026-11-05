# The Autonomous Campus Shuttle: a three-model teaching case

> Entirely fictional teaching data. This is not a real vehicle design, safety assessment or deployment authorization.

## Problem and boundary

A university wants a pilot shuttle service with accessibility-aware dispatch and intelligible rider updates. Vehicle motion safety resides in a separate onboard controller under independent operational authority. The dispatch platform may request routes and observe acknowledgements, but **cannot attest to physical stopping** without further hardware evidence. This boundary underpins all three courses.

## Layer 1 — MBSE operational chain

1. Stakeholder need `N-01`: riders can plan and understand pickup status.
2. Operational scenario `SC-01`: rider asks for accessible pickup during normal service; variations include unavailable vehicle, network partition and reassignment.
3. System requirement `R-01`: software-controlled platform delivers a receipt within an illustrative 900 ms nominal budget in a prescribed simulation workload.
4. Functional allocation `F-01`: accept request, check eligibility, select capacity, persist assignment, send status event.
5. Interface `IF-01`: trip-status event carries ID, version, event timestamp, valid-until time and source revision.
6. Planned V&V `T-01`: run a synthetic workload and inject out-of-order/duplicate events; compare outcomes to observable state guarantees.

## Layer 2 — OOAD domain and design

`TripRequest` has identity, rider, origin, destination and status. `Assignment` records trip, vehicle, validity interval and lifecycle. `VehicleCapability` and `AccessibilityPolicy` influence selection. A trip can have many historical assignments but at most one current active assignment. This is a domain invariant, not merely an application-layer convenience.

A design realization uses `TripRequestHandler` → `EligibilityPolicy` → `AssignmentService` → `AssignmentStore` → `EventOutbox`. The store must enforce the active-assignment invariant under competing requests. The outbox records a notification atomically with the business state so a relay can deliver it later. Receiver deduplication remains necessary.

The trip state machine is `Requested → Confirmed → InProgress → Completed`, with policy-bounded cancellation paths. A repeated acceptance message arriving after cancellation must not unconditionally restore the trip to `Confirmed`.

## Layer 3 — Software systems engineering

Architecture decisions include data ownership, deployment topology, retry limits, event ordering and audit boundaries. An illustrative end-to-end status latency budget is ingress 80 ms + queue 150 ms + compute 120 ms + persistence 100 ms + network 200 ms = 650 ms. Under a 900 ms nominal requirement this leaves 250 ms, but does **not** prove any tail-latency guarantee. That requires an experiment under specified load and failures.

A release case must tie requirements to tested builds and environments. If the operational connectivity assumption remains unverified or emergency fallback is untested, recommend a restricted laboratory milestone, not public operations.

## Cross-model audit table

| Intent | MBSE element | OOAD realization | Software evidence |
|---|---|---|---|
| Understand rider status | `N-01` / `R-01` | `TripRequest`, `NotificationPort` | timed load test and status usability scenario |
| Prevent double assignment | `F-01`, resource allocation rule | `Assignment` invariant | concurrent reservation and replay tests |
| Recover from network outage | `SC-01` exception / `IF-01` | outbox and idempotent consumer | partition/replay integration evidence |
| Maintain accountability | trace to `T-01` | audit event entities | revisioned logs and review disposition |

## Capstone exercises

1. Change the response threshold from 900 ms to 600 ms. Which model assumptions, interface budgets, design options and tests change? What hard evidence would establish feasibility?
2. Add a campus policy requiring all status messages to be deleted after 30 days, while safety audit events must be retained longer under separate authority. Draw the different data lifecycle and owner rules.
3. Inject a replayed assignment request after a successful transaction and lost reply. Show the new state if idempotency is absent, then state the guarded behavior.
4. Simulate a proposal to integrate emergency stopping into the dispatch platform. Explain why this changes system-of-interest responsibility, safety assurance, interfaces and operating permissions.

**Start the runnable investigations** in [`tools/README.md`](tools/README.md). Compare your results to the original course assessments rather than considering these short exercises sufficient for mastery.
