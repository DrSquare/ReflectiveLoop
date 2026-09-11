# ReflectiveLoop literature expansion

Research cutoff: **September 11, 2026, 04:01:44 UTC** (September 10 evening Pacific). This is a curated search, not an exhaustive survey. Scope: persistent improvement to agent harnesses, skills, retrieval infrastructure, and agentic systems.

## Delivered coverage

**10 newly ingested papers / 12 selected PDFs; 14 paper triples including the four upgraded seeds.** Two reviewed papers await exact-PDF publication because their uploads exceed the connection limit. Each admitted paper has an unchanged versioned PDF, manifest metadata, source note, wiki page, page citations, methods/results/limitations, and bidirectional synthesis coverage.

| Addition | Version | Principal contribution to the wiki |
|---|---|---|
| SkillAdam | [2609.08944v1](https://arxiv.org/pdf/2609.08944v1) | Persistent optimizer memory and adaptive edit scope for skill documents |
| SE-GoS | [2609.08228v1](https://arxiv.org/pdf/2609.08228v1) | Evolution of skill-retrieval graphs and descriptions |
| SkillForge | [2608.24747v1](https://arxiv.org/pdf/2608.24747v1) | Explicit skill calls, outcome tracking, and revision during RL |
| Prime Agent | [2608.23552v1](https://arxiv.org/pdf/2608.23552v1) | Persistent computation, recursive sessions, and versioned harness state |
| Evo-Harness | [2608.15071v1](https://arxiv.org/pdf/2608.15071v1) | One-shot failures compiled into guidance for later tasks |
| SESA | [2607.29468v1](https://arxiv.org/pdf/2607.29468v1) | Co-evolution of self-play curriculum, memory, and policy |
| Self-Harness | [2606.09498v1](https://arxiv.org/pdf/2606.09498v1) | Same-model harness proposal with regression-gated acceptance |
| Life-Harness | [2605.22166v1](https://arxiv.org/pdf/2605.22166v1) | Four runtime intervention layers and cross-model reuse |
| MCE | [2601.21557v2](https://arxiv.org/pdf/2601.21557v2) | Learned procedures for constructing context |
| Darwin Godel Machine | [2505.22954v1](https://arxiv.org/pdf/2505.22954v1) | Historical self-modifying coding-agent and archive baseline |

Start with [the catalog](../../index.md), [the expanded overview](../../wiki/overviews/self-improving-llm-agents.md), and [the updated research question](../../wiki/questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training.md).

## Main interpretation changes

The broad idea of optimizing an improvement procedure already has concrete prior art in MCE and DGM. A stronger research question isolates the extra effect of a learned editor and controlled transfer, compared with a fixed learned procedure or fixed stateful editor. SkillForge and SESA add useful controls for skill invocation and memory-off performance.

The synthesis preserves material negative or uncertain evidence: Self-Harness uses held-out scores for promotion; SE-GoS's disjoint-split gain is within the paper's noise band and repeated updates later degrade it; SkillAdam changes optimization-data access versus its baseline; Prime Agent uses external values in its headline ARC comparison. The literature does not justify a common performance ranking or a universal claim that repeated editing improves an agent.

## Search and triage record

Primary-source search covered self-improving agent harnesses, runtime adaptation, meta-context engineering, skill evolution with RL, self-play skill memory, and September 2026 arXiv entries. Example query families: `self improving agent harness Meta-Harness skills 2026`, `site:arxiv.org/abs/2609 harness`, `site:arxiv.org/abs/2609 skill evolution`, `site:arxiv.org/abs/2609 self-improving`. Bibliographic candidates from search were checked against exact arXiv PDFs before admission.

- Existing seeds were deduplicated against the catalog and PR #2.
- AutoSaddler (2608.23041) was skipped as an existing addition in PR #3.
- Seven follow-ups are explicitly deferred: HarnessCompass, AutoHarness, ACE, ADAS, DGM v3 versus v1, SkillMAS, and the distinct cloud-support SkillForge (2604.08618).
- Continual Harness (31,751,676 bytes) and SkillRL (13,153,200 bytes) exceed the GitHub connector's 16 MiB request limit after base64 encoding. Their exact PDFs were reviewed locally, but are not published or ingested. Complete draft analyses and hash metadata are preserved under agenda/llm-wiki-ops/pending-ingestions; retry them before new backlog work. See the [missing-PDF list](../../papers/README.md#missing-pdf-list).
- Author-linked GitHub pages for MCE, Evo-Harness, Prime Agent, SkillRL, SESA, and DGM returned HTTP 200. The Continual Harness author website returned HTTP 403 in this environment; its link remains identified as a PDF-supplied project link. No implementation was reproduced or comprehensively audited.
- Exact versions, hashes, pages, and ten admitted-paper visual spot-checks are in [the manifest](../../papers/manifest.json). A spot-check of a result page is not a full visual audit of every page or appendix.

## Repository and schedule

The expansion branch is `codex/self-improvement-literature-scan`, based on `codex/pdf-ground-seed-papers` (PR #2) at `5d653984717e8188d5e2c5924665547af5ba08b5`. This preserves the seed PDF corrections. AutoSaddler remains separate in PR #3. No PR is merged by this task.

The enabled ChatGPT task **Update ReflectiveLoop papers** runs daily at **08:00 America/Los_Angeles**. It performs additions and wiki updates via ingestion PRs, deduplicates across pending branches, and only advances the successful-scan watermark after publishing. See [the procedure](../../agenda/llm-wiki-ops/daily-paper-scan.md) and [state](../../agenda/llm-wiki-ops/scan_state.json).

## Verification

Run `python3 scripts/build_index.py --apply`, `python3 scripts/validate_wiki.py`, and `git diff --check`. Publication and the observed validation result are appended to the daily log after they succeed. These gates verify artifact integrity; they do not reproduce scientific claims.

Published as [PR #4](https://github.com/DrSquare/ReflectiveLoop/pull/4). Observed result: PASS for 14 PDF/source/wiki triples and 18 wiki pages, current catalog, local links, and reciprocal synthesis. The initial remote tree matched local Git tree 6613e90ad491a1e871d00d30834830b5ef7e183c exactly. Two oversized PDFs remain explicitly deferred.
