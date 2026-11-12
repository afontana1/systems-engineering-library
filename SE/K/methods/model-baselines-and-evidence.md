# Model-based systems engineering: baselines, constraints, and evidence currency

*Technical reference · Phase 4 · Typed links, change-impact analysis, SysML v2 context, and executable consistency rules*

**The engineering question.** What must a model contain so that a change in a requirement, component, or software build identifies the associated analysis and verification results that may no longer be applicable? This guide constructs a small, inspectable digital-thread model, checks it with Python, and explains where the model stops short of actual SysML v2 language conformance or real-world assurance.

**Prerequisites:** [Traceability graph](../encyclopedia/traceability-graph.md), [model language versus method versus tool](../encyclopedia/model-language-method-tool.md), [configuration assurance](../encyclopedia/configuration-assurance-and-change-control.md), and [MBSE semantics](mbse-semantic-modeling-handbook.md).

## 1. What belongs in an engineering model?

A systems model is a representation with explicit *types, relationships, semantics, and constraints* suited to specified purposes. A diagram with labeled rectangles may be understandable but still leave important questions unresolved: Does a line mean *depends on*, *verifies*, *implements*, or *was derived from*? Which configuration does the statement describe? What happens if its target changes?

For the fictional Campus Mobility release, use node types **Need**, **Requirement**, **Component**, **Hazard**, **Control**, **Evidence**, and **Baseline**. The graph includes typed edges:

\[
\mathrm{Need}\xrightarrow{derived\ into}\mathrm{Requirement}
\xrightarrow{allocated\ to}\mathrm{Component},
\]
\[
\mathrm{Requirement}\xrightarrow{addresses}\mathrm{Hazard},\qquad
\mathrm{Requirement}\xrightarrow{verified\ by}\mathrm{Evidence},
\]
\[
\mathrm{Hazard}\xrightarrow{mitigated\ by}\mathrm{Control}
\xrightarrow{supported\ by}\mathrm{Evidence}.
\]

The graph is *typed*: an evidence record is not a substitute for a component; a control is not proof of an effect. Each edge must be interpreted in an engineering ontology, not simply as an undirected hyperlink. A requirement can be structurally linked to a test that is irrelevant or inadequately performed. Traceability checks are necessary but not sufficient for validity.

## 2. Specify invariants rather than counting links

The case has two requirements: REQ-DOOR is allocated to the door controller and traces to hazard H-DOOR; REQ-ACK is allocated to dispatch service and traces to H-DISPATCH. Each requirement has one declared piece of supporting evidence. Define structural rules before writing a script:

1. IDs are unique and references resolve to the expected node type.
2. Each requirement identifies a source need, component allocation, applicable hazard and control, and at least one evidence record.
3. Each hazard names existing controls and each control has a responsible component and traceable evidence.
4. Evidence links back to the requirement it purports to verify and records a result, baseline and build.
5. The evidence baseline/build must match the configuration under review before a *current-evidence* claim is made.

Formally, if \(R\) is the set of requirements and \(E(r)\) the evidence records linked to requirement \(r\), the **link-completeness** predicate is

\[
\forall r\in R:\quad
\mathrm{need}(r)\neq\varnothing\;\land\;
\mathrm{component}(r)\in C\;\land\;E(r)\neq\varnothing.
\]

The stronger but still limited **configuration-currency** predicate is

\[
\forall e\in E_{\mathrm{release}}:\quad
\mathrm{baseline}(e)=\mathrm{baseline}_{\mathrm{release}}
\;\land\;\mathrm{build}(e)=\mathrm{build}_{\mathrm{release}}.
\]

Matching strings establish neither record integrity nor genuine build provenance. An authoritative digital thread additionally needs immutable artifact identifiers, versioned relations, controlled authoring and reviews, a trustworthy configuration registry, and defensible evidence applicability rules.

## 3. A reproducible configuration change

Open the JSON fixture [Campus Mobility release CM-B2](data/campus-mobility-release.json). The record names build `controller-2.4.1` and evidence EV-DOOR and EV-ACK tagged with exactly that build and baseline. The [auditor](code/model_thread_audit.py) uses only Python's standard library and reports two requirements, two hazards and two evidence records with no *structural* errors. It also emits warnings about unresolved verification and model limitations.

```sh
python3 SE/K/methods/code/model_thread_audit.py
```

Next open the [changed baseline CM-B3](data/campus-mobility-stale-evidence.json). Here only the release record has changed to `controller-2.4.2` while the two old results are still attached. The auditor correctly reports four issues: two stale model-baseline references and two stale build references.

```sh
python3 SE/K/methods/code/model_thread_audit.py SE/K/methods/data/campus-mobility-stale-evidence.json
```

That command intentionally exits with a nonzero status. A stale flag must prompt a *technical decision*: which evidence must be repeated, what analytical argument could permit reuse, and what changes to the model, operating conditions or test equipment invalidate comparability? It would be incorrect to silently edit the old evidence labels to match the new build.

The script tests declared graph invariants and simple timing limits. It does not parse SysML, inspect an actual controller binary, verify a cryptographic build hash, evaluate safety risk, or confirm that the evidence was produced by the claimed build. In particular, its positive result is not a safety-release approval.

## 4. Relating the exercise to SysML v2 and KerML

