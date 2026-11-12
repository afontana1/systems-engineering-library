# Chapter 2 — Choosing a language is not choosing a method

*Book III: Introduction to Model-Based Systems Engineering · Week 2 — Modeling plan, methodology, language, tool, and repository architecture*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 2](../labs/lab-02-modeling-plan-methodology-language-tool-and-r.md) before attempting [the assessed Week 2 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w02.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **modeling plan, methodology, language, tool, and repository architecture** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A modeling language supplies vocabulary and semantics; a method supplies the order and rules for using it; a tool stores and manipulates instances. Governance establishes authority. Separate all four before designing the repository. A small canonical model can be more valuable than a large diagram collection when the team can regenerate views from one maintained source. Versioning and package ownership must be decided before two teams edit the same concept.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Notation is not semantics

A modeling language provides symbols and relationships; an engineering method establishes why those relationships should exist, how they are checked, and what decisions they support. A block labeled “Vehicle” and an arrow labeled “controls” may be legal notation while remaining ambiguous about authority, direction, timing, and failure behavior. **Well-formed syntax is not sufficient for meaningful modeling.** The reader needs a definition of each element type and each relation's permitted interpretation.

A model is useful when it rules out at least some incorrect interpretations or configurations. A requirement-to-component allocation, for example, should identify responsibility for satisfaction, not merely show two boxes in proximity. A model that connects every requirement to every component has near-perfect visual coverage but little discriminating power. Explicit modeling conventions—including identities, units, ownership, consistency constraints, and expected queries—turn notation into a shared technical language. Without those conventions, diagrams are attractive pictures that different teams can interpret differently.

## Worked Northstar example

Create packages for Mission, Requirements, Behavior, Architecture, Analysis and Verification. Give requirement R-07 a stable identifier and a single definition. A state view and an interface view may both reference R-07; neither may silently redefine it. A repository review checks that branch merge preserves that identity.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

A tool may permit a relation that the chosen modeling method prohibits; syntactic validity therefore cannot establish method compliance.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 2: Choosing a language is not choosing a method](../labs/lab-02-modeling-plan-methodology-language-tool-and-r.md), you will: Design a repository for two fictional teams with conflicting edits to R-07. Define ownership, merge protocol, baseline tag, review query and restore drill. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 2 deliverable and grading rubric.


## Deeper theory: modeling method, language, and tool as independent design decisions

### Three choices solve different problems

A modeling *method* specifies the questions to answer and the sequence of reasoning. A modeling *language* provides constructs and semantics for representing the answers. A *tool* stores, queries, versions, checks, and presents model elements. Confusing them causes projects to buy a repository and assume a method has appeared, or to select a notation and assume all stakeholders interpret it identically. A graphical language can encode dependency structure faithfully while leaving the decision argument incomplete. Conversely, a strong methodology may be documented in several compatible notations and tool environments.

A useful way to choose modeling scope is to start from decisions and work backward to required facts. Suppose the review must decide whether centralized dispatch can maintain a response-time requirement during network partition. The model needs operational modes, communication assumptions, routing or fallback behavior, relevant delays, and a verification approach. It does not necessarily need detailed wheel geometry. A model is **fit for purpose**, not good merely because its element count is high. Model completeness is relative to a bounded decision and to the consequences of omitted phenomena.

### Formal semantics determine what can be concluded

A relation labeled “satisfies” is useful only if its meaning is controlled. Does it mean “allocated to,” “predicted by an analysis to meet,” “supported by passed verification evidence,” or “approved by authority”? Those are four different assertions. The modeling metamodel should constrain which element types can be related and what proof obligation follows from each relationship. Without this discipline, a query that reports 100% requirements satisfaction may only be counting links, not establishing compliance. A valid quality query tests the relationship's intended semantics, often including version, status, and evidence context.

Consider behavioral abstraction. A model may treat message delivery as instantaneous, reliable, and ordered. This is an acceptable abstraction for some allocation questions but invalid for evaluating duplicate or delayed commands. The correct engineering move is to preserve the assumption in the model's intended-use statement and introduce a more detailed representation when the decision depends on it. The model hierarchy should support refinement: coarse elements map to detailed elements with identified invariants, rather than silently changing meanings between diagrams.

### Model quality includes change impact and reproducibility

