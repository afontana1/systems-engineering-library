# SysML v1 and v2: conceptual continuity, not cosmetic conversion

**Concept library essay · Phase 1**

## What remains the same
Across SysML generations, engineers still need to express requirements, parts, behavior, quantitative constraints and relationships to analyses and evidence. A stakeholder does not care which syntax encodes a latency requirement; they care whether it is unambiguous, consistently allocated and defensible by test evidence. This conceptual continuity should drive learning before tool-specific syntax.

## Why the change is substantive
SysML v1 commonly extends UML conventions with requirements diagrams, block definitions, internal block views, activities, state machines and parametric diagrams. SysML v2 defines a newer language grounded in KerML, with textual and graphical representations, more formal semantics and an interoperability/API ecosystem. The exact language constructs and supported migration behavior depend on tool version and the official specification. A direct diagram-to-diagram 'translation table' is therefore an incomplete migration strategy.

## A safe learning approach
For the same shuttle example, represent five concepts without committing to notation: (1) need for predictable arrivals; (2) requirement for status freshness; (3) function to publish updates; (4) part or service responsible for publishing; (5) verification case under network disruption. Once these relations are clear, implement them in your chosen SysML environment and record which constructs express each meaning. Use a capability checklist to test whether your tool can query links, version models, export interoperably and validate constraints.

## Migration experiment
Export a small, reviewed baseline from a v1 tool if you have one. Import or recreate a controlled subset in a v2 implementation. Compare element identity, requirements content, interface meaning, relation cardinality, units, annotations, package visibility and evidence links. Report unsupported semantics instead of silently omitting them. Preserving a JPEG image does not preserve a model.

## Current primary source
The OMG SysML 2.0 language specification, formally adopted in 2025 and published with editorial updates in 2026, should be your normative reference. Vendor tutorials may be useful for a tool but do not override specification semantics.

[Back to Phase 1 library](../README.md)
