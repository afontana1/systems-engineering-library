# A02 — State machines, data contracts and failure semantics

**Competency:** define observable request states, interface preconditions and rejection rules, then demonstrate that a faulty message never becomes an unsupported successful outcome.

## From happy path to explicit semantics

In a normal demonstration the user submits a request, the system assigns it to a resource, and the record is completed. Systems engineering becomes harder when events are duplicated, delayed, reordered or missing. A well-written interface contract distinguishes *message delivery* from *service commitment*: receiving a message is not a promise that service will occur; acknowledging an attempt is not proof that the customer actually received the acknowledgement.

The minimal state machine in the model is `received → queued → assigned → completed`, with branches to `rejected` and `unserved`. These are **logical states**. The simulator additionally records `unobserved_message_loss`: a request exists in its experimental truth ledger but never reaches the simulated intake. A real operator would not magically know this had happened. That difference between an omniscient simulation recorder and implementable observability is a central assurance limitation.

## Invariants versus ordinary examples

An example test might assert that request R01 completes. An invariant is stronger: **for every completed request, one vehicle is assigned and its occupied interval does not overlap another completed interval on that vehicle**. Another invariant states that the number of distinct requests equals completed plus unserved-capacity plus lost-message requests. A third rule rejects identifier collisions when the payload conflicts.

An invariant can still be incomplete. For instance, non-overlap alone doesn't guarantee that travel is physically feasible or that the passenger has been safely picked up. State precisely which abstraction level is being checked.

## Worked failure: duplicate and conflict

The CSV fixture has 13 input rows for 12 distinct requests. `simulate` ignores the exact duplicate. Adding the same request identifier with a different origin produces a rejected conflict count, rather than silently rewriting history. That is a useful *single-process* idempotency example. It does not test two workers racing to persist the same request; concurrency would require an atomic ledger and a deliberately concurrent test.

Consider a message arriving 12 minutes late. Its `arrival_min` is the demand time and its `received_min` is when simulated intake sees it. Waiting is measured from the original demand time, not the delayed receipt time; using the latter would hide user-experienced delay and bias the reported service outcome upward.

## Worked interface checklist

| Field | Meaning | Validation |
|---|---|---|
| `request_id` | immutable logical request identity | nonempty; conflict if reused with differing payload |
| `delivery_key` | transport retry identity | one stable request per key |
| `arrival_min` | demand time relative to start | finite, nonnegative minutes |
| `received_min` | simulated receipt time | at least arrival time when delay is nonnegative |
| `status` | explicit terminal result | completed / unserved capacity / unobserved loss |

## Practice and deliverable

**Exercise 1.** Why can a count of *received* requests be misleading under packet loss?

<details><summary>Worked answer</summary>The denominator excludes messages that were never observed. The laboratory has an omniscient truth ledger to count them; a deployed design would need acknowledgements, reconciliations or an external demand measure to estimate missing attempts.</details>

**Exercise 2.** Design a race-condition test for deduplication.

<details><summary>Worked answer</summary>Launch multiple workers with the same idempotency key, synchronize their write attempts, and assert exactly one durable request and one effect. Use a transaction or unique constraint; a sequential in-memory dictionary is insufficient evidence.</details>

**Submit:** a versioned request-contract document, transition table with invalid transitions, and two negative tests. Related: [software prototype in v11](../../integrated-lab/chapters/05-software-prototype.md).

## U2 cross-lab credibility challenge — NS-U2.1

**Focus: State transitions and truthful fault observability.** This adds a controlled cross-version analysis to the original learning stage, which remains unchanged.

An *event truth ledger* and the information available to an operating agent are different things. v12's `LOSS` scenario classifies four of twelve unique requests as `unobserved_message_loss`; the simulator knows this because the fault injector holds the source list. A receiver that never receives the event cannot automatically distinguish it from an event that never occurred.

**State accounting:** `12 = 8 completed + 4 injected lost + 0 capacity unserved`. The independent U2 checker reconciles every scenario's ledger and injects a falsified record status to ensure the audit detects it. The 8 completed requests yield a reported `8/12 = 66.67%`, not `8/8 = 100%`.

**Exercise and explained solution:** How could a deployed message system detect missing requests? Use sender-generated monotonic identities, durable sender receipts, an acknowledgment contract, bounded retry semantics and reconciliation. None of these are established by counting the simulator's injected drop events; they require separate tests and authority to process real events.

**Reproduce:** [Cross-lab lab guide](../../lab-credibility-u2/README.md) · [Evidence gates](../../lab-credibility-u2/data/gates.json) · [Computed results](../../lab-credibility-u2/outputs/u2-cross-lab-results.json).
