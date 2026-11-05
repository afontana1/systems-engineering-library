# Chapter 10 — Recover the Project Without Rewriting Reality

*EN.645.667 · Week 10 · Technical performance, software delivery and recovery options · Preceded by [Chapter 9](09-leadership-and-communications.md); continue with [Chapter 11](11-proposal-red-team.md).*

> **Study contract.** This chapter teaches the concepts behind Week 10; practice them in [Hypothetical Lab 10](../labs/lab-10-integrated-recovery-control.md), then complete the [original Week 10 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

By Month 5, the shuttle pilot's signals are deteriorating together: a supplier is six weeks late, the software integration stream is behind plan, the false-stop rate is too high, and cost efficiency is poor. Managing each stream independently might worsen the others. Accelerating software testing against an unstable interface creates rework; buying overtime before identifying the integration bottleneck consumes money without producing verifiable progress.

A responsible recovery plan begins with an integrated causal hypothesis rather than a preferred “fast fix.” Separate **symptoms** (late supplier, false stops, weak CPI), **mechanisms** (incomplete interface specification, unavailable test bench, uncertain acceptance criterion), and **interventions** (freeze change, stage tests, add capacity, redesign an interface, or adjust a milestone). The hypothesis must be testable. Correlation in status reports is not proof of a single cause.

Agile or iterative software practices can reduce feedback latency and technical uncertainty, but backlog velocity is not equivalent to acceptance of the complete shuttle system. A working software increment can still fail integration, safety, documentation or contractual conditions. Program controls must connect iterations to the technical baseline and system-level evidence.

## Develop the method

Create a cross-domain exception dashboard: requirement or TPM, planned trajectory, measured value, data freshness, interpretation, owner, next decision. For each recovery option, estimate explicit cost, calendar impact, residual technical risk, and evidence produced. Challenge optimistic options with a **counterfactual**: what would the forecast look like if the supplier issue persists for another month? What if the intervention speeds one team but delays verification?

Make re-planning transparent. Preserve the variance against the approved baseline, show an updated forecast separately, and require change authority for any new commitment. Compare recovery value in terms of accepted capability, not merely activities completed or budget consumed.

## The mechanism beneath the method

Project recovery is a constrained replan that must preserve a truthful account of prior commitments while changing future action.

### Distinguishing related ideas

Rebaselining is not synonymous with improving performance; it can change the reference numbers without removing the underlying capacity or integration bottleneck.

### Interpretation and boundary conditions

Recovery alternatives should distinguish acceleration, descoping, sequencing and technical redesign, each with a different effect on risk and stakeholder value.

## Worked Northstar project example

The interim false-stop target is at most 2 per hour, while measured performance is 7 per hour. One team proposes a large filter change that could suppress false positives but also miss hazards. A second proposes targeted data labeling and controlled test scenarios before changing detection thresholds. The second path may appear slower yet provides interpretable evidence about false positives and missed obstacles. The comparison must specify detection safety, data provenance, test environment, cost and schedule—not just the count of false stops.

## Evaluate recovery proposals as engineering hypotheses

A recovery proposal should have a mechanism: “By validating the interface schema early, we will reduce integration rework by X because test fixtures can be completed before supplier release.” This is more useful than “add more engineers.” The latter could even slow work if new personnel need scarce experts for onboarding, or if the bottleneck is a single test rig.

Construct an option table with initial cost, forecast finish, expected evidence improvement, residual technical risk and reversibility. Distinguish short-term throughput from lifetime acceptance. A plan that suppresses reported false-stop events by discarding difficult data may improve a metric while worsening safety. Better test design includes conditions under which the intervention *fails*, not only scenarios selected to make it look favorable.

**Illustrative tradeoff.** Path A adds $180,000 in overtime and claims a four-week schedule improvement, but still uses an unverified interface. Path B spends $90,000 on targeted contract tests and claims only a two-week improvement, yet produces evidence relevant to a critical assurance gate. Under a schedule-only utility measure, A may appear superior. Under an admissible-completion constraint requiring valid integration evidence, A is infeasible until that evidence is produced. Recognizing feasibility constraints before value scoring prevents a misleading recovery recommendation.

Preserve three separate views: the original authorized baseline, the best current forecast, and the authorized revised plan if a change is approved. A project can make significant recovery progress while still showing a historical variance; hiding that variance destroys the learning signal. Managers should be rewarded for explaining uncertainty and improving decision quality, not for retroactively making charts green.


## Reproduce and challenge the numbers

Run the [Week 10 calculation notebook](../notebooks/04-recovery-decisions.ipynb) against the [editable dataset](../data/month-5-evm.csv) in the Markdown source package. Change at least one assumption, recompute the result, and write down which conclusion changes. This exercise checks arithmetic and reasoning within a fictional model; it does not validate the real-world estimate or program.

## Boundary of the method

“Recovery” is not proof of success if it uses a changed metric, deferred testing, or a new date with no recorded authorization. Ask which claim has become more credible.

## Retrieval questions and explained answers

1. **Question:** Why must a recovery plan include a counterfactual?
   **Explanation:** To compare intervention effects against a plausible alternative and expose causal assumptions.
2. **Question:** Does software velocity prove system acceptance?
   **Explanation:** No; system interfaces, safety, physical hardware and contract tests still constrain acceptance.
3. **Question:** Why preserve baseline variance after replanning?
   **Explanation:** To keep the historical commitment and approved changes auditable.


## Graduate depth: recovery control as constrained feedback intervention
### A late project is a dynamic system, not a frozen schedule

A recovery plan changes behavior within a network of task dependencies, capacity constraints, feedback loops, and human decisions. Adding personnel may initially reduce productivity because experienced staff must train new colleagues; accelerating design work can increase downstream rework; overlapping integration activities can amplify interface conflicts. Therefore, the claim “ten more engineers will shorten delivery by ten weeks” requires a production model, not arithmetic alone. In a simple task-flow representation, backlog evolves as `B(t+1) = B(t) + new work + rework - accepted completions`. The useful output is accepted work, not hours charged or tasks marked complete.

Project control also suffers from delayed observations. Earned value can indicate cost and schedule deviation against a baseline, but its diagnostic power depends on truthful completion criteria and a representative work breakdown. `CPI = EV / AC` and `SPI = EV / PV` are ratios, not causal explanations. A project can show favorable CPI while avoiding its highest-risk integration work; a recovery plan that improves CPI by deferring critical verification may make the ultimate delivery less credible.

### Recoverability depends on network structure

Task compression must respect precedence relationships and shared resources. In a precedence network, reducing the duration of a noncritical activity may not change the end date. As the critical path moves, additional acceleration can yield diminishing returns. Overlap, or fast-tracking, exchanges schedule for rework exposure when downstream tasks begin before upstream information is stable. Crashing exchanges money or capacity for duration, often with a nonlinear cost curve. These options should be evaluated with realistic limits, interface maturity, and alternative critical paths rather than treating all tasks as compressible.

Suppose integration testing is delayed because software and battery-management teams disagree about a telemetry interface. Assigning another test crew does not fix the missing contract. The dominant intervention may instead be an interface freeze, shared executable fixture, explicit arbitration, and a shorter review cycle. This example illustrates the distinction between symptoms (late tests), proximate causes (incompatible data), and structural causes (unowned cross-team decisions). Recovery plans should intervene at the level that produces lasting change.

### A recovery baseline requires explicit decision economics

Compare alternatives by expected completion time, cost exposure, technical confidence, operational risk, and reversibility. A schedule model can generate a distribution of completion dates under uncertain task durations and resource competition; its percentiles are credible only if dependence and scope assumptions are defensible. The probability of meeting a deadline is `P(T_finish <= T_due)`, but that probability should not be presented as precise when estimates come from uncalibrated expert judgments. Sensitivity analysis can still identify which assumptions dominate the decision.

Rebaselining is legitimate when scope, authority, or assumptions change with informed approval. It is not legitimate as a way to erase past underperformance. Retain the original reference, changes and reasons, current forecast, accepted residual risks, and the evidence needed to return to ordinary control. The recovery decision should say which work is delayed or removed, which tests remain mandatory, and what stop condition will trigger renewed review. A credible recovery plan protects the eventual system even when that means admitting that the initial date or budget cannot be met.

## Put this into practice

Work through [Lab 10: The Month Five Recovery Cell](../labs/lab-10-integrated-recovery-control.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 10 primer](../../P0-text/lessons/645-667-w10.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.
