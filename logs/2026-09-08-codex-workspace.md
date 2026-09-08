---
date: 2026-09-08
agent: codex
host: workspace
model: GPT
---

## [2026-09-08] ingest | self-improving-agents | Four seed PDFs

User requested retrieval of the exact papers and replacement of the
abstract-summary notes merged in PR #1. Read AGENTS.md, index.md,
indexes/, all eight notes, and the existing synthesis/question before
re-ingesting. Retrieval was explicitly authorized for this task.

Downloaded arXiv versions 2603.28052v1, 2603.19461v1, 2605.27276v2,
2609.04865v1. Copied all 4 PDFs into papers/ using existing shared stems;
recorded versions, hashes, byte/page counts, extraction and visual checks
in papers/manifest.json. Extraction: pdftotext -layout. Upgraded 8/8
source/wiki pages to source_format: pdf and text_extractor:
pdftotext-layout, with section/table/page citations. Zero PDFs remain on
the missing list. Historical September 7 log and ADR decision text were
preserved; appended a resolution to the ADR.

Supersede check:

- Meta-Harness: strengthens trace-access evidence with the ablation;
  narrows model-transfer, diagnostic-context, and coding-ranking claims;
  distinguishes same-benchmark coding search from independent tests.
- Hyperagents: narrows full self-modifiability and cross-domain transfer;
  preserves significant imp@50 evidence while qualifying nonsignificant
  compounding and customized-baseline comparisons.
- SIA: replaces “beats either alone” with “improves after harness-only
  search”; corrects denominators and code-generating task interpretation;
  records test-split reward exposure and frozen selector.
- CoSkill: clarifies shared weights, staged edits, fixed GiGPO/verifier,
  and imported baselines; records protocol/aggregate ambiguities and the
  absence of a cross-environment transfer experiment.

Updated only affected interpretations in the existing overview and
question. All four paper pages retain bidirectional overview links.
The combined Hyperagents–CoSkill question remains unresolved.
Detailed before/after claims: reports/2026-09-08-seed-pdf-upgrade.md.

## [2026-09-08] maintenance | llm-wiki-ops | Upgrade validation

Regenerate index.md with scripts/build_index.py --apply. Validate PDF
provenance, source/wiki metadata, required sections, citations and links.
No model training, benchmark rerun, or new literature admission is part
of this change. Reviewable work is on codex/pdf-ground-seed-papers.

Validation completed: 4 PDF signatures, hashes, byte counts, and page
counts verified; 4 source/wiki metadata pairs and required sections
verified; 156 versioned page-citation targets within PDF bounds; no broken
relative/wiki links; 4 bidirectional overview connections; no active
abstract-summary metadata. Catalog regeneration is unchanged and
git diff --check passes. Key result pages were also visually reviewed.
