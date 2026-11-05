# Boundaries and interfaces: where local correctness meets system risk

**Reference entry · Foundations and architecture · Expanded reference**

## Definition

An **interface** is an agreed boundary across which two parties exchange information, matter, energy, behavior, or responsibility. A drawing that merely connects boxes is not an interface specification. A useful interface describes **what must be exchanged, under which operating conditions, with which semantics, timing, failure behavior, and ownership**. The parties may be subsystems, organizations, software services, suppliers, operators, or a system and its environment.

Interfaces matter because constituent teams can each satisfy local specifications while the integrated system fails: the data arrive too late, units differ, retries duplicate commands, or no organization accepts responsibility for recovering from partial failure.

## The graph-and-contract view

Represent the architecture as a directed multigraph **G = (V, E)**. Multiple edges between the same nodes may represent distinct information, power, material, or authority relationships. Cutting the graph along a proposed subsystem boundary exposes crossing edges. Each crossing edge should map to a versioned **interface contract** with producer and consumer, schema, preconditions, postconditions, invariants, quality attributes, and exception behavior.

A simple request-response contract might state: requests carry a unique identifier; accepted requests receive exactly one durable acknowledgement; a retry of the same identifier does not create a second booking; an unavailable scheduler returns a documented error within two seconds. These are end-to-end properties, not merely an API signature.

**Assume–guarantee reasoning** supports composition. Component A guarantees an output property when its environmental assumptions hold; component B's guarantee may depend on those outputs satisfying its own assumptions. Integration needs to show that adjacent assumptions and guarantees actually match. A producer emitting temperature in Fahrenheit does not satisfy a consumer that assumes Celsius even if both fields are typed as floating-point numbers.

## Worked example: interface latency and failure

Assume a passenger request passes through an app, authorization service, dispatcher, and vehicle gateway. Their nominal 95th-percentile latencies are 0.15, 0.20, 0.40, and 0.25 seconds. **Adding those marginal 95th percentiles does not generally give the end-to-end 95th percentile**: the slowest transactions might be correlated, queues may change with load, and calls may be parallel or serial. For a safe design budget, first identify path structure, measure jointly in realistic traffic, and reserve margin for network, retries, and orchestration.

Suppose each of four independent serial interfaces succeeds with probability 0.995 during one transaction. Under the stated independence assumption, joint success is **0.995⁴ ≈ 0.9801**, meaning a roughly 1.99% transaction failure probability. With a shared identity service or network dependency, failures are correlated and that product is no longer justified. Reliability depends on the dependency architecture, not just four component dashboards.

## Interface assurance procedure

1. Identify all boundary crossings, including human and supplier handoffs.
2. Define meaning before encoding: units, identifiers, versions, coordinate frames, ownership, and authority.
3. Specify timing, throughput, resource budgets, and operational modes.
4. Specify retries, duplicates, timeouts, stale data, degraded operation, and recovery.
5. Assign a producer, consumer, and accountable integration owner.
6. Verify local contracts; then exercise multi-interface scenarios, fault injection, and recovery paths.

An interface-control document is evidence of an agreement, not evidence that the integrated behavior works. Test data must identify the exact versions and configurations exercised.

## Common errors and limits

Beware **syntactic interoperability without semantic interoperability**: a valid message may carry a misunderstood concept. Beware interface contracts that specify normal throughput but omit degraded behavior. Beware ownership gaps between contractual suppliers, and treat manual organizational handoffs as real interfaces with latency and error modes.

Interface completeness is context-dependent. A safety-critical control link may require temporal properties and fail-safe modes; an archival metadata link may prioritize provenance and migration. Neither can be evaluated solely by counting interface fields.

## Cross-disciplinary connections

The interface graph connects architecture to cybersecurity attack surfaces, reliability dependency graphs, queueing networks, digital-thread provenance, human factors, and federated systems-of-systems governance. Traceability should link each critical interface property to its verifying evidence and to the scenario in which its failure matters.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Reference chapters for lifecycle, needs, requirements, design, technical management, integration and V&V.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Breadth-first conceptual encyclopedia and pointers to further references.

**Expanded tutorial:** [System boundaries, ownership and interfaces](../deep-dives/01-system-boundaries-and-interfaces.md)


## Technical analysis: assume–guarantee contracts at a boundary

A component interface can be represented by an **assumption** `A` about its environment and a **guarantee** `G` about behavior when `A` holds. Composition is safe only if the neighboring component's guarantee satisfies the first component's assumptions, including timing, semantics, error handling, and operating modes. Passing a packet-format test alone establishes neither end-to-end capacity nor failure containment.

Suppose a dispatcher emits **8 assignments/s** on average and the downstream service can accept **10/s** under its tested configuration. The steady-state average capacity margin is **2/s**. If retries after an outage double the arrival rate to **16/s** while processing remains at **10/s**, backlog grows at **6 requests/s** for as long as that regime persists. After **30 seconds**, the idealized net increase is **180 requests**, before drops or admission control. The average condition therefore cannot substantiate a claim that overload recovery is safe.

**Evidence boundary.** Make timeouts, request identity, units, clock domains, validity periods, and fallback state explicit. Test bursts and retry storms, not merely nominal throughput. When components are allocated to independent suppliers, record who controls interface change and how compatibility is demonstrated for *each pair of released versions*.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Interface management identifies physical, functional and human interfaces and controls compatibility and change. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.3 Interface Management](https://www.nasa.gov/reference/6-3-interface-management/) · *direct guidance*.
- **C2:** Security and trustworthiness concerns must be engineered at system scope, not exclusively inside components. **Evidence:** [NIST — SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022), System security engineering concepts, activities, tasks, and trustworthiness principles](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) · *scope-supported interpretation*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [NIST · SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) — System-level security and trustworthiness engineering.

## Follow the knowledge

**Related concepts**

- [System of interest and purpose](system-of-interest.md)
- [Interface control and integration contracts](interface-control.md)
- [Functional, logical, and physical architectures](functional-vs-physical.md)
- [System of systems and constituent independence](sos-characteristics.md)

**Explore in the 240-chapter textbooks**

- [Book 1, Chapter 10: Chapter 10 — Failures Travel Through Interfaces and Organizations](../B1/chapters/10-failures-and-controls.md)
- [Book 7, Chapter 4: Book 7 · Chapter 4: Physical architecture and contracts](../B7/chapters/04-mature-the-physical-architecture-interfaces-and-perform.md)
- [Book 18, Chapter 5: Week 05 · System of Systems Engineering · Chapter 05 — Information architecture and multidimensional interoperability](../B18/chapters/05.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

