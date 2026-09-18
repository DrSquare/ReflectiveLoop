# Daily paper scan

Configured September 11, 2026 UTC by the user's explicit request. The connected ChatGPT task, **Update ReflectiveLoop papers**, runs at **08:00 America/Los_Angeles every day**. This is a wall-clock local schedule that follows daylight saving time. It is not a GitHub Actions cron job.

## Scope and authority

Search for papers on self-improving harnesses/scaffolds, evolving agent skills and retrieval infrastructure, learned improvement procedures, and self-improving agentic systems. The user's recurring request explicitly authorizes web search, PDF retrieval, repository additions, and LLM-wiki updates for each scan. This task-specific authorization satisfies AGENTS.md's explicit-search exception; it does not alter the general wiki rules.

Prioritize new primary research and substantial revisions, with concrete methods and evidence relevant to the existing synthesis. Include adjacent work only when it changes a method comparison or research question. Papers sharing a short name, such as SkillForge, must remain distinct by full title and canonical identifier.

## One scan

1. Read current AGENTS.md, catalog, indexes, source/PDF manifest, this procedure, scan state, recent logs, and open ingestion PRs. Check the remote head before creating changes.
2. Search since `last_successful_scan_utc` with a seven-day overlap for indexing delays. When no successful watermark exists, cover the previous 30 days. Also review the recorded backlog; do not treat an unreviewed candidate as rejected or already ingested.
3. Deduplicate by versionless arXiv ID or DOI, then normalized title, across main and pending PR branches. Update existing records for materially changed versions while documenting claim changes. Do not make duplicate pages for revised PDFs.
4. Retrieve an exact PDF; record its version, URL, hash, byte/page count, retrieval date and extraction method. If unavailable, record the candidate and actual failure in papers/README.md and the log. Do not create a placeholder source/wiki pair.
5. Write substantive PDF-grounded source and wiki notes. Preserve metric definitions, model/budget/split context, negative results, uncertainty, limitations, and verified implementation provenance. Inspect cited tables/figures visually when extraction alone is insufficient.
6. Add bidirectional synthesis links and a contextual sentence. Record whether the paper strengthens, narrows, contradicts, or leaves existing claims unchanged. Revisit the meta-procedure/co-training question only as supported by the new evidence.
7. Append the daily log; regenerate index.md; run `python3 scripts/validate_wiki.py` and `git diff --check`. Resolve concrete integrity failures before publishing.
8. Commit and push an ingestion branch; create or update a reviewable PR. Preserve unrelated changes and never force-push over them. Do not merge PRs. If an unmerged ingestion branch already holds necessary content, use/update it or stack explicitly and record the dependency.
9. After publishing succeeds, advance `last_successful_scan_utc` to the search coverage cutoff and record the publication in state/logs. This acknowledgement may require a small follow-up commit. If publishing fails, leave the successful watermark unchanged and report the actual blocker.

When nothing qualifies, do not manufacture additions. Report that briefly. Logs and state record admitted, duplicate/pending, deferred, and missing-PDF items. An inaccessible linked project page does not invalidate an available canonical paper PDF; describe its access status honestly.

## Initial branch relationships

PR #2 contains the four seed PDF upgrades. The initial expansion is based on its branch `codex/pdf-ground-seed-papers`, at `5d653984717e8188d5e2c5924665547af5ba08b5`, and published on `codex/self-improvement-literature-scan`. PR #3 contains AutoSaddler (2608.23041); do not add it again. Re-read live PR state instead of assuming these relationships remain current.

## Publication transport and deferred PDFs

If shell Git lacks authentication, use the connected GitHub Git Data API: upload binary blobs with base64, verify their Git SHAs, create the tree/commit, then update the ingestion branch without force. Verify the remote tree against the locally validated tree. The connector has a 16 MiB request-body limit; do not send a larger base64 payload. If an exact PDF cannot be published through available authenticated transport, preserve its reviewed drafts and provenance in agenda/llm-wiki-ops/pending-ingestions and keep it in the missing-PDF list. Do not admit its source/wiki pages until the exact PDF is present. Revisit missing_pdfs before the ordinary backlog even when the successful search watermark advances.

## September 11 repository-state update

PR #4 was merged into the still-open draft PR #2 branch at 6555ace849f087d3ff1b92dcc5d90ab2842f65c4. PR #3 merged AutoSaddler's abstract-only entry into main at 2695f7cccf1956d6a1eec3298147a4b183fe5ed2. The next scan branch is codex/paper-scan-2026-09-11, stacked on PR #2, with AutoSaddler upgraded under its existing main-branch stem. Check live refs and all ingestion branches before deduplicating or selecting a base; the closed PR #4 is historical, not the active publication target. Do not auto-merge or silently reconcile unrelated branch changes.
