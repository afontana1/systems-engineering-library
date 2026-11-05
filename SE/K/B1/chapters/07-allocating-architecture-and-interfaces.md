# Chapter 7 — Architecture Is the Allocation of Responsibility

*EN.645.662 · Week 7. Read after the functional baseline review in [Chapter 6](06-reviewing-the-functional-baseline.md); rehearse with [Hypothetical Lab 7](../labs/lab-07-interface-contracts.md).*

## The system doesn't live in a block diagram

After the functional review, Northstar must turn logical behavior into an implementable arrangement of software, vehicles, operators, infrastructure, procedures, and external service providers. The architecture is not just a list of pieces. It is a set of **responsibilities, relationships, and constraints** that allow the pieces to accomplish the mission together.

A diagram showing *vehicle ↔ cloud ↔ rider application* conceals several decisions: is dispatch authorized in the cloud or the vehicle? What happens when the cloud is inaccessible? Can the vehicle accept a boarding authorization without a fresh operator policy? Who manages stop accessibility information? Which team owns the interface if the consumer receives incompatible units or stale timestamps? Architecture is where these ambiguities are converted into design decisions, explicit dependencies, and accountable interfaces.

## 7.1 Separate logical, physical, and organizational views

A **logical architecture** represents functions and information exchanges independent of which product realizes them. A **physical architecture** assigns those obligations to elements that can be built, purchased, configured, staffed, or operated. An **organizational view** captures authorities and responsibilities. The three views should be consistent without being identical.

For example, `Assess trip feasibility` is a logical function. It could be allocated to a central dispatch service using vehicle telemetry, or to a distributed decision service in each vehicle with periodic coordination. The two choices create different connectivity dependencies and different risks. A team that has only one diagram may be unwittingly hiding an architecture assumption instead of analyzing it.

The project also needs enabling systems: depots, charging infrastructure, maintenance processes, integration test rigs, incident response tools, onboarding procedures, and training material. A shuttle plus app without these enabling products is an incomplete concept of operation.

## The mechanism beneath the method

Physical architecture allocates functions to components and thereby creates failure paths, interfaces, maintenance responsibilities and integration work.

### Distinguishing related ideas

A functional decomposition groups what must happen; a physical decomposition decides which parts carry out those functions, and the mapping is usually many-to-many.

### Interpretation and boundary conditions

Two candidate designs can realize the same function yet have different fault-containment, timing and replacement consequences because their allocations differ.

## 7.2 Allocate functions with a rationale

An allocation record should say which element owns the function, which other elements contribute, what performance budget it inherits, what alternatives were considered, and what evidence will eventually test the allocation. For the Northstar demonstration, allocate `Publish assignment` to a dispatch service, `Display booking status` to the rider app, and `Confirm physical boarding state` to the vehicle/controller. The dispatch service remains responsible for the *meaning* of its decision even if a third-party messaging service transports the message.

An effective **allocation matrix** identifies functions with no owner and elements with no justified capability. Both deserve investigation. Also watch for many-to-many allocation: safety-relevant actions may require both automated checks and a human authorization process. The matrix should name the decision authority, not merely list software modules.

## 7.3 An interface sheet is a contract

Consider a proposed `VehicleReadiness` event. A minimally useful interface contract specifies:

| Field | Teaching value |
|---|---|
| Producer and consumer | Vehicle telemetry gateway → dispatch validator |
| Semantics | Position, serviceability, door state, effective timestamp, schema revision |
| Units and reference frame | Meters, agreed coordinate system, UTC timestamps |
| Freshness | **Illustrative** limit of 5 seconds when accepting an assignment |
| Failure behavior | Reject stale readiness for new assignment; enter explicitly defined degraded flow |
| Owner and change authority | Gateway owner, dispatch consumer, interface control board |
| Verification | Contract tests for units, schema revisions, duplicates, missing messages and stale values |

The five-second figure is not a real safety-approved limit. It is a scenario assumption that students should challenge. For an interface, a syntactically valid payload can still be wrong: a latitude/longitude pair interpreted with inconsistent units, an outdated position, or a status that changed after message creation. Versioning and event time must therefore be treated as engineering semantics, not developer conventions.

