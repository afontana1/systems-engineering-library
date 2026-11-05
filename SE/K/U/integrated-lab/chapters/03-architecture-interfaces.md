# L03 · Architecture, interfaces, and model contracts

**Learning time:** 4–6 hours. **Gate:** Preliminary architecture review. **Prior reading:** [F05 — software architecture](../../flagships/F05-software-intensive-architecture.md).

## Allocate responsibility before you choose technology

The Northstar sandbox separates `SyntheticDemand`, `RequestLedger`, `Dispatcher`, `AuditLogger`, and `AssuranceReviewer`. The [interface register](../data/interfaces.csv) documents who produces and consumes a value, its schema, required invariants, and what happens when the contract is broken. This functional decomposition is more defensible than starting with microservices or database products: it tells you where correctness obligations live.

The `Request` data contract has six fields: a stable identifier, arrival time in minutes, fictional origin and destination, passenger count, and delivery key. The parser only accepts one passenger, finite nonnegative time, and distinct endpoints. The **scheduler contract** accepts validated requests and a configuration with positive fleet size and trip duration; it returns a list of assignment records and metrics. It does not emit physical commands or coordinate with vehicles. A response `completed` means “scheduled to finish within the *model* horizon,” not a record of real transportation.

## State and invariant reasoning

Represent a request as `received → validated → deduplicated → scheduled/completed` or `unserved_capacity`. An invalid input instead transitions to `rejected_input`, although the teaching code represents this with an exception before scheduling. A repeated identical delivery does **not** create a second request state. The main safety-relevant model invariant is: **for each vehicle, assignment intervals must not overlap**.

For two assignments with half-open service intervals `[s1,f1)` and `[s2,f2)`, if assignment 1 precedes assignment 2, require `f1 ≤ s2`. Half-open endpoints permit an assignment to begin at the moment another one ends. A heap ordered by the earliest free vehicle is enough to maintain the invariant in this single-threaded toy. An implementation with asynchronous workers would need atomic allocation or locking, and tests that exercise races.

## Architecture tradeoffs

The ledger is in-memory and produces a single-run hash of the audit summary. That hash detects certain output changes but is not a signed, tamper-resistant operational record; a SHA-256 digest alone supplies neither authenticated provenance nor durable persistence. The integration question is whether the interfaces preserve semantic meaning across changes—not merely whether JSON is well formed.

For example, suppose a new field `accessibility_support_required` is introduced. A backwards-compatible parser might treat its absence as false; but such a default could hide critical user needs. The correct architecture decision requires a stakeholder/assurance review, a schema version change, and tests for missing, malformed and true values. The reference design chooses rejection for unsupported passenger counts because silent accommodation would be worse.

## Engineering activity

1. Draw the dataflow and mark trust boundaries. Make a separate sequence diagram for exact duplicate and conflicting duplicate events.
2. Locate `deduplicate` and `dispatch` in [northstar.py](../src/northstar.py). Write preconditions, postconditions, invariants, and one failure outcome for each function.
3. Perform a change-impact walk for [CR-001](../data/change-requests.csv), support groups of two. List which interface, algorithm, metrics, requirements, and tests change and which cannot stay valid unchanged.
4. Write an interface-control rule defining version ownership, payload units, and rejection behavior. Check whether your rule handles stale deliveries.

## Knowledge check and explained answer

**Question.** Why is “exactly once delivery” not a property this prototype establishes?

<details><summary>Show explanation</summary>

The ledger shows idempotent treatment of exact repeated messages in one in-memory run. It does not guarantee network delivery, crash recovery, distributed transactions, ordering, or persistence. The more precise claim is **at-most-one unique processed request per accepted identifier in this single-run model**, conditional on payload equality.

</details>

**Gate evidence:** component responsibility table, interface-control document, state/invariant diagram, and a change-impact list with at least three new tests.
