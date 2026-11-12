# Safety engineering: fault trees, common causes, and assurance arguments

*Technical reference · Phase 4 · Failure logic, assumptions, control evidence, and release claims*

**The engineering question.** A design has redundant safeguards and passing component tests. Can its system-level safety claim be defended? This chapter shows why identifying hazards, modeling causal combinations, checking dependencies, and building an evidence argument are different—and mutually necessary—activities. It develops a complete numerical example using a fictional Campus Mobility door controller. All event probabilities are **invented teaching assumptions**, not observed rates or a safety certification.

**Prerequisites:** [System safety and hazards](../encyclopedia/system-safety-and-hazards.md), [reliability and maintainability](../encyclopedia/reliability-availability-maintainability.md), [assurance cases](../encyclopedia/assurance-cases-and-evidence.md), [probability and dependence](../encyclopedia/probability-and-dependence.md).

## 1. Start with loss, hazard, and safety constraint

A *loss* is an unacceptable consequence such as injury. A *hazard* is a system condition which, with a particular environment, can contribute to a loss. A *failure mode* is one way a component or function fails to perform as intended. These are not interchangeable. A component fault can be harmless in one mode, while an unsafe control action can create a hazard without a traditional component failure.

For a supervised shuttle pilot, define loss **L-01** as a person being exposed to vehicle motion during boarding. Define hazard **H-DOOR** as a door being released while the vehicle is moving. Derive the safety constraint **SC-01:** the door controller shall inhibit open-door authorization unless measured speed is at most 0.5 m/s **and** the parking brake is engaged. Record assumptions about sensor freshness, response latency, brake status, command authorization, and whether an emergency egress exception is required. The numerical threshold is a fictional training choice; a real safety case would justify it through hazard and human-factors analysis.

This sequence is *loss → hazardous condition → necessary control constraint → allocated design behavior → verification evidence*. Beginning only with a list of failing components misses interactions and normal actions issued in an unsafe context.

| Artifact | Fictional example | Why it is distinct |
|---|---|---|
| Loss | L-01: exposure to moving vehicle at a doorway | An outcome unacceptable to stakeholders |
| Hazard | H-DOOR: door released during motion | A system-level condition contributing to the loss |
| Safety constraint | SC-01: speed and brake conditions must hold | A boundary on permissible behavior |
| Control | CTRL-DOOR: inhibit unsafe authorizations | An allocated design mechanism |
| Verification claim | Door authorization is withheld under injected motion-state faults | An observable property of one baseline and test environment |

A good hazard log also records operating mode, causal scenario, severity, exposure, controls, verification status, owners, open assumptions, and authority for residual-risk decisions. A high-severity hazard must not disappear into an averaged risk score.

## 2. FMEA and fault trees answer different questions

**Failure Modes and Effects Analysis (FMEA)** works from items or functions toward local and higher-level effects: *if this input is stuck high, what changes?* It is helpful for systematic failure discovery and design actions, but it can omit unsafe interactions where no item has failed. **Fault Tree Analysis (FTA)** begins with a defined top event and decomposes combinations sufficient to cause it: *what events could produce unauthorized opening?*

A simplified illustrative fault tree for the **unsafe-open command** is

\[
T = C \lor (A \land B),
\]

where \(C\) is a shared state/common-cause fault that bypasses the intended safeguards, \(A\) is an erroneous open command, and \(B\) is failure of the independent interlock to block it. This tree models a *command-path event* per door-open demand; it does **not** model every physical pathway to a door opening while moving. Mechanical release, maintenance bypass, emergency override, stale-speed indication and malicious action would need separately justified branches or exclusions.

The two **minimal cut sets** are \(\{C\}\) and \(\{A,B\}\). A minimal cut set is a smallest combination of basic events that suffices for the top event in the proposed logic. It is not automatically the most likely cause, nor does its discovery prove that the tree is complete.

## 3. Derive the top-event probability without hiding assumptions

Assume event probabilities **per demand** of \(P(C)=0.003\), \(P(A)=0.02\), and \(P(B)=0.01\). Further assume the three basic events are statistically independent, their definitions are unambiguous, and each demand is a comparable opportunity. Then

