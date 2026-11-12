# System of interest: purpose, boundary, and evidence

**Reference entry · Foundations · Expanded reference**

## Definition and diagnostic distinction

A **system of interest (SoI)** is the collection of elements, interactions, and responsibilities being examined for a stated purpose. Its identity follows from a decision and a mission, not merely from the organization chart or a drawing. The same shuttle operation can be treated as a vehicle subsystem for a battery engineer, a dispatch-and-fleet system for an operations engineer, or a mobility service within a campus transportation ecosystem for a public-policy decision. All three boundaries can be legitimate, but their claims and evidence are different.

An *enabling system* supplies capabilities for creating, operating, maintaining, or retiring the SoI; an *external system* exchanges matter, energy, information, services, or obligations with it. A system can be an element of a larger system while simultaneously containing many smaller systems. A boundary therefore must declare what counts as internal, what is external, who owns each interface, and which assumptions are being held fixed.

## Theory: purpose precedes decomposition

A system description should connect a mission outcome to a measurable state or event. Let an operational scenario be a tuple **(actors, demand, environment, mission, constraints, observation window)**. An engineering claim is meaningful only over a defined set of such scenarios. “The service is reliable” is incomplete; “at least 98% of scheduled departures occur within five minutes during the academic weekday peak, excluding declared severe-weather closures” has a testable denominator, window, threshold, and scope.

The **system boundary** can be represented by a directed graph: nodes are constituents and external actors; edges are transfers or commitments. A boundary partitions nodes into internal and external groups. Every edge crossing the partition is an interface, and its assumptions must be made explicit. Boundary selection changes which causes are endogenous, which appear as disturbances, and who can actually change the outcome. A narrow vehicle-only analysis may miss a common dispatch outage that disables the entire service.

This also distinguishes *function* from *purpose*. Carrying a passenger is a function; enabling equitable, timely access to campus is a service purpose. A design can execute its assigned function correctly yet fail the larger mission when scheduling, accessibility, pricing, or human interaction is considered.

## Worked example: a decision that changes the boundary

Suppose a proposed campus shuttle redesign is evaluated during a one-hour peak. Assume 180 passenger requests, 162 completed within the target waiting time, 12 completed late, and 6 were not served. The **on-time service fraction over all requests** is 162/180 = **90%**. Reporting 162/174 = 93.1% instead silently excludes the six unserved passengers and can make a degraded service appear better.

If the design team excludes the reservation application from its SoI, the six abandoned requests can disappear from the measured demand. If it includes the app, dispatch, accessible-vehicle allocation, and operations staff, these become diagnosable causes. The right boundary is the smallest one that still contains the mechanisms and decision rights needed to explain the stated outcome—not necessarily the smallest hardware assembly.

A boundary review should ask: Would a plausible external dependency reverse our conclusion? If yes, model that dependency explicitly or treat it as a documented scenario variable rather than silently assuming it away.

## Engineering use: a repeatable boundary decision

1. **State the decision.** Specify the question the model or design must answer and its intended audience.
2. **Specify outcomes.** Name the beneficiary, metric, population, scenario, and time horizon.
3. **Draw the boundary.** Mark constituents, human actors, enabling systems, and environmental disturbances.
4. **Account for transfers.** For each crossing edge, specify units, protocols, latency, failure behavior, responsibility, and evidence.
5. **Stress the boundary.** Test it with maintenance, failure, cyber, access, seasonal demand, and retirement scenarios.
6. **Record exclusions.** Identify questions the representation cannot answer without expanding the boundary.

## Assumptions, failure modes, and evidence

A SoI definition is not a claim that the world is closed. Market incentives, operator decisions, infrastructure failures, and feedback may be outside formal control but still shape outcomes. Beware **boundary laundering**: excluding the failing mechanism and then declaring the remaining subsystem successful. Beware also uncontrolled expansion: a boundary so broad that no accountable decision remains.

Credible evidence includes a scenario catalog; a context diagram with typed interfaces; operational measures with explicit denominators; an ownership matrix for cross-boundary dependencies; and counterexamples that challenge the chosen boundary. The boundary should be revisited after major architecture, mission, or stakeholder changes—not assumed permanent.

