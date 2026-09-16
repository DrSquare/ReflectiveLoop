# ReflectiveLoop

A literature review knowledge base built on the LLM Wiki pattern
(see `AGENTS.md` for the full rules/schema). This branch has **1 PDF-grounded
admitted paper and 5 legacy abstract-only records**: **6 paper entries** in
the catalog and **8 wiki pages** in total. The [PDF manifest](papers/manifest.json)
keeps complete entries separate from legacy records awaiting PDF upgrades.

## Added September 16, 2026

- [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](wiki/self-improving-agents/lin-2026-stellar-colosseum-a-many-agent.md) ([arXiv:2609.15983v2](https://arxiv.org/abs/2609.15983v2)) — Readiness-gated proof planning, overlapping candidate-and-critique aggregation, and localized repair with persistent research memory. An inference-time harness comparator; learning the controller or model remains future work.

## Legacy records awaiting PDF upgrades

These five existing notes are based on abstracts/summaries on this branch.
Their full-text upgrades remain in separate pending work.

- [Meta-Harness: End-to-End Optimization of Model Harnesses](wiki/self-improving-agents/lee-2026-meta-harness-end-to-end.md) ([arXiv:2603.28052](https://arxiv.org/abs/2603.28052))
- [Hyperagents](wiki/self-improving-agents/zhang-2026-hyperagents.md) ([arXiv:2603.19461](https://arxiv.org/abs/2603.19461))
- [SIA: Self Improving AI with Harness & Weight Updates](wiki/self-improving-agents/hebbar-2026-sia-self-improving-ai.md) ([arXiv:2605.27276](https://arxiv.org/abs/2605.27276))
- [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution](wiki/self-improving-agents/feng-2026-coskill-joint-reinforcement.md) ([arXiv:2609.04865](https://arxiv.org/abs/2609.04865))
- [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](wiki/self-improving-agents/park-2026-autosaddler-automatic-harness-optimization-with.md) ([arXiv:2608.23041](https://arxiv.org/abs/2608.23041))

See [`index.md`](index.md) for the full generated catalog and
[`wiki/overviews/self-improving-llm-agents.md`](wiki/overviews/self-improving-llm-agents.md)
for synthesis and evidence boundaries. The [exact-PDF inventory](papers/README.md)
tracks which full texts are present on this branch.

## Adding a paper
Follow the ingest steps in [`AGENTS.md`](AGENTS.md), then regenerate the
catalog:
```bash
python3 scripts/build_index.py --apply
```
