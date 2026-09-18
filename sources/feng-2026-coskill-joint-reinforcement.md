---
title: "CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution"
authors: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu
year: 2026
doi: arXiv:2609.04865
category: [self-improving-agents]
pdf_path: /papers/feng-2026-coskill-joint-reinforcement.pdf
pdf_filename: feng-2026-coskill-joint-reinforcement.pdf
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: 2026-09-08
arxiv_version: 2609.04865v1
pdf_url: https://arxiv.org/pdf/2609.04865v1
pdf_pages: 25
pdf_sha256: 054cd5f7f77995ea29bf19690904298bfe59b49ec2d066a7bf718f99c25e1bca
full_text_reviewed_date: 2026-09-08
---

## One-line Summary

CoSkill jointly trains reasoning and skill-editing roles in one shared model, crediting staged skill edits through task re-execution before promotion; the learned component is an editing policy within a fixed retrieval, verification, and GiGPO training protocol. [§3, pp. 3-6](https://arxiv.org/pdf/2609.04865v1#page=3)

## 1. Document Information

- Feng et al., *CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution*, arXiv:2609.04865v1, September 4, 2026; 25 pages. Grounded in the exact [local PDF](../papers/feng-2026-coskill-joint-reinforcement.pdf), retrieved September 8, 2026. Citations use 1-based PDF pages.
- Training is described as built on veRL and verl-agent. This ingest verifies the paper, not execution of the implementation. [§4.1, p. 6](https://arxiv.org/pdf/2609.04865v1#page=6)

## 2. Key Contributions

- Recasts skill management as a learnable policy rather than external, frozen orchestration. Reasoning and Meta-Skill roles share Qwen2.5-7B-Instruct parameters and receive different prompts, observations, and rewards. They are not two independently parameterized models. [§§3.2, 4.1, pp. 4, 6](https://arxiv.org/pdf/2609.04865v1#page=4)
- Uses a two-level task/step hierarchy that restricts local retrieval and editing to a task-relevant subtree. [§3.1, pp. 3-4](https://arxiv.org/pdf/2609.04865v1#page=3)
- Separates proposed edits from persistent writes: task re-execution supplies delayed evidence of their value. Joint optimization then uses role-specific credit assignment. [§§3.3-3.4, pp. 5-6](https://arxiv.org/pdf/2609.04865v1#page=5)

## 3. Methodology and Architecture

Offline initialization collects eight trajectories per task group with an external LLM, distills task guidance and step procedures, and checks each step skill against a cited source trajectory/turn. Initial banks contain 300 task bundles with 1,625 ALFWorld step skills or 1,406 WebShop step skills. This initial data-generation stage is distinct from the jointly trained online actor. [Appendix B, pp. 15-16](https://arxiv.org/pdf/2609.04865v1#page=15)

At episode start, embedding retrieval chooses one task skill; each observation retrieves one child step skill. The Meta-Skill Agent observes the active skill, action, history, and environment feedback, then proposes `INSERT`, `UPDATE`, `DELETE`, or `KEEP`. The task-level guidance stays fixed during the attempt. Malformed edits map to `KEEP`. These are constrained local edits to skill text, not edits to arbitrary training code. [§§3.1-3.2, pp. 3-5](https://arxiv.org/pdf/2609.04865v1#page=3); [Appendix C, pp. 16-17](https://arxiv.org/pdf/2609.04865v1#page=16)

All proposals are staged until the baseline episode ends, then applied in order to a private bundle copy. The same task is reset and rerun with that edited copy. The editor reward is mean verification return minus baseline return, while each reasoning attempt retains its own environment return. The reported configuration uses **M=1** verification attempt. Valid, nontrivial edits whose verification success exceeds the baseline are eligible; top two bundle versions per task group can be promoted. [Eq. 13, p. 5](https://arxiv.org/pdf/2609.04865v1#page=5); [Algorithm 2, p. 18; Table 3, p. 20](https://arxiv.org/pdf/2609.04865v1#page=18)

GiGPO constructs episode- and step-level advantages separately for each role. Reasoning groups use task/state anchors; editing groups additionally condition on the active skill. The shared actor minimizes the sum of the two role objectives using clipped policy updates and KL regularization. The MSMDP is a modeling formulation, not a theorem establishing stable co-training or transfer. [Eqs. 14-15, p. 6](https://arxiv.org/pdf/2609.04865v1#page=6)

Table 3 specifies Qwen3-Embedding-0.6B, 16 task groups with eight rollouts each, learning rate 1e-6, eight GPUs on one node, and 160/200 ALFWorld/WebShop steps. It caps interactions at 30/15 actions, uses one task plus one step retrieval, and keeps 300 bundles with periodic eviction. WebShop uses the small 1K-product, non-human-goal setting. [Appendix F, p. 20](https://arxiv.org/pdf/2609.04865v1#page=20)

## 4. Key Results and Benchmarks

| Setting | Reported result | Precise comparison |
|---|---|---|
| Main ALFWorld table | 98.4% reported average success; 100% on five task categories and 90.0% on Cool | +3.5 percentage points vs RetroAgent's 94.9%; not the best Cool-category score. |
| Main WebShop table | Score 95.9; success 90.6% | Score +4.3 vs Skill1's 91.6; success +6.2 points vs D2Skill (O3)'s 84.4. These comparators differ. |
| Skill-free GiGPO | ALFWorld 90.8%; WebShop success 72.8% | CoSkill improvements of +7.6 and +17.8 points in the reported table. |

Main results and comparator provenance: [§4.2, Table 1, p. 7](https://arxiv.org/pdf/2609.04865v1#page=7). The caption says baseline values are generally drawn from prior reported tables, not all rerun under one protocol.

ALFWorld ablations at step 120 report full CoSkill **95.31%**, no editor-RL **92.19%**, flat library **93.75%**, and alternating updates every 10/20 steps **78.12%/81.25%**. Keep these checkpoint results separate from the main table's 98.4%. At step 20, full/no editor-RL scores are 70.31/57.81%. The no-editor-RL condition removes that role's objective; because weights are shared, it does not freeze a separate editor model. [Table 2, p. 8](https://arxiv.org/pdf/2609.04865v1#page=8); [Appendix G, pp. 20-21](https://arxiv.org/pdf/2609.04865v1#page=20)

Behavioral diagnostics show cumulative promotions 387 vs 739 without editor RL and fewer empty bundles; these support more selective editing in the tested environment, not universal optimality of favoring UPDATE. The authors report approximately 66 hours/526 GPU-hours for 160 ALFWorld steps; this is not a complete accounting of offline bank construction and all experiment costs. [Fig. 5, p. 9](https://arxiv.org/pdf/2609.04865v1#page=9); [Appendix F, p. 20](https://arxiv.org/pdf/2609.04865v1#page=20)

## 5. Limitations and Future Work

- **Generalization scope:** separate ALFWorld and WebShop experiments do not test transfer of one learned editor/library to the other environment. A broader transfer claim remains unsupported by these results. [§4 and Appendix F](https://arxiv.org/pdf/2609.04865v1#page=6)
- **Protocol ambiguity:** Appendix E describes D2Skill-based evaluation with 128 held-out tasks, 160 steps, frozen validation banks, and best-checkpoint reporting; Table 3 lists validation batch 64 and WebShop 200 steps. These may describe distinct configurations, but their exact mapping to Table 1 is not fully reconciled. Record both rather than inventing a single clean test protocol. [pp. 19-20](https://arxiv.org/pdf/2609.04865v1#page=19)
- **Uncertainty:** the main and ablation tables give point estimates without seed-level intervals or tests. Table 1 calls its ALFWorld aggregate a macro average, but the displayed CoSkill categories average about 98.33%, not 98.4%; retain the reported number and flag the discrepancy. [pp. 7-8](https://arxiv.org/pdf/2609.04865v1#page=7)
- **Verification limits (wiki inference):** one rerun of the same task supplies noisy, local evidence for an edit bundle; it does not isolate individual edits or establish usefulness on other tasks. Promotion after noisy comparison can select favorable rollouts. [§3.3, p. 5; Table 3, p. 20](https://arxiv.org/pdf/2609.04865v1#page=5)
- **Learned versus fixed:** role prompts, allowed operations, reward construction, promotion gate, and GiGPO objective remain designed components. No self-rewriting optimizer experiment is reported. The authors leave broader systems and more efficient credit/update mechanisms to future work. [§3](https://arxiv.org/pdf/2609.04865v1#page=3); [§5, p. 9](https://arxiv.org/pdf/2609.04865v1#page=9)

## 6. Related Work

[[zhang-2026-hyperagents]] edits meta-agent code; CoSkill optimizes the skill-editing policy's **weights** under a fixed protocol. [[hebbar-2026-sia-self-improving-ai]] also trains weights, but its Feedback-Agent selector remains frozen. CoSkill is therefore not an alternative to weight updates; it is a particular coupled weight-and-library learning design. See [[overviews/self-improving-llm-agents]] and [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].

## 7. Glossary

- **Task bundle:** task-level guidance and its linked child step skills.
- **Staged edit:** proposal withheld from the persistent library until verification.
- **Post-edit reward:** return difference after rerunning the task with the edited bundle.
- **GiGPO:** group-based policy optimization with episode- and step-level credit.
- **Shared actor:** one parameter set used under two role-specific contexts/objectives.
