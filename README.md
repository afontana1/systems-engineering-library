# Systems Engineering Library

The homepage is `index.html` at the repository root. The complete static
website (courses, textbooks, concepts, advanced readings, labs, datasets,
notebooks, diagrams, searchable Encyclopedia and bundled MathJax) is stored
in `SE/`. No database, external JavaScript framework, account system, or
study-progress storage is required.

## Deploy to GitHub Pages

1. Upload the repository contents to the root of your GitHub repository.
2. In **Settings → Pages**, select **GitHub Actions** as the deployment source.
3. Push to the `main` branch. The included workflow publishes `index.html`,
   `.nojekyll`, and `SE/` without a build process or external dependencies.

## Local preview

From the repository root, run:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/` in a browser.

The source Markdown, case models, notebooks, and engineering data remain in
`SE/` for education and independent reproduction. Historical release notes,
audits, build-time test harnesses, and internal tracking metadata have been
removed from this distributable website package.
