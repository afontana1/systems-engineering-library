# From diagrams to a semantically controlled model

**Concept library essay · Phase 1**

## The underlying problem: different pictures of one thing
A model is a claim about the world, not just a visual aid. If a requirement is displayed in three diagrams, those three shapes should not become three independent requirements. Identity is the key: an element needs a stable ID, a type, attributes, status and provenance, then views can render it according to a stakeholder's concern. In a spreadsheet, the same rule can be enforced by primary keys, typed relation columns, validation rules and configuration fields. The sophistication of a drawing tool matters less than whether the data remains consistent when you change it.

Suppose `REQ-S-12` describes reporting dispatch status. A model may connect it to `NEED-R-02`, function `FN-REPORT`, software component `SVC-NOTIFY` and test `T-FRESH`. Each relation makes a different claim. `derivedFrom` says a source justifies an obligation, `allocatedTo` says someone must realize behavior, and `verifiedBy` says a procedure supplies evidence about conformance. Do not use one generic 'links-to' relation when the review question requires a precise claim.

## A small relational model
Start with two data structures:

```text
Element(id, kind, title, revision, owner, status, source)
Link(source_id, relation_type, target_id, rationale, review_status)
```

Constraints then become possible: every link endpoint exists; IDs are unique; every baselined requirement has at least one source; every high-consequence requirement has a planned verification; an allocation targets a function or component of a permissible type; and every changed target generates an impact queue. These checks are necessary, but still not sufficient. 'All requirements have a source' can be satisfied by connecting everything to an irrelevant stakeholder need. Semantic quality requires review of samples and high-risk paths.

## Query design and review
Write the engineering question first. 'What changed?' needs revision comparisons. 'Are we ready to test?' needs requirements-to-test paths and test status. 'If the gateway is removed, what depends on it?' needs both direct and transitive impact queries. Keep model quality separate from V&V completion: a model may be internally consistent while representing incorrect physics or operations. Record both automated-rule reports and reviewed claims.

## Practice
Create three elements with the same label but different types: an operational function `NotifyRider`, an OOAD design interface `NotificationPort`, and a deployable software service `NotificationService`. Explain why merging them erases architecture decisions. Then draw links with rationale and a review decision for each. See `tools/model_graph.py` for a runnable representation.

[Back to Phase 1 library](../README.md)
