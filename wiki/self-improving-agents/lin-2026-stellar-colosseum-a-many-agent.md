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

## Summary

Stellar Colosseum uses a designed many-agent workflow to improve long mathematical arguments through exploration, adversarial review, dependency-aware construction, and targeted repair. It retains proof attempts and reusable findings across rounds. It is relevant as an inference-time harness comparator; the paper does not demonstrate learning a harness editor, updating model weights, or evolving a cross-task skill library. [PDF §§3-4, 8, pp. 5-10, 16-17](https://arxiv.org/pdf/2609.15983v2#page=5)

## Key Contributions

The system separates choosing a viable strategy from writing a proof. A readiness gate makes unresolved obligations explicit before decomposition, while a section dependency graph supports parallel work and local repair. Candidate proposals stay attached to their critiques during constructive aggregation, limiting the loss of objections when promising fragments are reused. [PDF §§4.1-4.3, pp. 6-9](https://arxiv.org/pdf/2609.15983v2#page=6)

This provides a concrete design for accumulating useful research state, including negative evidence. It also illustrates why a system that improves its current answer should be distinguished from one that learns how to improve itself across tasks. Adaptive compute control and trajectory-based post-training remain future work. [PDF §8, pp. 16-17](https://arxiv.org/pdf/2609.15983v2#page=16)

## Methodology and Architecture

- **Explore and gate:** strategy cards contain a route, risky lemmas, evidence, and proof obligations. Decomposition proceeds when the route is stable and remaining obligations have explicit paths to resolution; otherwise exploration continues.
- **Construct a proof DAG:** generate a LaTeX skeleton and section tasks with dependencies. Eligible sections run in parallel. Failed sections retry with their critiques, preserving unaffected work.
- **Verify and revise:** global reviewers inspect the assembled proof against its original target, including cross-section consistency. Localized defects drive repair; a broken central route triggers re-exploration. Local retry does not restructure the dependency graph.
- **Carry state forward:** the latest draft retains its criticism, while a curator stores evidence-qualified lemmas, failed approaches, references, and observations. [PDF §§4.2-4.3, pp. 8-9; §8.1, p. 16](https://arxiv.org/pdf/2609.15983v2#page=8)

Within stages, parallel proposals undergo falsification and overlapping random-group aggregation. Groups sample without replacement internally but may overlap with each other. Synthesizers can repair or combine proposals and retain unresolved conflicts; the procedure is not flat majority voting. A failed falsification attempt is not certification. [PDF §4.1, pp. 6-7](https://arxiv.org/pdf/2609.15983v2#page=7)

For both benchmarks, exploration widths are (32, 16, 8, 5, 1); other stages use (16, 8, 5, 1), with fan-in five capped by current width. These are population settings, not total-call budgets; the number of sections, retries, and global rounds also matters. [PDF Table 1, p. 10](https://arxiv.org/pdf/2609.15983v2#page=10)

## Results

| Evaluation | Reported result | Protocol needed to interpret it |
|---|---|---|
| TCS-Bench, 300 theorem tasks | Pro harness 54.0%; Flash harness 55.0%; cross-model selection 71.0% (213/300) | Two independent harness runs; eight Flash critiques select Pro if at least five approve, otherwise Flash; reference-assisted automated final grading |
| TCS-Bench comparators | Direct Pro 30.3%; DeepThink 52.0%; GPT-5.6 Pro (max) 68.0%; oracle 77.3% | Oracle knows which of two proofs passes; it is not an executable selector; baselines are not shown compute-matched |
| Codeforces, 222 problems | 218 accepted with execution probe, 213 without | Gemini 3.1 Pro; April-October 2025 contest suite; public samples and generated stress tests for feedback, hidden tests only for final grading |
| Open research cases | Five result summaries; 46/75-page Knuth drafts; 22-page Erdős draft over 15 exploration rounds | Selected contributions and artifacts, with complete research proofs/attribution deferred to companion work |

[PDF §§5-7 and Tables 2-5, pp. 10-15](https://arxiv.org/pdf/2609.15983v2#page=13)

The 71.0% score is **16 percentage points above the stronger single harness run**, with the cost of two runs and selection. The grader's reported >90% agreement comes from the separate 100-proof set used to optimize its prompt; it is not an independent human audit of these 300 outputs. Critique AUC is 0.896 relative to that grader, and routing with Pro's internal verifier reaches 64.7%. [PDF §6, pp. 13-14](https://arxiv.org/pdf/2609.15983v2#page=13)

Codeforces transfer retains mathematical decomposition and adds a terminal C++ implementation task and execution probe. All hidden tests must pass under the original checker, with no post-submission output repair. The reported 4263 rating is an estimate from the corpus's difficulty values and logistic formula, not an official competition rating. [PDF §7, pp. 14-15](https://arxiv.org/pdf/2609.15983v2#page=14)

## Limitations

No component ablations or matched total-compute comparison isolate the value of readiness gating, memory, critique retention, or aggregation. The five additional Codeforces successes cannot be assigned solely to feedback without matched calls/revisions. Aggregate benchmark scores are not accompanied by repeated-run uncertainty estimates. [PDF pp. 10, 13-16](https://arxiv.org/pdf/2609.15983v2#page=15)

Natural-language review can miss errors; retaining an objection is stronger bookkeeping, not a formal guarantee. The no-internet Erdős case does not by itself exclude training exposure. Open-research summaries and long drafts should not be treated as an independently verified success rate. Appendix A supplies shortened prompts, not a complete reproduction package. [PDF pp. 7, 10-13, 22-27](https://arxiv.org/pdf/2609.15983v2#page=22)

Cross-model execution and the theorem-to-program adaptation are useful transfer evidence, but they do not establish a learned transferable meta-procedure. Sampling is fixed before each run; local graph restructuring, adaptive allocation, and model post-training are proposed extensions. The Hyperagents/CoSkill research question therefore remains unanswered. [PDF §8, pp. 16-17](https://arxiv.org/pdf/2609.15983v2#page=16)

## Related Papers

Synthesis: [[overviews/self-improving-llm-agents]]. Research boundary: [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]]. The existing [[zhang-2026-hyperagents]] and [[feng-2026-coskill-joint-reinforcement]] records motivate the comparison, but remain abstract-based on this branch pending their separate PDF upgrade.

Detailed methods and provenance: [source note](../../sources/lin-2026-stellar-colosseum-a-many-agent.md); [exact PDF](../../papers/lin-2026-stellar-colosseum-a-many-agent.pdf). Paper-linked artifacts: [Knuth proofs](https://github.com/dpwoodru/knuthCycles), [Erdős draft](https://github.com/dpwoodru/erdos). These are proof artifacts; no official runnable harness release was identified.