A practical modeling plan defines authoritative sources, naming and identity rules, change control, review gates, exports, and query results that can be reproduced from a committed configuration. One useful measure is the fraction of important design questions that can be answered with a reproducible query and examined evidence. Another is the time required to determine which downstream requirements or tests a changed assumption affects. Neither metric is a substitute for validating the truth of the model's content. Automated consistency checks detect contradictions within a representation, not necessarily contradictions with the world.

The tool decision also carries lifecycle risk. Proprietary features, poorly specified imports, or manually maintained diagrams can make the model expensive to transfer to new teams. Exchange-format compliance is not sufficient when semantic details, identifiers, or custom constraints are lost. A serious tool evaluation uses a representative round-trip test: create, export, import, change, query, and compare a small but demanding model. The limiting principle is that model authority derives from justified semantics and controlled evidence, never from vendor branding or attractive visualization.

## Continuity

This chapter builds from [previous chapter](01-mbse-value-model-purpose-and-the-document-to-.md) and leads toward [next chapter](03-stakeholders-concerns-needs-context-conops-an.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w02.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: designing a governed model repository

### Separate the modeling method from its representation

A *method* defines the questions, products, order of work, and review rules. A *language* defines legal constructs and their semantics. A *tool* stores, edits, queries, transforms, and validates instances of that language. Confusing these leads to plans such as “use SysML and create diagrams” that never say what results must be trusted. The NS-MB3 model plan starts with stakeholder needs, identifies typed requirements, allocates each to a responsible component, registers verification procedures, and records evidence by both requirement revision and system baseline. A successful tool import is not an architecture review.

Organize the model as a small number of accountable packages: `Mission`, `Requirements`, `Behavior`, `LogicalArchitecture`, `Interfaces`, `Measures`, `Alternatives`, and `Verification`. Each element must have a stable ID, owner, definition, revision, and allowed outgoing relations. The model-plan specification should state whether multiple owners are permissible, how duplicated IDs are rejected, and what baseline identifier makes a report reproducible. For example, `REQ-03@2` is intentionally different from `REQ-03@1`; a passing fixture for the latter is not evidence for the former.

### Choose queries before views

| Model question | Necessary information | Check | Reviewer interpretation |
|---|---|---|---|
| Which needs have no requirement? | need IDs and `derives` relations | anti-join | Coverage omission, not proof that requirements are valid |
| Which requirements have no allocation? | requirement and component identities | missing-edge query | Investigate feasibility and responsibility |
| Which tests use older requirements? | revisions and baseline labels | equality test | Evidence currency is unsupported |
| Where can a command bypass authorization? | control-flow guards and modes | state reachability | Potential safety violation in the abstraction |

An executable model query is valuable only when its result has an interpretation. A list of all requirements is useful documentation, but it is not an assurance argument. A list of requirements whose **only** test is stale, on the other hand, can identify a concrete release gate.

### Establish a controlled change transaction

Consider an engineering change: position freshness decreases from 300 ms to 200 ms. The transaction consists of a proposed requirement revision, downstream dependency impact analysis, affected interface and state-model revisions, test redesign, new evidence collection, review, and acceptance or rejection of the updated baseline. The change must not silently mutate historical results. In [NS-MB3](../case/model-baseline.json), `REQ-03` is revision 2 while `TEST-03` still identifies revision 1. The repository is structurally connected but contains stale evidence. Both facts are true; a query must report the latter.

A repository may have many valid graphical views of one underlying model. Viewpoint design should follow the concerns and questions described by the architecture description discipline, not the menus available in a product. See [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) for the architecture-description standard; that standard does **not** prescribe a particular SysML workflow. For actual SysML v2 language definitions, use the [OMG specification](https://www.omg.org/spec/SysML/2.0). The case uses a notation-neutral training schema; do not interpret its JSON property names as standardized SysML constructs.

### Practice with answer

**Exercise.** A supplier imports a component `FLEET` into a new package, preserving its display name but creating a different ID. A requirement still allocates to the old ID. Is the model valid? **Answer:** A graph validator should flag a dangling reference or resolve it through an explicit, reviewed ID mapping. Matching display names is insufficient. The correct remedy is a controlled identity transformation and re-execution of dependent queries—not simply redrawing the same line.
