# v57 — Intelligent Discovery and Search

## Purpose

Improve finding and resuming learning materials across the existing Systems Engineering Learning Library. This release changes navigation and search behavior, not the subject-matter teaching text, laboratory content, or assessments.

## Offline search design

- **Plain-language questions:** 14 curated engineering question families suggest four relevant canonical concepts and an applicable learning route where available. This is an editorial topic mapping, not a generated answer or an AI semantic search service.
- **Engineering vocabulary:** 18 abbreviation and terminology groups map terms such as MBSE, FMEA, MTBF, ConOps, DOE, CI/CD, SoS, and digital twin to useful subjects without conflating their definitions.
- **Explainable ranking:** title, reference summary, course context, and document text contribute differently to relevance. Results explain whether they are curated starting points, strong title matches, full key-term matches, or related keyword matches.
- **Separate resource types:** concept references for lookup, textbook chapters for deeper study, existing labs for application, and supporting resources for further reference. The existing content-type selector remains available.
- **Search recovery:** suggested corrections appear for certain zero-result spelling mistakes. Fewer terms or All sources remain valid fallback strategies. No result should be mistaken for proof that every element of a question has been answered.
- **Learning continuity:** search-to-article-to-search navigation retains the query in the offline URL fragment; browsing, study markers, and route navigation remain intact.
- **Homepage:** search prompt now explains question and abbreviation searching, with three direct example questions.
- **Privacy:** all ranking and query parsing are local. No external API, account, server, analytics or generative model is required for the search feature. Browser-local study progress is subject to browser file-storage restrictions as before.

## Release QA

Source master: **v56**. Corpus and textbook contents are not rewritten.

- Retained: **1,076** indexed resources, **56** canonical concepts, **240** textbook chapters, and all existing learning routes, coursework, labs and course guides.
- The full extracted source tree was scanned for missing relative HTML file targets: **1,267 HTML files**, **20,722 local relative links**, **0 missing files**, **0 folder-only links** at time of the check.
- **3,159** original v56 files were byte-for-byte unchanged; only `SE/START-HERE.html` and three atlas interface files were edited. Added this report, a standalone offline search module and an optional Node.js smoke test.
- Local test: `node SE/INTERNAL/SEARCH-v57-SMOKE.js` passes **11 curated-question checks**, **one typo recovery**, **two resource filters**, and index consistency checks (no external packages).
- Representative Chromium direct-page interaction tests passed for queries, ranked results, link-to-article reading, return-to-search, spelling suggestion, concept filtering, lab filtering, and **390 px** mobile width without JavaScript page errors or horizontal overflow.
- Windows-friendly maximum internal path length: **94** characters.
- The ZIP integrity test must be completed as part of packaging.

## Outstanding quality checks

This execution environment blocks navigation to extracted `file://` pages, so full native offline clicking and history behavior across multiple files could not be verified in Chromium. Direct-page rendered interactions and static local-link resolution were tested separately. The library-wide accessibility audit, screen-reader testing, learner usability studies, and mathematical correctness review are outside this release's scope. Synonym, question-family and ranking rules are a deterministic curated search aid and will not understand every natural-language question.

## Manual acceptance scenarios

1. Extract ZIP and open `SE/START-HERE.html` without internet access. Try **How do I prove my design is safe?**; choose the safety reference and return to the same query.
2. Try **MBSE**, **MTBF**, **FMEA**, and **digital twin**. Confirm relevant reference concepts occur near the beginning.
3. Search **simulation test** with **Labs** selected. Verify the results are practice resources.
4. Type **reliablity** and click the suggested spelling correction.
5. Open a related textbook chapter, return to the atlas and resume the original learning route.
6. Test on narrow screens, keyboard only, and a browser with local storage disabled. Search should still work, while personal study markers may not persist.
