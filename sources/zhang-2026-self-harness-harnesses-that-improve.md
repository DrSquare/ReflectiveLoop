---
title: "Self-Harness: Harnesses That Improve Themselves"
authors: "Zhang, Hangfan; Zhang, Shao; Li, Kangcong; Zhang, Chen; Chen, Yang; Zhang, Yiqun; Bai, Lei; Hu, Shuyue"
year: 2026
doi: "arXiv:2606.09498"
category: ["self-improving-agents"]
pdf_path: "/papers/zhang-2026-self-harness-harnesses-that-improve.pdf"
pdf_filename: "zhang-2026-self-harness-harnesses-that-improve.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2606.09498v1"
pdf_url: "https://arxiv.org/pdf/2606.09498v1"
pdf_pages: 19
pdf_sha256: "065712f5bc1caeed717ad94e68bc0a011420417e86ef9b919ddb5e44e41398ab"
full_text_reviewed_date: "2026-09-11"
---

## One-line Summary

Self-Harness uses the same frozen model to solve tasks and propose bounded changes to its own harness, with regression scores deciding which edits survive.

## 1. Document Information

Self-Harness: Harnesses That Improve Themselves. 2606.09498v1; first submitted 2026/06/08. The exact [local PDF](../papers/zhang-2026-self-harness-harnesses-that-improve.pdf) has 19 pages. Citations use 1-based PDF pages. Review covers the main method, cited experiments and limitations; no reproduction was run. No unambiguous official implementation URL was verified in the reviewed PDF text; none is inferred from a project name.

## 2. Key Contributions

Connects verifier-grounded failure clusters to specific editable harness surfaces. Proposals include the suspected failure mechanism and an auditable edit; diverse candidates explore different repairs. It studies self-proposal without a stronger external proposer. [PDF p. 4](https://arxiv.org/pdf/2606.09498v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2606.09498v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2606.09498v1#page=6)

## 3. Methodology and Architecture

Each round mines failures, proposes candidate changes, evaluates them, and merges compatible accepted edits. The editable object is a DeepAgent harness definition. Acceptance requires nonnegative changes on both held-in and held-out splits and a strict gain on at least one. Model weights, evaluator, and that acceptance rule remain fixed. [PDF p. 4](https://arxiv.org/pdf/2606.09498v1#page=4) [PDF p. 7](https://arxiv.org/pdf/2606.09498v1#page=7) [PDF p. 8](https://arxiv.org/pdf/2606.09498v1#page=8)

## 4. Key Results and Benchmarks

On a filtered 64-task subset of the 89 Terminal-Bench-2.0 tasks, the paper reports held-out pass rates of 40.5% to 61.9% for MiniMax M2.5, 23.8% to 38.1% for Qwen3.5-35B-A3B, and 42.9% to 57.1% for GLM-5. Scores average two attempts per candidate unless stated otherwise. They are not directly comparable to full-benchmark rankings. [PDF p. 7](https://arxiv.org/pdf/2606.09498v1#page=7) [PDF p. 9](https://arxiv.org/pdf/2606.09498v1#page=9)

## 5. Limitations and Future Work

Crucially, the so-called held-out scores participate in candidate promotion (Algorithm 1 and Section 3.4). Hiding tasks from the proposer does not make those scores an untouched final test: selection still adapts to them. The wiki therefore classifies this as regression-gated development evidence. Multimodal and unstable-web tasks are excluded, and no cross-domain transfer of the editing procedure is established. [PDF p. 4](https://arxiv.org/pdf/2606.09498v1#page=4) [PDF p. 7](https://arxiv.org/pdf/2606.09498v1#page=7) [PDF p. 9](https://arxiv.org/pdf/2606.09498v1#page=9)

## 6. Related Work

[[lee-2026-meta-harness-end-to-end]]; [[zhang-2026-hyperagents]]. Synthesis: [[concepts/evaluating-self-improvement]] and [[overviews/self-improving-llm-agents]].

## 7. Glossary

Evidence bundle: failure clusters grounded in execution and verifier outcomes. Promotion gate: the rule selecting harness edits. Untouched test: data unused in proposal, tuning, selection, or stopping.
