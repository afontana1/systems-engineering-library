# Model-based systems engineering: semantics, constraints, and executable checks

*Technical method guide · MBSE, system architecture, traceability, and parametric analysis · Phase 1 expansion*

**What this chapter enables.** Construct a small but meaningful system model, specify the meaning of its relationships, evaluate parametric constraints, find stale evidence, and distinguish a consistent model from an acceptable real system. The examples are notation-independent so they can be applied in SysML v1, SysML v2, or a carefully governed tabular repository.

**Prerequisites:** [Model versus method versus tool](../encyclopedia/model-language-method-tool.md), [traceability](../encyclopedia/traceability-graph.md), and [functional versus physical architecture](../encyclopedia/functional-vs-physical.md).

## 1. What is the model meant to decide?

The fictional Northstar Campus Shuttle team is deciding whether a dispatch release and battery configuration can satisfy two claims: acknowledge requests on time and complete a representative route while preserving a usable-energy reserve. A schematic diagram is insufficient for both questions. The team needs information that can be queried, computed, checked for dimensional correctness, and tied to configuration-specific evidence.

Start with a **modeling question**: “For release `NS-2.3`, which in-scope requirements have applicable, accepted evidence, and under which operating assumptions does the proposed energy allocation remain feasible?” That question determines the minimum model elements and checks. Modeling for visual attractiveness without a query or decision produces expensive but weak artifacts.

## 2. Build a typed engineering graph

Represent the repository as a directed typed graph

\[
G=(V,E,\tau_V,\tau_E),
\]

where \(\tau_V\) maps each node to an artifact type (need, requirement, function, element, interface, verification case, test result), and \(\tau_E\) maps each relationship to a defined kind (derives-from, allocated-to, verifies, result-of, supports). Types alone are not proof: their allowed endpoints, direction, and meaning must be documented.

| Statement | Example edge | What it does **not** prove |
|---|---|---|
| R-ACK derives from N-RIDE | `R-ACK → derivesFrom → N-RIDE` | That R-ACK fully captures every aspect of N-RIDE |
| R-ACK is allocated to C-DISP | `R-ACK → allocatedTo → C-DISP` | That C-DISP actually meets the requirement |
| T-ACK targets R-ACK | `T-ACK → verifies → R-ACK` | That the test has run or passed |
| E-ACK came from T-ACK | `E-ACK → resultOf → T-ACK` | That the result is applicable to the current build |
| E-ACK supports R-ACK | `E-ACK → supports → R-ACK` | That an approving authority has accepted sufficient evidence |

The first and last arrows look similar on paper, but one justifies a lower-level requirement while the other makes a configuration-specific evidentiary claim. Do not infer one by traversing an arbitrary chain of arrows.

### Minimal metamodel rules

1. Every governed node has a stable identifier, type, and revision or configuration identity.
2. Every edge has a recognized relationship type and valid endpoint types.
3. Every in-scope requirement has a legitimate rationale or a documented justified exception.
4. Every claimed verification has an applicable test result, an approved method and decision rule, and a matching configuration.
5. Unit-bearing properties declare dimensions and applicable operating conditions.
6. A model baseline retains the test/evidence provenance used for decisions.

These are **engineering quality rules**, not an assertion that a particular SysML version mandates this exact schema.

## 3. Requirements, tests, and evidence must not collapse into one status

Consider model baseline `NS-2.3`. The repository contains test case T-ACK that targets requirement R-ACK. The *recorded result* E-ACK is marked passed but was measured on release `NS-2.2`. A simplistic dashboard counts one verification link and shows “covered.” A semantic quality check instead says **stale evidence for NS-2.3**.

The correct rule is more specific:

\[
\operatorname{CurrentEvidence}(r,b) = \exists e,t:\;\operatorname{targets}(t,r)\land\operatorname{producedBy}(e,t)\land\operatorname{accepted}(e)\land\operatorname{build}(e)=b\land\operatorname{scenarioApplicable}(e,r).
\]

