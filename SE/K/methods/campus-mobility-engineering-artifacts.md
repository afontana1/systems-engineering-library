# Campus Mobility: controlled engineering artifact package

## 1. One case, many engineering disciplines

This package develops the fictional Campus Mobility shuttle from the [longitudinal case](campus-mobility-engineering-case.md) into an inspectable **requirements–interfaces–hazards–verification–change** baseline. It is a teaching configuration, not a certified vehicle, a completed safety case, or a release authorization.

Everything is versioned to the **CM-B2** classroom baseline and the synthetic `controller-2.4.1` build. The subsequent CM-B3 change illustrates why accepting a result for one configuration does not automatically support a later configuration. Source files are open CSV/JSON and can be reviewed without specialized tooling.

| Artifact | Editable file | Main question it answers |
|---|---|---|
| Requirement specification | [campus-requirements.csv](data/campus-requirements.csv) | What behavior, conditions and observables define success? |
| Interface control extract | [campus-interfaces.csv](data/campus-interfaces.csv) | Who produces which information, with units and freshness constraints? |
| Verification cross-reference matrix | [campus-verification-matrix.csv](data/campus-verification-matrix.csv) | Which controlled tests and results support which claims? |
| Hazard and assurance register | [campus-hazard-log.csv](data/campus-hazard-log.csv) | Which losses and hazardous states remain incompletely controlled? |
| Configuration change impact | [campus-change-impact.csv](data/campus-change-impact.csv) | Which previous evidence needs re-evaluation after CM-B3? |
| Typed baseline fixture | [campus-mobility-release.json](data/campus-mobility-release.json) | Which IDs, controls, configuration and evidence connect the documents? |
| Changed baseline fixture | [campus-mobility-stale-evidence.json](data/campus-mobility-stale-evidence.json) | Can a checker distinguish stale evidence from current evidence? |
| Model illustration | [campus-mobility.sysml](models/campus-mobility.sysml) | What might the small structural slice look like in SysML textual notation? |

The `.sysml` file is explicitly **not claimed to be validated by a conforming SysML v2 parser**. The CSV/JSON checker validates limited engineering-document relationships, not the language semantics of that file.

## 2. Requirement specification: observable, qualified claims

The original CM-B2 model contains `REQ-DOOR` and `REQ-ACK`. The revised requirements extract makes the tested boundary clearer. `REQ-DOOR` is a positive safety constraint on *authorization*: if measured speed exceeds 0.5 m/s, parking brake is not engaged, or input validity fails, the system must inhibit door authorization. It does not by itself assert mechanical latching under every possible fault. `REQ-ACK` concerns accepted supervised requests within 2.0 s at a declared test load; a single passing maximum observation does not establish a rare-event deadline reliability target.

An important logical distinction is

\[
\mathrm{permitOpen}\Rightarrow
(\mathrm{speedValid}\land\mathrm{brakeValid}\land v\le0.5\;\mathrm{m/s}\land\mathrm{brakeEngaged}),
\]

not the false converse that the door *must* open whenever those conditions hold. This conditional statement must eventually be implemented as an actual controller invariant and supported with adequate evidence. See [requirements engineering and evidence](requirements-verification-handbook.md).

## 3. Interface control: freshness is a technical contract

The interface extract states `IF-SPEED` and `IF-BRAKE` as 50 ms periodic signals with **150 ms maximum allowable age** in this *invented* example. The controller's invalid-input action is `deny_open`. The values are design assumptions, not measured sensor performance, and are not offered as operational standards. The real specification would need message schemas, failure signaling, source identity, message ordering, timestamp basis, reset handling, electrical/network allocation, qualification environmental boundaries and cybersecurity concerns.

If speed is 0.3 m/s but its timestamp is 180 ms old, `IF-SPEED` is invalid. The authorization must remain inhibited despite an otherwise nominal speed/brake combination. A stale input is not evidence of a low-speed state. The test procedure should inject freshness violations, clock skew and contradictory sensor states, not only nominal values.

## 4. Verification matrix: pass reports versus evidence sufficiency

`TEST-DOOR-01` and `TEST-ACK-01` are **synthetic named procedures**, with illustrative passing evidence `EV-DOOR` and `EV-ACK`. The declared limits are crucial: injected software faults cannot establish all mechanical failure pathways, and one observed maximum of 1.74 s is not a confidence bound on the probability of missing the 2.0 s deadline. The matrix deliberately retains these limitations instead of silently converting `PASS` into a broad release claim.

