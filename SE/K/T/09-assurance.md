# Reliability, hazard controls, and resilience

*Core Concepts · Assurance · T09*

> Reason from failure pathways to layered controls, while acknowledging common causes.

**Recommended preparation:** [Requirements, traceability, and assurance arguments](02-requirements.md), [Uncertainty, statistical evidence, and Bayesian decisions](06-inference.md)

**Related course companions:** [Book 8](../B8/OPEN-BOOK.html), [Book 18](../B18/OPEN-BOOK.html), [Book 20](../B20/OPEN-BOOK.html)

## 1. Reliability is conditional on mission and environment
Component reliability is the probability of performing a specified function for a specified duration under specified conditions. “99.9% reliable” is nearly meaningless without those qualifiers. A shuttle that works on a dry test track may not maintain the same performance in a storm, under sensor contamination, or after years of battery degradation.

For independent components in a series success path, \(R_{series}=\prod_iR_i\). For two truly independent parallel alternatives, \(R_{parallel}=1-(1-R_1)(1-R_2)\). These formulas are simple; the real engineering challenge is defending independence, coverage, and failure detection. Two redundant sensors sharing the same power supply or software defect may fail together.

## 2. Hazard analysis begins with a loss, not a part
A hazard is a system state or condition that, in a particular environment, could contribute to a loss. Identify unacceptable losses first: injury during boarding, unsafe movement after a communication loss, denial of emergency access, or damaging an exposed pedestrian. Then identify unsafe control actions and causal scenarios. This prevents hazard analysis from becoming a checklist of broken components alone.

A control may prevent a hazard, detect its onset, limit its effect, or support recovery. Assess coverage of failure pathways. A reserve battery does not mitigate a software command that sends the wrong vehicle; a duplicate-check does not mitigate a power outage. Controls must match mechanisms.

## 3. Resilience includes graceful degradation and recovery
Traditional reliability focuses on successful performance; resilience also asks how the system absorbs a disturbance, continues essential functions, and recovers. Define degraded operating modes explicitly. If the dispatch network fails, perhaps existing trips continue under local control while new reservations are safely suspended. Measure recovery time, service preserved, and the burden shifted to users or operators.

Treat post-failure human action as a designed interface with workload, training, authority, and time bounds. “The operator will intervene” is not an adequate mitigation without demonstrating the operator can detect, understand, and act under the circumstances.

## 4. Construct a claim–argument–evidence case
A safety case makes a bounded claim supported by reasoning and evidence. The evidence can include test results, analysis, process records, and operational monitoring, but each has limitations. Make assumptions explicit: hardware version, location, user population, and maintenance state. A passed test does not warrant a claim outside its test domain.

A compelling assurance argument identifies counterevidence and open risks. Evidence that a subsystem behaves safely under one isolated fault should not be presented as proof that the entire service is safe under interacting faults.

## 5. Walk a hazard from cause to consequence
Choose the loss *passenger injured by unexpected shuttle movement*. Identify a hazardous system state: vehicle moves while a person is in the boarding envelope. Identify control actions that might create that state: a premature motion command, an ignored boarding sensor, a stale occupancy signal, or an operator override without situational awareness. Then analyze the paths by which these actions could occur and which independent controls prevent, detect, or mitigate each path.

Avoid the tempting shortcut of multiplying low component failure probabilities to produce a tiny loss probability. Such a number is meaningful only if the model covers the relevant scenarios and dependence mechanisms. Software faults, unsafe requirements, common power loss, maintenance errors, and environmental hazards can defeat nominal redundancy assumptions.

Design the degraded mode as a first-class requirement. For example, after losing telemetry, the vehicle might finish a safe stop and refuse new commands while presenting an unambiguous operator alert. The test should include loss onset at several mission stages and should measure both response timing and observable human cues.

**Check your reasoning:** A redundant brake controller improves nominal component availability, but both controllers run identical software and share a power source. It is incorrect to use the independent-parallel formula without accounting for shared failures. The evidence case should state how those common causes are prevented, detected, or bounded.

## Guided worked example

### Worked dependence caution
Two independent backup components each succeed with probability 0.95. Ideal parallel reliability is \(1-0.05^2=0.9975\). If both depend on one power source that is available 0.98 of the time, and the backups are conditionally independent given power, total reliability becomes \(0.98\times0.9975=0.97755\). The shared dependency dominates the benefit of redundancy.

## Independent transfer exercise

Write a fault tree for an unsafe vehicle dispatch, including at least one common cause. Specify a degraded operating mode and two acceptance tests for its recovery behavior.

[Open the companion hypothetical lab](labs/09-assurance-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

Your argument must distinguish fault occurrence, hazard exposure, and actual loss, and include evidence limitations for each proposed control.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.


<!-- STEP04-T1-START -->

## Step 04 T1 — Evidence-driven correction and worked transfer

### T1 audit finding: shared failure defeats an apparently strong redundancy claim

In NS-T4.1 each of two modeled dispatch channels succeeds with probability \(r=0.97\), conditional on the absence of a shared outage. If they were independent without other failure paths, the parallel availability-like success probability would be \(1-(1-r)^2=0.9991\). The case also assumes a common-cause loss probability \(c=0.035\). Conditional independence **only when the shared cause is absent** gives \(P(\text{mission success})=(1-c)[1-(1-r)^2]=0.9641315\), or 96.41315%.

The result is a **synthetic one-mission success probability**, not a measured steady-state availability, an exponential life-model reliability, or a safety-loss rate. The event definition, shared-cause parameter, observation horizon, and diagnostic coverage would require independent justification. Simply multiplying nominal component probabilities would miss the dominant failure path.

**Practice and explained solution.** If the shared-cause probability were zero, the result would be 99.91%. If it rose to 0.05, the result would become \(0.95\times0.9991=0.949145\). A component-level test that does not activate the shared power path cannot establish either result. [Review the evidence chain](labs/T1-INTEGRATED-CASE.md).

<!-- STEP04-T1-END -->