## Connections that matter

The SoI is the anchor for stakeholder analysis, ConOps, functional architecture, requirements, test scope, model credibility, and systems-of-systems governance. Traceability is only meaningful when a requirement's subject and operational boundary are unambiguous. A verification pass within the SoI does not automatically validate the parent mission.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Reference chapters for lifecycle, needs, requirements, design, technical management, integration and V&V.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Breadth-first conceptual encyclopedia and pointers to further references.

**Expanded tutorial:** [System boundaries, ownership and interfaces](../deep-dives/01-system-boundaries-and-interfaces.md)


## Technical analysis: boundaries determine both reliability and accountability

The system of interest (SoI) is the entity about which an engineering decision makes claims. Its boundary is an analytical and governance choice: which components, people, services, environmental conditions, and support functions are included in requirements and evidence? Declaring an external dependency out of scope does not make its effect disappear from delivered mission performance.

Suppose a vehicle subsystem operates successfully on **99%** of mission attempts when it receives valid dispatch data, but the dispatch service is available on only **95%** of attempts. If those events are independent under the same mission definition, end-to-end success is `0.99 × 0.95 = 0.9405`, or **94.05%**, not 99%. The calculation must not be used with dependent events without conditioning on common hazards. A narrow SoI boundary can report high component reliability while concealing degraded user outcomes.

**Evidence boundary.** Document the external dependency, accountable owner, interface promise, and observed success denominator. Maintain separate component and mission claims. When the boundary moves, revalidate the metrics, hazards, verification responsibilities, and configuration baseline; numbers copied without their original boundary can become misleading.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Systems engineering spans design, realization, management, operations and retirement of systems. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.1 Technical Planning](https://www.nasa.gov/reference/6-1-technical-planning/) · *scope-supported interpretation*.
- **C2:** System boundaries and mission operational needs affect who should be identified as a stakeholder and how success is defined. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.1 Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [SEBoK · Guide to the Systems Engineering Body of Knowledge, v2.14 (2026)](https://sebokwiki.org/wiki/Main_Page) — Community-maintained secondary guide; use its references for further research.



## Step 02 review studio — the system boundary changes the test you owe

A team declares the rider phone app to be its system of interest. That boundary is appropriate for testing app UI behavior; it is inadequate for concluding that a rider can reliably secure a shuttle. The full service includes dispatch, allocations, vehicle availability, operator procedures, notification networks, and external actors. The boundary chosen must match the claim made.

**Solved exercise:** the app passes 100% of its confirmation-screen tests, but some confirmations refer to reservations that were rolled back by the allocation database. Is the service-level booking claim satisfied? **No.** The app's display can be correct relative to its input and wrong relative to the underlying committed service state. Add end-to-end tests reconciling client state with a committed allocation and exercise retry/timeout conditions.

**Diagnostic:** identify the system's mission, owners, external exchanges, physical/operational domain, assumptions, failure modes, and authorized decisions. Explicit boundaries improve engineering reasoning; artificially narrow boundaries can transfer unowned risks rather than eliminate them.

## Follow the knowledge

**Related concepts**

- [Boundaries, environment, and interfaces](boundaries-and-interfaces.md)
- [Stakeholders, needs, and value](stakeholders-and-needs.md)
- [Concept of operations and scenarios](conops-and-scenarios.md)
- [System of systems and constituent independence](sos-characteristics.md)

**Explore in the 240-chapter textbooks**

- [Book 1, Chapter 1: Chapter 1 — What, exactly, is the system?](../B1/chapters/01-what-is-the-system.md)
- [Book 6, Chapter 1: Book 6 · Chapter 1: Framing before solutions](../B6/chapters/01-reopen-the-problem-and-audit-the-incumbent-baseline.md)
- [Book 20, Chapter 1: Week 01 · Management of Complex Systems · Chapter 01 — Complex problem situations, systems theory, and receiving review](../B20/chapters/01.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

