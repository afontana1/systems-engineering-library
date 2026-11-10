# UI and static-site simplification

This revision is intended for a small, static GitHub Pages learning website.
No student account, progress tracking, application cache, or backend is required.

## Navigation

- Reworked `index.html` into a simpler, search-first homepage.
- Added `SE/K/CONCEPTS.html`, a fast directory of all 56 canonical reference concepts grouped by seven subjects. It has live keyword filtering and links directly to standalone reference pages.
- Replaced the former shared study/navigation shell with a compact site-wide menu (concepts, subject guides, books, labs, courses), simple search, and a source-location breadcrumb.
- Removed the 395 KB shared learning map JS; the navigation no longer downloads it on each page.
- Kept the existing textbook, course, lab, encyclopedia and reference URLs to avoid breaking thousands of internal/external links. The optional deep-search atlas remains available.

## State and clutter

- Removed study-history, bookmarked, saved, and marked-studied features from the shared navigation and interactive atlas.
- Disabled historical completion storage within older standalone book/lab readers and hid the associated controls. Their reading content and chapter/lab navigation remain.
- `SE/K/STUDY-DESK.html` now redirects to the new concept directory for backwards compatibility.
- Removed `SE/INTERNAL/`, preserving its two active deployment checks as `scripts/check_links.py` and `scripts/check_search.js` and updating GitHub Actions accordingly.

## Mathematical notation

- Continued using the **bundled offline MathJax** engine rather than introducing an online KaTeX dependency.
- Converted 249 inline mathematical expressions in the 56 canonical reference pages to TeX delimited formula spans, synchronized with their copies in the full encyclopedia atlas.
- Fixed broken inline/display math delimiter settings on eight pages.
- Improved the shared equation enhancer to recognize unambiguous algebraic expressions that older HTML readers left as plain text.

## Updating and testing

Run these in the project root:

```sh
python scripts/prepare_github_pages.py
python scripts/check_links.py
node scripts/check_search.js
python -m http.server 8000
```

The generated root `index.html` should be committed along with `index.html` if previewing outside of GitHub Actions; the workflow regenerates it on deployment. `SE/K/CONCEPTS.html` is the recommended first stop, while `SE/K/U/OPEN-ENCYCLOPEDIA.html` remains the complete offline search corpus (~21 MB).

Validation is based on static link and JavaScript checks. A full graphical-browser rendering check was unavailable in this execution environment.

**Superseded:** see `CHANGES-NAVIGATION-RESTRUCTURE.md` for the current navigation and publishing structure.
