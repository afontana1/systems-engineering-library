# Agile engineering as a constrained flow and assurance system

*Graduate study for Book 15 — Agile Systems Engineering. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> When can faster sprint completion make a safety-relevant engineering program slower?

## Theory and conceptual structure

Agile systems engineering is not a prescription to replace lifecycle evidence with user stories. It is a strategy for delivering learning and integrated capability in smaller, inspectable increments while retaining responsibility for requirements, architecture, hazards, interfaces, and assurance. The key unit of work should carry an observable acceptance condition, configuration identifier and associated evidence—not merely a ticket in a completed column.

Queueing theory clarifies the relationship between work in progress (WIP), throughput and cycle time. Under a stable, well-defined boundary, Little's law relates mean WIP to mean throughput and mean time in the system. This is an average relationship, not a guarantee of individual lead time. A high utilization review board can exhibit long, volatile queues; raising the sprint team's coding throughput can simply move the bottleneck into test and verification.

A value stream includes design, model updates, integration, independent test, risk acceptance, and release. Visualizing only development tickets hides the true engineering cycle time. Split work into increments only when architectural interfaces and verification contracts permit meaningful evidence. If small deliveries each require repeated full qualification, batching policy may need to balance information value against setup cost.

Measurements are vulnerable to Goodhart effects. A team rewarded for closing tickets may reduce ticket size artificially, defer difficult defects, or declare done before safety evidence exists. Countermeasures include configuration-specific acceptance evidence, escaped-defect rates, rework flow, and decision latency. Continuous improvement must use these together rather than elevate a single velocity target into a success criterion.

## Formal model and derivation

\[L=\lambda W,\qquad W=\frac{L}{\lambda}.\]
For a simple M/M/1 approximation, \(W_q=\lambda/[\mu(\mu-\lambda)]\) when \(\lambda<\mu\). Near saturation, waiting time increases nonlinearly. These formulas require steady-state assumptions and a coherent definition of arrivals and completions.

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

Suppose a safety review board finishes an average of 8 engineering changes per week while 20 are in the queue/in process. Little's law implies 2.5 weeks mean time in the review system if the process is stable. Now development increases arrivals from 7 to 7.8/week while review capacity stays 8. In an M/M/1 illustrative model, mean total time jumps from 1 week at λ=7 to 5 weeks at λ=7.8. The point is not that actual review time is exponentially distributed, but that utilization and variation can swamp the benefit of faster upstream delivery.

![Model of the linked reasoning steps](../figures/15-agile-flow.svg)

## Counterexample and critical review

**Counterexample:** Leadership celebrates 30% more story closures while integration defects double and reviewers' queue ages. The supposed productivity gain reflects boundary selection. Re-measure from approved change proposal to evidence-backed capability release.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

A stable review system has WIP 24 and throughput 8/week. Estimate mean lead time.

<details><summary>Worked answer and engineering interpretation</summary>

W = 24/8 = 3 weeks. Clarify whether the 24 items and rate refer to the same workflow boundary.

</details>

### Problem 2

Using M/M/1, compare mean system times at λ=7 and 7.8 with μ=8 per week.

<details><summary>Worked answer and engineering interpretation</summary>

W = 1/(8−7)=1 week versus 1/(8−7.8)=5 weeks. This depends on a stylized arrival/service model.

</details>

### Problem 3

Propose a definition of done for a hazard-affecting software change.

<details><summary>Worked answer and engineering interpretation</summary>

It should include configured source, reviewed hazard impact, passed interface and regression tests, linked evidence, responsible safety acceptance and deployment rollback conditions.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/15-agile-flow.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 15 and its existing weekly lessons](../../B15/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)
