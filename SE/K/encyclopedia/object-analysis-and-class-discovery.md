# Object-oriented analysis: class discovery and responsibilities

**Reference entry · Object-oriented systems analysis, UML and software design**

## Start with behavior and domain language

Object-oriented analysis begins with stakeholder scenarios, invariants, boundaries and a domain vocabulary—not with drawing rectangles for every noun in a requirements paragraph. A **class** represents a cohesive concept with stable identity, state, behavior and meaningful rules. A role may be better expressed as an interface, a value as an immutable value object, and a changing fact as an event. A database table is not automatically a domain class; persistence concerns and domain behavior may have different boundaries.

For a Campus Mobility reservation service, a candidate glossary includes `Reservation`, `Passenger`, `Vehicle`, `Assignment` and `AvailabilityReport`. Ask what must remain true across events: one active assignment per reservation; one active reservation per worker at a time; assignments point to existing reservations and workers; historical reservations need not retain a live allocation. These invariants are more useful than a diagram that merely joins `Reservation` and `Vehicle` with a line.

## Worked realization of a request

Scenario: “A passenger requests a pickup, the dispatch policy chooses an available vehicle, and the service confirms or declines the request.” A plausible sequence is:

1. An application/controller receives a uniquely identified request and validates its authorization and input.
2. `ReservationService` reads an admissible, versioned availability snapshot.
3. `DispatchPolicy` evaluates feasible candidate vehicles; policy selection must not itself mutate reservation state.
4. A transactional repository attempts a reservation-and-assignment write, checking a uniqueness invariant at the storage boundary.
5. The response returns confirmation or a specific rejection, and an event log records the accepted transition.

The roles deliberately separate orchestration, domain policy and durable concurrency enforcement. A retry must not make a second assignment for an already accepted request. The analysis model should describe invariants and events before selecting ORM annotations, storage schema or framework-specific classes. See [UML realization](uml-realization-and-design-patterns.md) and [transactional concurrency](../methods/transactional-concurrency-and-assurance.md).

## Candidate-class triage

Use **CRC cards** (class, responsibilities, collaborators) or a role-responsibility table. A proposed `DispatchSystem` class responsible for every workflow is likely a “god object” with incompatible responsibilities. A `Timestamp` may be a value object rather than a full aggregate. Domain boundaries need explicit ownership of invariants: `Assignment` creation can be coordinated by a service but uniqueness must survive concurrent writes. Record candidate multiplicities (one-to-many, optional) and the cases that would falsify them.

## Tests from the model

Write executable acceptance examples independent of implementation: two requests racing for the same vehicle; duplicate delivery of one request; cancellation followed by reuse; stale availability; unauthorized assignment. Formalize the key state constraint as

\[
\forall w:\quad\bigl|\{a\mid a.\text{worker}=w\land a.\text{active}\}\bigr|\le1.
\]

This expression says **at most one active assignment per worker**, not “one assignment ever.” Confirm the domain assumptions: if pooled ride-sharing is supported, the constraint must be reframed around capacity rather than uniqueness.

## Exercise and check

A novice class diagram contains `Passenger`, `Vehicle`, `Location`, `Reservation`, `Trip`, and `AvailabilityReport`, all with public setters and no behavior. Choose a responsibility for each, identify which are values or entities, add the active-assignment invariant, and design two negative acceptance scenarios. A defensible answer explains *who* can authorize transitions, how stale reports are rejected and how transactionality preserves the invariant—not simply where arrows go.

## Caveats and references

- [OMG UML specification](https://www.omg.org/spec/UML/2.5.1) — UML notation and semantics.
- [OMG OCL specification](https://www.omg.org/spec/OCL/2.4) — constraint-expression language.

Related: [object responsibilities](object-responsibilities.md), [requirements](good-requirements.md), [software attributes](software-quality-attributes.md). This is a language-independent analysis method; it does not demonstrate conformance to a particular UML/OCL toolchain.
