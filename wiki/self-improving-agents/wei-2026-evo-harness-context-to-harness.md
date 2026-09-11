---
title: "Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents"
authors: "Wei, Tianxin; Shi, Zhan; Lin, Minhua; He, Bing; Liu, Zewen; Sang, Yisi; Bei, Yuanchen; Ning, Xuying; Zou, Jiaru; Li, Ting-Wei; Lin, Xiao; Zhao, Yanjun; Wang, Chi; Dumoulin, Benoit; Wang, Dakuo; He, Jingrui; Lu, Hanqing"
year: 2026
doi: "arXiv:2608.15071"
category: ["self-improving-agents"]
pdf_path: "/papers/wei-2026-evo-harness-context-to-harness.pdf"
pdf_filename: "wei-2026-evo-harness-context-to-harness.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2608.15071v1"
pdf_url: "https://arxiv.org/pdf/2608.15071v1"
pdf_pages: 16
pdf_sha256: "6fe9f508cd21fa8a1be9c46a4172bb3b433f5a79783ea50da948ceee9177a1b6"
full_text_reviewed_date: "2026-09-11"
---

## Summary

Evo-Harness compiles failed one-shot task executions into reusable general and task-type guidance for a frozen solver operating on a task stream.

## Key Contributions

Separates reflection on individual executions from consolidation into the active harness. Candidate memories carry a lesson, trigger, evidence, and scope hint; an evolver adds, merges, revises, or skips them. The evaluated skills are natural-language guidance rather than arbitrary executable harness rewrites. [PDF p. 3](https://arxiv.org/pdf/2608.15071v1#page=3) [PDF p. 4](https://arxiv.org/pdf/2608.15071v1#page=4) [PDF p. 9](https://arxiv.org/pdf/2608.15071v1#page=9)

## Methodology and Architecture

Before each batch, select and inject a bounded set of guidance entries. Solve tasks once, collect environment feedback, reflect on failures, and compile updated guidance for subsequent batches. General patterns and task-type procedures are maintained separately. The solver weights and overall update protocol remain fixed; the experiments vary feedback quality and solver/evolver pairing. [PDF p. 4](https://arxiv.org/pdf/2608.15071v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2608.15071v1#page=5)

## Results

With Opus 4.6, Table 1 reports TerminalBench-2 success 73.03% versus 62.92% without evolution, SWE-bench Lite 67.00% versus 63.67%, and CL-Bench 34.02% versus 29.54%. The dedicated train-split/model-transfer comparison gives 73.4% versus 68.8% without evolution, while online updating reaches 75.0%; these are different experimental settings. Table 4 shows self-generated feedback reducing CL-Bench to 27.96% and SWE-bench Lite to 61.67%. [PDF p. 6](https://arxiv.org/pdf/2608.15071v1#page=6) [PDF p. 7](https://arxiv.org/pdf/2608.15071v1#page=7) [PDF p. 8](https://arxiv.org/pdf/2608.15071v1#page=8)

## Limitations

Main task-stream results measure online adaptation, not one fixed harness on an untouched stream. Self-generated feedback can hurt, and richer feedback is not uniformly better: minimal feedback slightly exceeds standard feedback on SWE-bench Lite. A Sonnet solver degrades under both tested evolver pairings. These results narrow any claim of monotonic improvement from persistent skills. [PDF p. 7](https://arxiv.org/pdf/2608.15071v1#page=7) [PDF p. 8](https://arxiv.org/pdf/2608.15071v1#page=8)

## Related Papers

[[lee-2026-meta-harness-end-to-end]]; [[feng-2026-coskill-joint-reinforcement]]. Synthesis: [[concepts/procedural-self-improvement]] and [[overviews/self-improving-llm-agents]]. Detailed provenance: [source note](../../sources/wei-2026-evo-harness-context-to-harness.md); [PDF](../../papers/wei-2026-evo-harness-context-to-harness.pdf).
