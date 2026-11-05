# Chapter 11 — Operations is part of the design

*Book V: Software Systems Engineering · Week 11 — Manage delivery, operations, maintenance, evolution, and incidents*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 11](../labs/lab-11-manage-delivery-operations-maintenance-evolut.md) before attempting [the assessed Week 11 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w11.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **manage delivery, operations, maintenance, evolution, and incidents** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Deployment, telemetry, incident response, maintenance and retirement need architectural attention from the beginning. Operational readiness depends on rollback, secrets management, schema migration, alert quality, data retention and safe degraded modes. A postmortem should distinguish proximate trigger from systemic causes and specify a change whose effect can be measured.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Operations reveals assumptions that development cannot settle

A software design continues to evolve after release because workloads, dependencies, threats, and users evolve. Observability is not an afterthought; it is the ability to distinguish competing explanations for an unexpected state. A service may report healthy processes while trip requests are not reaching vehicles. The operational question is not only “is it running?” but “which mission promise is currently being delivered, and what evidence supports that conclusion?”

Recovery design must identify what state is durable, what must be reconstructed, and which actions are safe to repeat. A backup that cannot be restored within the required mission interval is not adequate recovery evidence. Similarly, a rollback that returns code but not compatible data may worsen failure. Treat monitoring thresholds, incident ownership, change windows, and configuration identity as part of the system's architecture because they determine how the service behaves under real stress.

## Worked Northstar example

A Friday deployment increases response tail latency and produces repeated vehicle assignments after a cache rebuild. Rolling back the service binary may not roll back a changed database schema. The release plan must say what can be reversed, what data transformations are irreversible and how to protect active trips.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Operational dashboards that show only CPU and HTTP success can miss mission harm; include user-impact and safety-relevant metrics.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 11: Operations is part of the design](../labs/lab-11-manage-delivery-operations-maintenance-evolut.md), you will: Run a fictional incident tabletop and prepare a timeline, rollback decision, communication plan, corrective-action experiment and follow-up measure. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 11 deliverable and grading rubric.


## Deeper theory: operational reliability, error budgets, and evidence-driven change

### Availability is a service property with a declared denominator

Software operations frequently report “uptime” without defining what a user could accomplish. A server can answer health probes while a traveler cannot complete a booking. A service-level indicator should measure a stakeholder-visible event with an explicit population, such as the fraction of eligible booking attempts that return a valid confirmation within three seconds. Denominator rules matter: excluding all timeouts, failed authentication attempts, or peak-load requests can make a broken service appear healthy. Monitor dependency failures and degraded modes separately so that the reason for an outcome remains diagnosable.

For a repairable service in a simplified stationary regime, availability can be approximated as `A = MTBF/(MTBF + MTTR)`. With mean time between failures of 200 hours and mean repair time of 2 hours, the approximation gives `200/202 ≈ 99.01%`. This does not predict end-to-end service availability when failures are dependent, recovery is nonstationary, or planned downtime is treated differently. MTBF is not necessarily a valid measure for software defects that activate under particular inputs. Event-based reliability, demand profiles, and dependency analysis may be more meaningful.

### Error budgets link operating risk to change policy

If an objective permits at most 0.5% unsuccessful requests over a defined month, then 200,000 eligible requests permit 1,000 unsuccessful requests under a count-based interpretation. This is an **error budget**, not permission to disregard individual safety-critical failures. Burning 800 errors in a major release can justify restricting additional risky deployments while investigations occur. Yet a purely monthly aggregate conceals bursts: 800 errors concentrated in five minutes may be unacceptable to riders even if the monthly budget is technically met. Combine service objectives with incident severity, time-window constraints, and safety requirements.

A release decision can be framed as an expected-loss trade. New software may add mission value while exposing the service to regression risk. The expected benefit of deploying now must be compared with the expected loss from faults, recovery cost, and the value of collecting more evidence. This is not reducible to “deploy faster” or “never deploy while any defect exists.” Reversibility matters: feature flags, staged rollouts, tested rollback paths, and data-migration compatibility lower the cost of a mistaken decision. Rollback is not guaranteed when irreversible database or physical-world actions have already occurred.

### Reliability engineering requires feedback with trustworthy provenance

A credible incident record identifies triggering conditions, version, dependency state, detection method, impact, operator actions, and how confidence in the cause was obtained. Logs that aggregate only successful transactions create survivorship bias. Monitoring should distinguish a failure to execute a function from a failure to observe it. Alert thresholds must balance false alarms and delayed detection, and on-call response capacity must be part of the design. High alert volume can itself increase repair time through fatigue and context switching.

Operations completes the lifecycle evidence loop: incidents update hazards, requirements, architecture assumptions, regression tests, and field restrictions. The boundary of inference is important. A week without incidents demonstrates little about a rare hazard when exposure is small or reporting is incomplete. Operational reliability is earned through explicit definitions, sustained exposure evidence, controlled change, and an organization empowered to act on adverse findings.

## Continuity

This chapter builds from [previous chapter](10-design-testing-ci-and-an-integrated-software-.md) and leads toward [next chapter](12-assess-technology-trends-and-defend-the-integ.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w11.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
