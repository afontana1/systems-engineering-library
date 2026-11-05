# Advanced Workshop · Concept Feasibility Before Scoring Alternatives

*Book 6 · Week 6 · hard constraints · charging-energy balance · screening · decision traceability*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-feasibility.md). The assessed course obligations remain in [the curriculum](../../../C/P2/EN645767.html).

## 1. Preference is irrelevant when a concept cannot meet its obligations

A concept selection meeting can produce an attractive weighted score while overlooking an impossible operating schedule. Northstar's fictional shuttle options trade capital cost, accessibility, route coverage, charging capacity, and exposure to outages. The engineer should first ask which requirements are **hard constraints**—properties without which the design is inadmissible. Only the remaining feasible alternatives belong in the preference ranking.

Distinguish a **requirement** from a modeling assumption. For example, “transport at least 100 eligible riders during the morning window” is a mission performance requirement if approved by the sponsor. “A vehicle will use 12 kWh per shift” is an energy estimate whose uncertainty should be modeled. Treating an estimate as a certain fact can produce unjustified confidence; treating a mandatory requirement as just another weighted criterion can produce an inadmissible winner.

## 2. Build a minimum physics budget

Energy cannot be created by an optimistic spreadsheet. In a simplified charging window, the delivered energy is

\[
E_{\mathrm{charge}}=N_c P_c t\eta,
\]

where \(N_c\) is the number of chargers, \(P_c\) is rated kW per charger, \(t\) is usable hours, and \(\eta\) is aggregate charging efficiency. A fleet using \(E_v\) kWh per vehicle requires \(E_{\mathrm{need}}=N_v E_v\) before reserve and distribution limitations. **Feasibility requires** \(E_{\mathrm{charge}} \ge E_{\mathrm{need}}\) in this toy budget. A credible design also checks whether chargers can physically reach the vehicles, whether charging occurs within allowable state-of-charge limits, charger downtime, peak-grid limits, and mobility demand during the window.

## 3. Worked screening case

Alternative A uses four vehicles consuming an estimated 12 kWh per shift each. It has two chargers rated at 7 kW and only three usable hours, with efficiency 85%. Demand is \(4(12)=48\) kWh; estimated supply is \(2(7)(3)(0.85)=35.7\) kWh. The **margin is −12.3 kWh** before operational reserve, making A infeasible under the stated charging plan. No weighted score can change that arithmetic.

Alternative B uses three lighter vehicles at 10 kWh each. Its demand is 30 kWh, leaving 5.7 kWh margin in the same charging window. This does not prove B meets ridership, accessibility or route constraints; it proves only that the *specified simplified charging constraint* is satisfied. If A can add a charger or increase the available window, it becomes a modified concept that should be costed and screened again—not silently admitted as the original A.

## 4. Multi-stage concept decisions

A disciplined conceptual design compares alternatives in stages: (1) reject or explicitly repair hard-constraint failures, (2) calculate mission outcome measures, (3) normalize and rank feasible options under declared stakeholder preferences, (4) examine weight sensitivity and uncertainty, and (5) decide what evidence is needed before concept baseline approval. Preserve rejected candidates and their exclusion reasons so that a reviewer can revisit a decision if an assumption changes.

Avoid false precision: a score of 0.783 instead of 0.779 may be meaningless when accessibility ratings are subjective and demand forecasts have broad uncertainty. Draw an uncertainty range or conduct scenario analysis. An architecture can be *conditionally preferred* while evidence gathering is incomplete, but do not mislabel that status as verified feasibility.

## 5. The right engineering question

The immediate choice is not “which shuttle is best?” It is “which alternative is feasible under explicit constraints and preferred for the sponsor's measurable mission, given what we currently know?” When the decision depends on charger utilization assumptions or actual demand, that uncertainty should become a targeted experiment in the next course phase.

## Worked problem set — attempt before revealing solutions

### Problem 1

Calculate delivered energy from two 7-kW chargers for three hours at 85% efficiency.

<details><summary>Show solution 1</summary>

2×7×3×0.85 = 35.7 kWh delivered under the aggregate-efficiency assumption.

</details>

### Problem 2

Compute the margin for four vehicles needing 12 kWh each.

<details><summary>Show solution 2</summary>

35.7 − 48 = −12.3 kWh, so the concept fails this one necessary energy constraint.

</details>

### Problem 3

If the fleet uses three vehicles at 10 kWh each, what is its energy margin?

<details><summary>Show solution 3</summary>

35.7 − 30 = +5.7 kWh; it meets this simplified constraint only, not all system requirements.

</details>

### Problem 4

If a team simply boosts a feasibility-failing concept’s “sustainability score,” can it become admissible?

<details><summary>Show solution 4</summary>

No. Soft scores cannot compensate for failed mandatory requirements. Change the design or governing constraint through an authorized process, then rerun screening.

</details>

## Independent transfer to the Northstar case

Use the energy CSV and `book6.py` to screen three candidates. Vary charger efficiency from 0.70 to 0.95 and identify when each concept becomes feasible. Add an explicit accessibility constraint that cannot be traded away. Produce a feasibility register separating requirements, model estimates, evidence, and design repairs; finish with a conditional recommendation.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-feasibility.md) · [Python source](book6.py) · [Experiment dataset](book6-concepts.csv) · [Interactive workbench](WORKBENCH.html).
