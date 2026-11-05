# Operational scenarios, use cases and software responsibilities

**Concept library essay · Phase 1**

## One mission, three different abstractions
An operational scenario answers what people and the system must accomplish in context. A software use case answers how a user goal interacts with the software boundary. A software architecture design answers where responsibilities live and what interfaces realize the use case. These descriptions overlap but their boundaries differ. If an autonomous vehicle enters a safe state when a communications link fails, the operational scenario may describe the full service consequence; the software use case may only describe a dispatcher alert; the onboard controller's logic may be outside the software team's authority.

Take 'rider requests pickup.' The operational scenario includes physical accessibility, stop selection, weather, fleet readiness and fallback transport. The software use case focuses on entering a request, eligibility validation, finding capacity, confirmation and failure. The design introduces policies, transactions, APIs and storage. Treating the design as the use case hides which choices are contingent and which user outcomes are obligatory.

## Deriving software requirements from a narrative
Use the following pipeline: (1) identify actors and outcomes; (2) identify each actor/system interaction; (3) enumerate normal, exceptional and malicious variations; (4) establish software versus nonsoftware authority; (5) specify measurable requirements; (6) connect candidate domain concepts; (7) map to verification or validation ideas. Example: a rider expects confirmation. Instead of 'the platform shall confirm immediately', write an illustrative measurable receipt requirement with workload and percentile, a separate booking-state requirement and a separate degraded-mode notification policy.

## Avoid accidental safety claims
The most dangerous ambiguity is confusing 'command acknowledged' with 'action accomplished.' A platform API may return HTTP 200 after a message is queued; that does not establish that a vehicle has executed it. Define event stages: accepted, enqueued, delivered, onboard validated, executed, observed. Different stages require different sensors and authorities. A graph of these stages is a more useful safety artifact than an optimistic status flag.

## Exercise
Write a use case for canceling a pending trip. Now change the precondition to 'passenger already onboard'. Which steps must move to vehicle control and operator procedures? Identify the new interface and the claim the software is actually allowed to make.

[Back to Phase 1 library](../README.md)
