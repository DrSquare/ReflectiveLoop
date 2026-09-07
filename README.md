# ReflectiveLoop

A literature review knowledge base built on the LLM Wiki pattern
(see `AGENTS.md` for the full rules/schema). It currently tracks four
papers on self-improving LLM agents:

- [Meta-Harness: End-to-End Optimization of Model Harnesses](wiki/self-improving-agents/lee-2026-meta-harness-end-to-end.md) ([arXiv:2603.28052](https://arxiv.org/abs/2603.28052))
- [Hyperagents](wiki/self-improving-agents/zhang-2026-hyperagents.md) ([arXiv:2603.19461](https://arxiv.org/abs/2603.19461))
- [SIA: Self Improving AI with Harness & Weight Updates](wiki/self-improving-agents/hebbar-2026-sia-self-improving-ai.md) ([arXiv:2605.27276](https://arxiv.org/abs/2605.27276))
- [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution](wiki/self-improving-agents/feng-2026-coskill-joint-reinforcement.md) ([arXiv:2609.04865](https://arxiv.org/abs/2609.04865))

See [`index.md`](index.md) for the full generated catalog and
[`wiki/overviews/self-improving-llm-agents.md`](wiki/overviews/self-improving-llm-agents.md)
for a synthesis of how the four papers relate to each other.

## Adding a paper
Follow the ingest steps in [`AGENTS.md`](AGENTS.md), then regenerate the
catalog:
```bash
python3 scripts/build_index.py --apply
```