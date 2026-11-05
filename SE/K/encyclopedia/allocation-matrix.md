# Allocation, coverage, and design responsibility

**Reference entry · Concept, design, integration and test · Expanded reference**

## Definition and diagnostic distinction

An **allocation** assigns responsibility for a function, requirement, performance budget, hazard control, or interface to a design element or organization. A matrix is one visualization of these typed relationships. It is not sufficient to put an `X` where a function meets a component: the assignment must include what is allocated, how performance is budgeted, and which actor is accountable for interfaces and emergent behavior.

## Theory: decomposition and feasibility

Represent functions as a set `F`, components as `C`, and allocation as a relation `A ⊆ F × C`. Some functions need several constituents; some allocations are alternatives, not simultaneous commitments. Feasibility requires checking coupled capacity constraints. For example, if task `i` requires processor time `c_i` every period `T_i`, a necessary utilization condition for a single processor is `Σ(c_i/T_i) <= 1` under idealized assumptions. This does not establish schedulability when tasks have blocking, jitter, priority interactions, or deadlines shorter than periods.

Requirements also flow downward through **derivation** rather than simple copying. A system response-time requirement may be allocated as budgets for detection, communication, computation, actuation, and margin. If the budgets sum above the system limit, the allocation is impossible before implementation begins. If each component is verified independently but shared clocks, network congestion, and failures are ignored, system behavior remains unverified.

## Worked example: response-budget allocation

An emergency stop must begin actuation within 200 ms. An initial budget assigns 35 ms sensing, 45 ms communications, 95 ms computation, and 20 ms actuation, totaling 195 ms. That leaves only 5 ms for synchronization, queuing, and uncertainty—a fragile design. Profiling shows the gateway can delay messages 25 ms under peak traffic; the **worst-case estimated total** rises to 220 ms. The allocation fails. Moving the stop logic nearer the actuator or reserving network capacity may restore feasibility, but both changes affect the system architecture and require new evidence.

## Engineering use and evidence

Maintain allocation records with source obligation, destination component, derived budget, owner, rationale, assumptions, and verification method. Check unallocated requirements, multiply allocated functions with no arbitration rule, budgets that exceed parent limits, and orphaned interface responsibilities. Review the allocation in operational and degraded modes; responsibility during a handoff can differ from responsibility during normal operation.

## Limitations and connections

A complete matrix can conceal an infeasible architecture or sociotechnical gap. Allocation is a design hypothesis until timing, capacity, fault behavior, and ownership are demonstrated. Connect this topic to **functional versus physical architecture**, **interface control**, **requirements traceability**, and **integration strategy**.

## Technical analysis: allocation is a constrained mapping

An allocation matrix is a relation `A[i,j]` between required functions `f_i` and implementation elements `e_j`, not automatically a one-to-one assignment. A function can be jointly provided by a human, software service, and physical actuator. Distinguish **primary responsibility**, supporting resources, supervision, and the authority to resolve conflicting commands; marking all four with the same checkmark hides potential gaps.

Suppose three functions require peak electrical power of **200 W**, **150 W**, and **120 W**. Adding all peaks gives **470 W**. But a mode analysis shows the first two can coexist while the third is prohibited in that operating mode; the peak concurrent sum is **350 W** (before conversion inefficiency and reserve). Conversely, simply choosing the largest single number, **200 W**, would violate the mode-1 budget. Formally, with binary mode activations `x_i(m)`, the power budget requires `max_m Σ_i x_i(m) P_i / η_i ≤ P_available`, with appropriate unit definitions and conversion efficiencies.

**Evidence boundary.** Capture mode assumptions, independence and common-cause failures, performance budgets, explicit interfaces, and verification responsibility. Treat the matrix as a queryable view derived from a versioned architecture model. A function assigned to two elements may be intentional redundancy, not two independent means of meeting a hazard objective; separation of power, control, and maintenance must be assessed before calling it fault tolerant.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Logical decomposition derives functions and associated requirements before realizing physical architecture. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.3 Logical Decomposition](https://www.nasa.gov/reference/4-0-system-design-processes/) · *direct guidance*.
- **C2:** Design solution definition compares alternative physical implementations of logical requirements. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.4 Design Solution Definition](https://www.nasa.gov/reference/4-4-design-solution-definition/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.

## Follow the knowledge

**Related concepts**

- [Functional, logical, and physical architecture: preserving intent across realization](functional-vs-physical.md)
- [Requirements: precise obligations, not persuasive sentences](good-requirements.md)
- [Interface control and integration contracts](interface-control.md)
- [Requirements traceability: a typed graph of engineering claims](traceability-graph.md)

**Go deeper in the 240-chapter textbooks**

- [Book 3, Chapter 07: Book III · Chapter 7: Function allocation is a hypothesis](../B3/chapters/07-logical-architecture-functional-allocation-de.md)
- [Book 7, Chapter 03: Book 7 · Chapter 3: Allocation and derived requirements](../B7/chapters/03-allocate-requirements-and-define-component-functions.md)
- [Book 9, Chapter 06: Book 9 · Chapter 06 — Specify interfaces, exchanges, allocations, ownership, and model-based change exposure](../B9/chapters/06-specify-interfaces-exchanges-allocations-ownership-and-model-based-c.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
