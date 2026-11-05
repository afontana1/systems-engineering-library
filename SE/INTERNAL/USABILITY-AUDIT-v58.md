# Systems Engineering Learning Library v58 — Usability and Accessibility Audit

## Scope and outcome

v58 is a targeted usability and structural accessibility repair release based on the complete v57 master. It does **not** add or rewrite learning content. It retains the 240 existing textbook chapters, 56 encyclopedia concepts, six guided routes, and the existing courses, labs, and practice files.

The audit covered all **1,268 HTML documents** using a reproducible Python standard-library parser and checked **20,736 local link targets**. A representative Chromium interaction suite passed **24 of 24 tests**. This is evidence of specific tested behaviors, **not** WCAG certification or a comprehensive assistive-technology audit.

## Defects corrected

1. **Shared navigation and keyboard usability:** enhanced study-drawer focus, closing with Escape and returning focus to the trigger, announcements for save/studied updates, full small-screen previous/next links, larger search controls, and a proper homepage skip link.
2. **Encyclopedia navigation and search:** focus transfers to the new view heading when hash navigation changes the active view; filter buttons expose `aria-pressed`; active view navigation exposes `aria-current`; result counts announce changes; long formulas and code receive overflow treatment, with reduced-motion support.
3. **Structural landmarks and headings:** added `main` to four older practice indexes and `h1` to nine resource indexes without altering their educational content.
4. **Control names:** added explicit accessible search names to three older book readers.
5. **Duplicate SVG IDs:** scoped repeated IDs in four phase readers and updated local SVG references; no remaining duplicated static document IDs were detected.
6. **Help and discoverability:** added `K/ACCESSIBILITY-HELP.html`, linked from the homepage and encyclopedia and through the shared study controls.

## Verified post-repair structural audit

| Check | Result |
| --- | ---: |
| HTML pages parsed | 1,268 |
| Relative local links resolved | 20,736 |
| Missing page `main` landmarks | 0 |
| Pages missing `h1` | 0 |
| Missing document `lang` or title | 0 |
| Documents containing duplicate IDs | 0 |
| Inputs without programmatic labels in static HTML | 0 |
| Missing file targets or folder-only targets | 0 |

The audit is reproducible using `python SE/INTERNAL/ACCESSIBILITY-STATIC-CHECKS-v58.py` after extracting the archive. Checks use the Python standard library only.

## Representative browser interactions

The 24/24 functional checks cover the shared navigation, skip targeting, drawer visibility and focus, Escape focus restoration, saved control state and status message, the `/` search shortcut, homepage skip/resume panel, 56-concept atlas load, hash-route focus, A–Z filter semantics, question search, announced result counts, opening and reading an article, responsive chapter previous/next links, and mobile overflow. Tested page JavaScript produced no uncaught errors. Screenshots were captured for chapter, homepage, search, article and 390px mobile views.

**Environment caveat:** Chromium rejected all native `file://` and localhost URL navigations with `ERR_BLOCKED_BY_ADMINISTRATOR`. Browser tests used rendered page contents with local bundled scripts injected and simulated localStorage. Relative-file integrity was verified separately. This is not an end-to-end native offline navigation test.

## Preservation

All existing non-HTML instructional files (Markdown manuscripts, CSV worksheets, notebooks, Python, diagrams, JSON data, and other bundled data) were compared against v57 and remain byte-for-byte unchanged. HTML changes are limited to specified navigation, names, headings, landmarks, and SVG identifiers. No assignments or labs were added, removed, or revised.

## Accessibility limits and next validation work

This release removes detected structural defects but does not prove WCAG 2.2 AA compliance. A real extracted-folder test on Windows, keyboard-only complete workflows, native browser storage behavior, NVDA/VoiceOver screen-reader sessions, 200–400% zoom testing across diverse diagrams, complete non-text equivalent review, mathematical notation accessibility, and exploratory learner studies are still recommended. The sampled foreground/background contrast combinations exceed 4.5:1, but this is **not** a full color and non-text contrast audit.

### Manual verification scenarios

1. Extract the master ZIP locally and open `SE/START-HERE.html`. Tab to the skip link, activate it, then navigate to a textbook chapter and check visible focus and previous/next links.
2. Open the study drawer, Tab through saved resources, press Escape, and verify focus returns to the Study list button.
3. Search the encyclopedia for “How do I prove my design is safe?”, open a concept, follow a related concept, use the article outline, and return to search with keyboard alone.
4. Mark a chapter studied, close and reopen the browser, and confirm whether your specific browser preserves progress from local files; some browsers may not.
5. At narrow mobile width, 200% zoom and with a screen reader, inspect navigation, article headings, math, diagrams and labeling for issues not captured by the automated suite.

## Audit artifacts

- `SE/INTERNAL/USABILITY-VALIDATION-v58.json`: machine-readable test results and preservation summary
- `SE/INTERNAL/ACCESSIBILITY-STATIC-CHECKS-v58.py`: offline, dependency-free static validation tool
- `SE/INTERNAL/USABILITY-CHANGED-FILES-v58.json`: exact set of modified and added paths
- `SE/K/ACCESSIBILITY-HELP.html`: reader-facing keyboard help and known limitations
