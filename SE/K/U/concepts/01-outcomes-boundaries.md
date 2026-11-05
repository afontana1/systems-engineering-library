# 01 · Outcomes, system boundaries, and operational scenarios

**Concept dossier · Foundations / conceptual design / enterprise engineering**  
**Prerequisites:** stakeholders, systems thinking, basic causal reasoning  
**When to use:** before writing requirements, buying a solution, declaring a capability gap, or choosing a metric.

## The key distinction

An **outcome** describes a change in the world that matters to stakeholders. A **system** is an arrangement of interacting elements that can contribute to that outcome. A **system boundary** identifies which elements, decisions, and behaviors are treated as inside the system of interest for a particular analysis. Boundaries are analytical choices, not facts of nature: a shuttle controller is a system when evaluating braking software, while a regional evacuation service includes operators, agreements, roads, dispatchers, and public trust.

A useful first question is not *Which system shall we build?* but *Which people need what outcome, under what conditions, with what tradeoffs?* A solution selected too early suppresses alternatives. The distinction between a need and a proposed solution is the foundation of defensible conceptual design.

## Three nested boundaries

Consider a fictional campus shuttle that serves people who cannot safely walk across a large site. We might examine three boundaries:

1. **Vehicle:** propulsion, perception, brakes, doors and onboard controller. Question: does the vehicle stop within a specified envelope?
2. **Service:** vehicles, dispatch, charging, curb infrastructure, incident response and people. Question: does a passenger complete an accessible journey?
3. **Enterprise ecosystem:** campus administrators, contractors, regulators, emergency services and nearby transit. Question: is the mobility service dependable, equitable and sustainable?

A performance improvement at one boundary can be a system-level regression at another. Faster dispatch might reduce average wait while increasing inaccessible pickup events. Every metric therefore needs a defined population and boundary.

## A reproducible scenario-to-measure chain

Construct an operational scenario as a tuple:

`scenario = (actor, goal, trigger, context, sequence, exception, outcome)`

Example: A wheelchair user requests a pickup during a storm; the curb is temporarily blocked, wireless connectivity is intermittent, and the shuttle must offer an alternate accessible boarding point. The scenario exposes three different concerns: **availability** (is service offered?), **accessibility** (can the user actually board?), and **resilience** (can the service adapt during disruption?).

A plausible service outcome metric is the fraction of eligible trip requests that result in completed accessible journeys within 20 minutes. Let `N_completed` count eligible requests meeting that definition and `N_eligible` count all eligible requests in the reporting window. Then `service_success = N_completed / N_eligible`. If 176 of 200 requests qualify, the observed fraction is 0.88. This is a descriptive estimate, not yet a general claim about future storms. A valid report also documents exclusions, missing records, subgroup performance, scenario mix and time window.

Do not turn “20 minutes” or “0.88” into a requirement without stakeholder negotiation, feasibility analysis and risk assessment. In a real service, stakeholders would need to agree on how requests cancelled by users, inaccessible locations and emergency interruptions count.

## Four questions for a boundary review

| Question | What to record | A failure it prevents |
|---|---|---|
| What belongs inside? | Elements, operators, decisions, controllable actions | Silent responsibility gaps |
| What crosses it? | People, material, energy, information, authority | Unmanaged interfaces |
| What is outside but influential? | Weather, regulations, incentives, other providers | Unrealistic independence assumptions |
| Who experiences consequences? | Users, maintainers, neighbors, excluded groups | Optimization for the easiest-to-measure stakeholder |

## Worked decision

Two proposed concepts compete: **A**, add another shuttle; **B**, introduce coordinated curb management and dispatch exception handling. Vehicle utilization data alone might favor A. Under the blocked-curb scenario, however, B may remove the actual bottleneck. A functional analysis should separate *transport capacity* from *accessible boarding coordination* before spending capital. A concept study should test both under multiple scenarios, record dependencies and maintain a no-action baseline.

## Misconceptions and failure modes

- “The boundary is the organizational chart.” Organizations may not own every critical dependency or consequence.
- “A metric tells us whether users benefit.” It tells us only what its operational definition measures.
- “A ConOps is a marketing story.” It is a structured statement of actors, operations, modes, off-nominal behavior, responsibilities and constraints.
- “One scenario proves the concept.” Scenarios sample a much larger space; they cannot by themselves establish completeness.

## Try it

**Exercise A.** Write a boundary statement for a medication delivery drone and name three interfaces that cross it. **Suggested answer:** “This assessment includes the dispatch service, drone, landing process and recipient confirmation, but not the hospital's prescribing system.” Interfaces include order authorization, airspace coordination and recipient handoff. Other defensible boundaries are possible if made explicit.

**Exercise B.** A team claims 98% “delivery success” after excluding weather cancellations. What would you ask? **Answer:** whether cancellations are part of the intended service population; how nonresponses and unsafe delivery attempts were counted; and whether the result generalizes across conditions and users.

**Transfer artifact:** one context diagram, one scenario set (nominal/degraded/emergency), a stakeholder-outcome table and a metric dictionary with units, exclusions and owner.

## Connections

**Build next:** [Requirements, evidence and traceability](02-requirements-evidence.md) → [Architecture and interfaces](03-architecture-states.md).  
**Revisit in:** [Enterprise capability and governance](13-sos-enterprise-governance.md) and [Causal interventions and fairness](14-causal-interventions.md).  
**Legacy primer:** [System of interest](../../encyclopedia/system-of-interest.md), [ConOps and scenarios](../../encyclopedia/conops-and-scenarios.md).
