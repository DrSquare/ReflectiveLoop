---
title: "SkillAdam: Stable and Efficient Skill Evolution for Agents"
authors: "Li, Gaoyuan; Fan, Meihao; Liu, Yizhe; Zhang, Shaolei; Fan, Ju; Wang, Siyi; Hou, Jiaheng; Weng, Xudong; Tian, Honghan; Li, Zang"
year: 2026
doi: "arXiv:2609.08944"
category: ["self-improving-agents"]
pdf_path: "/papers/li-2026-skilladam-stable-and-efficient-skill.pdf"
pdf_filename: "li-2026-skilladam-stable-and-efficient-skill.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2609.08944v1"
pdf_url: "https://arxiv.org/pdf/2609.08944v1"
pdf_pages: 17
pdf_sha256: "f6ad2c01fe4534b05cfe54e1beea0bea65cb6754ecbc8a0ef99d6aba4af9a64a"
full_text_reviewed_date: "2026-09-11"
---

## Summary

SkillAdam uses persistent issue history and an adaptive edit budget to stabilize optimization of natural-language skill documents around frozen models.

## Key Contributions

Carries optimizer state across textual revisions: an issue tracker remembers problems and attempted fixes, while a volatility estimate controls the extent of the next patch. The Adam correspondence is functional, not a claim that discrete skills have numerical gradients or Adam convergence guarantees. [PDF p. 5](https://arxiv.org/pdf/2609.08944v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2609.08944v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2609.08944v1#page=7)

## Methodology and Architecture

Run the current skill on a mini-batch, propose an edit using previous memory and edit budget, then evaluate the candidate on the same cases. A metric-specific gate accepts or rejects it. Paired case-level score changes update an exponentially weighted variance; high variation shrinks the next edit budget. Both accepted and rejected attempts update the issue tracker. These update rules and the patch generator remain fixed. [PDF p. 6](https://arxiv.org/pdf/2609.08944v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2609.08944v1#page=7)

## Results

Table 2 reports four strict wins and one tie versus SkillOpt across five short-horizon benchmarks; SearchQA is 87.5% versus 87.3%, Spreadsheet 81.1% versus 80.7%, and OfficeQA ties at 72.1%. Table 3 gives ALFWorld 89.6% versus 87.3% and DeepPlanning average 28.3% versus 21.7%. Table 5 transfers skills verbatim from GPT-5.5 to GPT-5.4-mini and averages 67.8% versus 63.1%, with SearchQA an exception. [PDF p. 10](https://arxiv.org/pdf/2609.08944v1#page=10) [PDF p. 11](https://arxiv.org/pdf/2609.08944v1#page=11)

## Limitations

The method merges train and selection partitions on six benchmarks while SkillOpt keeps its native split; test data are reserved for final evaluation. Thus optimization-data access and selection protocols differ. Short-horizon baselines are imported from SkillOpt, each test case is run once, and sub-point gains lack uncertainty intervals in the main tables. The ablation removes budget and then memory cumulatively; it cannot identify the full interaction. Transfer moves the skill document, not the optimizer. [PDF p. 9](https://arxiv.org/pdf/2609.08944v1#page=9) [PDF p. 10](https://arxiv.org/pdf/2609.08944v1#page=10) [PDF p. 11](https://arxiv.org/pdf/2609.08944v1#page=11)

## Related Papers

[[ye-2026-meta-context-engineering-via-agentic]]; [[yang-2026-skillforge-evolving-verifiable-skills-for]]; [[fu-2026-se-gos-self-evolving-graph]]. Synthesis: [[concepts/procedural-self-improvement]] and [[overviews/self-improving-llm-agents]]. Detailed provenance: [source note](../../sources/li-2026-skilladam-stable-and-efficient-skill.md); [PDF](../../papers/li-2026-skilladam-stable-and-efficient-skill.pdf).
