# Applied lab: System-of-systems mission dependencies and distributed assurance

*Advanced practice associated with Book 18 — System of Systems Engineering. Synthetic Northstar exercise.*

## Problem brief

Build a mission dependency graph for transit, emergency response and clinical triage. Find minimal cut sets, add a shared identity-provider outage, and negotiate a written contract that assigns detection, notification and recovery responsibility.

## Required evidence package

1. **Model contract:** define the decision, quantity units, system boundary, valid operating range, configuration and explicit assumptions.
2. **Reproducible calculation:** execute the [worked Python model](../tools/worked_models.py), inspect the [notebook](../notebooks/18-mission-networks.ipynb), then independently reproduce the example without copying its printed output.
3. **Adverse scenario:** change at least one assumption in a way that threatens the initial recommendation. Record the altered input, affected output and causal explanation.
4. **Engineering artifact:** construct a decision table, dependency graph, assurance argument, experiment plan or causal analysis suited to this study. Link every main claim to specific evidence.
5. **Review memo:** give a recommendation, bounded scope, remaining uncertainty, rejected alternatives and the observation that would trigger reconsideration.

## Starter inputs

Download [the example scenario CSV](../data/18-mission-networks.csv) and identify which values are facts, assumptions or invented teaching parameters. No external operational data is used.

## Assessment criteria

| Criterion | Weight | What constitutes strong evidence |
|---|---:|---|
| Conceptual and model validity | 30% | Explicit boundary, units, dependencies and assumptions; no category errors |
| Reproducibility | 20% | Another reviewer can rerun the calculation and obtain the stated values |
| Counterexample and sensitivity | 25% | A meaningful adverse scenario changes or challenges the original argument |
| Decision and communication | 25% | A justified recommendation with limits, accountable owner and revision trigger |

## Reflection questions

- Which assumption is most capable of reversing the preferred decision? Why?
- What observable result would falsify your model's central causal or structural claim?
- Who could be harmed by an apparently successful optimization, and how would they discover it?

Return to [the graduate chapter](../chapters/18-mission-networks.html) after evaluating the lab. The reference answers in the chapter are *examples*, not permission to omit independent analysis.
