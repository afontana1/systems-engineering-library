# Chapter 9 — Dependability is a claim supported by argument and evidence

*Book V: Software Systems Engineering · Week 9 — Build the dependability, safety, resilience, and supply-chain case*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 9](../labs/lab-09-build-the-dependability-safety-resilience-and.md) before attempting [the assessed Week 9 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w09.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **build the dependability, safety, resilience, and supply-chain case** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Safety, reliability, cybersecurity and supply-chain assurance interact but require different evidence. Failure mode analysis asks how a component fails and propagates; fault trees reason about combinations producing a top event; threat modeling examines adversarial paths; provenance evaluates what was built and from what. Assemble an assurance claim with an explicit operational envelope.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Dependability combines failure prevention, detection, containment, recovery and evidence under a defined operating environment.

### Distinguishing related ideas

Redundant instances do not yield independent availability when they share power, credentials, network paths or deployment mistakes.

### Interpretation and boundary conditions

Recovery exercises must reproduce realistic shared dependencies and verify that restored service has consistent state rather than merely an open port.

## Deeper theory: dependability claims require explicit failure and recovery models

### Reliability, availability, safety, and resilience measure different things

Reliability is the probability of performing a specified function without failure for a given interval and conditions. Availability concerns readiness to perform when required, often incorporating repair. Safety concerns unacceptable harm, and resilience concerns the ability to absorb, adapt to, and recover from disruption. These are related but not interchangeable. A service that quickly restarts after crashing may have high long-run availability and still fail a mission in which one interruption during boarding is unacceptable. An almost perfectly reliable service may be unsafe if its rare failure mode directly commands an uncontrolled movement.

Under a highly simplified alternating up/down model with constant failure rate `λ` and repair rate `μ`, steady-state availability is `μ/(λ+μ)`, equivalently `MTBF/(MTBF+MTTR)` when the quantities have the relevant meanings. This expression assumes particular renewal and repair conditions. It does not automatically account for planned downtime, logistic delay, shared power failures, partial service, or demand-weighted unavailability. Reporting five nines without specifying the service boundary and observation rules is a marketing statement rather than an engineering claim.

### Redundancy can create new dependencies

Two active controllers are not twice as safe simply because there are two. If the same faulty software release corrupts both, duplication offers little protection. A failover controller may require a health detector whose false positives cause disruptive switching, while false negatives leave the failed controller in command. The design must address fault coverage, switchover time, state reconciliation, and split-brain authority. A redundant system can have more complex failure modes than either constituent.

A dependability model should use a fault hypothesis: which faults are expected, how they manifest, what detects them, and which states are permitted after detection. Some faults are transient; some persist until repaired; some corrupt data invisibly. Graceful degradation means preserving a clearly bounded subset of safe service, not silently lowering standards. For Northstar, degraded operation might stop new dispatch requests while maintaining safe completion or controlled termination of already accepted trips. Whether that is acceptable depends on the ConOps and hazard analysis.

### An assurance case links claims, evidence, and assumptions

A dependability argument has at least a top-level claim, supporting subclaims, evidence, and context. For instance, “the dispatch controller tolerates a single loss of network connectivity while preventing unsafe boarding commands” may decompose into local interlock correctness, failure detection, stale-command handling, and restoration rules. Each subclaim needs matching evidence, such as requirements, independent analysis, injected-fault tests, and configuration records. Evidence for a different software build or environmental profile may not carry over.

No fixed quantity of tests establishes reliability for arbitrarily rare events. Observing zero failures in a small sample leaves considerable uncertainty, especially if tests are dependent or unrepresentative. Assurance must acknowledge known gaps and the authority that accepts residual operational risk. The purpose is not to prove that a complex system can never fail. It is to make the failure assumptions, containment mechanisms, and conditional scope of trust visible enough that an authorized decision maker can challenge them.

## Worked Northstar example

The top event “two active reservations for one vehicle window” may arise from a race condition or stale replica acceptance. Redundant servers alone will not mitigate a shared database rule defect. A database uniqueness constraint, chaos test and operator recovery procedure defend different layers.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Adding probabilities to unvalidated common-cause events can create a misleadingly precise safety number.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 9: Dependability is a claim supported by argument and evidence](../labs/lab-09-build-the-dependability-safety-resilience-and.md), you will: Construct a small hazard-and-threat case linking two failure paths to controls, tests, ownership and unresolved assumptions. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 9 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](08-specify-and-analyze-performance-networking-re.md) and leads toward [next chapter](10-design-testing-ci-and-an-integrated-software-.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w09.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Step 03 integrated reference: safety, availability and common-cause exposure

### Separate the claims before estimating them

Reliability concerns successful operation over an interval; availability concerns service being usable under a defined measurement rule; safety concerns unacceptable loss or harm; resilience concerns behavior during disruption and recovery. NS-SW5.1's availability objective is **not** a claim that vehicle motion is safe. Its SWS-08 operator fallback may help manage a software outage, but any physical-motion safety case needs independent system-level analysis and controls.

In a hypothetical 30-day window there are \(30\times24\times60=43{,}200\) minutes. A 99.9% **time-based** service availability target permits at most

\[B=(1-0.999)\times43{,}200=43.2\text{ unavailable minutes}.\]

The four synthetic [incidents](../case/incident-log.csv) total 5+7+10+14 = **36 minutes**. Remaining allowance is 7.2 minutes. This calculation assumes unavailability is measured as those incident durations, with no overlapping intervals and a fixed accounting policy. A request-based SLI would yield a different numerator and denominator. Never silently mix the two.

### Evaluate redundancy against shared failure

For two essential services whose independent interval availabilities are 0.9995 each, serial composition gives about 99.9000%. If a modeled shared-cause event with probability 0.001 can disable the entire path, the illustrative availability falls to 99.8001%. The point is not the exact synthetic percentage; it is that adding replicas on a shared deployment platform cannot eliminate platform-wide failure. A fault tree needs to represent power, identity, configuration and operator-induced common causes rather than assume every failure is independent.

### Build an assurance argument

Claim: reservation service fails visibly and does not claim success after a timeout. Subclaims: IF-01 returns an explicit failure, IF-02 prevents duplicate slot assignment, IF-03 rejects stale state, and operator fallback is correctly invoked. Supporting evidence includes transaction tests, boundary-condition tests, recovery drills and monitored operations, each bound to a build/configuration. The current recovery drill is `PLANNED`, so the corresponding argument is not closed. A model checker finding consistent IDs is not a safety case.

**Exercise.** An engineer adds a replica in the same region and claims that availability doubles. **Answer.** Availability is a probability or fraction, not an additive quantity. Derive the failure logic, include shared dependencies, and measure the service from the user boundary. Any resilience improvement requires demonstrated behavior under the faults it purports to tolerate.
