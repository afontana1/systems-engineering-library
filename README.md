# Systems Engineering Library

A static learning library of systems engineering concepts, textbooks, courses,
and practical exercises. The website homepage is generated from
`SE/START-HERE.html`.

## Publish with GitHub Actions

1. In the repository, open **Settings > Pages**.
2. Under **Build and deployment > Source**, select **GitHub Actions**.
3. Push this project, including `.github/workflows/deploy-pages.yml`, to `main`.
4. Open **Actions > Deploy GitHub Pages** to follow the deployment. You can also
   launch it using **Run workflow** on `main`.
5. When the workflow succeeds, use the website link in the deployment summary.

Each push to `main` regenerates `index.html` from `SE/START-HERE.html`, checks
library links and search behavior, and deploys the generated homepage plus the
complete `SE` folder. Repository tooling is excluded from the website artifact.

A repository named `<username>.github.io` publishes at
`https://<username>.github.io/`. Other repository names publish at
`https://<username>.github.io/<repository>/`. The site's relative links support
both layouts.

No framework, package installation, or server-side application is required.
The workflow publishes the static files directly, including `SE/K/_assets`.
Python lab files are downloadable exercises to run locally.

## Update or preview

GitHub Actions regenerates the homepage automatically. After editing
`SE/START-HERE.html`, regenerate it locally when previewing:

```powershell
python scripts/prepare_github_pages.py
```

To preview from this folder:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/`. Study progress is stored in the current browser.

The encyclopedia HTML is approximately 20 MB; its initial download can be slow
on mobile connections. The complete library is approximately 66 MiB.
