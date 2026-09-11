---
title: "HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses"
authors: "Luan Zhang; Ruochen Zhou; Dandan Song; Zhengyu Chen; Yuhang Tian; Jun Yang; Huipeng Ma; Chenhao Li; Guangyuan Feng; Xudong Li; Yizhou Jin; Yan Xu"
year: 2026
doi: "arXiv:2608.01918"
category: ["self-improving-agents"]
pdf_path: "/papers/zhang-2026-harnesscompass-guiding-automatic-harness-evolution.pdf"
pdf_filename: "zhang-2026-harnesscompass-guiding-automatic-harness-evolution.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2608.01918v1"
pdf_url: "https://arxiv.org/pdf/2608.01918v1"
pdf_pages: 17
pdf_sha256: "dd27f4d3d8846ac0e2dba8b6f4fabe6b177e334a072f8ec45a9c431dc04b4395"
---

## Summary

HarnessCompass constrains harness edits to task-agnostic changes, grounds agents' self-reports in execution traces, and separately optimizes structural and guidance components before merging them.

## Key Contributions

Makes anti-overfitting constraints and component interference explicit in automatic harness search. Its independent 450-task evaluation and frozen-harness cross-model test provide useful controls for the wiki's transfer experiments. The constraints and merge procedure remain designed rules, not a learned self-editing evaluator. [PDF pp. 3-6](https://arxiv.org/pdf/2608.01918v1#page=3)

## Methodology and Architecture

The frozen GPT-5.4 model fills task-agent, analyzer, feedback, and meta-agent roles in non-thinking mode. A minimal shell-only seed is evolved on 50 randomly selected SWE-bench Verified tasks; 450 tasks are reserved for evaluation. Global constraints forbid hardcoded task identifiers and instance-specific shortcuts. Blind and verdict-aware first-person feedback is reconciled against traces, so self-reports are candidate evidence rather than privileged truth. [PDF pp. 3-5](https://arxiv.org/pdf/2608.01918v1#page=3)

Two tracks modify structural components (tools, middleware, subagents) and guidance (prompts, descriptions, skills, memory). Both are evaluated on search tasks. R3 revision/recombination/refinement starts from the stronger track, retains useful nonconflicting edits, and removes redundancy. The resulting GPT-5.4 harness is frozen for Claude-Sonnet-4.6 evaluation, without further evolution. Appendix per-repository results specify two rollouts per task. [PDF pp. 5-6](https://arxiv.org/pdf/2608.01918v1#page=5) [Appendix, PDF p. 14](https://arxiv.org/pdf/2608.01918v1#page=14)

## Results

Table 1: seed versus HarnessCompass is 54.0% versus 66.0% on the 50 search tasks, 51.6% versus 60.4% on 450 held-out tasks, and 51.8% versus 61.0% overall. AHE reaches 54.7% held-out and 55.5% overall. Reported turns to the selected harness are 5 versus AHE's 20; turns are not a complete compute budget. [PDF p. 5](https://arxiv.org/pdf/2608.01918v1#page=5)

The cumulative ablation is nonmonotonic on held-out tasks: generalization gate 58.4%, adding proactive feedback 55.8%, adding R3 60.4%. With Claude-Sonnet-4.6, frozen-harness held-out performance is 73.6% versus 70.2% for its seed, and overall 73.8% versus 70.0%. [PDF p. 6](https://arxiv.org/pdf/2608.01918v1#page=6)

## Limitations

The 54-to-66 headline is search-set performance, not the held-out gain. Random task holdout within SWE-bench and transfer to one other model do not establish cross-domain or repository-disjoint transfer. The progressive ablation changes both components and number of search turns; it is not a factorial, equal-compute isolation of each component. Confidence intervals and independent-search variability are not provided in the main tables. [PDF pp. 5-7](https://arxiv.org/pdf/2608.01918v1#page=5)

Algorithm 1 selects/promotes using the winning track score, then assigns the merged harness; it does not show a separate post-merge score gate. That implementation detail should be checked before using it as a regression-safe merge recipe. Task-agnostic prompts constrain intent but do not formally guarantee absence of leakage or generalization. More feedback can hurt, as the held-out ablation shows. [PDF pp. 3-6](https://arxiv.org/pdf/2608.01918v1#page=3)

## Related Papers

[[zhang-2026-self-harness-harnesses-that-improve]]; [[xu-2026-adapting-the-interface-not-the]]; [[park-2026-autosaddler-automatic-harness-optimization-with]]. Synthesis: [[concepts/procedural-self-improvement]] and [[concepts/evaluating-self-improvement]]. Detailed provenance: [source note](../../sources/zhang-2026-harnesscompass-guiding-automatic-harness-evolution.md); [PDF](../../papers/zhang-2026-harnesscompass-guiding-automatic-harness-evolution.pdf).
