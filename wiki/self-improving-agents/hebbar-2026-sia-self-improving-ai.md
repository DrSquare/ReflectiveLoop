---
title: "SIA: Self Improving AI with Harness & Weight Updates"
authors: Prannay Hebbar, Yogendra Manawat, Samuel Verboomen, Alesia Ivanova, Selvam Palanimalai, Kunal Bhatia, Vignesh Baskaran
year: 2026
doi: arXiv:2605.27276
source: hebbar-2026-sia-self-improving-ai.md
category: [self-improving-agents]
pdf_path: /papers/hebbar-2026-sia-self-improving-ai.pdf
pdf_filename: hebbar-2026-sia-self-improving-ai.pdf
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: 2026-09-08
tags: [harness, weight-update, lora, multi-agent]
arxiv_version: 2605.27276v2
pdf_url: https://arxiv.org/pdf/2605.27276v2
pdf_pages: 15
pdf_sha256: 3f75a62487a5fb3fc2db8d06b78e6f6d598fc46b446cdfa9e205c33fb41de265
full_text_reviewed_date: 2026-09-08
---

## Summary

SIA uses a Feedback-Agent to choose harness edits or task-model weight updates. Adding weight updates after harness search improves reported results on three tasks; the paper does **not** include a weight-only control. [§6.2, pp. 8-9; Table 3, p. 11](https://arxiv.org/pdf/2605.27276v2#page=8)

## Key Contributions

- Gives one feedback loop access to both scaffold editing and model training.
- Reports task-specific training choices and incremental improvements over harness-only operating points.
- Leaves learning the Feedback-Agent's own action-selection policy to future work. [§§5, 7.3, 9, pp. 6, 12-13](https://arxiv.org/pdf/2605.27276v2#page=12)

## Methodology and Architecture

Claude Sonnet 4.6 initializes/revises the scaffold; gpt-oss-120b executes, with LoRA rank 32 and learning rate 4e-5 for weight updates. Each action freezes the other component. The reported runs begin with harness search and switch to training after stalling; the freely interleaved architecture is broader than the demonstrated schedule. [§§5.2-6.2, pp. 8-9; §9, p. 13](https://arxiv.org/pdf/2605.27276v2#page=8)

LawBench rollouts generate solution scripts, with TF-IDF/LinearSVC developed during harness search and PPO/GAE used for model training. TriMul uses entropic advantage weighting for fixed-shape kernel optimization; MAGIC denoising uses GRPO. The latter produces clipping/rounding code after training. [§6.3, pp. 9-11](https://arxiv.org/pdf/2605.27276v2#page=9)

## Results

| Metric | Initial | Harness-only | Harness + weights | Comparison |
|---|---:|---:|---:|---|
| LawBench accuracy | 13.5% | 50.0% | 70.1% | +20.1 points vs harness-only, +25.1 points vs cited prior 45.0%. |
| TriMul reward, higher better | 0.105 | 0.120 | 1.475 | Runtime 12,483 to 1,017 μs, a 91.9% reduction vs harness-only; 12.4% vs prior 1,161 μs. |
| Denoising `mse_norm`, higher better | 0.048 | 0.241 | 0.289 | About +19.9% vs harness-only; +20.4% vs prior 0.240; +502.1% vs initial. |

Operating points: [Table 3, p. 11](https://arxiv.org/pdf/2605.27276v2#page=11); runtime: [§6.3.2, p. 10](https://arxiv.org/pdf/2605.27276v2#page=10). Percent changes are computed from the displayed values. `mse_norm` is the paper's quality score, not conventional lower-is-better MSE.

**Limits:** §6.3.1 describes RL solution scripts scored against the LawBench test split, so 70.1% is not established as independent final-test generalization. TriMul uses a fixed shape and denoising has no reported train/test split. No weight-only, matched-compute, or repeated-seed comparison establishes universal complementarity. [Table 2/§6.3.1, pp. 8-9](https://arxiv.org/pdf/2605.27276v2#page=8); [Table 3, p. 11](https://arxiv.org/pdf/2605.27276v2#page=11)

## Related Papers

- [[overviews/self-improving-llm-agents]] retains the two-lever hypothesis with these evidence limits.
- [[lee-2026-meta-harness-end-to-end]] and [[zhang-2026-hyperagents]] are explicitly discussed in SIA's full text. Their inclusion is a methodological comparison, not proof of a matched experiment. Meta-Harness describes 215 LawBench classes; SIA describes 191. [SIA, §4.1, p. 4](https://arxiv.org/pdf/2605.27276v2#page=4); [Meta-Harness, p. 6](https://arxiv.org/pdf/2603.28052v1#page=6)
- [Detailed source analysis](../../sources/hebbar-2026-sia-self-improving-ai.md); [canonical PDF](../../papers/hebbar-2026-sia-self-improving-ai.pdf).
