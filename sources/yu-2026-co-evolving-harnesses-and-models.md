---
title: "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails"
authors: "Zhou Yu; Bin Bi; Shiva Kumar Pentyala; Shubham Mehrotra; Sougata Chaudhuri; Shilpa Bhagavath; Zeyuan Chen; Ran Xu; Phil Mui; James Zhu; Sitaram Asur"
year: 2026
doi: "arXiv:2609.09134"
category: ["self-improving-agents"]
pdf_path: "/papers/yu-2026-co-evolving-harnesses-and-models.pdf"
pdf_filename: "yu-2026-co-evolving-harnesses-and-models.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-21"
arxiv_version: "2609.09134v1"
pdf_url: "https://arxiv.org/pdf/2609.09134v1"
pdf_pages: 10
pdf_sha256: "ae8b8973f7964fca32b192fe3166ac66edb1afb78ad2b5212ec33b892a25cc34"
---

## One-line Summary

After task-specific harness evolution, full-trajectory expert imitation regresses a small agent; targeted expert corrections at student-visited states avoid most of that damage, illustrating that harness and weight improvements need not compose automatically.

## 1. Document Information

Salesforce AI preprint, September 8, 2026, pinned to arXiv:2609.09134v1. The exact [10-page PDF](../papers/yu-2026-co-evolving-harnesses-and-models.pdf) was retrieved again September 21 and matches the September 14 recovery hash and Git blob. All pages were read using Poppler layout extraction; Table 1, Table 2 and the Gemma replication on PDF p. 5 were visually checked. A font-type warning did not prevent extraction or rendering. No experiments were reproduced. No official implementation URL was verified from the PDF or its primary arXiv record; references to other projects are not this paper's code release.

## 2. Key Contributions

