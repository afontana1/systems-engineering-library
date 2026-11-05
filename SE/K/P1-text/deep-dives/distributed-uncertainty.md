# Distributed systems: timeouts, duplicates and eventual knowledge

**Concept library essay · Phase 1**

## The uncertainty behind a timeout
A caller sends a command to another process. The remote process updates its database but crashes before returning success. The caller observes a timeout. Was the command executed? Yes. Can the caller know from the timeout? No. Retrying can cause a second side effect unless the operation is idempotent. This is not an edge case caused by sloppy code; it follows from unreliable communication between independent failure domains.

A practical idempotency design stores a token, a canonical request representation, the resulting decision and the associated transaction. A second request with the same token and payload returns the same decision; the same token with a different payload is rejected. This can prevent duplicate effects for the protected operation. You still need to handle token retention, expired tokens, data migration and the difference between server state and external side effects.

## Consistency is a product decision
A dispatcher cannot assign the same unique accessible vehicle twice to overlapping trips. This invariant probably belongs within one authoritative transactional boundary. Rider status displays can be eventually consistent, as long as the user interface explains staleness and no safety decision relies solely on that stale projection. Strong coordination and availability under network partition pull in different directions: the correct answer depends on the business invariant and failure consequences.

## Compensating actions
A distributed workflow may not be able to atomically update a reservation database and a third-party notification provider. A transactional outbox records business change plus pending outbound event in one local transaction. A relay publishes later, potentially more than once; consumers deduplicate by event ID. If an external booking was created and a later step fails, a cancellation/compensation may be needed. Such compensation is a business action, not magic rollback of time.

## Practice
Simulate lost acknowledgement after a successful reservation. Show the database before and after retry. Then add a duplicate event and an out-of-order cancellation. Define what the client may safely display at each point. `tools/reservation_service.py` provides an executable toy model, not a production distributed transaction manager.

[Back to Phase 1 library](../README.md)
