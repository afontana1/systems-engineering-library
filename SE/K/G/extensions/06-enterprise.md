## Integrated case NS-G4.1 — Portfolio selection under legitimate authority

> **NS-G4.1 case convention.** Every number in this extension comes from a controlled, fictional emergency-dispatch dataset, unless explicitly identified as an illustrative assumption. A Python screening result is not an operational safety finding, a validated queue model, or an authorization from independently managed agencies. The case is shared with the other five advanced-studies chapters; use the same `revision: 1.0` throughout.

**Reproduce:** [controlled JSON](../data/ns-g4.1-case.json) · [Python model](../code/ns_advanced_case.py) · [computed results](../outputs/ns-g4.1-results.json) · [integrated laboratory](../labs/INTEGRATED-CASE.html).

### G1. Separate optimization, distributional impact, and permission

An enterprise intervention may improve dispatch stability without improving the lives of excluded passengers. The case has three policies: baseline, technical redundancy, and coordinated guardrails. The technical screen requires evidence age at most 30 s, expected route revision, operator queue wait at most 15 minutes, alarm PPV at least 35%, retry stability, joint availability at least 98.5%, and sufficient accessible max-flow slots. All thresholds are *invented instructional criteria*, not public-service standards.

The coordinated policy passes all six tests in the nominal scenario, but fails demand surge (queue wait **20.38 min**), rail outage (accessible flow **32** vs 55), compound disruption (availability about **95.62%** and flow 58 vs 62.15), and interface drift (R2 versus R3). Accordingly, only the nominal scenario's **0.55** illustrative weight clears its technical screen. A weighted total of 55% is not a frequentist estimate of operational success, because the five scenario weights were selected for teaching, not calibrated from incidents.

### G2. Enterprise inequalities cannot be hidden in average outcomes

The baseline uses 12-minute urban mean wait and 34-minute accessible mean wait, a 22-minute disparity. Technical redundancy reduces the difference to \(28-11=17\) minutes. Coordinated guardrails yield \(19-10=9\) minutes and meet an illustrative 12-minute maximum gap screen while costing $1.65 million, below a $1.8 million instructional cap. These means refer to stipulated groups and are not representative observations; they do not account for rejected or unserved requests. Report coverage, denied service, queue age, group means and tails, safety events, labor impact, and the population definition before discussing equity.

The governance record requires regional sponsor, road authority, accessible service owner, labor representative, and privacy officer permissions. It deliberately records **three absent approvals** (road authority, labor representative, privacy officer). The model therefore reports no operational authorization even if some numerical checks are green. The missing evidence is a necessary decision input, not a soft penalty to trade against mean wait or capital expense.

### G3. Causal inference requires more than an attractive before/after

To avoid attributing a seasonal trend to an intervention, the exercise compares a treated region (26 → 17 minutes) to a comparison region (23 → 19 minutes). Difference-in-differences estimates

\[
\widehat\delta_{DiD}=(17-26)-(19-23)= -9-(-4)=-5\,\mathrm{min}.
\]

Earlier two-period trends (28 → 26 in the treated region; 25 → 23 in the control) both decline by 2 minutes, so their *observed* pretrend difference is zero. This is a helpful falsification check, **not proof** of parallel counterfactual trends. Interference (shared vehicles), simultaneous staffing changes, regression to the mean, changing composition, and selective missing-data mechanisms can still bias the result. This is a four-number arithmetic demonstration, not a validated causal study; confidence intervals require a defensible sampling design, not invented precision.

### G4. Decision rights and reversible interventions

A responsible pilot begins with a written theory of change and staged permission matrix. Require independent route-status verification, operator practice assessment, explicit constituent agreements, and a privacy-impact review. The pilot must measure failed and abandoned requests, not only completed trips, and include accessible-rider participation in defining harms. Stop or revert the pilot for an unsafe departure, persistent group service deficit, unacknowledged route-revision drift, or expired authorization. Document who can suspend a service, who investigates, who may resume operations, and how disagreements are recorded.

### Worked exercise with explained solution

**Problem.** Would replacing a 1.8-million-dollar budget cap with a 2.0-million-dollar cap authorize the coordinated policy? What changes in the reported technical screen?

**Solution.** The coordinated policy already costs $1.65 million, so the new cap changes neither feasibility nor the 55% synthetic technical coverage. Three approvals are still absent, and four out of five scenarios still fail some technical constraints. The correct enterprise disposition remains **HOLD**, regardless of the higher budget. A favorable weighted score cannot resolve this missing evidence.
