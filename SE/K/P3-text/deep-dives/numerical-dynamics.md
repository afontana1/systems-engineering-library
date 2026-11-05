# Differential equations and solver error from first principles

**Cross-course pathways:** Advanced M&S 2–4 and 11; Systems Dynamics 5–8.

## Derive a state equation from a balance

Choose temperature T (°C) as a state, ambient temperature Ta and positive cooling coefficient k (1/min). In a well-mixed single-node cooling approximation, heat loss is proportional to temperature difference: `dT/dt=-k(T-Ta)`. Separate variables: `d(T-Ta)/(T-Ta)=-k dt`; integrate to obtain `T(t)=Ta+(T0-Ta)e^(-kt)`.

For T0=50°C, Ta=20°C, k=0.1/min and t=10 min, `T(10)=20+30 e^-1≈31.036°C`. This closed-form solution is an oracle for testing a numerical integrator. Do not interpret the result as a validated battery thermal model: real packs have distributed states and changing heat production.

## Explicit Euler, step size and stability

For a general ODE `dx/dt=f(x,t)`, Euler uses `x_(n+1)=x_n+h f(x_n,t_n)`. Here, `T_(n+1)=T_n-hk(T_n-Ta)`. Define error against the analytical solution, halve h and check the expected trend. For this linear homogeneous deviation, the Euler amplification factor is `(1-hk)`; absolute stability requires `|1-hk|<1`, i.e. `0<hk<2`. Even stable steps can be inaccurate or give nonphysical oscillations when h is too large.

Use `euler_cooling(step_min=1)` and compare with `step_min=0.1`. Inspect conservation and signs as additional checks. More complex stiff systems may require implicit methods and solver diagnostics.

## Hybrid switching is a separate issue

A controller that turns cooling on at 40°C and off at 37°C creates a hybrid model with continuous temperature and discrete switch state. A large time step can overshoot thresholds and miss rapid events. A real-time fixed-step implementation trades computation deadlines against event accuracy. Study hysteresis, event detection and end-to-end response rather than only smooth thermal trajectories.

**Practice:** derive the time to cool from 50°C to 35°C. **Solution:** `35=20+30e^(-.1t)` gives `e^(-.1t)=0.5`, so `t=ln(2)/0.1≈6.931 min`.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
