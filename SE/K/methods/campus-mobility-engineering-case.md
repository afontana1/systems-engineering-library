# Connected engineering case: Campus Mobility release CM-B2

*Longitudinal case study · Phase 4 · From stakeholder need to architecture, trade, hazard control, evidence, and release decision*

The library's subjects are usually taught through separate courses. A systems engineer, however, must make their assumptions and results agree **across those boundaries**. This case gives one deliberately small, internally connected example. It provides source data, explicit relationships, calculations, a controlled model change, review questions, and an honest unresolved-issues register. It is a **fictional teaching case**, not a project design approval.

## 1. Mission context and stakeholder needs

The Campus Mobility program considers a small supervised, low-speed shuttle on a fenced test route. Its participants include riders, attendants, fleet dispatchers, maintainers, safety reviewers, and the local operational authority. The immediate experiment is limited to dry-surface demonstrations under supervision. Future public operation is outside the stated intended use.

Two stakeholder needs are intentionally different:

- **NEED-ACCESS:** riders should be able to board and alight without exposure to a moving vehicle.
- **NEED-RELIABLE-SERVICE:** attendants should receive timely acknowledgement when a supervised dispatch request is accepted.

These needs become requirements only after the team states conditions, boundaries, observable measures, authority and acceptance methods. “Safe boarding” and “fast dispatch” are not by themselves measurable design requirements.

## 2. Derive operational requirements and acceptance conditions

| ID | Verifiable statement for the pilot | Allocated owner | Evidence type |
|---|---|---|---|
| REQ-DOOR | Inhibit open-door authorization unless indicated speed is at most 0.5 m/s **and** the parking brake is engaged | Door controller | Fault-injection functional test plus safety review |
| REQ-ACK | Acknowledge an accepted supervised dispatch request within 2.0 s under a specified test load | Dispatch service | Time-stamped integration test |

The requirements require clarification before real implementation. REQ-DOOR must specify sensor validity and age, speed measurement uncertainty, brake status trust, command/actuator delay, emergency egress and degraded modes. REQ-ACK must specify clock synchronization, load distribution, network conditions, definition of an accepted request and percentile or per-request pass criterion. In the synthetic fixture, EV-ACK reports a maximum observed time of 1.74 s, but no field or statistical guarantee is claimed.

Link each requirement to its originating need, owner, hazard, safety/control mechanism, test procedure, evidence record and configuration. The [traceability fixture](data/campus-mobility-release.json) implements these specific cross-links.

## 3. Logical architecture and interfaces

The minimal logical architecture has four components:

1. **Dispatch service** receives supervised route requests, validates preconditions and returns acknowledgements.
2. **Door controller** issues bounded door authorization commands.
3. **Speed sensor** reports measured vehicle speed with accuracy, timestamp and health status.
4. **Brake-status interface** reports whether the parking brake is engaged and the reading is trustworthy.

The door controller's safety-relevant decision depends on more than two boolean flags. A realistic interface contract would specify units (m/s), timing, sampling interval, age limits, plausible range, fallback on lost communication, calibration, watchdog behavior, and ownership of the interlock. If the measurements are stale, a conservative controller may inhibit opening, but that policy must be designed alongside emergency-exit needs and the actual hazard context.

A minimal decision predicate for authorized normal opening is

\[
\mathrm{allowOpen} = (v_{\mathrm{measured}}\le0.5\,\mathrm{m/s})
\land\mathrm{brakeEngaged}\land\mathrm{speedValid}\land\mathrm{brakeValid}.
\]

The given JSON fixture describes requirements and links; it does not claim to execute or verify this actual vehicle control logic. Formal state models would need transitions for moving, stopping, stopped, emergency and faulted modes, plus temporal properties over sensing and actuation.

## 4. Compare candidate architectures before freezing a design

Consider alternative A, a single speed channel with a brake-status gate; alternative B, duplicated speed sensing but shared power and software; alternative C, independent sensor and power designs with diverse fault handling. These are architectural descriptions, **not** evaluated candidates with measured failure rates. The expected safety benefit of B depends on common causes: duplicate sensors on the same power and processing path may provide far less independence than the diagrams suggest.

