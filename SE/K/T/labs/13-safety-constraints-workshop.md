# Practice Lab T13 — Safety engineering: from hazards to enforceable constraints

## Scenario
A geofence update normally arrives every 2 seconds. The shuttle dispatcher must not authorize motion if the last accepted update is more than 6 seconds old. A route release may be queued during a radio outage.

## Materials
Download [zone-events.csv](zone-events.csv) and [hazard_checks.py](../tools/hazard_checks.py). Open the source in the lab browser if you want to examine the actual conditions being tested.

## Investigation
1. State the system loss, one hazardous state, and three unsafe control actions.
2. For each event row, compute the age of the last valid feed at the decision time. Mark a release as permitted only when feed age is no greater than six seconds *and* the zone is clear.
3. Run the Python checker, then add one event with an invalid signature or negative clock age. Defend how the system should fail closed.
4. Draft an interface contract with units, valid states, revision identity, clock assumptions, and timeout rules.
5. Plan two negative tests and one integration-level test that would challenge this contract.

## Deliverable and self-check
Submit a one-page causal diagram, a safety-constraint table, and a five-row verification matrix. A complete answer treats stale or invalid input as distinct from an explicit “clear” indication. The script checks a simplified decision rule, not an operational safety guarantee.

[Return to the textbook chapter](../13-safety-constraints.md)
