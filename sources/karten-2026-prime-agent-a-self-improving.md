---
title: "Prime Agent: A Self-Improving RLM Harness"
authors: "Karten, Seth; Zhang, Alex L.; Thomas, Kevin; Müller, Sebastian; Bakouch, Elie; Auras, Daniel; Senghaas, Mika; Obeid, Fares; Dunas, Konstantin; Hagemann, Johannes; Jaghouar, Sami"
year: 2026
doi: "arXiv:2608.23552"
category: ["self-improving-agents"]
pdf_path: "/papers/karten-2026-prime-agent-a-self-improving.pdf"
pdf_filename: "karten-2026-prime-agent-a-self-improving.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2608.23552v1"
pdf_url: "https://arxiv.org/pdf/2608.23552v1"
pdf_pages: 16
pdf_sha256: "973323f2d3d85f3ec9b21709248b65ba236cf527cd5cc9ff556909104a5fd370"
full_text_reviewed_date: "2026-09-11"
---

## One-line Summary

Prime Agent packages a persistent REPL, recursive agent sessions, and versioned harness state into a runtime for long-horizon reasoning and execution.

## 1. Document Information

Prime Agent: A Self-Improving RLM Harness. 2608.23552v1; first submitted 2026/08/24. The exact [local PDF](../papers/karten-2026-prime-agent-a-self-improving.pdf) has 16 pages. Citations use 1-based PDF pages. Review covers the main method, cited experiments and limitations; no reproduction was run. [Author-linked project/code](https://github.com/PrimeIntellect-ai/prime-agent) is provided for follow-up; implementation behavior was not audited.

## 2. Key Contributions

Separates model weights, active context, retained REPL/session state, and disk-backed artifacts. Persistent sessions survive client detachment; recursive calls and direct messages coordinate work. This is a systems contribution, distinct from a learned meta-optimizer. [PDF p. 3](https://arxiv.org/pdf/2608.23552v1#page=3) [PDF p. 4](https://arxiv.org/pdf/2608.23552v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2608.23552v1#page=5)

## 3. Methodology and Architecture

An asynchronous rlm call creates a subagent with its own context, kernel, and history. Continual Harness edits versioned prompt notes, memories, executable skills, and subagent specifications at turn boundaries. A fixed base prompt remains immutable. Completion gates and resource accounting aggregate root and descendant work; the evaluated model weights stay fixed. [PDF p. 4](https://arxiv.org/pdf/2608.23552v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2608.23552v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2608.23552v1#page=6)

## 4. Key Results and Benchmarks

Table 1 shows mixed within-model outcomes: GPT-5.6 Sol reaches 0.940 versus Codex 0.900 on OOLONG, but 0.612 versus 0.646 on OBLIQ nDCG@10. Figure 5 reports 95.5% RHAE for Prime Agent with Opus 5 alongside 30.2% from an external ARC harness reference. The authors explicitly say external references situate the results rather than isolate a causal harness effect. Table 1 supplies no uncertainty intervals. [PDF p. 7](https://arxiv.org/pdf/2608.23552v1#page=7)

## 5. Limitations and Future Work

Do not interpret the roughly 30-to-95.5 headline as a matched-budget causal effect of self-improvement. Multiple runtime features and test-time compute change together, and native harnesses win some comparisons. Persistence/refinement capability alone does not demonstrate improvement in the algorithm that proposes improvements. A refinement-disabled comparison under matched cost would isolate that mechanism more directly; this is a wiki recommendation. [PDF p. 5](https://arxiv.org/pdf/2608.23552v1#page=5) [PDF p. 7](https://arxiv.org/pdf/2608.23552v1#page=7) [PDF p. 9](https://arxiv.org/pdf/2608.23552v1#page=9)

## 6. Related Work

[[lee-2026-meta-harness-end-to-end]]. Synthesis: [[concepts/evaluating-self-improvement]] and [[overviews/self-improving-llm-agents]].

## 7. Glossary

RLM: recursive language-model computation through programmatic context and calls. Persistent REPL: computation whose retained state survives turns. Refinement: versioned changes to supplemental harness state.
