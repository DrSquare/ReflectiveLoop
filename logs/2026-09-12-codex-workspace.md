---
date: 2026-09-12
agent: codex
host: workspace
model: "Codex; exact model identifier not exposed"
---

## [2026-09-12] ingest | self-improving-agents | Auto-RecSys and Ecdysis

The user explicitly requested two papers through LinkedIn short links. Resolved the public redirects and post paper references, then retrieved the primary arXiv records and exact versioned PDFs. Social-post text served only to identify the papers. Re-read AGENTS.md, index.md, indexes/, manifest, PDF README, daily-scan procedure/state, prior log, and synthesis. Live open PRs remained #2 and #5; #4 had merged into #2 and #3 had merged the AutoSaddler abstract entry into main. Deduplicated canonical IDs and titles against main and both pending branches. Neither paper was present or in the documented pending bundles.

Created `codex/add-harness-papers-2026-09-12` from PR #5 at `242cf8a6a2c1d607a4e78996fd51aa5372111391`. The new PR will target that branch so the two additions are reviewable separately from #5/#2. No merges or unrelated branch changes are part of this request.

| Paper | User link | Exact PDF | Review |
|---|---|---|---|
| Auto-RecSys | [supplied link](https://lnkd.in/p/g4GWF6f9) | [2609.10922v1](https://arxiv.org/pdf/2609.10922v1) | All 16 pages as extracted text; pp. 10–11 visually inspected |
| Ecdysis | [supplied link](https://lnkd.in/p/gzWd3Gmj) | [2609.11677v1](https://arxiv.org/pdf/2609.11677v1) | All 19 pages as extracted text; pp. 7 and 19 visually inspected |

Copied PDFs unchanged and recorded SHA-256, bytes, page counts, extraction method, discovery provenance, and visually inspected pages in the manifest. Both emitted a Poppler font warning, but extraction and reviewed renders were readable. Wrote substantive sources and paper wiki pages with pinned page citations, protocols, negative results, limitations, and reciprocal links to both concept pages and the overview. Exact PDF payloads fit the publication transport. The two preexisting oversized pending-ingestion bundles remain preserved and outside sources/wiki; this manual addition did not retry their uploads.

Verified Ecdysis's author-linked repository and public implementation tree at `ba21638addc1e3c94972822646ea4990c87d4768`; its release excludes local experiment configs, raw datasets, traces, and private artifacts. No official Auto-RecSys implementation was identified. Neither system's experiments were reproduced.

### Supersede checks

- **Auto-RecSys strengthens operational-memory evidence:** persistent playbooks and session recovery support multi-day industrial experimentation. Its monitor rewrite is a concrete observational example of modifying orchestration.
- **Auto-RecSys narrows the headline:** 4.0 → 1.3 major fixes describes stabilization; a baseline change causes regression before recovery to 0.5 and 5/6 zero-fix late iterations. The metric excludes implementation debugging. One model and 31 iterations do not isolate causal playbook benefit, scientific-quality gains, or cross-domain generalization.
- **Auto-RecSys narrows transfer and validation claims:** transferred playbook structure is filled interactively; cross-model scientific insights remain future work. Formal playbook promotion gates are absent. Correctly stored failure records do not ensure correct causal explanations or scope. Metadata/count/checkpoint inconsistencies are preserved in the source note.
- **Ecdysis strengthens a designed diagnosis baseline:** aggregate failures and sequential role refinement improve held-out/model-transfer averages under a shared initialization and training-only acceptance gate. It does not train the editor or identify failure causes causally.
- **Ecdysis narrows accuracy and efficiency claims:** 18.56% is relative across three datasets (58.67% → 69.56%), distinct from the two-domain 46.67% → 59.33% comparison. Full FDCR reaches 1.84× training speedup; aggregation alone is faster in the reported runs. FDCR loses on some individual metrics/cells.
- **Ecdysis narrows quarter-data equivalence:** the five-failure Retail experiment lowers cost but drops mean accuracy and Pass^3. It is one transfer cell, not broad statistical equivalence. Manual accommodation ratios lack agreement/uncertainty details; the source preserves token-definition, AgentBench protocol, and README/PDF discrepancies.
- **Research question remains unresolved:** neither paper tests jointly trained modifiable meta-procedure plus skill editor/reasoner roles with controlled cross-domain transfer. Updated contextual synthesis and evaluation controls; left the existing Hyperagents/CoSkill question page unchanged.

This is a user-directed two-paper ingestion, not a full daily scan. `last_successful_scan_utc` remains unchanged; a separate `manual_ingestions` entry will record publication for future deduplication.

## [2026-09-12] maintenance | validation | Twenty complete paper entries

Regenerated the catalog with `python3 scripts/build_index.py --apply`. `python3 scripts/validate_wiki.py` passed for 20 exact-PDF/source/wiki triples and 24 wiki pages, including hashes, sizes, page counts, successful extraction, required note sections, pinned citations, catalog freshness, local links, and reciprocal synthesis. `git diff --check` passed. Publication uses the connected GitHub Git Data API with binary Git-hash verification and comparison against the validated local tree.
