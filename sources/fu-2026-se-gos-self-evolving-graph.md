---
title: "SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale"
authors: "Fu, Dawei; Jiang, Cheng; Qian, Sitian; Wang, Huainan; Hao, Zhongkai"
year: 2026
doi: "arXiv:2609.08228"
category: ["self-improving-agents"]
pdf_path: "/papers/fu-2026-se-gos-self-evolving-graph.pdf"
pdf_filename: "fu-2026-se-gos-self-evolving-graph.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2609.08228v1"
pdf_url: "https://arxiv.org/pdf/2609.08228v1"
pdf_pages: 21
pdf_sha256: "67d9ee46a42297abef8631d9b6ed6c05aa1f2550fadaeaf7acdc4dae602808a0"
full_text_reviewed_date: "2026-09-11"
---

## One-line Summary

SE-GoS evolves the graph and descriptions used to retrieve existing skills, while preserving skill content, model weights, and the retrieval algorithm.

## 1. Document Information

SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale. 2609.08228v1; first submitted 2026/09/08. The exact [local PDF](../papers/fu-2026-se-gos-self-evolving-graph.pdf) has 21 pages. Citations use 1-based PDF pages. Review covers the main method, cited experiments and limitations; no reproduction was run. No unambiguous official implementation URL was verified in the reviewed PDF text; none is inferred from a project name.

## 2. Key Contributions

Separates skill retrieval infrastructure from skill creation. Execution traces update graph topology, edge weights, and retrieval-facing node descriptions. The structural channel uses trace arithmetic rather than an LLM prior about relationships; description editing still uses LLMs. [PDF p. 3](https://arxiv.org/pdf/2609.08228v1#page=3) [PDF p. 5](https://arxiv.org/pdf/2609.08228v1#page=5) [PDF p. 7](https://arxiv.org/pdf/2609.08228v1#page=7)

## 3. Methodology and Architecture

Start from a token-overlap similarity graph over 1,000 skills. Successful retrieval/use patterns add workflow edges; ordered use plus input/output matching adds dependencies. Unused retrieved skills receive weaker incoming edges. A bounded text-editing loop repairs poorly retrieved descriptions. Fixed lexical seeding and personalized PageRank consume the resulting graph. Avoid-edge handling is described but not exercised in the reported results. [PDF p. 4](https://arxiv.org/pdf/2609.08228v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2609.08228v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2609.08228v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2609.08228v1#page=7)

## 4. Key Results and Benchmarks

The full 87-task SkillsBench study re-evaluates the same tasks that generated traces: reward rises from static GoS 52.4% to 59.4%, with input tokens 3.67M to 3.45M per attempt. The roughly one-third token reduction uses full-library loading (5.06M) as the comparator, not static GoS. In the disjoint 50-train/37-test experiment, reward is 58.3% versus 52.9%; the authors explicitly place the +5.4-point gap inside their noise band. Repeated full-set evolution gives 59.4%, 59.8%, then 54.0%. [PDF p. 8](https://arxiv.org/pdf/2609.08228v1#page=8) [PDF p. 9](https://arxiv.org/pdf/2609.08228v1#page=9) [PDF p. 10](https://arxiv.org/pdf/2609.08228v1#page=10)

## 5. Limitations and Future Work

The held-out point estimate is promising but not resolved statistically. The main deployment-utility result is selection/exposure-sensitive, and more rounds can degrade the graph. The compared static substrate is semantic-only, not the full LLM-validated GoS graph. Some cross-backbone baselines are quoted from prior work. Failure accounting is ambiguous: the text excludes pre-verifier harness failures yet labels cells as all 174 attempts scored; raw denominators need verification before reproduction. Co-occurrence does not establish causal dependency or harm. [PDF p. 5](https://arxiv.org/pdf/2609.08228v1#page=5) [PDF p. 8](https://arxiv.org/pdf/2609.08228v1#page=8) [PDF p. 9](https://arxiv.org/pdf/2609.08228v1#page=9) [PDF p. 10](https://arxiv.org/pdf/2609.08228v1#page=10)

## 6. Related Work

[[wei-2026-evo-harness-context-to-harness]]; [[li-2026-skilladam-stable-and-efficient-skill]]. Synthesis: [[concepts/procedural-self-improvement]] and [[overviews/self-improving-llm-agents]].

## 7. Glossary

Retrieval substrate: graph and metadata read by a fixed retriever. Hydration: loading selected skill content under a budget. Deployment utility: remeasurement on tasks that supplied adaptation traces.
