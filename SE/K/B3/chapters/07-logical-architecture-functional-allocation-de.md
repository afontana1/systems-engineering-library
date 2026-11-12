# Chapter 7 — Function allocation is a hypothesis

*Book III: Introduction to Model-Based Systems Engineering · Week 7 — Logical architecture, functional allocation, derived requirements, and consistency*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 7](../labs/lab-07-logical-architecture-functional-allocation-de.md) before attempting [the assessed Week 7 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w07.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **logical architecture, functional allocation, derived requirements, and consistency** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Logical architecture identifies what must be accomplished without prematurely committing to a deployment device. Allocation maps functions to responsible components and exposes coupling, gaps and derived obligations. Distinguish necessary functions from candidate components: “check rider eligibility” may move from vehicle to cloud without changing the operational mission, but that change alters network dependence and privacy risk.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Allocating logical functions to physical or software elements is a design hypothesis that creates performance and failure consequences.

### Distinguishing related ideas

Functional responsibility does not imply a one-to-one component mapping; one controller may carry several functions and a safety function may require independent redundant implementations.

### Interpretation and boundary conditions

Allocation quality is judged by feasibility, traceability, coupling and resilience, not by how tidy the resulting block diagram looks.

## Deeper theory: function allocation is a constrained graph problem

### From behavioral obligations to responsible architecture elements

A functional architecture describes transformations and externally observable services; a logical architecture assigns those obligations to candidate abstract elements without yet committing to particular purchased devices. Formally, let `F` be a set of functions and `L` a set of logical elements, with allocation relation `A ⊆ F × L`. A row with no element may indicate missing responsibility. A function allocated to multiple elements may indicate redundancy, decomposition, or ambiguity. Counting allocation links alone does not establish completeness: the model must state which element has decision authority and how a shared obligation is coordinated.

The graph also contains flows among functions. If functions `f1` and `f2` exchange a safety-critical state signal and are allocated to different elements, that flow becomes a candidate logical interface. The interface is not generated merely because a drawing has an edge: it requires producer and consumer responsibilities, message meaning, units, time expectations, failure behavior, and ownership. A functional flow that crosses a distributed boundary incurs latency and partial-failure concerns that may be absent when the functions share a local control element.

### Allocation changes dependability and performance

Consider Northstar's `Authorize boarding` and `Monitor motion state` functions. Allocating both to one controller may reduce communication delay, but a controller fault can remove both capabilities simultaneously. Allocating them to independent elements may create useful fault containment, but only if power, data paths, software dependencies, and diagnostic authority are adequately separated. The allocation problem therefore has several simultaneous objectives: minimize critical communication, preserve independence of important safeguards, fit capacity constraints, support maintainability, and retain understandable responsibility. Optimizing any single objective can damage the others.

A simple capacity constraint might require `Σ_f demand(f) x(f,l) ≤ capacity(l)` for each logical element `l`, where `x(f,l)` indicates assignment. But real functions vary by operating mode and demand burst; average processor load cannot certify a worst-case response deadline. Interface timing should be analyzed along end-to-end paths: computation, queueing, transmission, retries, and actuation. When two functions compete for a resource, their performance budgets are coupled rather than independent rows in a spreadsheet.

### Completeness requires multiple interpretations of the model

One view can show a fully allocated function hierarchy while a scenario reveals that no element owns recovery after loss of the dispatch network. Conversely, a clean logical structure may contain an untraceable function introduced solely to match a vendor's product boundary. Coverage must be checked in both directions: each stakeholder outcome traces through required behavior to responsible elements, and each element's major responsibilities have justified upstream needs. This is not an argument for forbidding architecture innovation; emergent responsibilities may be legitimate but need explicit rationale and validation.

Allocation is a hypothesis because the logical decomposition will be challenged by physical design, tests, security analysis, and operations. Treat each significant allocation as a decision with alternatives, assumptions, expected interactions, and failure conditions. A model is valuable when a changed mission requirement makes affected elements and interfaces discoverable and when an integration failure can be traced back to a responsible design choice. The goal is not a perfectly colored matrix; it is an architecture whose responsibilities survive adverse scenarios.

## Worked Northstar example

Allocate authenticate, plan route, assign vehicle, record pickup and manage exception to Dispatch, Gateway, Vehicle and Operator Console. Now simulate loss of cloud connectivity. If both assignment and exception management live only in the cloud, the architecture may need a derived requirement for safe local fallback.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Allocating every function to the “main software” conceals ownership, information flow, failure domains and the basis of downstream test design.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 7: Function allocation is a hypothesis](../labs/lab-07-logical-architecture-functional-allocation-de.md), you will: Create a function-to-component matrix with primary and supporting responsibility. Change one allocation, update two interface obligations and document the new derived requirement. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 7 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](06-structure-interfaces-ports-connections-and-th.md) and leads toward [next chapter](08-values-units-measures-constraints-parametrics.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w07.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: logical functions, allocation and fault boundaries

### Function decomposition answers 'what must happen?'

Northstar's essential logical functions are `AUTHORIZE`, `PLAN`, `REPORT_POSITION`, `ISSUE_COMMAND` and `ACTUATE`. The [controlled model](../case/model-baseline.json) allocates them to `GATE`, `FLEET`, `TELEMETRY`, `DISPATCH` and `VEHICLE`, respectively. These labels describe responsibility, not implementation packaging. A logical architecture may be adequate even if an eventual physical component combines two functions, provided its timing, authority, and failure implications are analyzed.

A defensible allocation is a mapping \(f:F\rightarrow C\) from functions to accountable components, with additional constraints on interactions. Assigning the function is necessary but insufficient: it must be possible for data and control to flow between allocated owners, their authority must not conflict, and faults must not create forbidden bypasses. The decomposition may be incomplete if a behavior such as “handle stale telemetry” cannot be assigned anywhere. This is why allocation reviews inspect abnormal scenarios, not only component ownership.

### Allocation changes the failure structure

Compare two architectures. In a centralized implementation, the same service validates authorization and issues commands; its single failure may affect both functions. A split design assigns authorization to a dedicated `GATE`, but adds an interface whose failure could block dispatch. Which is safer cannot be answered from the number of components. A basic independent series-availability approximation for two required elements is

\[
A_{\mathrm{series}}=A_1 A_2.
\]

For illustrative values \(A_1=0.995\) and \(A_2=0.990\), this gives \(0.98505\). This is not a reliable field estimate unless independence, repair behavior, service window, and common-mode assumptions hold. If the gate can fail open, high availability may be achieved by forfeiting the safety function; availability and safety must be analyzed as distinct qualities.

### Check model consistency at three levels

First, **syntactic consistency** asks whether every allocated component exists: the JSON checker catches missing IDs. Second, **structural consistency** asks whether essential functions have responsible owners and compatible interfaces. Third, **behavioral adequacy** asks whether the resulting paths preserve safety in every modeled mode. Passing the first two does not establish the third. For example, `ISSUE_COMMAND` may be correctly allocated yet still bypass `AUTHORIZE` when an acknowledgement is lost. A review should deliberately pose this counterexample, identify the missing guard, and produce a testable model change.

**Exercise with answer.** An engineer merges `GATE` into `DISPATCH` because it eliminates one interface. What new evidence is required? At minimum, show that the authorization guard cannot be bypassed by retries or degraded modes, that failure of the shared host cannot produce unauthorized commands, and that the change preserves an independently reviewable safety claim. Fewer interfaces are not proof of lower risk.
