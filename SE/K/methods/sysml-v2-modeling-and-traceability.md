# SysML v2 modeling: language, architecture, traceability, and evidence

## 1. Engineering question and intended use

How can a systems team turn a requirement, interface and design into **one inspectable, versioned model** without confusing diagram completeness with engineering correctness? This guide uses the fictional Campus Mobility shuttle baseline CM-B2 to separate four different propositions:

1. A model *parses* according to a language grammar.
2. Its elements and references *resolve* to a well-formed model under the language's semantics.
3. Project-specific engineering constraints *hold* for a given configuration.
4. Real measurements and controlled reviews *support* an engineering claim about the built system.

These propositions are not interchangeable. A valid SysML document can describe an unsafe architecture. A verified JSON trace graph may be structurally sound without being SysML at all. A simulation that fits data does not prove a design is fit for service.

**Prerequisites:** [model semantics](mbse-semantic-modeling-handbook.md), [evidence configuration](model-baselines-and-evidence.md), [behavioral contracts](mbse-behavioral-contracts.md), and [the complete Campus Mobility case](campus-mobility-engineering-case.md).

## 2. What SysML v2 adds—and what it does not

OMG formally adopted **SysML 2.0** and its **KerML 1.0** foundation in 2025. SysML v2 provides textual and graphical expression for modeling structure, behavior, requirements and analysis. KerML supplies foundational semantic machinery; the separate Systems Modeling API and Services specification provides standardized access and interchange semantics. That does **not** make every JSON file a SysML model or ensure that two tools interpret every implementation-specific extension identically.

A useful information architecture distinguishes:

| Layer | Responsible artifact | What a reviewer checks |
|---|---|---|
| Normative language | SysML v2 + KerML specification | Syntax, abstract syntax, semantics, language version |
| Model source | `models/campus-mobility.sysml` | Names, definitions, usage typing, resolvable references |
| Engineering rules | Requirement set, interface constraints and evidence links | Coverage, units, multiplicities, version applicability |
| Physical/empirical evidence | Test records and independent observations | Intended-use conditions, controls, provenance and uncertainty |
| Decision authority | Controlled review and risk disposition | Which claim is accepted, conditions, remaining defects |

The language constrains *representation*. Engineering methodology supplies *process*. Modeling tools implement parts of the language and provide diagnostics. Evidence establishes the empirical basis for claims. None should be silently substituted for another.

## 3. From definitions to usages

Consider an abstract shuttle as a composition of a speed sensor, brake sensor, door controller and dispatch service. In SysML v2, `part def` introduces a reusable **definition**; `part name : Type` introduces a **usage** typed by a definition. They have different identities and should not be confused with a casual grouping of diagram boxes.

The [downloadable textual model](models/campus-mobility.sysml) contains the following deliberately limited structural slice:

```sysml
package CampusMobility {
    part def SpeedSensor;
    part def BrakeSensor;
    part def DoorController;
    part def DispatchService;
    part def Shuttle {
        part speedSensor : SpeedSensor;
        part brakeSensor : BrakeSensor;
        part doorController : DoorController;
        part dispatch : DispatchService;
    }
    part campusShuttle : Shuttle;
}
```

This is **instructional source**, not a statement of conformant parsing or a complete requirements model. Formal constraints, port/item definitions, state machines, requirement satisfaction, measurements and behavior are deliberately not asserted in this skeletal example. The `.sysml` file has **not** been passed through an official SysML parser in this release; do that before using it as a valid-language reference.

### A reproducible tool-validation procedure

