# A03 — Resource-constrained discrete-event experiments

**Competency:** explain the simulator's event ordering and resource logic, then use the resulting records to test carefully bounded capacity claims.

## What this simulation does—and does not—represent

A discrete-event model advances through changes in system state instead of computing every physical instant. Northstar maintains a resource availability time per vehicle, receives synthetic request events, and selects the resource with the earliest feasible service interval. Requests are ordered by **receipt time**. For a candidate vehicle the start is the later of receipt and availability, shifted forward until it no longer intersects a declared outage or central telemetry block. A 12-minute service interval is then reserved if completion fits the 80-minute demonstration horizon.

This is a centralized *reservation* model, not a geographic ride-hailing dispatch algorithm. It assumes service durations are identical, vehicles do not reposition, and a reservation can be planned while a previous job remains active. Those simplifications are useful for teaching capacity but too strong for field performance predictions.

## The event algorithm

For each received request, and for each candidate vehicle `v`, compute:

`candidate_start_v = first_unblocked_time(max(received_time, vehicle_ready_v), trip_duration)`

Choose the vehicle with the smallest candidate start, breaking ties by vehicle number. If `candidate_start_v + trip_duration` exceeds the horizon, record `unserved_capacity`; otherwise reserve the interval and advance that vehicle's `ready` time.

An interval block is half-open `[start,end)`. An outage from minute 0 to 70 therefore permits a vehicle to restart at exactly minute 70. In this synthetic reference case, the outage leaves six completed requests rather than 12. The underlying input stream and assumptions are otherwise identical, so the comparison isolates *modelled* outage behavior on that fixture.

## What to measure

**Completion fraction** is completed divided by distinct demands, including demands lost before intake (visible only to the lab's truth ledger). **Nearest-rank p90 wait** sorts completed waits and chooses rank `ceil(0.9n)`; this is conditional on completion. A service design that drops hard cases can improve its successful-customer p90 while making outcomes worse overall. Always report completion fraction and p90 together.

The baseline completes 12/12 and has p90 = 20 minutes. The message-loss case has a superficially better p90 among observed completed requests despite completing fewer requests. This is a concrete example of selection bias in operational dashboards.

## Practice and deliverable

**Exercise 1.** A vehicle becomes free at minute 22, has a blocked interval `[20,35)`, and the next trip lasts 12 minutes. When may service start?

<details><summary>Worked answer</summary>Minute 35, because the proposed interval `[22,34)` intersects the block and `35` is the earliest feasible time. This assumes no further blocked interval.</details>

**Exercise 2.** Why is the simulator insufficient for route-level feasibility?

<details><summary>Worked answer</summary>Service duration is constant and no location, road network, pickup/deadhead travel, demand geography, or capacity coupling is represented. A physical design decision would need these mechanisms and empirical calibration.</details>

**Submit:** your modified scenario file, a short algorithm walkthrough, and a table reporting all scenarios' completion, loss and conditional wait metrics with caveats. Related: [v11 simulation stage](../../integrated-lab/chapters/06-models-and-uncertainty.md).
