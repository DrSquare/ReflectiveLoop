---
title: "AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces"
authors: Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
year: 2026
doi: arXiv:2608.23041
category: [self-improving-agents]
pdf_path: /papers/park-2026-autosaddler-automatic-harness-optimization-with.pdf
pdf_filename: park-2026-autosaddler-automatic-harness-optimization-with.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-08
---

## One-line Summary
AutoSaddler casts automatic harness optimization as offline learning:
it diagnoses failure traces from mini-batches of agent executions,
generates structured patches that treat the harness as code, and keeps
only the updates that survive validation, yielding durable harness
improvements on GAIA2, SWE-Bench Pro, and Terminal-Bench 2.0.

## 1. Document Information
- arXiv: 2608.23041, version v1 submitted 24 August 2026.
- The arXiv abstract page links a project website and a code release;
  neither could be inspected from this environment (no network access to
  `arxiv.org`), so their URLs are not recorded here.
- No PDF is available in `papers/` for this paper; see the missing-PDF
  list in `papers/README.md`. Everything below is grounded in the
  publicly reported abstract only (`text_extractor: abstract-summary`).

## 2. Key Contributions
- Frames automatic harness optimization as an *offline learning* problem
  over previously collected agent execution traces, rather than as an
  online search that must re-run the agent for every candidate.
- Iterative updates driven by failure signals accumulated over
  mini-batches of tasks, rather than from a single trajectory.
- Failure-trace diagnosis ("deep debugging") as the source of the update
  signal, instead of shallow self-reflection over outcomes.
- Structured patch generation that treats the harness as code, so edits
  are targeted rather than unconstrained rewrites.
- Validation-based update selection, keeping only changes that
  generalize instead of those that repair one specific trajectory.

## 3. Methodology and Architecture
The reported pipeline is a loop over mini-batches of tasks: run the
current harness, collect execution traces, diagnose the failures in
those traces, generate a structured patch against the harness source,
and then accept or reject that patch based on validation performance.
Accepted patches are durable — they persist into subsequent iterations,
so improvement accumulates across mini-batches instead of being scoped to
the trajectory that produced the signal. The abstract does not describe
the harness representation, patch format, model choices, or
compute budget in enough detail to reproduce the system; those details
require the PDF.

## 4. Key Results and Benchmarks
Reported gains over the respective baselines:

| Benchmark | Reported gain |
|---|---|
| GAIA2 | +9.0 points |
| SWE-Bench Pro | +9.6 points |
| Terminal-Bench 2.0 | +10.0 points |

Ablations reported in the abstract favor:
- deep failure-trace debugging over shallow reflection;
- targeted, structured modifications over unconstrained editing;
- generalization-aware (validation-based) selection over
  trajectory-specific repair.

Baseline identities, harness/model configurations, and variance across
runs are not stated in the abstract.

## 5. Limitations and Future Work
- As summarized here, the evidence base is the abstract alone; no
  numbers were verified against the full paper.
- The method depends on collecting and storing agent execution traces
  and on having a validation split large enough to distinguish
  generalizing patches from trajectory-specific ones.
- Being offline, the approach optimizes against the task distribution
  present in the collected traces; behaviour under distribution shift is
  not addressed in the abstract.

## 6. Related Work
- [[lee-2026-meta-harness-end-to-end]] (Meta-Harness) — the closest
  neighbour in this wiki: also optimizes the harness around a frozen
  model using execution traces, but as an online agentic search over
  harness variants with full history in context, where AutoSaddler runs
  offline over mini-batches with validation-gated structured patches.
- [[hebbar-2026-sia-self-improving-ai]] (SIA) — pairs harness revision
  with model weight updates; AutoSaddler stays entirely on the harness
  axis.

## 7. Glossary
- **Harness**: The code and control flow surrounding a frozen LLM that
  determines what the model sees and how its outputs are used.
- **Durable update**: A harness change that is retained across
  optimization iterations rather than applied only to the trajectory
  that motivated it.
- **Structured patch**: A constrained, code-level edit to the harness,
  as opposed to an unconstrained rewrite.
- **Validation-based selection**: Accepting a candidate update only if
  it improves performance on held-out validation tasks.
