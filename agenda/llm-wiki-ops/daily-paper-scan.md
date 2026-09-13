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
8. Commit and push an ingestion branch; create or update a reviewable PR. Prefer the latest default branch when this does not import or lose pending content. Preserve unrelated changes and never force-push over them. If an unmerged ingestion branch already holds necessary content, stack explicitly and record the dependency; do not auto-merge that stack into a non-default branch. Apply the September 13 auto-merge policy below to eligible default-branch PRs.
9. After publishing succeeds, advance `last_successful_scan_utc` to the search coverage cutoff and record publication and merge status separately in state/logs. This acknowledgement may require a small follow-up commit. If publishing fails, leave the successful watermark unchanged and report the actual blocker. Revisit unmerged eligible PRs even when the search watermark has advanced.

When nothing qualifies, do not manufacture additions. Report that briefly. Logs and state record admitted, duplicate/pending, deferred, and missing-PDF items. An inaccessible linked project page does not invalidate an available canonical paper PDF; describe its access status honestly.

## Initial branch relationships

PR #2 contains the four seed PDF upgrades. The initial expansion is based on its branch `codex/pdf-ground-seed-papers`, at `5d653984717e8188d5e2c5924665547af5ba08b5`, and published on `codex/self-improvement-literature-scan`. PR #3 contains AutoSaddler (2608.23041); do not add it again. Re-read live PR state instead of assuming these relationships remain current.

## Publication transport and deferred PDFs

If shell Git lacks authentication, use the connected GitHub Git Data API: upload binary blobs with base64, verify their Git SHAs, create the tree/commit, then update the ingestion branch without force. Verify the remote tree against the locally validated tree. The connector has a 16 MiB request-body limit; do not send a larger base64 payload. If an exact PDF cannot be published through available authenticated transport, preserve its reviewed drafts and provenance in agenda/llm-wiki-ops/pending-ingestions and keep it in the missing-PDF list. Do not admit its source/wiki pages until the exact PDF is present. Revisit missing_pdfs before the ordinary backlog even when the successful search watermark advances.

## September 11 repository-state update

PR #4 was merged into the still-open draft PR #2 branch at 6555ace849f087d3ff1b92dcc5d90ab2842f65c4. PR #3 merged AutoSaddler's abstract-only entry into main at 2695f7cccf1956d6a1eec3298147a4b183fe5ed2. The next scan branch is codex/paper-scan-2026-09-11, stacked on PR #2, with AutoSaddler upgraded under its existing main-branch stem. Check live refs and all ingestion branches before deduplicating or selecting a base; the closed PR #4 is historical, not the active publication target. Do not auto-merge or silently reconcile unrelated branch changes.

## September 13 authorization: validation-gated automatic merge

The user requested: “Schedule this to run every day at 8AM PT and auto merge.” Updated and re-enabled the existing task, rather than creating a duplicate. Its exact schedule is daily 08:00 in America/Los_Angeles, starting September 14, 2026; it follows Pacific daylight-saving changes. The cloud task update succeeded September 13. This policy supersedes the earlier no-merge rule for the recurring ingestion workflow only.

Automatically merge this workflow's non-draft, default-branch-targeted ingestion PRs only when:

- Exact PDFs are published with correct hashes, substantive notes, and synthesis links; generated indexes and available validation pass on the exact PR head.
- Required CI and reviews are satisfied; there are no unresolved substantive findings, unrelated modifications, missing canonical files, or merge conflicts.
- The complete diff preserves existing full-text corrections, canonical-ID deduplication, and concurrent scan state; GitHub reports the PR as mergeable.

Use an expected-head-SHA guard for merging, verify the resulting default-branch tree, and record the merge commit. Never bypass branch protection or treat absent/unreadable check information as a passing requirement. If only enforced CI requirements are pending, GitHub auto-merge may be enabled when supported; otherwise retry on the next scan. Report blockers without merging.

The scheduling change does not merge draft PR #2, PR #5, or other preexisting stacked dependencies. Auto-RecSys/Ecdysis on `codex/add-harness-papers-2026-09-12` depends on #5 and remains open until that dependency is separately integrated and the PR can safely target the default branch. Preserve the AutoSaddler full-text upgrade when main is eventually reconciled.

Successful individual runs and no-new-paper outcomes do not complete this ongoing task. Keep it enabled. Keep missing-PDF and unmerged-PR retries independent of the search watermark.
