---
title: "Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents"
authors: "Xu, Tianshi; Wen, Huifeng; Li, Meng"
year: 2026
doi: "arXiv:2605.22166"
category: ["self-improving-agents"]
pdf_path: "/papers/xu-2026-adapting-the-interface-not-the.pdf"
pdf_filename: "xu-2026-adapting-the-interface-not-the.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2605.22166v1"
pdf_url: "https://arxiv.org/pdf/2605.22166v1"
pdf_pages: 18
pdf_sha256: "2706b7b971130e3f56d368a9de20cd2ce1f5677d570b2df0f2274aaeeff05bcc"
full_text_reviewed_date: "2026-09-11"
---

## Summary

Life-Harness turns training-trajectory failures into reusable runtime interventions and freezes the resulting harness for held-out evaluation across model backbones.

## Key Contributions

Organizes improvement into four interfaces: environment contracts, procedural skills, action realization, and trajectory regulation. This supplies a useful failure taxonomy for deciding whether a problem calls for a prompt, skill, action check, or recovery policy. Initial failure diagnosis includes manual inspection; this is not evidence of an entirely human-free discovery pipeline. [PDF p. 5](https://arxiv.org/pdf/2605.22166v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2605.22166v1#page=6)

## Methodology and Architecture

Qwen3-4B-Instruct produces training trajectories. A coding agent inspects them and edits an environment-specific harness. BM25 retrieves procedural skills, deterministic checks permit or block actions, and trajectory monitoring reacts to loops or exhausted budgets. The harness is frozen for testing and reused with 17 additional backbones; adapting within an episode is distinct from creating persistent interventions from test failures. [PDF p. 2](https://arxiv.org/pdf/2605.22166v1#page=2) [PDF p. 6](https://arxiv.org/pdf/2605.22166v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2605.22166v1#page=7)

## Results

The paper reports improvement in 116 of 126 model-environment settings (18 models across seven environments), with mean relative improvement reported as 88.5%. Figure 5 contains some negative and zero deltas. Tests cover airline, retail, telecom, ALFWorld, WebShop, OS, and DBBench. Business-workflow tasks use three runs and report single-run success and all-three-run success; AgentBench tasks use one run. These protocols should not be pooled without retaining their metric definitions. [PDF p. 3](https://arxiv.org/pdf/2605.22166v1#page=3) [PDF p. 7](https://arxiv.org/pdf/2605.22166v1#page=7)

## Limitations

Cross-model reuse within a target environment is not transfer to an unseen environment. Deterministic action admissibility and stable tool contracts are important assumptions; performance in stochastic or changing environments remains unresolved. The four-layer design is human-specified, and the reported relative average is not an 88.5 percentage-point gain. The main text refers to Table 1, but no Table 1 caption was found in this extracted version; the aggregate is retained as an author-reported claim rather than independently reconstructed. [PDF p. 4](https://arxiv.org/pdf/2605.22166v1#page=4) [PDF p. 7](https://arxiv.org/pdf/2605.22166v1#page=7) [PDF p. 8](https://arxiv.org/pdf/2605.22166v1#page=8)

## Related Papers

[[lee-2026-meta-harness-end-to-end]]; [[zhang-2026-self-harness-harnesses-that-improve]]. Synthesis: [[concepts/evaluating-self-improvement]] and [[overviews/self-improving-llm-agents]]. Detailed provenance: [source note](../../sources/xu-2026-adapting-the-interface-not-the.md); [PDF](../../papers/xu-2026-adapting-the-interface-not-the.pdf).
