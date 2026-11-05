# Chapter 8 — Performance and security share resource budgets

*Book V: Software Systems Engineering · Week 8 — Specify and analyze performance, networking, real-time, security, and privacy constraints*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 8](../labs/lab-08-specify-and-analyze-performance-networking-re.md) before attempting [the assessed Week 8 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w08.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **specify and analyze performance, networking, real-time, security, and privacy constraints** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Performance must be measured as a distribution under workload, not one benchmark number. Network delay, queueing and tail behavior affect user experience; security controls consume time and resources but also shape architecture. Identify threat boundaries, least-privilege roles, retention policies and failure-safe defaults. Never optimize latency by disabling required authorization.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Performance and security compete for the same scarce resources

Throughput, latency, confidentiality, integrity, and availability are often taught as separate quality attributes, yet they share processors, network capacity, queues, memory, and operational staff. Authentication, encryption, inspection, and logging consume resources. A security control can make the system safer against one threat while increasing latency or creating a centralized failure point. Conversely, disabling controls to satisfy a latency benchmark changes the system being evaluated.

Budget analysis should therefore identify the **operating scenario** and allocate resources and delay across the complete request path. A component's 95th-percentile latency does not simply add to another component's 95th percentile to produce an end-to-end percentile without assumptions about dependence. Nor can average throughput establish tail latency in a bursty system. The architecture problem is to manage coupled constraints and measure the right whole-system outcome, not to optimize isolated components until their local dashboards are green.

## Deeper theory: throughput, tail latency, and security constraints share one architecture

### Service capacity is a nonlinear property

A performance model needs arrival rates, service capacities, scheduling policies, resource sharing, and the shape of demand variability. For a simplified single-server system with Poisson arrivals and exponential service times, utilization is `rho = lambda / mu` and mean time in the system is `W = 1 / (mu - lambda)` when `lambda < mu`. As utilization approaches one, expected delay grows sharply. This is a property of the model's stochastic assumptions, not a universal formula for every software system. The general implication survives: little spare capacity under variable demand often causes disproportionate waiting and deadline failures.

Little's law, `L = lambda × W`, relates long-run average concurrency, throughput, and time in system for a stable system with consistent boundaries. It does not establish causality by itself and does not excuse ignoring dropped requests, timeouts, or retries. A load test reporting attractive response times while excluding failed or abandoned requests can make a capacity problem invisible by changing the denominator.

### Tail behavior matters when services compose

An end-to-end request may cross authentication, routing, dispatch, database, and telemetry services. Even if each component usually responds quickly, occasional slow stages create long tail latency. Shared infrastructure introduces correlations: high traffic may simultaneously exhaust thread pools, delay database access, and trigger additional retries. A service-level objective stated at the 99th percentile needs an explicit workload, observation interval, timeout policy, and treatment of failures. Adding individual 99th-percentile latencies does not automatically produce the system's 99th percentile.

Retry policies are a common feedback mechanism. When a slow service triggers retries, extra work can raise utilization further and cause additional timeouts. Backoff, admission control, circuit breakers, and load shedding attempt to interrupt this loop. Their correctness depends on a business distinction between requests that may be refused and safety-critical commands that must be serviced or moved to a safe alternative path.

### Security measures alter resource and failure models

Authentication, encryption, auditing, and access controls consume computation, storage, network capacity, and operator attention. Removing them to meet a performance target is not a valid optimization if it violates a security constraint. Conversely, strong controls implemented as a single fragile central dependency may reduce service availability under an identity-provider outage. Security and reliability should be co-designed through threat scenarios, trust boundaries, failure modes, and resource budgets rather than evaluated by separate teams after implementation.

A denial-of-service adversary changes the arrival process from benign stochastic demand to potentially adaptive overload. A benchmark assuming independent requests at a fixed rate may be irrelevant to that threat. Defensive controls such as rate limits and quotas must also respect accessibility and emergency-service priorities; otherwise a security mechanism can become an operational hazard.

### Measurements require causal interpretation

A faster benchmark does not necessarily mean a better architecture. Caching may reduce average latency yet serve stale vehicle availability; aggressive batching may improve throughput yet delay urgent events; asynchronous acknowledgments may appear fast while actual completion time worsens. Every performance claim should define when the clock starts, when it stops, which transactions are included, and what successful completion means. A credible design balances throughput, delay distributions, fault tolerance, trust, and the cost of degraded operation under a single system-level argument.

## Worked Northstar example

If offered load is 110 jobs/min and a service can complete 100 jobs/min, backlog grows by roughly 10 jobs/min under this simplified assumption. Improving median request processing time does not fix a sustained capacity deficit. Enabling extra workers helps only if a downstream database is not the real bottleneck.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### Stability versus a flattering benchmark

A simple workload balance is `backlog_growth = arrival_rate − completion_rate` when the difference is positive. At **110 requests/minute** arriving and **100 requests/minute** processed, average backlog grows around **10 requests/minute** under a stationary deterministic approximation; after six minutes, roughly 60 requests await service if the queue started empty. Median response time measured before saturation says little about steady-state operability.

Model queueing conditions and tail latencies under authentication, TLS and normal logging. Different distribution tails, bursts and service variability can make actual queues grow faster during congestion; explain which assumptions belong to the approximation.

## What can go wrong—and why

A performance test conducted with authentication disabled cannot support claims about the deployed secured system.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 8: Performance and security share resource budgets](../labs/lab-08-specify-and-analyze-performance-networking-re.md), you will: Design a load/privacy test plan with p95 latency, throughput, authorization checks, retention rules and a saturation scenario. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 8 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](07-engineer-cloud-service-distributed-and-config.md) and leads toward [next chapter](09-build-the-dependability-safety-resilience-and.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w08.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Advanced worked practice

- [Deep workshop — Performance Budgets, Queueing Tails, and Quality Attributes](../practice/slo.md)
- [Corresponding independent laboratory](../practice/lab-slo.md)
- [Interactive workbench](../practice/WORKBENCH.html)
