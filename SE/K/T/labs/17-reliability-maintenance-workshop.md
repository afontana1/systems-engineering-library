# Practice Lab T17 — Reliability, availability, and maintenance are different claims

## Scenario
A regional shuttle fleet must choose between buying a spare vehicle, stocking a repair module, or relocating part of the fleet to a second depot.

## Tasks
1. Calculate reliability for a 10-hour mission and steady availability using the simplifying assumptions in the chapter.
2. Use [reliability.py](../tools/reliability.py) to compute series and parallel reliability and vary component success probabilities.
3. Write an operational scenario in which two nominally independent vehicles fail through one common cause; identify which formula no longer applies.
4. Create a maintenance-state timeline (failure, detection, diagnosis, spare delay, repair, verification, release).
5. Decide which of the three investments is preferable under independent faults and under a depot-wide outage. Include the assumptions that would reverse your choice.

## Deliverable
Submit a brief architecture trade and a reliability evidence plan. Keep failure incidence, mission success, steady availability, and restoration time as different metrics.

[Return to the textbook chapter](../17-reliability-maintenance.md)