## 7.4 Interface contradictions reveal architectural risk

Assume the dispatch service treats any readiness message received within five seconds as fresh, while the vehicle publishes telemetry every eight seconds during normal operation. Even with zero network latency, legitimate readings may exceed the consumer's freshness limit. That creates a contradiction in the architecture. The solution is not simply to add a retry loop; the designers must decide whether to revise publication frequency, adjust the justified freshness rule, establish a direct-query path, or prohibit new assignments under that condition. Each choice has costs, performance consequences, and potential hazards.

Interface management includes agreements with *external* organizations. A transit stop may be owned by a facilities group, not the shuttle supplier. If the stop's boarding geometry is not controlled by the project, a vehicle-level accessibility demonstration does not by itself validate accessible service. The interface register must include the owner of the physical stop and the process for resolving incompatible assets.

## 7.5 Plan the integration sequence from dependencies

If the first integrated test connects every component at once, failures are hard to isolate. Instead build progressively: validate message schemas and state contracts in a software-only rig; then integrate the simulated dispatch logic with virtual vehicle state; then introduce telemetry dropouts and stale-message tests; only then proceed to higher-fidelity hardware or operational rehearsals as authorized. Each stage has entry and exit criteria and collects evidence against specific risks.

A useful dependency graph captures which interfaces must stabilize before a higher-level behavior can be demonstrated. Safety-relevant interfaces may require independent monitoring. A low-level message contract test does not replace scenario validation; it reduces uncertainty so higher-level tests become interpretable.


## Deeper theory — architecture as a distribution of constraints and authority

### Function is not component

An architecture describes *how responsibilities are separated and made to cooperate*. Functional reasoning begins with transformations that must occur: recognize a request, determine eligibility, select a vehicle, authorize a trip and report completion. Physical reasoning asks where those transformations occur—in an app, dispatch service, onboard controller or human operations team. Organizational reasoning asks who is entitled to change the behavior, who resolves conflicts and who bears the consequences of error. If these views are collapsed into a single block diagram, the diagram can appear complete while omitting its most consequential decisions.

The same function can be realized by different allocations. Trip eligibility might be decided centrally by a cloud service, locally by the vehicle, or through a split protocol with cached rules. These alternatives differ less in what they do nominally than in the failures they permit. A cloud-only decision is easy to update consistently but depends on connectivity. A vehicle-local decision may survive a network outage but risks using stale authorization. A hybrid requires a conflict-resolution rule. Every physical partition therefore creates a *coordination contract* that was unnecessary when the function was imagined as one uninterrupted activity.

### Coupling explains why interfaces become expensive

Decomposition creates modules, but it also creates dependencies. Two components are tightly coupled when a local change in one forces changes or new assumptions in the other. Coupling may concern data schemas, timing, control authority, failure modes, deployment schedules or even shared staff. A well-designed interface does not abolish coupling; it makes unavoidable coupling explicit and aims to keep it stable. For example, a booking client should depend on the meaning of “accepted request,” not the dispatcher's internal database layout. Otherwise a database migration becomes a system-wide safety and interoperability event.

An interface contract should include preconditions, accepted inputs, units, versions, causal ordering, success semantics and behavior under partial failure. If the dispatch service acknowledges a trip, does that mean the request was received, durably recorded, allocated to a particular vehicle or irrevocably accepted? Those four interpretations lead to different passenger expectations and recovery obligations. Architecture is partly the art of eliminating ambiguous promises at module boundaries.

### Propagation rather than component-by-component correctness

A local requirement can be satisfied while a system-level requirement fails. Suppose a booking service responds in 0.4 seconds and a vehicle controller responds in 0.3 seconds, both within their allocated thresholds. The user may nevertheless wait 12 seconds if requests sit in a shared queue or if a human approval is required. End-to-end performance is governed by the *composition* of service, waiting and communication, not just the speed of individually tested components.

