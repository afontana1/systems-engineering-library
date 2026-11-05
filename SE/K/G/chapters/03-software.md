# 3. Distributed software contracts, state and failure

*Graduate engineering sequence · Software-Intensive Systems · Northstar reservation service*

**Prerequisites:** object-oriented design, state machines, probability, concurrency, database transactions. **Courses:** Object-Oriented Analysis and Design, Software Systems Engineering, Model-Based Systems Engineering.

## 3.1 What an API contract must actually promise

An interface schema says how a request is encoded. A distributed systems contract must also specify **what action the request causes**, **how repeated requests behave**, **when its outcome becomes visible**, and **what failures mean**. Consider a passenger app that sends `ReserveTrip(rid, passenger, route)`. The network can delay, drop, duplicate or reorder packets; a client may time out after the server commits the reservation; a server may restart before sending its reply. None of these requires corrupt data. They are ordinary possibilities in a distributed system.

The service needs an invariant stronger than 'the API returns HTTP 200 when successful': for any logical reservation identifier, at most one committed capacity allocation exists. Let $C(r)$ count committed capacity assignments for request $r$. The safety invariant is $G(C(r)\le 1)$. A liveness expectation could state that a valid request eventually receives a definitive outcome, but that claim needs availability, retry, timeout and capacity assumptions. When dependencies can be unavailable indefinitely, 'eventually' is not guaranteed by the program alone.

**Idempotency** is a design property of the operation, not of the HTTP verb or the name of a key. Applying the same logical command twice must have the same externally relevant effect as applying it once. If the key is reused with a different route or passenger, the server must reject the mismatch rather than quietly return the old result or create a second trip. Keys require a namespace, lifetime, and deterministic interpretation of parameters. They may be retained for a bounded period; after expiry, the system must say what replay means.

![Reservation command, transaction and reply](../diagrams/03-software.svg)

## 3.2 The commit/acknowledgement gap

Imagine the following trace. At 09:00:00 the client sends request `R-71`; at 09:00:01 the service reserves the final seat and writes the result durably; at 09:00:02 the reply is lost; at 09:00:05 the client retries. If the service treats the retry as a new order, it may charge or allocate twice. If the client assumes no reply means no reservation, it may send the passenger elsewhere even though capacity was consumed. The correct implementation must preserve the outcome of the **logical request**, not the outcome of an individual network attempt.

A practical single-database design uses a uniqueness constraint on `(tenant_id, idempotency_key)` and records the canonical parameter digest and outcome within a transaction that also changes capacity allocation. A retry with the same digest returns the stored outcome. A retry with a conflicting digest returns a conflict. Merely maintaining an in-memory set of seen keys fails after restart and may fail under concurrent workers. A database write followed by an unrelated event publication is not atomic; an outbox pattern can persist the event intent in the same transaction and publish it asynchronously, with consumers that tolerate duplicate delivery.

An 'exactly once' end-to-end business effect is usually a composition of **at-least-once message delivery**, durable deduplication, and well-designed transactional boundaries. Calling a message bus 'exactly once' does not make arbitrary external side effects exactly once. A payment provider, passenger notification, or vehicle command may have a different transactional boundary, and each requires its own failure and reconciliation strategy.

## 3.3 State machines and legal transitions

A reservation can be `NEW`, `HELD`, `CONFIRMED`, `CANCELLED`, or `EXPIRED`. A transition model provides a legal relation $T\subseteq S\times Event\times S$. For example, `(NEW, place_hold, HELD)` and `(HELD, confirm, CONFIRMED)` may be permitted, while `(CANCELLED, confirm, CONFIRMED)` is prohibited without a new request. State models become significantly more useful when their **guards and effects** are specified: a confirmation requires an unexpired hold; expiration releases capacity only once; cancelling a confirmed reservation may create a separate refund obligation.

Invariants should involve external resources. If $capacity(v)$ is a vehicle's seat count and $booked(v)$ its committed allocations, require $0\le booked(v)\le capacity(v)$ at each transaction boundary. Model checking or exhaustive tests over a small state space can uncover sequences omitted in happy-path unit tests: two concurrent confirmations, cancellation racing with expiry, retry after restart, and duplicate late messages. A model that explores one request at a time does not establish safety under concurrent execution.

## 3.4 Queue stability and retry storms

