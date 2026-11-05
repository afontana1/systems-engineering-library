# Chapter 1 — Software engineering must preserve system intent

*Book V: Software Systems Engineering · Week 1 — Define the software systems engineering role and establish the baseline*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 1](../labs/lab-01-define-the-software-systems-engineering-role-.md) before attempting [the assessed Week 1 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w01.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **define the software systems engineering role and establish the baseline** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Software systems engineering bridges operational needs, allocated system requirements, deployable capabilities and credible evidence. A feature working in isolation does not establish mission performance. Define the software system boundary, external dependencies, authorities and configuration before selecting languages or cloud products. Treat risk and assurance as lifecycle responsibilities, not a final release ritual.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Software is a subsystem with responsibilities allocated by the whole-system architecture, not an isolated feature list.

### Distinguishing related ideas

System success may depend on sensors, operators and external services that software can observe but cannot control.

### Interpretation and boundary conditions

Software requirements must therefore distinguish controllable outputs, required external assumptions and degraded behavior when assumptions fail.

## Worked Northstar example

The shuttle operator must prevent double vehicle assignment. A unit test of the booking method is necessary but not sufficient: concurrency, message loss and restart behavior can violate the system-level invariant.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

A software roadmap that tracks story points but not system constraints can be on schedule and still unsafe or unusable.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 1: Software engineering must preserve system intent](../labs/lab-01-define-the-software-systems-engineering-role-.md), you will: Write a software assurance charter mapping three mission claims to allocated functions, quality measures and evidence owners. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 1 deliverable and grading rubric.


## Deeper theory: software systems engineering as system-level evidence orchestration

### Software behavior spans an engineered and a physical world

Software systems engineering connects implementation decisions to mission effects, physical constraints, organizational authority, and service operations. A control algorithm does not act on abstract state alone: sensor measurements have noise and latency, actuators have dynamics, users make unexpected choices, and networks fail partially. The engineering obligation is to state how software-visible inputs relate to physical quantities and how software outputs become safe physical effects. Correct source code is necessary for many claims, but cannot by itself establish vehicle safety or mission value.

Consider a location function returning latitude, longitude, and a nominal accuracy. If downstream code treats every returned coordinate as reliable, the software may be logically deterministic yet unsafe. A system-level contract needs reference frame, timestamp, uncertainty interpretation, integrity state, and behavior when observations become invalid. The same principle applies to occupancy sensors, charging commands, and access authorization. A typed data field is not a meaningful system interface unless its physical and operational semantics are explicit.

### Assurance follows a chain of conditional inference

A system claim such as “the vehicle stops before a protected boundary” may depend on perception coverage, estimator error bounds, decision latency, network failure handling, actuator response, tire-road interaction, and maintenance condition. A simple conservative stopping-distance model is `d_stop = v τ + v²/(2a)`, where `v` is speed, `τ` is combined detection-to-braking delay, and `a` is positive achievable deceleration under the modeled condition. At 4 m/s, 0.5 s of delay, and 2 m/s² deceleration, the calculated distance is `2 + 4 = 6` m. That is not an acceptance result: the example omits gradient, uncertainty, obstacle motion, brake variability, and safety reserve.

Software requirements and tests must therefore refer to the system operating domain. Unit tests can prove algorithm behavior for supplied inputs, integration tests can expose interface and scheduling errors, and vehicle tests can observe coupled behavior. Their conclusions have different scopes. A “passed unit test” should not silently inherit the authority of a system validation claim. Build identity, configuration, and test context connect the evidence layers.

### Feedback between operations and design is part of engineering

Field telemetry can reveal rare interactions missing from pre-release models, but operational measurements are not automatically unbiased. A service log may exclude failed sessions that never generated a transaction ID. A crash report may lack the environmental state required for root-cause analysis. Instrumentation design must anticipate what failures need to be distinguishable, what personal information should be minimized, and what operating restrictions apply to evidence collection. A data-retention policy can be a safety and privacy decision at the same time.

The software systems engineer's distinctive contribution is maintaining a coherent line from stakeholder outcome through architecture, data meaning, code configuration, verification evidence, and operational learning. This role is not equivalent to managing programmers or choosing tools. Its limit is shared authority: safety, human factors, hardware, operations, and security experts must challenge the assumptions that software specialists cannot establish independently.

## Continuity

This chapter builds from the earlier Foundation books and leads toward [next chapter](02-model-software-allocations-interfaces-and-the.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w01.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
