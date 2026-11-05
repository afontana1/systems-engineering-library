# Security, safety and release evidence as structured claims

**Concept library essay · Phase 1**

## Assurance starts with a bounded claim
A claim like 'the platform is safe and secure' is too broad to establish. Instead say 'the assignment service prevents duplicate active assignments in the specified simulated concurrency workload' and link the claim to design controls, tests, versions and conditions. A nested argument can show why a system-level claim depends on software, physical components, operating procedure and organizational response. Explicit assumptions are essential.

Security threats involve adversarial intent; accidental failures involve faults and mistakes; both may trigger similar controls. An API request can be authenticated but unauthorized. An event message can be well-formed but semantically stale. A supply-chain dependency can be unmodified in your source tree yet compromised upstream. Threat modeling identifies assets, entry points, trust boundaries and attack narratives. A failure mode review identifies component faults, effects, detection and recovery. Neither activity alone proves controls work.

## Evidence has quality levels
A design review can show a mitigation is intended. A unit test can show one local rule works. An integration test can show a particular interface behavior. A representative operational test can show a specified system behavior in one environment. Long-run field measurements and independent assessments answer different questions. Good assurance arguments attach the right level of evidence to the right claim.

## A release review under uncertainty
Assemble a table with claim, requirement ID, criticality, supporting evidence, configuration, outstanding gap, consequence and disposition. Define mandatory go/no-go rules before seeing favorable test results; otherwise the team may move the threshold to fit the evidence. Approval should be scoped: the lab simulator may be ready while the public-road system is not. Keep residual risks visible and owned.

## Practice
Create an assurance claim for duplicate assignment prevention, then deliberately inject three counterexamples: concurrent writes, replay after timeout and manual database repair. Which tests and operational controls are needed? Reference NIST SSDF for secure development practices and your original course guide for release rubric.

[Back to Phase 1 library](../README.md)
