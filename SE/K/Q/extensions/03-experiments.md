## Step 04 integrated case — a blocked \(2^2\) quantitative experiment

A useful experiment changes factors while holding the stochastic demand streams comparable. NS-QSE4.1 evaluates two policy factors on *twelve shared synthetic storm days*: factor \(A\) changes available parallel dispatch servers from two to three; factor \(B\) changes deterministic service duration from 10 to 8 minutes/request. The response \(Y\) is the **equal-day average of each day's mean waiting time**, in minutes, before service starts. The four cells do not establish real causal effects: their outcomes are causally defined **inside the model**, which excludes several potentially decisive physical mechanisms.

### Construct the factorial contrast

Let \(Y_{00}\) be two servers/10 minutes, \(Y_{10}\) three servers/10 minutes, \(Y_{01}\) two servers/8 minutes, and \(Y_{11}\) three servers/8 minutes. Controlled simulation gives:

| Factor setting | Mean of daily mean waits, min |
|---|---:|
| \(Y_{00}\), baseline | 16.880 |
| \(Y_{10}\), capacity | 5.368 |
| \(Y_{01}\), process | 10.032 |
| \(Y_{11}\), combined | 2.346 |

With factors coded \(-1,+1\), the **average main effect** of capacity is \(\widehat E_A=(Y_{10}+Y_{11}-Y_{00}-Y_{01})/2=-9.598\) minutes. The process effect is \(\widehat E_B=(Y_{01}+Y_{11}-Y_{00}-Y_{10})/2=-4.935\) minutes. The difference-in-differences is \(\Delta_{AB}=Y_{11}-Y_{10}-Y_{01}+Y_{00}=+3.826\) minutes. Under effect coding, the regression coefficient of the \(AB\) interaction is \(\widehat\beta_{AB}=\Delta_{AB}/4=+0.9566\) minutes. **Do not** confuse the interaction contrast with its coded regression coefficient. The positive interaction indicates diminishing combined benefit relative to simply adding the individual wait reductions on this response scale; it does not imply that combined service gets worse.

### Experimental units, paired blocks, and generalization

The day is the independent design unit in this controlled simulation. The per-request observations within a day share the generated environment and must not be treated as independent day replicates. The common-random-number construction pairs policy outputs within a day. The report provides a 2,500-resample paired interval for baseline minus combined daily mean wait of about **10.86–18.01 minutes**. Its uncertainty is conditional on only twelve synthetic days and a uniform-within-hour arrival generator, not on a measured population of emergency days.

A physical experiment would also randomize dispatch interventions where ethics and operations permit, block by weather, workload and shift, register deviations, and preserve safety and accessibility constraints. In an observational before–after pilot, concurrent roadworks, staffing changes, or seasonal demand can confound the policy comparison. Interaction estimates may also change if one reports p90 wait or abandoned requests rather than average waiting time.

### Adverse diagnostic

A policy can appear efficient because it completes service **after the one-hour intake window**. The simulator records `overtime_completions`; it does not silently drop those trips. A valid design-of-experiments report must say whether such overtime is allowed or charged to the next shift. Try a slower service time and observe both the waiting response and overtime fraction; an apparent improvement in one metric alone is not sufficient.

<details><summary>Worked exercises and interpretation</summary>

1. **Main effect.** Using the table, verify capacity effect: \((5.368+2.346-16.880-10.032)/2\approx-9.599\) minutes. Rounding causes a small difference from the full-precision result.
2. **Interaction.** Calculate \(2.346-5.368-10.032+16.880=3.826\) minutes. If \(\Delta_{AB}=0\), the two factors are additive on the specified response scale, not necessarily on reliability or cost scales.
3. **Confounding.** What if all high-capacity tests occur in clear weather and all low-capacity tests in storms? Capacity and weather are confounded; a difference in outcomes cannot be attributed uniquely to capacity. Block or randomize and collect weather-specific evidence.

</details>

The editable inputs, daily response CSV, and analysis code allow students to repeat the factorial contrast or intentionally change the response definition; such changes must be recorded as a **new analysis configuration**.
