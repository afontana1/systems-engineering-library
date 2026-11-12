## Integrated case NS-G4.1 — State transitions, idempotency and retry stability

> **NS-G4.1 case convention.** Every number in this extension comes from a controlled, fictional emergency-dispatch dataset, unless explicitly identified as an illustrative assumption. A Python screening result is not an operational safety finding, a validated queue model, or an authorization from independently managed agencies. The case is shared with the other five advanced-studies chapters; use the same `revision: 1.0` throughout.

**Reproduce:** [controlled JSON](../data/ns-g4.1-case.json) · [Python model](../code/ns_advanced_case.py) · [computed results](../outputs/ns-g4.1-results.json) · [integrated laboratory](../labs/INTEGRATED-CASE.html).

### G1. State machines define what messages are allowed to mean

The Northstar reservation service cannot treat network acknowledgement as the same event as durable completion. The sequence for a single request is `RESERVE → COMMIT → ACK`. Each message has a request key, integer monotone sequence number, type, and a payload digest. An exact replay of a previously accepted event is idempotent. Reuse of an idempotency key with a *different* payload is a conflict rather than a new reservation. An acknowledgement before a commit is an illegal transition, even if the message has a valid signature.

A minimal precondition for accepting an event \(e\) is

\[
valid(e) = known\_type(e)\land seq(e)=next(key(e))\land
payload(e)=stored(key(e))\land allowed(state(key(e)),type(e)).
\]

For the first event of a key, the stored payload condition means "either not yet set, or equal". The exercise's `trace_audit` implements a deterministic **sequential reference monitor**, not a concurrent transaction engine. It accepts E1–E3, counts E4 as an exact duplicate, rejects E5 (`ACK` before `RESERVE`) and E6 (conflicting payload for an existing key). The accepted state of REQ-17 remains acknowledged. This is a testable state-machine example; a production system would need atomic persistence, authentic message identity, concurrency isolation, and crash recovery.

### G2. Retry storms require load reasoning

If each attempted request independently retries with probability \(p<1\), the expected total number of attempts per external request is a geometric sum:

\[
1+p+p^2+\cdots=\frac{1}{1-p},\qquad
\lambda_{offered}=\frac{\lambda_{external}}{1-p}.
\]

At 80 external requests/s and \(p=0.25\), the service sees **106.67 attempts/s**. A server capable of 112 attempts/s is nominally stable in a simple infinite-buffer average-rate model. At retry probability 0.30, the offered rate is \(80/0.70=114.29\) attempts/s, exceeding service capacity. The stability boundary occurs at \(p=1-80/112\approx0.2857\). These are expectations; correlated retries, long tails, deadlines and shared state can invalidate average-rate conclusions. Add backoff with jitter, retry budgets, deduplication, circuit breaking, and a measured worst-case fault-injection experiment before claiming resilience.

### G3. An interface contract has more than a schema

Define a message contract: a producer identity and authorization scope, route revision, timestamp unit and clock source, ordering guarantee, uniqueness scope, idempotent response, expiry policy, retry semantics, and behavior after partial success. An interface change R2→R3 requires re-review of semantic assumptions even if fields still parse. In the integrated case, the `interface_drift` scenario makes the coordinated policy's R2 token ineligible for a route authorization expecting R3. Passing the retry load screen does not cure that safety defect.

In distributed execution, "exactly once" delivery is usually not an end-to-end primitive; a safer claim is *at-least-once delivery with idempotent effects under tested persistence and recovery assumptions*. Prove the intended invariant for a specific implementation or test its limits with crashes between committing a reservation and returning an acknowledgement. The reference trace by itself cannot prove serializability or linearizability.

### Worked exercise with explained solution

**Problem.** At \(\lambda_{external}=80\) requests/s and service rate 112/s, calculate the highest retry probability that maintains strict mean-rate stability. Then describe what to do after an ACK is lost.

**Solution.** Require \(80/(1-p)<112\), so \(p<1-80/112=2/7\approx0.285714\). Equality is a boundary, not a stability margin. A client may retry with the *same request key and payload*; the service must return the already committed result without consuming a second capacity slot. A changed payload must be reported as a conflict and investigated, not silently applied.
