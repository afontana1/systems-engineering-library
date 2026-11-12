# UML and OCL contracts for software model consistency

*Engineering method guide · Class models, invariants, preconditions, postconditions, invalid states, and executable checks · Phase 3*

**Learning outcome.** Interpret a UML-like domain model, write representative Object Constraint Language (OCL) invariants and operation conditions, create equivalent small-scale executable checks, exhibit counterexamples, and distinguish static-model consistency from implementation correctness. This chapter illustrates the standard's concepts and uses **hand-authored OCL**, not a certified OCL toolchain.

**Prerequisites:** [Model, language, method and tool semantics](../encyclopedia/model-language-method-tool.md), [software lifecycle evidence](../encyclopedia/software-lifecycle-evidence.md), [MBSE behavioral contracts](mbse-behavioral-contracts.md), and [software quality attributes](../encyclopedia/software-quality-attributes.md).

## 1. Why a diagram alone is not a specification

A UML class diagram may show `Reservation` with `id : String`, `status : Status`, and an optional `worker : Worker[0..1]`. Multiplicity limits what *one* reservation may reference, but it does not ensure uniqueness of IDs across objects, forbid a worker being allocated to two active reservations, or say when an assignment is legal. These are **cross-object and lifecycle constraints**. A student should distinguish:

- **Structure:** classes, attributes, type relationships and multiplicities.
- **Invariants:** statements intended to hold in every valid system state.
- **Operation contracts:** permitted inputs, preconditions, and required postconditions.
- **Behavior:** state transitions and event ordering; temporal progress or liveness may require a different formalism.
- **Persistence constraints:** guarantees that must remain enforced across transactions, restarts, concurrent requests and the data store.

OCL provides a declarative language for expressions over typed object models. An OCL constraint is not, by itself, an automatic database constraint, concurrency lock, executable state-machine guard, or formal proof that the deployed system meets a requirement. Its exact typing and null semantics depend on the modeled metamodel and a conforming OCL tool.

## 2. Define a minimal typed domain and its assumptions

Consider a fictional dispatch allocation domain:

| Element | Meaning | Stated assumption |
|---|---|---|
| `Reservation.id : String` | Stable identifier | Nonempty and unique in the observed repository scope |
| `Reservation.status : Status` | `Pending`, `Active`, `Closed` | Exactly one enumeration value |
| `Reservation.worker : Worker[0..1]` | Optional allocated worker | Present **only** for `Active` reservations |
| `Worker.id : String` | Stable worker identity | Unique worker objects are identified consistently across stores |
| `DispatchService.activate(r,w)` | Activate a pending request | Does not change unrelated reservations |

This model intentionally makes a simplified policy choice: a `Closed` reservation releases its worker immediately. Real operations may require transitional states, soft holds, audit history and delayed releases. That would require extending the model instead of silently weakening its invariants.

## 3. Express the invariants in readable OCL

The following expressions are **illustrative OCL 2.4-style syntax** to validate in a conforming environment with the `Reservation`, `Worker`, and `Status` classifier definitions above. They are not interpreted by the Python program below.

```ocl
context Reservation inv UniqueIdentifier:
    Reservation.allInstances()->isUnique(r | r.id)

context Reservation inv ActiveNeedsWorker:
    self.status = Status::Active implies
        not self.worker.oclIsUndefined()

context Reservation inv NonActiveHasNoWorker:
    self.status <> Status::Active implies
        self.worker.oclIsUndefined()

context Reservation inv WorkerAllocatedAtMostOnce:
    Reservation.allInstances()
        ->select(r | r.status = Status::Active)
        ->isUnique(r | r.worker)
```

Here `allInstances()` is interpreted over the population of objects in the model under evaluation, **not** automatically every object ever stored in every distributed database. If that population is incomplete, an apparently satisfied uniqueness expression may provide false assurance. Null and invalid OCL values must also be handled according to the language's evaluation rules; ordinary two-valued programming-logic intuition can be misleading.

An additional identifier rule can be expressed as an invariant with explicit type expectations: `self.id.size() > 0`, subject to the model declaring the `String` attribute mandatory and non-null. Identifiers should usually be normalized according to a defined policy if `"R-1"` and `" r-1 "` are intended to collide. A text-based identifier alone is not a concurrency mechanism.

## 4. Preconditions and postconditions specify an operation's obligation

An operation can be described as an OCL-style contract on a `Reservation` method (assuming a typed `Worker` parameter and appropriate object population):

```ocl
context Reservation::activate(w : Worker)
pre PendingAndWorkerFree:
    self.status = Status::Pending and
    Reservation.allInstances()->forAll(r | r.worker <> w)
post BecomesActive:
    self.status = Status::Active and self.worker = w
```

