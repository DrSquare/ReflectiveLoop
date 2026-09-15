# Reviewed evidence recovery: September 14 scan

These are recovered review notes, **not admitted wiki pages**. The complete prepared 21-file tree was not published before workspace disconnection. Exact PDF metadata, Git hashes and recovery steps are in [the recovery record](2026-09-14-recovery.json). Do not count these papers in README or the catalog until exact PDFs and validated source/wiki entries are published. No experiments were reproduced.

## HarnessForge

**Paper:** Mingju Chen, Can Lv, Guibin Zhang, Heng Chang and Shiji Zhou, *HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems*, arXiv:2606.01779v1, June 1, 2026. This was the highest-priority documented backlog item.

### Mechanism and protocol

The unit of optimization is an executable planning/action/memory harness paired with a lineage-specific LoRA-adapted reasoner. A fixed GPT-5.5 meta-agent diagnoses failures, retrieves fault-relevant Pareto-competitive archive examples, produces an improvement brief, and generates constrained executable children. The meta-operator is not trained or self-rewriting. Tool schemas, builder interfaces and smoke tests constrain children; at most three repair attempts precede rejection. The runner, evaluator, data and backend are preserved. [PDF §§3.1-3.4, pp. 3-5; Appendix C, pp. 15-18](https://arxiv.org/pdf/2606.01779v1#page=4)

Three rounds propose eight children and retain two through two 200-task half-selection stages within roughly 1,200-task round batches. Objectives are performance, negative tokens and negative latency; task performance breaks ties. Remaining tasks evaluate survivors. Each child receives an independent materialized parent policy and its own adapter, avoiding shared trainable parameters between siblings. Successful selection rollouts supply step-level SFT without a separate environment-collection phase. Default rank/alpha/dropout is 8/16/0.05; one epoch at 2e-6. Training and proposer costs still exist. [PDF pp. 15, 18-20](https://arxiv.org/pdf/2606.01779v1#page=18)

Qwen3-4B and Qwen3-8B are evaluated on five datasets in four families: ToolHop, SearchQA (HotpotQA/2Wiki), TMDB and API-Bank. The 3,800-task training pool includes 2,000 EnvScaler-RL, 800 ToolHop and 1,000 offline QA tasks. The paper specifies disjoint test IDs and normalized-instruction deduplication. ToolHop/TMDB/API-Bank tests have 195/100/114 examples. SearchQA uses token F1, not success accuracy. TMDB/API-Bank reuse ToolHop-evolved structure after replacing tools, schemas, wrappers and constraints, so this is **interface-adapted transfer**, not unchanged plug-and-play reuse or learned-editor transfer. [PDF Appendix B/E, pp. 12-14, 20-21](https://arxiv.org/pdf/2606.01779v1#page=20)

### Results and interpretation

Table 1: 4B ToolHop correctness 52.82 versus strongest baseline 49.74; TMDB success 76 versus 64; API-Bank success 77.19 versus 72.81. The headline 12% gain is **12 percentage points**. The reported +3.56 mean uses per-metric strongest comparators, not one common baseline. Gains are not universal: 4B 2Wiki F1 is 42.00 versus 43.33, and 8B ToolHop path score is 74.05 versus 75.62. [PDF p. 6](https://arxiv.org/pdf/2606.01779v1#page=6)

At round three, removing harness/policy evolution lowers 4B ToolHop from 52.82 to 46.67/50.26 and SearchQA from 42 to 37/39. API-Bank's final matched pair reaches 77.19; the reported average is 71.93 for its final harness with earlier policies and 71.06 for its final policy with earlier harnesses. These support pair-specific benefits, not universal diagonal dominance. [PDF pp. 6-7](https://arxiv.org/pdf/2606.01779v1#page=7)

The separate objective experiment gives ToolHop 50.77 SFT, 52.31 GRPO and 51.28 RLOO using 12K versus 45.6K rollouts. Do not replace Table 1's main-run value with Table 3's separate setting. Rollout accounting excludes proposer-generation overhead; it is not all-in dollar/compute cost. [PDF pp. 8, 20](https://arxiv.org/pdf/2606.01779v1#page=8)

### Limitations and reproducibility

Only one small-model family and three rounds; no repeated-search confidence intervals in the main table. Diagnostic categories do not establish causal attribution. Table 8 lists KL coefficient 0.01 while nearby GRPO prose says 1e-3, and the listed learning-rate sweep does not contain the 2e-6 default. SearchQA's evaluation F1 differs from its RL exact/substring reward. These need run-configuration reconciliation. [PDF pp. 9, 22](https://arxiv.org/pdf/2606.01779v1#page=22)

The PDF supplies [official code](https://github.com/mingju-c/HarnessForge). HEAD verified September 14: 05b3ecadb3c9a7a938f75129ea22b8f2b36cf289. Its [README](https://github.com/mingju-c/HarnessForge/blob/05b3ecadb3c9a7a938f75129ea22b8f2b36cf289/README.md) describes harness bundles, prompts, runners and policy manifests but says large checkpoints are not committed. This operational audit is narrower than Appendix F's release claim and belongs outside paper-grounded wiki evidence. No result replay was verified.

## Co-Evolving Harnesses and Models

**Paper:** Zhou Yu and ten coauthors, Salesforce AI, *Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails*, arXiv:2609.09134v1, September 8, 2026.

### Mechanism and protocol

Seven verifiable enterprise task families cover payroll, budget approval, stock alerts, anomaly detection, browser automation, website management and code refactoring. Gemini-3.1-Pro-Preview proposes GEPA-style harness edits around Qwen3-Coder-30B-A3B. Appendix A specifies three search seeds per task, a $20 budget and 600-second rollout limit; minibatch-improving candidates enter a Pareto pool and validation picks the winner. Test data stays held out. Direct database edits are forbidden where MCP tools are required, and tool errors are exposed, preventing exact comparison with the prior framework's unmodified environment. [PDF pp. 4, 9](https://arxiv.org/pdf/2609.09134v1#page=9)

Imitation mixes successful expert trajectories with student successes. Correction starts from student-generated failures, has an automated MLE agent localize one failing turn, and selects the best of three expert replacements with a quality judge. Surrounding steps are preserved. The paper does not sufficiently specify successful re-execution of every edited full trajectory after changing a middle action. The roughly 500-row dataset is described as approximately 400 corrections plus 50 successes, leaving the approximate remainder unspecified. [PDF pp. 6, 9-10](https://arxiv.org/pdf/2609.09134v1#page=10)

LoRA uses rank 16 or 64 (best scores reported), two epochs, learning rate 1e-4, bf16 and effective batch eight. Context is 49,152 tokens, extended to 98,304 if more than 5% truncates. Table 1 gives means and SEM over three runs; imitation specifically uses three LoRA-training seeds. Exact split sizes, every arm's data counts, rank-selection details and full correction costs are incompletely specified. Under-one-hour training on the study hardware is not total search/judge/pipeline cost. Gemma-4-26B-A4B replication covers Webarena only. [PDF pp. 5, 9-10](https://arxiv.org/pdf/2609.09134v1#page=5)

### Results and interpretation

Qwen mean test success: 29.2% baseline harness, 78.0% evolved harness, 63.1% after full expert imitation under the evolved harness, and 79.7% after local correction. Imitation loses **14.9 points** on average and 4.2-29.9 points on every task. Baseline-harness imitation instead reaches 35.5% (+6.3). Correction is +1.7 over harness-only and +16.6 over imitation. Five tasks improve; payroll/budget decline 0.4/0.6. Thus prose about matching or beating every task is an interpretation of noise, not literal non-regression or a formal equivalence test. [PDF Table 1, p. 5](https://arxiv.org/pdf/2609.09134v1#page=5)

Expert Gemini averages 84.4% baseline and 93.6% evolved, but payroll falls 97.4 to 97.0, budget 97.2 to 93.2, and refactoring ties. Table 1 row four's parenthesized gains compare with the weaker evolved student, not the expert's baseline. Gemma's one-task replication is 46.7 baseline, 55.6 evolved, 41.1 after imitation; no seven-task Gemma matrix or Gemma correction result. [PDF p. 5](https://arxiv.org/pdf/2609.09134v1#page=5)

Planning's LLM-judged share of failures changes 1.1% to 14.6% after imitation and 1.8% after correction. Knowledge shares are 46.2/44.5/43.2. Domain-recipe invocation rises 30.8 to 76.1% under imitation. These observations support an interference interpretation, not identification of planning drift as the sole cause. Failure shares use different denominators; lower knowledge share does not establish fewer absolute knowledge errors when total failures increase. [PDF pp. 5-6, 10](https://arxiv.org/pdf/2609.09134v1#page=6)

### Limitations

The correction gain is modest, with no reported paired significance/equivalence analysis. LLM-judge calibration, human agreement and class counts are not fully supplied. Section 3.4's failure rates 28.9 to 26.8% are not complements of Table 1's macro means; aggregation is unspecified. Several scaffold invocation categories decline despite broad prose that usage increases. No matched ablation separates on-policy coverage, edit locality, quality judging and example selection. [PDF pp. 5-7, 10](https://arxiv.org/pdf/2609.09134v1#page=7)

Sequential harness-then-weight adaptation is demonstrated, not repeated safe compounding. The conclusion leaves RL and harness search aware of future training to future work. No paper-specific official repository was verified; cited framework code is not this pipeline's release.

## Recovered synthesis and README plan

Strengthen matched-pair evaluation; narrow unconditional additive-gains assumptions. Compare old/new harnesses crossed with old/new policies, separate full expert imitation from successful self-trajectory SFT and local correction, match selection/supervision budgets, track per-task regressions and absolute failure counts, and account for proposer/judge/training cost. These are design inferences, not new experimental results.

Neither paper tests Hyperagents-style self-editable meta-procedures jointly trained with CoSkill-style skill-library roles. The research question remains unanswered, with stronger non-recursive baselines and interference controls.

The prepared but unpublished README had full linked titles, September 14 addition dates, concise contributions, and counts of two complete admissions plus five legacy entries (seven cataloged papers, ten wiki pages). The prepared compatibility concept and question/overview updates had reciprocal links. Recover and revalidate these files; do not copy their proposed counts into main before admission succeeds.
