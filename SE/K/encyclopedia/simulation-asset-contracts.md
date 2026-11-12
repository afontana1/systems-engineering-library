# Simulation asset interoperability and metadata contracts

**Reference entry · MBSE, FMI, HLA, co-simulation and model reuse**

## What “reusable model” means in practice

Reusing a simulation asset is not equivalent to copying its files or linking an XML description. An asset is reusable for a particular decision only when its model semantics, interfaces, initial conditions, solver assumptions, validity domain and provenance can be evaluated by a different team. Separate the **descriptive metadata** (what an asset claims), **executable interface** (what can be connected), and **credibility evidence** (why its outputs may be trusted). A successful file import establishes neither physical correctness nor fitness for use.

A practical manifest records `asset_id`, `source_hash`, `semantic_version`, `units`, `causality`, `coordinate_frame`, `time_basis`, `initialization`, `parameter_set`, `supported_solver_mode`, `communication_step`, `event_policy`, `validity_domain`, `verification_test`, `validation_dataset`, and `owner`. The content of an XML file is meaningful only relative to its declared schema and version. URI or path changes cannot silently be interpreted as semantic equivalence.

## Execution responsibilities and boundaries

FMI specifies interfaces for exchange and execution of models. In **Model Exchange**, the importer controls numerical integration; in **Co-Simulation**, an FMU can advance its internal model while a master/co-simulation algorithm coordinates information exchange. Scheduled execution and clocks introduce additional scheduling semantics. HLA addresses a different integration concern: federated simulation interoperability and time management. Treating these standards as synonyms conceals important design choices. A model may support one interface and not another; inspect the actual implementation and capability flags. See the [FMI 3.0 standard](https://fmi-standard.org/docs/3.0/).

## Worked contract: freshness error

Suppose a vehicle-velocity signal \(v=2\ \mathrm{m/s}\) is sampled every \(\Delta t=0.05\ \mathrm{s}\) and the receiving allocator holds the last sample. If velocity changes between messages, the unobserved traveled distance during one full interval is at most \(v\Delta t=0.10\ \mathrm m\) **under the assumed constant-speed upper bound**, excluding network delay and clock error. The result is a conditional geometric bound, not an assurance of obstacle clearance. Add 0.08 s of worst-case network delay and a motion bound of 2 m/s: the combined staleness distance could be \(2(0.05+0.08)=0.26\ \mathrm m\). A requirement on message period alone will not ensure freshness if delivery is delayed.

A co-simulation test should inject delayed, out-of-order, duplicated and missing messages; compare trajectories across at least two communication steps; check initial conditions; and verify interpolation or zero-order-hold assumptions. If two FMUs form a direct algebraic loop, a simple one-pass exchange might give an inconsistent solution even with perfectly named ports.

## A reusable-asset acceptance gate

Before approving an asset: (1) verify checksum and source license; (2) load exact schema/version; (3) validate units and signal causality; (4) reproduce a reference trajectory with tolerances; (5) test unsupported parameters and delayed-message cases; (6) assess physical validation against the target context; (7) record which configuration approved the asset. Put an explicit **not suitable for** statement in the manifest—e.g. no collision-safety decisions or operation outside 0–20°C—rather than silently relying on institutional memory.

## Exercise and solution outline

A velocity provider updates every 100 ms but a recipient assumes a 20 ms update. At 3 m/s, potential motion between samples is 0.30 m, not 0.06 m; state which additional delay and acceleration assumptions must be bounded to make that meaningful. Inspect a fictitious manifest with no coordinate frame or clock declaration and enumerate why its ports cannot safely be connected. The correct action is to reject or qualify the connection, not infer the missing semantics.

## References and limitations

- [Functional Mock-up Interface v3.0](https://fmi-standard.org/docs/3.0/) — formal interface semantics, capabilities and execution modes.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — configuration management, modeling and technical-data expectations.

Related: [digital thread](digital-thread-and-twin.md), [model queries](model-queries-and-validation.md), [model credibility](model-vv-and-credibility.md). This is an interoperability **engineering method**, not a conformance test for FMI, HLA or XML schema implementations.
