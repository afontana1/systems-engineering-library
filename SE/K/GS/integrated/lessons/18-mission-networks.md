## NS-GS4.1 extension — shared-cause reliability and shared throughput bottlenecks

The emergency-access architecture has two serial primary components, a standby backup path and a regional common-cause vulnerability. The independent-path calculation can be numerically correct and still be too optimistic when a failure disables all paths. The case uses invented component availabilities, not measured field reliability.

### Reliability derivation

The primary path succeeds only if both components succeed, so \(P(primary)=p_a p_b\). With an independent backup having availability \(p_c\), the at-least-one-path availability is

\[A_{ind}=1-(1-p_a p_b)(1-p_c).\]

At \(p_a=.98\), \(p_b=.97\), and \(p_c=.90\), this is \(1-(1-.9506)(.10)=.99506\), or 99.506%. If common-cause outage probability is \(q=.04\) and that outage disables **both** paths, \(A_{joint}=(1-q)A_{ind}=.96(.99506)=.9552576\), or 95.526%. Independence must be justified for the remaining path events; correlated failures outside the single modeled common cause are omitted.

### Capacity is not availability

The same architecture has 70 constituent slots but only 66 regional dispatch slots. Effective capacity is \(\min(70,66)=66\), against synthetic accessible demand of 62. This passes a nominal capacity count while reliability remains limited and policy screens fail compound disruption. An aggregate slot count omits routing time windows, EMS priority, hospital acceptance and constituent autonomy.

### Worked exercise and explained solution

**Problem.** If dispatch throughput falls from 66 to 60 slots during a network incident, what changes?

**Solution.** Effective capacity becomes \(\min(70,60)=60\). The specified demand is 62, so there is an unavoidable two-slot shortfall even if every constituent vehicle remains available. Enhancing vehicle uptime alone cannot remove the shared dispatch bottleneck. The [integrated laboratory](../integrated/labs/INTEGRATED-CASE.html) requires students to document owner authority and the field evidence needed for each link.

**Canonical overlap.** [Enterprise systems-of-systems flagship](../../U/flagships/F09-enterprise-systems-of-systems.html) covers the broader architecture and governance; this extension isolates the common-cause and min-cut errors.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