Availability design is tightly coupled to load. A server with service rate $\mu=100$ requests/second and external arrival rate $\lambda=80$ requests/second appears to have 20% headroom. If every failed or timed-out request is retried immediately with independent probability $p$, then a simplistic feedback approximation gives

$$
\lambda_{effective}=\lambda\sum_{k=0}^{\infty}p^k=\frac{\lambda}{1-p},\qquad 0\le p<1.
$$

For $p=0.25$, effective offered load is approximately $106.7$ requests/second, already beyond capacity. This is *not* a general queueing theorem for correlated real retries; it's a warning about amplification under a geometric attempt assumption. A system at $\rho\ge1$ cannot sustain a stationary M/M/1 equilibrium. Timeouts may make clients retry **because** queues grow, creating positive feedback. Backoff, jitter, circuit breakers, bounded attempts, admission control, and explicit overload responses are architectural interventions.

Latency is not only the sum of typical service times. Serial components contribute to an end-to-end time budget, but correlated waiting and heavy-tailed service durations can make a 99th-percentile response far greater than the sum of each component's median. A service-level objective should specify which requests count, over what interval, and which failures are included. Dropping slow requests from the denominator can manufacture a favorable latency percentile while worsening mission completion.

## 3.5 Consistency, partitions and authority

Distributed replicas can disagree during a network partition. A reservation system must choose where strong coordination is necessary: final-seat allocation is usually different from read-only map preview. A bounded-staleness read may be acceptable for a passenger's expected wait estimate but unacceptable for authorization to enter a restricted corridor. The key engineering task is to **classify operations by invariant and consequence**. Some can tolerate eventual consistency with reconciliation, others need a single writer, quorum, fencing token, or transactional coordination.

Leader election by itself does not prevent stale writers from issuing effects. A fencing token or monotonic revision can let downstream recipients reject commands from an obsolete leader. The receiver must actually enforce the token. Changing the sender while leaving the vehicle-side command acceptance permissive simply moves the split-brain problem downstream.

## 3.6 Assurance and the test strategy

Derive tests from the contract: replay the same request; replay with changed payload; inject duplicate and out-of-order messages; kill the process after the database commit but before acknowledgement; run concurrent attempts against one capacity unit; partition one replica; expire a reservation during cancellation; restore service and reconcile event streams. Record the generated identifiers, configured versions and resulting business state. Property-based testing can explore more sequences than a short list of examples, but the generator and invariants must still represent the actual environment.

### Worked concurrency scenario

Two threads each execute 'if seats available then subtract one.' Both read one seat and each concludes it can reserve, producing two accepted confirmations for one seat. Merely checking the condition in application code does not protect the invariant. An atomic database update conditional on remaining capacity, or a serializable transaction with a uniqueness constraint, can prevent the double allocation. Design the test to force both attempts to reach the same barrier before committing, not to rely on a probabilistic race.

## Problems — solve first

1. An external arrival rate of 60 requests/second experiences a retry probability of 0.2. Under the stated geometric approximation, compute effective load and test a service rate of 70 requests/second for stability.
2. Specify the transactionally persistent fields needed to defend reservation idempotency across process restart. Explain what should happen if the same key has a different payload digest.
3. A leader in epoch 17 sends a departure permission after epoch 18 has been elected. Why must the consumer check the epoch, and what property does that enforce?
4. Describe a counterexample to 'a unique idempotency key guarantees exactly-once passenger notifications.'

<details><summary>Worked solutions</summary>

1. $60/(1-0.2)=75$ attempts/second. A 70-per-second server is unstable under the stationary single-queue approximation. An intervention must reduce attempts or increase processing capability; a shorter client timeout alone can worsen overload.
2. Persist tenant and key, parameter digest, logical request state, canonical outcome, creation/expiry policy, and allocation record in a suitable transactional boundary. Reject mismatched digests; never silently reinterpret the key.
3. A delayed stale writer may otherwise issue conflicting actions after losing leadership. Receiver-side monotonic fencing rejects an epoch less than the maximum accepted epoch, assuming trustworthy token assignment and enforcement.
4. The reservation transaction may be idempotent while a downstream notification consumer receives duplicate events and sends duplicate messages. Notifications need their own deduplication or semantically harmless duplicates.
</details>

## Practice and sources

[Run the partition-and-retry laboratory](../labs/03-software.html) · [Python implementation](../code/system_models.py) · [Jupyter model](../notebooks/03-software.ipynb). **Reading:** [NIST SP 800-218 Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) gives security practices for software development; it is not a distributed-consistency specification.