The central contribution is an interference result, not a demonstration of unlimited recursive improvement. A harness evolved around a weaker model remains useful to a stronger model, yet copying that stronger model's trajectories can harm the weaker model's performance under the same harness. The proposed remedy changes the supervision distribution: retain student rollouts and replace a localized failing turn instead of adopting complete teacher plans. The authors interpret this as preserving model-harness planning fit. [Introduction and §§3.2-3.4, PDF pp. 2-7](https://arxiv.org/pdf/2609.09134v1#page=4)

## 3. Methodology and Architecture

**Harness stage.** A Gemini-3.1-Pro-preview meta-agent performs GEPA-style, failure-driven search over prompts, tools, hooks, context management and subagent configuration. Validation improvement selects edits. The student is Qwen3-Coder-30B-A3B-Instruct. Seven enterprise tasks cover payroll, budget approval, stock alerting, anomaly detection, browser automation, website management and code refactoring. Direct database modification is disallowed where MCP tools are required, and tool errors are exposed to the optimizer; these environment changes limit comparison with the antecedent benchmark. Training/validation guide optimization; final test tasks are held out. [§3.1, PDF p. 4; Appendix A, p. 9](https://arxiv.org/pdf/2609.09134v1#page=4)

**Imitation stage.** Successful Gemini trajectories and student successes are converted into the student's chat/tool format for LoRA SFT. The baseline-harness comparison tests whether this recipe is intrinsically harmful. A second student family, Gemma-4-26B-A4B, is tested on WebArena, not all seven tasks. [§§3.3-3.3.2, PDF pp. 4-5](https://arxiv.org/pdf/2609.09134v1#page=5)

**Correction stage.** A meta-level MLE agent localizes a failing turn in a student's own trajectory. The expert sees the task, student prefix and failed checkpoint, and proposes a corrected strategy sentence and tool call. Three candidates are sampled and a quality judge selects one. Surrounding turns are retained. Appendix B describes about 500 training rows, including about 400 corrected rows and about 50 self-success rows; these approximate counts do not completely specify the mixture. This is on-policy data collection followed by supervised fine-tuning, not an RL policy-gradient algorithm. [§3.4, PDF pp. 6-7; Appendix B, pp. 9-10](https://arxiv.org/pdf/2609.09134v1#page=10)

LoRA uses rank 16 or 64 with best scores reported, two epochs, learning rate 1e-4, effective batch eight, and 49,152-token sequences (98,304 if truncation exceeds 5%). Training uses H100/H200 resources; merged checkpoints are served on two H200s. The claimed under-one-hour training run does not account for complete harness search, teacher collection, correction judging and evaluation cost. [Appendix B, PDF p. 9](https://arxiv.org/pdf/2609.09134v1#page=9)

## 4. Key Results and Benchmarks

Table 1 reports test success percentages, task means and SEM over three runs. The headline imitation condition is described as three LoRA seeds (0, 101, 202); do not assume every error bar measures independent harness searches. [Table 1, PDF p. 5; Appendix B, p. 9](https://arxiv.org/pdf/2609.09134v1#page=5)

| Qwen condition | Mean test success | Difference from evolved base |
|---|---:|---:|
| Base model, base harness | 29.2% | -48.8 pp |
| Base model, evolved harness | 78.0% | reference |
| Expert imitation, evolved harness | 63.1% | -14.9 pp |
| Expert imitation, base harness | 35.5% | different harness; +6.3 pp over base/base |
| Localized correction, evolved harness | 79.7% | +1.7 pp |

Imitation decreases all seven Qwen task scores; correction increases five and decreases payroll by 0.4 points and budget by 0.6. Thus the prose claim that correction matches or beats every task is not literal monotonicity. The small aggregate improvement is not accompanied by a reported paired significance test. Gemini's mean improves from 84.4% to 93.6% when moved to the Qwen-evolved harness, but payroll and budget decline relative to Gemini's own baseline; upward transfer is not uniform taskwise. [Table 1 and §3.4, PDF pp. 5-7](https://arxiv.org/pdf/2609.09134v1#page=5)

Gemma's WebArena success is 46.7% with its base harness, 55.6% after harness evolution and 41.1% after expert imitation. This corroborates one interference case in another family, not seven-task replication or cross-domain editor transfer. [§3.3.2, PDF p. 5](https://arxiv.org/pdf/2609.09134v1#page=5)

Table 2 shows domain-computation recipe use rising from 30.8% to 76.1% after imitation, but several other component-use rates fall. Increased use of one recipe is not uniform increased harness use. In Table 3, planning defects rise from 1.1% to 14.6% of failed rollouts after imitation and are 1.8% after correction. These are failure-conditioned proportions, not absolute failure rates. Labels are LLM-judge diagnoses; case studies support but do not causally identify planning-style drift. [Tables 2-3, PDF pp. 5-6; Appendices C-D, p. 10](https://arxiv.org/pdf/2609.09134v1#page=6)

## 5. Limitations and Future Work

- Sequential harness evolution then SFT is evaluated; Figure 1's repeated co-evolution loop is a proposed use of the recipe, not a reported long multi-round learning curve. Joint optimization and RL remain future work. [PDF pp. 3, 7](https://arxiv.org/pdf/2609.09134v1#page=7)
- The planning-fit explanation is plausible, but failure-conditioned judge labels and selected examples do not isolate it from data mixture, supervision locality or training choices. No matched random-turn correction control is reported.
- Section 3.4's overall failure rates of 28.9% and 26.8% are not complements of Table 1's 78.0% and 79.7% task means. Their weighting or population is not reconciled; do not combine these denominators. [PDF p. 7](https://arxiv.org/pdf/2609.09134v1#page=7)
- Appendix B reports best rank scores without a fully explicit rank-selection protocol; do not infer test leakage, but require clarification before treating model selection as independently reproduced.
- Domains share the enterprise task suite. Upward harness reuse is not transfer of a learned editor, a skill bank, or an improvement procedure to a disjoint domain. Fine-tuning runtime alone is not end-to-end economics.

## 6. Related Work

[[hebbar-2026-sia-self-improving-ai]] and [[gao-2026-experience-funnel-a-state-policy]] motivate combining external state/harness changes with policy updates. This paper narrows any assumption that such gains automatically add. [[xu-2026-adapting-the-interface-not-the]] and [[yue-2026-ecdysis-efficient-and-effective-training]] study harness transfer/repair around frozen models; a subsequent weight update is a separate compatibility test. [[feng-2026-coskill-joint-reinforcement]] learns reasoning and editing roles, whereas the correction pipeline here is a designed procedure.

Synthesis: [[overviews/self-improving-llm-agents]], [[concepts/procedural-self-improvement]], [[concepts/evaluating-self-improvement]], and [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].

## 7. Glossary

Model-harness fit: compatibility between scaffold assumptions and a model's planning/execution behavior. On-policy correction: expert edits at states visited by the student, used for SFT. Upward harness transfer: reuse by a stronger model. Failure-conditioned proportion: fraction within failed rollouts, not within all trials. SEM: standard error of the reported mean, with the experimental unit requiring explicit interpretation.