1. Obtain the [official OMG Systems Modeling community SysML v2 release](https://github.com/Systems-Modeling/SysML-v2-Release/releases), recording the exact release and applicable language specification version (the release stream is updated regularly).
2. Open/import `campus-mobility.sysml` in its supplied pilot textual-notation implementation. Save diagnostics, the tool version and the model file hash. **If import fails, fix the source and document the difference—do not bypass diagnostics.**
3. Inspect the model's semantic element listing. Confirm that `campusShuttle` is a usage of `Shuttle` and that each contained usage resolves to its intended definition. A screenshot of a diagram is not a reference-resolution test.
4. Extend the model **inside the actual implementation** with the project's requirements, attributes, units, interface items and behavioral rules, using examples bundled with that implementation. Re-run parsing and semantic validations. Do not invent textual syntax from a drawing or from an unconstrained Python object graph.
5. Export the model through a versioned supported representation/API, then explicitly map project identifiers such as `REQ-DOOR` and `EV-DOOR` to canonical stable identifiers; test the export-import round trip and differences. Keep unrecognized constructs in a discrepancy log.

**Why this matters:** a repository can enforce CSV linkage invariants without ever validating the grammar or semantic typing of the `.sysml` source. The [crosswalk audit](code/sysml_trace_crosswalk.py) intentionally performs only the former.

## 4. A concrete end-to-end trace

The safety scenario is *door release during vehicle motion*. The stated stakeholder need `NEED-ACCESS` leads to `REQ-DOOR`; its allocated owner is `door-controller`; its related hazard is `H-DOOR`; the linked design control is `CTRL-DOOR`; and the test evidence is `EV-DOOR`. These names must remain stable across the [requirements](data/campus-requirements.csv), [interfaces](data/campus-interfaces.csv), [verification matrix](data/campus-verification-matrix.csv), and [model baseline](data/campus-mobility-release.json).

A conceptual typed chain is

\[
\text{Need} \xrightarrow{\mathrm{derivedInto}} \text{Requirement}
\xrightarrow{\mathrm{allocatedTo}} \text{Component}
\xrightarrow{\mathrm{testedBy}} \text{Procedure}
\xrightarrow{\mathrm{resultsIn}} \text{Evidence}.
\]

Its project rules should include:

- Every controlled requirement has a valid need, an identified allocation, a verification strategy and accountable owner.
- An evidence record names the **tested** requirement, environment, baseline, build, acceptance criterion, limitations and result. A `verifies` link alone does not assert that the test passed.
- Changes to allocated components or relevant interfaces trigger applicability review of associated requirements and evidence; matching link IDs are not sufficient.
- Safety controls use explicit state/input-validity preconditions, not merely boolean nominal threshold checks.

For the door controller, an illustrative property is

\[
\mathrm{permitOpen} \Rightarrow
(\mathrm{speedValid}\land\mathrm{brakeValid}
\land v\le 0.5\;\mathrm{m/s}
\land\mathrm{parkingBrakeEngaged}).
\]

This is an **engineering invariant**, *not* executable SysML v2 grammar; use an implementation-specific supported modeling construction when encoding it. The converse is not required: satisfaction of those inputs does not force the controller to open the door, because other interlocks may be active.

## 5. Executable trace crosswalk (and its honest boundary)

The standard-library program [sysml_trace_crosswalk.py](code/sysml_trace_crosswalk.py) checks several concrete, reviewable rules. From the repository root:

```sh
python3 SE/K/methods/code/sysml_trace_crosswalk.py
python3 SE/K/methods/code/model_thread_audit.py SE/K/methods/data/campus-mobility-release.json
```

The first checks IDs and allocations across the CSV artifact set, confirms evidence and build labels, and detects unclosed hazards. The second checks typed graph links and evidence currency. A passing result means the **specified local checks passed on those particular files**, not that SysML v2 was parsed or that a physical shuttle is safe. Edit a copied requirement row to change `allocation` to a nonexistent component and run the crosswalk again: it should fail. Restore the file before building the website.

## 6. Semantic and physical counterexamples

**Misleading “full coverage”:** all requirements have attached evidence, but `EV-DOOR` was collected with simulated sensor inputs and does not exercise a mechanical override. Links are complete; the safety claim is not.

**Misleading “passes parser”:** a grammar-valid model assigns a controller type to an instance but neglects a freshness requirement for the incoming speed sample. Conformance is not requirement adequacy.

**Misleading “same graph”:** a controller upgrade from CM-B2 to CM-B3 leaves identical requirement IDs but changes implementation behavior. Old tests must be assessed for applicability and re-executed when necessary; re-labeling old evidence is inappropriate.

**Misleading “same units”:** a model combines 150 milliseconds with 0.5 seconds as bare floating-point numbers. Consistent data types and physical quantities with conversion rules are required for meaningful comparison.

## 7. Practice problems and answer tests

1. Draw the distinction between definition, typed usage, requirement, verification case and measured evidence in the example. Explain why an untyped diagram edge is insufficient to audit a relation.
2. Suppose the speed sample age is 180 ms, and the interface contract requires no more than 150 ms. Even if the measured speed is 0.3 m/s and the brake is engaged, should the controller authorize opening? **No:** `speedValid` is false; the interlock remains inhibited.
3. Change a local *copy* of the requirements CSV so `REQ-DOOR` allocates to `dispatch-service`. Predict which cross-document check will fail, then execute it.
4. Design a parser-conformance test record containing tool version, language version, source hash, diagnostics, semantic identity checks and a review signature. Explain why none of those fields replaces operational evidence.

## 8. Sources, scope and curriculum paths

- [OMG SysML 2.0 specification](https://www.omg.org/spec/SysML/2.0) and [OMG formal specification history](https://www.omg.org/spec/SysML/About-SysML/) — official language scope and versions.
- [Official SysML v2 Release repository](https://github.com/Systems-Modeling/SysML-v2-Release/releases) — pilot implementation, language documentation, examples and updated releases; version-lock any tool-generated evidence.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — system decomposition, requirements and V&V context; does not certify this illustrative model.
- [Book 3, chapter 4](../B3/chapters/04-requirements-modeling-relationship-semantics-.md), [Book 3, chapter 6](../B3/chapters/06-structure-interfaces-ports-connections-and-th.md), [Book 9, chapter 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md); courses EN.645.631, EN.645.632 and EN.645.768.

**Scope:** educational design/crosswalk demonstration. No normative SysML v2 language-conformance result is claimed. A separate tool-run evidence package is required before any such claim.
