# Causal evaluation of systems-engineering process improvement

*Graduate study for Book 17 — Systems Engineering Process Improvement. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> If a pilot team becomes faster after adopting a new review process, how much improvement can the process claim?

## Theory and conceptual structure

Process improvement begins with an operational definition of the outcome. “Lead time” can mean time from request to assigned engineer, from ready-for-review to acceptance, or from change proposal to deployed validated configuration. These are different quantities; comparing one before the pilot with another after the pilot fabricates improvement. Use timestamped event logs, a stable workflow boundary and explicit censoring rules for open work.

Before-and-after comparisons are confounded by team experience, case complexity, staffing, demand and concurrent changes. A comparison group can improve inference, but causal claims still require assumptions. Difference-in-differences compares the treated team's change with a control team's change, relying particularly on a credible *parallel-trends* assumption in the absence of treatment. Pre-period event-time plots, balance checks and placebo outcomes help challenge that assumption.

Engineering outcomes are often skewed and correlated. Cycle times have long tails; medians and high quantiles may be more informative than means. Multiple changes from the same project are not independent observations. Bootstrap procedures or clustered uncertainty methods should reflect the unit of intervention. A statistically significant reduction in average lead time may still be unacceptable if escaped defects or hazard review omissions increase.

Sustainment requires a control plan: metric definitions, owners, measurement frequency, triggers and escalation. A one-time pilot result does not prove capability maturity across contexts. Process changes should be tied to the engineering assurance system so that faster throughput cannot come from bypassing mandatory gates.

## Formal model and derivation

\[\widehat\tau_{DiD}=(\bar Y_{T,post}-\bar Y_{T,pre})-(\bar Y_{C,post}-\bar Y_{C,pre}).\]
This estimates a treatment effect only under assumptions including no relevant spillover and parallel untreated trends. Because lower lead time is better, a negative estimate suggests improvement.

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

The pilot team's mean review lead time falls from 18 to 11 days, a 7-day decrease. A similar control team's time falls from 15 to 12 days, a 3-day decrease. The difference-in-differences estimate is −7 − (−3) = −4 days. That is the adjusted association under the proposed design—not proof of causation. If the pilot selected easy cases while the control absorbed complicated safety changes, the estimate may be biased. Examine pre-trends and severity stratification before making a rollout decision.

![Model of the linked reasoning steps](../figures/17-process-causality.svg)

## Counterexample and critical review

**Counterexample:** The pilot reports fewer defects because staff reclassify them as “enhancements.” Incident rates appear lower without a change in product quality. Audit taxonomy and sample underlying records before treating the series as comparable.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

Calculate DiD for treatment 20→12 days and control 17→14 days.

<details><summary>Worked answer and engineering interpretation</summary>

Treatment change −8; control change −3; adjusted effect −5 days, subject to the design assumptions.

</details>

### Problem 2

Explain why a random bootstrap over individual tasks may understate uncertainty.

<details><summary>Worked answer and engineering interpretation</summary>

Tasks within the same team or project share causes. Resample the cluster or use a model that accounts for dependency.

</details>

### Problem 3

Give a guardrail metric against faster but unsafe reviews.

<details><summary>Worked answer and engineering interpretation</summary>

Track escaped high-severity defects, missing traceability/evidence, hazard review omissions or reversal rates on configured releases.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/17-process-causality.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 17 and its existing weekly lessons](../../B17/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook)
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)
