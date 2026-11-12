# L04 · Evaluate competing designs without hiding constraints

**Learning time:** 4–6 hours. **Gate:** Architecture trade review. **Prior reading:** [F02](../../flagships/F02-decisions-and-architecture.md) and [F06](../../flagships/F06-optimization-and-control.md).

## First eliminate infeasible designs

A popular but misleading method is to rank alternatives using a weighted total before checking hard constraints. Northstar has three synthetic fleet options in [trade-study.csv](../data/trade-study.csv): one, two or three vehicles, with invented cost units 100, 185 and 260. The problem is not “Which score is highest?” but “Which alternatives can satisfy the demonstration's constraints **and** remain credible under uncertainty?” With one vehicle, the fixed fixture completes only 6/12 requests; that is infeasible for the declared 95% fixture threshold. Two vehicles complete 12/12. Three vehicles may lower waits but incur an additional invented cost of 75 units. These figures are merely a learning input, not quotes or engineering costs.

The scheduler's structural constraint is `start_i ≥ arrival_i`, `start_i ≥ vehicle_available`, and `finish_i = start_i + 12`. An assignment is accepted only if `finish_i ≤ 80`. With two vehicles, the fixed fixture produces start times 0, 4, 12, 16, 24, 28, 36, 40, 48, 52, 60, 64. Subtract the arrival times 0, 4, …, 44 to get waits `0,0,4,4,8,8,12,12,16,16,20,20`; nearest-rank p90 is the 11th ordered value, 20 minutes. The completion fraction is 1.0. Neither metric measures physical feasibility of the routes, since distance and travel-time variations are excluded.

## A useful sensitivity question

If a decision-maker lowers the fixture p90 threshold from 20 to 15 minutes, the two-vehicle alternative fails **without any code change**. That is not a software bug; it is a decision-rule revision. If a vehicle becomes unavailable, two-vehicle design becomes one-vehicle performance, so architecture alternatives must also be evaluated under degradation. A robust choice may prioritize graceful fallback, but no honest claim about real fallback is available without a model of actual vehicle reliability and recovery resources.

A weighted score can be used among feasible options, but every weight must be declared, justified, and varied. For utility `U = w_s S + w_c C`, a preference reversal is possible if changing weights moves one alternative above another; therefore show thresholds rather than presenting the weighted total as objective truth.

## Engineering activity

1. Run the reference configuration and variants with one or three vehicles; record `served_fraction`, `p90_wait_min`, and your chosen cost figure in the editable trade sheet.
2. Calculate a feasible set for four combinations of `vehicles` and `trip_min` at fixed horizon. Do not assign nonexistent monetary precision to your findings.
3. Show which alternative is nondominated on cost and p90 wait; explain why passing the fixture does not imply global Pareto optimality.
4. Write a one-page decision memo with evidence, sensitivity, uncertainty, and explicit reconsideration triggers. Update [decision-register.csv](../data/decision-register.csv).

## Knowledge check and explained answer

**Question.** If one vehicle has the lowest cost but fails a must-meet completion threshold, can it still win through weighted scoring?

<details><summary>Show explanation</summary>

Not when the completion threshold is truly a hard feasibility constraint. Score aggregation cannot override a declared hard constraint. A different solution would require changing the requirement with authority and documentation, not quietly raising its cost weight.

</details>

**Gate evidence:** completed trade sheet, sensitivity plot or table, feasibility logic, and an independently reviewable recommendation.

## U2 cross-lab credibility challenge — NS-U2.1

**Focus: Trade studies with noninterchangeable scenarios.** This adds a controlled cross-version analysis to the original learning stage, which remains unchanged.

The v11 degradation uses **one modeled vehicle for the entire horizon**; v12 `OUTAGE` uses two configured vehicles but blocks vehicle V01 through minute 70. They happen to complete **six of twelve** requests in the current fixture, yet their causal mechanisms differ. Matching output counts does not validate equivalence of configurations or physical policies.

**Analysis:** The nominal completion fraction is `12/12 = 1.00`. Both tested degraded scenarios yield `6/12 = 0.50`; the absolute change is `−0.50`, a **50 percentage-point reduction**, not a 50% confidence interval. Their timing curves, fault windows, and resources must be compared independently before using one as a surrogate for the other.

**Exercise and solution:** A manager claims a spare vehicle restores outage robustness because “two vehicles” appears in the v12 configuration. Reject the argument: one vehicle is unavailable for nearly the entire 80-minute horizon. Recompute *effective capacity*, not configured fleet count, and add an explicit operator escalation and permission gate before any proposed dispatch policy.

**Reproduce:** [Cross-lab lab guide](../../lab-credibility-u2/README.md) · [Evidence gates](../../lab-credibility-u2/data/gates.json) · [Computed results](../../lab-credibility-u2/outputs/u2-cross-lab-results.json).
