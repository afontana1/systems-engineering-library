# Chapter 10 — Verification planning and evidence are different objects

*Book III: Introduction to Model-Based Systems Engineering · Week 10 — Verification and validation modeling, configurations, events, and coverage*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 10](../labs/lab-10-verification-and-validation-modeling-configur.md) before attempting [the assessed Week 10 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w10.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **verification and validation modeling, configurations, events, and coverage** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A verification model should tell who will prove which requirement, using which method, on which configuration, in which environment and using what acceptance condition. Validation asks whether the operational need is met, which may require different participants and scenarios. Configuration, date and procedure version are essential evidence attributes; a green test badge without them is not portable knowledge.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Verification planning is a design activity because the choice of evidence constrains architecture and required access points.

### Distinguishing related ideas

A 'verifies' relation may connect a requirement to a proposed test, but only executed, configuration-specific results support a compliance claim.

### Interpretation and boundary conditions

If a safety requirement cannot be observed during an intended test, the model should expose an instrumentation or testability gap before integration.

## Deeper theory: verification architecture links claims to credible evidence

### A verification relation is not a passing test

Requirements and verification evidence occupy different logical categories. A requirement states an obligation; a test case specifies a planned observation; a test record reports what happened under a particular configuration; and an acceptance judgment interprets that record against the obligation. A model edge labeled *verified by* may connect a requirement to a test definition, but it cannot substitute for the dated result, calibration status, deviations, and authorized conclusion. This distinction becomes critical when a model repository automatically generates optimistic dashboards.

A useful assurance chain identifies an objective, its decision threshold, the measurement or analytical method, the applicable configuration, the observed result, and any inference limits. If a 200 ms command-latency requirement is verified on a low-load software simulator, the evidence supports a narrower statement than compliance on the deployed wireless network under peak operational load. The test may be useful for early defect discovery while remaining insufficient for final acceptance.

### Coverage is a graph property; sufficiency is an argument

Coverage queries can identify requirements with no planned verification, tests that trace to no requirement, and design elements without an associated evidence pathway. These are valuable structural checks. But a connected graph can still be wrong. A requirement may be linked to an irrelevant test, a test may use a nonrepresentative environment, or the pass criterion may silently relax the requirement. Sufficiency requires judging method fidelity, uncertainty, independence, and whether the sampled conditions span credible failure modes.

For a multi-mode system, coverage should account for combinations: operating modes, environmental ranges, faults, interfaces, user populations, and lifecycle states. Exhaustively testing their Cartesian product is usually infeasible. Selection then becomes risk-informed: which combinations expose distinct mechanisms, and what analytical argument supports extrapolation to untested cases? A minimal test suite is not automatically efficient if it leaves important mechanisms unchallenged.

### Evidence confidence depends on the observation process

Repeated passing observations are informative only under a model of how tests were selected and how failures would be observed. If a mission success probability p is estimated from independent, identically distributed trials, observing n successes with no failures has probability `p^n`. Under those assumptions, a one-sided 95% lower confidence bound after n successes is `0.05^(1/n)`. Thus even 100 clean trials support a lower bound of only about 97%, not 99.99%. More importantly, the calculation is invalid if runs share an undetected common cause, test selection is biased, or the system changes between trials.

Simulation, analysis, inspection, and physical testing may produce overlapping evidence; they should not be counted as independent merely because different reports exist. A simulation calibrated to the same physical tests used for validation shares information with those tests. Confidence grows when evidence sources probe different mechanisms and their dependencies are understood.

### Change invalidates evidence selectively, not universally

A software patch may leave enclosure vibration evidence intact while invalidating response-time and fault-recovery evidence. This is why evidence should be tied to assumptions and affected configuration elements, not to a single whole-system “passed” badge. A change-impact query identifies candidate evidence that might no longer apply; a qualified reviewer determines whether each result remains valid, requires analytical justification, or must be repeated.

The engineering objective is a defensible argument that the current system satisfies its obligations under stated conditions. A model can make the argument reconstructable and expose missing links, but it cannot replace the empirical or analytical content on which acceptance depends.

## Worked Northstar example

R-12 requires 3-second acknowledgement. An automated test on simulator build 0.9 has 28 successful trials of 30. Mark the requirement NOT VERIFIED under a strict all-trials acceptance rule; a test result from build 0.9 cannot verify build 1.0 without justified applicability.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Counting test cases is not verification coverage; tests may be obsolete, unexecuted or inapplicable to the released configuration.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 10: Verification planning and evidence are different objects](../labs/lab-10-verification-and-validation-modeling-configur.md), you will: Audit five requirements against test definitions, execution logs, configurations and validity windows. Classify each as verified, unresolved, failed or evidence-inapplicable. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 10 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](09-candidate-physical-architectures-model-based-.md) and leads toward [next chapter](11-model-quality-queries-reports-change-impact-g.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w10.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: model verification cases and evidence separately

### Five objects that should not be conflated

A requirement specifies an obligation; a verification case specifies how it might be assessed; a procedure gives the repeatable execution; an execution record documents what was observed; and an acceptance decision interprets the result for a particular release. A link between requirement and verification case establishes planned coverage, **not** successful verification. Model repositories need types for each object and a revision context that keeps the records from becoming an undifferentiated list of PASS labels.

Use the NS-MB3 synthetic evidence register as an example:

| Requirement | Recorded status | Correct interpretation |
|---|---|---|
| `REQ-01`, authorization | Current PASS fixture | Linked illustrative support; physical behavior not demonstrated |
| `REQ-02`, ideal capacity | Current PASS arithmetic | Analytical necessary bound only |
| `REQ-03`, telemetry freshness | PASS for revision 1; requirement at revision 2 | **Stale**: current requirement unsupported |
| `REQ-04`, nominal latency | Current PASS budget | Nominal serial-path calculation; degraded case not covered |
| `REQ-05`, shift energy | Current PASS arithmetic | Simplified energy conservation; uncertain inputs |
| `REQ-06`, duplicate-token rejection | Planned only | No observed passing result |

The checker identifies four current passing *fixtures*, one stale test and one without a passing result. It does not claim that any field tests have occurred. Even if all six were labeled PASS, the source and method metadata would matter: an analytical bound cannot be relabeled as a qualification test, and an inspected software artifact does not prove real-time control behavior.

### Make release applicability an explicit predicate

For a test execution \(e\) and requirement \(r\), define a basic currency predicate

\[
C(e,r,b)=\bigl[e.\mathrm{requirementID}=r.\mathrm{id}\bigr]
\land\bigl[e.\mathrm{requirementRev}=r.\mathrm{rev}\bigr]
\land\bigl[e.\mathrm{baseline}=b\bigr].
\]

Evidence is potentially relevant only if the predicate holds. It still needs a credible procedure, relevant operating scenario, measurement quality, passed acceptance criteria, and independent authorization where required. Applying `C` to the case excludes `TEST-03` from current support. It also makes it clear why retaining the historical test is useful: auditability is not the same as current applicability.

### Practical review of gaps

For each uncovered requirement, choose a disposition: new test, justified reuse by equivalence, change to the requirement, documented waiver with authority, or release hold. A method should be chosen from analysis, inspection, demonstration and test according to the nature of the claim, without treating a method name as proof of adequacy. For the duplicate-command claim, a concurrent-retry test and evidence of atomic enforcement are more persuasive than screenshots of a nominal sequence diagram.

**Exercise with answer.** A team moves a PASS record for `REQ-03@1` into the folder for baseline `NS-MB3.1` and changes its filename. Does this fix the gap? No. The record still documents an earlier requirement revision. A controlled equivalence rationale, with reviewer sign-off, or a new validated execution is required. Filesystem location cannot change what was tested.
