# From process event logs to defensible baselines

**Concept essay · EN.645.783 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

Most process-improvement plans begin with a map of how people **say** work moves. Event logs let us check how cases actually moved. A case needs a stable identifier and events need consistently defined states, timestamps and the responsible function. Without those, the reconstructed workflow can be misleading.

### Derive three quantities

For case `i`, define `T_i = t_release,i − t_valid_intake,i`. Compute median and upper percentiles rather than only a mean. Count review returns to estimate rework frequency and record whether the case was censored (still open when the observation period ended). Segment cases by risk and complexity to avoid unfair comparisons.

Suppose observed end-to-end times are 8, 9, 12, 13, 15, 18, 21, 22, 34 and 66 days. Median is 16.5 days, whereas the maximum is 66; an improving median could coexist with a damaging long tail. A 90th percentile depends on the interpolation convention and should be labeled accordingly.

### Event-log checks

* Every event belongs to an existing case ID.
* Events are in time order after timezone normalization.
* States match the allowed transition rules or are flagged as exceptions.
* Duplicate or missing events are surfaced, not silently imputed.
* Reopened cases have explicit lifecycle boundaries.

### Root cause is different from observation

Repeated returns from board review may arise from poor supplier input, vague requirements, a changing hazard model or overburdened reviewers. An event log describes where returns occur; interviews, artifact inspection and intervention tests are needed to distinguish mechanisms.

**Exercise.** From a CSV with intake, board, correction and release timestamps, calculate the time spent waiting for the board separately from active correction. Identify at least one unobservable interval.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645783) · [Further reading](../RESOURCE-SHELF.md)
