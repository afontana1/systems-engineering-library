# NS-SOS18.1 — Regional emergency access: controlled SoS engineering case

**Status:** fictional instructional exercise; source scenario probabilities, availability factors, costs and trip demands are *invented* for this release. They are not reconstructed from an agency or the previous textbooks. All capacities are **trip slots available over four hours**, not hourly trips, emergency patients, simulated trajectories or externally measured data. The case complements rather than replaces the existing Northstar Regional Emergency Access case in Book 18.

## Decision and constituent independence

The regional council asks whether a combination of battery backup, data interoperability and alternative routing can deliver **62 accessible trips** and **186 standard trips** within four hours while dispatch information is at most **5 minutes** old. Rail, paratransit, hospital intake, bus and campus shuttle owners retain separate authority, independent missions, and update clocks; the council cannot compel conformance by assigning a box in a drawing.

The controlled [input file](controlled-inputs.json) and [standard-library model](../tools/step03_book18_sos.py) describe six independently owned operational resources plus an accessible receiving interface. The [authority registry](authority-registry.csv), [mission thread](mission-thread.csv), [interface contracts](interface-contracts.csv), [distributed evidence matrix](vnv-distributed-matrix.csv), [assurance register](assurance-register.csv), and [decision record](decision-record.csv) make *authority, data, timing, assumptions and failed evidence* inspectable.

## Architecture and calculation

Two independently offered **accessible** routes (shuttle and paratransit) feed a common accessible receiving interface. Bus and rail provide independent **standard** paths. The shared dispatcher and hospital are not free capacity: they constrain both demand classes. The allocation policy **reserves accessible slots first**; standard users receive remaining common slots. If resource capacities are \(c_i\) and event-specific effectiveness factors are \(f_i\), let:

\[
A_{path}=\min(c_{sh}f_{sh}+c_{para}f_{para},\;c_{access}f_{access}),\quad
S_{path}=c_{bus}f_{bus}+c_{rail}f_{rail},\quad
C=\min(c_{dispatch}f_{dispatch},\;c_{hospital}f_{hospital}).
\]
\[
A=\min(D_A,A_{path},C),\qquad S=\min(D_S,S_{path},\max(0,C-A)).
\]

A mission screen passes only if \(A\geq62\), \(S\geq186\), timestamp age \(\leq5\) min, and the contract revision and associated evidence are current. This is a deterministic capacity **screen**, not a traffic assignment solver. The accessible-first rule is a policy choice with equity implications; the model neither optimizes fairness nor accounts for patient acuity, passenger travel time, crowding, routing, staff, charging, privacy agreements or evacuation feasibility.

In **normal** service, accessible path capacity is min(50+35,70)=70, standard path capacity is 150+110=260, and common slots=min(270,280)=270. Allocating 62 accessible leaves 208 common slots; 186 standard are therefore possible on the synthetic inputs. Under a **grid** disruption without mitigation, accessible path is 50(0.60)+35(0.85)=59.75 and common slots=min(270(0.90),280(0.90))=243. Accessible capacity fails the 62-trip target despite individually operating constituents.

## Reproduction and conditional results

From the repository root:

```bash
python SE/K/B18/tools/step03_book18_sos.py
python SE/K/B18/tools/step03_book18_sos.py --check
python scripts/check_step03_book18.py
```

Output includes [coverage by policy](policy-coverage.csv), all [policy-scenario screens](scenario-screens.csv) and [worked Bayesian, live-change and compound-stress evidence](computed-evidence.json). Hypothetical scenario weights are normal .55, grid .20, flood .15, comms .10; the **compound** stress is intentionally outside the nominal probability ensemble and does not have a defensible probability estimate.

| Policy | Added synthetic cost (million USD) | Weighted joint scenario pass | Compound stress |
|---|---:|---:|---|
| Status quo | 0.00 | 55% | Fail |
| Backup power | 0.70 | 75% | Fail |
| Data federation | 0.50 | 65% | Fail |
| Integrated | 1.65 | 100% | Fail |

The 95% *scenario-coverage* screen can be passed by the integrated option, but **coverage over four constructed scenarios is not 95% observed mission reliability**. Cost figures are assumed incremental costs, not approved estimates. The scenario factors are stipulated mitigation effects, not measurements. The integrated policy is unsuitable for operational qualification because the compound case fails, authority and clinical validation are missing, and a new rail interface revision makes the evidence status stale.

## Information fusion and critical uncertainty

Let \(B\) mean a blocked route. The fictional prior is \(P(B)=0.15\), and an alarm has sensitivity .85 and false-alarm probability .10. For a positive alarm, Bayes' theorem gives \(P(B\mid +)=.15(.85)/[.15(.85)+.85(.10)]=.60\). If a second conditionally independent confirmation has sensitivity .80 and false-positive probability .15, \(P(B\mid +,+)=.60(.80)/[.60(.80)+.40(.15)]=.8888889\). Correlated feeds, shared clocks, stale messages and unmeasured calibration invalidate the conditional-independence simplification. Confidence cannot override invalid operational authority or an expired data timestamp.

## Live constituent change and engineering board

An independent rail owner changes `dispatch-v1` from revision **1.0 to 2.0**, without refreshed evidence. The model's numerical throughput can still pass in nominal conditions, but `interface_current=false`, so the **joint screen fails**. The correct response is not to silently continue from a prior version: issue an impact record, negotiate a compatible contract or safe fallback, perform cross-owner integration tests, revise the mission and risk baseline, and obtain the agreed use authorization.

**Review disposition: HOLD for operational deployment.** A limited pilot proposal might be considered only after current owner commitments, accessibility and privacy review, source calibration, compound-hazard testing, route/clinical realism, independent validation, and an accountable board decision. A mathematically appealing capacity allocation does not discharge distributed verification, public legitimacy or operational safety obligations.
