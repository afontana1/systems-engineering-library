# Chapter 1 — Governance Is an Engineering Control System

*EN.645.667 · Week 1 · Project management, systems engineering, and decision authority · Preceded by [Introduction to Systems Engineering Volume I](../../B1/README.md); continue with [Chapter 2](02-rfp-and-proposal-strategy.md).*

> **Study contract.** This chapter teaches the concepts behind Week 1; practice them in [Hypothetical Lab 1](../labs/lab-01-governance-and-technical-authority.md), then complete the [original Week 1 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.


![Conceptual illustration: program governance](../figures/program-governance.svg)

*Figure — teaching diagram, showing relationships rather than evidence of system readiness.*

## The management problem

A project manager can produce a schedule and still be unable to lead a technical project. The missing ingredient is often not motivation but a reliable way for information to reach people who can authorize action. The campus shuttle team can discover a safety-relevant fault on Tuesday, understand its consequence on Wednesday, and still miss a decision on Friday because nobody knows who may suspend testing. Governance is the design of that decision-making system.

Systems engineering asks whether the selected solution will meet the need; project management asks whether the work needed to produce and substantiate that solution can be authorized, funded, coordinated, and delivered. The two are inseparable. A promise to deliver a shuttle by month 18 must be compared with the time required to validate interfaces and safety claims. The project manager cannot silently waive the validation, and the systems engineer cannot silently commit funds. Each needs a defined escalation path.

A project charter authorizes a bounded undertaking; it does not magically resolve contested technical authority. Distinguish **responsibility** (who does the work), **accountability** (who answers for the outcome), **decision rights** (who may approve a choice), and **technical concurrence** (whose specialist review is needed). A person may own cost and schedule without being permitted to accept a particular safety risk. A RACI table is a conversation starter, not a substitute for law, contract, or safety governance.

## Develop the method

Construct a decision-rights register with four columns: the decision, its approving authority, mandatory consultation, and its evidence record. Give separate entries to funding a work package, changing a software interface, accepting a residual hazard, and moving a review gate. Then test the map against a difficult case: a late supplier update would meet schedule but uses a different braking interface. The project manager can request a trade, but the configuration authority and safety authority must evaluate the technical consequences before release.

A useful management cadence couples daily exception reporting, weekly integrated project reviews, monthly baseline and risk reviews, and event-driven technical boards. Each meeting should have an input, a decision class, an owner, and a recorded action. If a board repeatedly receives the same unresolved issue, the defect may be insufficient authority or missing evidence, not merely poor meeting discipline.

A working project objective has several dimensions: the deliverable, acceptance conditions, target date, affordability envelope, operational stakeholders, and constraints. The charter should distinguish immutable customer conditions from internal planning assumptions that will be revisited.

## The mechanism beneath the method

Governance defines who can make technical commitments and who can accept residual risk, thereby shaping the feasible project architecture.

### Distinguishing related ideas

Accountability is not interchangeable with participation: several teams can contribute analysis while only one authority approves a changed performance baseline.

### Interpretation and boundary conditions

If decision rights are unclear, a late change becomes an unpriced commitment that spreads through scheduling, supplier work and test obligations.

## Deeper theory: governance is a distributed decision-control architecture

### Authority, information, and accountability are different resources

A program can have an unambiguous organization chart yet fail to make defensible technical decisions. The person authorized to spend money may not be qualified to determine safety adequacy; the specialist who understands a hazard may lack contractual authority to approve a deviation; the person affected by the outcome may have no formal vote. Effective governance defines at least three separable relationships: who may make a commitment, what evidence that person must consider, and who remains answerable for consequences. A RACI table communicates participation, but does not by itself confer legal or technical authority.

Governance can be modeled as a control system. Decision makers receive indicators of the current program state, compare them with objectives and constraints, issue authorized actions, and obtain feedback on whether those actions worked. Feedback must arrive before the next irreversible commitment. A review held after long-lead hardware has been purchased may document concern without preserving any useful ability to act. The value of a review therefore depends partly on decision timing and the remaining option set, not just on its checklist.

### Incomplete information creates agency problems

The program manager, engineering authority, supplier, safety organization, and eventual operator possess different information and incentives. A supplier rewarded for meeting delivery dates may rationally understate integration uncertainty; an engineering team rewarded for defect counts may defer finding defects until after a milestone. These are examples of principal–agent and information-asymmetry problems. They do not require misconduct. They arise because a local performance measure is an imperfect proxy for the purchaser's system-level outcome.

A governance mechanism can reduce such distortion through independent evidence, clearly defined escalation routes, traceable dissent, and acceptance criteria agreed before data are observed. Independent review does not replace accountable program decisions; it makes the limits of those decisions visible. Similarly, transparency is insufficient if no authorized person can act on the reported finding. Both information pathways and control authority must be designed.

### Decision thresholds must include the cost of delay

Suppose an unresolved interface uncertainty threatens a $3 million production commitment. An integration test costing $80,000 might reveal whether redesign is necessary. The test is valuable only if its information can arrive before the commitment and can change the chosen action. In decision-theoretic terms, expected value of sample information equals the expected utility under the best decision *after observing* test results minus the best expected utility without the test. The cost of the test and the delay it creates must then be subtracted. A mandatory review that cannot affect any downstream choice may be compliance activity, but it should not be confused with risk retirement.

The same reasoning explains why some decisions deserve centralized approval while others should be delegated. When consequences are local and reversible, rapid delegation may improve performance. When a decision changes shared safety assumptions, interfaces, or contractual acceptance criteria, local speed can impose uncontrolled external costs on the rest of the system. Governance should concentrate scarce scrutiny where decisions are consequential, coupled, or difficult to reverse.

### Escalation pathways are safety properties

An escalation route is operational only if it names a decision owner, maximum response time, required evidence, temporary operating rule, and resolution record. Without a time limit, an “open action” can act as silent authorization to proceed. Without a temporary rule, teams may make inconsistent assumptions while they wait. If technical authority and program authority disagree, the record should preserve the disagreement and the designated decision rule rather than erase the minority analysis.

In the fictional Northstar program, a schedule recovery proposal that removes a verification activity cannot be authorized solely by the person accountable for schedule. The safety or technical acceptance consequences must be evaluated by the proper authority, and the revised evidence path must be approved. Governance is effective when these constraints operate under pressure, not merely when the program is on plan.

## Worked Northstar project example

At the first governance hearing the sponsor asks to begin passenger trials before completion of a braking-interface verification. A decision audit lists: (1) proposed action; (2) affected requirements and hazards; (3) evidence available; (4) evidence missing; (5) approving role; and (6) conservative interim options. The project manager may authorize more bench testing within approved resources, but cannot equate sponsor urgency with independent safety approval. The defensible interim decision is to continue authorized non-passenger integration work and obtain the required technical disposition.

## Distinguishing management authority from evidence authority

Consider a four-stage project decision. The integration team first notices a behavior inconsistent with the interface specification. The responsible engineer diagnoses the defect and proposes a change. The project manager reviews its effects on money, people and milestones. A technical authority evaluates whether the changed design still satisfies the required functions and safety controls. A customer representative then determines whether a contractually significant baseline change is acceptable. These decisions may occur in different orders or under one board's charter, but the *decision types* must remain distinguishable. A signature from the wrong authority does not turn missing verification into valid evidence.

This distinction affects management reporting. If the PM reports that the gate is complete because the test plan was approved, a technical reviewer should ask whether tests have actually been performed and what their results support. Approval of a **plan** is not acceptance of a **product**. Conversely, the engineer's discovery of a technical problem does not automatically authorize unbudgeted work. The management process must convert the evidence into a bounded decision.

**Mini-case: a decision without a calendar.** Suppose an interface defect has a seven-day window before the supplier releases production firmware. The governance register lists the correct authority but the board only meets monthly. The authority map is formally complete but operationally inadequate. A workable escalation design includes an extraordinary-board procedure, minimum participants, data required for a temporary restriction, and a traceable final disposition. Governance has latency just like a technical control loop. When its response time exceeds the time available to prevent harm or rework, that mismatch is a real system defect.

**Try it.** For a design waiver, identify who proposes, who assesses technical effect, who funds the response, who approves the waiver, and who monitors conditions. If a single name occupies every role, explain why that concentration is or is not acceptable.

## Boundary of the method

An escalation path is not effective merely because it appears on an organization chart. Test it with a decision that crosses cost, safety and customer authority. A missing decision owner is a project risk, not an administrative footnote.

## Retrieval questions and explained answers

1. **Question:** Why is a RACI table insufficient for hazard acceptance?
   **Explanation:** Because assignment of participation is not the legal, contractual or specialist authority to accept safety risk.
2. **Question:** Can a PM approve a schedule recovery that invalidates a verification plan?
   **Explanation:** Not without required technical evaluation, change authorization and renewed evidence planning.
3. **Question:** What is an observable sign of governance failure?
   **Explanation:** Unresolved decisions recur without an authorized owner, due date or documented escalation.

## Put this into practice

Work through [Lab 1: The Authority Hearing](../labs/lab-01-governance-and-technical-authority.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 1 primer](../../P0-text/lessons/645-667-w01.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.

## Step 03 integrated reference — authority, evidence, and decision latency

A project authority chart is useful only if it specifies which decisions can change which controlled objects. In the fictional Northstar management baseline, **NS-M1** governs funding, schedule and work authorization while **NS-B1** governs the technical configuration and requirement evidence. A program manager may authorize additional funding within delegated limits; that does **not** authorize the safety authority to accept a hazard, nor does it allow a configuration custodian to declare a failed requirement verified. The two baselines are related but not interchangeable.

### Build an executable decision-rights matrix

| Controlled decision | Proposes | Technical recommendation | Authorizes | Required evidence |
|---|---|---|---|---|
| Change status-message timeout | Interface lead | Safety and V&V leads | Technical change board | Revised ICD, hazard impact, new test |
| Release management reserve | Control-account manager | Cost and risk leads | Delegated program manager | Causal risk event, updated EAC |
| Accept operational residual risk | System owner | Safety authority | Designated acceptance official | Hazard closure evidence and operating restrictions |
| Change project finish baseline | Scheduler | Independent planning review | Program baseline board | Logic, resources, impact, approved change |

A **RACI** chart describes participation but cannot replace a written decision authority and its limitations. For each decision, record an immutable identifier, exact baseline revision, assumptions, dissent, approver, date, effective scope, and conditions. The [NS-M1 decision register](../case/decision-register.csv) illustrates this separation. Its unresolved rows are intentionally *not* green approvals.

### Quantify the cost of a delayed decision

Suppose holding an integration fixture and specialist team costs a fictional $18,000 per week while a technical change is unresolved. If approval takes five weeks instead of two, the avoidable holding exposure is \(3\times\$18{,}000=\$54{,}000\), before any nonlinear knock-on effects. This is not a reason to waive assurance; it is a reason to identify decision prerequisites early and avoid queues caused by incomplete submissions. The number is a **conditional marginal cost**, not the total impact of the change.

A review board may delegate routine interface clarifications while reserving high-hazard changes for senior review, but escalation criteria must reference consequence and authority, not rank alone. Inspect the counterexample: a schedule board approves a two-second emergency-message timeout because it improves delivery; the safety analysis requires 1.5 seconds. Which decision is ineffective? The schedule decision does not overrule the controlled technical constraint. The proper response is a joint change proposal and new evidence, not silent reinterpretation of the acceptance criterion.

**Practice with answer.** A supplier asks to waive a missing NS-R-04 staleness indicator because its dashboard is otherwise complete. Identify (a) the object being changed, (b) the competent decision authority, and (c) the missing evidence. **Answer:** this changes a technical requirement and potentially an operational safety claim; a technical/acceptance authority must assess it, with revised hazard analysis, requirement disposition and verification evidence. A purchasing manager's sign-off is not enough.

**Reference connection:** NASA's [Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) distinguishes technical review, decision analysis, and verification/validation activities. Apply the principles within the specific project's delegated authority rules; the table above is instructional, not a universal governance standard.
