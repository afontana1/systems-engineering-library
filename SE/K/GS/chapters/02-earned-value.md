# Project performance as an integrated technical claim

*Graduate study for Book 2 — Management of Systems Projects. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> When a project reports that it is 60% complete, exactly what evidence has been used to earn that completion?

## Theory and conceptual structure

A schedule, cost baseline and engineering product baseline are different representations of one intended accomplishment. Earned value management (EVM) is useful only if the work package has an objectively measurable definition of done. A design package does not earn its full budget because its drawings exist; they must satisfy specified maturity and review criteria. If a team changes the definition of done after reporting progress, a mathematically consistent index may still describe an invalid measurement system.

A credible performance measurement baseline assigns responsibility for each control account, specifies scope, calendar position and time-phased budget, and retains configuration history. **Planned value (PV)** is budget authorized for work scheduled by the status date. **Earned value (EV)** is the budgeted value of objectively completed work. **Actual cost (AC)** is expenditure attributable to that work. These values are measured in budget currency, not in hours or counts of tasks. A project may have high EV for documentation while lacking test evidence for mission-critical requirements.

The work breakdown structure should be product-oriented enough to trace work to accountable technical outcomes. Schedule dependencies also need physical meaning. A predecessor link can represent a configuration handoff, delivered component, accepted test, or mere managerial preference. A baseline review must test each dependency and the availability of people, facilities and long-lead components. A critical path computed without resource constraints cannot by itself justify a delivery promise.

Forecasts are conditional hypotheses. Forecasting final cost from today's CPI assumes future efficiency resembles past efficiency; this can be badly wrong when remaining work is qualitatively different. A stronger forecast decomposes **estimate to complete (ETC)** by work package, models uncertainty and explicitly reserves effort for integration and verification. A management reserve is not a substitute for a technically feasible schedule.

## Formal model and derivation

\[CPI=\frac{EV}{AC},\quad SPI=\frac{EV}{PV},\quad CV=EV-AC,\quad SV=EV-PV.\]
With budget at completion \(BAC\), the simple efficiency extrapolation \(EAC=BAC/CPI\) is an *assumption*, not a physical law. A bottom-up forecast instead uses \(EAC=AC+ETC\). The two answers should be reconciled against technical remaining work.

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

Suppose a configured propulsion-and-charging project has BAC = $9.0M, PV = $4.0M, EV = $3.2M, and AC = $4.0M at the gate. CPI = 0.80, SPI = 0.80, and CV = −$0.8M. Efficiency extrapolation yields $11.25M. But the engineering team re-estimates the remaining integration and assurance work at $6.3M, leading to a bottom-up EAC of $10.3M. These numbers are not an arithmetic contradiction; they encode two forecasts with different assumptions. The $0.95M gap should become a review question, not be averaged without reasoning. If only 5% of integration evidence exists, a nominal 80% schedule index could be misleadingly reassuring.

![Model of the linked reasoning steps](../figures/02-earned-value.svg)

## Counterexample and critical review

**Counterexample:** A work package earns all of its budget at “software code complete,” but the interface is not integrated and safety tests fail. EV improves even though operational readiness deteriorates. Repair the measurement rule: allocate credit to independently reviewed design, integrated interface, and demonstrated requirement evidence. Do not simply inflate subjective percent-complete numbers.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

Calculate the two indices and cost variance from PV = 5.0, EV = 4.1, AC = 4.8 (millions).

<details><summary>Worked answer and engineering interpretation</summary>

CPI = 4.1/4.8 ≈ 0.854; SPI = 4.1/5.0 = 0.820; CV = 4.1 − 4.8 = −0.7 million. Both indices are below 1.0, but neither identifies the technical cause.

</details>

### Problem 2

BAC = $12M and CPI = 0.80. Compare efficiency EAC with an AC = $6M, ETC = $7M forecast.

<details><summary>Worked answer and engineering interpretation</summary>

Efficiency EAC = $15M; bottom-up EAC = $13M. Investigate the assumption about remaining work, not an arbitrary midpoint.

</details>

### Problem 3

A subsystem is accepted in a bench test but fails end-to-end latency. What must change in the baseline?

<details><summary>Worked answer and engineering interpretation</summary>

Retain the bench result as limited evidence; revise the requirement evidence mapping and remaining integration plan, record an accountable discrepancy and reforecast schedule and cost before claiming closure.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/02-earned-value.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 2 and its existing weekly lessons](../../B2/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)
