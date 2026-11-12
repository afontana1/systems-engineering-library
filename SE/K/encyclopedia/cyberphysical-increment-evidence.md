# Cyber-physical increments and continuous assurance evidence

**Reference entry · Agile systems engineering, hardware/software integration and DevSecOps**

## Why software deployment speed is not the system release rate

A cyber-physical increment can change control code, sensors, firmware, hardware, communications, operator workflow, training or maintenance procedures. Passing unit tests does not demonstrate safety in the physical environment. Design an incremental release as a controlled experiment with a bounded operational envelope, configuration-specific evidence, a rollback or containment plan, and an accountable decision authority. “Agile” does not waive verification, traceability or independent safety decisions.

An evidence-bearing pipeline has distinct gates: source provenance and review; static analysis and security scanning; deterministic component tests; executable model and interface checks; software-in-the-loop; hardware-in-the-loop; integration/environmental tests; restricted operational trial; independent review; deployment authorization; and monitoring. The sequence is tailored to risk and criticality, not all stages automatically required for every change. A gate must identify *what claim it supports* and which untested claims remain open.

## Worked timing acceptance with uncertainty

Suppose a hypothetical safety interlock has a requirement to respond within 150 ms. A lab measures 142 ms, but the timing method's stated expanded uncertainty/allowance is 12 ms under the test configuration. Under a conservative one-sided guard-band rule, the acceptance bound is

\[
142+12=154\ \mathrm{ms}>150\ \mathrm{ms}.
\]

Thus the observation **does not pass this rule**, even though the central measured value is below the limit. This calculation is not a statistically justified confidence interval without an uncertainty model and coverage statement. A different customer-approved decision rule may exist; the point is to document it before examining the result. Physical worst-case latency also depends on sensor sampling, scheduler, network jitter, actuator delay and operating temperature.

## Versioned evidence manifest

Record `requirement_id`, `hazard_id`, `source_commit`, `binary_digest`, `firmware`, `hardware_revision`, `calibration_id`, `test_procedure_version`, `environment`, `time`, `raw_data_hash`, `decision_rule`, `reviewer`, `result`, `known_exclusions`. A software commit alone is insufficient: a test on prototype sensor board H1 may not qualify production board H2. The model and experiment need clear configuration attribution. When a hardware configuration changes, evaluate affected assumptions rather than automatically carrying over all earlier acceptance claims.

A red-team or fault-injection trial should attempt invalid modes: link loss during braking, sensor stale data, conflicting operator commands, bypassed authentication, interrupted firmware update, and fallback-mode transition. Define what failure containment should look like. If deployment monitoring indicates violation, the rollback procedure must remain safe even when automated connectivity is lost.

## Exercise and answer direction

The same 150 ms interlock records 132 ms with a 10 ms acceptance allowance. It passes the specified conservative rule (142 ms total) **only for the tested mode and configuration**. Propose evidence needed to extend that decision to cold-start, degraded communications and an aged actuator. Then change the sensor calibration ID; list which tests become potentially stale and why the pipeline cannot decide that from code coverage alone.

## Limits and references

Cyber-physical verification depends on physical fidelity, operator actions and hazards. Security scans identify some classes of defects but cannot certify absence of vulnerabilities. Fast delivery metrics do not substitute for field outcome monitoring. Related: [V&V](v-and-v.md), [software lifecycle evidence](software-lifecycle-evidence.md), [measurement traceability](measurement-traceability-and-calibration.md), [model baselines](../methods/model-baselines-and-evidence.md).

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — secure development practice framework.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — verification planning and configuration control.

*Scope:* Numerical acceptance rule is explicitly hypothetical; safety qualification needs an approved project-specific uncertainty model and procedure.
