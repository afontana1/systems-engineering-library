# Phase 4 editable templates and lab toolkit

The `templates/` directory contains **15 editable CSV worksheets**, with headers that match the case artifacts used across the three courses. A few files contain deliberately synthetic example rows; remove or change these when creating your own controlled baseline. The `datasets/` directory provides a small *illustrative*, nonrepresentative process data sample.

The `tools/phase4_lab.py` script uses only the Python standard library and supports:

1. Stable-flow lead-time estimate from WIP and throughput.
2. Idealized M/M/1 queue time under explicit assumptions.
3. End-to-end critical-path duration for a directed acyclic task graph.
4. Version-consistent traceability checks.
5. Digital-twin state freshness and allowable-use decision.
6. Independent-series mission success for an illustrative scenario.
7. Average and nearest-rank percentile analysis for process case times.
8. Difference-in-differences arithmetic for group *means* (not a causal proof).

Run `python tools/phase4_lab.py` for demonstrations and `python -m unittest discover -s tools -p 'test_*.py'` for automated unit checks. No data science dependencies or internet connection are needed.

**Important:** Exercises are calculations, not certified digital twins, accredited simulations, clinical/safety decisions or evidence of field reliability. Review assumptions in each function docstring.
