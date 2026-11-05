# Concept of operations and scenarios

**Reference entry · Foundations and management · Expanded reference**

## Definition and diagnostic distinction

A **concept of operations (ConOps)** describes how people, equipment, software, supporting organizations, and external services jointly achieve a mission under specified conditions. It is not a feature list and it is not a design specification. A scenario makes a particular operational thread inspectable: the triggering situation, actors, environmental state, sequence of decisions, exceptional branches, and observable outcome. A use case may isolate a software interaction; a ConOps must also account for the physical operation and institutional responsibilities that make the interaction meaningful.

## Theory: operational threads expose hidden requirements

Describe a scenario as **(initial state, trigger, actors, environment, actions, exceptions, terminal state, measures)**. The initial state includes prior commitments and resource availability; the terminal state includes not only success but degraded, aborted, and recovery conditions. A mission measure needs a defined population and denominator. For a demand-response transit system, define the probability of timely service as `P(wait <= 8 minutes | eligible request during peak)`. If requests are discarded by a failing app before logging, the measured denominator is biased: apparent service improves exactly when access deteriorates.

A scenario set is a **coverage argument**, not an enumeration of every possible story. Cross important dimensions—demand, degraded infrastructure, accessibility needs, operator workload, weather, and cyber conditions—then select combinations informed by hazard and mission consequence. Pairwise coverage can reveal common interactions but cannot guarantee rare three-way failures. Transition tables distinguish commanded modes (normal, restricted, emergency) from transient states within a mode. Decision authority must be attached to each transition; otherwise the story relies on an imaginary all-knowing operator.

## Worked example: demand becomes a design obligation

A campus shuttle ConOps defines a weekday peak with 180 eligible requests, a severe-weather restriction mode, and a manual-dispatch fallback. In a pilot, 158 requests are served within eight minutes, 16 later, and 6 are never served. The timely-service estimate is `158 / 180 = 87.8%`; using only completed trips would incorrectly report `158 / 174 = 90.8%`. If the mission target is at least 95%, the design fails under this scenario. The scenario points toward explicit availability requirements for request intake, fallback dispatch, and accessible-vehicle allocation, rather than merely a faster routing algorithm.

## Engineering use and evidence

Write a normal thread, at least one credible off-nominal thread, and a recovery thread for each critical mission. Annotate who observes each condition, what information can be stale, and which decisions are automated. Link scenario steps to functions, interface exchanges, human tasks, hazards, requirements, and test cases. Validate the narratives with actual operators and affected users; a technically coherent storyboard can still misrepresent real work. Evidence includes walkthrough records, scenario coverage rationale, demand data, and a change log showing which architectural decisions were driven by which scenario.

## Limitations and connections

A ConOps is a hypothesis about use, not proof of utility. It can overrepresent articulate stakeholders and ideal operations. Stress it against nonusers, maintenance staff, emergency responders, and people excluded from normal instrumentation. Connect it to **system boundaries**, **stakeholder needs**, **metrics**, **requirements**, and **verification design**; each downstream claim should retain the operational conditions that gave it meaning.

## Technical analysis: scenarios as testable operational hypotheses

ConOps scenarios should be selected to expose distinct mission decisions and failure modes. A normal scenario, a degraded scenario, and a recovery scenario generally require different actors, data quality, authority, and success criteria. Specify the **population at risk** for each metric, including attempts that fail before the system creates an internal request record.

Consider **180 eligible** dispatch requests during a storm. **150** meet the service target, **20** arrive late, and **10** never enter the dispatch queue because the app is unavailable. A system that counts only its **170 accepted** requests reports `150/170 = 88.24%` timely service. The mission-level figure is `150/180 = 83.33%`. The **4.90 percentage-point** gap reflects boundary choice, not a discrepancy to average away. Even this larger denominator is not sufficient if eligible users who cannot access the app are not observed.

**Evidence boundary.** Require operational actors to review exceptional paths and human handovers. Trace each scenario to measures, functions, interfaces, hazards, and acceptance evidence. A scenario is a structured hypothesis about use; it must not silently become a requirements source without stakeholder validation.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Stakeholder expectations and ConOps are developed using mission scenarios, including off-nominal and human interactions. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.1 Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) · *direct guidance*.
- **C2:** Baselined concepts of operation and enabling support strategies inform technical requirements. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.2 Technical Requirements Definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [NASA · Systems Engineering Handbook appendix (requirements and verification matrices)](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) — Requirements review criteria and verification planning context.

## Follow the knowledge

**Related concepts**

- [System of interest: purpose, boundary, and evidence](system-of-interest.md)
- [Stakeholders, needs, and value: translating plural interests into engineering decisions](stakeholders-and-needs.md)
- [Requirements: precise obligations, not persuasive sentences](good-requirements.md)
- [Measures of effectiveness and performance](metrics-hierarchy.md)

**Go deeper in the 240-chapter textbooks**

- [Book 1, Chapter 03: Chapter 3 — Turn conflicting human needs into an operational concept](../B1/chapters/03-needs-and-conops.md)
- [Book 6, Chapter 03: Book 6 · Chapter 3: ConOps and mission measures](../B6/chapters/03-desired-end-state-conops-scenarios-and-mission-calculat.md)
- [Book 16, Chapter 10: Week 10 · Foundations of Digital and Mission Engineering · Book chapter: Mission engineering foundations and mission architecture](../B16/chapters/10.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
