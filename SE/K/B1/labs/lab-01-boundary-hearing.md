# Hypothetical Lab 1 — The Boundary Hearing

**Course link:** EN.645.662 Week 1 · **Book:** [Chapter 1](../chapters/01-what-is-the-system.md) · **Time:** 75–110 minutes · **Type:** paper-and-pencil engineering review.

## Situation

The fictional campus is planning a shuttle pilot. The procurement director wants a vehicles-only contract. The student-access office wants the campus to own booking, vehicle dispatch, alerts, and boarding assistance as one service. A third-party vendor offers dispatch as a separately licensed system. No proposal is automatically correct; your job is to make the accountability consequences legible.

## Evidence packet

In this fictional scenario, three vehicles operate from six stops. Booking, charging, and route permissions currently rely on campus services. The procurement director estimates the vehicle-only purchase at $420,000; campus-side integration, training, and support are tentatively $90,000, $35,000, and $50,000 respectively. The full-service offer is $510,000 plus tentative identity integration and oversight at $20,000 and $15,000. These are planning numbers only: uncertainty, overlap, cost years, and scope equivalence have not been evaluated.

## Your work

1. Write the *specific decision question* for the pilot acceptance authority. If it concerns passenger mobility, explain why vehicle uptime is insufficient.
2. Draw two boundaries. For each, name at least six external exchanges and the owner of the crossing. Include people and procedures.
3. Draft a contract for the booking-to-dispatch interface: request ID, timestamp convention, accepted/rejected states, timeout, duplicate handling, and owner of exception response.
4. Compute normalized *illustrative* costs, then identify at least three reasons the two figures are not yet credible comparable life-cycle estimates.
5. Write a five-sentence review recommendation. It must contain a condition under which you would change your recommendation.

## Deliverables

Produce `LAB01_BoundaryHearing.md`, `LAB01_ContextA.svg` or drawing, `LAB01_ContextB.svg` or drawing, and a six-row interface register. The larger original Week 1 assignment remains separate.

<details><summary>Reference response and teaching critique — reveal after attempting</summary>

For a service acceptance question, Boundary B is generally more coherent because booking-to-trip outcomes become the program-level obligation. Boundary A can still be reasonable for vehicle procurement if the campus explicitly assumes integration and end-to-end assurance. Illustrative normalized figures: A = $420,000 + $90,000 + $35,000 + $50,000 = **$595,000**; B = $510,000 + $20,000 + $15,000 = **$545,000**. They are **not** comparable validated costs: operating support duration, fleet warranties, contingency, escalation support, cybersecurity, and retirement are not harmonized. A defensible review finding is that network-loss behavior and interface ownership need explicit commitments before either option is declared ready.

A poor response draws boundaries without explaining why the decision changes with boundary choice. A stronger response identifies transferred obligations and the evidence needed to manage those obligations.

</details>

## Debrief

Ask whether the *selected boundary* makes the acceptance result more valid, or merely makes a supplier look more successful. Then return to [the original Week 1 rubric](../../../C/P0/EN645662.md) and assemble the formal controlled memo.
