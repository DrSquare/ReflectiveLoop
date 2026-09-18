---
title: "SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents"
authors: "Yang, Shidong; Ma, Ziyu; Huang, Tongwen; Wang, Xucong; Li, Renda; Hu, Yiming; Wang, Yong; Chu, Xiangxiang"
year: 2026
doi: "arXiv:2608.24747"
category: ["self-improving-agents"]
pdf_path: "/papers/yang-2026-skillforge-evolving-verifiable-skills-for.pdf"
pdf_filename: "yang-2026-skillforge-evolving-verifiable-skills-for.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2608.24747v1"
pdf_url: "https://arxiv.org/pdf/2608.24747v1"
pdf_pages: 22
pdf_sha256: "66d2e4d6baff6d377d2918e470cfa846a2f1585e18249cd8fe0215e7273752a6"
full_text_reviewed_date: "2026-09-11"
---

## One-line Summary

SkillForge makes skill invocation explicit in agent trajectories and revises skills using usage outcomes while training the policy with GRPO.

## 1. Document Information

SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents. 2608.24747v1; first submitted 2026/08/25. The exact [local PDF](../papers/yang-2026-skillforge-evolving-verifiable-skills-for.pdf) has 22 pages. Citations use 1-based PDF pages. Review covers the main method, cited experiments and limitations; no reproduction was run. No unambiguous official implementation URL was verified in the reviewed PDF text; none is inferred from a project name.

## 2. Key Contributions

Injects a compact skill catalog and reveals full content only after an explicit skill-call tag. This lets RL optimize invocation tokens and makes usage observable. Induction can extract success patterns, refine failures, or compare successes with failures, followed by lexical and semantic deduplication. [PDF p. 3](https://arxiv.org/pdf/2608.24747v1#page=3) [PDF p. 4](https://arxiv.org/pdf/2608.24747v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2608.24747v1#page=5)

## 3. Methodology and Architecture

Track each called skill with an exponential-moving-average success estimate and usage count. The underperformance score increases for frequently used, unsuccessful skills; a teacher reviews their contexts and keeps or revises the definition. The bank updates every five training steps in the reported setup. Qwen3-Max acts as the teacher, while Qwen instruction models receive GRPO updates. Invocation observability does not identify each skill's causal contribution. [PDF p. 4](https://arxiv.org/pdf/2608.24747v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2608.24747v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2608.24747v1#page=6)

## 4. Key Results and Benchmarks

Under Qwen2.5-7B, Table 1 reports ALFWorld 93.6% versus SkillRL 89.9%, WebShop success 83.0% versus 72.7%, and AppWorld TGC 23.8% versus 19.0%. With Qwen3-4B, removing explicit calls reduces ALFWorld from 87.9% to 77.9% and AppWorld TGC from 44.6% to 33.3%. Table 3 transfers a 4B skill bank to a 30B model without additional training; it is a separate setting from Table 1. [PDF p. 5](https://arxiv.org/pdf/2608.24747v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2608.24747v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2608.24747v1#page=7)

## 5. Limitations and Future Work

Verification is statistical tracking plus teacher review, not formal proof or a randomized test of skill utility. Successful episodes can credit skills that were incidental, and difficult tasks can penalize useful ones. The teacher and update rules are fixed, so this is not a learned editor like CoSkill. Teacher dependence and long-run retrieval growth remain limitations; reported table comparisons do not establish superiority under a common total training budget. [PDF p. 5](https://arxiv.org/pdf/2608.24747v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2608.24747v1#page=6) [PDF p. 9](https://arxiv.org/pdf/2608.24747v1#page=9)

## 6. Related Work

[[feng-2026-coskill-joint-reinforcement]]; [[fu-2026-self-play-meets-skill-evolution]]. Synthesis: [[concepts/procedural-self-improvement]] and [[overviews/self-improving-llm-agents]].

## 7. Glossary

Explicit skill call: a traceable request for a catalog entry. TGC/SGC: task/scenario goal completion. Underperformance score: heuristic priority for revising often-used unsuccessful skills.
