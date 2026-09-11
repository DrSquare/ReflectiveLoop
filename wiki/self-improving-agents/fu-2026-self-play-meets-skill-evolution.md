---
title: "Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember"
authors: "Fu, Zenghuang; Li, Zhaoyang; Ai, Qiuyuan; Wu, Haoyu; Wu, Minghui; Zhao, Chenxu; Wang, Ante; He, Guannan; Wang, Changwei"
year: 2026
doi: "arXiv:2607.29468"
category: ["self-improving-agents"]
pdf_path: "/papers/fu-2026-self-play-meets-skill-evolution.pdf"
pdf_filename: "fu-2026-self-play-meets-skill-evolution.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2607.29468v1"
pdf_url: "https://arxiv.org/pdf/2607.29468v1"
pdf_pages: 9
pdf_sha256: "21bc92c6619b2e688ea0ce6d961e92ecc96efd44669d771d0a5c7c2621ae196c"
full_text_reviewed_date: "2026-09-11"
---

## Summary

SESA couples search self-play to an evolving skill bank, allowing skill-conditioned learning to improve both model parameters and optional inference-time memory.

## Key Contributions

A separately parameterized challenger poses tasks while only the solver retrieves procedural memory. Difficulty-shaped rewards move the challenger toward the solver's competence boundary; informative failures produce new skills. It explicitly compares the same trained solver with and without its bank. [PDF p. 3](https://arxiv.org/pdf/2607.29468v1#page=3) [PDF p. 4](https://arxiv.org/pdf/2607.29468v1#page=4) [PDF p. 6](https://arxiv.org/pdf/2607.29468v1#page=6)

## Methodology and Architecture

Initialize memory with 15 handwritten and 142 bootstrap skills. GRPO trains challenger and solver; a bell-shaped challenger reward discourages trivial and unsolvable tasks. Consolidation deduplicates failure-derived entries, tracks helpful/hurt counts, and evicts low-utility non-seed skills under a capacity bound. The reward/editor protocol remains fixed. The advertised zero-data setting excludes target-benchmark questions but still uses 50,000 answer/hop seeds, initial skills, retrieval, and a distillation model. [PDF p. 3](https://arxiv.org/pdf/2607.29468v1#page=3) [PDF p. 4](https://arxiv.org/pdf/2607.29468v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2607.29468v1#page=5)

## Results

On 3,125 held-out questions across seven QA datasets, Qwen3-4B averages 56.2% versus SSP 53.9%. Disabling its final bank gives 55.7%: +1.8 points persist without retrieval, and retrieval adds 0.5. For Qwen3-8B, the corresponding scores are 59.5%, 56.3%, and 58.5%. A unified inference evaluation gives SESA 51.0% versus SkillRL 50.1% on Qwen2.5-7B, but does not equalize their training histories. [PDF p. 5](https://arxiv.org/pdf/2607.29468v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2607.29468v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2607.29468v1#page=7)

## Limitations

The headline metric includes a semantic judge fallback after normalized exact match, not pure exact match. Co-retrieved skills share outcome credit, which is not causal attribution. No confidence intervals appear in the main result tables. Some datasets worsen with retrieval, and memory priming/teacher cost must be counted. This is coupled curriculum-memory-policy evolution, not self-editing of the evolution procedure. [PDF p. 3](https://arxiv.org/pdf/2607.29468v1#page=3) [PDF p. 4](https://arxiv.org/pdf/2607.29468v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2607.29468v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2607.29468v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2607.29468v1#page=7)

## Related Papers

[[yang-2026-skillforge-evolving-verifiable-skills-for]]; [[feng-2026-coskill-joint-reinforcement]]. Synthesis: [[concepts/procedural-self-improvement]] and [[overviews/self-improving-llm-agents]]. Detailed provenance: [source note](../../sources/fu-2026-self-play-meets-skill-evolution.md); [PDF](../../papers/fu-2026-self-play-meets-skill-evolution.pdf).
