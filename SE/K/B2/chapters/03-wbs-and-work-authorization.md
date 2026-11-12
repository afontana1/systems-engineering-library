# Chapter 3 — Scope Becomes Controllable Through Products

*EN.645.667 · Week 3 · Product-oriented WBS, control accounts and authorization · Preceded by [Chapter 2](02-rfp-and-proposal-strategy.md); continue with [Chapter 4](04-estimating-and-reserves.md).*

> **Study contract.** This chapter teaches the concepts behind Week 3; practice them in [Hypothetical Lab 3](../labs/lab-03-wbs-and-work-authorization.md), then complete the [original Week 3 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

A list of activities can look busy and still omit a complete product. A schedule containing “design,” “develop,” and “test” for the shuttle pilot does not reveal whether the project includes accessible boarding, dispatch software, charging infrastructure, safety evidence, training, or interface integration. A **product-oriented work breakdown structure** changes the question from “what will people do?” to “what must the project deliver?”

The product breakdown structure describes the designed system; the WBS organizes all authorized project scope, including management, integration, test, and enabling work. A work package is a controlled portion of that scope with an owner, budget, schedule, completion criterion and evidence. Control accounts sit at intersections of work and accountable organizations. Planning packages can represent future scope not yet decomposed to executable detail, but they are not a license to conceal undefined work indefinitely.

The 100-percent rule is a completeness discipline: lower-level elements collectively cover their parent without overlapping scope. It is not an excuse to count the same interface test once under software and again under integration. Define the receiving organization and acceptance evidence for every delivery crossing a work-package boundary.

## Develop the method

Start with deliverables, not departments. Decompose “Shuttle Pilot” into vehicle and equipment, dispatch and passenger services, physical and digital interfaces, safety/verification evidence, transition to operations, and management. Write a WBS dictionary entry for each leaf: included scope, exclusions, assumptions, deliverable, completion rule, accountable manager and receiving party. Reconcile the WBS against the statement of work and the systems engineering product tree.

Next map WBS elements to an organizational breakdown structure using a responsibility assignment matrix. One accountable control-account manager should own each work package; specialist contributors may be multiple. **Authorization** is a formal decision to release defined work within approved constraints, not merely an informal request in a meeting. A revision to scope should trigger impact assessment before authorization.

## The mechanism beneath the method

A work breakdown structure partitions deliverable products, not simply work verbs; this makes it possible to assign acceptance and aggregate cost without double counting.

### Distinguishing related ideas

The organization chart answers who reports to whom, while the WBS answers what is to be delivered; equating them hides interfaces spanning departments.

### Interpretation and boundary conditions

A work package is useful only when its completion conditions can be evaluated and its dependencies to other products can be named.

## Deeper theory: work breakdown structures as conservation of contractual scope

A work breakdown structure (WBS) is easy to confuse with a task list because both contain named pieces of work. Yet the two structures answer different questions. A task list describes **actions in time**; a product-oriented WBS describes **what must exist when the project is complete**. This matters because activities can be performed without producing a usable deliverable, and a deliverable can be omitted even while every planned activity is marked done. A WBS should partition the authorized scope so that each required product or product-related service has a clear home. The familiar “100% rule” is best understood as a conservation principle: the union of child elements accounts for the parent's complete authorized scope, without double counting the same product in several places.

The idea can be formalized. Let \(S\) be the set of deliverable obligations for the project and \(W_1,\ldots,W_n\) the lowest-level WBS elements. A structurally complete decomposition aims for \(\bigcup_i W_i=S\). Good control also minimizes problematic overlaps: if a charging-station interface is assigned fully to both infrastructure and vehicle teams, overlapping ownership can generate duplicate work or, paradoxically, a gap because each team expects the other to perform acceptance testing. The real project rarely admits perfectly disjoint sets—interfaces are shared by nature—but **accountability for the interface artifact** can still be made explicit.

### Why products enable control accounts

A work package is not simply a small enough activity. It is a bounded obligation with a deliverable, defined completion evidence, estimated resources, and responsible organizational owner. A control account couples a segment of the WBS to the organization responsible for executing and controlling it. This lets cost, schedule, technical status, and change control refer to the same object. Without this coupling, management information becomes inconsistent: finance may report a department's labor spending, engineering may report completed drawings, and the schedule may report elapsed tasks, with no way to determine whether spending produced the required baseline.

Consider an accessible boarding subsystem. A weak WBS element named *accessibility work* obscures what is being bought or built. A stronger structure distinguishes the boarding mechanism, human-interface controls, installation interface, operating procedures, and qualification evidence. Each product can have an explicit acceptance condition. The decomposition is not automatically correct merely because it contains many nouns; the engineer must check whether the chosen level allows meaningful ownership and verification without creating thousands of administrative fragments.

### A schedule is a different projection of the same project

Suppose three products must be delivered: docking interface, reservation software, and operator procedure. The product structure does not itself say which must happen first. Scheduling overlays precedence relations, resource constraints, and durations on the work. Many-to-many connections are normal: several tasks may produce one artifact, and one test activity may validate several WBS products. Collapsing WBS hierarchy into schedule order loses important information. A vehicle interface and software service may be siblings in the WBS even though one integration test depends on both.

This distinction becomes especially important in earned value management. A deliverable should earn value when its agreed accomplishment criterion is satisfied, not merely when personnel have spent planned hours on it. Consider a work package budgeted at 100 units that is 90% time-expended but whose interface specification has not passed its acceptance review. Claiming 90 units of earned value may hide a technically blocked product. The measurement method must reflect **objective progress toward the product**, not the ease of reporting activity.

### Configuration and change create a time dimension

A WBS is not static if the authorized scope changes. Yet careless renumbering of WBS elements each time an interface evolves destroys historical traceability. A good baseline records what was authorized at each revision, which changes added or removed obligations, and how estimates were transferred. Product identifiers should survive reasonable re-planning when the underlying product remains the same. New products should be introduced through documented change, and abandoned products should remain explainable in the history.

The WBS is thus more than a budgeting outline. It is the project's **ontology of contractual responsibility**: a shared classification of products that enables engineering, finance, procurement, testing, and governance to discuss the same work without silently changing its meaning. A complete WBS does not guarantee a feasible project, but without one it is very difficult to know what “complete” means.

## Worked Northstar project example

Consider a simplified $720,000 subsystem tranche: vehicle integration $260,000; dispatch software $190,000; safety and verification $170,000; operations training $100,000. The leaf total is $720,000, matching the parent budget. Now discover that $35,000 of interface testing sits inside both the software and verification estimates. The apparent total double counts that work. Moving the interface test under a single accountable package and allocating receiving interfaces removes ambiguity; it may or may not change the total budget, depending on whether the duplicated amounts were genuine planned effort.

## Work packages and the problem of false completion

Suppose the software control account has a milestone called “dispatch feature complete,” worth $160,000. One manager defines completion as code merged, while operations assumes it means the feature works with vehicle hardware and approved passenger flow. The two definitions are inconsistent. The work package should define its *product*, its configuration at delivery, interfaces, receiving party and objective acceptance evidence. A milestone with subjective completion language can manufacture earned value while transferring unresolved work to integration.

Scope decomposition should also expose enabling products. A hypothetical dispatch subsystem may need executable code, interface definition, secure configuration management, deployment scripts, data schemas, operator guidance, verification procedures and archived results. A WBS that includes only source code has concealed a significant portion of the actual delivery. On the other hand, duplicating each interface test in both software and vehicle budgets can overstate effort and obscure ownership. A unique accountable work package can support multiple evidence consumers without being charged as two separate deliverables.

**Mini-exercise with arithmetic.** A parent WBS element is budgeted at $720,000. Its four authorized children total $260,000 + $190,000 + $170,000 + $100,000 = $720,000. That reconciles the budget numerically, but not necessarily the *scope*. If the first and third children both include the same $35,000 interface campaign, the nominal sum still matches while the work definition is ambiguous. An effective scope audit checks descriptions and evidence as well as totals. If the duplicated campaign is removed, the team must then establish whether $35,000 is unallocated funds, extra scope elsewhere, or a mistaken budget assumption.

Write a WBS dictionary entry for one leaf with five precise exclusions. Ask another learner to reconstruct what “complete” means without seeing your informal notes. If they cannot, improve the entry before using it as a basis for estimate and earned-value measurement.

## Boundary of the method

An attractive decomposition can still fail if “done” is defined by elapsed effort or percent of code written. A work package needs observable delivery evidence and an unambiguous transfer condition.

## Retrieval questions and explained answers

1. **Question:** Why is a phase-oriented WBS often weaker than a product-oriented WBS?
   **Explanation:** It can conceal missing products and blur ownership of interfaces and verification outputs.
2. **Question:** Can two teams contribute to one work package?
   **Explanation:** Yes; one accountable owner should coordinate the defined scope and completion evidence.
3. **Question:** What must happen before adding new authorized work?
   **Explanation:** Assess its technical, cost, schedule, risk and configuration impacts and obtain proper change approval.

## Put this into practice

Work through [Lab 3: The Missing Work Package](../labs/lab-03-wbs-and-work-authorization.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 3 primer](../../P0-text/lessons/645-667-w03.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.

## Step 03 integrated reference — connect scope, accounts, and evidence of completion

The **100% rule** means that the work breakdown structure covers every in-scope deliverable and no work outside the approved scope; it does not mean that the team has made the perfect decomposition. Begin with the acceptance boundary and product tree, then identify service and enabling products such as test fixtures, trained operators, interface control records, and evidence packages. If verification work is omitted merely because it is “supporting work,” a seemingly cheap architecture will lack the means to prove itself.

### Reconcile the controlled accounts

The [editable control-account table](../case/control-accounts.csv) contains five synthetic deliverable-oriented accounts:

| Account | Budget ($M) | Product-oriented scope |
|---|---:|---|
| CA-01 | 1.2 | Architecture and configuration |
| CA-02 | 2.0 | Vehicle/gateway integration |
| CA-03 | 1.6 | Dispatch software and interfaces |
| CA-04 | 1.4 | Verification and evidence |
| CA-05 | 1.0 | Deployment preparation and training |
| **Total** | **7.2** | NS-M1 performance measurement baseline |

Each account needs a **dictionary**: included deliverables, excluded scope, acceptance test, responsible manager, start/finish logic, budget basis, and change authority. Without that dictionary, an integration team may claim a sensor calibration procedure belongs to verification, while the verification team claims it belongs to integration. Both may mark their tasks complete while nobody owns the instrument calibration.

### Work authorization and earned-credit rules

Distinguish (1) budget authorized, (2) costs incurred and (3) measured accomplishment. An invoice for a half-complete gateway is cost, not proof of earned value. A milestone-based earned-value technique could award 30% for an approved interface specification, 40% for integrated demonstration and 30% for accepted evidence, **if** these gates reflect substantial work and are documented before execution. A manager should not choose 95% complete by intuition. Where work is genuinely level-of-effort, explain why that measurement technique does not independently demonstrate technical progress.

**Worked reconciliation.** CA-04 has a $1.4M budget but only $0.15M earned by the fictional month-five checkpoint, against $0.18M spent. Its account-level CPI is \(0.15/0.18\approx0.833\). That ratio does not show the technical verification quality; inspect which procedures and signed evidence contributed to the $0.15M earned credit.

**Practice with answer.** A supplier delivers an untested controller, and the team marks both “controller delivered” and “controller accepted” complete because the shipping manifest exists. **Answer:** shipping can close a logistics milestone but not a verification/acceptance milestone; the dictionary and work authorization must separate them to avoid double-counting progress.

**Reference:** PMI's [Practice Standard for Work Breakdown Structures](https://www.pmi.org/standards/work-breakdown-structures-third-edition) describes product-oriented coverage, decomposition and control relationships.