The equality test is deliberately conservative: an authorized configuration-equivalence argument may allow reuse across builds, but the model must explicitly record that review; it must not silently assume equivalence. The [trace audit program](code/model_trace_audit.py) checks these conditions on a small JSON repository and distinguishes **covered**, **missing**, and **stale** evidence. Compare the [stale baseline](data/model-stale.json) and [corrected baseline](data/model-corrected.json).

Notice the epistemic boundary: this query checks evidence *governance*. It cannot know whether the underlying experimental method was scientifically appropriate, whether a hazard was overlooked, or whether an accepted requirement addresses the user need. It is a useful filter for review, not automatic certification.

## 4. Model behavior, not only static structure

A dispatcher can have a valid component structure and still create duplicate assignments under repeated messages. Represent the booking lifecycle with controlled states such as `NEW`, `VALIDATED`, `OFFERED`, `ACCEPTED`, `REJECTED`, and `CLOSED`. Define transitions with guards and effects, for example:

| Transition | Guard | Required effect |
|---|---|---|
| `NEW → VALIDATED` | Syntax, authorization and service-domain checks succeed | Record validation event with request ID |
| `VALIDATED → OFFERED` | A viable dispatch candidate exists | Reserve candidate with expiring offer ID |
| `OFFERED → ACCEPTED` | User response is on time and offer remains valid | Commit at most one active assignment |
| `OFFERED → CLOSED` | Offer expires | Release resource reservation |
| `NEW → REJECTED` | Request fails defined check | Return governed error reason |

An invariant such as “every accepted request has at most one current committed assignment” can be expressed in notation-neutral mathematics:

\[
\forall r\in\mathcal R:\quad \operatorname{status}(r)=\mathrm{ACCEPTED}\implies\left|\operatorname{activeAssignments}(r)\right|\leq1.
\]

A model checker can explore state transitions under stated bounds; an integration test can observe actual software behavior. Neither alone proves that every relevant operational failure has been modeled. Always distinguish **formal proof about a model**, **test of an implementation**, and **validation in use**.

## 5. Parametrics: make a constraint executable and dimensional

Model route energy consumption as traction energy plus auxiliary energy:

\[
E_{\mathrm{req}}=e_dD+P_{\mathrm{aux}}T.
\]

Here \(e_d\) has units kWh/km, route distance \(D\) is km, auxiliary load \(P_{\mathrm{aux}}\) is kW, and operating time \(T\) is hours. Both terms yield kWh. This dimensional check catches the common error of adding kW directly to kWh.

Suppose \(e_d=0.24\) kWh/km, \(D=180\) km, \(P_{\mathrm{aux}}=2\) kW and \(T=10\) h. Then

\[
E_{\mathrm{req}}=0.24(180)+2(10)=43.2+20=63.2\ \mathrm{kWh}.
\]

With **70 kWh available usable energy under the declared configuration and conditions**, the illustrative reserve margin is \(70-63.2=6.8\) kWh, or approximately \(9.7\%\) of usable energy. If cold weather increases \(e_d\) to 0.29 kWh/km with the other assumptions unchanged, required energy becomes \(0.29(180)+20=72.2\) kWh, and margin becomes **−2.2 kWh**. The model fails the constraint even though the component diagram is unchanged.

A necessary constraint is

\[
E_{\mathrm{req}}\leq E_{\mathrm{usable}}.
\]

It is not automatically sufficient: range uncertainty, charging contention, pack degradation, route disturbances, reserve-policy obligations and performance limitations may require additional equations. A model's apparent precision must not be confused with predictive credibility.

## 6. Make models inspectable through questions and queries

A useful repository produces answers to concrete questions:

- Which approved requirements have no responsible system element?
- Which required interfaces lack units, direction, protocol, timing or error behavior?
- Which test cases exist without executed results?
- Which accepted results were collected against an older baseline?
- Which constraints have unbound parameters or inconsistent dimensions?
- Which requirements changed since the last accepted evidence package?
- Which derived requirements have no parent rationale?