\[
\begin{aligned}
P(T)&=P(C)+P(A\cap B\cap\neg C)\\
&=p_C+(1-p_C)p_Ap_B\\
&=0.003+(0.997)(0.02)(0.01)=0.0031994.
\end{aligned}
\]

This is **0.31994% per modeled demand**, *conditional on the invented event probabilities and exact tree*. If one omits the common-cause branch, the result is \(0.02\times0.01=0.0002\), or 0.02% per demand: an underestimate by a factor of about 16. A value such as 0.31994% must not be presented as the real-world probability of an injury or released door. It refers only to the tree's top event under assumed inputs.

The [executable fault-tree calculator](code/fault_tree_assurance.py) reads the [case baseline](data/campus-mobility-release.json), enumerates mutually exclusive basic-event states, computes the union probability, and reports minimal cut sets. Unlike the shortcut of multiplying each gate's output as independent, assignment enumeration handles reuse of a basic event at several places in a small fault tree. It scales exponentially and is intentionally limited to 16 basic events. It does **not** infer rates from field data.

Run from the repository root:

```sh
python3 SE/K/methods/code/fault_tree_assurance.py
```

Expected top-event probability: `0.0031994`; cut sets: `['common_cause']`, `['command_error','interlock_failure']`.

## 4. Why redundancy is not the same as independence

Two channels with independent failure probabilities \(q_1,q_2\) may have a joint unavailability \(q_1q_2\) under the correct *independent joint-failure* model. The calculation fails if they rely on the same software build, speed source, power supply, calibration procedure, operator, or environmental protection. A shared sensor may make two ostensibly separate control channels fail together.

An engineering review should therefore construct a *dependency inventory*: common sensors, power, communications, timing sources, human actions, update procedures, maintenance tooling, and shared requirements errors. It should ask whether the assumed joint distribution is substantiated by tests, physics-of-failure analysis, operational observations, or justified conservative bounds. **Fault-tree logic alone does not establish input independence.**

Sensitivity identifies where assumption work is worth investing. In the specific tree,

\[
\frac{\partial P(T)}{\partial p_C}=1-p_Ap_B=0.9998,
\quad
\frac{\partial P(T)}{\partial p_A}=(1-p_C)p_B=0.00997,
\quad
\frac{\partial P(T)}{\partial p_B}=(1-p_C)p_A=0.01994.
\]

Around these *illustrative* values, the modeled risk is much more sensitive to a one-unit change in the common-cause probability than to an equal absolute change in either individual-channel failure probability. Reducing the assumed common-cause probability tenfold to 0.0003, without modifying the other inputs, gives \(0.0003+0.9997(0.0002)=0.00049994\). That change is a *scenario analysis*, not a measured safety improvement.

## 5. Quantitative and qualitative safety arguments complement each other

Quantification is useful only when both the event logic and the probabilities have defensible interpretations. In systems with adaptive software, novel interactions or little operational exposure, an unjustified decimal probability can create false confidence. Consider alongside the fault tree: an FMEA; scenarios of unsafe control actions; timing and transition analysis; misuse or degraded-mode cases; interface and human-factors reviews; and fault-injection evidence. System-Theoretic Process Analysis (STPA) is a different causal-constraint method, not a numeric variant of FTA.

For a controller, a fault injection that proves a specific stuck-at-speed signal is detected establishes a bounded finding. It does not establish that the controller handles stale data, counter overflow, software timing races, all human override paths, or combinations with a simultaneous brake-sensor failure. Create an explicit *assurance gap register* instead of silently filling these gaps with optimistic interpretations.

## 6. Build a claim–argument–evidence chain

A structured assurance argument is more than a passing test register:

| Element | Example for Campus Mobility | Potential defeater |
|---|---|---|
| Claim | In pilot baseline CM-B2, unsafe door release is controlled in defined modes | A mode or override path is missing |
| Subclaim | Door command is gated by speed and brake status | Inputs become stale or disagree |
| Strategy | Evaluate hazard paths, implement interlock, test faults, review residual gaps | Shared implementation fault invalidates independence |
| Evidence | EV-DOOR functional fault-injection result, linked to REQ-DOOR and build | Limited cases; no common-cause demonstration |
| Evidence context | Specific firmware, test harness, sensor models and dry-course use | Different vehicle build or environment |
| Disposition | Review open questions and restrict release until adequately resolved | Unresolved high-severity risk accepted without authority |

