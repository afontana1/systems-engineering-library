# System-of-systems mission dependencies and distributed assurance

*Graduate study for Book 18 — System of Systems Engineering. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> How can every constituent system meet its local target while the joint mission fails?

## Theory and conceptual structure

A system of systems (SoS) comprises independently managed constituent systems whose coordination produces mission capabilities that no single participant supplies alone. Interoperability is not merely a data-format problem. It requires shared operational semantics, timing assumptions, responsibility for failure recovery, authority for changes and a mechanism for resolving conflicting objectives.

Represent a mission as a dependency network with paths, gates and minimal cut sets. A minimal cut set is a smallest set of failures sufficient to disable a mission claim. It tells decision makers where redundancy, monitoring or governance agreements may be valuable. The representation must distinguish **logical dependency** from probabilistic independence. Constituent systems may share facilities, providers, time synchronization or a cyber identity system; naive multiplication of local availabilities overstates mission reliability.

Assurance must be distributed. A central integrator may have a mission-level requirement but cannot unilaterally redesign a hospital, emergency agency or transit operator. Verification evidence therefore includes constituent promises, interface contracts, test windows, change notifications and consequences when an external participant withdraws service. The confidence placed in an external assurance claim should be conditional on provenance and independent challenge.

SoS behavior is evolutionary. New participants change network topology, demand and incentives. An optimized interface arrangement can become brittle when governance changes. Scenarios should include late data, conflicting jurisdictional rules, service rationing and authority disputes—not just component outages.

## Formal model and derivation

\[M=(A\land B)\lor C.\]
If path \(A\land B\) and backup \(C\) are independent, \(P(M)=1-(1-p_Ap_B)(1-p_C)\). If paths share a provider, independence is false; analyze shared-cause scenarios separately. Minimal cut sets for this structure include \(\{A,C\}\) and \(\{B,C\}\).

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

Suppose two jointly required constituents A and B each have availability 0.95, and an independent backup C has 0.80. The mission succeeds if both A and B work or C works. Under independence, P(M) = 1 − (1 − 0.9025)×(1 − 0.80) = 0.9805. Now suppose all three rely on one identity provider with a 3% shared outage probability, otherwise behaving independently. Total availability becomes approximately 0.97×0.9805 = 0.9511. The original 98.05% claim hid a shared dependency that no local participant owned as a mission risk.

![Model of the linked reasoning steps](../figures/18-mission-networks.svg)

## Counterexample and critical review

**Counterexample:** Two agencies agree to use the same JSON message field `priority`, but one interprets 1 as urgent and the other interprets 1 as routine. Syntactic interoperability holds, operational semantics fail. Contract testing requires controlled examples and end-to-end mission observation.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

Identify minimal cut sets of M=(A and B) or C.

<details><summary>Worked answer and engineering interpretation</summary>

{A,C} and {B,C}. Failure of either set disables both the main path and backup.

</details>

### Problem 2

Calculate the independent-path mission availability with A=B=.95, C=.80.

<details><summary>Worked answer and engineering interpretation</summary>

1−(1−.95²)(1−.80)=.9805, conditional on independence and correct mission logic.

</details>

### Problem 3

Describe a shared-cause failure that invalidates the independence model.

<details><summary>Worked answer and engineering interpretation</summary>

A common identity provider, network operator, geographic flood zone or authority revocation that can disable both principal and backup paths.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/18-mission-networks.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 18 and its existing weekly lessons](../../B18/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)
