# Functional, logical, and physical architecture: preserving intent across realization

**Reference entry · Architecture and design · Expanded reference**

## Three complementary views

A **functional architecture** describes transformations and behaviors needed to achieve mission outcomes: accept request, allocate capacity, dispatch vehicle, board passenger, handle exception. A **logical architecture** groups responsibilities into solution-independent roles, services, or collaborating components. A **physical architecture** identifies the actual hardware, software, human roles, networks, and facilities that realize those responsibilities. The views answer different questions; none is simply the next prettier diagram.

Functions are not synonymous with components. A single physical component may realize several functions; one function may be distributed across several components. Premature one-to-one mapping eliminates useful alternatives and may hide shared dependencies.

## Allocation as a constraint problem

Let functions be **F = {f₁,…,fₘ}**, candidate elements be **E = {e₁,…,eₙ}**, and **Aᵢⱼ = 1** indicate that element j owns or participates in function i. A baseline allocation must define which functions need a unique accountable owner, which may be replicated, and how interactions and derived requirements are assigned. A row with no supporting element is a gap; multiple owners may be intentional redundancy or an unresolved responsibility conflict.

Architectural feasibility also requires more than an allocation matrix. Each element has capacity and other constraints. If task k consumes resource **rₖ** and element j has effective capacity **Cⱼ**, then the assigned load must satisfy **Σₖ Aₖⱼ rₖ ≤ Cⱼ**, after accounting for contention, peak scenarios, degradation, and engineering margin. Static budget compliance cannot prove timing behavior in a queueing or networked system.

## Worked example: redundancy and hidden coupling

A dispatch design proposes two redundant servers, each independently available 98% of the relevant operating time. If the server failures are independent and either can handle full load, parallel availability is **1 − (1 − 0.98)² = 99.96%**. This apparent improvement is invalid if both servers share an unprotected power feed or identity service. With a common service required by both, the system availability is bounded by that service's availability regardless of the number of replica servers.

The **functional** question is whether dispatch continues after a fault; the **logical** question is which services and failover rules provide that behavior; the **physical** question is whether deployed servers, power, networking, software versions, and operators truly avoid common failure. All three views are needed to support a high-availability claim.

## Architecture reasoning sequence

1. Extract mission functions and failure responses from scenarios and requirements.
2. Specify flows of matter, energy, data, and control with units and timing.
3. Explore multiple logical decompositions before locking in technology.
4. Allocate functions to candidate physical elements; identify interfaces and ownership.
5. Analyze mass, power, latency, throughput, maintainability, security, and life-cycle cost together.
6. Revisit operational scenarios after fault or degradation to test whether the proposed allocation remains coherent.
7. Preserve the evidence linking each allocation decision to its assumptions and trade study.

## Common misconceptions

A block diagram is not an argument that the architecture works. An allocation that covers every function is not necessarily feasible under simultaneous loading. “Redundancy” can increase maintenance and configuration complexity, and it can fail to improve resilience when replicas share vulnerabilities. Architecture is an evolving set of constrained, testable hypotheses—not merely a picture and not a fixed one-way progression.

## Connections

Architecture connects system boundaries, interfaces, model-based systems engineering, functional failure analysis, requirements refinement, reliability block diagrams, optimization, and verification planning. Digital-thread provenance helps keep the allocation claim attached to a specific configuration.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Reference chapters for lifecycle, needs, requirements, design, technical management, integration and V&V.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Breadth-first conceptual encyclopedia and pointers to further references.


## Technical analysis: refinement does not equal allocation

A **functional decomposition** divides desired behavior into transformations, controls, and information exchanges. A **physical architecture** assigns realized behavior to hardware, software, humans, and external services with interfaces. Multiple physical architectures can implement the same logical functions; this is the point of retaining the logical model while exploring alternatives.

A safety function requiring two independent confirmations is allocated to two electronic channels. If each channel has conditional mission failure probability **0.02** and failures are independent, the joint private-mode probability is `0.02² = 0.0004 = 0.04%`. But if both channels depend on the same controller with failure probability **0.01**, and private failures are conditionally independent when the controller survives, the actual top-event probability is `0.01 + 0.99(0.02²) = 0.010396 = 1.0396%`. The apparent physical redundancy did not create independent safety protection.

**Evidence boundary.** Keep logical traceability stable while tracking shared physical resources, common software, maintenance, and power dependencies. Physical replication is not automatically functional independence; verification needs a failure-mode argument for the selected architecture and operating environment.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Logical decomposition separates required behavior from candidate detailed design solutions. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.3 Logical Decomposition](https://www.nasa.gov/reference/4-0-system-design-processes/) · *direct guidance*.
- **C2:** Physical design alternatives are assessed against derived technical requirements. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.4 Design Solution Definition](https://www.nasa.gov/reference/4-4-design-solution-definition/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.



## Step 02 review studio — trace one function across a changed implementation

The function **validate booking eligibility** may initially run in a single dispatch server and later move to a separate service. Its responsibility and correctness conditions do not disappear when the physical/software allocation changes. A functional model describes *what transformation is required*; a physical model records *which components embody it*.

**Solved exercise:** the system splits eligibility and allocation services. Previously, an atomic database transaction checked rider eligibility and committed a vehicle assignment. Now the services exchange asynchronous events. Which engineering claim requires renewed attention? **The end-to-end consistency obligation**: eligibility may change before allocation commits, and retries may duplicate work. The team needs explicit event ordering, version and idempotency contracts, plus new integration evidence. Updating the component diagram alone is not enough.

**Review test:** every critical function should have inputs, outputs, failure transitions, a primary owner, allocated components, and verification evidence. Component tests show local behavior; functional mission threads expose missing cross-component responsibilities.

## Follow the knowledge

**Related concepts**

- [Allocation, coverage, and design responsibility](allocation-matrix.md)
- [Interface control and integration contracts](interface-control.md)
- [Requirements and acceptance criteria](good-requirements.md)
- [Trade studies, constraints, and sensitivity](engineering-trades.md)

**Explore in the 240-chapter textbooks**

- [Book 1, Chapter 5: Chapter 5 — Before the Boxes: Functional Architecture and System Behavior](../B1/chapters/05-functions-and-behavior.md)
- [Book 3, Chapter 7: Book III · Chapter 7: Function allocation is a hypothesis](../B3/chapters/07-logical-architecture-functional-allocation-de.md)
- [Book 7, Chapter 3: Book 7 · Chapter 3: Allocation and derived requirements](../B7/chapters/03-allocate-requirements-and-define-component-functions.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

