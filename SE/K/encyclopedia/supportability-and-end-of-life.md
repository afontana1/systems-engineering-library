# Design for supportability, lifecycle sustainment, and end-of-life

**Reference entry · Design maturation, service engineering and lifecycle economics**

## Support is an architectural concern

Operational systems depend on enabling products: spares, tools, service instructions, technicians, data systems, suppliers, calibration services, and disposal paths. An architecture that meets initial throughput but cannot be repaired promptly may fail the mission. **Supportability** is the designed ability to keep restoring required service, not just the maintenance plan written after hardware selection. At concept and design reviews, quantify access, diagnosis, replaceability, sparing, interoperability, obsolescence risk, training burden and safe end-of-life handling.

Availability is not reliability. In a simple renewal approximation with independent alternating operating and repair times, inherent availability is

\[
A_i=\frac{\mathrm{MTBF}}{\mathrm{MTBF}+\mathrm{MTTR}}.
\]

An illustrative component with mean time between failures 200 h and mean corrective repair time 4 h has \(A_i=200/204\approx98.04\%\). That ignores logistics waiting, preventive maintenance, shared failures and mission scheduling. Operational availability requires a boundary that includes supply and administrative delays; a service-level denominator is not automatically component operating hours. If replacement requires a rarely stocked device, spares dominate real-world recovery.

## Worked discounted maintenance decision

Suppose a fictional subsystem redesign costs $70,000 now and is projected to avoid $18,000 in maintenance per year for six years, with year-end savings and a 4% annual discount rate. Its savings present value is

\[
PV=18{,}000\sum_{t=1}^{6}(1.04)^{-t}
=18{,}000\frac{1-(1.04)^{-6}}{0.04}
\approx\$94{,}358.
\]

The **net present value of maintenance savings alone** is approximately $24,358. The comparison omits operating disruption, additional training, energy impacts, risk, taxes, salvage, inflation and component life. The positive sign is conditional, not proof the redesign should be selected. For example, a mandatory capacity or safety constraint may favor a different design even if its financial NPV is lower.

## Spares and service constraints

A spares strategy needs demand distributions, replenishment time, supplier dependency, interchangeability and criticality. Using average demand alone hides stockout tail risk. For a simple Poisson demand model with mean \(\lambda=2\) units during replenishment lead time, the probability demand exceeds 3 stocked units is

\[
P(N>3)=1-e^{-2}\left(1+2+\frac{2^2}{2!}+\frac{2^3}{3!}\right)\approx0.1429.
\]

This is a **14.3% hypothetical lead-time stockout probability** for that simplistic model. A shared supplier outage or surge would change the distribution. Check the assumption rather than interpreting this number as field assurance.

## Engineering artifacts and lifecycle decisions

A complete design-for-support package includes: replaceable-unit breakdown and accessibility drawing, failure-detection coverage, maintenance task analysis, support equipment list, sparing rationale, supplier and obsolescence controls, reliability growth evidence, operator training concept, hazardous-material register, and disposal/recycling procedure. Every requirement should identify an owner, verification method, and operating configuration. A closed-loop sustainment review links observed failures and repair delays to revised design and lifecycle-cost assumptions.

## Exercise and answer

If repair time doubles from 4 h to 8 h at the same 200 h MTBF, inherent availability drops to \(200/208\approx96.15\%\). Show why a robust spare-parts plan could improve **operational** recovery without changing intrinsic component failure rate; distinguish a replacement time reduction from a reliability improvement. Name two end-of-life obligations that a cost-only portfolio would miss.

## Limits and primary sources

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — enabling products, operations, technical assessment and lifecycle support.
- [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — distribution models, uncertainty and reliability methods.

Related: [reliability/availability](reliability-availability-maintainability.md), [lifecycle economics](lifecycle-sustainment-economics.md), [supply-chain assurance](supply-chain-assurance-and-provenance.md). All figures are synthetic, and the simplistic availability and stockout models require project validation.
