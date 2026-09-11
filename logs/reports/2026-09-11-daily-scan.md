# ReflectiveLoop scan: September 11, 2026

Research cutoff: **2026-09-11 15:04:36 UTC**. Search overlap began September 4 at 04:01:44 UTC. This is a curated scan, not an exhaustive literature census; additions include previously recorded backlog, not only newly published papers.

## Reviewed and admitted

**Three new papers plus one full-text upgrade; 4/4 selected PDFs reviewed and copied unchanged.** This branch contains 18 complete PDF/source/wiki triples and 22 wiki pages, preserving the fourteen earlier full-text entries.

| Paper | Pinned full text | Why it matters |
|---|---|---|
| Experience Funnel (submitted September 8) | [2609.08919v1](https://arxiv.org/pdf/2609.08919v1) | Alternating textual-state evolution and policy consolidation is close prior art for the research question |
| HarnessCompass (August 3; backlog) | [2608.01918v1](https://arxiv.org/pdf/2608.01918v1) | Task-agnostic constraints, grounded self-feedback, separate component search, and independent holdout |
| AutoHarness (version metadata February 10; backlog) | [2603.03329v1](https://arxiv.org/pdf/2603.03329v1) | Generates per-environment action verifiers or complete executable policies |
| AutoSaddler (August 24; upgrade) | [2608.23041v1](https://arxiv.org/pdf/2608.23041v1) | Replaces the existing abstract-only entry with actual splits, patch selection, test results and caveats |

See [the catalog](../../index.md), [mechanism comparison](../../wiki/concepts/procedural-self-improvement.md), [evaluation boundaries](../../wiki/concepts/evaluating-self-improvement.md), and [revised research question](../../wiki/questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training.md).

## Evidence changes that affect the experiment

- Experience Funnel makes alternating state/policy updates and memory-free consolidation insufficient novelty by themselves. It does not demonstrate a learned self-editable editor transferred into an unseen environment. Its main and ablation SearchQA values differ (62.4% versus 63.6%), as do initial values across tables, with no clear protocol mapping. Treat small comparative gains cautiously. [PDF pp. 5-7](https://arxiv.org/pdf/2609.08919v1#page=5)
- Add both updated-state-success filtering and transition-weighted distillation baselines: the paper acknowledges that selecting 01+11 transitions reduces to updated-state success in its binary analysis. A comparison against unfiltered data alone cannot identify the value of transition history. [PDF p. 7](https://arxiv.org/pdf/2609.08919v1#page=7)
- HarnessCompass's 54-to-66 headline concerns its 50-task search set; the 450-task held-out comparison is 51.6-to-60.4. Its cumulative feedback ablation degrades held-out performance before R3 integration recovers it. Neither five search turns nor the task-agnostic gate establishes equal-compute superiority or guaranteed generalization. [PDF pp. 5-6](https://arxiv.org/pdf/2608.01918v1#page=5)
- AutoHarness generates a distinct program for each game. Legality testing spans 145 environments, while strategic comparison spans 32 games and full-code-policy comparison 16. Distillation into the base model is explicitly future work. [PDF pp. 3-6](https://arxiv.org/pdf/2603.03329v1#page=3)
- AutoSaddler's offline loop re-executes candidates during development; it is not fixed-log learning. The paper excludes task-agent memory and skill curation. Table endpoints imply base gains 9.0/9.6/10.0 points, while Section 5.2 prints inconsistent differences. Three test executions are distinct from independent optimization runs. [PDF pp. 4-8, 20-21](https://arxiv.org/pdf/2608.23041v1#page=4)

## Search, deduplication, and deferred work

Query families covered September arXiv harness, skills, self-improving/self-evolving agents, plus exact backlog titles. The overlapping search recovered already-ingested SE-GoS and other existing entries, which were not duplicated. Primary arXiv pages verified identifiers and versions before full-text admission. Similarly named AutoHarness software repositories were not misattributed to the Google DeepMind paper. The author-supplied AutoSaddler project redirect could not be opened; code availability is not asserted.

The two previously blocked PDFs were checked first. Exact local hashes still match, but Continual Harness requires a 42,335,568-byte base64 payload and SkillRL 17,537,600 bytes; both exceed the known 16,777,216-byte connection limit. Shell Git has no configured credential helper. No known-oversized upload was repeated. Both full analyses remain preserved outside the wiki in pending-ingestion bundles, with exact hashes and URLs in the [missing-PDF list](../../papers/README.md#missing-pdf-list).

New backlog includes [HarnessForge](https://arxiv.org/abs/2606.01779) (high-priority joint harness/policy comparator), [ADMET-EvO v2](https://arxiv.org/abs/2609.10121v2) (revised September 10; scientific evidence-gating), [Programmatic Skill Networks](https://arxiv.org/abs/2601.03509), and [Scanning the Harness](https://arxiv.org/abs/2609.07360) (adjacent safety measurement, not an improvement algorithm). These have primary metadata verified but no admitted wiki claims. ReSkill (2606.01619) was found in Experience Funnel's references and still needs primary metadata verification. ACE v3 was verified but remains a full-text backlog item alongside ADAS, DGM revision review, SkillMAS, and the cloud-support SkillForge.

## Repository state and verification

PR #4 merged into the still-open draft PR #2 branch; PR #3 merged AutoSaddler's abstract entry into main. This scan starts from PR #2 head `6555ace849f087d3ff1b92dcc5d90ab2842f65c4` on `codex/paper-scan-2026-09-11`. AutoSaddler preserves its existing main-branch stem and identifier. This scan does not merge PRs or resolve unrelated integration conflicts.

All four new PDFs passed signature, byte-count, SHA-256, extraction, and page-count checks. Result pages were rendered and visually inspected: Experience Funnel page 6, HarnessCompass page 6, AutoHarness page 5, and AutoSaddler page 7. This is a targeted evidence review, not a visual audit of every appendix or reproduction of experiments. Catalog, local-link, pinned-citation, and reciprocal-synthesis validation are required before publication. The successful search watermark remains unchanged until the new branch and PR are published.