Likewise, two nominally redundant servers are not independent if they share power, authentication, routing or a badly specified schema migration. Under ideal independence, the availability of two parallel elements each with availability \(a\) is \(1-(1-a)^2\). If a common-cause event disables both with probability \(q\), a simple illustrative model becomes \((1-q)[1-(1-a)^2]\), assuming the shared event is independent of the residual failure processes. This is not a universally valid reliability model; it shows why modeling the dependency structure is at least as important as improving component ratings. Architecture controls which failures can propagate and which can be contained.

### Allocation as an optimization under incompatible objectives

Architecture choices are usually multiobjective. Central dispatch may reduce administrative effort, while distributed authorization may improve continuity under outages. Assigning all safety decisions to a human could reduce certain automation hazards but overload that person during emergencies. There may be no architecture that is simultaneously cheapest, safest, fastest, easiest to maintain and most resilient. Engineering judgment must identify hard constraints first—such as a prohibited unsafe action—and then compare feasible alternatives under clearly stated preferences.

A weighted trade study is a tool for making a preference model inspectable, not a mechanical answer generator. If a design wins only because an arbitrary score weight changes from 0.49 to 0.51, the decision is fragile. If it fails a non-negotiable accessibility requirement, no attractive weighted average repairs that infeasibility. Architecture selection should preserve the distinction between constraints that must be met and benefits among which stakeholders are willing to trade.

### The three baselines that must stay aligned

A credible architecture links three different things. The **logical baseline** says what behaviors and obligations exist. The **physical baseline** identifies the elements and interfaces that are supposed to realize them. The **evidence baseline** identifies tests, analyses and observations that support claims about those elements and interfaces. A change in physical implementation can invalidate evidence even when the logical requirement text is unchanged. Similarly, moving an authorization decision from a vehicle to a cloud service can alter cybersecurity, timing and human-override assumptions without visibly changing the passenger-facing feature.

This is why integration planning should follow the *risk of interaction*, not simply the order in which components become available. Integrate the most uncertainty-bearing interface early enough to learn before the expensive architectural commitments are fixed. Then retain a record of which model versions, software builds, operating conditions and tests justify the resulting claims. A well-designed architecture is not just understandable on a diagram; it makes dependency, failure propagation and responsibility inspectable when reality departs from the nominal case.

## 7.6 Worked allocation trade: central or distributed dispatch?

Take a fictional service with intermittent connectivity. Architecture C uses a centralized assignment authority: decisions are globally coordinated but depend on backhaul. Architecture D allows each vehicle to accept requests in degraded mode: backhaul dependence decreases but duplicate assignment, conflict resolution, and safety authorization become more difficult. The right comparison is not “centralized is simpler” versus “distributed is resilient”; quantify communication assumptions, system state consistency, human oversight, and failure recovery. An architecture can improve one failure mode while creating another. Record competing values before selecting a concept in Chapter 8.

## 7.7 Practice with explanations

**A. Distinguish.** Is a maintenance center a system element? **Answer:** It can be an enabling system or constituent element depending on the chosen boundary and architecture. State its role and interfaces explicitly.

**B. Detect.** Consumer freshness limit = 5 seconds; normal publication interval = 8 seconds. Is the contract jointly satisfiable at all times? **Answer:** Not under the stated simple periodic model. A redesign or a specified degraded behavior is required.

**C. Assign.** Who owns correctness of `AssignmentDecision` if a messaging provider delivers the payload? **Answer:** The architectural decision owner remains responsible for semantic correctness, while the transport supplier owns contractually assigned transport behavior.

**D. Verify.** A schema test passes for a `position` field. Does that establish coordinate correctness? **Answer:** No; unit, reference frame, epoch, numeric range, and state freshness are separate semantics.

**E. Integrate.** Why validate lower-level interface contracts before scenario tests? **Answer:** To reduce ambiguity and isolate defects, while recognizing that end-to-end scenarios are still needed.

## Read, rehearse, produce

Complete [Hypothetical Lab 7](../labs/lab-07-interface-contracts.md), then return to the original Week 7 `662_W07_ArchitectureInterfaces_v1.0` deliverable. Its required architecture views, product breakdown, allocation matrix and interface sheets are more extensive than this fictional rehearsal.

**Next:** [Chapter 8 — Decisions under uncertainty](08-trade-studies-and-sensitivity.md).
