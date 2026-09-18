---
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
authors: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
year: 2026
doi: arXiv:2603.28052
source: lee-2026-meta-harness-end-to-end.md
category: [self-improving-agents]
pdf_path: /papers/lee-2026-meta-harness-end-to-end.pdf
pdf_filename: lee-2026-meta-harness-end-to-end.pdf
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: 2026-09-08
tags: [harness, scaffold-optimization, agentic-search]
arxiv_version: 2603.28052v1
pdf_url: https://arxiv.org/pdf/2603.28052v1
pdf_pages: 26
pdf_sha256: 7d9b90f53a9f4801a090f1a4acb843340cde81e4f865f97d53fff2a6a570eb73
full_text_reviewed_date: 2026-09-08
---

## Summary

Meta-Harness optimizes executable task harnesses around frozen LLMs. Its proposer selectively inspects prior source, scores, and traces stored on disk; it does not read the entire history in one prompt. This improves classification and math retrieval, while its coding result is benchmark-specific search. [§§3-4, pp. 4-9](https://arxiv.org/pdf/2603.28052v1#page=4)

## Key Contributions

- Searches whole harness programs with a coding-agent proposer, including retrieval, context construction, and orchestration.
- Raw-trace access improves classification search over scores-only and summary-feedback interfaces; it is an empirical result in this setup, not a general prohibition on compression. [Table 3, p. 7](https://arxiv.org/pdf/2603.28052v1#page=7)
- Provides held-out dataset/problem and additional-model evaluations. [Tables 5-6, p. 8](https://arxiv.org/pdf/2603.28052v1#page=8)

## Methodology and Architecture

Claude Code/Opus 4.6 proposes single-file Python harnesses, which are validated, evaluated, and added to a filesystem history. Search retains a population/Pareto frontier without a prescribed parent-selection rule. The task-model weights and proposer setup are not trained or self-rewritten. [§3, pp. 4-5](https://arxiv.org/pdf/2603.28052v1#page=4)

Discovered programs include label-aware TF-IDF classification, subject-routed BM25 math retrieval, and a pre-run environment snapshot added to Terminus-KIRA. The cited 10M tokens measure available diagnostic output; the audit reports a median 82 files read per iteration. [Appendices A-B, pp. 15-22](https://arxiv.org/pdf/2603.28052v1#page=15)

## Results

| Setting | Full-text result |
|---|---|
| Three classification datasets | Mean test accuracy 48.6% vs ACE 40.9%; additional context 11.4K vs 50.8K tokens. [Table 2, p. 6](https://arxiv.org/pdf/2603.28052v1#page=6) |
| Nine unseen classification datasets | 73.1% vs ACE 70.2%. [Table 5, p. 8](https://arxiv.org/pdf/2603.28052v1#page=8) |
| 200 unseen math problems | Mean 38.8% vs no-retrieval 34.1%; dense k=5 38.1%, BM25 37.5%. Five evaluated models include GPT-OSS-20B used in search and four unseen models. [§4.2/Table 6, p. 8](https://arxiv.org/pdf/2603.28052v1#page=8) |
| TerminalBench-2 | Opus 76.4% vs KIRA 74.7% (below reported ForgeCode 81.8%); Haiku 37.6% vs Goose 35.5%. [Table 7, p. 9](https://arxiv.org/pdf/2603.28052v1#page=9) |

**Limits:** TerminalBench search and evaluation share all 89 tasks, so the result is not untouched-test generalization. The introductory 6x harness gap is background from cited work. Context savings concern downstream prompts, not total optimization cost. [pp. 1, 6-9](https://arxiv.org/pdf/2603.28052v1#page=9)

## Related Papers

- [[overviews/self-improving-llm-agents]] places the result alongside the other seed papers and later harness-optimization scans.
- [[hebbar-2026-sia-self-improving-ai]] adds task-model training, but differs in LawBench setup; the studies are not a matched experiment.
- [[zhang-2026-hyperagents]] makes meta-agent code editable, a distinct mechanism.
- [[park-2026-autosaddler-automatic-harness-optimization-with]] optimizes the same harness axis with development-time mini-batch diagnosis, re-execution, validation-gated patches, and history-aware recombination rather than same-benchmark online search.
- [Detailed source analysis](../../sources/lee-2026-meta-harness-end-to-end.md); [canonical PDF](../../papers/lee-2026-meta-harness-end-to-end.pdf).
