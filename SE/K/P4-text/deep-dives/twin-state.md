# Digital twins: state, synchronization, trust and intended use

**Concept essay · EN.645.782 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

A digital twin connects a referent to a model for a declared purpose. The connection may be periodic or continuous, but synchronization and predictive fidelity must be quantified relative to what the model claims to do. Some applications need an accurate historical state; some need forecasts; others actively influence operations. These demand progressively stronger timing, safety and cybersecurity controls.

### Time alignment

Let `t_obs` be the time a sensor measured a state, and `t_used` the time a decision used it. Freshness age is `Δ = t_used − t_obs`. If a dispatch decision is updated every 30 seconds but battery health is sampled every 20 minutes, an out-of-date twin may still help maintenance planning but should not be treated as current operating truth.

Measurement error also matters: twin prediction error can be decomposed into sensor error, state-estimation error, model-form error and mismatch in operating context. These errors need not be independent. Confidence statements must specify calibration conditions and time horizon.

### Threat and failure modes

* Stale or reordered telemetry creating false state.
* Incorrect binding between physical asset ID and model instance.
* Spoofed updates that appear plausible but violate physics.
* Model drift when software or hardware changes.
* Unavailable network links causing confident but stale predictions.

### Worked fallback

When freshness exceeds five minutes during charging, a maintenance twin labels its state **stale** and suppresses optimization recommendations. It preserves the last valid observation and requests operator confirmation. For dispatch, a separate approved local-state controller continues operating within a conservative envelope.

**Exercise.** Define the maximum acceptable freshness age for three uses: weekly maintenance scheduling, immediate boarding release and offline fault analysis. Explain why these limits differ.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645782) · [Further reading](../RESOURCE-SHELF.md)
