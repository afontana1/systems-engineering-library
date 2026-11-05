# Northstar Mobility Systems — integrated Phase 4 case

## Context

Northstar Mobility Systems (NMS) operates a hypothetical autonomous campus shuttle service. The Phase 0–3 work established requirements, architecture, verification plans, simulation evidence and a baseline trade study. Phase 4 adds a changing environment: an accessibility rule change, a telemetry-security issue and a supplier delivery delay. These are **synthetic teaching scenarios**, not reports of real mobility service.

## The working problem

NMS needs to reduce elapsed time from discovery of a relevant operational concern to a safely verified and authorized response. Current change requests often wait for evidence reconciliation and shared specialist review. Faster code delivery alone is unlikely to solve the mission problem.

## Three linked courses and their decisions

| Course | Decision | Artifacts created |
|---|---|---|
| Agile Systems Engineering | How should the organization sense, learn and authorize change? | Response requirements, WIP measures, assurance-aware backlog, scaled operating model |
| Digital and Mission Engineering | Which data/models are authoritative for mission-relevant decisions? | Model catalog, configured trace graph, state freshness record, mission threads, credibility register |
| Systems Engineering Process Improvement | Which intervention can reliably reduce delay without compromising evidence? | Event log, measurement plan, root-cause assessment, simulation, pilot charter, control plan |

## Synthetic reference snapshot

* Backlog: 18 valid open changes.
* Throughput: 3 completed changes per week in the baseline period.
* Approximate stable-flow duration: 18 ÷ 3 = 6 weeks (Little's Law, subject to stable boundary/throughput assumptions).
* A high-risk safety change requires explicit independent authorization even if implementation is complete.
* The telemetry twin updates every 15 minutes; its ability to support minute-level dispatch decisions must be justified rather than presumed.
* Baseline process times and defect rates shown in the original course examples are **exercise inputs**, not consistent measurements from a real program. Treat each separately and record differences rather than combining them into a false single dataset.

## Example mission thread

Emergency event → mission owner issues evacuation directive → accessible rider demand observed → operator confirms availability → dispatcher assigns transport → vehicle and curb interface support boarding → operator acknowledges safe arrival → mission outcome is recorded.

Each dependency should have an owner, evidence source and fallback condition. Design performance is not the same as mission effectiveness.

## Final integration assignment

1. Define a bounded response requirement for a cybersecurity advisory and an accessibility change.
2. Draw the process and technical evidence chain needed to act on the requests.
3. Identify one stale or misconfigured model result; demonstrate how a validation query catches it.
4. Simulate or estimate the end-to-end change process, including waiting and rework.
5. Design a controlled pilot that reduces delay and leaves all assurance stop conditions intact.
6. Present a mission-outcome-focused decision memorandum with limitations and rollback conditions.

## Case limitations

No supplied example, synthetic data row, software test or illustrative scenario is a real-world authorization, safety claim, statistical estimate of fleet reliability, or professional certification. Reproduce methods on actual approved data before applying them to a real system.
