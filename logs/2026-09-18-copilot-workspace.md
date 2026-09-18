---
date: 2026-09-18
agent: copilot
host: workspace
model: "Copilot coding agent; exact model identifier not exposed"
---

## [2026-09-18] maintenance | integration | Merge main into the Stellar Colosseum branch

- Merged `origin/main` (`9d9a332`) into the Stellar Colosseum ingestion branch. No paper was admitted, removed, or re-reviewed; no PDF bytes changed.
- Conflicts resolved: `.gitattributes` (kept main's comment plus `*.pdf binary`), `README.md`, `papers/README.md`, `papers/manifest.json`, `logs/2026-09-16-codex-workspace.md`, `wiki/overviews/self-improving-llm-agents.md`. `index.md` was regenerated rather than hand-merged.
- Main now carries exact PDFs for the five records this branch had described as legacy abstract-only entries. Those branch-local "legacy" qualifications were therefore retired: counts move to **19 PDF-grounded papers**, the manifest keeps main's schema with the Stellar Colosseum entry appended, and the overview keeps main's seed/scan structure with the Stellar Colosseum comparator section added.
- `python3 scripts/build_index.py --apply` and `python3 scripts/validate_wiki.py` pass: 19 PDF/source/wiki triples, 23 wiki pages, catalog current, local and bidirectional synthesis links valid. Poppler tools are unavailable in this environment, so page counts and extraction were not re-checked here; the September 16 record stands.
- Publication-pending and missing-PDF entries, scan state, and open PRs are unchanged by this merge.

## [2026-09-18] maintenance | integration | Merge main into codex/paper-scan-2026-09-11

- Merged `origin/main` (`c4d34ef`, which carries Stellar Colosseum) into `codex/paper-scan-2026-09-11`. No paper was admitted, removed, or re-reviewed; no PDF bytes changed.
- Conflicts resolved: `README.md` (kept both the September 16 and September 11/12 sections), `papers/README.md` (kept all three added PDF rows), `papers/manifest.json` (kept all 21 entries), `wiki/overviews/self-improving-llm-agents.md` (count and scope sentence). `index.md` was regenerated rather than hand-merged.
- Counts move to **21 PDF-grounded papers** across README, `papers/README.md`, and the overview.
- `python3 scripts/build_index.py --apply` and `python3 scripts/validate_wiki.py` pass: 21 PDF/source/wiki triples, 25 wiki pages, catalog current, local and bidirectional synthesis links valid. Poppler tools are unavailable in this environment, so page counts and extraction were not re-checked here; the prior records stand.
- Publication-pending and missing-PDF entries, scan state, and open PRs are unchanged by this merge.
- Post-merge correction: the Stellar Colosseum page still said the Hyperagents and CoSkill records were abstract-based "on this branch". Both are PDF-grounded here, so that qualification was removed. The earlier entry above records the state of a different merge (19 papers) and is left unchanged as an append-only record.
