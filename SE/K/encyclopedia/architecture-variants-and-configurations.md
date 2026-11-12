# Architecture variants, product lines, and configuration identity

**Reference entry · System architecture and software engineering · Worked technical treatment**

## One architecture, many possible systems

A **variant** is a deliberately selected design alternative or configuration option. A **configuration** identifies a particular set of component, interface, software, parameter, and evidence versions. A **product line** uses an explicit feature model to derive allowable variant combinations from a shared architecture. Without a configuration identity, comparisons of tests, costs, hazards, and performance become ambiguous.

In the Campus Mobility example, the dispatcher can use a `central` or `distributed` control strategy; vehicles can contain a `standard` or `extended` battery; and a safety monitor is either `primary` or `primary+independent`. If each option were independent, \(2^3=8\) combinations would exist. But not every combination is necessarily permitted. A feature model makes legal combinations explicit rather than relying on informal team memory.

## Constraints define the feasible family

Suppose distributed control requires the independent safety monitor. Write the Boolean constraint

\[
\text{distributed}\Rightarrow\text{independentMonitor}.
\]

Of the eight nominal combinations, two violate this implication (distributed plus primary-only monitor, for either battery). Exactly six configurations remain in this simplified design space. This count is a **combinatorial model result**, not evidence of field compatibility, cybersecurity adequacy, or safety certification.

An architecture rule should be tested in both directions: assert that a compliant distributed/independent variant is admitted, and that a forbidden distributed/primary-only variant is rejected. If the legal combinations are generated automatically, retain the feature-model version that produced them.

## From product-line selection to controlled evidence

Represent a delivered configuration as a versioned tuple such as `(dispatch=distributed@2.1, battery=extended@1.4, safetyMonitor=independent@3.0, interface=ICD-07, evidenceSet=EV-B2)`. A passing test on a central-dispatch build does not automatically verify the distributed variant. The verification matrix should state which characteristics are invariant across variants, which results can be reused by justified similarity, and which require fresh evidence.

A variant comparison table should include: architecture features, system mode, applicable requirements, interface versions, safety controls, power/thermal limits, integration cost, test coverage, and unresolved risks. This prevents an attractive performance improvement from concealing an untested configuration transition.

## Variants versus operational states

An operational mode (normal, degraded, maintenance) is not necessarily a product variant. The same physical system may transition between modes. Conversely, a hardware variant can affect the legal modes and safety invariants. Confusing the two can make a transition model appear to approve a combination that cannot be assembled, deployed, or maintained.

## Worked reliability caution

If two independent monitors each have \(P(\text{failure on demand})=0.02\), a simple AND gate gives \(0.02^2=0.0004\). This calculation assumes independence and identical relevant failure definitions. A shared power supply or common software defect can defeat that assumption; the actual risk can be much higher. Selecting a redundant variant on the basis of the unqualified number would be unsound. See [common-cause fault-tree analysis](../methods/safety-fault-trees-and-assurance.md).

## Engineering exercise and common pitfalls

Enumerate the six legal feature combinations, then introduce a rule that the extended battery requires the new power interface. How many are still legal? State the feature vocabulary and count them explicitly, then decide what verification needs to be repeated. Common mistakes include unversioned feature flags, assuming all combinations are tested because each feature was tested once, conflating design-time features with run-time modes, and treating a configuration-management record as proof of system compatibility.

## Sources and connections

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — technical baselines, integration and V&V in context.
- [NASA Systems Modeling Handbook](https://standards.nasa.gov/node/3111) — structured relationships supporting engineering products.
- Related: [functional, logical and physical architectures](functional-vs-physical.md); [configuration assurance](configuration-assurance-and-change-control.md); [interface control](interface-control.md).

*Scope:* All features, versions, reliability numbers and configurations here are illustrative.

**Reproducible companion:** [Step 02 worked examples (standard-library Python)](examples/step02_examples.py). Run `python3 step02_examples.py --case all` from the downloaded examples folder; the program prints the declared synthetic inputs and computed results.
