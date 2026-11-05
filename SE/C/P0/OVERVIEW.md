> **Companion teaching library:** [Phase 0 Concept Textbook](../../K/P0-text/README.md) provides a second explanatory treatment for every week of EN.645.662 and EN.645.667; [offline reader](../../K/P0-text/OPEN-PHASE-0.html). The original 12-week guides below remain the source for graded deliverables and mastery gates.

# Phase 0 — Program foundations, readiness, and sequencing

The original curriculum begins with courses that already assume systems-engineering, project-management, programming, and quantitative knowledge. Phase 0 supplies those dependencies and defines the rules for progressing through the rest of the program. It also serves as the single location for the prerequisite map, recommended sequence, readiness gates, and safe parallelization guidance.

### Prerequisite policy

This revision preserves all 18 originally selected courses and adds two foundation courses that the rest of the curriculum assumes. It distinguishes three kinds of prerequisite:

* **Source prerequisite** — stated in the existing curriculum or on the JHU course page.
* **Self-study prerequisite** — a competency required by this curriculum even when the source course permits instructor approval or lists a looser prerequisite.
* **Recommended preparation** — useful background that improves learning but should not block progress.

The current JHU sources are not perfectly consistent. For example, the current course page for **EN.645.767 System Conceptual Design** lists **EN.645.764 Software Systems Engineering** or permission, while the February 2026 expected-offerings plan summarizes its prerequisites as **EN.645.662 and EN.645.667**. This curriculum therefore uses the stricter union for its linear path: complete 662, 667, and 764 before 767. [JHU-767] [JHU-SE-PLAN]


### Foundation courses

1. [**EN.645.662 — Introduction to Systems Engineering**](EN645662.md)
   Required before every systems-engineering course in the program. Its course file contains the complete specification and 12-week curriculum establishing lifecycle thinking, stakeholder needs, requirements, architecture, technical management, risk, integration, verification, validation, and technical reviews.

2. [**EN.645.667 — Management of Systems Projects**](EN645667.md)
   Required before Software Systems Engineering and the lifecycle core. Its course file contains the complete specification and fully developed 12-week curriculum covering proposal development, scope and work authorization, estimating, scheduling, earned value, integrated project control, risk and change, communications and leadership, technical-performance management, configuration, quality, and agile or hybrid delivery.

The two foundation courses can be studied sequentially or partially in parallel. On the first pass, take **645.662 first**, followed by **645.667**.

### Readiness gates rather than automatic extra courses

**Object-oriented programming gate** — required before EN.605.704. A learner passes by demonstrating basic proficiency with classes, interfaces, inheritance, composition, exceptions, collections, and unit tests in Java, C++, C#, Python, or a comparable language. A learner who does not pass should complete the [4-week OOP readiness bridge](oop-readiness-bridge.md), extending it to 6 weeks when additional programming practice is needed.

**Quantitative and computational gate** — required before the quantitative modeling sequence. A learner passes by demonstrating algebra, functions, introductory calculus, probability, descriptive statistics, confidence intervals, regression basics, spreadsheet analysis, and introductory Python or equivalent computational work. A learner who does not pass should complete the [8-week quantitative and computational bridge](quantitative-and-computational-bridge.md).

**Tooling gate** — recommended before Phase 1. Install and demonstrate basic use of Git, Markdown, a spreadsheet package, Python notebooks, a diagramming tool, and the selected UML/SysML tool.

### Master prerequisite and sequencing matrix

