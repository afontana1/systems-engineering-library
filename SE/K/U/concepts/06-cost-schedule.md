# 06 · Baselines, schedule logic, and project control

**Concept dossier · management of systems projects / agile delivery / portfolio governance**

## Technical planning and management are coupled

A **work breakdown structure** defines deliverable-oriented scope; a **schedule network** encodes precedence and resource logic; a **cost baseline** allocates authorized budget over time; a **configuration baseline** records what design and evidence have been approved. These are different structures with correspondences between them. A perfectly tracked schedule can still be tracking the wrong architecture or an unreviewed requirement change.

The useful unit for a planning discussion is an accountable deliverable with entry/exit evidence. “Build perception model” is ambiguous; “demonstrate scenario coverage with a versioned test report and approved limitations” gives reviewers a measurable completion condition.

## Critical path example

A small development network has activities:

| Activity | Duration (weeks) | Must follow |
|---|---:|---|
| A: define interfaces | 2 | — |
| B: implement dispatch | 4 | A |
| C: prepare test rig | 3 | A |
| D: integrate | 2 | B and C |
| E: acceptance review | 1 | D |

Earliest finishes: A=2, B=6, C=5, D=8, E=9. The longest chain A–B–D–E is **9 weeks**, while A–C–D–E is 8. The second chain has one week of total float under these simplistic assumptions. This is a deterministic precedence model: resource contention, calendar constraints, rework, probabilistic durations and external approvals can all change the plan.

## Earned value: calculation and interpretation

Suppose at review time the approved **planned value** PV is $200k, **earned value** EV is $170k, and **actual cost** AC is $190k. Then:

- `SV = EV - PV = -$30k` (earned less authorized work than planned by this date).
- `CV = EV - AC = -$20k` (earned work cost more than its budgeted value).
- `SPI = EV/PV = 0.85`; `CPI = EV/AC ≈ 0.895`.

These do not give an exact number of weeks late or the final cost automatically. CPI-based estimates at completion need an explicit forecasting assumption; nonlinear integration and late risk discovery can make a simple extrapolation misleading. If “earned” is credited for incomplete or unreviewed engineering artifacts, the measures become performative rather than informative.

## Connecting baselines to technical evidence

A change to the notification subsystem may alter requirements, interface contracts, test environments, work packages, procurement commitments and cost assumptions. A change-control decision should examine *both* technical impacts and authorized baseline impacts. A good change package includes affected requirements, design/model versions, verification plans, residual risks, cost/schedule effects and an approval rationale.

## Risk, issue and contingency

A **risk** is a possible event or condition with uncertain occurrence and consequences; an **issue** is something already observed or realized. “The test rig may arrive late” is a risk. “It did not arrive by the committed date” is an issue. Escalation and response options may differ. Risk exposure is not fully described by expected monetary value because catastrophic tail consequences and risk appetite matter.

## Exercises with answers

**A.** If EV rises through credit for unreviewed work, what can go wrong? **Answer:** SPI/CPI may look healthy while technical debt and verification risk accumulate. Define physical completion criteria.

**B.** Is the longest dependency path always the real controlling path? **Answer:** only under the model's assumptions; resource constraints and stochastic rework may create other bottlenecks.

**C.** What links an approved design change to project control? **Answer:** versioned requirements and model impact, updated affected work packages, schedule/cost authorization, test/evidence changes and accountable approval.

**Transfer artifact:** small WBS, precedence table, PV/EV/AC worksheet and linked change-impact record.

## Connections

[Requirements and evidence](02-requirements-evidence.md) · [Trade studies](05-trades-uncertainty.md) · [Agile delivery](12-agility-assurance.md).  
**Existing primer:** [WBS and baselines](../../encyclopedia/wbs-and-baselines.md).