A complete controlled verification record would additionally include instrument calibration, test personnel, timestamp provenance, code/build hashes, input fixtures, deviations, trace to acceptance criteria, raw readings, and independently reviewed disposition. Evidence quality depends on the claim being made, not the number of green status cells.

## 5. Hazard argument: claim, evidence and defeater

For `H-DOOR`, the loss is an injury from door opening while moving. The hazard is the unsafe vehicle state; `CTRL-DOOR` is one control pathway. A useful qualified claim is:

> On CM-B2 under the stated supervised test conditions, the controller's software command gate inhibits opening for the enumerated injected speed/brake test conditions.

Supporting evidence is the synthetic `EV-DOOR` result, with a configuration label and procedure. **Defeaters** include untested common-cause sensor invalidity, mechanical bypass of the command gate and broader operational environments. The hazard therefore remains **OPEN**. The [fault-tree reference](safety-fault-trees-and-assurance.md) explains how an incomplete causal model can understate risk; the [model-baseline reference](model-baselines-and-evidence.md) explains why a valid graph does not close that causal gap.

A decision board should have explicit authority, acceptance criteria, responsibility for open issues, and scope restrictions. The teaching package does not produce a release decision and does not recommend fielding a vehicle.

## 6. Configuration transition: do not relabel evidence

The change `CHG-01` updates the fictitious controller software from `controller-2.4.1` on CM-B2 to `controller-2.4.2` on CM-B3. The change-impact CSV identifies both requirement/evidence pairs as needing review because the illustrative baseline uses a shared build label. This does not mean every software change *always* requires an identical retest, nor that any old evidence is worthless. It means applicability must be established through controlled impact analysis.

An engineering impact workflow is: identify changed sources and dependencies → assess requirement/control implications → select affected tests and review of earlier evidence → collect new data where justified → resolve anomalies and hazards → obtain independent disposition. The [stale-evidence JSON](data/campus-mobility-stale-evidence.json) deliberately triggers errors with the [model audit](code/model_thread_audit.py). Editing the old evidence metadata to a new build without retesting would falsify provenance.

## 7. Run the document consistency checks

Use the two different standard-library educational validators from the project root:

```sh
python3 SE/K/methods/code/sysml_trace_crosswalk.py
python3 SE/K/methods/code/model_thread_audit.py SE/K/methods/data/campus-mobility-release.json
```

The crosswalk checks identifiers and allocation consistency among CSVs and the CM-B2 JSON, verifies that the reported test versions match the baseline, checks supported interface endpoints and checks that unresolved hazards remain open. It does not evaluate actual timing data or safety-critical sufficiency. The model audit checks graph and evidence-currency rules for the controlled baseline. Neither is a normative SysML validator or a field test.

**Negative test:** change `REQ-DOOR`'s allocation to `dispatch-service` in a temporary *copy* of the requirements CSV and run a modified path of the checker; the allocation mismatch is an error. Never rewrite the original baseline files to simulate a passing result. A program that cannot reject a deliberate mismatch is not a useful validation gate.

## 8. Course-specific extensions

| Course | Further deliverable with acceptance question |
|---|---|
| EN.645.662 requirements | Expand conditions into atomic shall statements; can each be verified with named inputs? |
| EN.645.768 architecture | Add physical/logical interface ownership and independent hazard control; are common causes addressed? |
| EN.645.631 / EN.645.632 modeling | Encode typed usages and relationships in an actual conforming modeling tool; do semantic references resolve? |
| EN.645.769 integration & V&V | Design fault-injection, test sampling and traceable procedures; which acceptance claims remain unsupported? |
| EN.645.764 assurance | Add causal pathways, defeaters and evidence limitations; what does a missing test leave open? |
| EN.645.784 quantitative decisions | Show how a new control changes cost, expected loss and robustness, with actual uncertainty sources. |

## 9. Sources and use restrictions

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — system requirements, technical interfaces and V&V processes.
- [OMG SysML 2.0](https://www.omg.org/spec/SysML/2.0) — normative language for formal models when using a conforming tool.
- [Book 1, chapter 4](../B1/chapters/04-requirements.md), [Book 8, chapter 10](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md), [Book 3, chapter 11](../B3/chapters/11-model-quality-queries-reports-change-impact-g.md).

**Use boundary:** all organizations, numbers, test dispositions, hazards and system configurations here are fictional examples. This package is for teaching traceability and critical review, not for authorizing operation or making a real safety determination.
