# Object-oriented domain models and responsibilities

**Reference entry · MBSE and software-intensive systems · Expanded reference**

## Definition and diagnostic distinction

An **object-oriented domain model** represents concepts with identities, state, behavior, and responsibilities; it is not a database table design disguised as a class diagram. The central question is “who has enough knowledge and authority to guarantee this invariant?” rather than “which class should contain this method?” Analysis models capture domain meaning; design models distribute responsibility across executable components and persistence boundaries.

## Theory: invariants, contracts, and concurrency

An **invariant** is a predicate that must hold in every permitted stable state. A **precondition** describes when an operation may execute; a **postcondition** describes what it guarantees if its precondition holds. Suppose a vehicle can hold at most one active dispatch assignment: `count(activeAssignments(vehicle)) <= 1`. Placing the invariant in a screen controller is unsafe because another API or asynchronous worker can bypass it. The domain or transaction boundary must enforce it independently of presentation paths.

Class responsibility follows cohesion and ownership of state transitions. A `Trip` may own lifecycle transitions, a `DispatchPolicy` may rank candidates, and an `AssignmentService` may coordinate atomic reservation. Interfaces should expose stable contracts while hiding internal storage details. Concurrent commands create race conditions: two dispatchers can both read “free” and assign the same vehicle unless a serializable constraint, compare-and-swap, or equivalent coordination mechanism prevents conflict.

## Worked example: an invariant under contention

Two requests arrive within 5 ms. Both workers read vehicle V7 as available and attempt assignment. Without coordination, both operations succeed in local memory. With a version counter starting at 18, worker A performs `UPDATE vehicle SET assigned=R1, version=19 WHERE version=18`; worker B's update using version 18 affects zero rows and must retry. The operation preserves the single-assignment invariant provided the check and update are atomic in the authoritative store. A retry strategy must also avoid starvation and duplicate downstream notifications.

## Engineering use and evidence

Identify domain events, invariants, failure states, transaction boundaries, and idempotency expectations before choosing class relationships. Express contracts in testable language and add adversarial concurrent tests, not just happy-path sequence diagrams. Design review should examine ownership of time, identity, and recovery: who decides that a timed-out assignment is genuinely released, and how do replicas converge afterward?

## Limitations and connections

Object-oriented decomposition is not always the best abstraction for dataflow, numerical computation, or embedded control. Shared mutable state and distributed partial failure can defeat an apparently elegant class structure. Connect this topic to **state-based architecture**, **software quality**, **interfaces**, and **verification evidence**.

## Technical analysis: invariants under concurrent decisions

An object's responsibility is not simply the methods listed in a class. It is the state and invariants the component alone can change atomically, plus the events it must communicate to others. In distributed systems, object-local correctness does not imply global consistency unless shared invariants have an explicit owner or coordination protocol.

Suppose two dispatch workers simultaneously read **one available vehicle** and each decides to assign it. Without an atomic reservation, both may report success even though the resource cannot serve two conflicting trips. A reservation transition should be conditional: `UPDATE vehicle SET status='reserved' WHERE id=... AND status='free'`, followed by confirmation that **exactly one row** was changed. A unique assignment constraint and idempotent request key provide complementary protection against retries and duplicate events.

**Evidence boundary.** Test races, partial network failures, replay, and database recovery. A transaction can protect a local state transition yet fail to make an external actuator action atomic. Document the consistency model, the handling of unknown completion status, and whether compensation is safe. Do not infer distributed exactly-once execution from a nominal unit test.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Trustworthiness principles apply throughout the system life cycle, including component interaction. **Evidence:** [NIST — SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022), System security engineering concepts, activities, tasks, and trustworthiness principles](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) · *scope-supported interpretation*.
- **C2:** Software engineering guidance covers architecture and configuration of releases, not just standalone code units. **Evidence:** [NASA — NASA-HDBK-2203 Software Engineering and Assurance Handbook, Software planning, configuration, assurance and product evidence (see software lifecycle topics)](https://swehb.nasa.gov/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) — System-level security and trustworthiness engineering.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.


## Step 02 review exercise: put invariants where they can be enforced

In a fictional reservation service, a `Dispatcher` requests an assignment, a `Reservation` stores lifecycle state, and a `WorkerPool` owns the allocation constraint. The invariant **one active reservation per worker** should not depend on each user-interface client performing a `search-before-create` check. Two clients can both observe an available worker and then both insert. At the persistence boundary, use an atomic transaction and a database uniqueness constraint scoped to active reservations; retry behavior must distinguish a safe duplicate request from a new conflicting request.

Responsibilities follow invariants and information ownership. A presentation class should not become the sole authority on allocation when background jobs and APIs can bypass it. Separate stable domain identities from serialization format, distinguish commands from events, and document who transitions each state. Pattern names do not automatically improve design quality.

**Exercise (answer).** If two concurrent requests both read `active_count = 0`, a subsequent pair of inserts can violate the invariant. A partial unique index on `(worker_id)` for active records rejects one insert. The application must then return a controlled conflict or retry using a different worker, without accidentally repeating external side effects.

## Follow the knowledge

**Related concepts**

- [Software quality attributes and architectural tactics](software-quality-attributes.md)
- [Interface control and integration contracts](interface-control.md)
- [Functional, logical, and physical architecture: preserving intent across realization](functional-vs-physical.md)
- [Verification cross-reference matrices and test design](verification-matrix.md)

**Go deeper in the 240-chapter textbooks**

- [Book 4, Chapter 04: Book IV · Chapter 4: Class discovery turns language into relationships](../B4/chapters/04-discover-candidate-classes-and-build-the-stat.md)
- [Book 4, Chapter 07: Book IV · Chapter 7: Design is the distribution of responsibility](../B4/chapters/07-assign-responsibilities-and-build-the-static-.md)
- [Book 4, Chapter 10: Book IV · Chapter 10: Constraints turn informal rules into testable predicates](../B4/chapters/10-express-precise-constraints-with-ocl-and-exec.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
