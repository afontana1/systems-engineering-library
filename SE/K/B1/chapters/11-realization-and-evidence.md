# Chapter 11 — From a Plausible Concept to Reviewable Evidence

*EN.645.662 · Week 11. Prepares the original Concept Review and [Hypothetical Lab 11](../labs/lab-11-verification-board.md).*

## The prototype worked; what exactly did that establish?

The Northstar team demonstrates a shuttle booking screen, a dispatch algorithm, and a virtual vehicle that follows an assigned route. The demo succeeds. Does this mean the concept can be built, integrated, accepted, and operated? Not yet. The demonstration proves only a bounded claim about a particular configuration under particular conditions. Systems engineering must create a chain of increasingly credible evidence from design assumptions to product realization and operational value.

A **realization strategy** explains how system elements will be acquired or developed, integrated, checked, transitioned, sustained, and retired. Early design need not know every manufacturing detail, but it must reveal enabling products and the dependencies that can invalidate the concept. In the shuttle case, these include the software build environment, a telemetry test rig, accessible stops, charging and maintenance facilities, operator training, cybersecurity monitoring, and incident procedures.

## 11.1 Four questions that sound similar but are not

**Verification:** Does the specified product conform to the applicable requirement? A test may establish that an interface rejects stale telemetry under a declared test profile.

**Validation:** Does the system in its intended context satisfy stakeholder needs? An accessible vehicle-level boarding motion may pass verification, while a real rider cannot use a particular stop. Validation requires the intended use and users to be represented appropriately.

**Qualification:** Does a design or item meet a defined set of conditions for a specified use, often including environmental or safety stresses? The required qualification basis depends on domain and authority.

**Acceptance:** Does a designated customer or authority accept delivery under agreed contractual or organizational criteria? Acceptance is a governance act supported by technical evidence, not synonymous with validation or qualification. **Certification** is yet another distinct formal decision when required by a competent authority; a self-study review cannot grant it.

These categories can share test data, but their purposes and evidence bases are different. An engineering team should label claims precisely so that a passing narrow test is not silently expanded into global approval.

## 11.2 Integration strategy is a hypothesis about risk

Choose an integration sequence that reveals important failures early and isolates them efficiently. For Northstar, start with message-contract tests using simulated clients. Add the dispatch state machine and simulated vehicle gateway. Inject late, duplicated, malformed, and missing telemetry. Then integrate operator workflows and accessible-service scenarios. Only after corresponding gates are met would higher-fidelity hardware, human-in-the-loop testing, or authorized field trials be considered.

Each integration stage needs explicit **entry criteria** (required configurations, interface versions, calibrated tools, hazard mitigations) and **exit criteria** (tests, evidence sufficiency, unresolved finding policy). A green aggregate test count is not enough. A single critical interface deficiency may preclude progression even if hundreds of unrelated checks pass.

A common mistake is integrating by organizational convenience: “we'll test the whole system once every team finishes.” That postpones discovery of mismatched semantics and makes failures hard to diagnose. Progressive integration deliberately discovers uncertainty while preserving attribution.

## 11.3 Design tests to support exact requirements

