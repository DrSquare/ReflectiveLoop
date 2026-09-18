# Canonical paper PDFs

This branch contains **18 / 18 admitted exact PDFs**: four seeds, thirteen later additions, and the full-text upgrade of AutoSaddler already cataloged on main. All have source notes, paper wiki pages, and synthesis connections. PDFs are copied unchanged; extracted full-text transcriptions are not committed.

| Paper stem | Pinned PDF | Pages | Retrieved (UTC date) |
|---|---|---:|---|
| [lee-2026-meta-harness-end-to-end](lee-2026-meta-harness-end-to-end.pdf) | [2603.28052v1](https://arxiv.org/pdf/2603.28052v1) | 26 | 2026-09-08 |
| [zhang-2026-hyperagents](zhang-2026-hyperagents.pdf) | [2603.19461v1](https://arxiv.org/pdf/2603.19461v1) | 60 | 2026-09-08 |
| [hebbar-2026-sia-self-improving-ai](hebbar-2026-sia-self-improving-ai.pdf) | [2605.27276v2](https://arxiv.org/pdf/2605.27276v2) | 15 | 2026-09-08 |
| [feng-2026-coskill-joint-reinforcement](feng-2026-coskill-joint-reinforcement.pdf) | [2609.04865v1](https://arxiv.org/pdf/2609.04865v1) | 25 | 2026-09-08 |
| [ye-2026-meta-context-engineering-via-agentic](ye-2026-meta-context-engineering-via-agentic.pdf) | [2601.21557v2](https://arxiv.org/pdf/2601.21557v2) | 46 | 2026-09-11 |
| [xu-2026-adapting-the-interface-not-the](xu-2026-adapting-the-interface-not-the.pdf) | [2605.22166v1](https://arxiv.org/pdf/2605.22166v1) | 18 | 2026-09-11 |
| [zhang-2026-self-harness-harnesses-that-improve](zhang-2026-self-harness-harnesses-that-improve.pdf) | [2606.09498v1](https://arxiv.org/pdf/2606.09498v1) | 19 | 2026-09-11 |
| [wei-2026-evo-harness-context-to-harness](wei-2026-evo-harness-context-to-harness.pdf) | [2608.15071v1](https://arxiv.org/pdf/2608.15071v1) | 16 | 2026-09-11 |
| [karten-2026-prime-agent-a-self-improving](karten-2026-prime-agent-a-self-improving.pdf) | [2608.23552v1](https://arxiv.org/pdf/2608.23552v1) | 16 | 2026-09-11 |
| [yang-2026-skillforge-evolving-verifiable-skills-for](yang-2026-skillforge-evolving-verifiable-skills-for.pdf) | [2608.24747v1](https://arxiv.org/pdf/2608.24747v1) | 22 | 2026-09-11 |
| [fu-2026-self-play-meets-skill-evolution](fu-2026-self-play-meets-skill-evolution.pdf) | [2607.29468v1](https://arxiv.org/pdf/2607.29468v1) | 9 | 2026-09-11 |
| [zhang-2025-darwin-godel-machine-open-ended](zhang-2025-darwin-godel-machine-open-ended.pdf) | [2505.22954v1](https://arxiv.org/pdf/2505.22954v1) | 64 | 2026-09-11 |
| [fu-2026-se-gos-self-evolving-graph](fu-2026-se-gos-self-evolving-graph.pdf) | [2609.08228v1](https://arxiv.org/pdf/2609.08228v1) | 21 | 2026-09-11 |
| [li-2026-skilladam-stable-and-efficient-skill](li-2026-skilladam-stable-and-efficient-skill.pdf) | [2609.08944v1](https://arxiv.org/pdf/2609.08944v1) | 17 | 2026-09-11 |

| [gao-2026-experience-funnel-a-state-policy](gao-2026-experience-funnel-a-state-policy.pdf) | [2609.08919v1](https://arxiv.org/pdf/2609.08919v1) | 11 | 2026-09-11 |
| [zhang-2026-harnesscompass-guiding-automatic-harness-evolution](zhang-2026-harnesscompass-guiding-automatic-harness-evolution.pdf) | [2608.01918v1](https://arxiv.org/pdf/2608.01918v1) | 17 | 2026-09-11 |
| [lou-2026-autoharness-improving-llm-agents-by](lou-2026-autoharness-improving-llm-agents-by.pdf) | [2603.03329v1](https://arxiv.org/pdf/2603.03329v1) | 21 | 2026-09-11 |
| [park-2026-autosaddler-automatic-harness-optimization-with](park-2026-autosaddler-automatic-harness-optimization-with.pdf) | [2608.23041v1](https://arxiv.org/pdf/2608.23041v1) | 44 | 2026-09-11 |

The [manifest](manifest.json) records SHA-256 hashes, byte counts, page counts, extraction methods, and visually inspected pages. Notes cite 1-based PDF pages in the pinned versions; these are version-specific analyses, not a guarantee that every PDF is the latest revision. DGM v3 was detected after reviewing v1 and is recorded for a separate revision comparison.

## Missing-PDF list

Five publication-pending candidates remain blocked or incomplete. They are not admitted to the wiki, and no source/wiki placeholders have been created. AutoSaddler's abstract entry merged through PR #3; its exact-PDF upgrade is now included among this branch's 18 admitted papers. The historical [seed upgrade report](../logs/reports/2026-09-08-seed-pdf-upgrade.md) preserves the corrections to the original abstract-level notes.

| Paper | Exact version | Blocker category | Current blocker |
|---|---|---|---|
| Continual Harness (`karten-2026-continual-harness-online-adaptation-for`) | [2605.09998v1](https://arxiv.org/pdf/2605.09998v1) | size-limit | Prior reviewed exact PDF is 31,751,676 bytes; base64 upload exceeds the GitHub connection's 16 MiB request limit. Draft bundle: [karten pending ingestion](../agenda/llm-wiki-ops/pending-ingestions/karten-2026-continual-harness-online-adaptation-for.json). |
| SkillRL (`xia-2026-skillrl-evolving-agents-via-recursive`) | [2602.08234v1](https://arxiv.org/pdf/2602.08234v1) | size-limit | Prior reviewed exact PDF is 13,153,200 bytes; base64 upload exceeds the GitHub connection's 16 MiB request limit. Draft bundle: [xia pending ingestion](../agenda/llm-wiki-ops/pending-ingestions/xia-2026-skillrl-evolving-agents-via-recursive.json). |
| HarnessForge (`chen-2026-harnessforge-joint-harness-and-policy`) | [2606.01779v1](https://arxiv.org/pdf/2606.01779v1) | transport | Download/hash reverified; interrupted binary upload; expected Git blob returns 404. |
| Co-Evolving Harnesses and Models (`yu-2026-co-evolving-harnesses-and-models`) | [2609.09134v1](https://arxiv.org/pdf/2609.09134v1) | transport | Download/hash reverified; not attached to a completed ingestion tree; binary connector read cannot be decoded. |
| The Last AI Built by Humans (`bengio-2026-the-last-ai-built`) | [2609.11873v2](https://arxiv.org/pdf/2609.11873v2) | review-incomplete | Exact download and partial review; PDF syntax warnings need rendering/validation; versioned hash and full review incomplete. |

See the [September 16 scan checkpoint](../agenda/llm-wiki-ops/pending-ingestions/2026-09-16-scan-checkpoint.json), [reviewed evidence note](../agenda/llm-wiki-ops/pending-ingestions/2026-09-14-reviewed-evidence.md), and [dated log](../logs/2026-09-16-codex-workspace.md) for the recovery checkpoint. Other candidates are in the [scan state](../agenda/llm-wiki-ops/scan_state.json). Retry publication through an authenticated Git transport capable of the blocked file sizes. Never compress or rewrite a canonical PDF to fit.
