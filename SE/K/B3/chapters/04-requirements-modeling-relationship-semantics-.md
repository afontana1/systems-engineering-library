# Chapter 4 — Relationships need semantics, not merely arrows

*Book III: Introduction to Model-Based Systems Engineering · Week 4 — Requirements modeling, relationship semantics, and traceability*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 4](../labs/lab-04-requirements-modeling-relationship-semantics-.md) before attempting [the assessed Week 4 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w04.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **requirements modeling, relationship semantics, and traceability** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Requirements are propositions about needed system behavior or qualities. Modeling adds typed relationships: derive, refine, satisfy, allocate, verify and trace are not interchangeable. “Satisfy” links a design element to a requirement under an architecture claim; “verify” links a test case to evidence about a requirement. Neither says that a test has passed. A trace path is useful only when every edge has a justified meaning and direction.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## A deeper explanation: what a model relationship actually claims

### A model is a typed argument, not a picture

Requirements traceability is often introduced as the ability to follow lines between boxes. That description misses the important part. The lines assert **different kinds of propositions**. A relationship such as *derives from* concerns the origin and reasoning of a requirement; *satisfies* concerns a design's claimed capability; *verifies* associates a requirement with a means of checking it. Their endpoints may look similar on a diagram, but their meanings are not interchangeable. If every relationship becomes a generic “is related to,” the model loses its ability to support structured reasoning.

Take a Northstar requirement that a passenger receive an assignment acknowledgement within three seconds under specified nominal connectivity. A design element may claim to satisfy the requirement because it includes a dispatch service, a message path, and an acknowledgement interface. A test procedure may be specified to verify the requirement using timestamps at an agreed observation boundary. The procedure's existence does not imply it has run. Its execution does not imply it passed. And a passing result does not necessarily validate the passenger's experience of receiving an intelligible message. These are **separate claims at different levels**.

### The difference between derivation, allocation, satisfaction, and evidence

*Derivation* answers, “Why does this lower-level requirement exist?” If the service-level acknowledgement must reach a passenger within three seconds, a communication-subsystem requirement might reserve a portion of that budget. The derivation must document assumptions about upstream processing and downstream delivery. *Allocation* answers, “Which element is responsible for meeting this obligation?” It is a distribution of responsibility, not yet proof of capability. *Satisfaction* answers, “How is the proposed design believed to fulfill the requirement?” That belief depends on architecture and models. *Verification* answers, “What observable result could distinguish compliance from noncompliance?” Evidence comes from an execution, inspection, analysis, or demonstration performed on a specified configuration.

A useful mental model is a chain of reasons: **need → requirement → responsible design → observable criterion → result → bounded conclusion**. Every arrow should have its own rationale. If a design changes but the test result is still linked to an old configuration, the diagram may remain connected while its conclusion becomes invalid. This is why provenance and baseline identity are semantic features, not clerical metadata.

### Why transitive tracing is dangerous

Suppose A derives from B, B is allocated to component C, and test T verifies A. It does not follow that T verifies C, or that C has been validated in the operational context of B. Different relationships do not compose as freely as ordinary equality. Some chains permit useful queries—“show the lower-level requirements connected to this mission claim”—but the resulting reachability must not be mistaken for proof. The precise meaning of a chain depends on the types of its edges and the semantics of their composition.

Think of this like type checking in programming. A program can reject adding a temperature to a distance even though both are numbers; a disciplined engineering model should similarly reject treating a stakeholder need as though it were a passed test. Typed relationships let automated queries find missing coverage, but the tool cannot replace human judgment about whether a requirement is sensible or whether the selected test measures the intended phenomenon.

### Model completeness and model correctness are different

A model may be complete *according to its own schema* yet misleading. Imagine every requirement has a `satisfy` link and a `verify` link. The tool reports 100% link coverage. That is a genuine structural fact. It does not say the requirements are necessary, the design is feasible, or the tests have relevant operational conditions. A single test that merely checks whether an acknowledgement function returns `true` could be linked to dozens of requirements and inflate coverage without producing useful evidence.

Conversely, a model may contain excellent technical reasoning but be structurally incomplete: undocumented assumptions, missing interface ownership, or an unidentified test configuration can prevent independent assessment. This yields two complementary quality questions. **Structural validity:** Does the model obey its defined relationship rules? **Engineering adequacy:** Does the model represent the right phenomena accurately enough for the decision at hand? The first is often automatable. The second requires domain knowledge, empirical evidence, and explicit judgment about intended use.

### Change impact is a reasoning problem

Suppose the shuttle's acknowledgement target changes from three seconds to two seconds. A naïve graph query returns all reachable elements. A useful impact analysis goes further: it identifies the timing budget, the software and network components that consume it, the performance assumptions embedded in analysis, and the tests whose procedures or acceptance criteria have become obsolete. Some linked elements will be unaffected; some elements not directly linked may be affected through shared resources or operational assumptions. Traceability provides an index into the reasoning, not the reasoning itself.

This is the deepest reason to prefer semantic models over pretty diagrams. The model should make it possible to **explain why a conclusion was reached and what would force it to be reconsidered**. The evidence graph is not proof by visualization. It is a disciplined record of hypotheses, responsibilities, tests, results, and their limits.

## The mechanism beneath the method

Model traceability is meaningful only when relationships have typed semantics, such as derives, satisfies, allocates or verifies.

### Distinguishing related ideas

An arrow from requirement to test is not proof of verification; it may indicate an intention, a procedure, or accepted evidence, depending on its type and state.

### Interpretation and boundary conditions

A sound model separates claims, planned checks, executed observations and authoritative approvals so tools cannot silently equate them.


## Deeper theory — the logic behind a model relationship

### Models are interpreted languages

A model consists of symbols together with rules that tell us what those symbols mean. Drawing a line between a “Requirement” box and a “Component” box does not by itself tell us whether the component satisfies the requirement, owns it, was derived from it or is merely associated with it. A modeling language supplies a *metamodel*: types of permissible elements, types of permissible relationships and often constraints on the endpoints. A methodology determines how an engineering organization uses those constructs to reason and decide. Keeping these apart prevents the common mistake of equating diagram syntax with engineering validity.

Imagine a model as a typed directed graph \(G=(V,E,\tau_V,\tau_E)\). The nodes \(V\) represent things such as stakeholder needs, requirements, functions, blocks and tests. The edges \(E\) represent relations. The typing functions assign a semantic category to every node and edge. Type checking can reject an edge when its endpoints are incompatible, but it cannot establish that a well-typed statement is true. A syntactically valid “satisfy” relationship can still be a false engineering claim. Type safety is a necessary defense against meaningless combinations, not a substitute for physical evidence.

### Four relationships with different proof obligations

A *derivation* relationship says that a downstream requirement was logically or analytically obtained from an upstream requirement or constraint. It must preserve the relevant intent, units and boundary conditions. An *allocation* associates a responsibility or behavior with the element that will perform it. This is an architectural decision, not a proof that the element can succeed. A *satisfaction* assertion says a design element realizes a requirement; its credibility depends on analysis, implementation and configuration. A *verification* relationship connects a claim to a method and ultimately to evidence under stated conditions. Confusing these categories makes a model look more complete than the engineering argument it represents.

For a shuttle, take the requirement “accepted trips must be assigned within three seconds under the peak-demand operating profile.” A derived constraint might reserve 0.3 seconds for communication and 1.0 second for the allocation algorithm. Allocating the algorithm to a dispatch service indicates *where* the functionality is supposed to exist. A unit benchmark showing a 0.6-second computation supports the algorithm's performance claim under its measurement environment. It does not automatically verify the whole three-second requirement because network delay, queueing, database contention and operational configuration may differ. The model should expose rather than hide this chain of inference.

### Why composition and transitivity are dangerous

Graph reachability is not semantic proof. Suppose need N links to requirement R, R links to block B, and B links to test T. A path exists from N to T. But the links may have incompatible meanings: B may only *partially* satisfy R; T may test a previous version; N may contain a stakeholder expectation never translated into a measurable condition. A query can correctly report structural coverage while the underlying argument remains unsound. This is the distinction between **syntactic completeness**—every expected field or edge is present—and **semantic sufficiency**—the relationships together justify the claim.

A model-based assurance question should therefore be formulated with conditions: for each current high-risk requirement, identify the responsible element, its exact configuration, a relevant verification method, a result from that method and unresolved exceptions. A query result is only as trustworthy as the model's type definitions, configuration rules and data provenance. “Green” in a dashboard is a statement about a database under a query, not automatically a statement about the deployed system.

### Identity, versioning and the meaning of change

In a living model, identity matters. If “Dispatch Service” denotes one logical service across many software releases, a verification result for software build A cannot be applied to build B without a change-impact argument. Requirements likewise evolve: a later threshold may supersede an earlier one rather than simply coexist with it. An evidence graph should represent this with explicit versioned identities and valid-time or baseline relationships. Otherwise traceability becomes a history-erasing diagram in which old tests appear to prove new claims.

Change impact then becomes a typed graph traversal followed by human analysis. A changed operating condition may affect a requirement, its derived timing budget, the physical allocation and the validity of a test procedure. But not every reachable edge implies a real impact: a shared glossary term may be indirectly linked yet unaffected. Automated queries should prioritize review; they cannot replace examination of what the changed assumption means physically or organizationally.

### Model consistency versus system truth

A consistent model may be wrong about the world. Conservation equations can be dimensionally correct yet use an unrealistic passenger load. An activity model can be free of deadlocks yet omit a rare emergency mode. A requirements model can have complete trace links but express stakeholder interests poorly. The proper question is not only “Does the model obey its formal rules?” but “What evidence warrants using this abstraction to make this particular decision?” That question ties model-based engineering to validation, uncertainty quantification and assurance. Good MBSE makes claims easier to inspect and challenge; it does not make them true merely because they are stored in a model repository.

## Worked Northstar example

R-12 requires assignment acknowledgement within 3 seconds under nominal connectivity. Interface I-ACK constrains the messaging contract, design element SW-DISPATCH claims to satisfy R-12, and test T-12 checks the time across 30 trials. T-12 existing in the model says nothing about whether results pass; add execution E-12 and its observed distribution.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### Worked relationship check: a claim is not a test result

Suppose *R-12* requires dispatch acknowledgement within three seconds, and *V-12* is a verification case targeting that requirement. The relation `V-12 verifies R-12` says that the case has been defined for that purpose. Only a dated execution record on a named configuration can support a performance claim. If 29 of 30 executions satisfy the time bound, an acceptance rule of 30/30 is not met; a different statistically specified rule must have been approved before seeing the data. Do not relabel a failed case as “verified” by adding a diagram arrow. Good modeling practice is to define relationship types, allowed endpoint types and what each edge *does not* imply.

**Trace query.** For every mandatory requirement, count applicable tests with completed valid results; enumerate requirements with no such evidence. A query that checks only for outgoing `verify` links overstates coverage.

## What can go wrong—and why

A common antipattern is a complete-looking graph with “trace” links everywhere but no semantics, versions or actual evidence.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 4: Relationships need semantics, not merely arrows](../labs/lab-04-requirements-modeling-relationship-semantics-.md), you will: Build a miniature typed graph for R-12 plus accessibility and safety requirements. Deliberately introduce two incorrect relation types and identify them with queries. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 4 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](03-stakeholders-concerns-needs-context-conops-an.md) and leads toward [next chapter](05-behavior-modeling-use-cases-activities-action.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w04.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Extended worked problems and lab

Study the [worked problem workshop on typed model graph queries](../practice/graph.md), then complete the [extended laboratory](../practice/lab-graph.md). The exercises are separate from the original assessed coursework.

## Worked semantic audit: a verification link is not a verified requirement

The [MBSE semantic-modeling method guide](../../methods/mbse-semantic-modeling-handbook.md) gives a complete typed-graph example with machine-checkable JSON and a repository audit program. The key addition to this chapter is that **identity and evidence applicability are part of relationship semantics**, not administrative notes.

Imagine requirement R-ACK, component C-DISP, test T-ACK and result E-ACK. Suppose the model includes `R-ACK allocatedTo C-DISP`, `T-ACK verifies R-ACK`, and `E-ACK resultOf T-ACK`. Even if result E-ACK is marked passed, a model baseline `NS-2.3` must not automatically inherit evidence from build `NS-2.2`.

Define current evidence as the existence of a relevant test and accepted result tied to the current build and scenario:

\[
\exists e,t:\operatorname{targets}(t,r)\land\operatorname{producedBy}(e,t)\land\operatorname{accepted}(e)\land\operatorname{build}(e)=b.
\]

This is an illustrative quality rule, not a universal formal proof obligation from the SysML standard. An authorized equivalence argument may permit evidence reuse, but the argument must be explicit and reviewed.

**Reproduce the finding:** Run the [audit program](../../methods/code/model_trace_audit.py) on [stale](../../methods/data/model-stale.json) and [corrected](../../methods/data/model-corrected.json) model baselines. The first identifies a stale timing test and a missing energy result; the second identifies two structurally covered requirements. Neither report alone proves real-world compliance. Separate the graph's structural checks from scientific evaluation of the evidence.

## Phase 5 technical reading: Tool-checkable requirement relationship semantics

In a controlled SysML v2 workflow, represent stable identifiers and explicit relation meanings rather than counting arrows. Campus Mobility's `REQ-DOOR` is derived from `NEED-ACCESS`, allocated to the door controller, related to `H-DOOR`, and tested by `TEST-DOOR-01`. The documentary crosswalk checks the consistency of those identities across a requirement table, interface definitions and evidence. A separate, conformant language tool must parse/resolve the SysML source: the teaching crosswalk is not a SysML parser. Review the [SysML v2 modeling and traceability chapter](../../methods/sysml-v2-modeling-and-traceability.md) and produce a diagnostics record tied to the tool and model versions.

## Step 03 integrated reference: traceability is a typed argument

### A graph edge must say exactly what it asserts

Model relations are not decorative arrows. `derive` relates a requirement to a motivating need; `allocate` identifies responsibility; `satisfy` asserts an architectural candidate is intended to meet a requirement; `verify` relates a test method or case to a requirement. The evidence *result* belongs to a particular execution, revision, configuration, scenario and measurement procedure. Even a perfectly populated trace matrix can contain an invalid technical assertion. In NS-MB3 all six requirements have named components and tests; that does **not** mean all six are verified.

Represent the trace graph as \(G=(V,E,\tau_V,\tau_E)\), where \(\tau_V\) and \(\tau_E\) give vertex and relationship types. A checker may enforce `test → requirement` but forbid `test → stakeholder` when the latter relation is not part of its declared metamodel. Referential integrity is necessary; it does not establish semantics. A test called `TEST-03` has a reference to `REQ-03`; its execution states requirement revision 1, while the current requirement is revision 2. That means the result is **stale**, not current evidence, regardless of the old PASS label.

### Calculate coverage without concealing failures

Let \(R\) denote requirements, \(A\) those with an allocated component, \(T\) those with linked tests, and \(E\) those with current passing fixtures. A graph audit of the synthetic NS-MB3 JSON yields

\[
|R|=6,\quad |A|=6,\quad |T|=6,\quad |E|=4.
\]

The first two structural coverage ratios are 100%, whereas the current linked-fixture ratio is \(4/6=66.7\%\). The denominator is deliberately explicit: a weak metric can appear strong by counting all historical results regardless of revision or by excluding planned tests from the denominator. The four passing fixtures are still *illustrations*; they are not observed physical-system evidence. The model's `TEST-06` is merely planned and `TEST-03` is stale. These cases should be represented separately, not hidden under one “incomplete” label.

### Preserve trace meaning through a change

When `REQ-03` changes, first update its revision and justification, then find dependent interfaces, measures, tests and stakeholder views. Determine whether each relation remains valid. Existing PASS results stay immutable as historical records, but cannot be promoted to support the revised requirement without an applicability argument or a new test. A critical review should follow one complete chain and ask where evidence quality or semantics could fail, rather than treating trace density as proof of system correctness.

### Practice with answer

**Exercise.** A reviewer sees six requirement-to-test links and declares 100% verification. Identify two errors. **Answer:** (1) Test assignment or test-case existence is not executed evidence; (2) both requirement revision and configuration must match the decision. The case has only four current passing *synthetic fixtures*, and independent operational validation remains absent. Run `python3 ../tools/step03_book3_model_check.py` from the book's `chapters/` directory or use the repository-root invocation in [the case README](../case/INDEX.html).
