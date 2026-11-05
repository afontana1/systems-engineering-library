# Advanced Workshop · State Machines, Invariants, and Idempotent Commands

*Book 4 · Week 6 · state transitions · transaction boundaries · exactly-once effects · invariants*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-state.md). The assessed course obligations remain in [the curriculum](../../../C/P1/EN605704.html).

## 1. What a state diagram really promises

A UML state machine is more than a drawing of arrows. It defines which events the system may accept in a particular condition, what changes as a consequence, and which states must never occur. Consider a fictional Northstar reservation: `REQUESTED → HELD → CONFIRMED → BOARDED → COMPLETED`, with cancellation possible before boarding. If a lost network acknowledgement causes the client to submit the same booking request twice, a diagram with happy-path states alone does not prevent two capacity holds. The *implementation* must uphold the invariant that one logical request has at most one live reservation.

An **invariant** is a predicate required to remain true across all reachable states. In this case: (i) confirmed holds never exceed physical capacity; (ii) each stable idempotency key maps to at most one logical booking outcome; (iii) a completed trip cannot be cancelled retroactively. The state machine describes a behavioral obligation; a transaction boundary determines whether concurrent execution can violate it. In UML terminology guards constrain transitions, entry/exit behaviors respond to events, and composite states can factor complex behaviors. In executable design we must also identify *who serializes competing events*.

A useful design separates **command acceptance** from **state transition**. The customer-facing API may accept an HTTP request and return a response, while the domain object accepts an event only if the transition is valid. A timeout does not prove that a command failed. It may have committed before the acknowledgement was lost. That ambiguity is precisely why the caller needs a stable request identifier and why the service should preserve the committed outcome against a repeat submission.

## 2. A constrained transition relation

Let the reservation state space be \(S=\{R,H,C,B,D,X\}\), meaning requested, held, confirmed, boarded, done, and cancelled. Let \(T\subseteq S\times E\times S\) be the permitted event relation. For a state \(s\) and event \(e\), a transition is admissible only when both \((s,e,s')\in T\) and its guard evaluates true. For example, `confirm` from `HELD` is allowed only if the hold has not expired. `cancel` from `BOARDED` is not allowed in this simplified design; actual operators might require a separate abort/emergency state.

A state diagram cannot by itself solve races among multiple services. Suppose two workers each read `capacity_used=7` for a vehicle of capacity 8, then each write `capacity_used=8`. Both customers can believe they have a seat. The postcondition of each local method looks fine, while the global invariant is false. An appropriate database transaction can atomically condition the increment on `capacity_used < capacity`, or a single sequencer can own the allocation operation. A version-number check prevents *lost updates*, but the specific storage consistency model must be documented.

## 3. Worked case: duplicate booking and lost acknowledgement

Northstar accepts key `req-17` when one place remains. The commit succeeds but its acknowledgement is lost. The client retries with the same key. A naïve procedure checks capacity again and either creates a duplicate or returns “full,” misleading the original customer. The guarded procedure first looks up the key and returns the original committed outcome; only unseen keys attempt a new allocation. The instructional `BookingLedger` model in the Python lab treats this as one atomic operation within a single process. For capacity one, `book('A'), book('A'), book('B')` yields `CONFIRMED, CONFIRMED, REJECTED` and one accepted allocation.

This is **idempotency of the externally visible effect**, not an unconditional guarantee of exactly-once message delivery. Messages may arrive multiple times; the service keeps the side effect logically once. If request keys expire, or different keys are used for one logical intent, even a correct ledger can duplicate reservations. If the key registry and reservation database are stored separately without a transaction, a crash between writes can reintroduce inconsistency. State the time horizon, key namespace, and durability assumption as part of the interface contract.

## 4. When the implementation is not a state machine

Many class diagrams declare `Reservation.status: String` and assume the behavior is thereby modeled. But an unconstrained setter allows impossible transitions such as `REQUESTED → COMPLETED`. Prefer a small domain method that checks both the current state and the event, rejects illegal transitions, and records a result suitable for verification. The state model should include negative tests: retry after commit; cancel twice; receive completion before boarding; race between cancellation and boarding; stale writer version.

An important design distinction is **safety** (“never double allocate”) versus **liveness** (“an accepted reservation eventually receives a terminal disposition”). A design that rejects every booking trivially satisfies the first property but fails the service mission. An effective review asks about both, including what occurs under partition, data recovery, and operator intervention.

## 5. Connecting analysis models to code

The course's use cases identify success guarantees and alternate flows. Sequence diagrams identify collaborators and message timing. The state machine identifies allowed transitions, while class responsibilities determine which component owns the invariant. Finally, tests link each invariant to an executable witness. Do not merge these representations into a single picture: they answer different questions, and disagreements among them are often the most valuable defects discovered during design.

## Worked problem set — attempt before revealing solutions

### Problem 1

A vehicle has capacity 8 and 7 assigned seats. Two workers both read 7 then independently add 1. What failure occurs, and which atomic operation repairs it?

<details><summary>Show solution 1</summary>

Both may confirm the eighth seat, making the physical allocation 9 despite a stored count of 8. Use an atomic conditional allocation tied to the reservation commit (or an equivalent single-writer rule). A post-hoc count check is too late.

</details>

### Problem 2

A booking commits, the response is lost, and the client retries. What does a robust command return?

<details><summary>Show solution 2</summary>

It returns the durable outcome associated with the same idempotency key, not a new booking. This requires a stable key namespace and a storage operation that preserves key-to-outcome consistency.

</details>

### Problem 3

A process reads version 3 and attempts to cancel after another process has confirmed version 4. What should optimistic concurrency do?

<details><summary>Show solution 3</summary>

Reject the stale write as a conflict. The caller must re-read the current state and decide whether cancellation is still valid; retrying the same write blindly is unsafe.

</details>

### Problem 4

Why does a ban on double allocation not imply a good service?

<details><summary>Show solution 4</summary>

It is a safety property only. A service that refuses every request meets it while violating liveness and mission outcomes. Define successful-progress obligations separately.

</details>

## Independent transfer to the Northstar case

Start with capacity two and a request fixture containing retries and cancellations. Write a transition table, identify all forbidden arcs, then run duplicate keys against `book4.py`. Introduce two conceptual writers reading the same stale version and show why a version check prevents lost updates. Change the key-retention assumption and document which new failure becomes possible. Submit a UML statechart, an invariant table, five negative tests, and a short review disposition.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-state.md) · [Python source](book4.py) · [Experiment dataset](book4-requests.csv) · [Interactive workbench](WORKBENCH.html).
