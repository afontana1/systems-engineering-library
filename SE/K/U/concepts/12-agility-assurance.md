# 12 · Agile flow without losing systems assurance

**Concept dossier · Agile Systems Engineering / process improvement / configuration control**

## Agility is the ability to respond responsibly

Agile methods shorten feedback loops and make uncertainty visible. For systems engineering, real agility means changing plans and designs **while preserving required evidence, safety constraints, authority and configuration coherence**. It is not the absence of documentation or a license to skip technical reviews.

A small software change might be reversible within minutes. A hardware interface change may require procurement, retesting, regulatory review and physical rework. Treat change categories differently; do not make every component follow the same iteration cadence.

## Flow and evidence capacity

Work-in-progress limits can reduce queueing at scarce technical review resources. Suppose a team starts 15 architecture changes per month but reviewers can dispose of 10; the review queue grows by 5 monthly in expectation. Merely increasing development velocity worsens approval lead time. Improve intake criteria, evidence quality, cross-training, reviewer capacity or decision-right boundaries. Also distinguish genuinely necessary assurance steps from repeated low-value handoffs.

Use a board with states such as `proposed → impact assessed → implemented → verified → integrated → approved`. Each state has an *exit criterion*. A ticket marked “done” because a pull request merged is not necessarily an integrated, validated system change.

## Change categories and risk

A useful tailoring scheme includes:

- **Low-impact reversible:** localized documentation, noncritical user copy, changes with narrowly bounded interfaces.
- **Moderate-impact:** interface contracts, performance budgets, updated data models and dependent services.
- **High-consequence:** safety logic, access-control rules, hardware tolerances and emergency procedures.

For every class define who approves, what evidence is needed, which regression tests apply, and what rollback or safe-state actions exist. Categorization itself must be audited; an incorrect “low risk” label can become a loophole.

## Worked failure and recovery

A team updates a dispatch policy to reduce waiting time and releases it after passing unit tests. A policy rule now deprioritizes wheelchair-accessible vehicles during peaks. The defect is not necessarily a coding bug—it may be an unexamined system-level objective and fairness requirement. A disciplined incremental release would include scenario-level acceptance tests, subgroup monitoring, guarded deployment, rapid rollback and an owner authorized to stop rollout.

Feedback after a release should update not only code but also needs, requirements, architecture, regression cases and risk registers. Otherwise each sprint creates a widening gap between the operational system and its documented assurance basis.

## Process improvement versus local speed

Improvement requires an operational definition: end-to-end time from proposed change to approved deployed evidence, rework rate, escaped defects, scenario coverage, recovery time, or stakeholder outcome. Measure across the whole flow, not one handoff. A change that shortens coding time while increasing field incidents is not overall improvement.

Use pilot and control approaches where possible, watch for demand-mix confounding, and include guardrails. Formal safety obligations remain independent of local delivery-method preference.

## Exercises with answers

**A.** Does sprint completion imply system acceptance? **Answer:** no. Acceptance depends on configured evidence, integration, requirements and legitimate authority.

**B.** What is a leading sign that more work is being started than completed? **Answer:** rising WIP and age of items; throughput and cycle-time distributions should be reviewed together.

**C.** What should be versioned after a safety-related change? **Answer:** impacted requirements, architecture/models, code/hardware, tests, evidence and approved decisions, with rollback/transition rules.

**Transfer artifact:** change-class policy, evidence-based work board, WIP/flow analysis and one bounded pilot evaluation.

## Connections

[Project control](06-cost-schedule.md) · [Queue dynamics](09-queues-feedback.md) · [Software architecture](04-software-quality.md) · [Digital provenance](11-digital-thread.md).  
**Existing primer:** [Agile tailoring](../../encyclopedia/agile-tailoring.md).
