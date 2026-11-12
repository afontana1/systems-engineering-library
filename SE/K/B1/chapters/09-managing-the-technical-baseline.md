# Chapter 9 — Technical Management Keeps Engineering Claims Coherent

*EN.645.662 · Week 9. Continues the concept decisions of [Chapter 8](08-trade-studies-and-sensitivity.md); then undertake [Hypothetical Lab 9](../labs/lab-09-technical-management.md).*

## The concept changed, but the project kept using the old answer

The Northstar architecture team decides that its dispatch service must reject vehicle-readiness reports older than five seconds. The requirement is revised; software updates its validation rule; an interface supplier still publishes every eight seconds; the test team runs an older scenario that expects a ten-second threshold. Every group can show a document with a green status. Taken together, however, the documents describe different systems.

This is the problem of **technical management**. Engineering work evolves through multiple people, products, tests, decisions, and revisions. The management system must preserve the relationships among them. Technical planning, risk management, configuration management, data management, and technical performance measurement are not administrative accessories to design. They are mechanisms that allow the design and its supporting evidence to remain valid over time.

## 9.1 A SEMP is an operating agreement

A Systems Engineering Management Plan (SEMP) should answer practical questions: who owns requirements, who decides architecture alternatives, how interfaces become controlled, what baselines exist, which reviews permit transitions, how tests establish evidence, how changes propagate, and who can accept residual risks. Avoid pasting a generic lifecycle essay into the SEMP. A useful plan states what the team will actually do, when, with which artifacts and decision rights.

For Northstar, a lightweight technical plan might define: (a) one controlled source of truth for each requirement and interface, (b) weekly trace audits, (c) a change board for safety-relevant modifications, (d) an experiment review before using simulation results in a recommendation, and (e) baseline reviews before integrating new constituents. Each rule should have a named owner and a reason tied to the project's risks.

A **product breakdown structure** (PBS) describes the product or solution elements to be realized; a **work breakdown structure** (WBS) organizes the work to be funded and controlled. The WBS must include activities such as interface qualification, training, and technical management that are not physical components in the PBS. Mapping PBS items to WBS work packages is useful; declaring them identical is generally wrong.

## The mechanism beneath the method

Technical management maintains consistency between changing claims about scope, cost, configuration, risk, performance and verification evidence.

### Distinguishing related ideas

A baseline is not a record that engineering has stopped; it is a versioned agreement that allows change impacts to be understood.

### Interpretation and boundary conditions

A software revision that changes stop-detection timing can invalidate earlier energy estimates or test results even if their numerical values did not change.

## 9.2 Risk is a causal claim, not a colored cell

Distinguish four records. A **risk** describes a possible future event with uncertain consequence. An **issue** is a condition that already exists. An **assumption** is a proposition accepted provisionally and requiring confirmation. An **opportunity** is a potentially beneficial uncertainty. The team can damage its reasoning by treating “the telemetry interface uses an inconsistent clock” (current issue) as if it were merely a low-probability risk.

Write a risk in cause–event–consequence form: *Given intermittent backhaul connectivity and an unproven fallback protocol, there is a possibility that dispatch decisions will be delayed or duplicated, resulting in passenger disruption and potentially unsafe coordination.* This formulation identifies a causal mechanism, a future event, and effects. Mitigations can then target the mechanism: interface contract tests, duplicate suppression, a clearly defined degraded state, and monitored retry policy.

Probability × impact scores may help triage a register, but treating ordinal categories (1–5) as accurate numerical probabilities is a mistake. Risks with different failure mechanisms can share the same color. Critical safety consequences require suitable controls and authorities regardless of their location in a simplistic matrix.

## 9.3 Configuration management preserves propositions across change

A **configuration item** is a controlled element whose identity and version matter to the system and its assurance argument. The current requirement set, functional model, interface schemas, architecture alternatives, test procedures, software configuration, simulation assumptions, and evidence records may all require control.

There are four recurring activities: **identification** (what is controlled), **change control** (who may alter it and why), **status accounting** (what revision and disposition exist), and **audit** (whether the authoritative configuration matches its records and obligations). The important outcome is reproducibility. A reviewer should be able to reconstruct the exact model and assumptions that led to a technical decision.

Suppose requirement `R-TEL-03` changes from ten-second data freshness to five seconds. The change impact is not limited to editing a sentence. The downstream interface contract, telemetry schedule, function budget, test thresholds, simulation settings, hazard controls, and previous evidence claims all require a disposition. Some tests remain relevant; others must be repeated. The change request should identify each affected artifact and provide explicit evidence for closure.

## 9.4 Technical performance measures anticipate problems

