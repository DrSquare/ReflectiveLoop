---
title: "Hyperagents"
authors: Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina
year: 2026
doi: arXiv:2603.19461
source: zhang-2026-hyperagents.md
category: [self-improving-agents]
pdf_path: /papers/zhang-2026-hyperagents.pdf
pdf_filename: zhang-2026-hyperagents.pdf
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: 2026-09-08
tags: [self-referential-agents, darwin-godel-machine, recursive-self-improvement]
arxiv_version: 2603.19461v1
pdf_url: https://arxiv.org/pdf/2603.19461v1
pdf_pages: 60
pdf_sha256: 92f9a73b43699c08c6000f7d4f1b68bec9fd872d217467fe4a1127e2f7981f1e
full_text_reviewed_date: 2026-09-08
---

## Summary

Hyperagents combine editable task-agent and meta-agent code inside an evolutionary archive. DGM-H improves agent-generation capability beyond coding, but its main experiments keep the foundation models, parent selection, and evaluation rules fixed. [§3, pp. 4-5; §7, p. 14](https://arxiv.org/pdf/2603.19461v1#page=4)

## Key Contributions

- Makes the mechanism that proposes future agents editable, alongside task-solving code.
- Tests the contributions of evolving meta-agents and archive-based exploration.
- Evaluates transferred meta-agents through a bounded improvement@50 experiment. [§§4.1, 5.2, pp. 6, 9-11](https://arxiv.org/pdf/2603.19461v1#page=9)

## Methodology and Architecture

A selected parent modifies task and/or meta code; the resulting task agent is evaluated and the candidate enters the archive. Selection uses validation scores where available and training scores otherwise. Models are frozen and can differ by task and role. Robotics additionally trains a downstream robot policy using the generated reward function. [§§3-4, pp. 5-7](https://arxiv.org/pdf/2603.19461v1#page=5); [Table 3, p. 35](https://arxiv.org/pdf/2603.19461v1#page=35)

The transfer experiment moves **both task and meta implementations** from joint paper-review/robotics runs to IMO-level grading. It then freezes the transferred meta-agent and lets it generate task-agent variants for 50 iterations; validation selects the best for test evaluation. This tests adaptation efficiency, not zero-shot accuracy or transfer among every domain pair. [§5.2, pp. 9-11](https://arxiv.org/pdf/2603.19461v1#page=9)

## Results

- Polyglot full-benchmark performance rises 0.084 to 0.267 (95% CI 0.231-0.280); the full benchmark includes training tasks. Original DGM is reported at 0.307, so the finding is comparable improvement, not dominance. [pp. 7-8](https://arxiv.org/pdf/2603.19461v1#page=7)
- Joint search produces paper-review test accuracy 0.710 and robotics score 0.372. Improvements over customized DGM are not statistically significant. Initial review scores of zero include missing output parsing. [pp. 8-9](https://arxiv.org/pdf/2603.19461v1#page=8)
- Transferred DGM-H achieves imp@50 of 0.630 (CI 0.540-0.630), versus 0.0 for the initial meta-agent; the paper reports p<0.05. [pp. 10-11](https://arxiv.org/pdf/2603.19461v1#page=10)
- After 200 iterations, transfer initialization gives 0.640 vs 0.610 without transfer, **p>0.05**. This suggests reusable improvements but does not establish compounding superiority. The best evolved ProofAutoGrader artifact separately improves full-benchmark accuracy 0.561 to 0.601. [pp. 12-13](https://arxiv.org/pdf/2603.19461v1#page=12)

Main results use five runs with median/95% bootstrap intervals. Persistent memory and tracking are qualitative mechanisms, not separately isolated causes. Editable parent selection is only a preliminary appendix experiment and does not significantly beat the handcrafted rule. [§5, p. 7](https://arxiv.org/pdf/2603.19461v1#page=7); [Appendix E.5, p. 57](https://arxiv.org/pdf/2603.19461v1#page=57)

## Related Papers

- [[overviews/self-improving-llm-agents]] distinguishes editable programs from weight learning.
- [[lee-2026-meta-harness-end-to-end]] searches task harnesses; [[hebbar-2026-sia-self-improving-ai]] trains task-model weights.
- [[feng-2026-coskill-joint-reinforcement]] learns a skill-editing policy within a fixed protocol; the combination remains open in [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].
- [Detailed source analysis](../../sources/zhang-2026-hyperagents.md); [canonical PDF](../../papers/zhang-2026-hyperagents.pdf).
