# State machines, contracts, and distributed failures

*Core Concepts · Modeling & software · T05*

> Explain why correct local code may yield incorrect system behavior when messages and time intervene.

**Recommended preparation:** [Architecture, interfaces, and design tradeoffs](03-architecture.md), [Model semantics, viewpoints, and digital traceability](04-model-semantics.md)

**Related course companions:** [Book 4](../B4/OPEN-BOOK.html), [Book 5](../B5/OPEN-BOOK.html), [Book 16](../B16/OPEN-BOOK.html)

## 1. States encode obligations through time
Consider a trip request with states `NEW`, `ACCEPTED`, `ASSIGNED`, `BOARDED`, `COMPLETED`, `CANCELLED`. A state machine states which transitions may occur and under what conditions. A transition must specify event, guard, state update, and observable effect. A label such as “process booking” is too ambiguous to test.

A central invariant might be: *a trip cannot be completed unless boarding has been recorded*. Another: *one active request key corresponds to at most one active assignment*. These become executable assertions. A diagram helps explain the design; it does not replace guards and failure cases.

## 2. Local contracts are not global guarantees
A service API contract may say a request with a valid identifier returns an acknowledgment within 250 ms when the service is reachable. But the journey depends on repeated messages, clock skew, duplicate requests, network partitions, and human responses. A distributed workflow may have no single instant when all participants agree on its state.

A caller may retry after a timeout even though the first request succeeded. Therefore **idempotency** matters: a repeated command with the same idempotency key should not create a duplicate reservation. This is stronger than just catching exceptions, and distinct from exact-once network delivery, which should not be assumed merely because the protocol is reliable under nominal conditions.

## 3. Model failure semantics explicitly
For each operation, classify whether a timeout means definitely failed, possibly succeeded, or unknown. The last category is common in distributed systems. Design reconciliation: query by idempotency key, use monotonic revision numbers, or record an event log with explicit recovery behavior. Document which state changes are reversible, compensatable, or irreversible.

Suppose the scheduler assigns a vehicle and then fails before sending acknowledgment. An unsafe recovery may send a second vehicle. A safer policy persists a unique assignment record before acknowledgment, retries using the same key, and exposes a way to inspect the current status. It still requires tests for data corruption and concurrent requests.

## 4. Quality attributes are scenarios
Availability, security, latency, and maintainability are not abstract marks on an architecture. Form each as a scenario: source of stimulus, operating environment, affected artifact, expected response, and response measure. “The service is resilient” is not testable; “after one scheduler instance fails during an accepted request, processing resumes without a duplicate assignment within 60 seconds” is much closer.

Avoid claiming that a working demo establishes reliability. A demo tests selected paths. Assurance requires explicit operational conditions and evidence about the critical failures not exercised in the demo.

## 5. From sequence diagram to executable obligation
Write a short chronological trace for a request that succeeds and another that suffers message loss. Annotate each point where durable state changes. Then define a transition table: current state, triggering event, guard, next state, persisted action, and response. A state machine without persistent state semantics may be correct in memory and wrong after a process restart.

Concurrency introduces another failure class. Two workers can both read `unassigned` and then assign different vehicles unless the storage update is atomic or guarded by a version check. An invariant such as *one request key maps to one active assignment* must be preserved under concurrent execution, not merely in a single-threaded test. Test by scheduling interleavings, forcing restarts, and replaying stored messages.

Avoid equating **idempotency** with ignoring all repeated commands. A new cancellation event may be legitimate even if the original booking request was repeated, and a retry from a different logical operation needs a different key. Define key scope, retention window, state-dependent behavior, and reconciliation when the client has received no conclusive answer.

A useful assurance argument for the service connects an explicit invariant to tests at three levels: pure transition tests, component tests with persistence and concurrency, and an end-to-end fault-injection scenario. These are complementary, not redundant.

## Guided worked example

### Worked failure trace
At 10:00:00 a client sends `reserve(key=K7)`. The server commits assignment V2 at 10:00:01, but the acknowledgment is lost. At 10:00:03 the client retries. A non-idempotent service assigns V3 as well; both vehicles arrive. The repaired contract stores `K7 → V2` before reply and returns V2 on retry. Test the retry, concurrency, and retention period; do not only test the happy path.

## Independent transfer exercise

Draw a seven-state request machine and list five transition guards. Write test sequences for lost acknowledgment, duplicate request, cancellation after boarding, and a delayed completion event.

[Open the companion hypothetical lab](labs/05-software-contracts-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

A defensible design identifies illegal states, defines idempotency scope, and handles ambiguous outcomes without creating a second assignment.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