The precondition specifies when the caller may invoke the operation; the postcondition defines an obligation on the resulting state. It does **not** automatically enforce atomicity. Under two simultaneous requests, each thread could evaluate “worker free” before either commits and both might activate using the same worker. An implementation needs an actual transaction/unique constraint or another concurrency-safe allocation design. The OCL should be evaluated and refined using a modeling tool and the precise metamodel in a real project.

A better engineering question than “Does the diagram look reasonable?” is: *Which unacceptable states are representable, and what prevents the system from reaching them under concurrency, retries and partial failures?*

## 5. Make a concrete counterexample, then repair it

The [Python contract-audit example](code/ocl_contract_audit.py) checks JSON snapshots equivalent to **four simple policy statements**: IDs are nonempty and unique; `Active` reservations have workers; nonactive reservations have none; allocated workers are not duplicated. It also demonstrates a pure `activate` operation with explicit preconditions and poststate assertions. This is a pedagogical analogue of constraints, **not an OCL parser**.

| Input fixture | Expected finding | Engineering significance |
|---|---|---|
| [Valid snapshot](data/reservation-valid.json) | No invariant violations | A necessary, not sufficient, check |
| [Duplicate worker](data/reservation-duplicate-worker.json) | Same worker allocated twice | Resource exclusivity invariant broken |
| [Missing worker](data/reservation-missing-worker.json) | Active request has no worker | Lifecycle/association invariant broken |

The valid fixture has one active reservation `R-1` on worker `W-3`, one pending `R-2`, and one closed `R-3`. Activating `R-2` with free worker `W-8` yields two active reservations with distinct workers; the active count increases exactly once. An attempted second allocation of `W-3` is rejected before a new snapshot is committed. Run:

```sh
python3 SE/K/methods/code/ocl_contract_audit.py
```

The checker intentionally **cannot** prove absence of races, lock-order defects, unbounded event sequences, database transaction anomalies, or all possible state-machine behaviors. It only audits the represented finite snapshot and one explicit operation's transition. To test concurrency, combine contracts with transaction-level integration tests and the bounded state exploration described in [MBSE behavioral contracts](mbse-behavioral-contracts.md).

## 6. Connecting constraints to persistence

A student implementing this in a relational datastore should consider a schema with a non-null primary key on `reservation.id`, a constrained status enumeration, a nullable worker foreign key, and a database-level uniqueness/partial-index design that prevents two **Active** records from allocating the same worker. An application-only pre-insert `SELECT` is not adequate for concurrent allocations. The precise index syntax differs among database engines; do not assume all engines handle `NULL`, partial indexes or transaction isolation identically.

A more sophisticated distributed service must additionally address retries and idempotency, state-machine versioning, stale reads, and event delivery. The source of truth, consistency model and error behavior determine which assumptions the OCL-level specification captures. When UML terminology, API contracts and database semantics disagree, assign one authoritative system rule and document the refinements and exceptions.

For model-based engineering, trace each constraint to a stakeholder obligation (for example “A worker cannot execute two reservations simultaneously”), a design enforcement mechanism, an automated check, and evidence of correctness under an appropriate workload. A constraint without a tested enforcement point is a documented intention, not assurance.

## 7. Counterexamples, tests, and a student exercise

1. Draw the classes and association multiplicities implied by the domain table. Explain why `Worker[0..1]` alone does not guarantee exclusivity across reservations.
2. Write an invariant that forbids empty IDs, then decide how to normalize whitespace and casing.
3. Predict the output of the JSON audit for the two invalid fixtures before running the code.
4. Add an illegal `Closed` reservation with a worker to a new fixture; verify the tool catches it and explain the business-rule assumption.
5. Modify `activate` so it performs assignment without checking other workers; show the exact violation the snapshot audit exposes.
6. Design a concurrency test where two simultaneous activations target the same worker. Explain the datastore guarantee necessary to rule out the outcome.
7. Describe how to express a temporal rule (“every accepted request eventually completes or times out”) and why this is not merely a static invariant.

**Curriculum crosswalk:** [EN.605.704](../../C/P1/EN605704.md), [EN.645.631](../../C/P1/EN645631.md), [Book 3 ch 11](../B3/chapters/11-model-quality-queries-reports-change-impact-g.md), [Book 9 ch 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md), and [Book 3 ch 5](../B3/chapters/05-behavior-modeling-use-cases-activities-action.md).

## Primary technical references

- [OMG Object Constraint Language (OCL) v2.4](https://www.omg.org/spec/OCL/2.4). Normative language definition and separate typing/evaluation semantics.
- [OMG UML specification](https://www.omg.org/spec/UML/2.5.1). Modeling notation and metamodel context.
- [NASA-STD-7009B](https://standards.nasa.gov/node/263). Model V&V and intended-use credibility principles applicable by analogy; not an endorsement of software models.

*These are original synthetic examples, not certified UML/OCL implementations or operational requirements.*
