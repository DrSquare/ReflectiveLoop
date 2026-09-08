---
title: "SIA: Self Improving AI with Harness & Weight Updates"
authors: Prannay Hebbar, Yogendra Manawat, Samuel Verboomen, Alesia Ivanova, Selvam Palanimalai, Kunal Bhatia, Vignesh Baskaran
year: 2026
doi: arXiv:2605.27276
category: [self-improving-agents]
pdf_path: /papers/hebbar-2026-sia-self-improving-ai.pdf
pdf_filename: hebbar-2026-sia-self-improving-ai.pdf
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: 2026-09-08
arxiv_version: 2605.27276v2
pdf_url: https://arxiv.org/pdf/2605.27276v2
pdf_pages: 15
pdf_sha256: 3f75a62487a5fb3fc2db8d06b78e6f6d598fc46b446cdfa9e205c33fb41de265
full_text_reviewed_date: 2026-09-08
---

## One-line Summary

SIA lets a frozen Feedback-Agent select harness edits or task-model training; its reported harness-plus-weight results improve on harness-only search in three tasks, but do not establish superiority over weight-only training or clean out-of-sample generalization. [§§5-7, pp. 6-12](https://arxiv.org/pdf/2605.27276v2#page=6)

## 1. Document Information

- Hebbar et al., *SIA: Self Improving AI with Harness & Weight Updates*, arXiv:2605.27276v2, May 28, 2026 (first submitted May 26); 15 pages. Grounded in the exact [local PDF](../papers/hebbar-2026-sia-self-improving-ai.pdf), retrieved September 8, 2026. Citations use 1-based PDF pages.
- This note distinguishes reported experiments, proposed architecture, and this wiki's assessment of evidential limits. It does not reproduce the experiments or certify the paper's SOTA claims.

## 2. Key Contributions

- Adds model training as an action available to the feedback loop, alongside scaffold edits. The Meta-Agent initializes a task agent, the task agent executes, and the Feedback-Agent reads source, trajectories, and scores to choose a change. [§§3.2-3.3, pp. 3-4](https://arxiv.org/pdf/2605.27276v2#page=3)
- Reports higher results from adding weight updates after harness progress plateaus on LawBench, TriMul kernel optimization, and MAGIC denoising. Table 3 contains initial, prior-SOTA, harness-only, and harness-plus-weight conditions; **no weight-only condition** is reported. [§6.2, pp. 8-9](https://arxiv.org/pdf/2605.27276v2#page=8); [Table 3, p. 11](https://arxiv.org/pdf/2605.27276v2#page=11)
- Uses different training choices across the three tasks, rather than one universal RL objective. [§7.3, p. 12](https://arxiv.org/pdf/2605.27276v2#page=12)

## 3. Methodology and Architecture

The Meta-Agent and Feedback-Agent use Claude Sonnet 4.6. The task agent uses gpt-oss-120b or an adapted checkpoint. LoRA rank is 32 and the reported learning rate is 4e-5; the paper describes H100/Modal training infrastructure. During a harness action the current model is frozen; during a weight action the current scaffold is fixed. [§4.3, p. 5](https://arxiv.org/pdf/2605.27276v2#page=5); [§§5.2-6.1, p. 8](https://arxiv.org/pdf/2605.27276v2#page=8)

The architecture permits choosing between the two actions, but the reported experiments begin with scaffold iteration and switch to training after stalling. Section 9 describes current rounds as coarse-grained and leaves finer interleaving to future work. The conceptual freely interleaved diagram should not be read as a measured comparison of schedules. [§5.1/Fig. 2, pp. 6-7](https://arxiv.org/pdf/2605.27276v2#page=6); [§6.2, pp. 8-9](https://arxiv.org/pdf/2605.27276v2#page=8); [§9, p. 13](https://arxiv.org/pdf/2605.27276v2#page=13)

Task details materially refine the original summary:

- **LawBench:** the generated artifact is classification code. Harness search develops TF-IDF + LinearSVC and tunes n-grams/regularization. PPO with GAE applies to generated solution scripts, whose executions produce accuracy rewards. This is more specific than directly fine-tuning an LLM to emit a criminal charge. [§6.3.1, p. 9](https://arxiv.org/pdf/2605.27276v2#page=9)
- **TriMul:** the agent writes a kernel for a fixed input shape on H100. Entropic weighting emphasizes high-reward rollouts in a sparse reward setting. The verifier score is 1500/runtime, with runtime in microseconds. [Table 2, p. 8](https://arxiv.org/pdf/2605.27276v2#page=8); [§6.3.2, pp. 9-10](https://arxiv.org/pdf/2605.27276v2#page=9)
- **Denoising:** the task optimizes MAGIC parameters/preprocessing on pancreas scRNA-seq data. GRPO-trained output introduces nonnegative clipping and integer rounding. The paper calls `mse_norm` a normalized reconstruction-quality score with **higher better**; it is not ordinary MSE. [§6.3.3, pp. 10-11](https://arxiv.org/pdf/2605.27276v2#page=10)

## 4. Key Results and Benchmarks

| Task/metric | Initial | Paper's prior-SOTA comparator | Harness only | Harness + weights | Interpretation |
|---|---:|---:|---:|---:|---|
| LawBench top-1 accuracy | 13.5% | 45.0% | 50.0% | 70.1% | +20.1 percentage points vs harness-only; +25.1 points vs cited prior score, not 25.1% relative. |
| TriMul reward (1500/runtime) | 0.105 | 1.292 | 0.120 | 1.475 | Corresponding reported runtimes: harness-only 12,483 μs, combined 1,017 μs, prior 1,161 μs. |
| Denoising `mse_norm`, higher better | 0.048 | 0.240 | 0.241 | 0.289 | Approximately +19.9% relative to harness-only, +20.4% to prior, +502.1% to initial. |

All tabulated operating points come from [Table 3, p. 11](https://arxiv.org/pdf/2605.27276v2#page=11); runtime comparisons are in [§§1.3 and 6.3.2, pp. 2, 10](https://arxiv.org/pdf/2605.27276v2#page=10). Relative percentages above are calculated from the displayed values. The runtime reduction is 91.9% against harness-only and 12.4% against the prior comparator. **12,483 μs is the harness-only peak, not the initial baseline.** Figures and tables mix speedup, runtime, and reward; these are not interchangeable units.

## 5. Limitations and Future Work

- **Test-feedback exposure:** Table 2 names a held-out test-split grader, and §6.3.1 explicitly says RL rollouts are solution scripts executed against that test split. Consequently the reported 913-example score is not demonstrated to be an untouched final test after adaptive search/training. The 5,332/913 split alone does not establish independence. This is an inference from the stated protocol, not a code audit. [pp. 8-9](https://arxiv.org/pdf/2605.27276v2#page=8)
- **Other tasks:** TriMul is fixed-shape optimization; denoising has no train/test split reported in Table 2. These demonstrate optimization against supplied verifiers, not broad cross-task transfer. [p. 8](https://arxiv.org/pdf/2605.27276v2#page=8)
- **Ablation limits:** no weight-only control, matched total-compute comparison, repeated-seed uncertainty, or factorial interaction estimate is provided in the reported results. The evidence supports incremental gains after harness search; it does not prove that both levers are necessary, universally complementary, or better than either alone. [§§6-7, pp. 8-12](https://arxiv.org/pdf/2605.27276v2#page=8)
- **Mechanism limits:** observations of new kernels or rounding after training do not prove those outputs were impossible for another harness around the base model. The paper's stronger claims about inaccessible domain knowledge remain interpretations. [§7.4, p. 13](https://arxiv.org/pdf/2605.27276v2#page=13)
- The authors identify shared-verifier overoptimization as a limitation. Their Nash-equilibrium description is discussion, without a formal game/proof here. The action selector uses a frozen LLM prior; learning that selector through meta-RL is explicitly future work. [§§8-9, p. 13](https://arxiv.org/pdf/2605.27276v2#page=13)

## 6. Related Work

The full text explicitly discusses [[lee-2026-meta-harness-end-to-end]] and [[zhang-2026-hyperagents]] in §4.1 and Table 1. This corrects the old synthesis's blanket absence-of-comparison claim. However, a methodological comparison and reported prior scores do not establish a controlled head-to-head run. Meta-Harness describes 215 LawBench classes; SIA describes 191 and code-generating rollouts, so identical evaluation cannot be assumed. [SIA, pp. 4, 6, 9](https://arxiv.org/pdf/2605.27276v2#page=4); [Meta-Harness, §4.1, p. 6](https://arxiv.org/pdf/2603.28052v1#page=6)

[[feng-2026-coskill-joint-reinforcement]] also updates model weights, but jointly trains reasoning and skill-editing roles under one shared actor. See [[overviews/self-improving-llm-agents]] for the bounded synthesis.

## 7. Glossary

- **SIA-H:** best reported harness-only operating point.
- **SIA-W+H:** operating point after adding weight updates.
- **LoRA:** low-rank trainable adapters to the task model.
- **Verifier:** task scoring mechanism used to guide optimization; its exposure determines whether evaluation is independent.
