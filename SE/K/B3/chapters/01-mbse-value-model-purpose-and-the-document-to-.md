# Chapter 1 — A model has to earn its existence

*Book III: Introduction to Model-Based Systems Engineering · Week 1 — MBSE value, model purpose, and the document-to-model transition*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 1](../labs/lab-01-mbse-value-model-purpose-and-the-document-to-.md) before attempting [the assessed Week 1 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w01.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **mbse value, model purpose, and the document-to-model transition** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A model is an information structure with identities, properties, relationships and rules. A picture can be produced from that structure, but the picture is not the model. Begin with a decision: determining whether the dispatch system can meet a specified passenger wait target. Backward-chain from that decision to the demand assumptions, fleet-capacity parameters, scenarios, requirements and evidence that must be maintained. A diagram without queryable relationships may help a meeting yet still fail to reduce technical risk.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Models are purposeful abstractions: each representation selects a subset of reality to answer a bounded engineering question.

### Distinguishing related ideas

A model can be well-formed in its language yet useless for a design decision if it omits the failure condition or operational context that matters.

### Interpretation and boundary conditions

Model purpose should determine required fidelity, views, queries and acceptable uncertainty before tool features determine what gets drawn.

## Deeper theory: an engineering model is an argument under abstraction

### Models are selective representations, not miniature realities

A model is useful because it excludes most of the world while preserving relationships relevant to a decision. A requirements model may preserve traceability and allocation but omit physical dynamics. A performance model may preserve queueing and timing but omit contract ownership. Neither becomes defective merely because it cannot answer the other's questions. The failure occurs when a decision maker treats a model as authoritative outside the scope for which its abstractions were justified.

An explicit modeling contract identifies the **question**, the system boundary, retained variables, omitted mechanisms, assumptions, expected accuracy, and intended decisions. These choices form a chain of reasoning. A diagram's syntactic validity says little about whether its abstractions are sufficient. For example, representing dispatch as one action might be valid for a high-level mission narrative but invalid for evaluating network failover latency. A model can be well formed and decision-inadequate at the same time.

### Structural, behavioral, and parametric views constrain each other

An architecture model is strongest when different views share meaning rather than merely resemble each other. A behavior that issues a reservation confirmation must have an allocated performer; the performer must use an interface capable of transmitting the relevant data; and the performance budget must account for that interface. These are cross-view consistency conditions. They can be represented as graph constraints, such as “every mission-critical action is allocated to an element” or “every logical exchange has a defined source and destination.”

A model query checking these rules is more repeatable than a visual inspection of drawings. Nevertheless, queries validate only the conditions they encode. A query can confirm that a connector exists without showing that sender and receiver agree on units, timing, error semantics, or trust. Formal consistency is therefore necessary for some modeling objectives but not sufficient for interoperability or adequacy.

### The strength of a model claim has levels

Distinguish at least four claims: the repository is internally consistent; the model represents intended design choices; the represented design is physically or operationally plausible; and the actual fielded system will meet stakeholder outcomes. Each step requires additional evidence. Repository constraints support the first claim, reviews and traceability support the second, analyses and experiments inform the third, and representative system testing and operational data inform the fourth. Jumping directly from “the model contains a verification link” to “the requirement is verified” mistakes an evidence relationship for the evidence itself.

Calibration has the same epistemic limitation. Fitting parameters to observed shuttle delays can improve agreement with those data but cannot establish predictions under an unseen storm or communications outage without a defensible generalization argument. Validation must be tied to the planned application domain and to uncertainties relevant to the decision. An error of 10 ms may be negligible for an hour-scale demand model but catastrophic for a safety-critical control loop.

### Model ownership is a change-control problem

When a model becomes the coordination center for a program, its elements acquire lifecycles. Names, identities, relationships, units, and baselines must survive tool exchanges and reorganizations. Recreating an object with the same label is not necessarily preserving the same engineering identity. Similarly, changing a source requirement without regenerating affected views can cause apparent agreement among stale representations. A trustworthy model-based workflow records provenance, version alignment, transformations, and the assumptions under which linked views remain consistent.

MBSE delivers value when it reduces ambiguity, detects inconsistency early, and improves decisions under change. Counting diagrams or model elements measures activity, not that value. The decisive question is which costly engineering mistakes became easier to prevent, diagnose, or correct because the model exists.

## Worked Northstar example

Two documents use the term “available vehicle.” One means powered on; the other means dispatched and able to accept new passengers. Importing both as the same model property creates a false agreement. Create VEH-STATE and VEH-ELIGIBILITY as distinct properties, define their derivation and record the discrepancy before accepting the imported source.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Tool purchase is not an outcome; uncontrolled duplication, misleading completeness and unrecorded assumptions are foreseeable failure modes.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 1: A model has to earn its existence](../labs/lab-01-mbse-value-model-purpose-and-the-document-to-.md), you will: Audit six supplied claims about shuttle capacity. Identify which belong as authoritative model elements, source references, calculations or unresolved issues. Produce a model-value hypothesis with a measurable test. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 1 deliverable and grading rubric.

