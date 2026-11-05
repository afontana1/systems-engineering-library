# Encyclopedia Reconstruction · v48 · Stage 1

## Editorial objective
The textbooks teach progressively; the encyclopedia is a reference for looking up a concept, understanding its mechanisms and limits, and navigating to deeper explanations, evidence and related concepts. This stage repairs search and establishes the canonical editorial structure without altering assignments or the 240 textbooks.

## Scope delivered
- **40** existing concept records catalogued, with explicit editorial statuses.
- **12** independently reconstructed Markdown concept articles, each including conceptual mechanism, a worked illustration, assumptions, limitations, and cross-disciplinary links.
- **28** earlier primers retained in place and marked as awaiting reconstruction. Their repeated v8 sections have not been certified as graduate-level references.
- **1060** unified records retained with original stable identifiers and normalized searchable text and snippets. The v47 schema had **177** records missing nonempty `text`; those were rebuilt using original `searchText` where available and embedded document HTML otherwise.
- All **240** textbook chapters remain inside the unified reader and are reachable through full-text search. Curated book-chapter links are provided for the 12 reconstructed concepts.
- The offline HTML reader has been redesigned around concept lookup, subject browsing, and cross-references. It preserves `#doc=<id>` links to all historical records.
- A–Z static HTML index, editable Markdown index, machine-readable JSON catalog, and CSV editorial status are available.

## Editorial state
Reconstructed concepts (12): boundaries-and-interfaces, digital-thread-and-twin, engineering-trades, functional-vs-physical, good-requirements, model-vv-and-credibility, probability-and-dependence, sos-characteristics, stakeholders-and-needs, system-of-interest, traceability-graph, v-and-v.

These are substantial illustrative references, **not independently peer-reviewed standards compliance determinations**. Mathematical, pedagogical, and technical subject-matter reviews across the entire collection remain to be done. Original sources and all labs are preserved, not rewritten.

## Verification results

- v47 master archive: 3075 files; v48 master: 3080 files.
- Changed pre-existing files: 29; newly added: 5; untouched and byte-for-byte identical: 3046.
- All 1,060 records have nonempty normalized search fields; stable ID uniqueness and 240 textbook records confirmed.
- All 124 checked local links in the 12 rebuilt standalone articles resolve, and 36 curated book-chapter links target existing indexed chapters.
- Chromium inline-content smoke tests: 40 concept cards, 12 rebuilt labels, search, reconstructed entry, legacy book chapter, and legacy primer displayed without JavaScript page errors. Direct file navigation was blocked by the test environment; a full interactive file:// navigation audit remains outstanding.
- ZIP integrity check passed; maximum archive path length 94 characters.

## Verification plan
1. Compare archive entries against v47 and confirm that only the reference system, v48 assets, 12 Markdown/HTML entries and new status files changed.
2. Validate all 1,060 records have nonempty `text`, `excerpt`, and `searchText`, unique stable IDs and valid article URLs.
3. Use Chromium to search terms that failed in v47, open reconstructed and legacy entries, follow cross-references, and test browser back/forward.
4. Confirm the 240 book chapters and the original 40 primer sources remain present.
5. Verify standalone article and local link paths; check Windows path lengths and ZIP integrity.

## Next editorial batches
Prioritize the 28 original primers by use and prerequisite centrality, not an arbitrary word target. Then perform concept overlap/contradiction reviews against the 240 textbooks, notation and derivation audits, accessible math rendering, search ranking tests and link-health checks across the full archive. Extend curated links from 12 concepts to all 40 and validate definitions against primary standards and authoritative sources where relevant.

## Preservation rule
The historical v47 course guides, assignments, labs, and 240 textbook source chapters are not revised in this release. Only encyclopedia assets, 12 reference articles, navigation entry points and documentation are changed.
