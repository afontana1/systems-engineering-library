# Laboratory — Typed model and revision-impact audit

*Architecture and Assurance · Applied investigation · Fictional Northstar system*

[Read associated textbook chapter](../chapters/02-models.html) · [Download executable model](../code/model_checks.py) · [Open sequence index](../INDEX.html)

## Case briefing

Your engineering model contains requirements, components, tests and produced evidence. During a proposed update, a developer changes a route permission timeout. Management assumes that any requirement with a test link is verified, but the model contains both missing evidence and a deliberately ambiguous relationship.

## Experiment and analysis tasks

1. Load `data/model.json`. Run `validate_model`. Preserve the baseline report.
2. Introduce three model errors independently: connect a Requirement to a Need using `produces`, delete one high-criticality verification link, and point to an unknown node. Confirm that the checks detect the corresponding errors.
3. Restore the baseline and add a requirement concerning route freshness. Attach it to a responsible component and a *planned* verification procedure. State clearly why the model is not evidence of a successful test.
4. Write a change-impact memo for doubling the route timeout. Include physical, behavioral, operational and assurance dependencies.
5. Compare this simplified typed graph with actual SysML v2 concepts. Identify at least three semantics or services absent from the teaching model.

## Submission package

Submit a reproducibility log (exact parameter values and code version), a model or data table, a primary engineering finding, a plausible counterexample, a one-page assumption and uncertainty register, and a **300–500 word** decision memo. Preserve adverse results. If you vary a parameter, show both the baseline and modified results rather than silently replacing an earlier outcome.

## Hints and instructor check

<details><summary>Reference observations — open only after attempting the lab</summary>

The reference validator must flag a type violation, a missing test and a broken edge in the three separate mutations. It need not flag a semantically irrelevant but well-typed test; this is a critical limitation to explain. Do not label the JSON file “SysML v2” or claim standards conformance.

</details>

## Assessment rubric (100 points)

| Criterion | Points | What constitutes persuasive performance |
|---|---:|---|
| Conceptual and modeling correctness | 25 | Types, definitions, units and assumptions are justified |
| Reproducible evidence | 25 | Another reader can regenerate each numerical or state result |
| Adverse case and sensitivity | 20 | At least one meaningful counterexample is analyzed |
| Engineering decision quality | 20 | Scope, limitations, residual risks and next test are explicit |
| Traceability and communication | 10 | Version, data, and claims are clearly linked |

A numerically correct result with a missing denominator, incompatible revision, or hidden failed case does not earn full evidence credit. This exercise is a synthetic teaching investigation, not a deployment approval.

## Files for this laboratory

[Download lab instructions (Markdown)](02-models.md) · [Download Jupyter notebook](../notebooks/02-models.ipynb) · [Download executable Python model](../code/model_checks.py) · [Open code and lab browser](../../LAB-LIBRARY.html).
