# Phase 1 — Modeling and Software Companion Textbook (v1.0)

**36 complementary chapters | 3 courses | 36 worked shuttle examples | 108 retrieval questions with explained answers | 8 deeper concept essays | 4 Python learning tools | 9 editable CSV worksheets.**

This first-pass textbook is designed to sit beside, not replace, your original Phase 1 courses. The original guides define full assignments, readings, rubrics and mastery gates. The companion concentrates on meaning, model semantics, concrete reasoning, common failure modes and small reproducible exercises. All examples, values, designs and tests are synthetic learning material, **not production-grade or safety-approved**.

**Start with the offline reader:** [Open the website](OPEN-PHASE-1.html) (self-contained content and search, no server needed). The Markdown sources remain editable and portable. If reading the HTML outside the extracted ZIP, its links to CSV/Python/older guide files only work after placing it back in the expected directory.

## Courses and weekly explanations

### EN.645.631 — Introduction to Model Based Systems Engineering

01. [EN.645.631, Week 01 — MBSE value, model purpose, and the document-to-model transition](lessons/645-631-w01.md)
02. [EN.645.631, Week 02 — Modeling plan, methodology, language, tool, and repository architecture](lessons/645-631-w02.md)
03. [EN.645.631, Week 03 — Stakeholders, concerns, needs, context, ConOps, and operational scenarios](lessons/645-631-w03.md)
04. [EN.645.631, Week 04 — Requirements modeling, relationship semantics, and traceability](lessons/645-631-w04.md)
05. [EN.645.631, Week 05 — Behavior modeling: use cases, activities/actions, interactions, states, and modes](lessons/645-631-w05.md)
06. [EN.645.631, Week 06 — Structure, interfaces, ports, connections, and the midcourse model review](lessons/645-631-w06.md)
07. [EN.645.631, Week 07 — Logical architecture, functional allocation, derived requirements, and consistency](lessons/645-631-w07.md)
08. [EN.645.631, Week 08 — Values, units, measures, constraints, parametrics, and analysis integration](lessons/645-631-w08.md)
09. [EN.645.631, Week 09 — Candidate physical architectures, model-based trades, and alternative evaluation](lessons/645-631-w09.md)
10. [EN.645.631, Week 10 — Verification and validation modeling, configurations, events, and coverage](lessons/645-631-w10.md)
11. [EN.645.631, Week 11 — Model quality, queries, reports, change impact, governance, and SysML transition](lessons/645-631-w11.md)
12. [EN.645.631, Week 12 — Integrated model baseline, capstone review, oral defense, and lessons learned](lessons/645-631-w12.md)

### EN.605.704 — Object-Oriented Analysis and Design

01. [EN.605.704, Week 01 — Establish the OOAD problem, scope, and modeling discipline](lessons/605-704-w01.md)
02. [EN.605.704, Week 02 — Elicit and structure software requirements](lessons/605-704-w02.md)
03. [EN.605.704, Week 03 — Capture functional requirements with use cases and scenarios](lessons/605-704-w03.md)
04. [EN.605.704, Week 04 — Discover candidate classes and build the static analysis model](lessons/605-704-w04.md)
05. [EN.605.704, Week 05 — Analyze dynamic behavior and discover collaborations](lessons/605-704-w05.md)
06. [EN.605.704, Week 06 — Model state-dependent behavior and conduct the Analysis Model Review](lessons/605-704-w06.md)
07. [EN.605.704, Week 07 — Assign responsibilities and build the static design model](lessons/605-704-w07.md)
08. [EN.605.704, Week 08 — Realize use cases with dynamic design models](lessons/605-704-w08.md)
09. [EN.605.704, Week 09 — Apply design patterns with restraint](lessons/605-704-w09.md)
10. [EN.605.704, Week 10 — Express precise constraints with OCL and execute a change red-team](lessons/605-704-w10.md)
11. [EN.605.704, Week 11 — Design persistence and conduct the Design Readiness Review](lessons/605-704-w11.md)
12. [EN.605.704, Week 12 — Baseline and defend the integrated OOAD design](lessons/605-704-w12.md)

