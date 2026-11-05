# Interfaces, end-to-end margins and hidden coupling

*Phase 2 concept library deep dive · Independent instructional synthesis*

## A connection is not a contract
A functional architecture shows necessary exchanges, but real integration demands much more: schema version, byte order or units, maximum and typical rates, sender/receiver authority, security identity, timeout, retry behavior, staleness, concurrency and shutdown state. An Interface Control Document should state who controls each field and what happens when assumptions break. Two components can both pass their unit tests while disagreeing about milliseconds versus seconds or "confirmed" versus "acknowledged".

A timing budget is useful because it forces ownership. Under strictly serial stages, total processing time is the sum. In an example with ingress 80 ms, queue 150 ms, selection 120 ms, storage 100 ms, network 200 ms, the nominal total is 650 ms and a 900 ms threshold provides nominal margin 250 ms. This is **not** enough to claim the 99th percentile meets 900 ms. Stage latency is variable; correlations and shared resources matter, and high-percentile stage statistics do not combine by simple arithmetic into a system percentile without distributional reasoning.

## Coupling changes the shape of failures
A new encryption gateway adds workload that consumes CPU cycles shared with queue scheduling; a growing queue increases latency nonlinearly as utilization approaches capacity. A higher polling rate raises bandwidth demand and potentially causes the very message staleness it was meant to prevent. A larger battery can extend range while affecting mass and stopping assumptions. System-level margins must be tracked across physical disciplines and test conditions.

For a stable arrival rate `λ` and service rate `μ` in a very simplified M/M/1 queue, expected time in system is `1/(μ−λ)` when `λ < μ`. At `μ = 10` requests/s and `λ = 8`, mean time is 0.5 s; at `λ = 9.5`, it is 2 s. This demonstrates sensitivity near saturation, not a valid prediction for a real dispatch system without verifying queue assumptions.

## A testability checklist
Every critical interface needs observable ingress/egress or equivalent instrumentation, a fault-injection mechanism and traceable revision. Review interface budget owners together, rather than checking each in isolation. Test degraded modes independently: a nominal latency budget says nothing about no connectivity. If the design chooses buffering, specify retention and stale-data handling.

## Exercise
An added stage costs 180 ms nominal. With unchanged original stages, nominal total becomes 830 ms and margin falls to 70 ms. **Question:** Does the system meet the 900 ms 99th-percentile requirement? **Answer:** Not established. You need a defined workload, synchronized measurement, population rules and enough tail data; this arithmetic only exposes shrinking nominal headroom.

[Back to Phase 2 companion index](../README.md)
