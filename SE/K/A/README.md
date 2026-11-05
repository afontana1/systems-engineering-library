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
