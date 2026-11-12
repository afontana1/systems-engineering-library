# Systems Engineering: Book Companion, Volume I — complete introductory course (v14)

**Course:** EN.645.662 — Introduction to Systems Engineering · **Scope:** 12 reading chapters and 12 fictional practice laboratories, one pair per original weekly learning unit.

This is the actual teaching companion to the course guide, not an accreditation claim or an operational authorization. The guide supplies independent assignments and mastery rubrics; this book explains their prerequisites and the labs provide fictional rehearsals. All twelve original chapters have been retained and now include a coordinated technical studio using one controlled synthetic engineering baseline.

## How to study

1. Start with the [original course guide](../../C/P0/EN645662.md); each week now points directly to its book chapter and practice lab.
2. Read the book chapter with a notebook; redo the calculations and critically evaluate the assumptions.
3. Complete its hypothetical lab and review the explanation only after attempting the tasks.
4. Use the older [short weekly primer](../P0-text/lessons/645-662-w01.md) or [unified encyclopedia](../U/OPEN-ENCYCLOPEDIA.html) for alternate perspectives.
5. Complete the **course guide assignment**, which is more extensive and authoritative than its lab rehearsal.

## One controlled example across the full book

The [Northstar NS-B1 integrated case](case/INDEX.html) carries requirements, interfaces, architecture decisions, hazards and verification evidence through all twelve chapters. Its [editable baseline](case/northstar-reference-baseline.json), [traceability matrix](case/traceability.csv) and [standard-library reproducibility script](tools/step03_case_check.py) permit independent checking. One test record is deliberately stale to make evidence-validity review meaningful. All figures are fictional; the case does not authorize an actual shuttle system.

## Chapter and lab index

| Week | Book chapter | Fictional lab |
|---:|---|---|
| 1 | [Chapter 1 — What, exactly, is the system?](chapters/01-what-is-the-system.md) | [Hypothetical Lab 1 — The Boundary Hearing](labs/lab-01-boundary-hearing.md) |
| 2 | [Chapter 2 — A life cycle is a strategy for acquiring evidence](chapters/02-lifecycle-evidence.md) | [Hypothetical Lab 2 — The Design-Gate Debate](labs/lab-02-design-gate.md) |
| 3 | [Chapter 3 — Turn conflicting human needs into an operational concept](chapters/03-needs-and-conops.md) | [Hypothetical Lab 3 — The Stakeholder Hearing](labs/lab-03-stakeholder-hearing.md) |
| 4 | [Chapter 4 — Requirements are promises that must survive a test](chapters/04-requirements.md) | [Hypothetical Lab 4 — The Requirements Clinic](labs/lab-04-requirements-clinic.md) |
| 5 | [Chapter 5 — Before the Boxes: Functional Architecture and System Behavior](chapters/05-functions-and-behavior.md) | [Hypothetical Lab 5 — The Missing State](labs/lab-05-functional-architecture.md) |
| 6 | [Chapter 6 — A Review Is a Decision, Not a Presentation](chapters/06-reviewing-the-functional-baseline.md) | [Hypothetical Lab 6 — The Functional Review Board](labs/lab-06-functional-review-board.md) |
| 7 | [Chapter 7 — Architecture Is the Allocation of Responsibility](chapters/07-allocating-architecture-and-interfaces.md) | [Hypothetical Lab 7 — The Interface Contract Hearing](labs/lab-07-interface-contracts.md) |
| 8 | [Chapter 8 — A Trade Study Makes Judgment Inspectable](chapters/08-trade-studies-and-sensitivity.md) | [Hypothetical Lab 8 — The Architecture Decision Hearing](labs/lab-08-decision-hearing.md) |
| 9 | [Chapter 9 — Technical Management Keeps Engineering Claims Coherent](chapters/09-managing-the-technical-baseline.md) | [Hypothetical Lab 9 — The Baseline Audit](labs/lab-09-technical-management.md) |
| 10 | [Chapter 10 — Failures Travel Through Interfaces and Organizations](chapters/10-failures-and-controls.md) | [Hypothetical Lab 10 — The Fault That Passed Every Green Check](labs/lab-10-red-team.md) |
| 11 | [Chapter 11 — From a Plausible Concept to Reviewable Evidence](chapters/11-realization-and-evidence.md) | [Hypothetical Lab 11 — The Evidence That Isn't There](labs/lab-11-verification-board.md) |
| 12 | [Chapter 12 — Engineering Synthesis: Defend the System, Not the Slide Deck](chapters/12-synthesis-and-defense.md) | [Hypothetical Lab 12 — Defend a Concept with Imperfect Evidence](labs/lab-12-final-defense.md) |

## Source files and extras

All chapters and labs are editable Markdown in `chapters/` and `labs/`. Fictional exercise CSVs are in `data/`, executable Python calculations and unit tests in `tools/`, and editable DOT plus rendered SVG diagrams in `figures/`. Run the tests with `cd tools && python -m unittest test_book_companion.py test_v14.py -v`.

Original unmodified guides from the prior collection are in `orig/`. The current weekly course guides contain only added reading callouts; they do not replace the original course requirements.

**Other 19 courses:** retain their first-pass weekly teaching lessons and course-linked primers; they have not yet received twelve book-depth chapters each. This volume completes the first course only.

**Evidence caveat:** All shuttle values, alternatives, faults and test runs are synthetic teaching assumptions. This volume is not a technical assurance or regulatory approval of any real mobility system.


## Deeper concept readings

- [Safety engineering: from hazards to enforceable constraints](../T/13-safety-constraints.md)
- [Human factors: design for decisions made under pressure](../T/14-human-factors.md)
