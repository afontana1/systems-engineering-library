# Phase 0 concept library — knowledge threads

The curriculum is a path; a thread is a reusable cluster of ideas that appears across weeks. Read down a thread to understand *why* concepts are prerequisites and how a decision in one discipline affects the other.

## Value and validation

A mission problem becomes a set of user journeys, measurable success criteria, verifiable obligations and actual acceptance evidence.

1. [645-662 · W1: System boundaries, emergent behavior and interface contracts](lessons/645-662-w01.md)
1. [645-662 · W3: From missions and stakeholders to measurable success](lessons/645-662-w03.md)
1. [645-662 · W4: Writing verifiable requirements and preserving rationale](lessons/645-662-w04.md)
1. [645-662 · W11: Integration, verification, validation and transition](lessons/645-662-w11.md)
1. [645-662 · W12: Synthesis: from trace chains to defensible system concepts](lessons/645-662-w12.md)
1. [645-667 · W2: From customer opportunity to compliant technical proposal](lessons/645-667-w02.md)
1. [645-667 · W12: Management synthesis: defend the commitment and learn](lessons/645-667-w12.md)

**Test your understanding:** Which claim or artifact passes from one step to the next? Which assumption could break the chain?

## Architecture and integration

Functions allocate to products; interface contracts become integration evidence; exceptions reveal dependencies hidden by isolated tests.

1. [645-662 · W5: Functional analysis: behavior before architecture](lessons/645-662-w05.md)
1. [645-662 · W7: Physical architecture, allocation and contract-level interfaces](lessons/645-662-w07.md)
1. [645-662 · W9: SE management plans, metrics and configuration discipline](lessons/645-662-w09.md)
1. [645-662 · W10: Systemic failures, causal reasoning and red-team thinking](lessons/645-662-w10.md)
1. [645-662 · W11: Integration, verification, validation and transition](lessons/645-662-w11.md)
1. [645-667 · W10: Managing integrated hardware, software and agile delivery](lessons/645-667-w10.md)

**Test your understanding:** Which claim or artifact passes from one step to the next? Which assumption could break the chain?

## Technical decisions and authority

Feasibility, preference and approval are distinct: the strongest concept still requires the right authority and evidence.

1. [645-662 · W2: Lifecycle reasoning, iteration and review decisions](lessons/645-662-w02.md)
1. [645-662 · W6: Technical reviews as falsifiable assurance arguments](lessons/645-662-w06.md)
1. [645-662 · W8: Trade studies, AHP and sensitivity without false precision](lessons/645-662-w08.md)
1. [645-667 · W1: Governance, decision rights and the PM–SE interface](lessons/645-667-w01.md)
1. [645-667 · W8: Risk, issue, opportunity and baseline change as one control system](lessons/645-667-w08.md)
1. [645-667 · W11: Proposal red teams and executable-plan stress tests](lessons/645-667-w11.md)

**Test your understanding:** Which claim or artifact passes from one step to the next? Which assumption could break the chain?

## Scope and executable commitments

Required capability flows into product scope, work packages, resources, estimates, dependencies and an integrated baseline.

1. [645-662 · W3: From missions and stakeholders to measurable success](lessons/645-662-w03.md)
1. [645-662 · W9: SE management plans, metrics and configuration discipline](lessons/645-662-w09.md)
1. [645-667 · W2: From customer opportunity to compliant technical proposal](lessons/645-667-w02.md)
1. [645-667 · W3: Product-oriented WBS, control accounts and work authorization](lessons/645-667-w03.md)
1. [645-667 · W4: Estimating, budget structure and uncertainty](lessons/645-667-w04.md)
1. [645-667 · W5: Critical path, network logic, float and schedule credibility](lessons/645-667-w05.md)
1. [645-667 · W6: Integrated baseline reviews: can the plan actually be executed?](lessons/645-667-w06.md)

**Test your understanding:** Which claim or artifact passes from one step to the next? Which assumption could break the chain?

## Uncertainty and control

Uncertainty appears as fragile decisions, technical risks, schedule exposure and forecast variance. Control must change decisions, not just reports.

1. [645-662 · W8: Trade studies, AHP and sensitivity without false precision](lessons/645-662-w08.md)
1. [645-662 · W10: Systemic failures, causal reasoning and red-team thinking](lessons/645-662-w10.md)
1. [645-667 · W4: Estimating, budget structure and uncertainty](lessons/645-667-w04.md)
1. [645-667 · W5: Critical path, network logic, float and schedule credibility](lessons/645-667-w05.md)
1. [645-667 · W7: Earned value, performance indices and honest forecasts](lessons/645-667-w07.md)
1. [645-667 · W8: Risk, issue, opportunity and baseline change as one control system](lessons/645-667-w08.md)
1. [645-667 · W12: Management synthesis: defend the commitment and learn](lessons/645-667-w12.md)

**Test your understanding:** Which claim or artifact passes from one step to the next? Which assumption could break the chain?

## Concept-to-artifact chain for the running project

```text
Mission and stakeholder context
  └── ConOps + scenarios + outcome measures
       └── Requirements + trace rationale
            └── Functional architecture + state behavior
                 └── Physical allocation + interface contracts
                      └── Trade study + controlled concept
                           └── Integration / verification / validation evidence
                               
                           WBS + scope dictionary
                             └── Work authorization + resources
                                  └── Cost / schedule integrated baseline
                                       └── EV / risks / changes / forecast
                                            └── Review + acceptance decision
```

A vertical chain here is a reasoning aid, not a claim that technical and project activities happen only in that order. Engineering and management iteratively influence each other.
