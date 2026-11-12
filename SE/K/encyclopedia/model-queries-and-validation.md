# Model queries and automated validation: questions that a model can answer

**Reference entry · MBSE and digital thread · Worked technical treatment**

## Query, validation rule, and evidence are different

A **model query** retrieves model facts under a stated selection criterion. A **validation rule** evaluates an invariant over those facts. An **engineering evidence claim** additionally requires that the rule is appropriate, the model represents the intended system, and the checking tool and configuration are credible. A dashboard reporting “100% allocated” can pass while every requirement is allocated to the wrong subsystem.

The analysis pipeline is: declare purpose -> define model schema and relationship types -> select scope and version -> evaluate the query -> inspect exceptions -> document model limitations -> decide whether independent physical or analytical evidence is still needed. Preserve a model-diagnostic report even when a query returns zero exceptions.

## A miniature typed graph

Consider requirements \(R=\{r_1,r_2,r_3,r_4\}\), logical elements \(L=\{d,b\}\) (dispatcher and brake controller), and allocation edges \(A=\{(r_1,d),(r_2,d),(r_3,b)\}\). The missing-allocation query is

\[
Q_{\text{missing}}=\{r\in R\mid\nexists\ell\in L:(r,\ell)\in A\}=\{r_4\}.
\]

Allocation coverage is \(3/4=75\%\), but it would be misleading to announce “75% of the engineering work complete.” The metric only assesses the existence of allocations within this declared requirement set. It says nothing about the validity, completeness or adequacy of the requirements, or about unmodeled stakeholder needs.

Add a relation `verifiedBy`, a typed test record, and a declared configuration `CM-B2`. A more meaningful rule is: *every safety-significant allocated requirement must have applicable verification evidence for the same approved configuration*. This rule needs at least four predicates: applicable safety scope; valid allocation type; test purpose consistent with the requirement; matching evidence baseline. A test for `CM-B1` is not automatically valid for `CM-B2`.

## Automated checks worth building

1. **Referential integrity:** all referenced identifiers exist, are unique where required, and have legal types.
2. **Completeness against a declared set:** each in-scope requirement has an owning element and disposition; do not quietly exclude “unknown” scope.
3. **Semantic consistency:** units, state names and interface roles agree across relationships.
4. **Change impact:** traverse dependents of a modified requirement or component, capturing transitive affected tests and safety claims.
5. **Evidence currency:** test versions and configurations are applicable; outdated evidence is reported as such, not silently accepted.
6. **Counterexample diagnostics:** a failure report identifies the precise nodes, links, assumptions, and rule violated.

A query can be written in SQL, graph query languages, a model-tool API, or a local Python data checker. The syntax is secondary to specifying the semantics and testable failure cases.

## A reproducible negative test

For the four-requirement example, an expected unit test is `missing == {'r4'}`. Next introduce a dangling allocation `(r5,d)`: a complete referential-integrity rule must flag `r5`, even though it would not change the denominator of the original coverage query. Finally, relabel a verification record to a stale baseline and check that evidence currency fails. This is a small but important principle: **test the checker with deliberately malformed inputs**, not only a valid demonstration model.

## Tool validation is separate from language conformance

A project-specific CSV/JSON checker can detect broken links but cannot claim that SysML v2 textual source conforms to OMG grammar or that its semantic model is consistent. A language parser, a semantic model tool, a project-specific constraint checker, and product V&V serve different roles. Record tool version, query version, input baseline and diagnostics so another person can reproduce the result.

## Failure modes, applications and reading

Common failure modes include counting labels instead of typed links; circular relations presented as independent evidence; stale snapshots; silently excluded data; ambiguous requirement identity; and rule changes without baselined test cases. Particularly useful applications are design-review readiness, impact analysis, configuration control, and assurance-case evidence review.

- [NASA Systems Modeling Handbook](https://standards.nasa.gov/node/3111) — generating SE work products from structured models.
- [OMG SysML v2](https://www.omg.org/spec/SysML/2.0) — language and API specifications.
- Related: [requirements traceability](traceability-graph.md); [model baselines and evidence](../methods/model-baselines-and-evidence.md); [controlled Campus Mobility artifacts](../methods/campus-mobility-engineering-artifacts.md).

*Scope:* The graph example is a teaching abstraction; no claim of formal proof or SysML parser conformance is made.

**Reproducible companion:** [Step 02 worked examples (standard-library Python)](examples/step02_examples.py). Run `python3 step02_examples.py --case all` from the downloaded examples folder; the program prints the declared synthetic inputs and computed results.
