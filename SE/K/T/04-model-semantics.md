# Model semantics, viewpoints, and digital traceability

*Core Concepts · Modeling & software · T04*

> Know which claims a model can support and how its meaning survives revisions.

**Recommended preparation:** [Requirements, traceability, and assurance arguments](02-requirements.md), [Architecture, interfaces, and design tradeoffs](03-architecture.md)

**Related course companions:** [Book 3](../B3/OPEN-BOOK.html), [Book 9](../B9/OPEN-BOOK.html), [Book 16](../B16/OPEN-BOOK.html)

## 1. A diagram is a view, not the model
A system model encodes entities, relationships, constraints, and sometimes executable behavior. A diagram displays a selection of that model. Two diagrams can look similar while having incompatible meaning: a dashed arrow may represent a dependency, a realization relation, or a flow, depending on the language and model conventions. A line without a declared semantic type is a weak basis for automated engineering decisions.

Start by defining the metamodel, even if it is informal: permissible element types, relation types, identities, units, and validation rules. For a simple shuttle model, types might be Requirement, Function, Component, Interface, Hazard, and Test. Relations might be `refines`, `allocated_to`, `exposes`, `mitigates`, and `verifies`. Declare whether a relation is directional and what evidence or preconditions make it legitimate.

## 2. Separate consistency, completeness, and correctness
A graph can be internally consistent but wrong about the world. Consistency checks catch impossible relations and dangling IDs. Completeness checks seek missing allocations or missing tests. Correctness requires inspection, measurements, stakeholder confirmation, and independent review. Automated validators can rule out certain mistakes but cannot establish that a mission concept is socially acceptable or physically workable.

Use invariants. Each high-priority requirement must have an accountable owner; each exposed interface must have a contract; each safety claim must be supported by evidence at a specified revision. Report these as measurable queries rather than vague declarations of model maturity.

## 3. Parametric models are conditional arguments
Suppose battery energy \(E\) must cover trip energy and contingency. One simple constraint is \(E_{usable}\geq n e_{trip}+E_{reserve}\). This is a model, not a fact of nature. Temperature, battery aging, payload, slopes, and regenerative braking can change \(e_{trip}\). The model gains credibility when assumptions, inputs, calibration data, and a domain of applicability are explicit.

Units are part of semantics. Adding kW to kWh is an error even if a diagram tool allows the formula. For each parameter, store unit, value, uncertainty, source, validity interval, and revision.

## 4. Build a revision-aware digital thread
A requirement-to-test link is only operationally useful if it refers to specific versions. Imagine a test passed specification v3, while the approved system uses v4 with an altered charging deadline. The link still exists, but the result may not apply. Treat revision, configuration, timestamp, and origin as first-class properties of the evidence chain.

A digital thread connects claims across tools; it is not necessarily one database. Federated records can be trustworthy if identifiers, semantic mappings, change control, and validation rules are clear. A single file can also be untrustworthy if it silently overwrites provenance.

## 5. Practice separating representation from inference
Suppose a SysML-like model contains a block named `Battery`, a property `capacity=40`, and a connector to `DriveMotor`. That alone does not prove a forty-kilowatt-hour battery can power a route. What are the units? Is the property nominal, usable, or aged capacity? Does the connector describe electrical energy, data, or logical dependency? Is there a constraint binding the route-energy estimate to the battery property? A human may mentally fill these gaps; an engineering model should not require guesswork.

Define a simple validation rule: every numerical performance parameter must have a declared unit and source. Another rule requires every high-criticality requirement to have at least one test link whose configuration is current. Now distinguish validation rules from **inference rules**: a structural validation can establish that a link is well-formed, while a performance inference needs a computational constraint and accepted input values. The strength of the conclusion must not exceed the strength of the weakest relevant assumption.

**Model reviews should be question-driven.** Ask what decision the model is supporting; which elements and behaviors are in scope; which views make the relevant relationships legible; how values were obtained; how uncertainty is represented; and what change would invalidate the result. A single model repository may support many decision-specific views, but no view can be treated as universally complete.

**Check your reasoning:** A model has no dangling identifiers and passes its schema validator. Does it establish that the design is feasible? No. It establishes only selected structural properties. Feasibility requires credible physics, resource, behavior, and operational analyses.

## Guided worked example

### Worked check: completeness versus meaning
A model has 20 requirements. Eighteen have allocations, giving 90% allocation coverage. All 20 have test IDs, giving 100% test-link coverage. Yet two linked tests use deprecated configurations. An automated report should flag these separately; a combined “model quality 95%” hides the kind of action required.

## Independent transfer exercise

Use the model CSV in the companion lab to identify orphan requirements, bad relation types, and evidence linked to the wrong revision. Propose two validation rules and one issue that still needs human judgment.

[Open the companion hypothetical lab](labs/04-model-semantics-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

Distinguish graph structure from operational truth. A passing validator is evidence of syntax and selected invariants, not a certification of the system.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
