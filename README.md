# Systems Engineering Library

The homepage is **`index.html` at the repository root**. It links directly to
Concepts, Subject Guides, Courses, Textbooks, Labs, and the Encyclopedia. There
is no separate homepage source or homepage generator.

Website: https://afontana1.github.io/systems-engineering-library/

## Main sections

- **Concepts:** `SE/K/CONCEPTS.html` for the 56 reference concepts; `SE/K/T/INDEX.html` for cross-course core concepts.
- **Subject Guides:** `SE/K/LEARNING-PATHWAYS.html` and `SE/K/LEARNER-JOURNEYS.html`.
- **Courses:** `SE/C/PROGRAM.html`, with six curriculum phases and direct links from each course to its book and assigned concepts.
- **Textbooks:** `SE/K/OPEN-BOOKS.html`, listing 20 course-aligned books and the advanced architecture, quantitative, graduate-methods, and other advanced texts.
- **Labs:** `SE/K/LAB-LIBRARY.html`.
- **Encyclopedia:** `SE/K/U/OPEN-ENCYCLOPEDIA.html`, available from the shared global navigation bar.

The common navigation is implemented in `SE/K/_assets/learning-shell-v55.js`
and `learning-shell-v55.css`. Drop-down menus expose only useful secondary
choices; other pages do not require an encyclopedia detour to reach concepts.

## GitHub Pages deployment

1. In **Settings > Pages**, choose **GitHub Actions** as the build and deployment source.
2. Push the repository, including `.github/workflows/deploy-pages.yml`, to `main`.
3. The workflow runs link and search tests and publishes `index.html`, `.nojekyll`, and the complete `SE/` tree.

All links are relative so both repository Pages and `<username>.github.io`
root-hosted layouts are supported. There is no framework, database, application
cache, account management, or study-progress storage.

## Local preview and validation

From the repository root:

```bash
python -m http.server 8000
```

Open http://localhost:8000/. To run the same checks as the deployment:

```bash
python scripts/check_links.py
node scripts/check_search.js
```

Mathematical notation is rendered using the bundled offline MathJax files.
The source directory retains the original chapter, concept, lab, and textbook
URLs to keep existing cross-references intact. The full Encyclopedia is large
(approximately 21 MB), so the lighter Concepts directory is the default topic
entry point.
