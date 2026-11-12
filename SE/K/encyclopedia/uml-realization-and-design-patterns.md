# UML realization and design patterns: from scenarios to robust software structure

**Reference entry · Object-oriented design and software-intensive systems · Worked technical treatment**

## Realize behavior, not just a class diagram

**Use-case realization** translates an external actor's goal into collaborations among internal objects. A UML sequence diagram can describe an interaction trace; a class diagram can show responsibilities and associations; a state machine can constrain legal lifecycle transitions. None of these is sufficient alone. A design is credible when the structural model, operation contracts, and expected error scenarios agree.

For a mobility reservation, the actor calls `ReservationService.reserve(requestId, passenger, route)`. The service checks identity, asks `AvailabilityPolicy` for eligible resources, attempts an atomic reservation through `ReservationRepository`, and returns a documented success or rejection. `Reservation` owns the domain state; a database constraint must still enforce uniqueness under concurrent requests. Simply drawing a `getAvailableWorker()` call before an `insert()` does not make the behavior atomic.

## Separate responsibilities by reason to change

A boundary object translates external requests; a controller coordinates one use case; domain entities enforce business invariants; infrastructure adapters perform storage and messaging. These are roles, not rigid UML stereotypes that must correspond one-to-one to classes. The guiding question is: **which change should force this element to change?** If an entity knows API transport details, database schema and presentation formatting, its responsibilities are probably tangled.

A useful class model might include `Reservation(id, workerId, status, requestKey)`, `AllocationPolicy`, `ReservationRepository` and `ReservationService`. Capture the multiplicity and invariant “at most one active reservation per worker” and clarify whether rejected, expired or pending reservations count.

## Design patterns are tradeoffs

The **Strategy** pattern makes selection algorithms replaceable without changing the reservation entity. The **Repository** pattern abstracts persistence access but can hide critical transaction boundaries if used carelessly. A **State** pattern can make legal transitions explicit but may overcomplicate a small finite state machine. The goal is not to maximize recognizable patterns: it is to reduce change impact while preserving correctness and comprehensibility.

Apply a pattern only after identifying a source of variation and testing the resulting dependency structure. For example, `AllocationPolicy` might support a nearest-worker strategy and a fairness-aware strategy, but both must obey the same atomic repository constraint. A change in algorithm cannot be allowed to bypass the safety invariant.

## Worked realization and contract

Consider `reserve(k,w)`. A possible contract is:

- **Precondition:** \(k\) is a valid idempotency key; \(w\) is an eligible worker for the route and time window.
- **Postcondition on success:** there exists exactly one active reservation with key \(k\), owned by \(w\); the response identifies it.
- **Postcondition on conflict:** no additional active reservation for \(w\) is created; the request returns a typed conflict result.
- **Invariant:** for every worker \(w\), \(\sum_r \mathbf{1}[r.\mathrm{worker}=w\land r.\mathrm{active}]\leq1\).

The invariant is a specification, not a concurrent correctness proof. It needs atomic enforcement and tests for duplicate requests, lost acknowledgements, retries and failures between database and message publication. An illustrative local SQLite constraint is explored in [transactional concurrency and assurance](../methods/transactional-concurrency-and-assurance.md).

## Trace the use case to testable evidence

Write three paths: normal allocation, no eligible worker, and two simultaneous attempts on the same worker. For each path record the participating objects, critical message, expected state, and observable evidence. Then change the dispatch policy: a good design keeps reservation state invariants and API contracts stable, even if a ranking algorithm changes. If not, the advertised encapsulation may be cosmetic.

## Pitfalls and source context

Watch for diagram-only designs, hidden global mutable state, service classes that own every responsibility, state transitions with unspecified failure semantics, and untested asynchronous retries. A design pattern can be locally elegant while making distributed behavior harder to prove.

- [OMG UML specification](https://www.omg.org/spec/UML/) — normative language definition for UML structure and behavior.
- [OMG OCL specification](https://www.omg.org/spec/OCL/) — formal constraints and operation contracts.
- Related: [object responsibilities](object-responsibilities.md); [UML/OCL contracts](../methods/uml-ocl-software-contracts.md); [software quality attributes](software-quality-attributes.md).

*Scope:* The example is a design teaching case, not an OCL-interpreter-validated or production-certified implementation.

## Step 02 deeper treatment: realize a reservation use case through enforceable contracts

**Worked example:** A `ReserveWorker` use case receives a passenger request, selects a vehicle, and produces a reservation. A sequence diagram might show `Controller → Policy → ReservationRepository → EventPublisher`. That diagram remains incomplete until we identify (a) the transaction boundary, (b) the invariant that a worker cannot have two active allocations, (c) the authorized rejection behaviors, and (d) the meaning of retries.

Define the precondition as “the request is syntactically valid and authorized”; availability should **not** be a precondition if it can change concurrently after evaluation. Define a postcondition with two disjoint outcomes: either one durable assignment exists for the request and its worker was not assigned elsewhere at commit, or no assignment is created and an explicit rejection is recorded. A uniqueness constraint in durable storage prevents two concurrent request handlers from violating the invariant even if both earlier read “available.” A `Policy` object should not be granted direct access to database mutations solely for convenience.

**Exercise:** change the use case to pooled ride-sharing. Which invariant must change? Replace at-most-one-active-assignment with a capacity constraint over active passenger seats and define the relevant concurrency unit. A design pattern name such as “Strategy” does not supply the missing domain semantics. Use the [OMG UML specification](https://www.omg.org/spec/UML/2.5.1) to distinguish diagram conventions from application-specific requirements.
