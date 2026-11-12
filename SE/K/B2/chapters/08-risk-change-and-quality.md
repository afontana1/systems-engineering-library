# Chapter 8 — Risk, Change, and Configuration Are Coupled

*EN.645.667 · Week 8 · Risk/issue distinction, change control, configuration and quality · Preceded by [Chapter 7](07-earned-value-and-forecasting.md); continue with [Chapter 9](09-leadership-and-communications.md).*

> **Study contract.** This chapter teaches the concepts behind Week 8; practice them in [Hypothetical Lab 8](../labs/lab-08-risk-change-and-quality.md), then complete the [original Week 8 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

The pilot has a supplier risk, a current braking-interface problem, and an opportunity to simplify the dispatch architecture. They are different management objects. A **risk** concerns uncertain future events; an **issue** is present now; an **opportunity** is an uncertain favorable outcome worth evaluating. Treating everything as a red-yellow-green item obscures the decision and the required response.

A risk register needs an initiating cause, possible event, consequence, owner, trigger, action, and review date. A high-risk item should influence budget, schedule, test design or choice of architecture—not just be recited at a monthly meeting. A configuration record identifies exactly which requirement, interface, software build, document or baseline is being changed. Quality management asks how work will consistently satisfy requirements and how defects will be detected and corrected. Together, they keep changes from causing unexamined downstream consequences.

Change control is not opposition to evolution. The point is to understand second-order effects before committing. A software patch that improves the dispatch algorithm might alter the onboard message format, which changes the vehicle interface specification, integration tests, training documentation, and safety evidence. The lowest apparent implementation cost may have the highest requalification cost.

## Develop the method

Evaluate a proposed change in six steps: identify the controlled configuration items and triggering need; map interfaces and requirements affected; estimate cost, schedule, safety, and verification consequences; compare options including rejection and deferment; obtain required approvals; then confirm implementation and evidence closure. Keep the **before** and **after** records. For risks, look for thresholds: a supplier slip of one week may be absorbable; a slip past the test-facility booking may add a month and a new cost driver.

Quality controls can use prevention, detection and corrective action. A review finding is not closed because a revised document exists; closure may require an independent test of the corrected behavior. Separate acceptance of a change request from evidence that the change worked.

### Change control protects the meaning of prior evidence

Configuration control is sometimes presented as an administrative brake on progress. Its deeper function is to prevent a change from silently altering the object that earlier tests, cost estimates, and approvals described. If a communications component changes its message timing, the product may still look functionally identical in a demonstration while invalidating interface performance evidence and assumptions in the safety analysis. The relevant question is not whether the change is “small” in lines of code; it is which claims depend on the modified behavior.

Risk and change management are coupled because a new option can reduce one uncertainty while creating another. Change decisions should distinguish urgency, authorization, technical effect, resource cost, and evidence that must be regenerated. A baseline is therefore an **agreement about identity and decision context**, not a ban on learning. Without baseline history, earned-value comparisons and technical acceptance statements become ambiguous: the numbers may refer to different products and different meanings of “complete.”

## Deeper theory: risk, change, and quality are coupled through causality

### Risk is conditional on the design state

A risk is a proposition about a possible future event under specified conditions. Its probability and consequences depend on architecture, operational exposure, mitigation status, and the version of the system being assessed. A statement such as “interface failure: medium likelihood, high impact” has little predictive meaning without identifying the interface, initiating events, workload, failure detection, and time horizon. The quantity `P(failure | configuration, environment, controls)` is conceptually different from a universal failure rate.

Changes update those conditions. Replacing a network adapter may reduce one type of packet loss while introducing different timing and driver behavior. Closing the old issue because the component was replaced is not the same as demonstrating the system's residual risk. The system engineer needs a claim that connects mitigation to the relevant failure mode, and then evidence that the modified design actually behaves as assumed.

### Common causes defeat independent-risk arithmetic

Risks associated with different work packages are not necessarily independent. A single supplier, shared software library, constrained laboratory, or untested assumption can affect many items simultaneously. If two interface failures both depend on the same identity service, multiplying their nominal independent probabilities understates joint outage risk. The proper analysis identifies a common cause C and considers terms such as `P(A and B | C)` and `P(C)`, or uses a fault tree, event tree, or causal network whose dependency assumptions are explicit.

This matters for contingency allocation. Ten individual risk allowances do not necessarily add to an appropriate program reserve when losses occur together. Conversely, summing each team's worst case can be overly conservative when scenarios are mutually exclusive. Program-level reserve should consider the aggregate loss distribution under plausible dependence, coupled with management judgment about low-probability consequences and non-financial constraints.

### Quality assurance and testing answer different questions

Quality assurance asks whether the process is likely to produce controlled, conforming outputs; quality control and verification ask what the actual product or evidence shows. A perfect process audit cannot prove that a changed interface satisfies its latency contract. A passing test cannot prove the process will consistently reproduce the same outcome after uncontrolled supplier or configuration changes. The two sources of confidence are complementary but not interchangeable.

Consider a revised emergency-stop command. The change record identifies affected interfaces; the hazard analysis identifies conditions under which command latency matters; configuration management identifies the exact implementation; testing measures latency under a relevant workload; and an authorized decision evaluates whether the remaining hazard is acceptable. Each link addresses a different possible failure of the argument. Treating a closed change ticket as equivalent to system safety acceptance skips several links.

### Learning can increase measured risk before reducing real risk

An effective fault-injection campaign may uncover additional failure modes and temporarily make a risk dashboard look worse. That does not necessarily imply declining system quality. It may reflect improved observation of a previously hidden problem. Conversely, a declining number of open defects may arise from narrower tests, reduced reporting, or premature closure rather than genuine improvement. Risk trends should separate the latent underlying condition from the detection process and the closure criteria.

An integrated control loop therefore records what was discovered, how the model of risk changed, what design action followed, and what independent evidence demonstrates improvement. The most useful risk metric is tied to future mission outcomes and decision quality, not simply to the visual appearance of a register.

## Worked Northstar project example

A firmware supplier requests a communication timeout increase from 200 ms to 500 ms. Software reports improved connectivity, but safety analysis assumes a 300 ms maximum for a certain degraded-mode transition. The proposed change could violate a critical interface contract. The correct sequence is impact analysis, alternative timeout policies, engineering and safety disposition, synchronized interface artifacts, revised tests, and configuration release. A successful nominal communications test does not validate the safety argument.

## Risk exposure across interfaces and time

Many project risks are *coupled*. A late vehicle supplier pushes integration into a different test-facility window; that creates overtime, compresses software regression testing, and increases the probability of discovering safety defects near acceptance. A register containing independent rows for supplier delay, test access and software overtime may double count some costs while also missing the shared trigger. A causal dependency diagram can reveal which interventions address more than one symptom.

Not every risk should be quantified as probability × impact. The multiplication may be useful for prioritization under consistent assumptions, but it often erases threshold effects. A ten-day delay before a facility closure might be vastly more costly than a nine-day delay; the expected value alone might hide a low-probability high-consequence event. Include credible worst cases, trigger dates and the owner's ability to act. Risks affecting human safety need appropriate specialist assurance beyond a generic financial register.

**Worked change impact.** Increasing a communications timeout from 200 ms to 500 ms changes behavior by 300 ms. If an approved safety response requires a transition no later than 300 ms under a defined condition, a 500-ms timeout may invalidate that claim. The correct response is not to average the two time constants. Identify whether the contractual condition applies to the same event, test a bounded alternative, and seek the appropriate technical disposition. If approved, update interface definitions, code, regression tests, operator documents, evidence provenance and cost/schedule baselines as required.

A robust change log distinguishes **authorization**, **implementation**, **verification**, and **closure**. The four may occur on different dates with different decision makers. This makes downstream audits possible when a later failure is traced to a particular release.

## Boundary of the method

Probability multiplied by impact is a rough screening aid, not a complete decision rule. Tail severity, time dependence, and correlated failures can dominate a simple score.

## Retrieval questions and explained answers

1. **Question:** When does a risk become an issue?
   **Explanation:** When the uncertain event has occurred or the adverse condition is now observed.
2. **Question:** Can a change board close a risk by approving a patch?
   **Explanation:** Only if closure criteria and effectiveness evidence are met; approval alone is not verification.
3. **Question:** Why preserve configuration versions in test evidence?
   **Explanation:** A pass on one build may not support claims about a materially different build.

## Put this into practice

Work through [Lab 8: The Timeout Change Board](../labs/lab-08-risk-change-and-quality.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 8 primer](../../P0-text/lessons/645-667-w08.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.

## Step 03 integrated reference — one technical change, multiple control systems

A change to a safety-relevant interface can affect requirements, failure modes, cost, schedule, supplier obligations and verification evidence at the same time. The management task is to preserve a **causal impact record** across those objects. NS-B1's emergency-status allocation is 2.5 seconds; suppose a supplier proposes a gateway revision that increases network latency by 0.3 seconds. Under a deterministic allocated-budget model, the existing 1.65-second nominal allocation becomes 1.95 seconds and leaves 0.55 seconds of allocation margin. That arithmetic does not establish compliance at the tail of a real latency distribution.

### Change-control sequence

1. Record the exact proposed interface value and affected configuration.
2. Recompute the technical budget and identify operating conditions where the assumption may fail.
3. Trace to NS-R-02 and NS-R-04, hazard controls, and any stale procedures or evidence.
4. Identify affected WBS accounts (gateway, software, verification), schedule dependencies, and vendor commitments.
5. Present options, residual risks and authority separately; approve the technical and financial decisions through their proper boards.
6. Rebaseline only the approved objects and preserve the original values for future comparison.

There is an important distinction between **risk** (an uncertain future event), an **issue** (a condition already observed), and **change** (a proposed adjustment to a controlled baseline). A supplier delay that has already happened is no longer merely a prospective probability. The remaining duration and secondary rework uncertainty still require forecasts, but past variance cannot be erased by moving it back into the risk register.

### Quantify the mitigation decision

Using NS-M1's fictional supplier event, baseline probability 0.25 and incremental cost $0.4M imply $0.10M expected cost exposure. An intervention costing $0.03M that reduces probability to 0.10 yields residual exposure $0.04M. Gross reduction is $0.06M and net expected reduction $0.03M, conditional on the stated model. If the intervention causes a one-week acceptance-test delay or raises safety risk, those consequences must be examined separately. Also examine whether interface-rework event costs overlap with supplier rework, to avoid double counting.

### Quality control is not configuration control

Quality assurance evaluates whether the agreed process can produce credible results; quality control inspects outputs against acceptance criteria. Configuration management identifies which revision an observed result applies to. A valid test performed on NS-B0 may be a well-executed test yet insufficient evidence for NS-B1. Quality and configuration checks jointly prevent “green-but-stale” evidence.

**Practice with answer.** A revised gateway reduces unit price but requires repeating an environmental qualification. Can the cost board authorize it solely from the price delta? **Answer:** no; the total change includes technical acceptance, configuration-specific evidence, qualification cost, schedule and delegated approvals. Prepare a consolidated change package and name any open conditions rather than marking them resolved.

**Reference:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) discusses configuration management, risk and product verification as coordinated engineering processes.
