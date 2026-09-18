---
title: "Meta Context Engineering via Agentic Skill Evolution"
authors: "Ye, Haoran; He, Xuning; Arak, Vincent; Dong, Haonan; Song, Guojie"
year: 2026
doi: "arXiv:2601.21557"
category: ["self-improving-agents"]
pdf_path: "/papers/ye-2026-meta-context-engineering-via-agentic.pdf"
pdf_filename: "ye-2026-meta-context-engineering-via-agentic.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2601.21557v2"
pdf_url: "https://arxiv.org/pdf/2601.21557v2"
pdf_pages: 46
pdf_sha256: "da2d47e8ade571d41fdca14da027542e363fb16f052a0c29499f3500351f0973"
full_text_reviewed_date: "2026-09-11"
---

## Summary

MCE evolves the instructions and code that build context, then executes those skills to produce context artifacts, while keeping model weights frozen.

## Key Contributions

Separates the context-building procedure from its output. The meta-agent searches prior skills, artifacts, and scores through a filesystem; the base agent runs the selected procedure. This makes learned improvement procedures concrete prior work for ReflectiveLoop, beyond retrieving a fixed skill library. [PDF p. 5](https://arxiv.org/pdf/2601.21557v2#page=5)

## Methodology and Architecture

The outer loop proposes a skill folder by agentic crossover over the accumulated history. The inner loop uses training rollouts and that skill to construct a context function comprising files and executable operators. Validation selects the better context and preserves the history. Algorithm 1 keeps the outer orchestration and selection rule fixed; it does not recursively rewrite the whole optimizer. The experiments instantiate the output as a one-shot query-to-context interface. [PDF p. 5](https://arxiv.org/pdf/2601.21557v2#page=5) [PDF p. 6](https://arxiv.org/pdf/2601.21557v2#page=6) [PDF p. 7](https://arxiv.org/pdf/2601.21557v2#page=7)

## Results

Offline Table 1 reports FiNER accuracy 75.0% versus ACE 71.0%, USPTO50k 20.0% versus 18.0%, Symptom2Disease 89.2% versus 79.2%, LawBench micro-F1 0.70 versus 0.65, and Aegis F1 0.80 versus 0.68. These are different metrics, not a common accuracy scale. Table 2 transfers learned contexts to smaller models on three datasets; it does not test a transferred RL skill editor. [PDF p. 8](https://arxiv.org/pdf/2601.21557v2#page=8)

## Limitations

Online evaluation scores each item before learning from it; its MCE skill is fixed from the task specification. The no-skill variant exceeds the guided variant on three of five online columns, so skill guidance does not uniformly help. Cross-model context transfer is narrower than cross-domain transfer of an improvement policy. No joint RL training of reasoning and editing roles is demonstrated. [PDF p. 7](https://arxiv.org/pdf/2601.21557v2#page=7) [PDF p. 8](https://arxiv.org/pdf/2601.21557v2#page=8)

## Related Papers

[[lee-2026-meta-harness-end-to-end]]; [[feng-2026-coskill-joint-reinforcement]]; [[zhang-2026-hyperagents]]. Synthesis: [[concepts/procedural-self-improvement]] and [[overviews/self-improving-llm-agents]]. Detailed provenance: [source note](../../sources/ye-2026-meta-context-engineering-via-agentic.md); [PDF](../../papers/ye-2026-meta-context-engineering-via-agentic.pdf).
