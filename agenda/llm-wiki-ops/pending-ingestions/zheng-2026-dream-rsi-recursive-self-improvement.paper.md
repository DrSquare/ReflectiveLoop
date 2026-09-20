# Dream-RSI — paper review draft

**Not admitted:** exact PDF reviewed locally but not published. Canonical files and README changes are preserved in the [complete bundle](zheng-2026-dream-rsi-recursive-self-improvement.json). Local links below are adapted for reviewing this draft; the bundle preserves the intended canonical text.

## Summary

Dream-RSI revises executable exploration policies using replay of recorded scientific-discovery trees, then deploys the selected policy to collect more live experience. The coding agent, LLM policy developer, evaluator and execution interfaces stay fixed. It is an evolving search controller under a designed improvement loop. [PDF §3, pp. 4-6](https://arxiv.org/pdf/2609.14858v1#page=4)

## Key Contributions

- Converts discovery history into a replay environment with known outcomes, enabling many controller evaluations without regenerating the candidate programs.
- Uses a shared online/replay decision interface for branch continuation, root opening, concurrency and stopping.
- Tests live discovery across algorithm engineering, mathematical optimization and GPU kernels, including held-out datasets for the discovered Lasso solver.

The replay world covers stored continuations; it is not a learned dynamics model that predicts unobserved outcomes. [PDF pp. 3-8](https://arxiv.org/pdf/2609.14858v1#page=5)

## Methodology and Architecture

Each tree node stores an artifact, filesystem snapshot, diagnostics and score. Online attempts resume selected workspaces and append evaluated children. Offline replay reveals existing children, preserving branch order and resetting controller state for each historical world. Candidate policies are revised by a fixed developer and scored on the same accumulated pool. [PDF pp. 5-6](https://arxiv.org/pdf/2609.14858v1#page=5)

Equation 1 rewards the best revealed score, penalizes represented calls and rewards concurrency. Retaining the incumbent guarantees nondecrease only on that fixed pool/objective. Appendix B specifies a different beta-swept attainment-AUC minus parallelism-penalty objective, a prefix-only portfolio policy, recovery rules and pre-episode grid planning. The appendix also permits multiple root cells in one batch. These implementation details need reconciliation with the main formalism. [PDF pp. 6, 19-23](https://arxiv.org/pdf/2609.14858v1#page=19)

Replay selection is adaptive reuse of development data. No untouched replay-world test is specified. Moreover, the online discovery prompt reads cross-branch history; this note's inference is that changing search order can change the context that produced a recorded child. Therefore exact stored replay does not establish exact counterfactual online value. [PDF pp. 5-6, 18-19](https://arxiv.org/pdf/2609.14858v1#page=19)

## Results

The controlled comparator uses the same discovery model, evaluator, initialization and per-round caps but keeps exploration fixed. Main cost plots count discovery-agent calls, without complete policy-development/replay accounting. [PDF p. 7](https://arxiv.org/pdf/2609.14858v1#page=7)

| Setting | Result versus fixed exploration | Qualification |
|---|---|---|
| Lasso, Pro, five rounds | 550 → 317 calls; average 3587.1 → 2931.0 ms | RCV1 improves; five other held-out datasets regress |
| Lasso, Flash, five rounds | 3200 → 1879 calls; average 2516.7 → 2350.6 ms | Five datasets improve; DNA regresses |
| Mathematical discovery, Pro, ten rounds | Sum-Difference improves; Circle Packing ties | Autocorrelation worsens 1.456001 → 1.456375, where lower is better |
| VGG16 / LayerNorm | Comparable performance with 2.43× / 1.79× fewer generations | Target-performance comparison, not all-in cost |
| ConvDiv / ConvMax | 2.09× / 1.44× higher inverse-runtime score at comparable budgets | Selected discovery-curve comparison |

[PDF Figure 3/Table 1/Figure 4, pp. 8-10](https://arxiv.org/pdf/2609.14858v1#page=8)

Lasso search uses 17 synthetic instances; six downstream datasets are held out. Its correctness gate compares objective values to sklearn plus 1e-6 on fresh instances distinct from timing cases. The roughly 162× call-count headline compares Pro to SimpleTES with another model; Flash's corresponding ratio is about 27×. No independent-run confidence intervals accompany the main comparisons. [PDF pp. 7-8, 17](https://arxiv.org/pdf/2609.14858v1#page=17)

## Limitations

The fixed-pool selection guarantee does not imply monotonic live gains, unbiased off-policy estimation or transfer of one learned controller across domains. The reported Lasso holdout concerns the discovered solver. Cost matching must include the developer and evaluator, not just discovery calls. Exact replay objectives, hyperparameters and runtime settings need reconciliation before reproduction. A one-task guidance ablation should not be generalized into a claim that memory hurts discovery. [PDF pp. 5-11, 19-23](https://arxiv.org/pdf/2609.14858v1#page=11)

## Related Papers

[[overviews/self-improving-llm-agents]], [[concepts/procedural-self-improvement]] and [[concepts/evaluating-self-improvement]] connect this replay-selected search controller to the wiki's mechanism and evaluation taxonomy. The [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]] question remains unanswered: Dream-RSI has no skill-editor/reasoner co-training and does not learn its controller-development procedure.

Details and exact provenance: [source note](zheng-2026-dream-rsi-recursive-self-improvement.source.md). Paper-linked official repository: [zhengkid/Dream-RSI](https://github.com/zhengkid/Dream-RSI).
