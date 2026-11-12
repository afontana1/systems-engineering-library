# Northstar integrated engineering laboratory — v11.0

**Format:** ten linked Markdown learning stages, executable Python 3.10+ prototype, test suite, four notebooks, editable CSV design artifacts, evidence outputs, an independent review board packet, and an offline website.

**Mission:** develop and defend a **fictional**, software-only regional-mobility request scheduler as a complete systems engineering evidence chain. No real vehicle commands, no production interfaces, no safety or service certification. The inputs, targets, costs, and demand distributions are synthetic teaching assumptions.

## Start here

- **Offline study website:** [OPEN-LAB.html](OPEN-LAB.html) (read without a network connection).
- **Sequence:** [L01](chapters/01-mission-boundary.md) → [L02](chapters/02-requirements-traceability.md) → [L03](chapters/03-architecture-interfaces.md) → [L04](chapters/04-trades-and-configuration.md) → [L05](chapters/05-software-prototype.md) → [L06](chapters/06-models-and-uncertainty.md) → [L07](chapters/07-verification-evidence.md) → [L08](chapters/08-human-factors-safety.md) → [L09](chapters/09-change-and-digital-thread.md) → [L10](chapters/10-readiness-board.md).
- **Final review:** [review board brief](review/REVIEW-BOARD.md), [assessment rubric](review/RUBRIC.md), and [instructor / self-review key](review/REFERENCE-RESPONSES.md).
- **Traceability:** [stage to course / flagship crosswalk](CROSSWALK.csv).

## Run the reference project

From this directory in a terminal:

```bash
python -m unittest discover -s tests -v
python -m src.run_lab
```

The runner regenerates `outputs/results.json`, `outputs/dispatch-assignments.csv`, and `outputs/input-hashes.json`. These are synthetic experimental records: **passing fixtures are not proof of deployed system safety, efficacy, equity, or reliability**.

To change the example, edit `data/config.json` or copy the input file to a new version. Keep configuration and evidence together; changes invalidate prior results. Only the Python standard library is needed for the runner and tests. Notebook files are readable as JSON and runnable in any local Jupyter environment.

## Initial evidence snapshot

Under the reference 2-vehicle, 12-minute trip, 80-minute-horizon fixture, 13 event rows resolve to 12 unique requests; 12 are completed, nearest-rank p90 wait is 20 minutes, and no overlap appears. The one-vehicle degradation case serves 6 of the 12. A seeded stochastic arrival stress test, under its **invented** interarrival distribution, often fails the demonstration targets; it is a sensitivity study, not a field-performance prediction. Recompute rather than relying on figures here.

## Completion standard

A learner must submit the ten stage deliverables, executable evidence with versioned input hashes, one change-impact analysis, a model-credibility assessment, an honest limitations and risk register, and a board decision supported by both favorable and unfavorable evidence. A perfect unit-test run alone is insufficient.

The case intentionally stops at **prototype study**. It contains no operational security hardening, no validated human-factors design, no real traffic or fleet data, and no independent expert assurance. All references to field assessment are *proposed future activities*.

## Release U2 cross-laboratory evidence exercise

The [U2 cross-lab credibility lab](../lab-credibility-u2/README.md) replays this source without rewriting its baseline data or tests. The U2 sections now teach fault, provenance and authorization checks.