### EN.645.764 — Software Systems Engineering

01. [EN.645.764, Week 01 — Define the software systems engineering role and establish the baseline](lessons/645-764-w01.md)
02. [EN.645.764, Week 02 — Model software allocations, interfaces, and the digital thread](lessons/645-764-w02.md)
03. [EN.645.764, Week 03 — Interpret and critique the system model for software realization](lessons/645-764-w03.md)
04. [EN.645.764, Week 04 — Frame the software architecture within the system architecture](lessons/645-764-w04.md)
05. [EN.645.764, Week 05 — Integrate agile product engineering with systems evidence](lessons/645-764-w05.md)
06. [EN.645.764, Week 06 — Design and evaluate architecture with quality attributes](lessons/645-764-w06.md)
07. [EN.645.764, Week 07 — Engineer cloud, service, distributed, and configurable architectures](lessons/645-764-w07.md)
08. [EN.645.764, Week 08 — Specify and analyze performance, networking, real-time, security, and privacy constraints](lessons/645-764-w08.md)
09. [EN.645.764, Week 09 — Build the dependability, safety, resilience, and supply-chain case](lessons/645-764-w09.md)
10. [EN.645.764, Week 10 — Design testing, CI, and an integrated software V&V evidence chain](lessons/645-764-w10.md)
11. [EN.645.764, Week 11 — Manage delivery, operations, maintenance, evolution, and incidents](lessons/645-764-w11.md)
12. [EN.645.764, Week 12 — Assess technology trends and defend the integrated software baseline](lessons/645-764-w12.md)

## Cross-cutting tools and learning paths

- [Eight deep-dive concept essays](deep-dives/) — see links below.
  - [From diagrams to a semantically controlled model](deep-dives/model-meaning.md)
  - [Operational scenarios, use cases and software responsibilities](deep-dives/operational-to-software.md)
  - [SysML v1 and v2: conceptual continuity, not cosmetic conversion](deep-dives/sysml-versions.md)
  - [State machines, invariants and precise behavioral contracts](deep-dives/behavior-and-contracts.md)
  - [Distributed systems: timeouts, duplicates and eventual knowledge](deep-dives/distributed-uncertainty.md)
  - [Quantitative performance and reliability without misleading averages](deep-dives/quantitative-qualities.md)
  - [Change impact, provenance and controlled evidence](deep-dives/trace-change.md)
  - [Security, safety and release evidence as structured claims](deep-dives/assurance.md)
- [Cross-course learning threads](KNOWLEDGE-THREADS.md)
- [Integrated shuttle case study](INTEGRATED-CASE.md)
- [Concept glossary](GLOSSARY.md)
- [Resource shelf](RESOURCE-SHELF.md)
- [Python tools and 12 tests](tools/README.md)
- [Editable templates](templates/)
- [Week-to-chapter crosswalk CSV](PHASE-1-CROSSWALK.csv)
- [Illustrated model maps](diagrams/)

## Recommended use for each week

Read the new companion explanation, reproduce the worked example, attempt three retrieval questions before expanding the answers, complete the mini-exercise and then execute the original guide's full assessment. Review the relevant deep-dive essay when you encounter a conceptual barrier. Cross-link your work to the Phase 0 artifacts rather than starting a separate ungoverned model.

## Status and limitations

**Full weekly topic coverage is not encyclopedic completeness.** These are first-pass conceptual chapters and illustrative implementations, not exhaustive graduate-level treatises or substitutes for assigned standards, textbooks, model-tool practice, domain expertise, peer review, or independent assurance. The offline website has no external dependencies for reading and search; third-party references still require access to those sites. The Python labs are intentionally simplified and should never control actual vehicles or production services.
