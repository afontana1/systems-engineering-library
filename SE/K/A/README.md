# Architecture and Assurance — textbook-depth sequence

This **single canonical set of source chapters** complements the existing 20 book companions. It covers five connected concepts from mission to configured evidence. HTML pages are rendered reading views of these Markdown sources, not separately maintained books.

## Sequence

1. [Mission and measurable claims](chapters/01-mission.md) — [laboratory](labs/01-mission.md)
2. [Typed models and SysML reasoning](chapters/02-models.md) — [laboratory](labs/02-models.md)
3. [Behavioral contracts and temporal safety](chapters/03-behavior.md) — [laboratory](labs/03-behavior.md)
4. [Interfaces and quantitative budgets](chapters/04-budgets.md) — [laboratory](labs/04-budgets.md)
5. [Assurance cases and evidence provenance](chapters/05-assurance.md) — [laboratory](labs/05-assurance.md)

## Scope

The model is a deliberately small typed graph and is not an implementation of OMG SysML v2. All Northstar data are synthetic. Educational verification checks do not establish real-world safety.

Use the Python standard library: `python -m unittest discover -s code -p "test_*.py"`; run the notebooks from the `notebooks` directory. The primary web reader is `INDEX.html`.

## Step 04 — integrated architecture and assurance extension

All five source chapters now include the controlled **NS-AA4.1** case: eligibility denominators and timestamp guard bands; typed paths versus applicable evidence; finite-state dispatch counterexamples; latency and shared-cause reliability budgets; and a rebuttable assurance decision. Existing chapters, labs, diagrams, notebooks, and the original `model_checks.py` remain in place.

- [Controlled case register](data/advanced-case.json) and [individual request records](data/advanced-requests.csv)
- [Executable analysis](code/advanced_case.py) and [negative-case tests](code/test_advanced_case.py)
- Editable extension components are in [`extensions/`](extensions/); canonical Markdown and HTML are synchronized by `python3 scripts/sync_step04_architecture.py` from the repository root.
- Run `python3 scripts/check_step04_architecture.py` and `python3 -m unittest discover -s SE/K/A/code -p 'test_*.py'` before publishing.

The new sample is fictional and deliberately produces a HOLD finding. Graph closure is not semantic sufficiency, numerical screening is not operational validation, and no permission or safety authority is inferred.