A **technical performance measure** (TPM) is a planned metric whose trend helps decide whether a technical target is likely to be met. The team might track the 95th percentile of dispatch notification latency under a controlled load profile, the fraction of assignments rejected for stale telemetry, or battery reserve under a representative duty cycle. A useful TPM defines the measurement method, configuration, expected trajectory, threshold, review trigger, and decision owner.

Consider a proposed target that the 95th-percentile notification latency be no more than eight seconds. In three successive prototype builds, the observed p95 values under the *same* controlled workload are 6.2, 7.1, and 8.4 seconds. The latest build breaches the target; the worsening trend demands investigation even if the average latency remains acceptable. But if the third run used a higher workload or revised instrumentation, the comparison is confounded. Technical management requires both a measure and its context.

A dashboard should contain **decision rules** rather than decorative charts: if p95 exceeds the trigger, identify the owner, hold the relevant baseline gate, investigate queue buildup, and create an evidence-backed corrective action. Metrics without consequences produce reporting theater.

## Deeper theory: technical baselines as a graph of versioned claims

### A baseline fixes meaning, not merely files

A technical baseline is a controlled set of propositions about what the system is expected to do, how it is designed to do it, and what evidence supports those claims. A requirements document, interface definition, model element, test procedure, software build, and acceptance result have different meanings, but all can participate in the same engineering argument. The baseline becomes incoherent when these objects refer to incompatible versions. Calling a folder “approved” does not establish that a completed test was performed against the configuration now proposed for release.

Treat the baseline as a directed dependency graph. Nodes represent versioned artifacts or claims; edges represent relations such as *derived from*, *allocated to*, *implements*, *verified by*, and *depends on*. A change to the dispatch request timeout should trigger consideration of reachable nodes: response-time requirements, API contracts, retry policies, test data, service-level measures, and possibly hazard controls. Reachability does not prove that every reachable item must change; it identifies where an engineer must evaluate consequences. Conversely, an absent trace edge is not proof that an effect is absent. Informal coupling and shared resources also require investigation.

### Change control is a consistency-preserving transaction

The analogy with database transactions is useful. An authorized change begins with a stated intent and a known configuration; evaluates dependent objects; produces a candidate consistent state; checks evidence; and finally commits an approved new baseline. If the process updates a requirement but leaves the corresponding test's pass criterion untouched, it has committed a partial transaction. The resulting repository may be internally readable yet technically contradictory.

A configuration identifier should therefore refer to more than a document revision. For software-intensive systems it may need a build hash, configuration parameters, deployed interface versions, hardware variant, calibration state, and operating assumptions. A result saying “the system passed” without this information is not reproducible. Neither configuration control nor a digital thread creates correctness automatically: each preserves the ability to inspect the *claims actually made* and the artifacts against which they were tested.

### Performance measures are indicators with prediction error

A technical performance measure, or TPM, tracks a characteristic likely to affect mission success before acceptance testing is complete. Suppose dispatch latency is forecast to be 180 ms against a 250 ms threshold. The 70 ms difference is not automatically a reliable margin: measurement error, future load, software growth, and integration overhead may erode it. A realistic forecast should represent a distribution or scenario band rather than a single extrapolated line. If `L` denotes eventual latency, the decision-relevant quantity may be `P(L <= 250 ms | current evidence)`, not simply the current average latency.

Thresholds also create incentives. A team measured only on average latency can reduce its reported mean while worsening 99th-percentile delay or dropping hard requests. A good TPM definition specifies the workload, percentile, test environment, exclusions, and change rule. It is paired with a leading indicator when possible, such as queue occupancy or retry count, and with a system-level outcome that prevents local optimization from hiding service degradation.

### Risk, change, and evidence form a feedback loop

A risk register is a set of time-dependent causal hypotheses, not a static collection of colors. Proposed mitigations alter design or operating controls; those changes alter the baseline; verification produces new evidence about residual risk. An unresolved hazard must not disappear merely because a new mitigation action was assigned. The causal chain should be stated explicitly: initiating condition, propagation pathway, consequence, barrier, verification of the barrier, and remaining exposure.

For example, increasing retry attempts could lower transient request failures yet increase network congestion and duplicate commands during peak load. Change evaluation must recognize this feedback, revisit the workload assumptions, and ask whether the resulting baseline remains both safe and operationally acceptable. Technical management succeeds when decisions preserve coherent meaning across time, not when every individual document is perfectly formatted.

## 9.5 Worked change-impact walk-through

Northstar receives `CR-017`: reduce the allowable freshness age from ten seconds to five seconds to address a scenario discovered during safety review. The change board first asks *who authorized the proposed safety rule and what outcome it protects*. Then it examines impacts: telemetry may have to publish more frequently; communication load may increase; the dispatch contract must reject older state; tests must cover boundary ages (4.9, 5.0, 5.1 seconds under declared clock semantics); operational fallback behavior must be defined. The board may approve a staged experiment but cannot simply mark the overall architecture verified. Closure requires a controlled revised set plus evidence that the new behavior works and that the new resource demands remain acceptable.

