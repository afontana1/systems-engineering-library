# Chapter 10 — Constraints turn informal rules into testable predicates

*Book IV: Object-Oriented Analysis and Design · Week 10 — Express precise constraints with OCL and execute a change red-team*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 10](../labs/lab-10-express-precise-constraints-with-ocl-and-exec.md) before attempting [the assessed Week 10 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w10.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **express precise constraints with ocl and execute a change red-team** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Object Constraint Language expresses invariants, preconditions and postconditions over object models without specifying a particular algorithm. Translate informal statements into quantifiers, cardinalities and uniqueness where needed. A precise model rule still requires runtime enforcement and tests; OCL itself cannot enforce distributed database transactions.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Formal constraints express invariants and pre/postconditions as predicates over states and transitions.

### Distinguishing related ideas

Type correctness checks allowed values, while domain correctness checks relationships across fields and time; a nonnegative seat count alone does not prevent overbooking.

### Interpretation and boundary conditions

Specify when a condition must hold—before, during or after a transaction—and what observation would reveal a violation.

## Worked Northstar example

Invariant: an active vehicle has at most one overlapping active assignment at a time. Writing “vehicle.assignments->size() <= 1” is wrong because it excludes completed historical assignments. Filter by active status and overlapping interval before counting.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### Precision without pretending to have executable proof

An OCL-like constraint for a vehicle might be `self.assignments->select(a | a.isActive and a.overlaps(nowWindow))->size() <= 1`. The filter matters. `self.assignments->size() <= 1` would incorrectly reject any vehicle that completed more than one historical trip. Conversely, a check of `isActive` without overlap could reject two non-overlapping future reservations. The rule's exact meaning depends on how `nowWindow` and `overlaps` are specified.

Use this predicate to derive test cases for overlapping, adjacent and completed assignments. Treat the formal expression as a specification that still needs an implementation enforcement mechanism, especially under concurrent transactions.

## Graduate synthesis: formal contracts, execution traces, and invariant preservation

### What a constraint actually guarantees

An Object Constraint Language (OCL) invariant is a logical predicate intended to hold for every admissible system state; a precondition limits legal method invocation; and a postcondition constrains the state transition after the operation. These are different proof obligations. For an operation `board(rider)`, a precondition may require an authorized stop and a door-open state; a postcondition may require either an incremented occupancy or a recorded rejection. An invariant such as `occupancy <= capacity` describes all reachable states, not merely the ones exercised in a demonstration.

Formal correctness requires relating specifications to state transitions. Write `I(s)` for the invariant and `T(s, a, s')` for a permitted action `a` taking state `s` to `s'`. The induction obligations are `I(s₀)` for each initial state and `I(s) ∧ T(s,a,s') => I(s')` for every transition. Satisfying these shows safety over reachable execution sequences *within the modeled transition system*. It says nothing by itself about sensor deception, implementation defects, physical actuator delays, or behaviors omitted from the model.

### Temporal properties are not ordinary invariants

A Northstar boarding request can remain waiting forever without violating the instantaneous capacity invariant. Liveness adds an eventuality requirement: under a stated fairness and resource-availability assumption, every accepted request is eventually served or explicitly terminated. In temporal-logic shorthand, `G(accepted -> F(resolved))` means “always, an accepted request is eventually resolved.” The formula is false for an infinite execution in which a request is never resolved. If communications or vehicles can fail permanently, unconditional liveness is an unrealistic requirement; specify the environmental assumptions and exception paths explicitly.

Concurrency complicates reasoning because sequential method contracts may be valid individually but invalid under interleaving. If two boarding threads both read occupancy 9 of a capacity 10 and then each write 10, the representation may conceal a physical occupancy of 11. The repair is a transaction or atomic reservation protocol, not another diagram. A useful design reviews the linearization point at which capacity is irrevocably reserved and identifies how a timeout, retry, or duplicate message affects the record.

### Model, execute, and challenge the same property

The strongest connection between OOAD and assurance is a three-way correspondence: the textual rule, its formal predicate, and a counterexample-oriented test. For `occupancy <= capacity`, generate boundary cases at `capacity − 1`, `capacity`, and after concurrent requests; then check that all observations use the same capacity units and authoritative source. A proof over an abstract state machine and a passing implementation test are complementary. One examines all modeled transitions; the other samples real software and its environment.

An OCL expression can be syntactically well formed yet conceptually incomplete: a definition of `availableVehicles` might ignore maintenance lockout, for example. Treat each constraint as a *model of an operational meaning*, review it with domain owners, and maintain traceability to requirements and test or verification evidence. The graduate-level question is not “does the predicate evaluate to true?” but “have we shown the right predicate holds in the right model under justified assumptions?”

## What can go wrong—and why

Formal-looking syntax may conceal incorrect scope, missing null cases and time-dependent assumptions.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 10: Constraints turn informal rules into testable predicates](../labs/lab-10-express-precise-constraints-with-ocl-and-exec.md), you will: Write three invariants in plain English and OCL-like notation, including one temporal condition. Construct a counterexample object graph for each. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 10 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](09-apply-design-patterns-with-restraint.md) and leads toward [next chapter](11-design-persistence-and-conduct-the-design-rea.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w10.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: formal constraints and operational enforcement

### 10.1 Translate statements into predicates

The Object Constraint Language (OCL) is a declarative notation associated with UML models; its expressions do not mutate the model. The fragment below is **illustrative OCL 2.x-style syntax** whose class and enumeration names assume an explicitly declared model. It has not been executed by an OCL-conforming tool.

```ocl
context Reservation
inv AccessibilityEligibility:
  self.assignment->notEmpty() implies
    (not self.accessibilityRequired or
      self.assignment.vehicle.accessible)

context Assignment
inv UniqueActiveVehicleSlot:
  Assignment.allInstances()->select(a |
    a.state = AssignmentState::ACTIVE and
    a.vehicle = self.vehicle and a.slot = self.slot
  )->size() <= 1
```

The first invariant requires that an assigned accessibility-requesting rider use an eligible vehicle. The second counts active assignments at the same vehicle and slot. In a richer time model the slot comparison must be replaced with an interval-overlap relation. `allInstances()` also has tool- and scope-dependent interpretation; a model snapshot is not necessarily a complete operational store.

### 10.2 What the model constraint does not guarantee

OCL expresses a rule for review and model validation. It is **not** a concurrent transaction protocol. Even if two request objects each satisfy the rule when checked, overlapping commits can violate it without a serialization mechanism. The [reference implementation](../tools/step03_book4_contract_check.py) therefore enforces the active-slot rule with a partial SQLite `UNIQUE` index and records the resulting conflict. Domain predicate, model checker, integration test, and database constraint play complementary roles.

For cancellation, a postcondition can state that after a successful call the reservation is terminal and it has no active assignment. A method contract must also specify what remains unchanged and what happens on repeated calls. A system-level audit rule may extend beyond the object graph into event and configuration provenance.

### 10.3 Positive and negative constraint tests

Use the [fixture table](../case/scenario-fixtures.csv) as a small executable contract suite. `F-03` must reject an inaccessible vehicle; `F-05` must reject a competing active assignment; `F-06` must reject stale telemetry. A passing test on a purposely narrow fixture does not establish completeness: especially important are overlapping slots, eligibility changes after reservation, and distributed races.

**Solved checkpoint.** A reviewer proposes `self.vehicle.accessible = true` for *every* reservation. That would incorrectly reject ordinary bookings on nonaccessible vehicles. The correct condition is an implication restricted to reservations requiring accessibility, and only where an assignment exists.

**Exercise.** Rewrite the uniqueness rule using interval overlap instead of fixed slots. State which data must be available to evaluate it and whether the result could be enforced using a simple composite unique index. Consult the [OMG OCL specification](https://www.omg.org/spec/OCL/2.4) for normative semantics rather than treating these examples as parser certification.
