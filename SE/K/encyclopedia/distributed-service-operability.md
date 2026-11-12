# Distributed services, reliability budgets, and operations

**Reference entry · Service architecture, cloud systems and software operations**

## The distributed boundary

A service diagram hides important system behavior if it shows only request arrows. Define data ownership, trust zones, request and event semantics, concurrency, timeouts, retries, idempotency, failure isolation, observability, configuration and recovery. “Highly available service” is an end-to-end claim about a specified user journey and time window; it is not established by a single component's advertised availability.

### Worked serial-availability budget

If three indispensable service stages each have independent availability \(A_i=0.9995\), an idealized serial journey succeeds with probability

\[
A_{\mathrm{journey}}=\prod_{i=1}^{3} A_i=0.9995^3\approx0.99850075.
\]

That is approximately **99.8501%**, below a 99.9% journey objective. Over an illustrative 30-day window (43,200 min), the equivalent unavailability allowance is about \(43{,}200(1-A_{\mathrm{journey}})=64.77\) minutes, versus 43.2 minutes for 99.9%. This is **not** a measured downtime forecast: independence, constant failure behavior and continuous exposure rarely hold exactly. Shared cloud regions, shared credentials and common software defects produce correlated outages.

A chain with optional stages, cached responses or graceful degradation needs a state-dependent success model, not the simple serial product. Compute the user-facing SLO from request outcomes, and pair it with data correctness and freshness measures. A 200 response can still be semantically stale.

## Interface contract and failure-injection design

For an allocation API, specify: `POST /allocations` request ID, worker and reservation IDs, timeout, idempotency key, authorization scope, expected version, response semantics, duplicate behavior, and audit record. A retry after a timeout can reach the server twice. If the operation is not idempotent and the storage layer has no uniqueness constraint, duplicated requests can create duplicate allocation. Request identifiers must be scoped and retained for an agreed period; “exactly once” should not be promised at the message transport layer without a precise end-to-end mechanism.

Circuit breakers isolate saturated dependencies but can also reject useful work; timeouts protect latency while creating uncertain completion outcomes. Budget both availability and correctness through scenarios: lost ACK, slow database, stale cache, partial region outage, reordered message, expired credential, and rollback. For each, define a user-visible safe state and a recovery invariant.

## Operational evidence is design evidence

Capture deployment configuration, dependency versions, latency distributions, error rates, saturation, traces linked to correlation IDs, and incident timeline. Test failover under representative load, and maintain an incident-review record that ties corrective action to a regression test. A sampled metric without a defined denominator or clock window cannot support a quantitative SLO claim. An incident-free interval alone cannot establish resilience to untested faults.

## Exercise

Compute the hypothetical serial availability if four independent indispensable stages each have 99.95% availability: \(0.9995^4\approx0.9980015\), or about 99.8002%. Discuss two alternative architectures that could improve *journey* availability, and one correlated-failure mechanism that would invalidate the independence calculation. Specify a fault-injection test for duplicate assignment and identify the observable invariant that must remain true.

## Primary sources and scope

- [NIST SP 800-204A: Secure Microservices Using Service-Mesh Architecture](https://csrc.nist.gov/pubs/sp/800/204/a/final) — service identity, security and resiliency mechanisms.
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — secure software development practices.

Related: [software quality attributes](software-quality-attributes.md), [transactional concurrency](../methods/transactional-concurrency-and-assurance.md), [software lifecycle evidence](software-lifecycle-evidence.md). Illustrative availability mathematics are not operational performance evidence.
