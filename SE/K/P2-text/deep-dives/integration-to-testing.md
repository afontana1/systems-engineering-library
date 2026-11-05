# From an integration build-up to a formal evidence package

*Phase 2 concept library deep dive · Independent instructional synthesis*

## The same experiment changes status through the lifecycle
During design, an informal bench script may reveal a faulty field mapping. During integration, the script becomes a repeated regression check across controlled interfaces. For formal qualification, it must be transformed into an approved procedure that is traceable to requirements, executable against a documented test article and supported by calibrated instrumentation, data control and authorized dispositions. Automation alone does not perform that transformation.

Consider a staged path: mock interface schema → real database and queue → simulated vehicle gateway → supervised operator console → system test bed → controlled validation scenario. Every stage has an identified purpose and a scope limitation. A failure in the second stage should not require rebuilding the entire architecture. Preserve known-good images and record which release, hardware and configuration produced each outcome.

## Readiness reviews are evidence checks
The Integration Readiness Review asks whether interfaces, elements, personnel, enabling equipment and safe work procedures are ready for assembly and integrated testing. The Test Readiness Review asks whether a specific formal test can execute safely and produce valid evidence. The final evaluation review asks which claims the collected evidence actually supports. All three involve reviews, but they examine distinct obligations and cannot substitute for one another.

A strong test procedure names the controlled requirement, objective, article serial/build, environment, instrument pedigree, stimulus sequence, expected observation, stop criteria, data retention and results authority. It also defines how a deviation is recorded and what evidence supports retesting. If the harness silently discards missing responses, formal test results will be systematically biased regardless of how precisely the other timestamps are measured.

## How to trace one discrepancy
A timed request fails. Record the original run and data without alteration. Investigate whether the device, interface or measurement chain caused the mismatch. If device behavior failed a valid criterion, open a product discrepancy and corrective action. If timestamp clocks were invalid, document an instrument/test-system discrepancy; after authorized disposition, repair the test setup and rerun. In either case, preserve the failed/invalidated run rather than silently deleting it.

## Exercise
Create a promotion checklist that turns an exploratory network-partition test into a qualification procedure. **Model answer elements:** stable input stimulus and versioned harness; verified failure injection; controlled test article; preapproved thresholds; time synchronization; evidence trace to a requirement; operator safety stop; configuration manifest; deviation workflow; independent review and signoff.

[Back to Phase 2 companion index](../README.md)
