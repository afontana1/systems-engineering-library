# Laboratory: Model credibility review board

*Quantitative textbook laboratory · bounded claims and provenance · fictional Northstar case*

## Mission context

You are supporting an engineering review of a regional mobility dispatch system. Management has received a favorable numerical result but cannot yet explain the assumptions under which it holds. Your job is to turn that result into a reproducible, limited engineering claim.

## Preparation

Read [the associated textbook chapter](../chapters/08-credibility.md), identify the derivation used in the worked example, and list the specific validity assumptions before running any model.

## Task

Prepare a validation matrix with at least four scenario rows and three response columns. Identify held-out data and model deficiencies. Recompute uncertainty propagation for y=2a+b, then write a bounded verdict suitable for technical review.

Begin with the reproducible reference calculation:

```python
from engineering_math import *
print(linear_uncertainty(.1,.3))
```

The program is [available for download](../code/engineering_math.py). Use the [associated notebook](../notebooks/08-credibility.ipynb) and, where relevant, the [factorial data](../data/factorial-waits.csv), [queue data](../data/queue-arrivals.csv), or [decision data](../data/decision-payoffs.csv).

## Deliverables

1. A one-page model contract: what the model represents, its units, initial/operating conditions, and explicit exclusions.
2. A reproducible output table with at least one alternative case and a description of input changes.
3. An uncertainty and failure-mode paragraph identifying conditions under which the finding would reverse or fail.
4. A technical decision memo of 300–500 words: what is supported, what is not supported, and what test should be performed next.

## Assessment criteria

The approximate SD is sqrt(.13)≈.361 under independence; a correct number does not validate the model in untested contexts.

Use the textbook chapter's worked solution only after making your own calculation. If a result changes after a modeling assumption is modified, preserve both outputs and explain the cause rather than replacing the old result silently.

## Further challenge

Ask whether an apparently better statistic can arise from worse service. Propose a second metric and a deliberately adversarial condition to falsify the original conclusion.

[Return to the textbook sequence](../INDEX.html)
