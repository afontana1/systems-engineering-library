
---

## Step 04 advanced integration — a rebuttable release argument (NS-AA4.1)

### A1. Assemble the actual claim/evidence table

A candidate claim in the [NS-AA4.1 input register](../data/advanced-case.json) is: *the `rev2` dispatcher is ready for the stated Northstar emergency-dispatch exercise under its declared service, timing, reliability, route-safety and authority constraints*. The evidence set contains nominal service tests, an older route-interface smoke result, a deterministic latency budget, and a simplified two-channel reliability calculation. The following are **separate defeaters**, not five votes that can be averaged:

| Evidence topic | Mechanical result | Defeater or boundary |
|---|---:|---|
| All-request timely fulfillment | 43/50 = 86% guarded | Below the invented 90% threshold |
| Accessible timely fulfillment | 10/12 = 83.33% guarded | Below the invented 85% threshold |
| Sequential latency | 6.7 s worst-case bound | Passes only without omitted shared stalls |
| Two-channel reliability | 0.967575 modeled | Below the invented 0.97 threshold |
| Route-status evidence | `E-ROUTE` at `rev1` | Stale for the `rev2` target interface |
| Operational permissions | All explicitly absent | No operator, safety, or stakeholder authority |

The [executable case evaluator](../code/advanced_case.py) reports these failures individually. It **never produces a field-ready decision**, including for hypothetically green mechanical inputs. Mechanical pass conditions are necessary information but not authorization, representativeness, or validation. The correct status is **HOLD**.

### A2. Separate aleatory and epistemic uncertainty

The repeated-trip uncertainty represented by a stochastic demand model would be *aleatory* only after that model was defended. Unknown route-provider behavior, uncalibrated timestamp accuracy, omitted common faults, and unclear stakeholder consent are *epistemic* gaps: more simulations of the same imperfect model do not close them. An evidence plan must state what observation or review could resolve each gap. For example, clock calibration could justify a smaller guard band, but cannot by itself validate population fairness. New interface tests could restore `rev2` applicability, but do not infer operator authorization.

For failure-rate illustration, zero failures in \(n\) independent identical Bernoulli trials supports the one-sided confidence bound \(p_U=1-\alpha^{1/n}\). At 95% confidence with \(n=30\), \(p_U=1-0.05^{1/30}\approx0.09503\). This bound concerns a *specified trial population*. A campaign containing only favorable open-road tests offers no defensible estimate of failures during simultaneous loss of communications and accessible capacity. A confidence bound is not a posterior probability that a system is safe.

### A3. Change-impact closure and adverse evidence

The route interface has advanced to version 2.0. A disciplined change-impact record lists changed message fields, revised timeout semantics, affected dispatch guards, impacted requirements, required adverse tests, and evidence links that require requalification. Retain `E-ROUTE` as historical evidence rather than deleting or relabeling it; an auditable rejected result is useful evidence of engineering process integrity.

A common but invalid argument says: *the graph is complete, the service test is marked PASS, and the average latency is under budget; therefore deploy.* Each premise is too weak for the conclusion. The guard-band counterexample refutes the unqualified service assertion, the shared-cause result refutes the reliability target, and the configuration mismatch breaks evidentiary inheritance. No aggregation of favorable test counts can authorize activities whose permissions are absent.

### A4. Evidence closure plan and review questions

For a bounded next experiment, require a calibrated timing system and declared measurement adjudication, an accessible-service acceptance protocol agreed with affected stakeholders, a revised interface contract with negative and stale-status test cases, a defensible common-cause model, and signed operational responsibility. Record each as `OPEN` until independent evidence supports closure. Run the modified checker against the exact proposed release hash; preserve the old `rev1` artifacts for reproducibility. Ask reviewers to build the strongest countercase and list **what observation would overturn their objection**.

**Exercise.** Assume new synthetic trials yield 300 no-failure runs, but all use the old `rev1` route service. May the `rev2` route requirement be declared verified? **Worked solution:** no. The numerical zero-failure bound would be \(1-0.05^{1/300}\approx0.00994\) under its own assumptions; it does not establish configuration applicability, scenario representativeness, or approved operation. Retest or formally justify revision equivalence independently.

**Reproduce:** run `python3 SE/K/A/code/advanced_case.py`, examine `evidence_findings` and `screen_failures`, and then run `python3 -m unittest discover -s SE/K/A/code -p 'test_*.py'`. The code is a deliberately simplified educational validator, not a SysML v2 implementation, formal model checker, accredited simulator, or safety certification authority.
