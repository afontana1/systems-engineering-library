# Laboratory — Counterevidence and configuration-specific readiness review

*Architecture and Assurance · Applied investigation · Fictional Northstar system*

[Read associated textbook chapter](../chapters/05-assurance.html) · [Download executable model](../code/model_checks.py) · [Open sequence index](../INDEX.html)

## Case briefing

The project produced favorable baseline evidence at revision v1. Before release, route freshness and dispatch fallback rules changed at revision v2. The review board has also received an adverse accessibility test and one missing evidence record. Management requests a declaration of full readiness.

## Experiment and analysis tasks

1. Read `data/evidence.csv` and use `check_evidence` to flag missing evidence, failures and revision mismatches for a proposed v2 baseline.
2. Build an assurance table linking each system claim to a verification procedure, configured evidence, operational scenario, assumptions and a credible defeater.
3. Recalculate the one-sided 95% upper failure-probability bounds for zero failures at n=30 and n=299; explain exactly what trials would need to be sampled for the latter to mean anything.
4. Identify two v1 evidence artifacts that could be retained under an explicit equivalence argument and two that must be rerun. Document your reasoning.
5. Write two separate memos: a best defensible bounded operational release claim and a critical countercase. Make a conditional go/no-go decision and list decision-changing tests.

## Submission package

Submit a reproducibility log (exact parameter values and code version), a model or data table, a primary engineering finding, a plausible counterexample, a one-page assumption and uncertainty register, and a **300–500 word** decision memo. Preserve adverse results. If you vary a parameter, show both the baseline and modified results rather than silently replacing an earlier outcome.

## Hints and instructor check

<details><summary>Reference observations — open only after attempting the lab</summary>

The checker flags stale v1 evidence, nonpassing v2 evidence and missing evidence identifiers. At n=30 the one-sided upper bound is about 9.50%, while at n=299 it is just under 1% under identical independent trial assumptions. The expected board verdict is not automatically “go”; the author must defend a condition-specific scope and preserve negative evidence.

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

[Download lab instructions (Markdown)](05-assurance.md) · [Download Jupyter notebook](../notebooks/05-assurance.ipynb) · [Download executable Python model](../code/model_checks.py) · [Open code and lab browser](../../LAB-LIBRARY.html).
