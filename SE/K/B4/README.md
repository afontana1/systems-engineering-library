# Book IV — Object-Oriented Analysis and Design

Course: EN.605.704 · Phase 1 · 12-week book companion

Each chapter teaches concepts for the correspondingly numbered course week, and each fictional laboratory prepares you for an independent course deliverable. These materials supplement rather than replace the assessment rubric.

## Start

Open `OPEN-BOOK.html` for the searchable, self-contained offline reader. Source chapters live in `chapters/`; practice labs in `labs/`. The optional computational notebook is in `notebooks/`.

## NS-OO4.1 integrated case

All twelve chapters use the same [reservation-service study case](case/INDEX.html), with controlled [requirements and model data](case/model-baseline.json), [scenario fixtures](case/scenario-fixtures.csv), [traceability](case/traceability.csv), a [responsibility diagram](diagrams/oo4-reservation-model.svg), and a [standard-library Python/SQLite checker](tools/step03_book4_contract_check.py). The tests demonstrate narrowly scoped design obligations; they do **not** establish language-model conformance, operational safety, or production correctness.

## Book contents

- Week 1: [Chapter](chapters/01-establish-the-ooad-problem-scope-and-modeling.md) → [Hypothetical lab](labs/lab-01-establish-the-ooad-problem-scope-and-modeling.md) — Analysis discovers concepts; design assigns responsibilities
- Week 2: [Chapter](chapters/02-elicit-and-structure-software-requirements.md) → [Hypothetical lab](labs/lab-02-elicit-and-structure-software-requirements.md) — Software requirements need multiple kinds of precision
- Week 3: [Chapter](chapters/03-capture-functional-requirements-with-use-case.md) → [Hypothetical lab](labs/lab-03-capture-functional-requirements-with-use-case.md) — Use cases describe externally valuable behavior
- Week 4: [Chapter](chapters/04-discover-candidate-classes-and-build-the-stat.md) → [Hypothetical lab](labs/lab-04-discover-candidate-classes-and-build-the-stat.md) — Class discovery turns language into relationships
- Week 5: [Chapter](chapters/05-analyze-dynamic-behavior-and-discover-collabo.md) → [Hypothetical lab](labs/lab-05-analyze-dynamic-behavior-and-discover-collabo.md) — Sequence models expose missing responsibility
- Week 6: [Chapter](chapters/06-model-state-dependent-behavior-and-conduct-th.md) → [Hypothetical lab](labs/lab-06-model-state-dependent-behavior-and-conduct-th.md) — State machines are executable constraints on lifecycles
- Week 7: [Chapter](chapters/07-assign-responsibilities-and-build-the-static-.md) → [Hypothetical lab](labs/lab-07-assign-responsibilities-and-build-the-static-.md) — Design is the distribution of responsibility
- Week 8: [Chapter](chapters/08-realize-use-cases-with-dynamic-design-models.md) → [Hypothetical lab](labs/lab-08-realize-use-cases-with-dynamic-design-models.md) — A design sequence should be realizable
- Week 9: [Chapter](chapters/09-apply-design-patterns-with-restraint.md) → [Hypothetical lab](labs/lab-09-apply-design-patterns-with-restraint.md) — Patterns are named tradeoffs
- Week 10: [Chapter](chapters/10-express-precise-constraints-with-ocl-and-exec.md) → [Hypothetical lab](labs/lab-10-express-precise-constraints-with-ocl-and-exec.md) — Constraints turn informal rules into testable predicates
- Week 11: [Chapter](chapters/11-design-persistence-and-conduct-the-design-rea.md) → [Hypothetical lab](labs/lab-11-design-persistence-and-conduct-the-design-rea.md) — Persistence design is about identity and failure recovery
- Week 12: [Chapter](chapters/12-baseline-and-defend-the-integrated-ooad-desig.md) → [Hypothetical lab](labs/lab-12-baseline-and-defend-the-integrated-ooad-desig.md) — A defendable design is a consistent set of claims
