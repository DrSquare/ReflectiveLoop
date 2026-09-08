---
title: "Hyperagents"
authors: Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina
year: 2026
doi: arXiv:2603.19461
category: [self-improving-agents]
pdf_path: /papers/zhang-2026-hyperagents.pdf
pdf_filename: zhang-2026-hyperagents.pdf
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: 2026-09-08
arxiv_version: 2603.19461v1
pdf_url: https://arxiv.org/pdf/2603.19461v1
pdf_pages: 60
pdf_sha256: 92f9a73b43699c08c6000f7d4f1b68bec9fd872d217467fe4a1127e2f7981f1e
full_text_reviewed_date: 2026-09-08
---

## One-line Summary

Hyperagents make both task-agent and meta-agent code editable within an evolutionary archive; experiments support transferable agent-generation capability in a specific source-to-target setting, with fixed foundation-model weights and important limits on claims of fully recursive or compounding improvement. [§§3-5, pp. 4-13](https://arxiv.org/pdf/2603.19461v1#page=4)

## 1. Document Information

- Zhang et al., *Hyperagents*, arXiv:2603.19461v1, March 19, 2026; 60 pages. Grounded in the exact [local PDF](../papers/zhang-2026-hyperagents.pdf), retrieved September 8, 2026. Citations use 1-based PDF pages.
- Paper-linked [code and experiment logs](https://github.com/facebookresearch/Hyperagents); no reproduction was performed in this ingest.

## 2. Key Contributions

- Separates improving target-task performance from improving the procedure that generates future agents. Both components live in the editable Python program. This removes an architectural dependence on coding-task competence being aligned with modification competence; it does not prove improvement on arbitrary tasks. [§3, pp. 4-5](https://arxiv.org/pdf/2603.19461v1#page=4)
- Combines that representation with DGM's archive of intermediate agents, enabling reuse of stepping stones. Ablations separately remove evolving meta-agents or archive-based exploration. [§4.1, p. 6](https://arxiv.org/pdf/2603.19461v1#page=6)
- Introduces improvement@k experiments that hold an evolved meta-agent fixed while testing its ability to generate better task agents in a new domain. [§5.2, pp. 9-11](https://arxiv.org/pdf/2603.19461v1#page=9)

## 3. Methodology and Architecture

DGM-H alternates selecting a parent, generating a modified hyperagent, evaluating the task component, and adding it to an archive. Main experiments use a handcrafted parent-selection rule favoring performance and exploration; the rule and evaluation protocol are outside the editable core. Appendix E.5 separately explores editable parent selection. Thus the **task/meta program is editable**, but the entire experimental optimizer is not unrestricted. [§3, p. 5](https://arxiv.org/pdf/2603.19461v1#page=5); [§7, p. 14](https://arxiv.org/pdf/2603.19461v1#page=14)

The initial task agent is a single model call; the meta-agent has shell and file-editing tools. Foundation-model weights remain frozen. Models differ by role/domain: Polyglot uses Claude 3.5 Sonnet for modification and o3-mini for evaluation; other domains use Claude 4.5 Sonnet for modification, with GPT-4o for paper review, Claude 4.5 Sonnet for robotics, and o4-mini for grading. Robotics trains a separate robot policy using generated rewards; that is not training the foundation model doing self-modification. [§4, p. 5](https://arxiv.org/pdf/2603.19461v1#page=5); [§4.2, p. 7](https://arxiv.org/pdf/2603.19461v1#page=7); [Table 3, p. 35](https://arxiv.org/pdf/2603.19461v1#page=35)

Paper review and math grading each use 100 training, 100 validation, and 100 test tasks. Coding uses 60 training/165 test tasks; robotics uses six training and six testing repetitions. Parent selection uses validation when available, training otherwise; staged screening can assign zeros to unevaluated tasks. Robotics trains reward designers for walking, then tests reward generation for maximizing torso height. [§4.2, pp. 6-7](https://arxiv.org/pdf/2603.19461v1#page=6); [Table 2, p. 28](https://arxiv.org/pdf/2603.19461v1#page=28)

## 4. Key Results and Benchmarks

Unless otherwise indicated, §5 reports five runs, medians, and 95% bootstrap intervals from 1,000 resamples; significance claims below are the authors' Wilcoxon-test reports. [p. 7](https://arxiv.org/pdf/2603.19461v1#page=7)

| Experiment | Full-text result | Evidence |
|---|---|---|
| Polyglot, 80 iterations | Full-benchmark performance 0.084 to 0.267 (CI 0.231-0.280). This full set includes training tasks. Original DGM is reported at 0.307; the conclusion is comparable coding improvement, not superiority over DGM. | [§5.1, pp. 7-8](https://arxiv.org/pdf/2603.19461v1#page=7) |
| Joint paper-review/robotics search, 100 iterations | Test paper-review accuracy 0.710 (0.590-0.750); robotics task score 0.372 (0.355-0.436). DGM-custom gives 0.590 and 0.348; DGM-H's advantage over that customized baseline is not significant (p>0.05). | [§5.1, pp. 8-9](https://arxiv.org/pdf/2603.19461v1#page=8) |
| Source-to-target transfer, frozen meta-agent, 50 iterations | Agents transferred from joint paper-review/robotics runs to IMO grading achieve imp@50 0.630 (0.540-0.630), vs initial DGM-H meta-agent 0.0 (0.0-0.130). The paper reports p<0.05. | [§5.2, pp. 10-11, Fig. 3](https://arxiv.org/pdf/2603.19461v1#page=10) |
| Continued evolution on IMO grading, 200 iterations | Transferred initialization 0.640 (0.550-0.720), initial-agent initialization 0.610 (0.510-0.680); p>0.05. | [§5.3, pp. 12-13, Fig. 4](https://arxiv.org/pdf/2603.19461v1#page=12) |
| Strong task-agent initialization | Best evolved ProofAutoGrader artifact: full IMO-GradingBench accuracy 0.601 vs 0.561; MAE 0.175 vs 0.178. Distinct from the smaller test split's 0.700 vs 0.670. | [§5.3, p. 13](https://arxiv.org/pdf/2603.19461v1#page=13) |

Transfer carries **both the task and meta implementation**, selected by discounted descendant improvements. The meta component is frozen during imp@50; task-agent variants continue to be generated, with the reported best selected using validation. This is adaptation under a generation budget, not zero-shot transfer of final task accuracy or an all-pairs domain-transfer matrix. [§5.2, pp. 9-11](https://arxiv.org/pdf/2603.19461v1#page=9); [Appendix D.4, pp. 36-37](https://arxiv.org/pdf/2603.19461v1#page=36)

## 5. Limitations and Future Work

- **Initialization matters:** initial paper-review and math scores are zero because required output parsing is absent. Large gains include making a usable task interface, not solely improving substantive judgment. [pp. 8, 10](https://arxiv.org/pdf/2603.19461v1#page=8)
- **Transfer attribution:** carrying both task and meta code does not isolate the meta component under identical task scaffolds. Persistent memory and performance tracking are inspected examples; they are not individually ablated causal explanations. [§5.2, pp. 10-12](https://arxiv.org/pdf/2603.19461v1#page=10)
- **Compounding:** the 0.640 vs 0.610 endpoint is suggestive, not statistically established superiority or evidence of unbounded acceleration. [§5.3, p. 12](https://arxiv.org/pdf/2603.19461v1#page=12)
- **Outer-loop boundary:** fixed tasks, selection, and evaluation constrain self-modifiability. Preliminary editable selection scores 0.491 vs random 0.428 and handcrafted 0.532; differences are not significant. [§7, p. 14](https://arxiv.org/pdf/2603.19461v1#page=14); [Appendix E.5, p. 57](https://arxiv.org/pdf/2603.19461v1#page=57)
- Task metrics differ: peer-review accuracy measures agreement with acceptance outcomes; robotics measures downstream simulated policy performance. They cannot be pooled as equivalent evidence of general intelligence. [§4.2, pp. 6-7](https://arxiv.org/pdf/2603.19461v1#page=6)

## 6. Related Work

[[lee-2026-meta-harness-end-to-end]] optimizes task harness code with a fixed proposer setup. [[hebbar-2026-sia-self-improving-ai]] adds task-model weight updates. [[feng-2026-coskill-joint-reinforcement]] learns an editor policy under a fixed RL protocol. These are different editable components, not a demonstrated dominance hierarchy. See [[overviews/self-improving-llm-agents]] and [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].

## 7. Glossary

- **Hyperagent:** one editable program containing task and meta agents.
- **Metacognitive self-modification:** edits to how future agent variants are generated.
- **imp@k:** task-performance improvement obtained by a fixed meta-agent over a bounded number of generated variants; preserve validation-based selection in implementation.
- **Archive:** previous candidates retained as possible parents, including intermediate stepping stones.
