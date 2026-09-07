---
title: "SIA: Self Improving AI with Harness & Weight Updates"
authors: Prannay Hebbar, et al. (Hexo Labs)
year: 2026
doi: arXiv:2605.27276
category: [self-improving-agents]
pdf_path: /papers/hebbar-2026-sia-self-improving-ai.pdf
pdf_filename: hebbar-2026-sia-self-improving-ai.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
---

## One-line Summary
SIA combines harness (scaffold) revision with model weight updates (RL +
LoRA) in one self-improvement loop, addressing the "human bottleneck" of
manually designing/tuning both the model and its surrounding scaffold.

## 1. Document Information
- arXiv: 2605.27276, submitted May 2026, from Hexo Labs.
- Code: https://github.com/hexo-ai/sia (MIT-licensed)

## 2. Key Contributions
- Diagnoses that prior work improves either the harness (with weights
  fixed) or the weights (with a fixed pipeline), never both together.
- Proposes a three-agent architecture: a Meta-Agent that generates the
  initial scaffold, a Task Agent that executes and logs, and a
  Feedback-Agent that reviews full trajectories and decides whether to
  revise the harness or update model weights.
- Shows combining harness and weight updates consistently beats using
  either alone.

## 3. Methodology and Architecture
- **Meta-Agent** (Claude Sonnet): generates an initial scaffold for a task
  from a specification.
- **Task Agent** (GPT-style base model): executes the task and logs
  actions/results.
- **Feedback-Agent** (Claude Sonnet): reviews full trajectories and picks
  between harness revision (prompts, logic, tool dispatch, error handling)
  or weight update (RL with LoRA) as the next self-improvement step.

## 4. Key Results and Benchmarks
- LawBench (Chinese legal charge classification, 191 classes): 13.5%
  initial → 50% after scaffold iteration → 70.1% with full SIA (weights +
  harness), a 25.1+ point improvement over the previous SOTA.
- GPU kernel optimization (AlphaFold2-like CUDA kernel): scaffold-only
  gives 1.14x speedup; full SIA cuts runtime from 12,483μs to 1,017μs
  (91.9% reduction).
- Single-cell RNA denoising: 502% improvement over baseline.

## 5. Limitations and Future Work
- Weight updates rely on LoRA-based RL, which may not capture all forms of
  task-specific "intuition" for every domain.
- Three-agent architecture introduces coordination/orchestration overhead
  that is not deeply characterized in the reported results.

## 6. Related Work
- Directly comparable to [[lee-2026-meta-harness-end-to-end]]
  (Meta-Harness), which optimizes only the harness, not model weights.
- Related to [[zhang-2026-hyperagents]] (Hyperagents), which also unifies
  a task-solving and a self-modifying component, but focuses on making the
  meta-level procedure itself modifiable rather than choosing between
  harness vs. weight updates.

## 7. Glossary
- **Harness/scaffold**: Tools, prompts, control logic, and retry policy
  around a model.
- **Weight update**: Applying RL (here, LoRA) to change the underlying
  model's parameters directly.
