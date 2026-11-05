# Advanced Workshop · Distributed Failures, Retry Storms, and Idempotent APIs

*Book 5 · Week 7 · partial failure · replay · bounded retries · backpressure · interface assurance*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-distributed.md). The assessed course obligations remain in [the curriculum](../../../C/P1/EN645764.html).

## 1. Failure is ambiguous across a network

A call from the booking service to the fleet dispatcher can fail in at least three different ways: the request is lost before execution, the dispatcher executes the request but the response is lost, or the dispatcher is slow and the client times out while execution is still in progress. A caller who sees `timeout` cannot infer which occurred. If it retries indiscriminately, duplicated side effects are possible. If it does not retry, transient loss may unnecessarily reduce mission success. Distributed engineering therefore begins by separating transport evidence from business outcomes.

The typical requirement is not *exactly one message*. Networks reorder, duplicate, or delay messages. A more defensible contract is **at-least-once attempt with at-most-once business effect per stable idempotency key** for a documented retention period. The server needs a durable deduplication rule; the client must preserve the key across retries. If the client generates a fresh key per attempt, the design defeats itself.

## 2. The hidden mathematics of retries

Assume each attempt independently fails with probability \(p\), and the client makes at most \(n\) attempts. Then the probability that all attempts fail is \(p^n\), so the chance of at least one successful attempt is

\[
P(\mathrm{success\ by\ }n)=1-p^n.
\]

With \(p=0.15\) and \(n=3\), the result is \(1-0.15^3=0.996625\), roughly 99.66%. This looks excellent. But the assumptions are unusually strong: failures must be independent, attempts must have the same probability, request deadlines must permit retries, and a success must correspond to a valid business outcome. During a shared network outage or overloaded service, failures can be highly correlated; the repeated attempt may have nearly the same fate.

Retries also **create load**. The expected number of attempts per original request is \(1+p+p^2+\cdots+p^{n-1}\). Under the same example this is \(1.1725\), so 100 initial requests per second generate an expected 117.25 downstream attempts per second. This calculation is not a traffic forecast under outage correlation; it is a teaching estimate under independent identical attempts.

## 3. Engineering the retry budget

A retry policy must specify (i) which errors are retryable; (ii) maximum attempts; (iii) exponential backoff and random jitter; (iv) a total request deadline; (v) an idempotency token; and (vi) what happens after exhaustion. Retrying an authorization refusal, invalid request, or permanent capacity rejection adds load without creating success. Client timeouts should be chosen with an understanding of downstream service-time distributions and the remaining user deadline.

A circuit breaker can stop traffic to a failing dependency for a period, while **bulkheads** limit the blast radius between mission functions. Load shedding can protect a service from collapse, but creates rejected demand that must be visible in system-level service metrics. A queue that accepts every request without a bounded capacity merely stores overload until latency becomes unacceptable.

## 4. Worked failure injection

Suppose Northstar receives 100 booking requests per second and an external dependency can reliably process 110 attempts per second. With \(p=0.15\) and up to three attempts, the expected attempted load becomes 117.25/s—above the nominal downstream service capacity. The independent-attempt success formula would predict 99.66% success **if the system could serve all those attempts under the stated probabilities**. The load result undermines that assumption. Under a simple queue approximation, the implied utilization exceeds one, so waiting time would grow without bound until demand or service changes.

This is an engineering contradiction, not an arithmetic error: the reliability gain from retries can destroy the capacity assumption used to justify the gain. Try capped retries with jitter, an overload rejection policy, or a different fleet-service interface. Record both completed requests and rejected/timed-out requests; a dashboard showing only the latency of successful bookings is systematically misleading when overload causes failures to be excluded.

## 5. Connect software tests to system assurance

A unit test can demonstrate that a handler reuses the original idempotency key. It cannot demonstrate recovery from real partitions. A component integration test can inject a lost acknowledgement. A load test must measure retry amplification across the relevant dependency graph. A fault-injection experiment should preserve a known baseline, control the disturbance, and track safety-relevant effects such as stale route commands. The test oracle needs to check invariants, not merely a 200 status code.

## Worked problem set — attempt before revealing solutions

### Problem 1

Compute the independent three-attempt success probability for p=0.15.

<details><summary>Show solution 1</summary>

1 − 0.15³ = 0.996625, conditional on independent identical attempt failures and enough time/capacity for all attempts.

</details>

### Problem 2

At 100 requests/s with p=.15 and three attempts, compute expected attempts/s.

<details><summary>Show solution 2</summary>

100(1 + .15 + .15²) = 117.25 attempts/s. That exceeds a 110/s dependency and invalidates a stable-capacity assumption.

</details>

### Problem 3

What changes if all attempts share a single network outage event?

<details><summary>Show solution 3</summary>

The outcomes are correlated. The formula 1 − p³ is inappropriate, and repeating a request may not improve success at all during the outage.

</details>

### Problem 4

Why should a fault-injection experiment count rejected bookings?

<details><summary>Show solution 4</summary>

Latency measured only for completed bookings is subject to selection bias. Rejections and timeouts are mission outcomes and must remain in the denominator.

</details>

## Independent transfer to the Northstar case

Use `book5.py` to sweep failure probability, retry count, and incoming request rate. Identify configurations where retry amplification overloads a 110 attempts/s dependency. Construct a table distinguishing transient transport failure, durable business rejection, and lost acknowledgement. Propose circuit-breaker and idempotency contracts, and write an integration test for each failure class.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-distributed.md) · [Python source](book5.py) · [Experiment dataset](book5-failures.csv) · [Interactive workbench](WORKBENCH.html).
