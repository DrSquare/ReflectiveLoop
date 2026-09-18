---
title: "Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents"
authors: "Wenbo Gao; Zhaomou Song; Zhiyuan Ji; Renxi Liu; Xing Li; Xianzhi Yu; Xiaoguang Li; James Chung-wai Cheung; Weizhe Lin; Yaoyuan Wang"
year: 2026
doi: "arXiv:2609.08919"
category: ["self-improving-agents"]
pdf_path: "/papers/gao-2026-experience-funnel-a-state-policy.pdf"
pdf_filename: "gao-2026-experience-funnel-a-state-policy.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2609.08919v1"
pdf_url: "https://arxiv.org/pdf/2609.08919v1"
pdf_pages: 11
pdf_sha256: "a3b8af3a22a02b602196d779eb67a23d9b9f836070340547fed698b8335d4bac"
---

## One-line Summary

Experience Funnel alternates validated textual-state revisions with selective policy consolidation, aiming to internalize useful experience while retaining complementary external guidance.

## 1. Document Information

Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents. 2609.08919v1; submission date 2026-09-08. The unchanged [local PDF](../papers/gao-2026-experience-funnel-a-state-policy.pdf) has 11 pages. Citations are 1-based PDF pages. Review covers methods, reported results, and cited limitations, not experiment reproduction or a complete code audit. No official implementation URL was identified in the reviewed PDF or arXiv metadata; no repository is inferred from the title.

## 2. Key Contributions

Separates fast editable experience from slower parametric consolidation. Rollouts without state, with the previous state, and with the updated state identify newly useful, persistently useful, regressive, and inactive guidance. This directly sharpens the wiki's skill/policy co-evolution question, but does not show that the state editor or outer update rule itself learns. [PDF pp. 2-3](https://arxiv.org/pdf/2609.08919v1#page=2)

## 3. Methodology and Architecture

Cross-trajectory reflection proposes textual-state edits; validation accepts improvements under the current policy. Define benefit as reward with state exceeding reward without state. Newly useful (0,1) rollouts receive weight 1, persistent (1,1) rollouts weight alpha, and the other transitions weight zero. Within selected trajectories, Jensen-Shannon divergence between state-conditioned and state-free predictions weights responsive tokens. Reverse-KL distillation and state-free reward optimization train the policy; state-free validation gates checkpoint acceptance. Later rollouts drive state retention, revision, or retirement. [PDF pp. 3-4](https://arxiv.org/pdf/2609.08919v1#page=3)

The experiment uses a Qwen3.5-4B student and a fixed Qwen3.5-27B teacher on Ascend 910B3 NPUs. Training, selection validation, and reporting test roles are separated in prose. Five state rounds are described, with rounds 1 and 4 accepted. Different OPD budgets across environments prevent interpreting the cross-environment average as a matched-budget comparison. [PDF pp. 4-5](https://arxiv.org/pdf/2609.08919v1#page=4)

## 4. Key Results and Benchmarks

Table 1 reports SearchQA 62.4%, ALFWorld 67.9%, WebShop 42.4%, average 57.6%, versus its SkillRL comparator 61.9/66.4/40.2/56.2. These are the paper's own configurations, not directly comparable to numbers in other papers. Table 5 gives SearchQA state-free policy 58.1% before versus 61.3% after consolidation, 62.4% with full state, and 61.3% with residual state. Residualization therefore preserves the no-state score, not the full-state score. [PDF pp. 6-7](https://arxiv.org/pdf/2609.08919v1#page=6)

Teacher ablation: 27B without state produces 56.29%, versus 61.21% with updated state; 4B yields 59.79% without state and 57.57% with it. This suggests an interaction in this experiment, not a proven general law. The selected 01+11 subset reaches 63.0% versus 58.9% unfiltered in a separate analysis. The authors acknowledge that binary 01+11 selection reduces to updated-state success, so this alone does not identify the extra value of transition history. [PDF p. 7](https://arxiv.org/pdf/2609.08919v1#page=7)

## 5. Limitations and Future Work

Reporting needs reconciliation: Table 2's full-loop SearchQA score is 63.6%, not Table 1's 62.4%; Table 3 begins at 56.9%, not the 58.1% base used elsewhere. The text describes five state rounds, while plotted axes extend to ten. Section 3.1 says final repeated-run uncertainty is reported, but the displayed final tables provide no intervals or standard deviations. Treat the small comparator gaps cautiously. [PDF pp. 5-7](https://arxiv.org/pdf/2609.08919v1#page=5)

The mathematical teacher branch is defined using the frozen current policy, while implementation uses a separate 27B teacher; the mapping is not fully specified. Alpha, optimization budgets, split counts, and detailed training settings are insufficiently specified for a faithful reproduction. JSD measures sensitivity to conditioning, not correctness or causal skill credit. Separate experiments on three environments do not establish transfer of one learned editor/state/policy into an unseen environment. Recurring related tasks, usable outcome feedback, and extra multi-condition rollouts are assumed. [PDF pp. 3-5, 9](https://arxiv.org/pdf/2609.08919v1#page=3)

## 6. Related Work

[[feng-2026-coskill-joint-reinforcement]]; [[fu-2026-self-play-meets-skill-evolution]]; [[ye-2026-meta-context-engineering-via-agentic]]. Synthesis: [[concepts/procedural-self-improvement]] and [[concepts/evaluating-self-improvement]].

## 7. Glossary

State: editable textual experience. Consolidation: training a state-free policy from state-enabled behavior. Transition label: change in outcome benefit across two state versions. Residual state: remaining guidance after policy consolidation.