A trade study should record candidate constraints, whole-life cost, interface complexity, response latency, maintenance burden, hazard controls, evidence and uncertainty. It is incorrect to select C solely because it sounds safer: specify the decision criteria and derive consequences for the actual mission profile. The existing [Pareto/robust-design guide](pareto-and-robust-design.md) supplies a reproducible numerical trade method; the [Bayesian decision guide](bayesian-decision-handbook.md) explains when information gathering is worth the cost.

## 5. Hazard analysis and a quantitative counterexample

The hazard H-DOOR is defined as a door release while the vehicle is moving. A fault tree for the much narrower *unsafe-open command* uses a common-cause bypass event \(C\), an erroneous command \(A\), and an interlock failure \(B\):

\[
T=C\lor(A\land B).
\]

Assign the hypothetical per-demand event probabilities \(p_C=0.003\), \(p_A=0.02\), and \(p_B=0.01\), with independence assumptions. Then

\[
P(T)=0.003+(1-0.003)(0.02)(0.01)=0.0031994.
\]

Ignoring the common cause would yield 0.0002, about sixteen times smaller. This is **not** the operational probability of a physical injury, real door release or even the complete H-DOOR hazard. It is a sensitivity demonstration for one assumed causal pathway. The [fault-tree chapter](safety-fault-trees-and-assurance.md) derives the logic, cut sets, sensitivities and assurance limitations; the [code](code/fault_tree_assurance.py) reproduces it.

The key lesson is not the result's decimal precision. It is how an unvalidated assumption about dependence can dominate an apparent safety margin. A legitimate release claim requires identifying excluded pathways and defending inputs with evidence.

## 6. Verification plan and what the observations prove

| Claim | Proposed verification | What it cannot establish alone |
|---|---|---|
| REQ-DOOR command gating | Inject moving/stopped conditions and sensor faults; capture authorized outputs and timestamps | Every mechanical release path, shared sensor defects, untested override mode |
| REQ-ACK timing | Instrument accepted requests, measure response under named load and network conditions | Behavior at greater field load, tail reliability, clock validity without calibration |
| Safety controls remain applicable | Link evidence to a specific baseline, software build and relevant interfaces | Hazard inventory completeness, total system safety |

Suppose, separately, a binary response-time objective says no more than 1% of requests may fail under an independent identically distributed test demand model. With **300 failures-free trials**, the exact one-sided 95% Clopper–Pearson upper bound on failure probability is

\[
p_U=1-0.05^{1/300}\approx0.009936.
\]

This is just below 1% *under that binomial sampling model*. The current fixture's solitary maximum timing observation of 1.74 s is **not** a 300-trial data set; do not claim this statistical conclusion from the fixture. Repeated requests can be correlated by environment, software state, shift, network load or operator, requiring a different sampling design or conservative interpretation. See [requirements and verification evidence](requirements-verification-handbook.md).

## 7. Construct the safety and release evidence argument

The top-level qualified claim might read: *In the stated supervised dry-route conditions, CM-B2 incorporates specified door-release controls, and the enumerated test results support the checked aspects of those controls.* This is intentionally narrower than “the shuttle is safe.” Its supporting argument identifies requirements, control allocations, covered failure conditions, test provenance, limitations, unsatisfied assumptions and decision authority.

`EV-DOOR` is a **fictional passing observation** with the explicit limitation “Only injected cases; no common-cause fault demonstration.” `EV-ACK` is a **fictional timing rehearsal** with the limitation that a tail reliability rate has not been established. The JSON schema also includes unresolved questions about the common-cause rate, sensor freshness and operating environment. A release board should retain those open points and decide which require more evidence or operational restrictions. A structural model checker cannot provide that judgment.

## 8. Change CM-B2 into CM-B3 and expose stale evidence

Run the [model audit](code/model_thread_audit.py) against the two fixtures:

```sh
python3 SE/K/methods/code/model_thread_audit.py SE/K/methods/data/campus-mobility-release.json
python3 SE/K/methods/code/model_thread_audit.py SE/K/methods/data/campus-mobility-stale-evidence.json
```

