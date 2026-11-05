# Practice Lab T15 — Cybersecurity engineering: threats, trust boundaries, and recovery

## Scenario
A signed route-clearance message arrives after a new closure revision has been posted. The operator insists that a valid signature should be enough to resume service.

## Investigation
1. Draw the route-clearance data flow and mark trust boundaries, especially signing, policy lookup, dispatch, and execution.
2. Download [clearance-messages.csv](clearance-messages.csv) and inspect each message against the authorization and freshness contract.
3. Run [clearance.py](../tools/clearance.py). Add a case where a newer revision exists but the signed message is still within its nominal expiry period.
4. Draft a four-stage incident response: contain, reconcile, verify configuration, authorize resumption.
5. Identify one safety hazard created by a security control that blocks an emergency stop, and redesign that boundary.

## Deliverable
Submit a threat table, a trust-boundary diagram, six negative tests, and a bounded security claim with known gaps. Do not claim that the exercise proves real-world resistance to an adversary.

[Return to the textbook chapter](../15-threat-modeling.md)
