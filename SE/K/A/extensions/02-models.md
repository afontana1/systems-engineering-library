
---

## Step 04 advanced integration — graph reachability versus applicable evidence (NS-AA4.1)

### A1. Formalize what the typed graph can establish

The [case model](../data/advanced-case.json) contains three high-criticality requirements, three allocated components, three tests, and three evidence nodes. A planned verification path for requirement \(r\) has the form

\[
r\xrightarrow{\mathrm{verifiedBy}}t\xrightarrow{\mathrm{produces}}e,\]

with a separate allocation edge \(r\xrightarrow{\mathrm{allocatedTo}}c\). A simple graph checker can assert the existence of both relationships and check node types. In a finite graph, enumerating the edges is a decidable mechanical task. The model does **not** prove that the component actually implements the requirement, that the test samples relevant hazards, or that the evidence was collected on the proposed configuration.

Define the applicability predicate \(A(e,v,s)=1\) when the evidence record exists, identifies configuration revision \(v\), has `PASS` status, and includes a scenario description \(s\). This is an **administrative screening rule**, not a scientific rule of sufficiency. For a requirement \(r\), the checker seeks an allocated component and a path to at least one applicable evidence record:

\[
\mathrm{Screen}(r,v)=\mathrm{Allocated}(r)\land\exists(t,e)\,[\mathrm{VerifiedBy}(r,t)\land\mathrm{Produces}(t,e)\land A(e,v,s)].
\]

The [executable screening code](../code/advanced_case.py) computes defects for each requirement, but does not equate a complete path with mission readiness.

### A2. Work a version transition, not just a missing-link exercise

At configuration `rev1`, a route-interface smoke test was recorded as `PASS` for `E-ROUTE`. The decision package now targets `rev2`, with the road-status interface changed to version 2.0. The route evidence remains tagged `rev1`; consequently `R-ROUTE` has a complete typed path but fails the applicability screen as `stale-revision`. Its status is **not repaired by renaming its evidence ID** or copying the `PASS` field into a new row. An acceptable requalification path would document interface compatibility, update the test procedure if needed, rerun adverse route-status conditions, attach revision-specific results, and obtain an appropriate review.

A valid reachability graph is a useful change-impact *starting point*. If the change affects a shared time service or an external route provider not represented in the graph, reachability can miss the affected requirement: this is a false negative. If a contract is proven unchanged, reachability can conservatively flag an unaffected result: this is a false positive. Completeness of the dependency model is therefore an independent assumption.

### A3. Counterexample: syntactically green, semantically invalid

In this case `E-TIME` and `E-ACCESS` are recorded `PASS` for `rev2`. Their nominal campaign was evaluated without the declared timestamp guard band. The graph checker returns no structural or revision defects for them; however, the [measurement analysis](01-mission.html) shows both requirements fail under the conservative measurement contract. This is an intentionally constructed **semantic counterexample** to the proposition that passing linked tests establishes system compliance.

A stronger assurance architecture records (i) procedure identity and admissible scenarios, (ii) intended claim and adjudication rule, (iii) provenance hashes and target configuration, (iv) observed data including anomalies, and (v) independent reviewers and unresolved objections. A claim/evidence graph may then help find missing relationships, while human and empirical review decides inferential validity.

**Exercise.** Suppose `E-ROUTE` is copied into a new record labeled `rev2` without rerunning the test. Will the current checker flag a stale revision? **Worked solution:** no; the syntactic screen sees matching strings. The assurance case must therefore require stronger provenance (immutable inputs and test-run identifiers, authorized sign-off, reproducible event logs). This deliberate weakness is part of the teaching case, not a hidden guarantee.

**Reproduce:** inspect `evaluate()['evidence_findings']`, then mutate `case['evidence']['E-ROUTE']['revision']` in a temporary in-memory copy. The result demonstrates what the checker can and cannot detect. Continue to [behavioral transition checks](03-behavior.html).