The first command finds no defined structural errors, but emits warnings. The second intentionally fails: the release baseline/build has changed to CM-B3 / `controller-2.4.2`, while EV-DOOR and EV-ACK still cite CM-B2 / `controller-2.4.1`. The four errors are the two stale baselines and two stale builds. Changing evidence labels to make the checks pass would be data corruption, not configuration assurance.

Engineering response: compare the changed components, re-evaluate affected requirement and hazard claims, decide whether an existing procedure still tests the right behavior, collect current evidence as necessary, and document the review/approval basis. **Model consistency is not field verification or safety acceptance.**

## 9. Course-by-course learning route through one case

| Course family | Study task | Deliverable to build |
|---|---|---|
| Foundations, EN.645.662 | Turn needs into verifiable conditions | Requirement rationale, ConOps, acceptance criteria |
| Architecture, EN.645.768 | Allocate controls and identify interface contracts | Context, logical/physical alternatives, interface specification |
| MBSE, EN.645.631 / EN.645.632 | Encode typed relationships, invariants and change effects | Model trace graph and reproducible consistency queries |
| Trade/quantitative, EN.645.784 / EN.645.756 | Compare candidate architectures under dependent risk | Decision model, uncertainty and sensitivity argument |
| Test & evaluation, EN.645.769 | Justify measurements, test design and evidence sufficiency | Controlled verification matrix and discrepancy/limitations record |
| Assurance/resilience, EN.645.764 / EN.645.771 | Challenge hazard controls and common-cause pathways | Hazard log, assurance argument, accepted-risk disposition |

Each row corresponds to existing instructional topics in the course-aligned textbooks. The result is a cumulative technical baseline, not a disconnected exercise invented afresh in each subject.

## 10. Capstone exercises and answer checks

**Exercise 1 — Requirement critique.** Rewrite REQ-DOOR to define valid/stale sensor behavior and a response-time limit. Distinguish the *safety constraint* from the *normal-operation requirement*. An adequate answer states measurable inputs, faults, observables, operating modes and how test evidence can show compliance.

**Exercise 2 — Fault-tree calculation.** Change the common-cause probability to 0.001 with A and B unchanged. The resulting assumed per-demand top-event probability is \(0.0011998\). Explain what additional measured evidence would justify using the new parameter.

**Exercise 3 — Statistical inference.** Prove the upper bound \(1-0.05^{1/300}\) by solving \((1-p_U)^{300}=0.05\). Explain why it is *not* a valid inference from a single synthetic maximum of 1.74 s.

**Exercise 4 — Model-change audit.** Predict the four errors in CM-B3, run the checker and identify at least two other changes (sensor timing, requirement limit, environment) that could invalidate evidence *even without* changing a build string.

**Exercise 5 — Assurance review.** Write a claim–argument–evidence tree with at least two explicit defeaters, a restricted intended use, an unresolved hazard item, and a separate reviewer/acceptance authority. A good answer does not issue a blanket “safe” or “certified” verdict.

## Next step: inspect the controlled engineering artifacts

The [Campus Mobility engineering artifact package](campus-mobility-engineering-artifacts.md) provides editable requirements, an interface-control extract, a verification matrix, a hazard register and a configuration-change impact record. These are tied to the same synthetic CM-B2 release and are suitable for cross-course critique. The package deliberately preserves the open evidence gaps rather than asserting a fictional release approval.

## 11. Materials and source references

- [Case baseline JSON](data/campus-mobility-release.json) and [changed baseline](data/campus-mobility-stale-evidence.json).
- [Fault-tree analysis code](code/fault_tree_assurance.py) and [model trace audit code](code/model_thread_audit.py).
- [Safety/fault-tree technical reference](safety-fault-trees-and-assurance.md), [model baseline and evidence reference](model-baselines-and-evidence.md), [reliability](reliability-and-censored-evidence.md), [robust trades](pareto-and-robust-design.md) and [verification/acceptance](requirements-verification-handbook.md).
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/); [NASA-STD-8719.13C with Change 2](https://standards.nasa.gov/sites/default/files/standards/NASA/C-Change-2/0/nasa-std-871913c_with_change_2_0.pdf); [OMG SysML v2](https://www.omg.org/spec/SysML/2.0).

*Use boundary:* This is educational fiction. No numbers describe a real vehicle, safety case, conformity assessment, certified model, or operational release.
