# Systems Engineering Library

A static learning library of systems engineering concepts, textbooks, courses,
and practical exercises. The website homepage is generated from
`SE/START-HERE.html`.

## Publish with GitHub Pages

1. Create a GitHub repository and upload this folder's contents, including
   `index.html`, `.nojekyll`, and the complete `SE` folder. Include the dotfile
   when uploading.
2. In the repository, open **Settings > Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select the branch containing these files (usually `main`), select **/(root)**,
   and save.
5. Wait for the Pages deployment to finish, then use the website link shown there.

A repository named `<username>.github.io` publishes at
`https://<username>.github.io/`. Other repository names publish at
`https://<username>.github.io/<repository>/`. The site's relative links support
both layouts.

No framework, package installation, or server-side application is required.
The `.nojekyll` file preserves the static assets in `SE/K/_assets`.
Python lab files are downloadable exercises to run locally.

## Update or preview

After editing `SE/START-HERE.html`, regenerate the root homepage:

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
