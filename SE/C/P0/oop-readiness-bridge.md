# Optional bridge — Object-oriented programming readiness

[Back to Phase 0](OVERVIEW.md) · [Back to program README](OVERVIEW.md)

## Purpose

This bridge is for learners who do not yet meet the object-oriented programming gate required before **EN.605.704 — Object-Oriented Analysis and Design**. It is not an additional degree course and does not replace the OOAD course. Its purpose is to make the learner able to read, write, test, and explain small object-oriented programs so the later course can focus on analysis and design rather than syntax.

## Entry assumptions

The learner should be able to:

- use a computer terminal or integrated development environment;
- create, edit, run, and debug a small program;
- use variables, conditions, loops, functions, and basic data structures;
- use Git or another version-control system at an introductory level.

Choose one language and keep it for the entire bridge: Java, C++, C#, Python, Kotlin, or another language with classes, interfaces or protocols, exceptions, collections, and a unit-test framework.

## Exit gate

The bridge is complete when the learner can, without step-by-step instructions:

1. define classes with clear responsibilities and invariants;
2. distinguish object identity, state, behavior, class, instance, and interface;
3. use composition and explain when inheritance is inappropriate;
4. implement polymorphic behavior through an interface, protocol, or abstract base type;
5. use collections and exceptions without hiding error conditions;
6. write repeatable unit tests for normal, boundary, and failure cases;
7. read a small unfamiliar codebase and sketch its class and interaction structure;
8. restore and run the work from a clean repository checkout.

Recommended threshold: **80%** on the final gate, with no critical defect in test repeatability, object responsibility, or repository restoration.

## Four-week bridge

Plan on **7–10 hours per week**. Extend any week when the learner cannot complete the independent assignment without copying a tutorial solution.

### Week 1 — Objects, classes, state, behavior, and tests

**Outcomes**

- Define classes, constructors, methods, fields, and invariants.
- Separate input/output code from domain behavior.
- Write unit tests before or alongside implementation.

**Practice system:** a small campus mobility fare and eligibility calculator.

**Exercises**

- Implement `Rider`, `Trip`, and `FarePolicy` concepts.
- Write tests for ordinary, boundary, invalid, and accessibility-assistance cases.
- Refactor a procedural solution into collaborating objects.
- Record which responsibilities belong to each object and which do not.

**Deliverable:** source, tests, a one-page responsibility table, and a clean-run script.

### Week 2 — Composition, interfaces, polymorphism, and dependency control

**Outcomes**

- Prefer composition when reuse does not represent a true substitutable relationship.
- Define an interface or protocol and provide multiple implementations.
- Inject dependencies rather than constructing every collaborator internally.

**Exercises**

- Implement fixed, distance-based, and concession fare policies behind one interface.
- Add a clock or pricing-data dependency through injection.
- Write a short comparison of inheritance and composition for the case.
- Identify and remove one high-coupling design choice.

**Deliverable:** revised code, tests, dependency sketch, and design rationale.

### Week 3 — Collections, lifecycle state, exceptions, and persistence boundaries

**Outcomes**

- Use collections to manage groups of domain objects.
- Model valid state transitions explicitly.
- Distinguish expected domain outcomes from exceptional failures.
- Keep persistence mechanisms outside core domain rules.

**Exercises**

- Add trip requests with `Requested`, `Scheduled`, `InService`, `Completed`, and `Cancelled` states.
- Reject invalid transitions with clear behavior and tests.
- Add an in-memory repository interface and implementation.
- Test duplicate identity, missing records, and concurrent-looking update scenarios at a conceptual level.

**Deliverable:** lifecycle model, repository boundary, code, and tests.

### Week 4 — Integrated mini-project and readiness defense

Build a small **Mobility Operations Console** that:

- creates riders and trip requests;
- applies interchangeable eligibility or fare policies;
- schedules, cancels, and completes trips through valid transitions;
- stores and retrieves objects through a repository abstraction;
- reports errors without corrupting state;
- includes at least 20 automated tests.

Submit:

- restorable repository;
- source and test instructions;
- class diagram or equivalent responsibility model;
- two interaction diagrams or structured traces;
- test report;
- 5–8 minute recorded walkthrough;
- a one-page reflection identifying the weakest design decision.

## Critical failures

The learner has not passed the bridge when any of the following remains:

- tests cannot be run from a clean checkout;
- one class owns most unrelated responsibilities;
- inheritance is used where subclasses cannot safely substitute for the base type;
- invalid state transitions silently succeed;
- exceptions are swallowed or used as ordinary control flow without rationale;
- persistence details dominate domain objects;
- the learner cannot explain the difference between analysis concepts and implementation classes.

## Readiness-review questions

1. What is the difference between a class and an object?
2. What is an invariant, and where is it enforced?
3. When is composition preferable to inheritance?
4. What makes two implementations substitutable behind one interface?
5. Why should a unit test be repeatable and isolated?
6. How should invalid domain state differ from infrastructure failure?
7. Why separate persistence from domain rules?
8. Which design change would be hardest in your mini-project, and what dependency causes that difficulty?

A learner who can answer these questions using the submitted code is ready to begin EN.605.704.
