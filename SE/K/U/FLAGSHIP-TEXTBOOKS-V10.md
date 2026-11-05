# v10 · Five additional textbook-depth domains

Open [the unified offline encyclopedia](OPEN-ENCYCLOPEDIA.html) and choose **Textbook-depth chapters**. The **F01–F04** sequence from v9 remains available and unchanged. New additions:

1. [F05 — Software-intensive architecture](flagships/F05-software-intensive-architecture.md) · contracts, retries, state invariants, security, failure modes · [notebook](flagship-notebooks/05-software-architecture.ipynb).
2. [F06 — Optimization and control](flagships/F06-optimization-and-control.md) · feasible design, Pareto analysis, KKT reasoning and feedback stability · [notebook](flagship-notebooks/06-optimization-control.ipynb).
3. [F07 — Human factors and safety](flagships/F07-human-factors-and-safety.md) · unsafe control actions, operator workload and safety argumentation · [notebook](flagship-notebooks/07-human-factors-safety.ipynb).
4. [F08 — Simulation and uncertainty](flagships/F08-simulation-uncertainty.md) · replication uncertainty, dependence, factorials, numerical and model credibility · [notebook](flagship-notebooks/08-simulation-uncertainty.ipynb).
5. [F09 — Enterprise and SoS](flagships/F09-enterprise-systems-of-systems.md) · governance, emergence, portfolio dependencies and adaptive transformation · [notebook](flagship-notebooks/09-enterprise-sos.ipynb).

## Contents and use

The five new chapters include **44 fully explained exercises**, five editable Graphviz/SVG diagrams, five standard-library Python modules with 29 tests, five notebooks and five CSV worksheets. Source Markdown is editable and the standalone HTML is designed for offline reading/search. The notebooks require the extracted archive and local Python/Jupyter; browser HTML does not execute them.

### Recommended progression

F01 → F05 → F07 reinforces how software and human constraints affect assurance. F02 → F06 → F08 connects decision models, optimization and quantified evidence. F04 → F09 connects dynamic feedback to cross-agency coordination. These are recommended learning paths, not formally validated course prerequisites.

### Limitations

All scenarios and numeric inputs are invented instructional cases. Methods and tests are **not** externally reviewed engineering certifications. Risk and availability models are deliberately simplified; when using professional systems, consult current authoritative standards and domain specialists. Local Markdown code examples have been executed in a test environment, but no operational service is assessed.

References: [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [SEBoK](https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_%28SEBoK%29), [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).
