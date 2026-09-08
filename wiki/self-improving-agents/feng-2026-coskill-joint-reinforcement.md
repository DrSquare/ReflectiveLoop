---
title: "CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution"
authors: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu
year: 2026
doi: arXiv:2609.04865
source: feng-2026-coskill-joint-reinforcement.md
category: [self-improving-agents]
pdf_path: /papers/feng-2026-coskill-joint-reinforcement.pdf
pdf_filename: feng-2026-coskill-joint-reinforcement.pdf
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: 2026-09-08
tags: [skill-library, multi-agent-rl, hierarchical-skills]
arxiv_version: 2609.04865v1
pdf_url: https://arxiv.org/pdf/2609.04865v1
pdf_pages: 25
pdf_sha256: 054cd5f7f77995ea29bf19690904298bfe59b49ec2d066a7bf718f99c25e1bca
full_text_reviewed_date: 2026-09-08
---

## Summary

CoSkill jointly trains reasoning and Meta-Skill roles using one shared Qwen2.5-7B-Instruct actor. The editor learns local step-skill revisions from post-edit task execution, within a fixed retrieval, verification, and RL protocol. [§3, pp. 3-6](https://arxiv.org/pdf/2609.04865v1#page=3)

## Key Contributions

- Learns both skill use and skill editing through shared model parameters and role-specific objectives.
- Restricts step-skill retrieval to children of a retrieved task skill.
- Verifies staged edit sequences before promoting bundle versions. [§§3.1-3.4, pp. 3-6](https://arxiv.org/pdf/2609.04865v1#page=3)

## Methodology and Architecture

An external-LLM offline pipeline seeds 300 task bundles per environment. Online interaction retrieves one task skill and one observation-relevant child skill. After each reasoning transition, the editor proposes `INSERT`, `UPDATE`, `DELETE`, or `KEEP`; proposals wait until episode end before being applied to a private copy. [Appendices B-D, pp. 15-18](https://arxiv.org/pdf/2609.04865v1#page=15)

The task is rerun with the edited bundle. Editor reward is verification return minus the original return; reported experiments use one verification attempt. Only valid edits improving verification success qualify for top-two promotion within a task group. Reasoning and editor trajectories receive separate GiGPO advantages, then jointly update the shared actor. Neither the permitted operations nor GiGPO's update rule is self-rewritten. [§§3.3-3.4, pp. 5-6](https://arxiv.org/pdf/2609.04865v1#page=5); [Table 3, p. 20](https://arxiv.org/pdf/2609.04865v1#page=20)

## Results

- Main ALFWorld average is reported as 98.4%, +3.5 points vs RetroAgent 94.9%. WebShop score is 95.9 and success 90.6%; the +6.2 success-point comparator is D2Skill (O3), 84.4%. Most main-table baseline values are imported from prior tables. [Table 1, p. 7](https://arxiv.org/pdf/2609.04865v1#page=7)
- At step 120 in the ALFWorld ablation, full/no-editor-RL/flat-library success is 95.31/92.19/93.75%; alternating every 10/20 steps yields 78.12/81.25%. These are distinct from the 98.4% main result. Removing editor RL removes its loss, not all parameter change to an independent editor. [Table 2, p. 8; Appendix G, p. 20](https://arxiv.org/pdf/2609.04865v1#page=8)
- The reported ALFWorld training run takes about 66 hours on eight GPUs (approximately 526 GPU-hours). WebShop uses the 1K-product, non-human-goal setting. [Appendix F, p. 20](https://arxiv.org/pdf/2609.04865v1#page=20)

**Limits:** no cross-environment editor transfer is tested. One verification replay measures local bundle utility with limited noise control. Main tables lack seed-level intervals; Appendix E and Table 3 give differing validation/training configurations that are not fully mapped to the headline result. The displayed ALFWorld categories average about 98.33%, although the table reports 98.4%; preserve the reported value with this caveat. [pp. 5, 7, 19-20](https://arxiv.org/pdf/2609.04865v1#page=19)

## Related Papers

- [[overviews/self-improving-llm-agents]] contrasts learned editor weights with editable meta-agent programs.
- [[zhang-2026-hyperagents]] motivates the open combination in [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].
- [[hebbar-2026-sia-self-improving-ai]] also updates task-model weights, but leaves its selector frozen.
- [Detailed source analysis](../../sources/feng-2026-coskill-joint-reinforcement.md); [canonical PDF](../../papers/feng-2026-coskill-joint-reinforcement.pdf).
