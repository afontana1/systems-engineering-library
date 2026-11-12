# Model, method, language, tool, and repository

**Reference entry · MBSE and software-intensive systems · Expanded reference**

## Definition and diagnostic distinction

A **model** is a purposeful representation of selected properties of a system; a **language** defines allowed constructs and their semantics; a **method** prescribes how engineers create, check, and use representations; a **tool** implements editing and analysis capabilities; a **repository** manages identity, versions, access, and relationships. Choosing SysML or another notation does not by itself provide a modeling method, and purchasing a repository does not establish an authoritative digital thread.

## Theory: semantics determine the inferences a model supports

A diagram is a projection of an underlying information model. A block-connection arrow may mean physical connectivity, information exchange, dependency, or merely commentary—unless the relationship type is defined. Typed relations constrain inference: `allocatedTo(function, component)` is not interchangeable with `satisfies(component, requirement)` or `verifiedBy(requirement, test)`. A consistent metamodel supports queries such as “find requirements with no verification evidence” without guessing from line placement.

Distinguish **syntax validity**, **semantic consistency**, and **fitness for intended use**. A model may parse, satisfy all repository constraints, and still omit the environmental dynamics that determine mission success. Conversely, a small spreadsheet with documented units, equations, data, and assumptions may be more credible for a particular decision than a vast visually polished system model. Model fidelity should follow the decision consequence and needed discrimination among alternatives.

## Worked example: a misleading architecture report

A shuttle model contains a `Dispatcher` element, `Vehicle` elements, and “serves” arrows. One analyst interprets “serves” as dispatch assignment; another interprets it as successful passenger pickup. A query counts ten served requests, but only eight pickups occurred. Separating `assigns(vehicle, request)` from `completes(vehicle, trip)` and adding timestamps reveals the difference. A typed constraint that every completion refers to an assigned request can then detect orphan records—without claiming that the resulting model validates the real service.

## Engineering use and evidence

Publish a modeling charter: intended decisions, modeling questions, viewpoints, element and relation definitions, naming and units conventions, configuration rules, validation queries, ownership, and review gates. Treat tool-generated diagrams as views of versioned model facts. Run automated checks for missing types, unresolved references, multiplicity violations, requirement coverage, and contradictory parameter units. Independently test important computations with known examples and boundary cases.

## Limitations and connections

Tools can enforce syntactic discipline but cannot determine which operational assumptions are true. Tool migration can preserve graphical appearance while corrupting semantics. Connect this topic to **views and viewpoints**, **traceability**, **functional allocation**, **digital-thread provenance**, and **model credibility**.

## Technical analysis: semantics, method, and implementation are distinct

A model language defines permitted structures and meanings; a method prescribes how teams use model artifacts to make decisions; a tool stores and manipulates them. Conformance to a modeling syntax alone does not establish that a model is complete, logically consistent, or relevant to the engineering decision. Maintain explicit constraints on identity, quantity units, state transitions, and relationship types.

Consider a logical model in which `remaining_energy` is measured in **kWh** but the code subtracts power in **kW** without multiplying by elapsed **hours**. With a **2 kW** load over **30 minutes**, energy consumption is `2 × 0.5 = 1 kWh`; subtracting `2` incorrectly removes **2 kWh**. Both quantities may be represented as floating-point values, so a syntactically valid diagram or generated program can still encode a dimensional error. Typed quantities and invariant checks catch a class of mistakes that diagram review alone does not.

