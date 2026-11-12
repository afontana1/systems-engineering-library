# Chapter 6 — Structure is not the same as connectivity

*Book III: Introduction to Model-Based Systems Engineering · Week 6 — Structure, interfaces, ports, connections, and the midcourse model review*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 6](../labs/lab-06-structure-interfaces-ports-connections-and-th.md) before attempting [the assessed Week 6 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w06.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **structure, interfaces, ports, connections, and the midcourse model review** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

The architectural structure names parts, hierarchy and interfaces; the connection model specifies interactions among those parts. A port describes a boundary interaction contract, not an ornamental mark on a block. Each connection needs direction, information or material type, timing assumptions, ownership and failure handling. Review model consistency before claiming an interface is integrated.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Structural models distinguish composition, association, ports and item flows; the differences determine ownership, multiplicity and the obligations of connection.

### Distinguishing related ideas

A block that contains another block is not the same assertion as two blocks exchanging data; confusing them causes wrong change-impact or interface analysis.

### Interpretation and boundary conditions

An interface is adequately modeled only when units, direction, timing, legal values and responsibility are constrained enough to reject an invalid exchange.

## Deeper theory: interfaces as contracts across separate authorities

A block diagram shows parts and connectors, but it does not automatically explain what a connection **means**. Two boxes connected by a line may exchange matter, energy, data, commands, mechanical load, or a combination. They may also belong to different organizations and have distinct rules for changing the interface. Calling all of these edges “connections” is like calling every relationship in a legal contract “knows about”: the structure may be visible, but the obligations are missing. Engineering interfaces require semantic contracts that define permitted interactions and observable behavior across a boundary.

A useful interface description has at least four layers. The **physical layer** specifies medium, geometry, units and environmental limits. The **information layer** specifies message types, fields, encoding, timestamps and identifiers. The **behavioral layer** specifies allowable sequences, state-dependent commands, retries and timeouts. The **assurance layer** specifies how compliance will be demonstrated and how revisions will be governed. For a charger-to-vehicle interface, a connector drawing is only one part of the contract: power negotiation, safety interlock states, thermal limits, interruption recovery, and version compatibility may determine whether the coupled system is safe.

### Why ports are more than names on a diagram

A modeling port can describe a boundary through which a block interacts with its environment, but the interpretation depends on the modeling language and the selected semantic layer. In a SysML-style structural model, a proxy port may expose features of a boundary rather than define a physical part. A full port may represent a constituent with its own properties and behavior. A connector establishes a relationship between endpoints; it does not independently prove that the connected interfaces are compatible. Compatibility requires stronger assertions: connected flow directions, types, units, rates, protocols and state conditions must agree.

Consider a dispatch service sending a requested pickup time expressed as a number. If the producer interprets `120` as seconds after midnight and the consumer interprets it as minutes after the request, a syntactically well-typed integer connection is semantically invalid. The problem extends beyond units: a field named `vehicle_available` may mean “not currently on a trip,” “not undergoing maintenance,” or “suitable for this passenger and route.” A model's usefulness depends on **shared semantics**, not simply on having typed attributes.

### Assume–guarantee reasoning and compositional limits

For subsystem \(i\), let \(A_i\) denote assumptions about its environment and \(G_i\) the behavior it guarantees when those assumptions hold. The contract has the logical form \(A_i\Rightarrow G_i\). To compose two subsystems responsibly, the guarantee of each must be strong enough to satisfy the other's assumptions under the intended operating conditions. If a vehicle controller assumes command latency below 100 ms and the network only guarantees a 95th-percentile latency below 100 ms, the mismatch is conceptual: the controller has implicitly assumed a **hard bound** that the network has not provided.

An interface budget must also account for shared sources of uncertainty. Suppose sensor processing, networking, dispatch computation and actuation each claim “less than 50 ms in 99% of cases.” It is invalid to conclude that the end-to-end chain takes less than 200 ms in 99% of cases. The distribution of a sum depends on the dependence among its terms, and a rare overload may slow all stages simultaneously. Deterministic worst-case composition requires genuine hard bounds; statistical composition requires a justified joint model. An interface contract should not mix the two without explanation.

### Versioning is part of architectural behavior

In a long-lived engineered system, components are upgraded independently. A change that adds a new field or tightens a timeout can break an older participant even when the connector remains physically unchanged. “Backwards compatible” must be defined by the class of interactions older participants are permitted to perform. Compatibility can be tested using representative traces and explicit assumptions; a mere shared version number is insufficient.

The deeper lesson is that structural models are maps of **responsibility and mutual obligation**. Their value lies in making visible where assumptions cross organizational or technical boundaries and where a locally correct part may rely on an unavailable environmental guarantee. A rigorous interface model is less a picture of wiring than a compact statement of what each participant can safely rely on.

## Worked Northstar example

Dispatch sends AssignmentRequest(request_id, vehicle_id, expires_at) to VehicleGateway. Gateway returns Accepted or Rejected. The payload schema is valid but a stale expires_at should still be rejected; structural compatibility is weaker than behavioral compatibility. At the Week 6 review, test the stale-message case explicitly.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

A polished block diagram cannot establish that both sides agree on units, time basis or fault behavior.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 6: Structure is not the same as connectivity](../labs/lab-06-structure-interfaces-ports-connections-and-th.md), you will: Prepare a six-element architecture model and an interface control sheet. Inject one unit mismatch and one timeout disagreement for a mock review board. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 6 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](05-behavior-modeling-use-cases-activities-action.md) and leads toward [next chapter](07-logical-architecture-functional-allocation-de.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w06.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Phase 5 technical reading: Treat interface freshness as an explicit model constraint

A speed interface reported as `0.3 m/s` can be unusable when its timestamp is older than its contract allows. In the fictional CM-B2 interface control extract, speed and brake signals are refreshed every 50 ms with 150 ms maximum valid age; a 180 ms-old value must inhibit door opening irrespective of a nominal magnitude. This requires not just a connection arrow but an item definition, units, clock semantics, validity rule and associated verification. The [worked SysML/traceability reference](../../methods/sysml-v2-modeling-and-traceability.md) includes the minimum structural notation, related interface CSV and a plan for validation in an official parser without claiming the skeleton has been tool-certified.

## Step 03 integrated reference: ports are contracts, not lines

### Make interface claims observable

A useful interface contract specifies producer, consumer, payload type, units, time base, validity interval, failure behavior and responsible authority. Connecting a component box to another component box does not establish that their representations agree. In NS-MB3, `IF-01` sends a position-age measure from `TELEMETRY` to `DISPATCH`, expressed in milliseconds with an allowed age of 200 ms. That contract is incomplete unless it states which clock created the timestamp, what happens on clock resets, whether message age is measured on receipt or use, and the response to unavailable telemetry.

A basic data-age predicate is

\[
a(t)=t_{\mathrm{use}}-t_{\mathrm{sample}}\le 200\ \mathrm{ms}.
\]

This is meaningful only if the timestamps are on a sufficiently synchronized clock or the age is computed through a monotonic local clock under a justified transport model. If a sensor message is sampled at 1.000 s and used at 1.245 s, its observed age is 245 ms and the freshness constraint fails, irrespective of whether the network delivered it “successfully.” A validation rule should reject missing timestamps, negative ages caused by clock inconsistency, unexpected units and malformed identifiers.

### Budget processing delay explicitly

The nominal dispatch command path comprises four synthetic processing segments: 90, 110, 80 and 45 ms. Under an additive serial-path assumption,

\[
L_{\mathrm{nom}}=90+110+80+45=325\ \mathrm{ms},\quad
M_{\mathrm{nom}}=400-325=75\ \mathrm{ms}.
\]

In degraded mode the segments are 120, 140, 120 and 80 ms, for a total of \(460\) ms and margin \(-60\) ms. The nominal requirement `REQ-04` is not automatically violated by a degraded-mode result because its declared scope is nominal; however, the degraded result is a **design issue** that must be evaluated against service and safety needs. It would be misleading to claim universal command responsiveness from the nominal 75-ms margin. If segments execute in parallel, adding them overstates latency; if retries or batching occur, the four-component estimate may understate tail behavior. A verified interface analysis needs an execution model or measured traces.

### Contract tests and change impact

For each interface, define a valid case and at least one failure case: wrong unit, missing timestamp, out-of-order sequence, duplicate message, stale value, and incompatible schema revision. Record whether the receiver rejects, falls back, or enters a degraded state. A release should not infer compatibility from matching component names; the consuming function's preconditions and assumptions must be checked against what the producer guarantees.

**Exercise with answer.** A position update is sampled at 12.000 s and used at 12.180 s. Is `IF-01` satisfied? Under the stated synchronized-clock assumption, yes: age is 180 ms, leaving a 20-ms margin. If telemetry is sampled at 12.000 s and used at 12.245 s, no: age is 245 ms. The same payload can therefore be acceptable at one use instant and stale at another.
