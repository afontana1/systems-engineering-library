# Reliability, redundancy and the cost of assumptions

*Phase 2 concept library deep dive · Independent instructional synthesis*

## What probability describes
Reliability is a probability of successful function across a specified time or demand under stated conditions. A component marked "99% reliable" is meaningless until the mission length, operating envelope and failure definition are known. In serial systems, independent component reliabilities multiply: for two required elements with `R1 = R2 = 0.98`, `Rsys = 0.9604`. In redundant parallel success, the independent failure probabilities multiply: `Rsys = 1 − (1−R1)(1−R2) = 0.9996` for the same two components.

The arithmetic is not the main difficulty. **Independence is.** If both branches share a power bus, network, software library or maintenance procedure, a common cause can defeat both. Introduce a simple shared common-cause success probability `q` that must hold before independent branches can operate: `Rsys ≈ q × [1 − (1−p)^2]`. If `q = 0.99` and each branch `p = 0.98`, then `Rsys ≈ 0.989604`, much less than the idealized 0.9996. This is still only a schematic model; common-cause analyses can require more detailed mechanisms.

## Repair changes the objective
Steady-state inherent availability under a particular repairable-system model is `A = MTBF/(MTBF+MTTR)`. At MTBF 500 h and MTTR 5 h, A is approximately 0.9901. It excludes waiting for spares, operator response, transport, scheduled outages and logistical downtime. A repairable component can be reliable over a short mission but operationally unavailable because repair support is slow. Identify what "time down" includes.

## Test planning matters
A high numerical reliability claim demands evidence across relevant demands, environments and time. A few no-failure demonstrations do not prove extremely low rare-failure rates. Reliability analysis should inform architecture, fault detection, maintainability provision and test design together. Different failure modes may warrant different measures: rate of hazardous failures, mean downtime, probability of service loss or safe degradation.

## Exercise with answer
Two independent branches each have 0.95 reliability, but a shared common-cause element has 0.98 success. The illustrative system probability is `0.98 × [1 − (0.05)^2] = 0.97755`. **Lesson:** redundancy's benefit can be dominated by a 2% shared failure chance. Improve architecture by separating the common cause or explicitly designing a safe degraded state; merely adding a third dependent branch may do little.

[Back to Phase 2 companion index](../README.md)
