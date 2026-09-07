---
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
authors: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
year: 2026
doi: arXiv:2603.28052
source: lee-2026-meta-harness-end-to-end.md
category: [self-improving-agents]
pdf_path: /papers/lee-2026-meta-harness-end-to-end.pdf
pdf_filename: lee-2026-meta-harness-end-to-end.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
tags: [harness, scaffold-optimization, agentic-search]
---

## Summary
Meta-Harness automates the design of the code "harness" surrounding a
frozen LLM by framing it as a search problem: an agentic proposer with
filesystem access to the full history of harness source, scores, and
execution traces (up to 10M tokens/step) proposes better harnesses than
hand-engineering or prior scalar-feedback optimizers.

## Key Contributions
- The harness, not just model weights, can swing benchmark performance up
  to 6x.
- Prior automatic harness/prompt optimizers compress feedback too much
  (scalar scores / short summaries), which caps improvement.
- An agentic proposer with full historical context (source, scores,
  traces on disk) outperforms these compressed-feedback optimizers.

## Methodology and Architecture
Iterative search over harness variants: at each step, the proposer reads
the complete history of previously tried harnesses (not a compressed
summary) and proposes the next candidate.

## Results
- +7.7 points on text classification vs. SOTA, with 4x fewer context
  tokens.
- +4.7 points on IMO-level math accuracy (averaged across 5 LLMs).
- Surpasses best hand-designed harness baselines on TerminalBench-2.

## Related Papers
- [[overviews/self-improving-llm-agents]] — one of four papers surveyed
  there on turning fixed agent components into optimization targets.
- [[hebbar-2026-sia-self-improving-ai]] — also separates harness updates
  from a second improvement axis (SIA uses model weight updates; SIA's
  Feedback-Agent explicitly chooses between the two).
