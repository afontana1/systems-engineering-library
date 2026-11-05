# From arrivals to waiting-time distributions

**Cross-course pathways:** Simulation Foundations 4–8; Metrics 2 and 9; Systems Dynamics 5.

## Separate event time from state

In discrete-event simulation (DES), time advances from one scheduled event to the next. The state may include `busy`, the waiting queue, resources, number served and the event calendar. At time t, process all relevant event types with deterministic tie rules; then schedule future events. Two critical assertions are that no resource serves two jobs simultaneously and every completed job must have entered the system.

A minimal example has arrivals at minutes `[0,1,2]`, one server and constant three-minute service. The first starts at 0 and leaves at 3. The second starts at 3, waits two minutes and leaves at 6. The third starts at 6, waits four minutes and leaves at 9. Mean waiting is `(0+2+4)/3=2` minutes. Run both `deterministic_queue` and `des_queue` to confirm this known-answer fixture. A code trace is more informative than an animation for detecting double booking.

## Analytic queueing model and its limitations

For a stationary M/M/1 queue with Poisson arrival rate λ, independent exponential service rate μ and λ<μ, utilization is `ρ=λ/μ`. Expected total time in system is `W=1/(μ-λ)`, queue wait is `Wq=λ/[μ(μ-λ)]`, and expected number in system is `L=λW` by Little's law. If λ=8/hour and μ=12/hour, `ρ=2/3`, `W=0.25 h=15 min`, and `Wq=8/(12×4) h=10 min`. These are *steady-state expectations*, not 95th percentiles or guarantees. At λ≥μ the ideal stationary mean diverges.

## How to analyze a simulation

Define horizon, initial queue, arrival regime, service discipline, abandonments and replications. If studying the 8–9 a.m. rush period, starting with an empty queue may be appropriate *if that is the real state at 8 a.m.*; applying warm-up to remove the rush period would be wrong. If studying long-run behavior, quantify warm-up bias and serial correlation. Report variation across independent replications, not across adjacent timestamps.

**Exercise:** Keep μ=12 and increase λ from 8 to 11. Why does `W` triple from 15 to 60 minutes even though arrival rate rises only 37.5%? **Answer:** queueing delay grows nonlinearly as slack capacity `μ-λ` shrinks from 4 to 1/hour.

**Boundary:** Real dispatch is multi-server, possibly priority-based, transient, spatial and state dependent. M/M/1 gives intuition, not automatic design acceptance.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
