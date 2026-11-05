# Hypothetical Lab 7 — The Interface Contract Hearing

**Course:** EN.645.662 Week 7 · **Reading:** [Chapter 7](../chapters/07-allocating-architecture-and-interfaces.md) · **Time:** 100–140 minutes.

## Situation

The central dispatch service accepts `VehicleReadiness` records with fields `vehicle_id`, `position`, `time`, `health`, and `door_state`. A supplier explains that `time` is the *arrival time at the cloud broker*. The consumer assumes it is the *time the measurement was taken on the vehicle*. A vehicle publishes every eight seconds. The proposed dispatch freshness limit is five seconds. Another supplier interprets `position` in a different coordinate reference system. No one is named as the interface control owner.

## Engineering work

1. Draw the logical function `Determine assignment feasibility` and at least two physical allocation alternatives. Identify the actor or software element with authority to accept and reject a readiness record.
2. Write an interface control sheet distinguishing *event measurement time* from *broker receipt time*, including the time source, unit, epoch, schema version, maximum age, error and duplicate behavior, and change authority.
3. Show why an eight-second reporting interval is inconsistent with a persistent five-second freshness expectation in the simple periodic case. What operational behavior is authorized during stale-data intervals? Do not solve the contradiction by silently changing a requirement.
4. Create a four-row contract-test table: ordinary valid record, 6-second-old measurement, missing timestamp, and schema revision mismatch. Include expected dispatch decision and evidence collected.
5. Record at least two external interfaces: accessible stop geometry and operator escalation. Identify who owns each, what the project can control, and which agreements are required.
6. Compare integration order under central and distributed dispatch. Which contract tests should run before whole-system scenario trials?

## Deliverables

`LAB07_Allocation.md`, `LAB07_InterfaceControl.csv`, `LAB07_ContractTests.csv`, and a brief unresolved-assumption list. Include an interface ownership field in each record.

<details><summary>Reference critique</summary>

The published `time` field is semantically ambiguous. A broker receipt time cannot be used as a measurement-age guarantee, especially during buffering. Even with negligible latency, a periodic eight-second publication rate can leave the latest measurement older than five seconds for a substantial part of each cycle. A candidate response is to disallow new assignments while freshness is not established; the final policy requires appropriate engineering and safety authority. The position field needs explicit units and coordinate reference. Contract validation must cover semantics and failure behavior, not just parseable JSON.

</details>

## Transfer

Use the same reasoning when building the original Week 7 `662_W07_ArchitectureInterfaces_v1.0` with three views, allocation matrix and five controlled interface sheets.