## Continuity

This chapter builds from the earlier Foundation books and leads toward [next chapter](02-modeling-plan-methodology-language-tool-and-r.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w01.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: model value as a falsifiable investment

### Decide what the model must make cheaper, safer, or more reliable

Model-based systems engineering begins with a decision that is expensive to make badly. A repository of diagrams is not inherently superior to a collection of documents. Its advantage is that an element has an identity, relationships carry defined meanings, and a change can be propagated into questions that can be checked. Choose the smallest model whose *queries* justify its maintenance. In the [NS-MB3 case](../case/INDEX.html), the initial question is whether an architecture can support eight shuttle trips in the design peak hour while enforcing authorization, timeliness, and an energy reserve. A model that cannot expose the shortage in candidate A has little decision value, regardless of its number of diagrams.

The initial candidate has two vehicles, each assumed to complete three trips per hour. Its ideal throughput is

\[
Q_A = n_A r = 2(3)=6\ \mathrm{trips/h}.
\]

The requirement is eight; the analytical shortfall is two trips per hour. This is a necessary feasibility check, **not** a simulated demonstration of real operating capacity. A stochastic service model would additionally require dwell-time variation, failures, dispatch conflicts and charging constraints. The model is worthwhile here because the contradiction can be found before committing to a detailed physical design.

### Construct a model-purpose contract

Write down four items before choosing a modeling language: (1) the decision and its date, (2) stakeholders and the questions their viewpoints must answer, (3) element and relationship types needed to answer those questions, and (4) what observation would falsify the model's prediction. For NS-MB3, the model must answer: Which candidate meets the ideal capacity bound? Which requirements have allocated components? Which tests target the current requirement revisions? Does the timing budget hold in degraded operation? A drawing-only model can communicate the answer to one question, but cannot reliably answer all four without manually rediscovering identity and version metadata.

A useful accounting model for adoption is

\[
V = N\Delta h - H_{\mathrm{build}} - H_{\mathrm{maint}} - H_{\mathrm{review}},
\]

where \(N\) is the number of decisions or changes the model supports, \(\Delta h\) is hours saved per decision *relative to a specified baseline practice*, and the remaining terms measure building, upkeep and review. Suppose a pilot consumes 80 hours up front and 40 hours of updates and review, but saves an estimated 4 hours for each of 30 changes. Then \(V=30(4)-80-40=0\) hours: the project is at a break-even estimate, not an established success. The threshold is 30 changes, conditional on savings being real and measured. If a manual workflow already has versioned identifiers and scripts, the incremental benefit may be smaller. Cost or schedule benefits should be measured across comparable change requests, not inferred from diagram quality.

### Practice with answer

**Exercise.** A revised model costs 100 hours to build and 20 hours to maintain. An observed pilot suggests a mean saving of 5 hours per change. How many changes are needed to break even, and what could invalidate this estimate?

**Worked answer.** \(N=(100+20)/5=24\). If the pilot measured easy changes only, or if common model queries require manual cleanup after imports, the five-hour saving is biased. Run a representative pilot with both simple and cross-disciplinary changes; record observed effort and erroneous decisions, not only the time to edit diagrams.

**Boundary of this chapter.** Formal language conformance, model fidelity, and operational validation are separate from the economic justification. The independent teaching audit in [the case checker](../tools/step03_book3_model_check.py) validates a small JSON schema, **not** a SysML implementation.
