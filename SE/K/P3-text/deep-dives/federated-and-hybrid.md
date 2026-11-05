# Coupling simulators without coupling their errors

**Cross-course pathways:** Advanced M&S 4–8 and 11; MBSE Analytics 6 and 10.

## Interoperability has three layers

Syntactic interoperability means tools exchange structured bytes. Semantic interoperability means each side agrees what those bytes *mean*, including unit, coordinate frame, clock, causality and operational range. Dynamic interoperability means the coupling accurately handles time advancement, events, delays and conservation. Success at one layer does not prove the others.

The Functional Mock-up Interface (FMI) is a standard format/API for exchanging dynamic simulation models as Functional Mock-up Units, with different types for model exchange, co-simulation and scheduled execution. Its specification defines interfaces, not universal numerical correctness. HLA provides federation mechanisms for simulation interoperability; one must still make application-specific time and ownership decisions.

## Step exchange and delay

Suppose the propulsion simulator integrates at h=0.01 s and the fleet/dispatch simulator communicates once each second. On a fast controller event, the dispatch side sees up to roughly 1 s of stale physical-state information depending on the handshake. A solver refined to 0.001 s inside propulsion does not eliminate interface staleness. Refine *communication* step, evaluate event-driven exchange, or establish a safe bounded interpolation with explicit error justification.

If electric input power is 10 kW with 85% mechanical efficiency, then heat and other losses total 1.5 kW. A coupled thermal module receiving 0.6 kW either omits a loss path or violates the energy accounting. Reconcile flows at interfaces with a declared system boundary.

## Hybrid state and event handling

Continuous temperature may cause a discrete cooling mode to switch on at 40°C and switch off at 37°C. Hysteresis helps avoid chatter; the simulator must detect threshold crossings, handle exactly simultaneous events and restore consistent continuous states. Fixed-step real-time simulation needs deadline margin and safe test isolation; a model that runs offline does not automatically fit hardware-in-the-loop execution.

**Checklist:** model manifest; typed variables; clocks; owner; initialization; scenario; time sync; event priority; conservation; step-refinement evidence; failure behavior; baseline revisions.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
