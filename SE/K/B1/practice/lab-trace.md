# Extended laboratory · Evidence review board

**Course:** Book 1, Week 4 · **Time:** 100–140 minutes · **Companion reading:** [Evidence applicability and requirements](trace.md)

## Your role

You are the independent verification lead. Engineering wants to release configuration A despite a misleading green dashboard. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`trace.csv`](trace.csv) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Run the ledger tool without changing its acceptance rules. Separate admissible results, affirmative passes and valid failures.
2. Investigate each of the four statuses other than VERIFIED_PASS. For each, specify the next engineering action and authority.
3. Create a revision-4 test plan for R-03 and a discrepancy record for R-04; distinguish missing evidence from demonstrated nonconformance.
4. Prepare a one-page decision note with a table of six requirements and a conditional gate recommendation.

## Extension challenge

Change only the test revision of R-03 to match the current requirement. Re-run and explain why changing the CSV is not itself acceptable proof in a controlled project.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 4 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

Initial result: three admissible records, two supported claims and one valid failure. R-03 is stale; R-05 is on the wrong configuration; R-06 lacks execution. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
