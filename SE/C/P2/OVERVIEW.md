> **New complementary teaching volume:** [36 Phase 2 Markdown chapters](../../K/P2-text/README.md) · [Offline searchable Phase 2 website](../../K/P2-text/OPEN-PHASE-2.html). The three original course guides remain authoritative for complete assessment work.

# Phase 2 — Core systems-development lifecycle

Phase 2 is the curriculum's principal realization chain. It takes a system from a defensible concept decision through design maturation and integration, then into verification, validation, test, evaluation, and readiness judgment.

The phase is intentionally cumulative:

1. **EN.645.767 — System Conceptual Design** reopens the problem, develops operational and functional baselines, explores alternatives, and selects a concept.
2. **EN.645.768 — System Design & Integration** transforms that concept into a controlled design, interface, integration, and technical-management baseline.
3. **EN.645.769 — System Test & Evaluation** develops and evaluates the evidence needed to determine whether the realized system meets requirements and operational needs.

The current JHU course descriptions and planning material treat these subjects as a connected lifecycle sequence. The self-study curriculum therefore requires the courses to be completed in order and uses one continuing program case. [JHU-767] [JHU-768] [JHU-769]

## Phase purpose

By the end of Phase 2, the learner should be able to:

* frame and investigate an operational problem without prematurely selecting a solution;
* formulate needs, scenarios, measures, conceptual requirements, and logical architecture;
* generate and compare credible physical concepts under performance, affordability, schedule, uncertainty, and risk;
* mature a selected concept into a design baseline;
* define and control interfaces across technical and organizational boundaries;
* plan integration build-up, technical reviews, customer involvement, and technical management;
* construct a verification and validation strategy tied to requirements and stakeholder expectations;
* plan and interpret developmental, integration, environmental, operational, and acceptance testing;
* analyze discrepancies, limitations, residual risk, and evidence sufficiency;
* make and defend proceed, conditional-proceed, rework, or stop recommendations.

## Required course order

1. [**EN.645.767 — System Conceptual Design**](EN645767.md)
2. [**EN.645.768 — System Design & Integration**](EN645768.md)
3. [**EN.645.769 — System Test & Evaluation**](EN645769.md)

Do not reorder the chain. EN.645.768 should receive a controlled conceptual baseline from EN.645.767, and EN.645.769 should receive the design, interface, integration, and V&V planning products from EN.645.768.

## Entry requirements

Before beginning Phase 2, the learner should have completed Phase 0 and Phase 1 or demonstrate equivalent competence in:

* systems thinking, lifecycle reasoning, requirements, architecture, interfaces, risk, configuration, and technical reviews;
* project governance, WBS, schedule, cost, earned-value basics, risk, and change control;
* model-based traceability across needs, requirements, behavior, structure, and verification;
* object-oriented and software-system analysis sufficient to judge software feasibility and architecture implications;
* spreadsheet and basic computational analysis;
* technical writing, review facilitation, and oral defense.

EN.645.767 includes a formal readiness diagnostic. Failing it should trigger the specified bridge work rather than silent continuation.

## Common running case

Phase 2 continues the **Autonomous Campus Mobility 2030** program.

The case is used differently in each course:

### EN.645.767 — concept recompetition

The earlier autonomous-shuttle baseline is treated as an incumbent proposal, not as the answer. The learner must reopen the problem and consider human-driven, fixed-route, partnership, hybrid, and bounded-autonomy concepts. The output is a selected conceptual baseline plus a retained alternative and explicit conditions.

### EN.645.768 — design and integration

The selected concept becomes the starting point for design maturation. The learner develops subsystem and discipline views, interfaces, enabling systems, design decisions, a SEMP, integration strategy, V&V planning, customer feedback, and review readiness.

### EN.645.769 — test and evaluation

The designed system becomes the test article and operational capability under evaluation. The learner defines critical test parameters, test architecture, environments, developmental and operational events, discrepancy processes, data analysis, and readiness recommendations.

## Baseline-continuity policy

Each course must import the prior baseline with a formal receiving review. Imported artifacts must be classified as:

* **baselined** — approved for use unless changed through control;
* **conditional** — usable only under named assumptions or actions;
* **reference** — informative but not authoritative;
* **retained alternative** — preserved as a hedge or fallback;
* **open** — unresolved and assigned for closure.

A downstream course may change a prior decision, but only through recorded change impact, updated evidence, and review approval. It may not quietly replace earlier requirements, values, architecture, or assumptions.

## Shared review spine

