---
title: "AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces"
authors: "Sungho Park; Wonjoong Kim; Rongyuan Tan; Jue Zhang; Wook-Shin Han; Pengfei Gao; Chanyoung Park; Yongqiang Yao; Rao Fu; Elsie Nallipogu; Qingwei Lin; Saravan Rajmohan; Dongmei Zhang"
year: 2026
doi: "arXiv:2608.23041"
category: ["self-improving-agents"]
pdf_path: "/papers/park-2026-autosaddler-automatic-harness-optimization-with.pdf"
pdf_filename: "park-2026-autosaddler-automatic-harness-optimization-with.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2608.23041v1"
pdf_url: "https://arxiv.org/pdf/2608.23041v1"
pdf_pages: 44
pdf_sha256: "9c6af65c3aa725e654e90d5496948e5d9b7589d09a4d6ae1accec45eec3ecc5e"
---

## Summary

AutoSaddler performs development-time harness optimization with fresh mini-batch executions, evidence-grounded code patches, and history-aware candidate recombination, then selects on development data before untouched-test evaluation.

## Key Contributions

Combines diagnosis, a prompt/tool/middleware patch taxonomy, capability-to-steering scheduling, and an EvoDAG of edits and outcomes. The full text corrects the old abstract-derived interpretation: offline means before deployment, not training only on fixed previously collected traces without re-executing candidates. Memory and skill curation are outside its stated task-agent optimization scope. [PDF pp. 3-6](https://arxiv.org/pdf/2608.23041v1#page=3)

## Methodology and Architecture

Each iteration runs the current harness on a training mini-batch, jointly diagnoses failures and edits harness code, and re-executes the patched harness on that mini-batch. A positive mini-batch delta triggers development-set evaluation. Reflection records fixed, regressed, still-failing, and still-passing cases regardless of acceptance. EvoDAG stores candidate history; an evolution agent can recombine different lineages. The final choice maximizes development score and is not modified using test feedback. [PDF pp. 4-6](https://arxiv.org/pdf/2608.23041v1#page=4)

The three optimizer roles use Claude Agent SDK; default underlying LLM is Opus 4.6. GAIA2 train/dev/test counts are 75/65/300 with disjoint universes; SWE-Bench Pro is 79/80/237 with disjoint repositories; Terminal-Bench 2.0 is a random 30/19/40 task split, not group-disjoint. Generally one optimization run is followed by three test executions. AutoSaddler/GEPA run 2 epochs on GAIA2/SBP and 4 on TB2; Meta-Harness gets larger epoch counts to avoid a smaller task-execution budget. [PDF pp. 7, 20](https://arxiv.org/pdf/2608.23041v1#page=20)

## Results

Tables 2-3 report test Pass@1 (mean +/- standard deviation over three executions): GAIA2 62.0 +/- 1.2 versus base 53.0 +/- 1.5; SWE-Bench Pro 46.9 +/- 1.8 versus 37.3 +/- 4.8; TB2 final iteration 50.0 +/- 0.0 versus 40.0 +/- 0.0 on 40 test tasks. Computed from displayed endpoints, base-harness gains are 9.0, 9.6, and 10.0 percentage points. Against the strongest automated rows, computed gaps are 7.4 (GEPA 54.6), 4.4 (GEPA 42.5), and 6.7 (Meta-Harness 43.3). Section 5.2 prints inconsistent deltas (8.4, 6.2, and 4.4); retain the table endpoints and explicit arithmetic. [PDF pp. 7-8](https://arxiv.org/pdf/2608.23041v1#page=7)

GAIA2 ablations score 57.8 without deep diagnosis, 56.9 without structured intervention, and 50.6 without generalization-aware selection, versus 62.0 full. An independent optimization run's 58.6 result is specifically Universe 22, not the aggregate three-universe score. The reported 147 traces leveraged for optimization are not total environment executions: the best development checkpoint needs approximately 1,000 executions. [PDF pp. 2, 7-8, 21](https://arxiv.org/pdf/2608.23041v1#page=21)

## Limitations

Three test executions measure deployment stochasticity, not three independent optimization runs; the extra GAIA2 optimization check covers one universe. Small TB2 test size and zero observed execution variance do not imply zero uncertainty. Test groups differ for GAIA2 and SBP, but TB2 uses random task holdout. The matched task-execution budgets do not equalize all optimizer cost; deep code diagnosis adds work. [PDF pp. 7-8, 20-21](https://arxiv.org/pdf/2608.23041v1#page=7)

Requires supervised task-level outcomes and largely stateless independent tasks. Generalization claims should not be extended to persistent user memory, evolving skill curation, or arbitrary new domains. Structured patching changes a runtime, not a learned outer optimizer or shared editor-policy RL objective. Arithmetic inconsistencies in the narrative require checking tables. The authors recommend human review/security validation before production deployment. [PDF pp. 4, 44](https://arxiv.org/pdf/2608.23041v1#page=44)

## Related Papers

[[lee-2026-meta-harness-end-to-end]]; [[hebbar-2026-sia-self-improving-ai]]; [[zhang-2026-harnesscompass-guiding-automatic-harness-evolution]]. Synthesis: [[concepts/procedural-self-improvement]] and [[concepts/evaluating-self-improvement]]. Detailed provenance: [source note](../../sources/park-2026-autosaddler-automatic-harness-optimization-with.md); [PDF](../../papers/park-2026-autosaddler-automatic-harness-optimization-with.pdf).