Write these questions **before** building dashboards. Each query should state what its output measures and what it does not imply. For example, “coverage = 100%” needs a denominator (all current applicable requirements) and a definition of “covered” (accepted relevant evidence), not just a nonempty test link.

## 7. SysML v1, SysML v2, and the underlying engineering method

SysML v1 and v2 support systems modeling but differ in language architecture and representation. SysML v2 is based on KerML and includes textual as well as graphical syntax, with a standardized model API ecosystem. OMG's [SysML v2 specification](https://www.omg.org/spec/SysML/2.0) and [SysML v2 overview](https://www.omg.org/sysml/SysML-2.htm) are the proper sources for **actual language syntax, semantics and conformance requirements**. This chapter intentionally does not present unverified pseudo-SysML as code readers can paste into a conformant tool.

A stable engineering practice should specify the **modeling purpose, viewpoint, metamodel, invariants, evidence rules and review workflow** before choosing which graphical view or tool feature to use. Where a tool generates diagrams from model elements, keep the underlying identities and relation types authoritative. A correct rendering is not, by itself, a correct engineering model.

### Safe migration checklist

Before transforming a SysML v1 model to a SysML v2 representation, inventory your stereotypes, profiles, custom relationship semantics, IDs, quantity definitions, opaque constraints, external links, and generated reports. Define semantic equivalence tests for key queries and calculations. Preserve the old baseline for comparison. Migration should be treated like a data and behavior transformation with validation evidence, not merely a graphics conversion.

## 8. Fully guided repository exercise

**Task.** Inspect [model-stale.json](data/model-stale.json). The audit should find accepted result E-ACK bound to obsolete software, and requirement R-ENERGY with no completed evidence. Neither is automatically verified. In [model-corrected.json](data/model-corrected.json), the result is tied to the current build and a test result for R-ENERGY is added. This makes the sample structurally covered under the stated policy.

**Run:**

```bash
python3 code/model_trace_audit.py data/model-stale.json
python3 code/model_trace_audit.py data/model-corrected.json
```

**Expected interpretation.** The first command reports at least one **STALE** and one **MISSING** requirement. The second reports both **COVERED**. A structural pass does **not** prove an instrument was calibrated, a load profile was representative, or an energy model is trustworthy. Those are independent reviews.

**Extension.** Add a new requirement R-NETWORK with an allocation and a test plan but no result. What does the coverage report say? Then change the evidence build to `NS-2.4` without changing the requirement baseline. Explain why a simple link count remains unchanged but the engineering conclusion does not.

## 9. Review criteria and sources

A model review should inspect intended decisions; definition of scope and system boundary; typed relationship glossary; stakeholder/requirement justification; architecture/interface allocation; units and parameter provenance; behavioral exception cases; consistency and coverage query results; configuration identities; test and evidence applicability; and independent challenge of important assumptions.

- [OMG SysML 2.0 specification](https://www.omg.org/spec/SysML/2.0) — normative language and transformations.
- [OMG SysML v2 introduction](https://www.omg.org/sysml/SysML-2.htm) — KerML foundation, textual notation, and API overview.
- [NASA Systems Modeling Handbook](https://standards.nasa.gov/node/3111) — model planning, organization, and generation of engineering artifacts.
- [Book 3, Chapter 4](../B3/chapters/04-requirements-modeling-relationship-semantics-.md), [Book 3, Chapter 8](../B3/chapters/08-values-units-measures-constraints-parametrics.md), [EN.645.631 course](../../C/P1/EN645631.md).
- [Model-language-method-tool reference](../encyclopedia/model-language-method-tool.md), [traceability reference](../encyclopedia/traceability-graph.md).

**Scope note:** The schema, examples, state names and audit policies here are original educational examples, not a normative interpretation of SysML or a vendor-conformant model. The JSON audit is intended to expose reasoning and provenance, not replace a qualified MBSE environment.
