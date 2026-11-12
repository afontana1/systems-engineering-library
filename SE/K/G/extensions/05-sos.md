## Integrated case NS-G4.1 — Constituent authority and network flow

> **NS-G4.1 case convention.** Every number in this extension comes from a controlled, fictional emergency-dispatch dataset, unless explicitly identified as an illustrative assumption. A Python screening result is not an operational safety finding, a validated queue model, or an authorization from independently managed agencies. The case is shared with the other five advanced-studies chapters; use the same `revision: 1.0` throughout.

**Reproduce:** [controlled JSON](../data/ns-g4.1-case.json) · [Python model](../code/ns_advanced_case.py) · [computed results](../outputs/ns-g4.1-results.json) · [integrated laboratory](../labs/INTEGRATED-CASE.html).

### G1. An accessible mission thread is a constrained network

Requests reach a dispatch hub, then rail and paratransit constituents, and finally a care destination. The owners of rail, paratransit, road access, and dispatch independently control their capacity and interfaces. For an initial *upper-bound screening exercise*, assign each directed arc a synthetic maximum number of accessible trip slots in a common decision window. Let \(f_{ij}\) be flow on arc \((i,j)\) and \(c_{ij}\) its capacity. Maximize sink flow subject to

\[
0\le f_{ij}\le c_{ij},\qquad
\sum_i f_{iv}=\sum_j f_{vj}\quad\text{for each internal node }v.
\]

The included Edmonds–Karp implementation finds an augmenting path in the residual graph and increases its flow until no positive-capacity source-to-sink path remains. Its result is a **structural upper bound on trip slots**, not a vehicle timetable, proof of accessibility compliance, or endorsement by constituent owners. Travel times, charging, scheduling, patient needs and jurisdictional rules are outside this small model.

**Worked calculation.** The baseline route capacities to care are 43 via rail and 25 via paratransit, while the shared Request→Dispatch arc holds 70. Thus nominal maximum flow is \(43+25=68\) slots, above the illustrative requirement of 55. With the coordinated policy, rail and paratransit arcs are increased but the shared dispatch input still caps total nominal flow at **70 slots**. Removing the rail constituent leaves only **32 slots** via paratransit under that policy, below 55. In the compound disruption, the shared input falls by 12 to **58** while demand is \(55(1.13)=62.15\) slots. The loss occurs even though more downstream resources are available: the bottleneck moved upstream.

### G2. Constituent change control must be explicit

The network graph encodes only capacity. To deliver a genuine mission thread, every constituent must publish: compatible interface revision, service interpretation, data-protection scope, real-time status semantics, authority to pause or override, and the evidence supporting each claim. A supplier revision can invalidate a thread without deleting any graph edges. In the `interface_drift` scenario, the route authority expects R3 but the coordinated policy still presents R2; the safety authorization check fails despite 70 nominal slots.

A federation integration test should exercise unavailable constituents, mismatched time bases, incompatible priorities, and emergency handoffs. It should also check provenance: *who asserted the capacity, when, at what revision, and under what obligation?* A central architect can propose a change, but cannot simply declare independent agencies to be under central command.

### G3. Bayesian evidence belongs to a declared question

Suppose the prior probability of a route blockage is \(P(B)=0.15\), the alarm sensitivity is 0.80 and its false positive probability is 0.10. A positive alarm yields

\[
P(B\mid+)=\frac{0.80(0.15)}{0.80(0.15)+0.10(0.85)}\approx0.5854.
\]

This belief update may guide what to investigate next, not a self-authorizing route closure or departure. Two alarms produced from one shared sensor do not count as conditionally independent confirmations. Keep belief about the hazard separate from legal authority and the route freshness evidence required to act.

### Worked exercise with explained solution

**Problem.** Eliminate the paratransit constituent under the coordinated policy. What is the maximum flow, and which assumptions prevent you from asserting that all 55 accessible requests can be served?

**Solution.** Rail has \(43+8=51\) slots into care, so max flow is **51**, below 55. Even a nominal 55 or greater would not establish geographic reachability, vehicle availability, journey timing, or patient suitability. Agency ownership and interface evidence remain independent gates.
