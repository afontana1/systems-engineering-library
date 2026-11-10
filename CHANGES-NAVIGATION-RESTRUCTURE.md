# Navigation restructure

## Changes

- The root `index.html` is now the only homepage source. `SE/START-HERE.html`
  and `scripts/prepare_github_pages.py` were deleted. The GitHub Pages
  workflow validates and deploys `index.html` directly.
- All internal homepage breadcrumbs and resource links were updated to the
  root homepage. The old `K/U/START-HERE-V15.html` standalone guide was
  renamed to `K/U/OVERVIEW-V15.html`, retaining its content.
- Shared global navigation has six sections: **Concepts, Subject Guides,
  Courses, Textbooks, Labs, Encyclopedia**. Contextual menus expose the
  cross-course concepts, subject journeys, course phases, and advanced books.
  The Encyclopedia is linked from the global navigation only.
- The **Concepts** page now presents cross-course core concepts alongside the
  56 reference concepts. It no longer routes search to the Encyclopedia.
- The **Textbooks** page now lists the advanced architecture, quantitative,
  engineering studies, methods, and graduate-study collections before the 20
  course-aligned textbooks. Textbook cards link straight to books, not courses.
  Course-number/title filtering and phase jump links are available.
- Course pages retain **Concept reading** and direct **Companion book and
  laboratories** links; redundant **Explore concepts** links were removed.
- Guided learning journeys now link directly to the 12 relevant concept pages
  rather than opening an Encyclopedia pane. Their JSON manifest is updated.
- Repeated Encyclopedia links in legacy hubs, readers, and other pages were
  redirected to the relevant concept or subject page; the atlas itself and its
  full reference corpus are unchanged.
- The homepage and section headings use straightforward descriptive wording.
  Shared navigation and dropdowns do not store state.

## Compatibility and coverage

Content URLs were preserved for existing chapters, textbooks, datasets,
notebooks, labs, and concept references. Only the retired homepage source,
its generator, and one renamed legacy guide changed paths. Existing static
pages remain valid without a build step.

Tests: `python scripts/check_links.py` and `node scripts/check_search.js`.
These validate the root homepage, local links and fragments, journey steps,
book directory, and search index. Browser interactions (including dropdowns
and keyboard Escape) were tested using the supplied HTML and scripts in a
headless browser. Network navigation was blocked in the test environment,
so a full served-site browser walkthrough remains recommended after publishing.
