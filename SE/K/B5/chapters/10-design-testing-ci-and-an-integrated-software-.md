# Chapter 10 — The verification chain includes build identity

*Book V: Software Systems Engineering · Week 10 — Design testing, CI, and an integrated software V&V evidence chain*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 10](../labs/lab-10-design-testing-ci-and-an-integrated-software-.md) before attempting [the assessed Week 10 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w10.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **design testing, ci, and an integrated software v&v evidence chain** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Unit tests assess local functions; integration tests assess collaboration; system tests exercise allocated requirements; acceptance and validation involve operational intent. A continuous-integration pipeline is a repeatable means to produce evidence, not itself proof of correctness. Connect requirements to tests and results with immutable build identity, environment and acceptance criteria.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Verification pipelines connect source revisions, build artifacts, tests, environments and release identities to preserve the meaning of test evidence.

### Distinguishing related ideas

A passing CI badge is a statement about a particular artifact under particular tests; it cannot certify a later build or an untested configuration.

### Interpretation and boundary conditions

Reproducibility, test-data provenance and environment parity are architectural concerns because they affect whether results can be reused.

## Worked Northstar example

Run T-ACK for build 1.2 on a simulated network and observe 29 of 30 acknowledgements under three seconds. Whether this passes depends on the approved acceptance rule. The result does not automatically qualify build 1.3 or a deployed network with different latency.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### How a green pipeline can be false reassurance

If test T-ACK executes against build `1.2` on a low-latency simulator and finds 29/30 acknowledgements under three seconds, its result is tied to that **configuration**, **environment**, **acceptance rule** and **sample**. A later build `1.3` is a different artifact; an unreviewed new runtime environment is a different condition.

Define coverage at several levels: requirements with a test design; requirements with an execution; requirements with passing, applicable evidence; and stakeholder outcomes supported by validation. These counts need not agree. A passing unit suite does not by itself establish the software system's operational readiness.

## What can go wrong—and why

A thousand passing tests can leave a critical hazard uncovered if coverage is counted without requirement and scenario semantics.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 10: The verification chain includes build identity](../labs/lab-10-design-testing-ci-and-an-integrated-software-.md), you will: Create a coverage report with five requirements, test cases, results, versions and an explicit rejected “green” release. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 10 deliverable and grading rubric.


## Graduate depth: continuous integration as a chain of supply and assurance
### A green test result is meaningful only for a particular artifact

Continuous integration can provide rapid feedback, but it does not automatically establish software correctness or deployment readiness. A defensible result identifies the exact source revision, dependency versions, compiler and build configuration, test harness, environment, inputs, and output criteria. If a successful test belongs to a different binary than the one deployed, its assurance value is sharply reduced. This is the software counterpart of configuration-specific qualification in systems engineering.

A build can be viewed as a transformation `artifact = F(source, dependencies, tools, configuration, environment)`. Reproducibility requires controlling enough of these inputs that the same intended result can be reconstructed and unexpected variation can be detected. Bit-for-bit reproducibility is powerful where achievable, but not every toolchain is deterministic; projects must document acceptable variance and verify identity through signed manifests, checksums, or other provenance mechanisms. The build chain itself becomes part of the assurance boundary, particularly when third-party packages or remote runners are involved.

### Verification layers answer different questions

Static checks can identify forbidden dependencies or certain classes of unsafe code without executing it. Unit tests can challenge local logic with narrow fixtures. Contract tests can detect interface incompatibility. Integration tests exercise cross-component state and timing, while system and operational tests examine behavior under mission-relevant environments. Security analysis and fault injection target failure modes unlikely to arise in happy-path tests. Each method has a distinct detection envelope; high line coverage says little about the severity of untested scenarios.

A risk-based test strategy can be expressed in terms of failure consequence, exposure, and uncertainty, but a numerical risk score should not conceal what is unknown. A single untested safety interlock may matter more than thousands of passing routine tests. Mutation testing and property-based tests can improve sensitivity by deliberately challenging assumptions, yet they remain bounded by the properties specified and the faults introduced. Test design must be traceable to actual system obligations rather than driven solely by whichever checks are cheapest to automate.

### Deployment changes create their own proof obligations

Suppose Northstar updates routing software while vehicles are operating. A staged rollout, feature flag, and rapid rollback may limit exposure, but rollback itself must be feasible if a data migration is irreversible. A safe release plan identifies compatibility windows, degraded-mode behavior, operational monitors, intervention authority, and a stop criterion. Monitoring does not replace predeployment verification, yet it can detect unexpected field conditions and supply evidence for future revisions.

Software supply-chain risks cut across all these layers. A malicious or compromised dependency may pass the project's own functional tests. Provenance, constrained privileges, dependency review, and signing reduce exposure but do not guarantee absence of compromise. The governing assurance argument is therefore continuous and configuration-specific: **what was built**, **what was tested**, **what threats and failures were considered**, **what was deployed**, and **what evidence will trigger rollback or re-evaluation**. CI is valuable not because everything turns green, but because it makes these questions answerable quickly and repeatedly.

## Continuity

This chapter builds from [previous chapter](09-build-the-dependability-safety-resilience-and.md) and leads toward [next chapter](11-manage-delivery-operations-maintenance-evolut.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w10.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
