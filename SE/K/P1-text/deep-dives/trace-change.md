# Change impact, provenance and controlled evidence

**Concept library essay · Phase 1**

## One change touches several models
Change the status freshness requirement from 10 seconds to 3 seconds. At first it looks like editing one threshold. But the system behavior may need a faster event cycle; the interface must preserve timestamps; cloud budgets and mobile push behavior may change; stale-state policy may become more visible; old tests no longer establish compliance. The correct unit of change analysis is a set of claims and dependencies, not the paragraph that carried the original number.

Track every element with a stable ID and revision. A dependency link should have a declared meaning and version relevance. When `REQ-ETA` changes, traverse to functions and designs, then to analysis inputs and tests; label links as confirmed, suspected or explicitly unaffected after review. Preserve older baselines so historical test runs remain interpretable.

## A minimum change workflow
1. Record change request, source, reason, proposed target and impact window.
2. Query direct and transitive dependencies; expand scope through domain-expert review.
3. Identify decisions, tests, data models and operating procedures with likely impact.
4. Propose alternatives and evaluate cost, risk and risk of not changing.
5. Approve an implementation baseline and assign work.
6. Update models and evidence, rerun checks and publish new controlled state.

A change report should explain why a linked element is or is not affected. A generated list of 400 links without prioritization is not useful decision support. Focus on high-consequence chains first.

## Practice
Use the `model_graph.py` tool to find transitive impact of a changed requirement. Compare its mechanically inferred set to a human-reviewed set. Mark at least one false positive and one missing link. This teaches why automated traces accelerate—not replace—systems reasoning.

[Back to Phase 1 library](../README.md)
