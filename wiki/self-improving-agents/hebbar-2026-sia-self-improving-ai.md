---
title: "SIA: Self Improving AI with Harness & Weight Updates"
authors: Prannay Hebbar, et al. (Hexo Labs)
year: 2026
doi: arXiv:2605.27276
source: hebbar-2026-sia-self-improving-ai.md
category: [self-improving-agents]
pdf_path: /papers/hebbar-2026-sia-self-improving-ai.pdf
pdf_filename: hebbar-2026-sia-self-improving-ai.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
tags: [harness, weight-update, lora, multi-agent]
---

## Summary
SIA jointly updates an agent's harness (scaffold) and its model weights
(via RL + LoRA) in one self-improvement loop, using a Meta-Agent /
Task Agent / Feedback-Agent split, and shows combining both update types
beats using either alone.

## Key Contributions
- Diagnoses the "human bottleneck": prior work improves either the harness
  (weights fixed) or the weights (fixed pipeline), never both together.
- Three-agent architecture: Meta-Agent generates the scaffold,
  Task Agent executes and logs, Feedback-Agent reviews trajectories and
  picks harness revision vs. weight update as the next step.

## Methodology and Architecture
Meta-Agent (Claude Sonnet) creates the initial scaffold; Task Agent (GPT-style
model) executes; Feedback-Agent (Claude Sonnet) reviews full trajectories and
decides between revising the harness (prompts/logic/tool dispatch/error
handling) or updating model weights with LoRA-based RL.

## Results
- LawBench: 13.5% → 50% (scaffold only) → 70.1% (full SIA), +25.1 points
  over prior SOTA.
- GPU kernel optimization: runtime cut from 12,483μs to 1,017μs (91.9%
  reduction).
- Single-cell RNA denoising: 502% improvement over baseline.

## Related Papers
- [[overviews/self-improving-llm-agents]] — surveyed alongside
  Meta-Harness, Hyperagents, and CoSkill.
- [[lee-2026-meta-harness-end-to-end]] — SIA's harness-revision arm is
  directly comparable to Meta-Harness's harness-only optimization; SIA
  additionally shows adding weight updates on top consistently helps
  further.
