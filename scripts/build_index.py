#!/usr/bin/env python3
"""Regenerate index.md from the contents of wiki/.

Usage:
    python3 scripts/build_index.py --apply

Without --apply, prints the generated catalog to stdout without writing it.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
INDEX_PATH = REPO_ROOT / "index.md"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def read_title(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if match:
        for line in match.group(1).splitlines():
            if line.startswith("title:"):
                return line.split(":", 1)[1].strip().strip('"')
    return md_path.stem


def build_catalog() -> str:
    lines = [
        "# Index",
        "",
        "Generated catalog of `wiki/` pages. Regenerate with",
        "`python3 scripts/build_index.py --apply`. Do not hand-edit.",
        "",
    ]
    if not WIKI_DIR.is_dir():
        lines.append("_No `wiki/` directory found._")
        return "\n".join(lines) + "\n"

    for category_dir in sorted(p for p in WIKI_DIR.iterdir() if p.is_dir()):
        pages = sorted(category_dir.glob("*.md"))
        if not pages:
            continue
        lines.append(f"## {category_dir.name} ({len(pages)})")
        lines.append("")
        for page in pages:
            title = read_title(page)
            rel = page.relative_to(REPO_ROOT)
            lines.append(f"- [{title}]({rel})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write index.md")
    args = parser.parse_args()

    catalog = build_catalog()
    if args.apply:
        INDEX_PATH.write_text(catalog, encoding="utf-8")
        print(f"Wrote {INDEX_PATH}")
    else:
        print(catalog)


if __name__ == "__main__":
    main()