The [model-thread auditor](code/model_thread_audit.py) checks whether the links and evidence belong to the named configuration. Its passing result says **only** that declared structural rules passed; it cannot evaluate whether a test is physically representative, a hazard inventory is complete, or a risk is acceptable.

The assigned organization—not the calculator—must decide whether evidence suffices and whether a planned use is authorized. A formal assurance review would require documented responsibilities, hazard severity criteria, safety analyses, independent challenges appropriate to the consequences, and an approved residual-risk disposition.

## 7. Counterexamples and common mistakes

- **Common cause omitted.** The independence-only shortcut undercounts the modeled top event dramatically in this example.
- **Wrong unit of probability.** A per-demand event probability is not a per-hour failure rate; converting demands into a mission probability requires a defensible demand model and dependence assumptions.
- **Reliability substituted for safety.** A reliable actuator may consistently issue an unsafe command; high availability does not guarantee safe behavior.
- **High RPN treated as mathematically precise.** Severity × occurrence × detection scores are generally ordinal screening aids, not probabilities or cardinal measures of harm.
- **Test coverage treated as assurance.** A passed test does not demonstrate untested operating modes, configuration currency, or independence of evidence sources.
- **No change analysis.** A software update or new speed sensor may invalidate an otherwise well-constructed argument and its prior tests.

## 8. Exercises with checkable answers

**A. Recompute the fault tree.** Change \(p_C\) from 0.003 to 0.001 while keeping \(p_A=0.02\), \(p_B=0.01\). Predict the new modeled event probability before editing the JSON fixture. Answer: \(0.001+0.999(0.0002)=0.0011998\).

**B. Explain a failure of the model.** Suppose both the command source and the interlock share one speed sensor whose output can freeze. Show why the asserted event independence is no longer justified; propose a new basic event or causal dependency and specify the evidence needed to estimate it.

**C. Review evidence.** The functional test passes for build 2.4.1 but the release configuration is changed to build 2.4.2. Identify which claim depends on retesting, what engineering analysis might justify carrying evidence forward, and what the model auditor reports if the evidence record remains stale.

**D. Challenge causal completeness.** List three ways a physical door might release despite no unauthorized *software* open command. Identify the fault tree branches or independent analyses needed before making a physical-door hazard claim.

## 9. Connections to books, curriculum, and sources

- **Read in sequence:** [Reliability evidence and common-cause calculations](reliability-and-censored-evidence.md) → this safety chapter → [verification and acceptance](requirements-verification-handbook.md) → [traceable configuration audit](model-baselines-and-evidence.md) → [connected Campus Mobility case](campus-mobility-engineering-case.md).
- **Course connections:** EN.645.764 (systems security and assurance), EN.645.768 (architecture and controls), EN.645.769 (test evidence), EN.645.771 (resilience and governance).
- **Textbook connections:** [Book 1 ch 10](../B1/chapters/10-failures-and-controls.md), [Book 8 ch 8](../B8/chapters/08-plan-environmental-quality-reliability-maintainability-.md), [Book 7 ch 7](../B7/chapters/07-design-for-reliability-availability-and-maintainability.md).
- **Primary references:** [NASA-STD-8719.13C with Change 2](https://standards.nasa.gov/sites/default/files/standards/NASA/C-Change-2/0/nasa-std-871913c_with_change_2_0.pdf) (system/software safety analysis considerations); [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) (technical lifecycle and assurance context); [NASA Software Safety Guidebook](https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/nasa-gb-871913.pdf) (illustrative top-down fault tree and bottom-up failure modes analysis).

*Editorial scope:* These numerical values, diagrams, and release artifacts are teaching models. An actual safety analysis requires a justified system boundary, detailed physical hazard mechanisms, measured or bounded inputs, competent domain review, and appropriate authorization.
