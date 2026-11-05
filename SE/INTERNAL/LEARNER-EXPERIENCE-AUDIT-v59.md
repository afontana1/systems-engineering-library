# Systems Engineering Learning Library v59 — Learner Journey Audit and Repair

## Release purpose

Version 59 follows v58. Its goal is to help a learner move through a complete, coherent sequence — from a question to a concept, from concept to textbook explanation, from explanation to an existing exercise, and back to their place in the library. It is an integration and usability repair release, **not** a new textbook-depth pass or an addition to the assignments.

The existing 240 textbook chapters, 56 canonical encyclopedia references, 1,076 indexed resources, and six comprehensive learning pathways remain available.

## Six curated learning journeys

A new guide at `SE/K/LEARNER-JOURNEYS.html` presents six question-driven scenarios. Each includes two existing canonical concept references, a standalone textbook chapter, an existing laboratory, an explicit learning outcome, and a reflection question:

| Journey | Learning question | Textbook + practice |
| --- | --- | --- |
| Stakeholder needs | How does a vague request become a testable obligation? | Book 1 chapter 3 and laboratory 3 |
| Safety evidence | What evidence supports a bounded safety claim? | Book 8 chapter 10 and laboratory 10 |
| Simulation credibility | When can simulation output inform a design decision? | Book 11 chapter 9 and laboratory 9 |
| Robust trade studies | When would uncertainty reverse the preferred alternative? | Book 14 chapter 11 and laboratory 11 |
| Interface integration | How can an interface contract survive design and configuration changes? | Book 7 chapter 4 and laboratory 4 |
| Model-based engineering | What semantics and traceability defend a function allocation? | Book 3 chapter 7 and laboratory 7 |

Every destination was checked against the existing library. These **24 steps** are curated navigation recommendations. They do not constitute new exercises, grades, completion requirements, or verified learning outcomes.

## What was repaired

1. **Orphaned deep links** — one homepage link to a nonexistent book workshop anchor was redirected to the existing advanced practice collection; twelve links from Phase 4 deep dives now target the full section IDs used by their course companion index.
2. **Graduate-topic book links** — ten reader links used fragment IDs that did not exist in the interactive book HTML. They now point to the corresponding existing standalone graduate chapter and laboratory HTML pages.
3. **Lab catalog shortcuts** — twenty textbook readers formerly linked to `#B1`, `#B2`, etc., which the dynamic lab viewer did not recognize as file paths. They now point to the corresponding book's first existing lab file identifier in the viewer's actual dataset.
4. **Learning continuity** — opting into a journey activates a browser-local context strip on its encyclopedia, chapter, and laboratory pages. That strip links back to the route and forward to its next resource. The study desk shows a link back to the active journey.
5. **Discoverability** — the main library homepage, encyclopedia navigation, and study desk now link to the six scenario journeys. The shared page map recognizes the new guide.

The conventional six extensive, prerequisite-aware pathways remain unchanged. The six new scenarios demonstrate how to connect resources into a short start-to-practice sequence.

## Reproducible offline checks

After extracting the ZIP, run:

```bash
python SE/INTERNAL/LEARNER-JOURNEY-CHECKS-v59.py
```

The script uses only the Python standard library. It examines HTML local target references (including stylesheets and scripts), static fragment identifiers, dynamic lab-viewer file hashes against the embedded catalog, encyclopedia document IDs, and the six journey manifests.

| Static check | Result |
| --- | ---: |
| HTML pages checked | 1,269 |
| Local targets resolved | 23,220 |
| Dynamic lab fragments checked against indexed files | 260 |
| Dynamic encyclopedia fragments recognized and checked | 162 |
| Missing local targets | 0 |
| Broken local fragment anchors | 0 |
| Journeys and navigation steps | 6 journeys / 24 steps |
| Pages without a main landmark | 0 |
| Pages without a page heading | 0 |

Representative Chromium interactions passed **16/16** checks. They covered rendering six paths, step structure, starting and retaining a local journey, opening a deep-linked encyclopedia reference, displaying the reading companion, offering the next lab from a standalone textbook chapter, marking a chapter studied, reflecting that marker in the guide, resuming from the study desk, homepage discoverability, and a 390-pixel mobile overflow check. No uncaught page JavaScript errors were observed in that suite.

## Preservation

Comparison against the v58 ZIP found 3,171 original files: **3,134 byte-for-byte identical**, 37 intentionally modified, and zero deleted. Modifications are confined to navigation links and user-interface assets (home, atlas, book readers, Phase 4 deep-dive HTML links, study desk, shared navigation map and shared shell). All instructional source manuscripts, assignments, original lab contents, datasets, and notebooks are untouched. Additional files are limited to the journey guide, its machine-readable manifest, and release audit/validation material.

## Scope and limitations

- **No live human learner study has been conducted.** The journeys are editorially curated and tested using representative, scripted tasks, not measured comprehension or observed task-success rates from students.
- The test environment blocks native `file://` and localhost/HTTP browser navigation. The Chromium functional checks used direct-page rendering, the locally bundled JavaScript, and controlled localStorage. They are **not** proof of cross-page navigation or state persistence in a particular Windows browser after ZIP extraction.
- Local storage is browser-dependent. The study guide still functions as static links even if progress cannot be saved.
- This work does not independently validate all 240 chapters, test every mathematical expression, certify WCAG conformance, or replace NVDA/VoiceOver testing.

## Manual Windows acceptance checklist

1. Extract the full ZIP to a normal folder with a short path and open `SE/START-HERE.html` in Edge or Chrome.
2. Choose **Open the six learner journeys**. In **Safety evidence**, open the first concept and confirm the next-resource banner; move to the second concept, chapter and lab. Check Back navigation and the guide's return link.
3. On a standalone chapter, mark the page studied. Return to the journey guide and confirm the studied indicator. Close and reopen the browser and check the result; note browser-specific limitations.
4. On a book reader, open the lab catalog shortcut and confirm it selects a real lab source instead of a blank or unrecognized category hash.
5. Try the Phase 4 deep-dive “Related course lessons” link and one graduate chapter/lab link in Book 2, 9, 12, 13 or 14.
6. Repeat the safety journey with keyboard only (Tab, Shift+Tab, Enter, Escape), then at narrow viewport and high zoom. Test with NVDA or VoiceOver if possible.

## Subsequent priority

Run a small, real usability study with novice and experienced learners using a locally extracted Windows copy. Record whether each participant can find, understand, practice, and resume material, the number of backtracks or dead ends, and their comprehension of the next step. Use those observations to decide the next set of interface changes.
