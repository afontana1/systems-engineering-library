# Integrated practice case — From a campus shuttle mission to an executable pilot

**Purpose:** Work one fictional problem from stakeholder outcomes through engineering decisions into an executable, measured project. The figures are teaching assumptions, **not** predictions, operational recommendations or safety certifications. Reproduce all calculations with `tools/phase0_calculators.py`, then change one assumption and explain which artifacts must be updated.

## Case brief and baseline assumptions

A university wishes to test an accessible, low-speed, supervised shuttle between three campus stops for 90 days. It values predictable late-evening transport and wants evidence before expanding public service. The project team is accountable for a controlled pilot, not unrestricted autonomy. Assumptions: two vehicles, one dispatch service, a campus-owned communications network, campus-provided charging infrastructure and an accessible passenger support route. Vehicle safety decisions are subject to designated authority and applicable rules (not determined by this exercise).

### 1. Boundary alternatives

**B1 / vehicle-only:** supplier provides two vehicles and onboard software; dispatch and rider support remain outside the contract. **B2 / pilot service:** contractor provides vehicles, dispatch, operating procedure and measured service outcomes; campus retains permits, roadway control, utility infrastructure and emergency authority. Choose B2 for a service-level evaluation, but create explicit boundary contracts for the campus-owned systems. The decision transfers integration responsibility to the pilot team—it does not make campus infrastructure optional.

**Interface contracts to define:** I-01 route assignment (dispatch→vehicle); I-02 vehicle status (vehicle→dispatch); I-03 boarding assistance request (rider app→operator); I-04 charging availability (campus facility→fleet); I-05 emergency response (vehicle/controller→designated supervisor). Each needs payload/physical flow, units, timestamps, authorization, normal and abnormal response, owner and interface test.

### 2. Value chain and evidence

| Stakeholder need | Example measurable obligation | Implementation responsibility | Verification and validation |
|---|---|---|---|
| Predictable late rides | During the 90-day pilot, >=95% of scheduled rides completed within 5 minutes of published arrival, under a defined cancellation/exclusion policy | Dispatch, operations, vehicles | Time-stamped trip log audit; rider journeys and operational scenarios |
| Accessible boarding | All approved mobility-device boarding scenarios completed with specified geometry and trained operator support | Vehicle boarding system, campus stops, operators | Representative physical tests, independent accessibility review and operator validation |
| Safe response to network loss | After dispatch link loss beyond defined timeout, controller follows an approved safe-state transition | Vehicle controller and dispatcher | Fault injection on configured system; operational drill and hazard review |

The first row is a possible mission MOE. The third row is deliberately incomplete until the safety authority defines the safe state, allowable speed/environment and time requirements. Do not claim the vehicle is safe because the row exists.

### 3. Functions and allocation

Functions: F1 receive/validate trip request; F2 allocate capacity; F3 send route command; F4 execute route; F5 monitor hazards; F6 enter degraded safe mode; F7 assist boarding; F8 log operational outcomes. Allocate F1/F2/F3 primarily to dispatch, F4/F5/F6 to onboard controller, F7 to vehicle/operator/campus facilities and F8 to the integrated service. Cross-boundary functions require agreed handshakes and fallback procedures.

### 4. Two alternatives and conditional trade

Compare A (vehicle-local autonomy with dispatch coordination) and B (dispatch-heavy route control). Assume both pass mandatory preliminary constraints; otherwise do not score them. Illustrative normalized scores on access/cost/maintainability are A=(90,60,70), B=(70,85,80). At weights (0.50,0.30,0.20): A=77; B=76.5. However, at weights (0.40,0.40,0.20): A=74; B=78. This is a *fragile choice* and must be revisited with actual hazard, interface and operational evidence.

### 5. Scope decomposition and cost logic

Use deliverable-oriented WBS: 1.1 vehicles and onboard control; 1.2 dispatch and passenger communication; 1.3 campus interfaces and charging integration; 1.4 verification and pilot preparation; 1.5 operational readiness. Each work package needs a dictionary, owner, explicit exclusion and measurable completed output. External network and charging construction must appear as dependencies and contractual assumptions even if the campus pays directly.

An illustrative early engineering estimate contains 160 h×$130/h=$20,800, $18,000 equipment, $2,500 licenses and $6,000 independent test, subtotal $47,300. A provisional 10% contingency of $4,730 gives $52,030 for this **limited example scope only**. Do not mistake this teaching subtotal for total capital or lifecycle cost of a two-vehicle pilot. The actual pilot budget would require full WBS-level estimation and documented risks.

### 6. Network schedule

| Activity | Description | Duration (days) | Predecessors |
|---|---|---:|---|
| A | Architecture authorization | 3 | — |
| B | Procure interface equipment | 5 | A |
| C | Define controller and dispatch integration | 4 | A |
| D | Integration demonstration | 3 | B, C |
| E | Pilot acceptance review | 2 | D |

Forward pass gives 13-day earliest finish for this *small demonstration slice*. A–B–D–E is the critical path; C has one day of total float. This model assumes unlimited resource availability and no external permit delays. It is not the full pilot installation schedule.

### 7. Progress, forecast and authority

Suppose the total project management control case (separate from the small engineering subtotal) has BAC=$500,000, PV=$250,000, EV=$200,000 and AC=$240,000 at a selected status date. CPI=0.8333 and SPI=0.8; a cumulative-CPI continuation gives an indicative EAC near $600,000. This forecast is sensitive to remaining work and should be compared with a bottom-up EAC. The sponsor, PM, chief engineer and customer authority must decide whether to reduce scope, modify resourcing, change authorization, or accept revised commitments.

### 8. Review decision and pilot restriction

The concept team proposes authorizing detailed design and controlled integration tests **only**. It explicitly withholds authorization for public shuttle operation pending accessibility, emergency response, network-loss integration, operator training and legal/operational readiness evidence. The project manager revises the cost/schedule forecast while the systems engineer maintains the technical trace and review findings. No unresolved mandatory requirement is treated as waived merely because the schedule is late.

## Independent transfer questions (try before looking below)

1. If charging infrastructure shifts outside the project contract, which technical and management artifacts still require an entry?
2. The route command schema adds a mandatory timestamp. Which dependent tests and work packages must change?
3. Supplier delivery B increases to 7 days. What is the new logical earliest finish and which planned milestone needs escalation?
4. PV rises to $275k while EV and AC remain unchanged. What changed in SPI and what did not change in CPI?

<details><summary>Reasoned solutions</summary>

1. Boundary decision, context and interface contract, assumptions/exclusions, risk register, WBS dictionary dependencies, supplier/campus agreement and schedule logic all still require explicit recognition. External funding is not external irrelevance.
2. Interface ICD and version, dispatcher producer contract tests, vehicle consumer negative tests, end-to-end integration, configuration index, related requirements and the scope/schedule/cost work for rework and regression.
3. A–B–D–E grows to 3+7+3+2=15 days. Recalculate all paths and resources, then notify milestone decision owner under escalation thresholds.
4. SPI = 200/275 ≈0.727 (worse); CPI = 200/240 ≈0.833 (unchanged). More work planned by the status date does not mean more work earned or dollars spent.

</details>

## Evidence chain challenge

For each of the eight sections, record at least one **claim**, **assumption**, **configuration-controlled artifact**, **failure mode** and **decision owner**. If you cannot fill a cell, that is the topic to research next. Use the companion chapters for the underlying logic and the original course rubrics for your full deliverables.
