# D11 · Behavioral state machines and interface contracts

**Skill:** Prevent illegal transitions and define observable software behavior without mistaking a diagram for verification.
![Instructional diagram for 11 state machines contracts](../diagrams/05-software-states.svg)



## States and invariants

A trip request might move through `Requested → Assigned → EnRoute → Completed`, with alternative `Cancelled` and `Failed` states. A finite-state model is an abstraction of allowed system behavior. Transitions have events, guards, actions and postconditions. Invariants must hold in every reachable state: for example, a `Completed` trip has exactly one final charge record, and an unassigned trip cannot have a live driver instruction.

A transition table makes the rules auditable:

| Current | Event | Guard | Next | Action |
|---|---|---|---|---|
| Requested | assign | eligible vehicle available | Assigned | reserve vehicle |
| Assigned | start | driver authenticated | EnRoute | record departure |
| EnRoute | arrive | destination confirmed | Completed | close trip |
| Requested/Assigned | cancel | policy permits | Cancelled | release reservation |

The same event in a different state may be rejected, ignored or handled idempotently; decide deliberately. “Happy path only” state machines hide most integration failures.

## Concurrency and retries

Distributed calls can be delayed, duplicated or reordered. If an assignment command is retried, the same trip must not allocate two vehicles. Use an idempotency key tied to the logical operation, transactional reservation where possible, and a reconciliation path when responses are lost. Exactly-once delivery is not a general property of the network; design behavior so at-least-once execution is safe where appropriate.

## Model checking mindset

Check reachability (can Completed be reached?), safety (can two trips claim the same exclusive vehicle?), and liveness under fair conditions (can a valid request eventually progress or terminate?). A unit test of one method doesn't prove those properties across concurrency and failure states. Derive transition-based test cases, including forbidden transitions and race conditions.

## Practice

**Question:** The same `assign(trip42)` request arrives twice after a timeout. What response protects the booking state?

<details><summary>Solution</summary>

Recognize the identical logical operation via its stable idempotency key and return or reconstruct the existing outcome rather than creating a second reservation. Still verify the underlying storage transaction and timeout-reconciliation rules.

</details>

**Transfer artifact:** State-transition table, invariant list, negative tests and duplicate/reorder fault-injection scenarios. See [object responsibilities](../../encyclopedia/object-responsibilities.md) and [interface control](../../encyclopedia/interface-control.md).