Consider `R-TEL-03`: *When authorizing an assignment under the defined simulated operational profile, dispatch shall not rely on vehicle-readiness measurements older than five seconds.* A useful verification plan states the **configuration**, stimulus, input measurement age, expected outcome, logs and clocks, instrumentation, test repetitions, and the handling of borderline values. Use ages 4.9, 5.0, and 5.1 seconds (subject to the rule's precise inclusive boundary) as *boundary-value tests*.

Do not write “Test: telemetry works.” A well-designed procedure states what would falsify the requirement. For example, if the contract is “not older than five seconds,” a 5.0-second sample is permissible while a 5.1-second sample must be rejected under exact, ideal timestamp semantics. Real clock uncertainty may require guard bands or a different acceptance policy, so the simplified result is not a field safety claim.

**Verification methods** include test, analysis, inspection, and demonstration. The appropriate choice depends on the requirement and the claim. Model-based analysis can support a limited performance prediction, but its validity depends on credible assumptions and representative data; a simulation result cannot independently establish behavior omitted from the model.

## 11.4 Evidence provenance is part of evidence quality

Every recorded result should answer: which requirement, test procedure, configuration, data source, tool version, execution date, environment, operator, and decision rule produced this result? If the team cannot reproduce a calculation or locate the model revision, the evidence is difficult to audit. The **traceability matrix** should connect requirements to verification cases, execution results, defects, and closure actions—not just link every requirement to the word “Test.”

Suppose the team has 24 critical requirements. It has planned verification cases for all 24 but actually executed and passed only 18. Its **planned coverage** is 24/24 = 100%; its **passed-execution coverage** is 18/24 = 75%. Neither figure describes the criticality or relevance of the six missing cases. A readiness decision must examine what they concern, the approved policy for open evidence, and whether any are gating.

## 11.5 Validation cannot be reduced to verification coverage

Suppose every technical interface test passes, yet a rider who uses a wheelchair cannot safely navigate the boarding area when another vehicle blocks the curb. The product may conform to interface requirements but fail the operational need. Validation uses stakeholder-oriented scenarios, human-factors observations, operational measures of effectiveness, and appropriate environmental representation. It often uncovers missing requirements; those findings flow back into concept and architecture changes.

Operational transition adds another question: *Can the receiving organization actually operate and sustain this solution?* Training, staffing, maintenance, incident response, spare parts, cyber monitoring, and retirement must be considered. If the operational model assumes human assistance is always available but no staffing plan exists, the concept is not ready for that assumption to be trusted.

### Verification and validation make different kinds of assertions

Verification asks whether a specified claim about an artifact is supported under stated conditions. Validation asks whether the selected claims and system are appropriate for the intended use. A braking interface may pass its latency test and still be unsuitable because the latency requirement omitted a realistic degraded mode. That is not a contradiction: the interface can be verified against the specification while the specification itself is invalid for the mission.

Evidence acquires meaning from its **configuration and context**. A test result without an identified build, procedure, environment, acceptance rule, and observed outcome is a story, not a reconstructable claim. Nor does an impressive test count guarantee relevance: a thousand nominal runs cannot substitute for evaluating a rare but important transition. The evidence argument should expose a chain from stakeholder outcome to requirement, allocated behavior, test condition, result, and limitation. The remaining uncertainty then becomes a subject of explicit technical judgment rather than a footnote concealed by a green status indicator.

## 11.6 Practice and worked answers

**A. Classify.** A supplier demonstrates that a door actuator moves in 20 seconds. **Answer:** Potential verification of a device-level timing requirement, not validation of accessible boarding in the operational context.

**B. Compute.** Cases are planned for 24 critical requirements; only 18 have passed. **Answer:** Planned coverage 100%, passed-execution coverage 75%, with six critical claims still lacking passed execution evidence. Check their gates and causes.

**C. Boundary test.** The rule rejects measurements older than five seconds. What should happen at 5.1 seconds? **Answer:** Reject under the exact simplified semantics; field clock uncertainty requires further design and testing.

**D. Evidence.** A result is labeled “pass” without software revision or test profile. **Answer:** Its applicability is uncertain; record provenance before treating it as authoritative.

**E. Transition.** Why include maintenance and operator training in the concept? **Answer:** These enabling systems determine whether the mission can be sustained, even if the core technical product initially works.


## Deeper theory: realization evidence as a structured assurance argument

### A delivered system and an accepted claim are different objects

Realization takes an intended architecture into manufactured, configured, installed, and operated instances. Every instance depends on a controlled configuration: software revision, hardware serial range, parameter set, external interfaces, installation instructions, and operating procedures. A successful demonstration of one configuration is evidence about that configuration and those test conditions. It is not a universal statement about every fielded instance. The meaning of “the system passed” must therefore be narrowed to a claim, the relevant configuration, an operational domain, and the evidence available when the decision was made.

An assurance argument links a top-level claim to supporting claims by explicit reasoning. For example, “the shuttle can board riders safely under approved operating conditions” may require evidence for door-force limits, interlock behavior, obstacle detection, exception handling, and operator response. Each claim depends on assumptions about terrain, loading, maintenance, weather, and human behavior. A verification matrix records planned checks; an assurance case explains *why* those checks collectively support the particular conclusion. A row marked “pass” has little meaning if the associated measurement, calibration, software build, or deviation record cannot be recovered.

### Evidence strength is conditional and correlated

Suppose two tests both succeed. It is tempting to treat them as independent confirmation, but tests executed on the same simulator, using the same invalid sensor model, can share a common systematic error. Independent-looking evidence is often dependent through tools, requirements interpretation, calibration, or personnel. The probability of at least one hidden defect is not reduced by simply multiplying assumed failure probabilities unless their dependence has been justified. Diversity of test method and failure mode matters more than raw test count. A ground test, analytical bound, and operational trial may provide more complementary evidence than three repetitions of the same script.

A useful acceptance calculation separates *measurement uncertainty* from *engineering margin*. If a force limit is 150 N, a measured maximum of 147 N with expanded measurement uncertainty of ±5 N does not straightforwardly demonstrate compliance under a conservative guard-band rule: the upper plausible value reaches 152 N. The team must apply the documented decision rule rather than silently redefine the measurement or specification. Conversely, a conservative rule can reject some genuinely compliant units; the cost of false acceptance and false rejection should be decided before inspecting the results.

### Failure to demonstrate is not necessarily demonstrated failure

When a test cannot be executed because a facility lacks the required environment, the claim is *unverified under that condition*; it need not be intrinsically false. A genuine failed test is different from missing evidence, an invalid test, or a deviation accepted by formal authority. These distinctions protect technical review from rhetorical inflation. For each open item, record the affected claim, current evidence, root cause or uncertainty, permitted operating restrictions, owner, and a concrete closure criterion. A risk acceptance can authorize limited use, but it cannot transform a missing technical fact into established truth.

The realization gate should consequently ask which mission outcomes are supported, what configurations are covered, what exceptions remain, and what operational monitoring is required after release. An evidence package is a time-stamped decision basis, not a permanent guarantee. Supplier updates, new environments, changed maintenance intervals, or incident data can invalidate an earlier inference and trigger targeted re-verification.

## Read, rehearse, produce

In [Hypothetical Lab 11](../labs/lab-11-verification-board.md), inspect a mixed evidence packet and decide what is actually verified. Then prepare original Week 11 `662_W11_ConceptReview_v1.0`, with integration, V&V, validation, transition, review findings and closure evidence. The assessment gate belongs to the original course, not the fictional review board.

**Next:** [Chapter 12 — Synthesis and defense](12-synthesis-and-defense.md).
