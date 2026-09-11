# ReflectiveLoop

A literature-review knowledge base for self-improving agent harnesses, skills, and systems, following the LLM Wiki pattern. This branch contains **14 PDF-grounded papers**, with source notes, synthesis pages, and research questions.

Start with the [generated catalog](index.md), [overview](wiki/overviews/self-improving-llm-agents.md), [mechanism comparison](wiki/concepts/procedural-self-improvement.md), and [evaluation boundaries](wiki/concepts/evaluating-self-improvement.md).

## September 11, 2026 UTC additions

- [SkillAdam](wiki/self-improving-agents/li-2026-skilladam-stable-and-efficient-skill.md) — SkillAdam uses persistent issue history and an adaptive edit budget to stabilize optimization of natural-language skill documents around frozen models.
- [SE-GoS](wiki/self-improving-agents/fu-2026-se-gos-self-evolving-graph.md) — SE-GoS evolves the graph and descriptions used to retrieve existing skills, while preserving skill content, model weights, and the retrieval algorithm.
- [SkillForge](wiki/self-improving-agents/yang-2026-skillforge-evolving-verifiable-skills-for.md) — SkillForge makes skill invocation explicit in agent trajectories and revises skills using usage outcomes while training the policy with GRPO.
- [Prime Agent](wiki/self-improving-agents/karten-2026-prime-agent-a-self-improving.md) — Prime Agent packages a persistent REPL, recursive agent sessions, and versioned harness state into a runtime for long-horizon reasoning and execution.
- [Evo-Harness](wiki/self-improving-agents/wei-2026-evo-harness-context-to-harness.md) — Evo-Harness compiles failed one-shot task executions into reusable general and task-type guidance for a frozen solver operating on a task stream.
- [SESA](wiki/self-improving-agents/fu-2026-self-play-meets-skill-evolution.md) — SESA couples search self-play to an evolving skill bank, allowing skill-conditioned learning to improve both model parameters and optional inference-time memory.
- [Self-Harness](wiki/self-improving-agents/zhang-2026-self-harness-harnesses-that-improve.md) — Self-Harness uses the same frozen model to solve tasks and propose bounded changes to its own harness, with regression scores deciding which edits survive.
- [Life-Harness](wiki/self-improving-agents/xu-2026-adapting-the-interface-not-the.md) — Life-Harness turns training-trajectory failures into reusable runtime interventions and freezes the resulting harness for held-out evaluation across model backbones.
- [MCE](wiki/self-improving-agents/ye-2026-meta-context-engineering-via-agentic.md) — MCE evolves the instructions and code that build context, then executes those skills to produce context artifacts, while keeping model weights frozen.
- [Darwin Godel Machine](wiki/self-improving-agents/zhang-2025-darwin-godel-machine-open-ended.md) — The Darwin Godel Machine evolves a population of coding agents that modify their own implementations, retaining useful stepping stones under empirical evaluation.

The four original papers are Meta-Harness, Hyperagents, SIA, and CoSkill. Their PDF-grounded corrections are preserved from PR #2; AutoSaddler is separately pending in PR #3. This expansion is stacked on the seed-PDF branch and does not merge either PR.

## Daily scan

A ChatGPT task is configured for **08:00 America/Los_Angeles every day**, including daylight-saving changes. It searches primary sources, checks duplicates across the catalog and open PRs, adds exact PDFs and substantive notes, updates synthesis, validates the wiki, and publishes an ingestion PR. It does not merge PRs. See the [scan procedure](agenda/llm-wiki-ops/daily-paper-scan.md) and [scan state](agenda/llm-wiki-ops/scan_state.json). No API key or GitHub Actions runner is required by this repository configuration; the scheduled task uses the connected research and GitHub tools.

## Add or validate papers

Follow [AGENTS.md](AGENTS.md), then run:

```bash
python3 scripts/build_index.py --apply
python3 scripts/validate_wiki.py
```

The [PDF manifest](papers/manifest.json) records versions and provenance. The [scan report](logs/reports/2026-09-11-literature-scan.md) records coverage, evidence qualifications, and pending work. All wiki content is English.
