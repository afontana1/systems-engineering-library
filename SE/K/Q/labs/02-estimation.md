# Laboratory: Evidence design for a waiting-time claim

*Quantitative textbook laboratory · sampling and failures · fictional Northstar case*

## Mission context

You are supporting an engineering review of a regional mobility dispatch system. Management has received a favorable numerical result but cannot yet explain the assumptions under which it holds. Your job is to turn that result into a reproducible, limited engineering claim.

## Preparation

Read [the associated textbook chapter](../chapters/02-estimation.md), identify the derivation used in the worked example, and list the specific validity assumptions before running any model.

## Task

Construct a measurement dictionary with start/end timestamps and missing-request policy. Calculate the 95% upper failure bound for n=30, 100 and 299. Then explain why the same easy test repeated 299 times could still fail to support an operational claim.

Begin with the reproducible reference calculation:

```python
from engineering_math import *
print(zero_failure_upper(30))
```

The program is [available for download](../code/engineering_math.py). Use the [associated notebook](../notebooks/02-estimation.ipynb) and, where relevant, the [factorial data](../data/factorial-waits.csv), [queue data](../data/queue-arrivals.csv), or [decision data](../data/decision-payoffs.csv).

## Deliverables

1. A one-page model contract: what the model represents, its units, initial/operating conditions, and explicit exclusions.
2. A reproducible output table with at least one alternative case and a description of input changes.
3. An uncertainty and failure-mode paragraph identifying conditions under which the finding would reverse or fail.
4. A technical decision memo of 300–500 words: what is supported, what is not supported, and what test should be performed next.

## Assessment criteria

The zero-failure upper bound is about 0.0950 for 30 trials; the report must name independence and representativeness assumptions.

Use the textbook chapter's worked solution only after making your own calculation. If a result changes after a modeling assumption is modified, preserve both outputs and explain the cause rather than replacing the old result silently.

## Further challenge

Ask whether an apparently better statistic can arise from worse service. Propose a second metric and a deliberately adversarial condition to falsify the original conclusion.

[Return to the textbook sequence](../INDEX.html)
