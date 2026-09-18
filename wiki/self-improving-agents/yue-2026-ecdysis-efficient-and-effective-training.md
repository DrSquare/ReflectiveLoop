---
title: "Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents"
authors: "Ruiqing Yue; Yu Cui; Zhuoyu Sun; Sicheng Pan; Xianhong Xue; Tingyu Li; Ting Li; Wenzhuo Zhu; Yi Chen; Yifei Liu; Baohan Huang; Zhe Cui; Haibin Zhang; Cong Zuo"
year: 2026
doi: "arXiv:2609.11677"
category: ["self-improving-agents"]
pdf_path: "/papers/yue-2026-ecdysis-efficient-and-effective-training.pdf"
pdf_filename: "yue-2026-ecdysis-efficient-and-effective-training.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-12"
arxiv_version: "2609.11677v1"
pdf_url: "https://arxiv.org/pdf/2609.11677v1"
pdf_pages: 19
pdf_sha256: "1cf10e040ab33542852e4979a415c159ad1afad4c8a1fc949ce88ad29bffcfb8"
---

## Summary

Ecdysis evolves a runtime harness by grouping failures across tasks and refining a repair specification before invoking a coding agent. It shows benefits from aggregation and additional diagnostic roles under a common initialization and training gate. Cross-task recurrence is a useful heuristic, not causal identification of a harness defect.

## Key Contributions

One implementation call per nonempty evolution round replaces repeated per-failure coding calls. Failure-Driven Collaborative Refinement (FDCR) separates diagnosis from implementation: Analyst, Critic, and Engineer roles discuss failure evidence before a Moderator proposes bounded changes. Singleton failures remain auxiliary evidence; recurrence is prioritized, not an absolute eligibility rule. [§§3.1–3.4, PDF pp. 3–6](https://arxiv.org/pdf/2609.11677v1#page=3)

## Methodology and Architecture

The evolving methods begin from the same human-augmented Life-Harness, keep task-model weights fixed, and use Qwen3-8B for at most three candidate rounds. Full FDCR runs two sequential diagnostic passes; roles and OpenCode's coding model use DeepSeek-V4-Pro. Fresh training executions accept a candidate only if total training score strictly improves. Individual-task regressions remain possible. The final harness is frozen before held-out evaluation. [Algorithm 1 and §4.1, PDF pp. 4, 6–7](https://arxiv.org/pdf/2609.11677v1#page=4)

Each τ²-Airline/Retail subset contributes 20 training and 20 test tasks, with three reset trials per test task. Frozen Qwen3-8B-evolved harnesses are evaluated with five task models: Qwen3-8B/14B/32B, MiniMax-M2.7, and Llama-3.1-8B. The transfer is between models within evaluated environments. Supplementary AgentBench results have less complete task/split documentation. [PDF pp. 6–7, 18–19](https://arxiv.org/pdf/2609.11677v1#page=6)

## Results

- Across ten model/τ²-domain cells, mean accuracy is **46.67%** for serial evolution, **54.67%** for aggregation alone, and **59.33%** with FDCR; the human-augmented baseline is 51.67%. Full FDCR's Pass@3/Pass^3 are 71.50%/45.00%, meaning success in any/all of three trials. [Table 1, PDF p. 7](https://arxiv.org/pdf/2609.11677v1#page=7)
- The **18.56% relative** headline uses three datasets including AgentBench: **58.67% → 69.56%**, or **10.89 percentage points**. On Airline, transferred Qwen3-32B improves 51.67% → 68.33% versus serial evolution. FDCR does not improve every metric/cell: MiniMax Retail accuracy is 96.67%, below aggregation-only's 100%. [§6.1, Tables 2 and 7, PDF pp. 8–9, 18](https://arxiv.org/pdf/2609.11677v1#page=8)
- Full FDCR's training speedups over serial evolution are **1.30× Retail / 1.84× Airline**; aggregation alone is faster at 1.42× / 3.23×. AgentBench full FDCR reaches only 1.03×. This measures actual wall-clock runs, including differing coding calls and service behavior. [Tables 6 and 12, PDF pp. 12, 19](https://arxiv.org/pdf/2609.11677v1#page=12)
- Across the ten τ² cells, reported average token consumption falls 12.19% versus serial evolution, but individual cells can cost more or run slower. FDCR trades extra diagnosis cost for higher aggregate accuracy. [§6.2 and Tables 3–5, PDF pp. 8, 10–11](https://arxiv.org/pdf/2609.11677v1#page=8)
- Five selected failures in one Retail transfer experiment yield **71.67%** accuracy versus **75.00%** using all 20 tasks; Pass^3 drops **60% → 45%**, while reported training cost drops **$5.763 → $0.291**. Five random failures give 65.00%. “Comparable” is not established equivalence across metrics. [Table 13, PDF p. 19](https://arxiv.org/pdf/2609.11677v1#page=19)

## Limitations

The manual model-accommodation ratio falls from 60.0% to 45.5%, but lacks reported annotator agreement and a fully specified labeling protocol. Recurring failures can reflect shared model weaknesses, and the update decomposition is conceptual. Small task samples, one evolution model and coding-model family, and absence of independent replicated searches constrain generalization and uncertainty claims. Three task trials do not replicate the optimizer. [PDF pp. 3, 6–7, 13](https://arxiv.org/pdf/2609.11677v1#page=3)

The [official code](https://github.com/cuiyu-ai/Ecdysis) is verified, but public release excludes run configurations, raw data, and traces. Its README uses MAD terminology, different dispersion values, and “held-out” wording for staged evaluation; the PDF specifies training-only acceptance. The PDF also differs between task-only and task-plus-simulator token definitions, and its AgentBench immediate post-evolution results differ from the frozen matrix. Preserve these distinctions; see the source note for exact values and provenance. [PDF pp. 6–8, 18–19](https://arxiv.org/pdf/2609.11677v1#page=6); [inspected README](https://github.com/cuiyu-ai/Ecdysis/blob/ba21638addc1e3c94972822646ea4990c87d4768/README.md)

## Related Papers

[[xu-2026-adapting-the-interface-not-the]] supplies Life-Harness; [[park-2026-autosaddler-automatic-harness-optimization-with]] and [[zhang-2026-harnesscompass-guiding-automatic-harness-evolution]] provide complementary edit/selection procedures. [[zhang-2026-self-harness-harnesses-that-improve]] motivates distinguishing selection from final tests. [[li-2026-auto-recsys-harnessing-autonomous-research]] provides long-running playbook evolution with an explicitly absent validation gate.

Synthesis: [[concepts/procedural-self-improvement]], [[concepts/evaluating-self-improvement]], and [[overviews/self-improving-llm-agents]]. Detailed provenance and reporting qualifications: [source note](../../sources/yue-2026-ecdysis-efficient-and-effective-training.md); [exact PDF](../../papers/yue-2026-ecdysis-efficient-and-effective-training.pdf).
