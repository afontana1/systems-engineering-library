# Safety engineering: from hazards to enforceable constraints

*Core Concepts · Assurance · T13*

> Build a safety argument from unsafe control actions, causal scenarios, controls, and residual uncertainty.

**Recommended preparation:** [02 Requirements](02-requirements.md), [09 Assurance](09-assurance.md)

**Related companion books:** [Book 1](../B1/OPEN-BOOK.html), [Book 7](../B7/OPEN-BOOK.html), [Book 8](../B8/OPEN-BOOK.html), [Book 17](../B17/OPEN-BOOK.html)

## 1. Begin with losses, not a list of defective parts
A system can be unsafe even when each component behaves exactly as specified. An autonomous shuttle may respond correctly to a dispatch request while its dispatch policy permits a vehicle to enter a pedestrian zone during an evacuation. The safety failure is a **system-level interaction**: instructions, timing, authority, and operating context combine to produce a hazardous state. A component failure list alone will miss it.

Define the unacceptable losses first: serious injury, obstruction of an emergency corridor, or loss of emergency access. Then identify hazardous system states that could contribute to them. For example, **H-1**: a shuttle is commanded to move when its operational exclusion zone intersects an active emergency route. Unlike a broad statement that the shuttle should be safe, H-1 gives an engineer something observable to investigate.

Safety engineers distinguish a *hazard* (a system condition with the potential to contribute to a loss) from a *risk* (which also reflects likelihood and consequence). Ranking all hazards by a subjective 1–5 score may help organize discussion, but a low score never removes a design constraint; poorly understood severe outcomes often need analysis precisely because frequency estimates are weak.

## 2. Reason about the control structure
Draw the controller, controlled process, actuators, sensors, operators, and feedback. A dispatch service issues a route release; a vehicle controller implements it; a geofence service provides zone state; a human operator may issue emergency stops. Each link has time delays and possible stale data. The system can fail because a control action is missing, provided when prohibited, issued too early or late, or applied for too long.

For H-1, examine four kinds of unsafe control action:

1. Dispatch *provides* a move command despite an active exclusion.
2. Dispatch *fails to provide* a stop command after an exclusion is declared.
3. Dispatch provides a safe command *too late* to avoid entering the corridor.
4. Dispatch permits continued movement *too long* after location evidence becomes stale.

Convert the actions into constraints: **SC-1**: a release authorization shall include the latest validated exclusion-zone revision. **SC-2**: when the zone feed is stale beyond an allocated threshold, the vehicle shall transition to a defined restricted state. **SC-3**: a stop command shall be accepted independently of normal dispatch availability. None of these is meaningful without definitions of “latest,” “stale,” and “restricted.” Those definitions belong in interface contracts and tests.

## 3. Contrast three analysis methods
**FMEA** begins with items or functions and asks how their failure modes affect higher-level performance. Its useful columns include failure mode, effects, current detection mechanisms, compensating action, and verification evidence. It tends to be bottom-up. **Fault-tree analysis** starts with an unwanted event and combines contributing events using AND/OR logic; it is top-down. **STPA-style causal analysis** examines unsafe controls and inadequate feedback even without failed components. They answer overlapping but different questions and should not be forced into one ranking table.

For a simple fault tree, suppose unsafe release can arise through either **A**, a stale-zone feed accepted as current, or **B**, a bypassed authorization rule. If the events are independent and each has probability 0.01 per specified demand, then

\[
P(A\cup B)=P(A)+P(B)-P(A)P(B)=0.0199.
\]

If they share a configuration defect, independence is not defensible. A fault tree is a *model of causal possibilities*; an arithmetic answer is only as credible as the event definition, dependency assumptions, and supporting evidence.

## 4. Derive a verification plan from constraints
For each safety constraint, identify a measurable claim, a test stimulus, a witness observable, and the required configuration. For SC-2, configure a valid zone feed, deliberately stop updates, record the last accepted revision and timestamps, and check the state transition with a timing tolerance. Repeat at boundary conditions: one update before the threshold, exactly at the threshold, and just after. Then test interactions with a pending route release and a disconnected operator console.

A simulation can demonstrate that the transition logic behaves as intended for modeled delays, but it cannot establish the behavior of a physical vehicle unless the model's sensor, timing, and actuation assumptions are justified. A completed test line is not the same thing as a closed safety argument. Keep unresolved hazards, assumptions, configurations, and restrictions visible in an assurance case.

## 5. Allocate safety authority
Safety constraints should have owners. A service team may own stale-message detection; vehicle software may own a safe-state transition; an operations team may own emergency-corridor procedures. A constraint spanning multiple owners also needs an *integration* verification method. Without an authoritative contract for the boundary, each constituent can pass its own tests and still create an unsafe behavior at the system level.

A safety claim should be bounded: “In simulated scenarios S-01 to S-09, configuration R-4 entered the restricted state within the 2-second allocated deadline” is narrower but more defensible than “The shuttle is safe.” Reviewers should ask: What contexts were excluded? Which assumptions are unverified? What monitoring would detect a changed operational environment?

## 6. Worked decision: stale evidence versus mission continuity
Northstar wants continued operation when the zone feed is lost. One option allows a 20-second grace period; another requires immediate restricted operation. The grace period preserves trips, but it also permits 20 seconds of motion based on information no longer known to be current. The engineering decision cannot be made solely from average trip delay. Estimate the worst credible motion distance during the grace period, evaluate exclusion-zone boundaries and stopping behavior, and record the cost of both missed service and hazard exposure. At 5 m/s, 20 seconds represents 100 m of potential travel *before* accounting for reaction, braking, and spatial uncertainty. That estimate is not a safe stopping-distance calculation—it is a prompt to study the real dynamics.

## Questions to solve before checking the answer
**A.** Explain a hazardous interaction that occurs even if every device is working as designed. **B.** Draw a two-event fault tree with an OR gate, then explain one reason its independence assumption could fail. **C.** Write a testable stale-feed safety constraint using explicit time and state variables.

<details><summary>Instructor reasoning</summary>

A valid A identifies a policy, interface, or timing mismatch and its loss pathway. For B, use the inclusion-exclusion probability formula; a common software revision, data source, or maintenance activity can couple events. For C, define a last-valid timestamp, an authorized state, a threshold, and a measurable transition deadline. A good answer also describes how a deliberate clock skew will be handled.

</details>

## Further connections
Read [Requirements and assurance](02-requirements.md) for traceability and [Statistical evidence](06-inference.md) before interpreting accident or test counts. Book 8 develops the test campaign; Book 17 addresses governance of engineering controls.

## Guided laboratory

[Open the corresponding case-based lab](labs/13-safety-constraints-workshop.md)
