# Chapter 6 — A Review Is a Decision, Not a Presentation

*EN.645.662 · Week 6. This chapter builds on the functional baseline in [Chapter 5](05-functions-and-behavior.md) and prepares [Hypothetical Lab 6](../labs/lab-06-functional-review-board.md).*

## The beautiful slide deck that could not be approved

The Northstar team prepares a polished 20-slide presentation: mission, requirements, functional hierarchy, attractive renderings, and an optimistic schedule. The review board asks to see the current definition of the request state machine and the requirement it is meant to satisfy. Three people give three versions. The evidence folder contains a PDF whose source model is missing; the test plan cites a superseded requirement; a stakeholder disagreement has been removed from the summary. The presentation may communicate ambition, but it cannot support the decision the board has been asked to make.

A **technical baseline review** is a structured decision under uncertainty. The question is not “Did the team work hard?” but “Is the current baseline coherent, controlled, and sufficiently mature to support the next commitment?” The reviewer must know the decision at issue, the evidence needed, the limitations of that evidence, and the conditions under which work may proceed. The team should expect findings. The quality criterion is whether findings are specific and acted upon, not whether the presentation receives praise.

## 6.1 Define the decision and the authority

A midcourse functional baseline review is not permission to manufacture autonomous vehicles or operate on public roads. Its narrow purpose in this fictional curriculum is to decide whether the chain from mission boundary through needs, requirements, scenarios, and functional logic is mature enough to begin serious concept allocation. The board could return one of three decisions:

- **Proceed:** required entry and exit criteria are met and no unacceptable open findings remain.
- **Proceed with controlled actions:** limited next-step work is permitted, with named conditions, owners, and dates. This cannot be used to waive a critical safety requirement silently.
- **Rework and reconvene:** fundamental gaps undermine confidence; the next commitment is not authorized.

Before review, decide who may approve a baseline change, who can accept residual risk, and who speaks for each critical stakeholder need. A project manager cannot automatically accept every technical hazard merely by accepting schedule pressure. Decision rights are part of the system of engineering governance.

## The mechanism beneath the method

Technical reviews are information-to-commitment gates: they should change what an organization is willing to invest, freeze or expose to risk.

### Distinguishing related ideas

A review slide showing that tasks are complete is weaker than evidence that unresolved assumptions cannot reverse the immediate decision.

### Interpretation and boundary conditions

An open interface uncertainty might be acceptable before a feasibility study but not before a costly production commitment; gate criteria depend on irreversibility.

## 6.2 Entry evidence is a set of resolvable objects

The evidence index should contain a controlled identifier, revision, owner, status, link, and applicable review criterion for each item. For Northstar, it can include the mission boundary, stakeholder register, ConOps and five scenario descriptions, approved needs, requirement baseline, requirement-to-function trace matrix, function hierarchy, state model, flow dictionary, assumption register, and change log. An index entry pointing to a nonexistent model is not evidence. Neither is a link to a document that has been materially changed after it was reviewed without recorded approval.

Different claims require different kinds of support. A diagram may support the claim that the team has modeled dispatch states; it does not demonstrate that the states are exhaustive under network failure. A scenario walk-through may support completeness for a defined scenario set; it does not establish that all plausible operational conditions have been considered. A trace count can demonstrate structural coverage; it cannot show that the links express the correct relationship.

The board should use an **evidence sufficiency question** for each claim: *Does this controlled object, in this revision and context, support precisely the proposition the team makes?* That question is more demanding than “Was a file submitted?”

## 6.3 Findings are engineering change instructions

A finding needs five parts: **observed condition, expected condition, consequence, responsible owner, and closure evidence**. Severity and due date should also be explicit. Weak: “Improve the architecture.” Strong: “The functional state model permits an assigned request to be closed without either trip completion or a documented cancellation. This violates the request-accounting rule and could conceal unmet service. Owner: dispatch model lead. Closure: revised controlled model, scenario traces for both outcomes, independent review, and updated requirement link.”

A **major finding** blocks the next commitment when it compromises a critical requirement, mission argument, or review validity. A **moderate finding** may be managed under a documented action plan if the decision authority accepts the residual consequences. A **minor finding** is not an excuse to leave the baseline permanently ambiguous. There is no universal severity matrix: the case-specific consequence and review policy matter.

Do not confuse *closure* with *someone checking a box*. True closure requires evidence that the condition has been corrected and that the correction has not broken something else. The system engineer must perform **change-impact analysis** whenever a finding changes requirements, functions, interfaces, test plans, or assumptions.

## 6.4 Worked board decision

Suppose the submitted review has eight declared criteria. Six are satisfied. One medium-severity item concerns an incomplete flow dictionary for a noncritical report; one major item concerns an undefined safe response when telemetry becomes stale. An unweighted completion count would be 6/8 = 75%. It would be a serious error to call the baseline “75% ready” and proceed because a nominal score is high. The missing telemetry response may invalidate the operational safety reasoning. Review criteria are **decision gates**, not interchangeable points.

The board should choose **rework and reconvene** until the major issue is resolved. It may permit isolated exploratory work that cannot create unapproved integration commitments. The team should add a function for stale-data detection, specify the transition to a safe or degraded state, update scenarios and requirement links, and produce an evidence-backed closure record. The medium finding may remain under a controlled action if the defined review policy allows it. The decision record should explain why the major item changes the decision even though most files exist.

