# System safety engineering: hazards, controls, and residual risk

**Canonical reference · Safety and assurance · Expanded reference · Internal editorial review; independent peer review not performed**

## Definition and scope

**System safety engineering** identifies, analyzes, and controls conditions that can lead to unacceptable loss during design, integration, operations, maintenance, and disposal. A *hazard* is a system condition with the potential to contribute to a loss; a *mishap* is the realized harmful event. A failed component is neither necessary nor sufficient for a mishap: incorrect interactions between individually functioning controllers, operators, environments, and interfaces can create hazards. NASA describes system safety as a life-cycle pursuit of acceptable mishap risk using a holistic systems perspective, not a final inspection activity.

Consider a hypothetical autonomous campus shuttle. An unintended motion command is a **hazardous control action** when a passenger is boarding. The harm requires further circumstances, such as a person occupying the swept path and failed intervention. The engineering objective is not merely to calculate how frequently a motor controller fails; it is to show how the combination of control, perception, human action, and environment can or cannot create an unacceptable event.

## Construct a loss-to-control argument

A disciplined analysis begins with (1) losses to be prevented; (2) hazardous system states and interactions; (3) the control constraints required to keep the system out of those states; (4) credible causal scenarios including software logic, sensor ambiguity, common power, maintenance error, and misuse; (5) designs and procedural controls; and (6) evidence that each control actually works under the stated operating envelope. A hazard log tracks severity, exposure, initiating conditions, owners, mitigations, verification evidence, assumptions, and residual decision authority. Revision identifiers are essential: a newly introduced operating mode can invalidate an earlier hazard closure.

Fault-tree analysis works backwards from a specified top event using AND/OR logic. Failure mode and effects analysis usually proceeds forward from element-level failure modes to effects and detection paths. Scenario and control-structure analysis complements both by examining unsafe interactions even when hardware has not failed. No single method guarantees all hazards have been found. Risk matrices are rough prioritization aids; their ordinal categories cannot validly be multiplied into quantitative probabilities without a justified calibration.

## Mathematical reasoning: independence is an explicit claim

Suppose a stop action fails only when *both* the primary controller and an independent emergency channel fail. If their conditional probabilities of failure on a demanded stop are 0.02 and 0.01, the joint failure probability is `0.02 × 0.01 = 0.0002`, **but only if those failures are independent given the defined demand and environment**. Suppose, additionally, a common power fault independently disables both channels on 0.001 of demands. The stop failure probability then becomes `0.001 + (1 − 0.001) × 0.0002 = 0.0011998`, about **0.120% per demand**—nearly six times the naive redundant estimate.

This number is an illustrative conditional *stop-failure* probability, **not** the probability of injuring a passenger. Injury assessment would require the frequency of demands, the presence of people, exposure duration, intervention opportunities, harm severity, and dependencies among them. If the common fault also changes demand frequency or exposure, the simple mixture is insufficient. Sensitivity to unmeasured common causes is often more important than a fourth decimal place.

## Design controls and assurance evidence

Favor prevention through inherently safer geometry, separation and energy limits before depending exclusively on alarms or operator response. Then apply protective interlocks, detection, safe state transitions, inspection, training, and procedures with clear responsibility. A stop controller with a perfect bench test can still fail in the integrated system through an incorrect pin assignment, stale configuration, disabled maintenance interlock, or power-domain coupling. The test argument must identify the exact build, interfaces, faults injected, scenarios exercised, and the limits of extrapolation to actual exposure.

An effective safety case makes a bounded claim: *for a specified configuration and operating domain, identified controls are adequate to keep residual risk within the authorized acceptance basis*. A claim about every possible environment or misuse requires a far stronger argument. Residual risk acceptance is an organizational decision by designated authority; engineering analysts report evidence and uncertainty rather than declaring that a system is universally safe.

## Failure modes, misconceptions, and decision boundary

- **Failure of enumeration:** a fault tree lists component breaks but omits an incorrect command issued by a functioning algorithm.
- **Failure of independence:** nominally redundant channels share power, data, calibration, operating software, or human maintenance.
- **Failure of evidence:** a hazard is marked mitigated because a design was proposed, not because its implemented configuration was verified.
- **Failure of scope:** a safety demonstration excludes degraded states, installation, repairs, environmental exposure, or operator handover.

For a design review, require the hazard-to-control-to-evidence chain, unresolved assumptions, active operating limitations, and explicit residual-risk disposition. Safety assurance has to follow the configuration throughout the life cycle.

## Selected source-to-claim references

- **S1 · System-level and life-cycle hazard reasoning:** [NASA Office of Safety and Mission Assurance, System Safety — definition and methods](https://sma.nasa.gov/sma-disciplines/system-safety). Supports the systems-safety framing, not the illustrative stop probabilities.
- **S2 · Safety activities in software assurance:** [NASA-STD-8739.8B, Software Assurance and Software Safety Standard — document scope](https://standards.nasa.gov/standard/nasa/nasa-std-87398). Supports systematic assurance and IV&V across software life cycle; NASA applicability is project-specific.

## Phase 4 technical reading: A complete hazard-to-control calculation

For a fictional shuttle's unauthorized door-open command, distinguish the loss (rider exposed to motion), hazard (door released while moving), safety constraint (speed and parking-brake conditions), and implementation control. A deliberately small fault tree defines \(T=C\lor(A\land B)\), where \(C\) is a shared-state bypass, \(A\) an incorrect command, and \(B\) an interlock failure. Assuming independent events with per-demand probabilities \(0.003\), \(0.02\), and \(0.01\), respectively, gives \(P(T)=0.003+(1-0.003)(0.02)(0.01)=0.0031994\). Omitting the common cause yields only 0.0002 and materially misstates the conditional model. These invented inputs are not a measured safety probability; the tree covers just one command pathway, not the complete physical hazard. [Work through the fault tree, FMEA distinction, dependencies and evidence claim](../methods/safety-fault-trees-and-assurance.md) and compare the same controlled baseline in the [cross-course case](../methods/campus-mobility-engineering-case.md).



## Step 02 review studio — calculate a shared-cause counterexample

Assume **fictional** per-demand probabilities: common-cause loss of status `0.003`, channel A failure `0.01`, channel B failure `0.02`, with conditional independence of A and B when the common cause is absent. The top event is a common cause OR simultaneous channel failures when no common cause occurred. Its probability is

\[
P(T)=0.003+(1-0.003)(0.01)(0.02)=0.0031994.
\]

A calculation treating the channels as fully independent would return `0.0002`, missing most of the modeled probability. **Solved exercise:** if only channel A improves to 0.005, the new result is `0.003+0.997(0.005)(0.02)=0.0030997`. The improvement is just `0.0000997`, demonstrating why common-cause controls may be more important than polishing an already redundant component.

**Limits:** a fault-tree result is conditional on event definitions, per-demand versus time-based units, dependence assumptions, mission profile, and completeness of the hazard model. Neither illustrative probability is an operational safety target or an authorization. Evidence of control effectiveness and independent acceptance remain separate questions.

## Follow the knowledge

- **Prerequisites:** [Risk versus issue](risk-vs-issue.md), [Probability and dependence](probability-and-dependence.md).
- **Related concepts:** [Reliability, availability, and maintainability](reliability-availability-maintainability.md), [Assurance cases](assurance-cases-and-evidence.md), [Human systems integration](human-systems-integration.md).
- **Go deeper:** [Book 7, Chapter 8 — Humans, safety and security](../B7/chapters/08-design-for-human-performance-safety-security-usability-.md); [Book 18, Chapter 9 — Cascading risk and mission assurance](../B18/chapters/09.md).
