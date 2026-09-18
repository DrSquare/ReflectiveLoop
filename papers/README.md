# papers/

Canonical PDFs go here, copied (never symlinked), named
`{first-author-lastname}-{year}-{first-5-title-tokens}.pdf`.

## Exact-PDF inventory

This branch contains **1 exact PDF** and **5 legacy abstract-only records**.
The complete entry is recorded in [manifest.json](manifest.json); legacy records
are listed separately there and below, and are not counted as PDF-grounded admissions.

| Paper | Pinned version | Pages | Added / retrieved |
|---|---|---:|---|
| [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](lin-2026-stellar-colosseum-a-many-agent.pdf) | [2609.15983v2](https://arxiv.org/pdf/2609.15983v2) | 27 | 2026-09-16 |

See its [wiki note](../wiki/self-improving-agents/lin-2026-stellar-colosseum-a-many-agent.md)
for methods, benchmark protocol, limitations, and synthesis.

## Missing-PDF list (legacy records on this branch)

At initial seeding, the working sandbox could not download the PDFs below
from `arxiv.org`. Their exact PDFs are still absent from this branch; upgrades
remain pending in [PR #2](https://github.com/DrSquare/ReflectiveLoop/pull/2). Their `sources/`
and `wiki/` pages were written from publicly reported abstracts/summaries
instead (see `text_extractor: abstract-summary` in their frontmatter). Drop
the real PDF into this folder and re-run the ingest steps in `AGENTS.md` to
upgrade them to full PDF-grounded pages.

| Stem | arXiv | Title |
|---|---|---|
| `lee-2026-meta-harness-end-to-end` | [2603.28052](https://arxiv.org/abs/2603.28052) | Meta-Harness: End-to-End Optimization of Model Harnesses |
| `zhang-2026-hyperagents` | [2603.19461](https://arxiv.org/abs/2603.19461) | Hyperagents |
| `hebbar-2026-sia-self-improving-ai` | [2605.27276](https://arxiv.org/abs/2605.27276) | SIA: Self Improving AI with Harness & Weight Updates |
| `feng-2026-coskill-joint-reinforcement` | [2609.04865](https://arxiv.org/abs/2609.04865) | CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution |
| `park-2026-autosaddler-automatic-harness-optimization-with` | [2608.23041](https://arxiv.org/abs/2608.23041) | AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces |

## September 16 recovery checkpoint: not admitted

These are retrieval/publication-pending candidates, not additional catalog entries.
No source/wiki placeholder has been created. See the [scan checkpoint](../agenda/llm-wiki-ops/pending-ingestions/2026-09-16-scan-checkpoint.json) and [dated log](../logs/2026-09-16-codex-workspace.md).

| Paper | Exact version | Current blocker |
|---|---|---|
| HarnessForge | [2606.01779v1](https://arxiv.org/pdf/2606.01779v1) | Download/hash reverified; interrupted binary upload; expected Git blob returns 404 |
| Co-Evolving Harnesses and Models | [2609.09134v1](https://arxiv.org/pdf/2609.09134v1) | Download/hash reverified; not attached to a completed ingestion tree; binary connector read cannot be decoded |
| The Last AI Built by Humans | [2609.11873v2](https://arxiv.org/pdf/2609.11873v2) | Exact download and partial review; PDF syntax warnings need rendering/validation; versioned hash and full review incomplete |
| Continual Harness | [2605.09998v1](https://arxiv.org/pdf/2605.09998v1) | Prior reviewed exact PDF exceeds 16 MiB base64 request limit; shell Git lacks authentication |
| SkillRL | [2602.08234v1](https://arxiv.org/pdf/2602.08234v1) | Prior reviewed exact PDF exceeds 16 MiB base64 request limit; shell Git lacks authentication |

The five legacy entries above remain unchanged. Their separate pending PDF upgrades,
including AutoSaddler's full-text corrections, must not be lost during integration.
