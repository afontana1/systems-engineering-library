# Chapter 9 — Communication Is a Technical Risk Control

*EN.645.667 · Week 9 · Stakeholder communication, conflict and leadership · Preceded by [Chapter 8](08-risk-change-and-quality.md); continue with [Chapter 10](10-integrated-recovery-control.md).*

> **Study contract.** This chapter teaches the concepts behind Week 9; practice them in [Hypothetical Lab 9](../labs/lab-09-leadership-and-communications.md), then complete the [original Week 9 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

Technical programs are coordination problems between people whose incentives, information and responsibilities differ. The supplier wants to protect delivery promises; the chief engineer wants a valid technical baseline; the sponsor wants visible progress; the operator fears a service that cannot be maintained. These positions may be rational within each role and still produce a failing project when information is withheld or disagreement is treated as insubordination.

The project manager should design communication around decisions and risk, not information volume. A thirty-page status report can be less useful than a one-page exception brief identifying what changed, which baseline is affected, whose authority is required, and when the decision must occur. Tailor communication by audience while preserving one authoritative set of facts. Contradictory “executive” and “engineering” versions of the same metric destroy trust.

Good leadership is not the absence of conflict. Productive technical conflict exposes assumptions and competing values. Dysfunctional conflict turns unknowns into personal blame or suppresses dissent. Psychological safety helps teams raise concerns early, but it does not remove accountability for evidence or decisions. Escalation is a safeguard when people cannot legitimately settle a matter at their level.

## Develop the method

Build a stakeholder communication matrix with information need, decision influence, cadence, owner, medium, confidentiality requirement, and feedback mechanism. Use a common reporting grammar: observation, interpretation, uncertainty, required decision, due date. For conflicts, interview each party to identify facts, assumptions, interests, and constraints separately. Reframe “the software team is late” into “the interface definition changed after the estimate; how much additional work is authorized?”

Run decision meetings with a stated scope and pre-read, invite relevant dissent, record alternatives and commitments, and assign follow-up. After a crisis, perform a learning review that distinguishes system conditions from individual conduct without erasing either.

## The mechanism beneath the method

Technical communication is a control mechanism because engineers and managers act on different beliefs unless status, assumptions and decision ownership are synchronized.

### Distinguishing related ideas

More reporting does not automatically improve control: indicators that arrive too late or suppress dissent can increase response delay.

### Interpretation and boundary conditions

A useful status report names an observation, what it implies, what remains uncertain, and which authorized decision it requires.

## Worked Northstar project example

The sponsor says “stop discussing technical problems; we need to keep the public date.” The safety lead says “the demonstration is not ready.” A better meeting question is “which demonstrations can be performed without passengers, under what controls, and what evidence remains before the public date becomes a credible commitment?” This separates a non-negotiable evidence gate from negotiable sequencing. The resulting decision memo contains facts, authority, limits, owner, and a revisit trigger.

## Conflict-resolution as a controlled experiment in assumptions

The sponsor and assurance lead often appear to be arguing about a date, but the underlying conflict may be about what “demonstration” means. One means a closed-track, unoccupied vehicle exercise; another means a public passenger trial. Clarify the operating mode, exposure, requirements and authorization before trying to negotiate the date. A strong facilitator separates genuine value conflicts from misunderstandings that can be resolved through definitions.

Build communication channels for *upward* reporting as well as downward instructions. When a test engineer reports an anomaly, the system should preserve its configuration and context, ensure the concern reaches a technical owner, and prevent status metrics from silently discarding it. A culture that reports only clean metrics selects data toward success and can make risk management worse. The project manager should ask what remains unknown and whether a team member would face retaliation for raising it.

**Mini-case.** An executive summary says “software delivery is 85% complete.” A technical lead says “85% of the planned stories are closed, but three critical interfaces remain unverified.” Those statements may both be literally true. A good leader translates them into one shared account: completed backlog items are not equivalent to verified mission capability. The executive brief should include integration status, evidence gaps, forecast and upcoming decisions.

A communication matrix also needs information classification. Public relations, vendor negotiations, cybersecurity weaknesses and personal data may require different access controls. A single source of technical truth does not imply that every artifact is disseminated to everyone. Build both controlled provenance and role-appropriate presentation.

## Boundary of the method

A communication plan measured by number of meetings encourages activity rather than decisions. Measure cycle time for important decisions, aging of blocked actions, and whether affected teams received consistent revisions.

## Retrieval questions and explained answers

1. **Question:** Why is conflict sometimes useful?
   **Explanation:** It can reveal incompatible assumptions, constraints or missing evidence before they become rework.
2. **Question:** How can a status report become unsafe?
   **Explanation:** By suppressing or redefining technical risk to satisfy a schedule narrative.
3. **Question:** What should a decision memo preserve?
   **Explanation:** Evidence, assumptions, alternatives, authority, disposition and follow-up trigger.


## Deeper theory: organizational communication as a distributed control system

### Technical organizations act with delayed, partial information

In a complex project, no participant sees the entire system state. Engineers observe local tests, suppliers observe component production, project managers observe schedules, and operators observe field behavior. These observations are delayed, noisy, and filtered through reporting conventions. The team therefore resembles a distributed estimator: each participant maintains a partial picture, while decision channels attempt to reconcile those pictures before actions become incompatible. A status report that says “green” without a date, definition, and supporting evidence is a low-information message even if every stakeholder receives it.

Consider an issue that takes two days to detect, three days to escalate, four days to decide, and five days to implement. The nominal response delay is fourteen days, before considering queueing or rework. If the system changes materially every week, a fourteen-day feedback loop may react to a state that no longer exists. Faster meetings do not necessarily improve control; shortening the delay requires better event triggers, clear authority, shared evidence, and a path for urgent exceptions. This is the organizational analogue of phase lag in engineering feedback systems.

### Communication quality depends on decision bandwidth

A useful message communicates the claim, the evidence supporting it, the uncertainty, the action requested, the decision deadline, and the owner. The receiver must be able to tell whether a message is for awareness, concurrence, approval, or immediate intervention. Ambiguous authority creates both duplicated work and dangerous gaps. High message volume can also degrade decision quality: if every engineering anomaly becomes a top-level escalation, the scarce attention of technical authorities is consumed before the genuinely critical signal arrives. Classification by safety consequence, irreversibility, and timing is more useful than sorting by who is most vocal.

Some disagreements contain information that a summary can erase. Mechanical and software teams may agree on an interface name while assigning different meanings to “ready.” One team means that power is available; another means that a safety self-test has completed. The conflict becomes productive when its hidden assumptions are written as explicit predicates and tested against realistic transitions. Suppressing dissent to protect a schedule metric destroys this evidence before it can influence architecture.

### Governance must account for incentives and truthful reporting

Metrics change behavior when they are attached to reward or penalty. If a project measures success by the count of closed defects, people may close duplicates, reclassify unresolved issues, or avoid reporting difficult problems. This is a special case of Goodhart's law: when a measure becomes a target, its usefulness as an independent indicator can deteriorate. Balanced indicators should include recurrence, time-to-detection, escaped defects, decision aging, and evidence of actual risk reduction. None is immune to gaming, so the organization needs independent review and a protected route for raising concerns.

For Northstar, a high-quality escalation might state that an intermittent dispatch timeout has affected 7 of 120 controlled trials, identify the tested software build and load conditions, describe the rider consequence, request authority to constrain operations, and propose an evidence-producing next step. It should not claim a population failure rate from a convenience sample or imply that seven occurrences prove a particular root cause. Communication is engineered when it preserves uncertainty while enabling timely action.

## Put this into practice

Work through [Lab 9: The Supplier–Safety Negotiation](../labs/lab-09-leadership-and-communications.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 9 primer](../../P0-text/lessons/645-667-w09.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.

## Step 03 integrated reference — communication as a control-loop design

Communication failures can be modeled as failures of feedback and authority, not merely as interpersonal misunderstandings. A supplier knows an interface will arrive late; the integrator's schedule still assumes the old date; the safety lead has test evidence tied to the prior configuration. Each group may be locally rational yet collectively wrong. A usable communication protocol states **what observation triggers notification, to whom, with what evidence, and within what response time**.

### Design a project status message with a decision payload

A helpful report is not “Amber: integration.” It says: *NS-B1 gateway test record references the previous interface revision; technical status is not accepted; acceptance test is blocked; proposed retest requires six fixture-days; owner is CA-04; review decision requested by a specified date.* That message connects the observed condition to its consequence and to an authorized next action. It remains intelligible to engineers, finance and operations without falsely declaring a completed safety argument.

An escalation protocol should include (1) objective trigger, (2) source revision, (3) confidence/uncertainty, (4) decision deadline, (5) reversible and irreversible options, and (6) explicit receipt/acknowledgment. A delivery receipt is not agreement or comprehension. For safety-critical messages, independent confirmation or closed-loop readback may be necessary. Project meeting attendance likewise is not evidence of an approved technical change.

### Quantify an escalation window

Suppose a stalled fixture costs an illustrative $18,000 per week and the right escalation route shortens a decision queue from five weeks to three. Avoided holding exposure is \((5-3)\times\$18{,}000=\$36{,}000\). It does not follow that an underinformed, faster decision is beneficial; an incorrect release can cost far more. Measure **decision cycle time** alongside **decision quality and corrective rework**, not instead of them.

### Avoid an optimistic common narrative

Three reports may agree because they all copy the same supplier status, not because they independently corroborate it. Separate facts (dated test records), interpretations (likely schedule effect), forecasts (probability of additional delay), and authorization (approved scope change). If safety and program leadership disagree, preserve both positions and the applicable decision authority rather than editing one record until apparent consensus is achieved.

**Practice with answer.** Management says “the schedule is green because the supplier confirmed delivery,” while the acceptance procedure requires an untested interface. **Answer:** distinguish supplier delivery status from verification acceptance; publish the evidence configuration and the blocked gate explicitly, with owner and time-bounded next decision. Reaching agreement on a slide color is not technical closure.

**Reference context:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) addresses technical reviews and decision analysis; adapt communication frequency and escalation authority to the project's actual risk and governance.
