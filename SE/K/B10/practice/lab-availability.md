# Extended laboratory · Redundancy and shared-dependency investigation

**Course:** Book 10, Week 8 · **Time:** 100–135 minutes · **Companion reading:** [Common-cause availability](availability.md)

## Your role

Two redundant servers appear to deliver five nines under independence, but a shared network dependency threatens both. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`reliability.csv`](reliability.csv) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Compute single-unit and independence-based pair availability using the provided repair/uptime data.
2. Include 0.8% common-cause unavailability and compare against a 99.5% required gate.
3. Construct a dependency map covering facilities, power, network, identity, software release and operator controls.
4. Recommend two verifiable mitigations with measurable failure-injection criteria.

## Extension challenge

Choose a common-cause target such that modeled availability just reaches 0.995. Show the algebra and explain why lowering q in a spreadsheet is not mitigation evidence.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 8 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

Single-unit availability about 0.97561; independent pair 0.999405; with q=.008 adjusted pair about 0.991410. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
