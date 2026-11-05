# Operational readiness as claims, arguments, evidence and limits

*Phase 2 concept library deep dive · Independent instructional synthesis*

## A review is not a vote for optimism
An operational readiness recommendation states what is supportable now, within which configuration and operating context, under whose authority. Construct the case from explicit **claims**, **evidence**, **assumptions**, and **defeaters**—observations or unresolved risks that could invalidate the argument. Visual status dashboards can help navigation but cannot turn a critical untested hazard into a green overall verdict.

A well-structured claim set includes: requirements verified for design baseline `DES-1.3`, operational goals evaluated for a stated user group, safety controls independently reviewed within their authorized domain, supportability arrangements ready, and known anomalies dispositioned. For each claim name accepted results, test environment and validity limit. A simulation can support claims about its modeled behavior only to the extent its model credibility permits. A restricted lab demonstration does not establish street-operation readiness.

## Example of a conditional argument
Claim: a dispatch software demonstrator can be used in a closed laboratory. Evidence: controlled builds passed specified functional, fault-injection and latency tests under `WL-01`. Counterpoint: no representative campus-wide network partition and no complete accessibility user study. Disposition: restricted lab continuation; field trial not approved. Condition to expand: an authorized network-resilience evaluation, stakeholder validation with appropriate access needs, and updated incident-response procedures. A governing body still has to decide whether and under what rules any broader trial is lawful or acceptable.

The final package should let a future reviewer reproduce the evidence story: baseline manifest, verified requirement statuses, validation findings, test procedures and runs, uncertainty calculations, issue/risk registers, signed actions and explicit unknowns. If a design revision follows the test, the old evidence must be reassessed for relevance.

## A counterfactual drill
Suppose 99th-percentile response latency passes in the lab but the fleet telemetry system changes to a cellular provider whose coverage has not been measured on the campus route. Does the old performance test establish field readiness? **No.** The operating environment, failure modes and interface assumptions changed. The right response is to restrict the claim, plan representative evidence, update the architecture's degraded-mode handling and document authority for any field test.

## Final self-check
Ask an independent reviewer to answer: What exactly passed? Against which requirement revision? On which article and environment? Who signed the evidence? What does it *not* prove? Which observation would force the organization to stop or rework? If any of these lacks an answer, readiness is an open engineering question.

[Back to Phase 2 companion index](../README.md)
