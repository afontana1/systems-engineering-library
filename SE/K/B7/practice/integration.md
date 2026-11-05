# Advanced Workshop · Reliability Allocation, Common Cause, and Integration Evidence

*Book 7 · Week 9 · series reliability · redundancy · common-cause failure · incremental integration*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-integration.md). The assessed course obligations remain in [the curriculum](../../../C/P2/EN645768.html).

## 1. A collection of dependable components may still be unreliable

Mission success depends on the structure of the system and its failure modes. Three essential elements arranged in series each need to operate for the mission to succeed; their failure opportunities accumulate. When component successes are independent, system availability for a series path is the product of element availabilities. For values 0.99, 0.98 and 0.995, the result is

\[
A_{\mathrm{series}}=0.99(0.98)(0.995)=0.965349.
\]

The result is approximately 96.53%. It is not permissible to multiply availability numbers when failures share a power supply, software image, network, common maintenance window or other dependency without examining the effect of that dependence. The calculation also presumes the stated availability applies to the same observation period and operational definition.

## 2. Redundancy works only when failure modes differ

Two independent identical components, each available with probability \(a\), provide parallel availability \(A_{\parallel}=1-(1-a)^2\) when either component can fulfill the function and switching is effective. At \(a=.98\), this equals 0.9996. It is tempting to call that “four nines,” but shared dependencies can dominate.

Introduce a stylized common-cause outage with probability \(c=.01\) that makes both redundant components unavailable. Conditional on no common-cause outage, suppose their failures are independent. Then

\[
A_{\parallel,cc}=(1-c)\,[1-(1-a)^2]=0.989604.
\]

That is only about 98.96% for the redundant function, despite excellent nominal independent redundancy. The event model is deliberately simplified: real common-cause processes may be time-dependent and partially overlapping, and failover has nonzero detection and recovery delay. The engineer should not treat \(c\) as known without relevant evidence.

## 3. From probability arithmetic to failure logic

A fault tree starts with an unacceptable **top event**, such as “dispatch cannot provide authorized route guidance during the operating window.” Then it decomposes conditions connected by AND/OR gates. Minimal cut sets show the smallest combinations of basic events sufficient for the top event under the model. A shared data center outage can be a single-event cut set that defeats duplicated application instances. It may be more important than a second copy of an already reliable component.

Failure Mode and Effects Analysis starts from potential element failure modes and propagates their local and system effects. The methods complement each other: fault trees reason backward from loss of function, while FMEA reasons forward from element failures. Neither method proves completeness. Human operations, maintenance access, cyber incidents and software common-mode defects need explicit coverage where relevant.

## 4. Integration should reduce uncertainty stage by stage

A responsible integration sequence exercises interfaces in an order designed to expose faults early. Start with contract tests and controlled stubs, then hardware/software integration under known fixtures, then faulted interactions, then full mission scenarios. Freeze or identify the configuration for each result. A subsystem result can support a particular local claim without proving integrated performance; that distinction should appear in the evidence register.

For Northstar, sequence test of message validity and freshness before integrated dispatch timing. Then test dispatch against a vehicle simulator, then a real vehicle interface (in an authorized safe test setting), then end-to-end scenarios with deliberate telemetry loss. A new route-planner version that changes timestamp semantics may invalidate prior integrated results even if the API schema remains unchanged.

## 5. Engineering acceptance, not numerical theater

The goal is an evidence-backed judgment about the operating scenario, not the largest reliability number on a slide. Describe the boundary, failure dependence, maintenance and recovery assumptions, test configurations, observed defects, and unresolved hazards. If common-cause behavior is poorly known, report conditional ranges and propose evidence gathering instead of a single precise release claim.

## Worked problem set — attempt before revealing solutions

### Problem 1

Compute series availability for .99, .98, and .995.

<details><summary>Show solution 1</summary>

.99×.98×.995 = .965349, or 96.5349%, under the independence and consistent-period assumptions.

</details>

### Problem 2

For two independent .98-available components, calculate parallel availability.

<details><summary>Show solution 2</summary>

1 − (1−.98)² = .9996, provided either component can provide service and failure independence holds.

</details>

### Problem 3

Introduce independent common-cause outage probability .01 as a gating event. Compute adjusted parallel availability.

<details><summary>Show solution 3</summary>

(1−.01)×.9996 = .989604. The common-cause gate reduces the result to about 98.96%.

</details>

### Problem 4

Why can successful unit tests not justify end-to-end readiness?

<details><summary>Show solution 4</summary>

They do not establish interface semantics, coupled failures, operating conditions, fault recovery, or configuration-specific mission effectiveness. Integrated evidence is additionally required.

</details>

## Independent transfer to the Northstar case

Use `book7.py` to compare the three-element series path with redundant middle element, both with and without a shared power outage. Write a fault tree with a single-point common-cause cut set. Draft a staged integration sequence with contract tests, simulated dependencies, degradation tests, and end-to-end evidence. Include test IDs and an explicit acceptance limitation.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-integration.md) · [Python source](book7.py) · [Experiment dataset](book7-interfaces.csv) · [Interactive workbench](WORKBENCH.html).