## 6.5 Manage baseline changes without destroying history

Suppose the review changes the threshold for “stale telemetry.” Do not quietly edit the approved requirement in place and leave old tests attached. Record the change request, rationale, affected model elements, revised version, approval, and impact on planned tests. Superseded revisions remain historical evidence of what was reviewed at the time. The current authoritative baseline must be unambiguous. A reviewer should be able to reconstruct *which version supported which decision*.

A review board also needs independence of thought. Independence is not necessarily organizational separation, but it means the reviewer can challenge the team's assertions without being required to defend the design. Ask one reviewer to take the position of a rider, another an operator, another a verifier, another a safety representative. If they all examine the same approved requirement from different perspectives, they will detect different classes of omission.

## 6.6 Practice with explained answers

**A. Diagnose.** A finding says “Requirements are weak.” Is it closable? **Answer:** Not yet; it lacks the specific condition, expectation, impact, and objective closure evidence.

**B. Decide.** Seven of eight checklist rows are complete; the open row concerns absence of safe degradation behavior. Can the board average it away? **Answer:** No. A critical gap can block a decision regardless of checklist percentage.

**C. Evidence.** A requirements matrix refers to model revision 2, but the team demonstrates revision 4. What must be done? **Answer:** Re-establish the controlled review configuration and trace the change impacts; revision 4 is not automatically verified by revision 2 evidence.

**D. Roles.** Should the same author who changed the model be the sole closure authority for a critical finding? **Answer:** Usually not. Independent checking increases credibility; the precise independence requirement depends on project risk and governance.

**E. Residual risk.** What does “approved with actions” require? **Answer:** Explicitly permitted work, bounded conditions, responsible owners, due dates, accepted residual risks, and evidence required to close each action.


## Graduate depth: technical reviews as assurance decisions
### Review gates separate evidence quality from confidence

A functional baseline review is an inference process: reviewers observe a limited set of artifacts and must decide whether committing to a subsequent design stage is justified. The artifacts are not the system itself. They are evidence about requirements completeness, behavioral consistency, stakeholder alignment, and the organization's ability to reproduce its conclusions. This distinction matters because a large document package can create an illusion of certainty while concealing untested claims. A board should therefore formulate a decision proposition in advance: *Given this configuration, operating envelope, known uncertainties, and stated conditions, is the next commitment acceptably bounded?* That proposition is narrower than declaring the entire system correct.

Evidence can be organized as a directed assurance graph. A claim depends on subclaims, each of which depends on arguments and observations. For example, the claim that a dispatch function is sufficiently specified depends on complete normal and exceptional scenarios, consistent state transitions, and identified human overrides. A review finding should identify the exact broken inference link. An unlabeled test screenshot cannot support a claim unless the scenario, configuration, instrumentation, procedure, and acceptance rule are known. Independence of review can reduce motivated reasoning, but independence does not compensate for missing measurements or an invalid model.

### Decisions have asymmetric error costs

The board faces at least four possible outcomes: proceed, proceed with restrictions, rework before proceeding, or stop. A false approval can propagate defects into expensive hardware, contracts, and operations; an unnecessary rejection can delay useful learning. A simple conceptual decision loss is `L(d, s)`, where `d` is the gate action and `s` the actual maturity state. With defensible likelihoods, an expected-loss comparison uses `E[L(d,S) | evidence] = sum_s L(d,s) P(s | evidence)`. This is a reasoning aid, not a requirement to manufacture numerical probabilities. When probabilities are unknown, scenario-based loss ranges and explicit worst-case exposure are more honest than a spurious decimal score.

Approval with conditions is meaningful only if restrictions really constrain exposure. If the dispatch team's timeout behavior is not verified, the board might authorize interface prototyping in a sandbox while prohibiting field deployment. The action has a traceable owner, evidence criterion, deadline, and clearly bounded permitted work. Calling an unknown item “low risk” without a plausible failure mechanism or closure plan does not make it low risk.

### A baseline is a reproducible snapshot

A review package should identify the requirement version, system boundary, model revision, interfaces, open anomalies, accepted assumptions, and approval authority. A dependency chain such as `need → requirement → function → behavior → verification method` allows reviewers to find contradictions across artifacts. The chain is not necessarily one-to-one: a safety requirement may constrain several functions, and a function may serve several needs. Traceability establishes coverage and change impact; it does not, by itself, establish semantic correctness.

Consider a hypothetical service whose model shows cancellation after assignment but whose stakeholder scenario permits cancellation while boarding. The discrepancy may be caught by checking the behavioral contract against the scenario, not by counting completed diagrams. The board should request a corrected model and tests of the disputed transition. This example illustrates how assurance, configuration control, and governance interact: the value of the gate lies in a decision whose assumptions can still be interrogated months later.

## Read, rehearse, produce

Conduct [Hypothetical Lab 6](../labs/lab-06-functional-review-board.md) as a simulated board hearing. Then prepare the original course's `662_W06_FBR_Package_v1.0`, including the review criteria, indexed evidence, recorded findings, closure actions, and defensible decision. Your course guide's actual gate is authoritative; the lab supplies only a rehearsal.

**Next:** [Chapter 7 — Architecture and interfaces](07-allocating-architecture-and-interfaces.md).
