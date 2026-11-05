# Extended laboratory · Adversarial readiness board

**Course:** Book 8, Week 10 · **Time:** 100–140 minutes · **Companion reading:** [Test evidence and readiness](readiness.md)

## Your role

The operations team reports a p90 wait pass for a 12-request case and proposes immediate release. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`requests.csv`](requests.csv) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Recalculate p90 wait using the stated nearest-rank method and retain dropped requests in the service denominator.
2. Construct an evidence table separating pass, fail and not-tested conditions.
3. Identify why completed-only latency is a conditional measure that can improve when service degrades.
4. Write an evidence-limited go/no-go recommendation and a dissenting reviewer note.

## Extension challenge

Change one dropped request to served with 30-minute wait. Recompute both metrics and explain why a one-number score is unsuitable for the gate.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 10 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

Nearest-rank p90 among served is 18 minutes; completion 10/12=83.3%, below the 95% threshold. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
