---
title: "AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces"
authors: Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
year: 2026
doi: arXiv:2608.23041
source: park-2026-autosaddler-automatic-harness-optimization-with.md
category: [self-improving-agents]
pdf_path: /papers/park-2026-autosaddler-automatic-harness-optimization-with.pdf
pdf_filename: park-2026-autosaddler-automatic-harness-optimization-with.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-08
tags: [harness, scaffold-optimization, offline-learning, execution-traces]
---

## Summary
AutoSaddler treats automatic harness optimization as offline learning
over already-collected agent execution traces. It diagnoses failures in
mini-batches of traces, emits structured code patches against the
harness, and keeps only the patches that survive validation — so the
improvements are durable across iterations rather than fixes for a
single trajectory.

## Key Contributions
- Offline formulation of harness optimization, driven by failure signals
  aggregated over mini-batches of tasks.
- Failure-trace diagnosis (deep debugging) as the update signal.
- Structured patch generation that treats the harness as code, keeping
  edits targeted.
- Validation-based selection of updates, favouring generalization over
  trajectory-specific repair.

## Methodology and Architecture
Iterative loop: execute the current harness on a mini-batch of tasks →
collect execution traces → diagnose failures → generate a structured
patch to the harness source → accept or reject the patch on validation
performance. Accepted patches persist into later iterations. The
abstract does not specify the harness representation, patch format, or
model/compute configuration; those need the PDF.

## Results
- GAIA2: +9.0 points.
- SWE-Bench Pro: +9.6 points.
- Terminal-Bench 2.0: +10.0 points.
- Ablations favour deep debugging over shallow reflection, targeted
  modification over unconstrained editing, and generalization-aware
  selection over trajectory-specific repair.

Baselines, configurations, and run-to-run variance are not stated in the
abstract this page is based on.

## Related Papers
- [[overviews/self-improving-llm-agents]] — the synthesis anchor for
  harness/meta-agent/skill-library optimization in this wiki; AutoSaddler
  is the offline, validation-gated point in that design space.
- [[lee-2026-meta-harness-end-to-end]] (Meta-Harness) — the closest
  comparison: also optimizes the harness from execution traces, but via
  online agentic search with full history in context, whereas
  AutoSaddler learns offline from mini-batches and gates each structured
  patch on validation.
- [[hebbar-2026-sia-self-improving-ai]] (SIA) — combines harness
  revision with weight updates; AutoSaddler improves only the harness.
