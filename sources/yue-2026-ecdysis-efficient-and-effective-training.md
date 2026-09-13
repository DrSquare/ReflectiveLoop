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

## One-line Summary

Ecdysis aggregates recurring failures across tasks and uses structured multi-role diagnosis before editing a runtime harness, reducing repeated coding calls and improving frozen-harness performance in small held-out task/model evaluations.

## 1. Document Information

Public preprint, arXiv:2609.11677v1, submitted September 10, 2026; retrieved unchanged September 12. The user supplied [this LinkedIn short link](https://lnkd.in/p/gzWd3Gmj); its post and paper comment identified the canonical arXiv paper. Scientific claims below come from the [19-page PDF](../papers/yue-2026-ecdysis-efficient-and-effective-training.pdf), not the social post. All PDF pages were reviewed as extracted text; result/protocol pages 7 and 19 were visually inspected. No experiments were reproduced.

The PDF explicitly links the [official implementation](https://github.com/cuiyu-ai/Ecdysis) on p. 1. Its [README at inspected commit ba21638](https://github.com/cuiyu-ai/Ecdysis/blob/ba21638addc1e3c94972822646ea4990c87d4768/README.md) and repository tree were checked September 12. They contain implementation modules, experiment CLIs, and tests, but exclude local YAML experiment configurations, raw benchmark data, generated traces, and private artifacts. Code availability is verified; exact reproducibility is not. The release calls FDCR “MAD” and uses differing uncertainty values and review wording, detailed below.

## 2. Key Contributions

The persistent object is runtime harness code around a fixed task model. A batch of failures becomes one proposed change specification and coding-agent invocation per nonempty round, rather than one invocation per individual failure. Analyst, Critic, and Engineer roles discuss causes and repair scope before a Moderator emits the specification. Cross-task recurrence is explicitly an inductive bias for repair, not proof that a failure originates in the harness. [§§3.1–3.4, PDF pp. 3–6](https://arxiv.org/pdf/2609.11677v1#page=3)

## 3. Methodology and Architecture

**Collection and aggregation.** Under a fixed evaluator, trajectories below a score threshold become records containing task identity, termination reason, tool history, and context. Groups spanning at least two distinct tasks receive priority; singleton groups remain auxiliary evidence, and not every group requires a repair. Aggregation reduces coding calls, but role-based diagnosis and re-evaluation still consume resources. [§3.3, PDF p. 5](https://arxiv.org/pdf/2609.11677v1#page=5)

**Diagnosis before implementation.** In the full variant, Analyst, Critic, and Engineer execute sequentially through two passes, each seeing the growing transcript. The Critic checks overbroad triggers, blocked legitimate actions, runtime-contract violations, and regressions. The Moderator consolidates the evidence into a structured specification; OpenCode implements it. All four diagnostic roles and the coding agent use DeepSeek-V4-Pro. This is a designed fixed refinement procedure, not learned role weights or recursive evolution of the diagnostic algorithm. [§§3.4, 4.1, PDF pp. 5–7](https://arxiv.org/pdf/2609.11677v1#page=5)

**Selection and evaluation.** All evolving methods start from the same human-augmented Life-Harness. Qwen3-8B supplies task trajectories, with at most three candidate-generation rounds. Fresh full training evaluations accept a candidate only when its overall training score strictly improves; individual-task regressions are allowed. Fresh trajectories still use the same training tasks. A final training evaluation accepts or rejects the last candidate without another proposal, then the harness is frozen. Held-out scores do not drive evolution under the PDF protocol. [Algorithm 1 and §4.1, PDF pp. 4, 6–7](https://arxiv.org/pdf/2609.11677v1#page=4)

For each τ²-Airline/Retail subset, the study uses 20 training tasks and 20 test tasks. Each test task has three trials with environment resets, giving 60 held-out trajectories per model/subset/method. The transfer matrix reuses Qwen3-8B-evolved harnesses with Qwen3-8B/14B/32B, MiniMax-M2.7, and Llama-3.1-8B, without further evolution. Task-model temperature is 0.0. AgentBench has supplementary results, but its task composition and split protocol are less fully specified than the two τ² subsets. [§4.1 and Tables 7–12, PDF pp. 6–7, 18–19](https://arxiv.org/pdf/2609.11677v1#page=6)

## 4. Key Results and Benchmarks

Across ten model/τ²-subset cells, Table 1 reports:

| Method | Mean accuracy | Pass@3 | Pass^3 |
|---|---:|---:|---:|
| Direct | 38.17% | 53.50% | 22.50% |
| Fixed human-augmented harness | 51.67% | 66.00% | 37.00% |
| Serial Self-Evolution | 46.67% | 63.50% | 29.00% |
| Ecdysis without FDCR | 54.67% | 66.50% | 42.00% |
| Ecdysis with FDCR | 59.33% | 71.50% | 45.00% |

Pass@3 means at least one successful trial; Pass^3 means all three. Aggregation adds 8.00 percentage points over serial evolution; FDCR adds approximately 4.67 more. The full method gains 12.66 points over serial evolution, or about 27.1% relative. The **18.56% headline** instead pools five models across three datasets including AgentBench: 58.67% to 69.56%, a **10.89-point** absolute gain. These are different denominators, not conflicting headline calculations. [§§3.5, 5–6, Tables 1 and 7, PDF pp. 6–8, 18](https://arxiv.org/pdf/2609.11677v1#page=6)

On τ²-Airline, full Ecdysis versus serial evolution improves Qwen3-8B from 35.00% to 60.00% and transferred Qwen3-32B from 51.67% to 68.33%. FDCR is not uniformly better: MiniMax-M2.7 Retail averages 96.67%, below aggregation-only's 100%; Qwen3-8B Airline Pass^3 is 40% versus 45% without FDCR. [Table 2, PDF p. 9](https://arxiv.org/pdf/2609.11677v1#page=9)

Training wall time includes initial evaluation through final freezing. Retail is 1,831.4 seconds for serial evolution, 1,292.4 without FDCR, and 1,405.9 with FDCR; Airline is 8,120.6 / 2,510.8 / 4,403.0. Thus the full method's speedups are 1.30× and **1.84×**, while aggregation-only reaches 1.42× and 3.23×. AgentBench full FDCR gains only 1.03×. These are actual execution paths with different coding-call counts and API behavior, not equal-token-budget comparisons. [Tables 6 and 12, PDF pp. 12, 19](https://arxiv.org/pdf/2609.11677v1#page=12)

Reported training API totals for Retail/Airline fall from $8.484/$6.382 under serial evolution to $5.763/$2.609 with FDCR. Inference figures averaged over the ten τ² cells show 11.567M versus 10.157M tokens (12.19% reduction) and 126.08 versus 118.69 seconds per trajectory. Full FDCR uses more input tokens than serial evolution during Retail training despite lower API cost; caching and token mix matter. Inference savings are not universal across cells. These are historical study costs, not current price estimates. [Tables 3–5 and §6.2, PDF pp. 8, 10–11](https://arxiv.org/pdf/2609.11677v1#page=8)

The quarter-data experiment is one Retail transfer cell: evolve with Qwen3-8B, evaluate Qwen3-32B. Full data gives 75.00% accuracy / 60% Pass^3 / $5.763; five selected training failures give 71.67% / 45% / $0.291; five random failures give 65.00% / 45% / $0.505. Reduced-data Pass@3 is 90% versus full-data 85%. This is a quality-cost tradeoff, not equality on every metric or a demonstrated statistical equivalence. [Table 13, PDF p. 19](https://arxiv.org/pdf/2609.11677v1#page=19)

## 5. Limitations and Future Work

**Causal attribution remains unresolved.** Manual coding labels 60.0% of serial modification decisions and 45.5% of Ecdysis decisions as model accommodation. The report lacks a full coding rubric, decision counts, annotator agreement, and uncertainty. Recurrence across tasks can also arise from systematic model weaknesses. The mixture decomposition is conceptual, not an identified causal model of nonlinear code edits. No counterfactual interventions prove the cause of each repair's success. [§§3.1, 8.3, PDF pp. 3, 13](https://arxiv.org/pdf/2609.11677v1#page=3)

**Scope and replication.** Small selected task sets, one evolution task model, one coding-model family, and shared human-augmented initialization limit breadth. Three evaluation trials are not three independent harness-evolution runs. Cross-model reuse within evaluated environments does not establish transfer to new domains or tool ecosystems. The reduced-data experiment is a single model/domain cell; task-selection/search overhead and repeated selection variability are not fully accounted for. [PDF pp. 6–7, 12–13, 19](https://arxiv.org/pdf/2609.11677v1#page=6)

**Reporting boundaries.** Section 3.5 defines final tokens using the task model, while §6.2 includes the user simulator; do not silently mix these definitions. Table 7's AgentBench Qwen3-8B frozen-matrix FDCR score is 90%, versus 93.33% in the separately captioned immediate post-evolution Table 10; the corresponding split/run relationship needs clarification. Table 1 PDF dispersions (e.g. 59.33 ± 25.03) differ from the official README (59.33 ± 5.08); the common mean does not make these interchangeable uncertainty estimates. They are not confidence intervals over independent searches. [PDF pp. 6–8, 18–19](https://arxiv.org/pdf/2609.11677v1#page=6); [inspected README](https://github.com/cuiyu-ai/Ecdysis/blob/ba21638addc1e3c94972822646ea4990c87d4768/README.md)

**Implementation provenance.** The README calls the role procedure MAD and says staged edits are evaluated on held-out tasks. The paper instead specifies training-only acceptance followed by frozen held-out evaluation. This review follows the pinned PDF for reported experimental claims; the README wording alone neither establishes test leakage nor resolves the protocol. Full code-to-experiment reconciliation remains open because private run configurations and traces are excluded from the release.

## 6. Related Work

[[xu-2026-adapting-the-interface-not-the]] (Life-Harness) supplies the harness initialization and direct methodological lineage. [[park-2026-autosaddler-automatic-harness-optimization-with]] and [[zhang-2026-harnesscompass-guiding-automatic-harness-evolution]] are complementary designed procedures for trace-grounded, constrained edits; no matched comparison against their complete systems is reported here. [[zhang-2026-self-harness-harnesses-that-improve]] highlights why a selection-exposed split must be separated from final testing. [[li-2026-auto-recsys-harnessing-autonomous-research]] supplies observational playbook evolution without formal promotion gates, distinct from Ecdysis's aggregate training-score gate.

Synthesis: [[concepts/procedural-self-improvement]], [[concepts/evaluating-self-improvement]], and [[overviews/self-improving-llm-agents]].

## 7. Glossary

FDCR: Failure-Driven Collaborative Refinement, a fixed sequential role dialogue preceding coding. Model accommodation: a manually classified edit addressing a task model's limitation. Harness repair: a proposed correction to reusable runtime behavior. Aggregate gate: strict improvement of total training score, permitting individual-task regressions. Pass^3: success on all three trials, distinct from success on any trial.
