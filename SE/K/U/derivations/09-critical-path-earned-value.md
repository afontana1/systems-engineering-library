# D09 · Critical paths and earned-value measures are not the same thing

**Skill:** Derive schedule dependencies and cost/schedule performance without confusing expenditure with accomplishment.

## Forward-pass schedule

Consider activities (duration in days): A=3, B=5; C=4 after A; D=2 after B; E=3 after both C and D. A starts at day 0 and finishes day 3; C finishes day 7. B finishes at day 5 and D at day 7. E starts at day 7 and completes at day 10. There are **two critical paths**: A–C–E (3+4+3=10), and B–D–E (5+2+3=10). Delaying either chain delays the project unless another schedule change compensates.

Do not confuse a critical path with the only important work: a noncritical activity can still have safety or interface importance. Resource constraints, uncertainty and calendar availability may change the real schedule.

## Earned value at a status date

Let planned value `PV=80`, earned value `EV=60`, and actual cost `AC=75` (all in budget units). Schedule performance index `SPI=EV/PV=0.75`; cost performance index `CPI=EV/AC=0.8`. Schedule variance `SV=EV−PV=−20`; cost variance `CV=EV−AC=−15`.

EV is the budgeted value of completed work. It is not the amount spent, not the time elapsed and not necessarily the delivered stakeholder value. Earned-value percentages depend critically on verifiable work-package completion criteria and controlled baselines.

If the approved budget at completion is `BAC=200`, a simple estimate-at-completion assuming unchanged cost efficiency is `EAC≈BAC/CPI=250`. This estimate is conditional on future work behaving like past work and ignores separately analyzed risks and scope changes.

## Why both views matter

Network analysis explains *which dependencies* determine schedule risk; earned value summarizes *how much planned scope has been accomplished for the resources spent*. Neither by itself reveals whether a design is technically valid. A team can “earn” value on documentation and still fail integration.

## Practice

**Question:** With two critical paths ending together, which single activity may be delayed without extending the project?

<details><summary>Solution</summary>

None of A, B, C, D or E has positive total float in this example. Both chains are length 10. If a new independent noncritical activity were added, its float could be calculated against the project finish.

</details>

**Transfer artifact:** Dependency graph, forward/backward passes, baseline, objective completion rules and separate technical maturity indicators. See [WBS and baselines](../../encyclopedia/wbs-and-baselines.md).
