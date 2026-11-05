# Extended laboratory · Model quality and evidence audit

**Course:** Book 3, Week 4 · **Time:** 90–120 minutes · **Companion reading:** [Typed model graph queries](graph.md)

## Your role

An MBSE model passes a naive “links exist” check, but the verification lead disputes the acceptance report. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`model.json`](model.json) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Run the typed graph validator on the provided model; draw a three-node-type relationship legend.
2. Classify each finding as a structural gap, revision problem, configuration mismatch or actual failed result.
3. Repair R3 structurally by adding an authorized satisfaction edge, then rerun; explain why this does not demonstrate verification.
4. Create a new model query that lists tests with no current execution, and write the exact acceptance semantics for that query.

## Extension challenge

Introduce a mistaken `verifies` edge from block B2. Explain which type-check should reject it and why counts alone may not notice the defect.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 4 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

Only R1 is initially supported. R2 has stale evidence; R3 lacks a satisfying block; R4 has the wrong configuration. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