| Course | Source prerequisite in curriculum | Self-study prerequisite | Recommended preparation |
|---|---|---|---|
| EN.645.662 Introduction to Systems Engineering | Not previously included | None | Engineering or technical work context |
| EN.645.667 Management of Systems Projects | Not previously included | 645.662 or concurrent enrollment after completing its functional baseline | Basic project experience |
| EN.645.631 Introduction to MBSE | 645.662 or an alternate introductory SE course | 645.662 | 645.667; tooling gate |
| EN.605.704 OO Analysis and Design | OOP experience | OOP readiness gate | Take before 645.764 |
| EN.645.764 Software Systems Engineering | Introductory SE and Management of Systems Projects, or approval | 645.662 + 645.667 | EN.605.704 |
| EN.645.767 System Conceptual Design | 645.764 or approval in the curriculum/course page; JHU planning table lists 645.662 + 645.667 | 645.662 + 645.667 + 645.764 | 645.631; 645.784 concepts |
| EN.645.768 System Design & Integration | 645.767 or approval | Full core through 645.767 | 645.631 |
| EN.645.769 System Test & Evaluation | 645.768 or approval | Full core through 645.768 | Software testing experience |
| EN.645.757 Foundations of M&S | 645.662 | 645.662 + quantitative gate | 645.767 |
| EN.645.784 Decision Science & Analytics | None stated in the curriculum | 645.662 + quantitative gate | 645.767 |
| EN.645.781 Systems Thinking and Systems Dynamics | 645.662 + 645.767 | 645.662 + 645.767 + quantitative gate | 645.784 |
| EN.645.756 Metrics, Modeling, and Simulation | 645.662 + 645.667 + 645.767 | Source prerequisites + quantitative gate + 645.757 | 645.784 |
| EN.645.632 Applied Analytics for MBSE | 645.631 | 645.631 | 645.757 + 645.767 + 645.784 |
| EN.645.758 Advanced Systems M&S | 645.662 | 645.662 + quantitative gate + 645.757 | 645.756 |
| EN.645.780 Agile Systems Engineering | 645.662 | 645.662 + 645.764 | 645.631 + 645.768 |
| EN.645.782 Digital and Mission Engineering | 645.662 | 645.662 | 645.631 + 645.757 + 645.769 |
| EN.645.783 SE Process Improvement | None stated in the curriculum | 645.662 + 645.667 | 645.768 + 645.769 |
| EN.645.771 System of Systems Engineering | 645.769 or approval | Full lifecycle core through 645.769 | 645.781 + 645.782 |
| EN.645.753 Enterprise Systems Engineering | 645.769 or approval | Full lifecycle core through 645.769 | 645.771 + 645.781 |
| EN.645.742 Management of Complex Systems | 645.769 or approval | Full lifecycle core through 645.769 | 645.771 + 645.753 + 645.781 |

### Recommended linear path

For a learner taking one course at a time, use this order:

1. EN.645.662 Introduction to Systems Engineering
2. EN.645.667 Management of Systems Projects
3. EN.645.631 Introduction to MBSE
4. EN.605.704 Object-Oriented Analysis and Design
5. EN.645.764 Software Systems Engineering
6. EN.645.767 System Conceptual Design
7. EN.645.768 System Design & Integration
8. EN.645.769 System Test & Evaluation
9. EN.645.757 Foundations of Modeling and Simulation
10. EN.645.784 Decision Science & Analytics
11. EN.645.781 Systems Thinking and Systems Dynamics
12. EN.645.756 Metrics, Modeling, and Simulation
13. EN.645.632 Applied Analytics for MBSE
14. EN.645.758 Advanced Systems Modeling and Simulation
15. EN.645.780 Agile Systems Engineering
16. EN.645.782 Foundations of Digital and Mission Engineering
17. EN.645.783 Systems Engineering Process Improvement
18. EN.645.771 System of Systems Engineering
19. EN.645.753 Enterprise Systems Engineering
20. EN.645.742 Management of Complex Systems

#### Safe parallelization

After completing Phase 0, the following pairs can be studied concurrently only after the learner has completed at least two courses successfully, can sustain approximately 20–24 hours per week, and can preserve separate baselines and review cycles:

* EN.645.631 with EN.605.704
* EN.645.757 with EN.645.784
* EN.645.781 with EN.645.756, after their shared preparation is complete
* EN.645.780 with EN.645.782

Do not parallelize the 645.767 → 645.768 → 645.769 lifecycle chain on the first pass.

### Phase 0 completion standard

Proceed when you can:

* describe the system lifecycle and major technical processes;
* distinguish stakeholder needs, requirements, architecture, verification, and validation;
* create a basic project plan, risk register, and configuration baseline;
* pass the OOP gate before OOAD;
* pass the quantitative gate before the modeling-and-simulation sequence;
* use the program sequence and course matrix to explain why your next course is appropriate.

---

## Course files

- [EN.645.662 — Introduction to Systems Engineering](EN645662.md)
- [EN.645.667 — Management of Systems Projects](EN645667.md)
- [Optional OOP readiness bridge](oop-readiness-bridge.md)
- [Optional quantitative and computational bridge](quantitative-and-computational-bridge.md)

[Back to program README](OVERVIEW.md)

## References

[JHU-767]: https://ep.jhu.edu/courses/645767-system-conceptual-design/ "JHU EP — System Conceptual Design"
[JHU-SE-PLAN]: https://ep.jhu.edu/wp-content/uploads/2025/04/scheduleplan-se.pdf "JHU EP — Expected Course Offerings, Systems Engineering, February 2026"
