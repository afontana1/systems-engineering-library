"""Generate the GitHub Pages homepage from SE/START-HERE.html.

Run from any directory: python scripts/prepare_github_pages.py
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def main():
    source = (ROOT / "SE" / "START-HERE.html").read_text(encoding="utf-8")
    # Move the homepage up one directory while keeping fragment-only links local.
    # Both HTML links and the inline search handler use quoted K/ or C/ paths.
    homepage = re.sub(r"([\"'])(K|C)/", r"\1SE/\2/", source)
    # Shared navigation creates its links from this prefix at runtime.
    homepage = homepage.replace('data-se-root=""', 'data-se-root="SE/"')
    homepage = "<!-- Generated from SE/START-HERE.html by scripts/prepare_github_pages.py. -->\n" + homepage
    (ROOT / "index.html").write_text(homepage, encoding="utf-8")
    # Serve the static library directly, including K/_assets.
    (ROOT / ".nojekyll").write_bytes(b"")
    print("Prepared index.html and .nojekyll for GitHub Pages.")


if __name__ == "__main__":
    main()
