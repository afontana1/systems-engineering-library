# Workshop 3 · Typed relationships and trustworthy model queries

*Companion to Book III, Chapter 4 · Requirements model semantics*

## When a line on a diagram is not enough

The Northstar model includes requirements, functional behaviors, components, and tests. An analyst adds four arrows and reports “the requirements have been traced.” But a line from a requirement to a component could mean *allocated to*, *derived from*, *implemented by*, or something the tool does not understand. Model-based systems engineering adds value only when relationships carry **stable semantics** that a reviewer or automated query can interpret.

The running case contains four requirements. R1 requires dispatch acknowledgment; R2 protects against stale route authorization; R3 controls accessible boarding; R4 requires operational telemetry. Each requirement should have a relationship to a satisfying block and to a verifying test. A `satisfies` edge answers which design element claims to meet the obligation. A `verifies` edge connects a test case to a requirement; it does not mean the test passed. Actual test *results* must be associated with a revision, configuration, and test execution.

## The typed graph

For this workshop, nodes have types `requirement`, `block`, and `test`. A legal `satisfies` edge runs **from block to requirement**, and a legal `verifies` edge runs **from test to requirement**. That direction is a modeling convention adopted for the dataset, not the only conceivable graph notation. The important condition is that every tool and analyst agrees on it.

An integrity query can ask:

1. Does each requirement have at least one satisfying block?
2. Does it have a verifying test with a defined method?
3. Has an execution yielded an acceptable result for the **current revision and configuration**?
4. Are there prohibited relations—for example a `verifies` edge from a physical block rather than a test?

The first two are **structural consistency checks**. The third is a claim about **evidence sufficiency**. A structurally sound model can still describe an unsafe or unverified design. Confusing those levels is the central modeling error in this workshop.

## A worked query

The provided JSON model has R1 through R4. R1 has block B1, test T1 and a current, passing execution. R2 has block B2 and test T2, but its passing execution evaluates an older revision. R3 has test T3 but lacks a satisfying block. R4 is linked to block B4 and passing test T4, but has the wrong execution configuration. A basic link-count dashboard will imply that three or four requirements are well connected. The stronger query finds only **one requirement ready for a verification claim**. R2 is a re-verification concern; R3 is an architecture/allocation gap; R4 is a configuration applicability gap.

Notice the logical form of the query: a requirement is `structurally_complete` if it has a correctly typed satisfaction edge and test edge. It is `supported` only if it is structurally complete *and* a result matches the current requirement revision, intended configuration, applicability conditions, and acceptance criterion. This can be expressed as

\[
\text{supported}(r)=\text{complete}(r)\land \exists e:\text{admissible}(e,r)\land\text{pass}(e).
\]

The existential statement matters: multiple tests may exist, but one passing test is not enough if the verification plan demands multiple environments or methods. This simplified lesson assumes one required method per requirement; an actual model should encode the acceptance rule explicitly.

## Failure modes worth modeling

**Duplicate identifiers:** Two requirements with the same ID but different meanings make graph traversal non-deterministic. **Unowned derived requirements:** The derived constraint exists but nobody can approve changes. **Direction drift:** Tools exchange relations with inconsistent source/target semantics. **Stale evidence:** Test T2 passes, but R2's predicate changed after execution. **Unmodeled operating domain:** The requirement is claimed verified in a lab environment that does not exercise the relevant interface. Each is a different failure class and requires a different remedy.

## Worked problems

**Problem 1.** R3 has test coverage but no block allocation. Is it a traceability defect or an evidence defect?

<details><summary>Worked solution 1</summary>

It is primarily an allocation/architecture traceability defect. A passing test might exist, but the model cannot identify which design element claims the responsibility. A reviewer should not infer a satisfying block from the presence of a test.
</details>

**Problem 2.** R2 changes from revision 2 to revision 3. T2 passed at revision 2. What status does an automated review assign?

<details><summary>Worked solution 2</summary>

`STALE_EVIDENCE` (or similar), not `PASS`. Reverification or a controlled change-impact equivalence argument is required before accepting the revision-3 claim.
</details>

**Problem 3.** A diagram draws `B2 --verifies--> R2`. What is wrong under this model's convention?

<details><summary>Worked solution 3</summary>

`verifies` must originate at a test node, not a block. A block may satisfy a requirement, and its behavior may be investigated through a test. The wrong edge type misrepresents the engineering claim.
</details>

**Problem 4.** Why is a high graph-completeness percentage insufficient evidence for system safety?

<details><summary>Worked solution 4</summary>

Graph completeness checks structure, not the truth of design assumptions, operational representativeness or test validity. An incorrect but perfectly connected model can still mislead; assurance needs independent validation and reviewed evidence.
</details>

## Transfer to engineering work

Run the JSON model validator and inspect all four requirements. Repair *one* defect by changing the model—not by changing the validator's interpretation—and explain why your edit is justified. Produce a typed relationship legend, a query definition, and a table separating structural completeness from evidence sufficiency. This builds directly on Book III's requirements modeling chapter and prepares the later model-quality query work.