| Course | Review | Primary decision |
|---|---|---|
| EN.645.767 | Problem Definition Review | Is the study frame neutral, evidence-based, and decision-ready? |
| EN.645.767 | Functional Architecture Review | Is the logical baseline sufficient for concept generation? |
| EN.645.767 | Down-select Review | Is the preferred concept robust to values and uncertainty? |
| EN.645.767 | Concept Validation/Baseline Review | Should the concept proceed to detailed design, and under what conditions? |
| EN.645.768 | System Requirements/Design Review | Is the specification-to-design chain coherent and mature? |
| EN.645.768 | Interface and Integration Readiness Review | Are interfaces, enabling products, environments, and build-up plans ready? |
| EN.645.768 | Preliminary/Critical Design-style reviews | Is the design sufficiently mature to implement and integrate? |
| EN.645.769 | Test Readiness Review | Are articles, environments, procedures, instrumentation, data, and safety controls ready? |
| EN.645.769 | Verification/Validation Evidence Review | Does the evidence support requirement and stakeholder claims? |
| EN.645.769 | Operational Readiness Recommendation | Should the system proceed, proceed conditionally, rework, or stop? |

Review names are educational approximations. The decision criteria and evidence matter more than matching one organization's exact gate terminology.

## Shared artifact chain

The phase should produce a continuous evidence chain:

> problem and opportunity  
> → stakeholders and needs  
> → ConOps and scenarios  
> → objectives, MOEs, MOPs, and thresholds  
> → conceptual requirements  
> → functional architecture  
> → physical concept alternatives  
> → quantitative decision and risk evidence  
> → selected concept baseline  
> → design decomposition and interfaces  
> → implementation and integration baseline  
> → verification and validation plan  
> → test procedures and data  
> → discrepancy and corrective-action evidence  
> → readiness recommendation

Every major claim should be traceable upstream to rationale and downstream to planned or actual evidence.

## Phase-wide engineering rules

1. **Do not confuse document completion with technical maturity.**
2. **Do not let the favored concept determine the measures used to select it.**
3. **Do not accept screenshots as the only source for models or calculations.**
4. **Do not treat a requirement as verified because a test was run; evaluate the result and evidence quality.**
5. **Do not treat operational validation as a synonym for requirement verification.**
6. **Record assumptions, dissent, waivers, and limitations.**
7. **Use ranges and sensitivity where point values imply false precision.**
8. **Include operators, maintainers, users, accessibility, safety, security, privacy, support, and transition concerns throughout the chain.**
9. **Preserve configuration and change history across course boundaries.**
10. **Require oral defense and receiving-team acceptance at each final handoff.**

## Workload and pacing

A fully expanded Phase 2 course is designed for approximately **10–13 hours per week**, with review and capstone weeks occasionally requiring more. Learners completing the program alongside full-time work may use a 16–18 week pace per course.

Do not overlap the three courses unless the learner is using a real project with adequate mentoring and can preserve baseline discipline. Starting test planning early is good systems engineering; beginning EN.645.769 before the EN.645.768 design and integration baseline exists is not.

## Current development status

| Course | Status | Last major revision |
|---|---|---|
| EN.645.767 System Conceptual Design | **Fully expanded** | 2026-08-05 |
| EN.645.768 System Design & Integration | **Fully expanded** | 2026-08-05 |
| EN.645.769 System Test & Evaluation | **Fully expanded** | 2026-08-05 |

All three Phase 2 courses are fully expanded. “Fully expanded” means the course includes a complete specification, readiness diagnostic, detailed weekly learning outcomes and readings, worked examples, guided and independent exercises, deliverable specifications, rubrics, mastery gates, formal reviews, a capstone, and handoff requirements.

## Phase exit criteria

Phase 2 is complete when the learner can present a controlled portfolio showing:

* a defensible concept decision with alternatives, uncertainty, affordability, schedule, and risk;
* a coherent design and interface baseline;
* an integration and enabling-system strategy;
* a requirement-linked V&V and T&E architecture;
* actual or realistically simulated test data and discrepancy analysis;
* configuration, change, review, and corrective-action records;
* a readiness recommendation with residual risk and limitations;
* an oral defense that connects the entire evidence chain.

## Course files

* [EN.645.767 — System Conceptual Design](EN645767.md)
* [EN.645.768 — System Design & Integration](EN645768.md)
* [EN.645.769 — System Test & Evaluation](EN645769.md)

[Back to program README](OVERVIEW.md)

## References

[JHU-767]: https://ep.jhu.edu/courses/645767-system-conceptual-design/ "JHU — System Conceptual Design"
[JHU-768]: https://ep.jhu.edu/courses/645768-system-design-integration/ "JHU — System Design & Integration"
[JHU-769]: https://ep.jhu.edu/courses/645769-system-test-evaluation/ "JHU — System Test & Evaluation"