**Evidence boundary.** Record metamodel/version, transformation rules, validation constraints, and generated-artifact provenance. A tool certification claim cannot stand in for validation of a particular model's assumptions, boundary conditions, or decision relevance.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Logical decomposition models and work products must make functional and behavioral relationships explicit. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §4.3 Logical Decomposition](https://www.nasa.gov/reference/4-0-system-design-processes/) · *direct guidance*.
- **C2:** The credibility of a particular model or simulation remains application- and evidence-dependent. **Evidence:** [NASA — NASA-STD-7009B, Standard for Models and Simulations (2024), Document Scope; credibility in model/simulation life cycle](https://standards.nasa.gov/node/263) · *direct standard scope*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [NASA · NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263) — Credibility practices for modeling and simulation used in decisions.

## In-depth method: a model that supports decisions and audit queries

The [MBSE semantic-modeling method guide](../methods/mbse-semantic-modeling-handbook.md) constructs a governed graph of needs, requirements, architecture elements, verification cases, and evidence; adds a state-machine invariant and a dimensional energy balance; and includes a [reproducible trace audit](../methods/code/model_trace_audit.py). It is intentionally notation-independent so the engineering logic is visible independent of a SysML tool.

### Type checks prevent false inference

A `verifies(test, requirement)` link describes a planned relation between test and requirement. It is **not** proof that the test was executed or that current evidence was accepted. A defensible evidence claim also requires an appropriate scenario, baseline match and result disposition. If test evidence is from build `NS-2.2` but the model baseline is `NS-2.3`, a graph can be complete in link count and still have **stale verification evidence**.

### Parametric models expose physical contradictions

A route-energy model might state

\[
E_{\rm required}=e_d D+P_{\rm aux}T.
\]

For \(e_d=0.24\) kWh/km, \(D=180\) km, \(P_{\rm aux}=2\) kW and \(T=10\) h, demand is 63.2 kWh. With 70 kWh usable energy, margin is 6.8 kWh. Increasing traction use to 0.29 kWh/km raises demand to 72.2 kWh, producing a negative margin. A diagram can be syntactically valid while this engineering constraint fails. Units, assumptions, and analysis provenance therefore belong in the model, not in an unattached spreadsheet.

**Standards distinction:** the engineering schema above is an educational example. For normative SysML v2 syntax, rely on the [OMG specification](https://www.omg.org/spec/SysML/2.0); a validated model and a conformant language implementation are separate assurance questions.

## A behavioral invariant is a claim about allowed traces

The technical meaning of a state-machine model can be expressed as a transition relation \(s\xrightarrow{e}s'\), with explicit guards and effects. For a vehicle with one assignable seat, a testable safety invariant is \(0\le\mathrm{allocated}(s)\le1\). An `ASSIGN` event may be legal only for a validated request and only when an assignment is available; a repeated `ASSIGN` must be idempotent or rejected without changing capacity.

A small state-space exploration can produce the counterexample `VALIDATE(0) → ASSIGN(0) → ASSIGN(0)` when a defective model increments capacity twice. This is evidence of a defect in **that finite abstract model**, not proof of a distributed implementation's correctness. Read [state contracts and bounded model checking](../methods/mbse-behavioral-contracts.md) alongside the existing typed model/evidence handbook to connect model semantics to verified architecture claims.

## Phase 3 technical reference: Language semantics and executable assertions are not interchangeable

A UML association of optional `Worker[0..1]` to a reservation describes one object's multiplicity. It does **not** ensure that a worker is unique across **all** active reservations. OCL-style invariants can specify cross-object consistency—e.g., `Reservation.allInstances()->select(r | r.status = Status::Active)->isUnique(r | r.worker)`—while preconditions express when an activation is permitted. Neither an OCL statement nor a Python snapshot validator automatically supplies transaction isolation or a conforming language implementation. The [UML/OCL worked guide](../methods/uml-ocl-software-contracts.md) demonstrates valid and invalid fixtures, operation contracts and a concrete duplicate-allocation counterexample, distinguishing model claims from enforcement evidence.

## Phase 4 technical reading: Distinguish language conformance from model checking

SysML v2 is a modeling language specified by OMG with a KerML semantic foundation; a modeling methodology specifies activities and rationale; a modeling tool implements notation, semantics, queries, repository behavior and diagnostics. A tiny JSON object graph can teach traceability and check typed links, but it is **not** SysML v2 text, a conformant API representation, or a formal language proof. The Campus Mobility exercise validates declared need–requirement–component–control–evidence relationships and configuration labels; it cannot establish real component behavior or that the hazard inventory is complete. The [baseline and semantic-validation guide](../methods/model-baselines-and-evidence.md) gives an exact migration plan for tool-based SysML parsing and query validation.

## Phase 5 technical reading: From modeling syntax to a defensible engineering model

A modeling language, a modeling method and a validation tool are distinct. The SysML v2 example starts with definitions (`part def Shuttle`) and typed usages (`part campusShuttle : Shuttle`) and then builds an external, inspectable trace from `NEED-ACCESS` through `REQ-DOOR`, the door controller and `EV-DOOR`. Structural references can be tested independently of the language parser, but a passing graph check is **not** SysML v2 conformance. The invariant \(\mathrm{permitOpen}\Rightarrow(\mathrm{speedValid}\land\mathrm{brakeValid}\land v\le0.5\;\mathrm{m/s}\land\mathrm{brakeEngaged})\) shows how engineering rules supplement structure. The [SysML v2 and traceability guide](../methods/sysml-v2-modeling-and-traceability.md) provides the illustrative text, exact tool-validation workflow, testable CSV crosswalk and explicit limitations.



## Step 02 review studio — four kinds of agreement that should not be conflated

A modeling *method* specifies why and how engineers reason; a *language* specifies legal forms and semantics; a *tool* implements some functions over those forms; a *model* is a particular statement about a particular system. A diagram can be visually persuasive while being semantically invalid, and a syntactically valid model can encode a false design assumption.

**Solved exercise:** a local Python checker confirms every requirement ID in a JSON graph points to an existing component and test. Does this make the graph a SysML v2-conformant model? **No.** It demonstrates one limited graph property. Language conformance requires checks against the actual relevant grammar/semantics in a conforming implementation, while engineering adequacy requires a separate intended-use, correctness, and evidence review.

**Practice:** write four separate acceptance claims for a model: parse succeeds; typed relations are well formed; a target engineering invariant holds; and results are credible for a stated decision. Record which tool and which test supplies evidence for each; do not promote a static-graph check into formal language conformance.

## Follow the knowledge

**Related concepts**

- [Architecture views, viewpoints, and consistency](views-and-viewpoints.md)
- [Requirements traceability: a typed graph of engineering claims](traceability-graph.md)
- [Digital thread and digital twin: preserving engineering meaning across time](digital-thread-and-twin.md)
- [Simulation verification, validation, and credibility](model-vv-and-credibility.md)

**Go deeper in the 240-chapter textbooks**

- [Book 3, Chapter 01: Book III · Chapter 1: A model has to earn its existence](../B3/chapters/01-mbse-value-model-purpose-and-the-document-to-.md)
- [Book 3, Chapter 02: Book III · Chapter 2: Choosing a language is not choosing a method](../B3/chapters/02-modeling-plan-methodology-language-tool-and-r.md)
- [Book 9, Chapter 11: Book 9 · Chapter 11 — Extend the modeling language and automate queries, validation rules, matrices, and generated products](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
