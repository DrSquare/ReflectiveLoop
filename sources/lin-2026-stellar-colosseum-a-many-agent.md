---
title: "Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science"
authors: "Honghao Lin, David P. Woodruff, Yuan Deng, Jieming Mao, Song Zuo, Vahab Mirrokni"
year: 2026
doi: "arXiv:2609.15983"
category: [self-improving-agents]
pdf_path: "/papers/lin-2026-stellar-colosseum-a-many-agent.pdf"
pdf_filename: "lin-2026-stellar-colosseum-a-many-agent.pdf"
source_collection: arxiv
source_format: pdf
text_extractor: pdftotext-layout
text_extracted_date: "2026-09-16"
arxiv_version: "2609.15983v2"
pdf_url: "https://arxiv.org/pdf/2609.15983v2"
pdf_pages: 27
pdf_sha256: "08d3ddee02b0e6dcdde3c03e718477ccc0889efc60850ad8bc00d07d64b1b34f"
---

## One-line Summary
Stellar Colosseum organizes long mathematical investigations through gated strategy exploration, dependency-aware proof construction, adversarial aggregation, and reusable research state; it improves artifacts within a run without demonstrating learned harness updates or model training.

## 1. Document Information

- **Authors and affiliations:** Honghao Lin and David P. Woodruff are co-first authors; all authors list Google Research, and Woodruff also lists Carnegie Mellon University. [PDF p. 1](https://arxiv.org/pdf/2609.15983v2#page=1)
- **Canonical version:** arXiv:2609.15983v2, revised September 15, 2026; first submitted September 14. This ingestion uses v2 throughout, not a mixture of versions.
- **Full text:** unchanged [local PDF](../papers/lin-2026-stellar-colosseum-a-many-agent.pdf), 27 pages, 501,606 bytes; SHA-256 and extraction metadata are in the frontmatter and [manifest](../papers/manifest.json). Page citations use 1-based PDF pages, which match printed page numbers.
- **Review scope:** full PDF, including selected prompt templates; key result tables visually inspected on pp. 13 and 15. Experiments and companion mathematical proofs were not independently reproduced.
- **Implementation provenance:** Appendix A supplies shortened prompts with repeated instructions and implementation details omitted. The paper cites author-hosted [Knuth proof artifacts](https://github.com/dpwoodru/knuthCycles) and an [Erdős proof artifact](https://github.com/dpwoodru/erdos), not a complete runnable release of the harness. Both repository endpoints were verified on September 16; no official harness implementation was identified. [PDF pp. 17-18, 22](https://arxiv.org/pdf/2609.15983v2#page=17)

## 2. Key Contributions

The contribution is a concrete orchestration design for uncertain, interdependent proof work: explore before committing to a route; delay decomposition until remaining obligations fit a stable architecture; preserve objections during aggregation; and route global failures back to the affected sections. A shared directory carries useful results and failure evidence across research rounds. These are mechanisms for inference-time adaptation of research state, not evidence that the controller rewrites its own improvement procedure. [§§3-4, PDF pp. 5-9](https://arxiv.org/pdf/2609.15983v2#page=5)

The paper applies the design to open research, 300 research-level theorem tasks, and 222 competitive-programming problems. Its strongest TCS-Bench number uses two separate model runs plus a critique-based selector. The Codeforces adaptation retains mathematical decomposition and adds an implementation endpoint and execution probe. [§§5-7, PDF pp. 10-15](https://arxiv.org/pdf/2609.15983v2#page=10)

## 3. Methodology and Architecture

### Outer workflow and persistent state

1. **Strategy exploration and readiness:** generate route proposals with reductions, risky lemmas, and falsifiable tests. The readiness gate permits decomposition when the mechanism and proof architecture are stable and remaining obligations have concrete proof or verification paths. It does not require a finished proof. An unresolved issue that could change the route returns the system to exploration. [§4.2.1 and App. A.1, PDF pp. 8, 22-24](https://arxiv.org/pdf/2609.15983v2#page=8)
2. **Decomposition:** produce a LaTeX skeleton and a directed acyclic graph of meaningful section-level subproblems. Exposition order and dependency order have distinct roles. Independent eligible sections can run concurrently; each solver receives the relevant completed material. [§4.2.2, PDF p. 8](https://arxiv.org/pdf/2609.15983v2#page=8)
3. **Local review and retry:** critique each section against its assigned goal and dependencies. Retry with the failed text and criticism, preserving completed work elsewhere. Current local retries keep the assigned subproblem and dependencies fixed; local graph restructuring is proposed future work. [PDF pp. 8, 16, 25-26](https://arxiv.org/pdf/2609.15983v2#page=16)
4. **Global verification and repair:** review the complete proof against the original target, including cross-section assumptions and unresolved local objections. A concrete fatal objection is sufficient for rejection. Feedback identifies the relevant sections; repair the viable strategy or return to exploration when its mechanism fails. Appendix revision prompts constrain outline edits and discourage rewriting correct material merely for style. [PDF pp. 8-9, 26-27](https://arxiv.org/pdf/2609.15983v2#page=26)
5. **Cross-round memory:** retain the latest full draft with its verifier feedback, plus a curated directory of lemmas, failed approaches, references, and observations. Entries keep supporting evidence and caveats; storing a claim does not certify it. [§4.3, PDF p. 9](https://arxiv.org/pdf/2609.15983v2#page=9)

### Inner generation, falsification, and aggregation

Each stage produces typed candidate artifacts, pairs them with targeted critiques, then repeatedly synthesizes random groups. Sampling is without replacement inside a group; groups overlap across aggregation nodes. Synthesis can combine useful components, repair flaws, or retain unresolved disagreements rather than simply vote. Expected candidate reuse at one transition is next-level width times sample size divided by current width; 128 to 64 nodes with sample size five gives 2.5 expected reuse. Failure to find a flaw is expressly not a correctness proof. [§4.1, PDF pp. 6-7](https://arxiv.org/pdf/2609.15983v2#page=7)

TCS-Bench and Codeforces exploration use widths **(32, 16, 8, 5, 1)**; other stages use **(16, 8, 5, 1)**. Sample size is five, capped by current population size. Open research uses variable exploration trees, sometimes above 100 leaves. These widths do not specify total calls: proof sections, retries, and revision rounds add computation. Adaptive sample/compute allocation and model post-training are future directions. [Table 1 and §8, PDF pp. 10, 16-17](https://arxiv.org/pdf/2609.15983v2#page=10)

## 4. Key Results and Benchmarks

### TCS-Bench: reference-assisted automated grading

The benchmark has 300 theorem tasks from FOCS/STOC/SODA papers dated 2020-2026. A separate reference-assisted grader sees the ground-truth proof; its prompt was optimized on 100 expert-labeled proofs, with reported accuracy above 90% on that set. This is calibration-set performance, not a guarantee that 90% of this paper's decisions are correct. The grader scores final submissions and is not used by the selector. [§6, PDF p. 13](https://arxiv.org/pdf/2609.15983v2#page=13)

| Configuration | Reported accuracy |
|---|---:|
| Direct Gemini 3.1 Pro | 30.3% |
| Direct Gemini 3.1 DeepThink | 52.0% |
| Direct GPT-5.6 Pro (max) | 68.0% |
| Colosseum with Gemini 3.1 Pro | 54.0% |
| Colosseum with Gemini 3.7 Flash | 55.0% |
| Cross-model selection | 71.0% (213/300) |
| Oracle best of the two Colosseum runs | 77.3% |

The selector requests eight Gemini 3.7 Flash critiques of the Pro proof and chooses it if at least five judge it correct; otherwise it submits the Flash proof. The 71.0% result is 48 more successes than the stronger individual run (165/300), or **16 percentage points**, with both runs and selection included. It is not the accuracy of Flash alone. The oracle uses correctness labels and is an upper bound, not the deployed selector. Critique AUC is 0.896 relative to grader labels; routing using Pro's internal verifier alone yields 64.7%. [Table 2 and §6, PDF pp. 13-14](https://arxiv.org/pdf/2609.15983v2#page=13)

### Codeforces: hidden tests reserved for grading

The suite contains all 222 problems with clist.by difficulty estimates above 1500 from April-October 2025 contests, spanning 52 contests in the evaluation snapshot. The proof pipeline ends in a single C++ implementation. The added probe executes public samples and model-generated stress inputs, returning checker, time, and memory feedback. Hidden tests are unavailable to the workflow and used only for final grading with the original checker. [§7, PDF pp. 14-15](https://arxiv.org/pdf/2609.15983v2#page=14)

| Gemini 3.1 Pro configuration | Accepted / 222 | Corpus performance rating |
|---|---:|---:|
| Without execution probe | 213 | 3918 |
| With execution probe | 218 | 4263 |

The observed difference is five problems (about 2.25 percentage points). Strict as-submitted grading produces the same score. Ratings solve the paper's logistic difficulty equation using stored corpus estimates; **4263 is not an official contestant rating**. The comparison does not supply matched total calls, tokens, or revision budgets, so it does not isolate the effect of feedback from added inference. [§7 and Table 5, PDF pp. 14-15](https://arxiv.org/pdf/2609.15983v2#page=15)

### Open research and long-form artifacts

Section 5 summarizes contributions to five results: improved coreset dependence for subspace approximation; a conditional sparse least-squares lower bound; a stronger embedding-dimension lower bound; single-stage Hadamard quantization; and near-optimal prefix-matrix factorization lower bounds. Full proofs and attribution are delegated to companion papers, not established independently by this ingestion. [PDF pp. 10-12](https://arxiv.org/pdf/2609.15983v2#page=10)

Two case studies report 46- and 75-page Knuth-cycle proof drafts and a 22-page Erdős unit-distance draft after 15 exploration rounds with internet access disabled. These illustrate persistent research artifacts and reuse of failure evidence. Internet isolation alone does not establish absence of training-data exposure or independently certify the draft. [§§5.6-5.7, PDF pp. 12-13](https://arxiv.org/pdf/2609.15983v2#page=12)

## 5. Limitations and Future Work

- **No causal component isolation:** the evaluations do not ablate readiness gating, critique retention, the knowledge directory, or overlapping aggregation under matched compute. The table configurations and shortened prompts do not fully specify total run cost or all implementation details. Model diversity, selection, and extra computation are intertwined. [PDF pp. 10, 13-16, 22](https://arxiv.org/pdf/2609.15983v2#page=10)
- **Verification is fallible:** natural-language local/global reviewers are not formal proof checkers. TCS-Bench uses automated judgments; reported aggregate scores lack repeated-run uncertainty estimates. Codeforces hidden tests give a stronger executable acceptance criterion, but a different kind of evidence from proof validity or novel research discovery. [PDF pp. 4, 7-8, 13-15](https://arxiv.org/pdf/2609.15983v2#page=13)
- **Bounded transfer claim:** adapting the proof workflow to Codeforces requires a C++ endpoint and execution tool. Two model backbones and these task families do not establish universal model or domain transfer. Nor is the paper a test of learned skill-library transfer across tasks. [PDF pp. 13-15](https://arxiv.org/pdf/2609.15983v2#page=15)
- **Self-improvement boundary:** current sampling settings are fixed before a run, and local retry keeps the task graph neighborhood fixed. Clustered exploration has only preliminary, nonsystematic evidence; local restructuring, adaptive inference allocation, and training from externally validated trajectories are proposed extensions. Credit assignment across branching trajectories remains open. [§8, PDF pp. 16-17](https://arxiv.org/pdf/2609.15983v2#page=16)
- **Research outcomes:** the companion results and selected drafts are not a complete denominator of attempted open problems or a controlled study of autonomous discovery. This note attributes those claims to the authors rather than presenting independent mathematical verification. [§5, PDF pp. 10-13](https://arxiv.org/pdf/2609.15983v2#page=10)

## 6. Related Work

Wiki synthesis: [[overviews/self-improving-llm-agents]]. Paper page: [[lin-2026-stellar-colosseum-a-many-agent]]. Colosseum adds a useful inference-time comparator to the repository's focus on changing the harness, meta-procedure, weights, and skills. Its own proposed post-training extension does not answer [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]]. Comparisons against the five legacy entries on this branch remain provisional because their PDF upgrades are still pending separately.

## 7. Glossary

| Term | Meaning in this paper |
|---|---|
| Readiness gate | Determines whether unresolved obligations fit a stable proof plan |
| Falser / falsifier | Reviewer seeking concrete defects, without treating silence as proof |
| Candidate-critique bundle | Proposed artifact preserved together with objections |
| Overlapping aggregation | Independently sampled groups that can reuse a candidate across syntheses |
| Knowledge directory | Evidence-qualified research memory retained across rounds |
| Architecture transfer | Reuse of proof orchestration with an implementation endpoint and execution feedback |