OMG's [SysML v2 specification](https://www.omg.org/spec/SysML/2.0) describes a language with graphical/textual notations and a semantic foundation in [KerML](https://www.omg.org/spec/KerML/1.0). Its separate [Systems Modeling API and Services specification](https://www.omg.org/spec/SystemsModelingAPI/1.0) supports model integration. These are distinct from an engineering *method* and from a specific executable modeling *tool*.

The case's JSON is a deliberately small educational **interchange-like representation**, **not valid SysML v2 textual syntax or an OMG-conformant API payload**. A serious SysML v2 implementation would model parts, requirements, connections, actions and verification cases using the language's actual declared semantics. It would bind model element identifiers to versioned evidence, export or query with a supported implementation, and run a real tool's parser and semantic validation. Do not relabel a JSON consistency audit as a “formal SysML v2 proof.”

A practical migration path is:

| Educational model element | SysML v2 modeling concern | Additional review needed |
|---|---|---|
| `components` | Part/structure definitions and usages | Owner/port/typing semantics and multiplicity |
| `requirements` | Requirement definitions/usages, constraints | Stakeholder context, satisfy/verify relationships and units |
| `hazards` and `controls` | Dedicated engineering profile/metadata and trace links | Safety ontology, causal completeness and owners |
| `evidence` | Verification cases, artifacts and configuration metadata | Test applicability, result provenance and reuse policy |
| `baseline`/`build` | Version-managed model/project and configuration data | Change control, immutable IDs and actual artifact hashes |

To make a future *tool-validated* example, add an actual `.sysml` source based on normative language rules, run a compatible parser/validator in CI, capture tool version and diagnostics, and test representative queries. That step **has not been performed in this release**; it should not be inferred from the passing Python audit.

## 5. Change impact is more than link traversal

Suppose a braking sensor is replaced. The first-order affected set comprises requirements that use it, controls relying on its readings, verification steps using it, interface contracts, and parameterized analyses that assume its accuracy or latency. The transitive impact follows typed dependencies. But edge existence alone does not say *which* results are invalid: for example, one changed display label may not affect a validated timing analysis, whereas a sensor sampling interval change may alter fault detection time.

Use an impact record with **changed property, relevant behavior, affected claims, evidence assumptions, decision on reuse, reviewer, and effective baseline**. A change in a requirement threshold can invalidate evidence even when the tested binary is unchanged. A hardware change can invalidate a software integration test even if software has not been rebuilt. Two records with the same revision label can still differ in content unless integrity is verified.

For consequential engineering, track relation-level and artifact-level provenance: source revision, author, approval, timestamps, calibration, external dependency versions, parameter/units, tool version, code commit, and test article identity. Keep the data minimal where possible, but never omit attributes needed to judge whether a claim applies to the configuration of interest.

## 6. Four ways an apparently complete graph can mislead

**Coverage without relevance.** One `PASS` record is linked to a door requirement but tests only the green dashboard indicator. Structural coverage is 100%; verification relevance is nearly zero.

**Current labels, stale assumptions.** Evidence tags are updated to CM-B3 without rerunning the test or evaluating changed conditions. The checker passes, but the evidence is misrepresented.

**Incorrect risk abstraction.** A common-cause fault is absent from the model because component diagrams emphasize independence. No traceability completeness rule discovers an omitted hazard automatically.

**Semantic ambiguity.** Two teams use `verifies` to mean different things: a test is planned versus passed. Define link properties such as `planned`, `executed`, `accepted`, with criteria, result and scope.

These are reasons to augment model validation with engineering review and evidence challenge, not reasons to abandon traceability.

## 7. Exercises and worked checks

**A. Baseline mismatch:** Explain why CM-B3 fails exactly four currency checks. *Answer:* Both EV-DOOR and EV-ACK cite CM-B2 and build 2.4.1, so each has a mismatched baseline and build; the other declared links still resolve.

**B. Missing allocation:** In a copy of the fixture, rename `dispatch-service` in the `components` list but leave REQ-ACK unchanged. The audit must report a missing allocation for REQ-ACK and an unknown owner for CTRL-TIME. Identify the additional functional or interface tests required after a real architectural reallocation.

**C. Misleading pass:** Replace EV-DOOR with a passing test for an irrelevant user-interface function. Why would the script fail to detect this? Propose a precise evidence-coverage predicate (stimulus, expected observable behavior, operating mode, fault conditions, and requirement acceptance criteria) and the data fields it needs.

**D. SysML tool selection:** Compare a SysML v2 textual model, a model interchange API representation, and the executable JSON exercise. For each, specify its standards conformance requirements and which actual tool diagnostics would substantiate that claim.

## 8. Where this belongs in the curriculum

- EN.645.631 and EN.645.632: model semantics, change-impact queries, verification cases and machine-checkable constraints.
- EN.645.768: trace safety controls into physical/logical architecture and interface responsibilities.
- EN.645.769: check evidence applicability and build-specific release claims.
- [Book 3 ch 11](../B3/chapters/11-model-quality-queries-reports-change-impact-g.md) and [Book 9 ch 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) provide the course-aligned methods.
- Continue to the [safety/fault-tree reference](safety-fault-trees-and-assurance.md) and the [connected case study](campus-mobility-engineering-case.md).

**Primary references:** [OMG SysML v2 specification](https://www.omg.org/spec/SysML/2.0), [OMG Systems Modeling API and Services specification](https://www.omg.org/spec/SystemsModelingAPI/1.0), [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/).
