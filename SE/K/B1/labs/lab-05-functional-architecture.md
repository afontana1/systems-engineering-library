# Hypothetical Lab 5 — The Missing State

**Course:** EN.645.662 Week 5 · **Reading:** [Chapter 5](../chapters/05-functions-and-behavior.md) · **Time:** 90–120 minutes · **Nature:** fictional dispatch-model design review.

## Situation and controlled inputs

Northstar's dispatch group supplies the following incomplete behavior: `RequestReceived → Accepted → Assigned → Closed`. It assumes all assignment messages arrive once, vehicles remain available, and a request can be closed at any time. The group has not modeled refusal, rescheduling, or loss of telemetry. The stated operational need is that each received request have an accountable final disposition and that an unsafe or unsupported assignment not be issued.

The fictional service has an eight-second provisional booking-status budget. Candidate allocations are intake 0.5 s, validation 1.0 s, assignment 3.0 s, persistence 1.0 s, notification 1.0 s and contingency 1.5 s. The numbers are invented for instruction.

## Tasks

1. Write at least six verb–object functions independent of software module names. For each identify its triggering event, output, and likely failure mode.
2. Produce a functional hierarchy with `Manage trip service` at its root. Explain why `Send push notification` is narrower than `Inform rider of decision` and where each belongs.
3. Repair the state machine to permit rejected, canceled, disrupted, and degraded outcomes. Specify guard conditions for assignment and closure. No request should become `Closed` without a recorded disposition.
4. Create two flow definitions: `AssignmentDecision` and `VehicleReadiness`. Include producer/consumer, key fields, timestamp meaning, units where relevant, timing and invalid-message behavior.
5. Build a four-row matrix linking scenarios (normal trip, no available vehicle, telemetry loss, duplicate request) to functions and requirement intents. Mark unresolved source assumptions rather than inventing approvals.
6. Sum the provisional timing budget and identify a case where adding averages is not an acceptable end-to-end performance assurance method.

## Deliverables

Create `LAB05_FunctionTree.md`, `LAB05_StateTransitions.csv` and `LAB05_FlowDictionary.csv`. The state table should include `from_state,event,guard,to_state,side_effect`. In your short review memo, distinguish a hypothetical design from a validated dispatch system.

<details><summary>Reference reasoning — open only after attempting the lab</summary>

Necessary functions include `Validate request`, `Check resource readiness`, `Allocate feasible vehicle`, `Publish status`, `Record decision`, `Detect disruption` and `Manage fallback`. A defensible state model should avoid direct `Assigned → Closed` transitions unless an explicit completion, cancellation or failure disposition is recorded. A `telemetry_stale` transition might cause assignment suspension, not blind continuation. The budget sums to eight seconds; it is not tail-latency evidence. Lost notifications and retry queues can violate the nominal budget. The flow dictionary should distinguish measurement time from receipt time. Structural scenario coverage alone will not prove a safe fallback.

</details>

## Transfer to assessed work

Return to original `662_W05_FunctionalArchitecture_v1.0`. Its three behavioral views, trace matrices, change log and original mastery rubric require a more extensive independent artifact than this practice case.
