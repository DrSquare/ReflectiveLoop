---
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
authors: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
year: 2026
doi: arXiv:2603.28052
category: [self-improving-agents]
pdf_path: /papers/lee-2026-meta-harness-end-to-end.pdf
pdf_filename: lee-2026-meta-harness-end-to-end.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
---

## One-line Summary
Meta-Harness treats the code "harness" around an LLM (what to store,
retrieve, and present) as a search problem, using an agentic proposer with
filesystem access to full harness history, scores, and execution traces to
discover better harnesses than hand-engineering or prior scalar-feedback
optimizers.

## 1. Document Information
- arXiv: 2603.28052, submitted March 2026.
- Project page: https://yoonholee.com/meta-harness/
- Code: https://github.com/stanford-iris-lab/meta-harness

## 2. Key Contributions
- Identifies that the harness (control/data flow around a frozen model),
  not just model weights, can swing benchmark performance up to 6x.
- Argues prior text-optimizer approaches for harnesses compress feedback
  too aggressively (scalar scores or short summaries), capping achievable
  improvement.
- Introduces Meta-Harness: an agentic proposer that can read up to 10M
  tokens of diagnostic logs per optimization step (vs. ~26K for prior
  methods), by keeping full harness source, scores, and traces on a
  filesystem rather than compressing them into a prompt.

## 3. Methodology and Architecture
Harness optimization is framed as an iterative search: at each step the
proposer agent inspects the full history of previously tried harnesses
(source code, evaluation scores, and execution traces) stored on disk, and
proposes a new harness variant. This avoids the information bottleneck of
scalar-only or short-summary feedback used by earlier automatic prompt/harness
optimizers.

## 4. Key Results and Benchmarks
- Text classification: +7.7 points over state-of-the-art systems while
  using 4x fewer context tokens.
- Retrieval-augmented math reasoning: +4.7 points on IMO-level problem
  accuracy, averaged across five different LLMs.
- Agentic coding (TerminalBench-2): surpasses the best hand-designed
  harness baselines.

## 5. Limitations and Future Work
- Relies on being able to log and store large volumes of execution traces
  (up to 10M tokens per step), which has storage/compute cost implications.
- Evaluated on a specific set of benchmarks (text classification, math
  reasoning, agentic coding); broader domain generalization is future work.

## 6. Related Work
- Contrasts with prior automatic prompt/harness optimizers that compress
  feedback into scalar scores or brief summaries.
- Related to [[hebbar-2026-sia-self-improving-ai]] (SIA), which also
  separates harness updates from weight updates in a self-improvement loop.

## 7. Glossary
- **Harness**: The code surrounding a frozen LLM that decides what
  information to store, retrieve, and present to the model.
- **Agentic proposer**: An LLM-driven component that proposes new harness
  variants based on full historical context rather than compressed
  feedback.
