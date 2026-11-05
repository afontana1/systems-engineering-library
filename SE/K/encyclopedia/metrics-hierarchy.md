# Measures of effectiveness and performance

**Reference entry · Analytics, modeling, simulation and decisions · Expanded reference**

## Definition and diagnostic distinction

A **measurement hierarchy** connects stakeholder outcomes to system measures of effectiveness (MOEs), technical measures of performance (MOPs), and management indicators. MOEs assess whether a mission or service outcome is achieved; MOPs characterize how a design behaves; internal leading indicators measure conditions that may influence future outcomes. Confusing these levels creates optimization of easily measured activity rather than meaningful value.

## Theory: measurement is a causal model

Define a measure as `(construct, population, operational definition, unit, denominator, sampling window, instrument, uncertainty, decision threshold)`. An indicator is valuable when its causal relationship to the objective is credible. Throughput, utilization, and average latency are not interchangeable with equitable access, mission completion, or hazard reduction. Surrogate measures create **Goodhart risk**: once a proxy becomes a target, teams may improve the proxy without improving the intended outcome.

Ratios need stable denominators. On-time percentage per completed trip differs from on-time percentage per request; a performance metric conditional on successful service can improve while more requests are abandoned. Disaggregation can expose disparities hidden by aggregate means. When combining multiple measures into a value score, normalize attributes and check preference independence and double counting rather than adding arbitrary weights.

## Worked example: the attractive but misleading dashboard

A transit operation handles 200 eligible requests. In period A, 180 are on time, 10 late, and 10 unserved, giving 90% on-time over all requests. After an optimization, 175 are on time, 5 late, and 20 unserved: average travel time for completed rides improves, but timely service drops to 87.5% overall. A dashboard showing only completed-ride speed reports success. A meaningful hierarchy preserves the mission MOE, exposes unserved demand, and uses technical speed metrics only as explanatory drivers.

## Engineering use and evidence

For each measure, document the operational question and what decision follows a threshold crossing. Evaluate instrument resolution, missing data, sample selection, seasonality, and incentive effects. Use leading metrics to diagnose change but retain lagging outcome measures for validation. Test whether a plausible intervention can change the displayed metric without changing the actual mission; if so, redesign the measure or add controls.

## Limitations and connections

All measurement systems select whose experience is visible. Numerical precision does not guarantee construct validity. Connect metrics to **stakeholder needs**, **ConOps**, **test evidence**, **process improvement**, and **multiattribute decisions**.

## Technical analysis: a metric needs a unit of analysis and a causal claim

Measures of effectiveness (MOEs) concern whether a mission outcome matters to stakeholders; measures of performance (MOPs) describe technical behavior; technical performance measures (TPMs) monitor selected design parameters against planned trajectories. These levels are related, not interchangeable. A low dispatch latency may coexist with poor passenger access when the intake channel is unavailable.

Suppose a service handles **990 of 1,000 eligible requests**, with **950** of the handled requests meeting its time target. Conditional on acceptance, reported punctuality is `950/990 = 95.96%`. Across eligible demand it is `950/1000 = 95.0%`. If requests that fail before logging are not represented among the 1,000, *both* metrics can be biased. Show the numerator, denominator, exclusion rules, time window, and configuration beside any KPI.

**Evidence boundary.** Use outcome measures to test whether a performance improvement is useful, and lagging safety indicators to detect harm. A TPM trend crossing its margin is a management signal, not proof the product violates a released requirement until its operational conditions and acceptance rules are checked.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Measures of effectiveness reflect stakeholder mission success criteria in the stakeholder expectations process. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.1 Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) · *direct guidance*.
- **C2:** Technical assessment uses measures of effectiveness, performance, and technical performance indicators for monitoring. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.7 Technical Assessment](https://www.nasa.gov/reference/6-7-technical-assessment/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.

## Follow the knowledge

**Related concepts**

- [Stakeholders, needs, and value: translating plural interests into engineering decisions](stakeholders-and-needs.md)
- [Concept of operations and scenarios](conops-and-scenarios.md)
- [Pareto frontiers and multiobjective decisions](pareto-and-value.md)
- [Process capability and continuous improvement](process-improvement.md)

**Go deeper in the 240-chapter textbooks**

- [Book 10, Chapter 01: Book 10 · Chapter 01 — Define the lifecycle technical-measurement strategy and decision chain](../B10/chapters/01-define-the-lifecycle-technical-measurement-strategy-and-decision-cha.md)
- [Book 6, Chapter 03: Book 6 · Chapter 3: ConOps and mission measures](../B6/chapters/03-desired-end-state-conops-scenarios-and-mission-calculat.md)
- [Book 14, Chapter 02: Book 14 · Chapter 02 — Translate stakeholder values into objectives, measures, and value structure](../B14/chapters/02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