## 9.6 Practice with explained answers

**A. Classify.** “A test found that the message timestamps are inconsistent.” **Answer:** A current issue, not merely a risk; downstream risks may arise from its consequence.

**B. Distinguish.** Does the PBS necessarily include the training work package? **Answer:** No. Training is work and potentially an enabling deliverable; the PBS and WBS serve different purposes and require mapping.

**C. Audit.** A test cites software v3 but the baseline claims software v4. **Answer:** The test does not automatically verify v4; establish change impact and whether the earlier result remains valid.

**D. Interpret.** What does a rise from p95=6.2 to 8.4 seconds prove? **Answer:** Under controlled comparable conditions it signals degraded tail performance and threshold breach, not the cause of degradation.

**E. Repair.** “Network issues: high, owner TBD.” **Answer:** Replace with a causal risk statement, assessment rationale, treatment, owner, trigger, due date, and monitoring plan.

## Read, rehearse, produce

In [Hypothetical Lab 9](../labs/lab-09-technical-management.md), audit a conflicting set of change records and technical measures. Then complete the Week 9 original `662_W09_TechnicalManagement_v1.0` deliverable: SEMP, PBS/WBS crosswalk, risk and CM records, data plan, and TPMs. Do not claim baseline coherence based only on file count.

**Next:** [Chapter 10 — Systemic failure and red teaming](10-failures-and-controls.md).


## Step 03 technical studio — link cost/schedule signals to controlled product evidence

A project baseline combines approved scope, versions, interfaces, planned work, resources, and verification obligations. Earned-value metrics answer questions about **performance against an agreed plan**; they do not by themselves tell you whether the intended system works.

Consider an illustrative review: planned value `PV=$400k`, earned value `EV=$320k`, actual cost `AC=$360k`. Then

\[
CPI=\frac{EV}{AC}=0.889,\qquad SPI=\frac{EV}{PV}=0.80.
\]

The project has earned less budgeted work than the spending and plan imply, but neither number measures the probability of a vehicle collision or the sufficiency of a verification report. Calling a test “complete” to improve earned value when its evidence is not applicable to the current configuration is a governance failure.

### Change-impact graph

Suppose NS-B1 changes the status-message schema and becomes NS-B2. At least four connections deserve review: the publisher's implementation, the console's interpretation, the interface tests, and the verification evidence for NS-R-02 and NS-R-04. The [case traceability matrix](../case/traceability.csv) demonstrates a stale item even **before** that change. An impact analysis follows typed links, not a blanket assumption that a previously green test remains valid.

### Solved management exercise

A team proposes removing NS-R-04 from the baseline because its test is stale and re-running the test delays a milestone. Would this be a legitimate schedule recovery action? **Only if** the requirement is formally reassessed against stakeholder needs and authorized by the appropriate decision authority. Deleting a requirement simply to improve an indicator changes the product claim. The original hazard and operational need still exist even if the dashboard displays fewer failed tests.

For every significant change, record the *before and after configuration*, changed obligations, affected evidence, owner, authority, and retest or justified nonimpact. This provides an auditable technical management record rather than a version label alone.

## Step 03 reference deepening — a baseline is a graph of claims with dates

A traceability row is not just a link from requirement to test; it asserts that a particular observation **supports a particular version** of a claim under specified assumptions. Consider the fictional NS-B1 case: a test record labelled NS-B0 may establish a property of the previous software and interface configuration. It does not automatically transfer to NS-B1. A proper change-impact review traverses requirement → allocated component → interface and configuration → procedure → evidence → acceptance decision.

A minimal record therefore needs requirement revision, owner, allocated element revision, procedure version, evidence location, measured result, validity interval and disposition. Failure cases include a missing reference, a current file with an old software build, an accepted test whose instrumentation calibration expired, and a signed decision that applies only to supervised use. A checker can find structural mismatches, but engineering judgment must evaluate actual representativeness and claim sufficiency.

Financial progress is related but distinct. Earned value can show more budgeted work completed while a technical baseline contains stale evidence. Conversely, a necessary safety test can be technically successful and still require a forecast revision after unplanned fixture use. Do not permit one progress indicator to overwrite the other; present cost/schedule and evidence readiness side by side at the review gate.

**Practice:** If every requirement has one evidence link but half the links point to NS-B0, what is the coverage? **Answer:** syntactic trace-link coverage may be 100%, but current acceptable evidence coverage can be much lower. Report both and preserve the change history rather than retroactively relabeling old records.
