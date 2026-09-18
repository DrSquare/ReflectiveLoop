# Dream-RSI — source review draft

**Not admitted:** exact PDF reviewed locally but not published. Canonical files and README changes are preserved in the [complete bundle](zheng-2026-dream-rsi-recursive-self-improvement.json). Local links below are adapted for reviewing this draft; the bundle preserves the intended canonical text.

## One-line Summary

Dream-RSI alternates online scientific-program discovery with offline replay of recorded discovery trees to revise executable exploration policies, keeping the discovery model, policy-development agent, evaluator and interfaces fixed.

## 1. Document Information

- **Identity:** Tong Zheng and 16 coauthors; Google, University of Maryland, Google DeepMind and University of Virginia. Submitted September 14, 2026; this note pins arXiv:2609.14858v1. [PDF p. 1](https://arxiv.org/pdf/2609.14858v1#page=1)
- **Artifact:** [exact PDF](https://arxiv.org/pdf/2609.14858v1), 36 pages including appendices, 954,448 bytes; SHA-256 `b2d13d5944d052c2b63d40e65dce116ebcc606e3b756f6acfc938afe21fe2db9`; Git blob `0cb845272e11df00319a97fc62ecdbb700db0640`. Poppler layout extraction succeeded with a font-type warning. PyMuPDF independently parsed all pages; result pages 8-10 were rendered and inspected. Bytes were not modified.
- **Official repository:** [zhengkid/Dream-RSI](https://github.com/zhengkid/Dream-RSI), linked by PDF p. 1. Publication/code availability is separately recorded in the [operational audit](../dream-rsi-code-audit-2026-09-18.md). No experiment was reproduced.
- **Reading scope:** main method and all empirical sections; Appendix A task definitions, Appendix B controller/discovery prompts, and inspection of Appendix C's supplied Lasso implementation. Citations use 1-based PDF pages.

## 2. Key Contributions

The reusable object is a **recorded search process**, not only a successful answer, a natural-language skill or a generated dynamics model. A controller can test different stopping, batching and branch-continuation choices against stored outcomes without regenerating each candidate program. Selected controller code then produces additional live experience, which expands the replay pool. This is a concrete alternative to evaluating every proposed exploration strategy through a fresh long online search. [PDF §§2-3, pp. 3-6](https://arxiv.org/pdf/2609.14858v1#page=4)

The contribution is bounded: replay covers realized branches, the policy-development procedure remains designed and fixed, and empirical transfer concerns discovered solvers evaluated on new datasets rather than a single learned controller transferred between domains. Eight discovery tasks span one algorithm task, three mathematical tasks and four GPU kernels. [PDF pp. 3-10](https://arxiv.org/pdf/2609.14858v1#page=7)

## 3. Methodology and Architecture

### State, action and persistence

A node records a filesystem snapshot, generated artifact, evaluation diagnostics and score, with one primary parent identifying the workspace from which the attempt began. In the main formulation the controller selects up to W eligible nodes: the root or observed leaves. Live execution restores selected workspaces, calls the fixed discovery agent, evaluates its outputs and appends children. The controller's code stays fixed within one live rollout; historical trees are separate from the new tree. An empty batch or the round cap ends exploration. [PDF §3, p. 5](https://arxiv.org/pdf/2609.14858v1#page=5)

Offline, each policy/world pair resets to the root. Selecting a non-root frontier reveals its unique recorded continuation; selecting the root reveals its earliest unopened branch. No unseen outcome is generated. Branches retain parent-child order, although depth, batching, branch opening and stopping can differ. Exhausted support returns no child; replay also stops at its round cap or after exposing the whole tree. [PDF pp. 5-6](https://arxiv.org/pdf/2609.14858v1#page=6)

### Objective and promotion

For a revealed subtree, let N be the number of non-root nodes and k the number of completed decision rounds. The main replay objective is

`V = best revealed score - beta_1 * N + beta_2 * N / max(1, k)`.

The terms reward solution quality, penalize represented discovery calls and reward useful concurrency. Scores are averaged across the fixed historical pool. A fixed LLM developer revises controller code from replay trajectories and scores; the best evaluated candidate, including the incumbent, becomes the next live controller. Therefore selection cannot lower **that pool's replay score under that objective**. It does not guarantee better expected online discovery, held-out replay, all-in cost or a future expanded pool's score. [PDF §3, p. 6](https://arxiv.org/pdf/2609.14858v1#page=6)

### Appendix implementation contract and discrepancies

Appendix B is substantially more prescriptive than a generic policy search. It constrains `OptimalPolicy.solve` to revealed prefixes, uses failure/repair histories to rank a portfolio of exploitation, exploration and at most one recovery candidate, prohibits hardcoded winning cells and random sampling, and requires an explicit pre-episode `plan_grid`. Grid plans can vary width/depth within hard caps; replay plans outside recorded structural support cannot earn reward. A scalar beta is fixed within an episode, swept offline, and its next default adjusted between live cycles from archived evidence. The developer is therefore editing within a substantial fixed scaffold. [PDF pp. 19-23](https://arxiv.org/pdf/2609.14858v1#page=19)

Two descriptions need reconciliation before reproduction. The appendix ranks a beta-swept attainment/work curve using `pareto.auc - lambda * parallel_penalty`, unlike the best-score-minus-work-plus-concurrency objective in Equation 1. Its interface also permits several distinct roots in one batch, while the main mathematical action is a set containing a single root symbol. Neither equivalence nor exact experimental configuration is resolved in this note. The main section additionally mixes M evaluated versions indexed 0 through M-1 with wording about M revisions and a generated Mth version; that accounting should be checked against a runnable release. [PDF pp. 5-6, 19, 21-23](https://arxiv.org/pdf/2609.14858v1#page=19)

## 4. Key Results and Benchmarks

### Controlled comparison and cost unit

Recursive Fixed Exploration shares the discovery agent, evaluator, initialization and per-round caps; both start with the same hand-designed parallel-refinement policy. Pro uses 10 workspaces with up to 11 steps (110 calls/round); Flash uses 32 with up to 20 (640). Later Dream-RSI rounds revise the controller. The reported discovery-cost unit is **discovery-agent calls**, not total tokens, dollars, policy-development LLM calls, replay CPU work or measured end-to-end latency. The latter distinction follows from the stated accounting and separate developer loop. [PDF pp. 4, 7](https://arxiv.org/pdf/2609.14858v1#page=7)

### Lasso solver discovery

Both methods run five rounds using 17 synthetic search instances; the resulting solver is measured on six held-out biological/nonbiological datasets. Correctness requires every path objective to be no worse than sklearn's value plus 1e-6, on fresh instances distinct from timing instances. Any failed check gives search score zero. Otherwise the search reward is inverse geometric-mean runtime; the reported downstream table is a separate six-dataset average in milliseconds. [PDF pp. 7-8, 17](https://arxiv.org/pdf/2609.14858v1#page=17)

| Backbone | Fixed calls → Dream-RSI calls | Fixed average runtime → Dream-RSI | Derived reduction |
|---|---:|---:|---|
| Gemini-3.1-Pro | 550 → 317 | 3587.1 → 2931.0 ms | 42.4% fewer calls; 18.3% lower average runtime |
| Gemini-3.7-Flash | 3200 → 1879 | 2516.7 → 2350.6 ms | 41.3% fewer calls; 6.6% lower average runtime |

The averages conceal heterogeneous effects. Pro improves RCV1 (19550.1 → 14616.0 ms) but is slower on the other five datasets, including Gisette (1861.8 → 2841.0). Flash improves five datasets but loses on DNA (29.8 → 31.4). The large absolute RCV1 times heavily influence the unnormalized average. This contradicts an interpretation of uniform superiority over the controlled baseline. [PDF Figure 3, p. 8](https://arxiv.org/pdf/2609.14858v1#page=8)

Against SimpleTES's 51,200 generations, the count ratios are about 161.5 for Pro and 27.2 for Flash. The often-highlighted 162-fold figure is specific to Pro and compares different model families; it is not an isolated controller-effect or dollar-cost estimate. The paper lists a second dagger-marked SimpleTES row without an explanation in the figure/caption; avoid pooling it with the unmarked row. The supplied solver uses strong-rule screening, adaptive Cauchy-Schwarz KKT pruning and lazy Gram construction. Appendix C supplies this program, not the complete exploration runtime. [PDF pp. 8-9, 23-36](https://arxiv.org/pdf/2609.14858v1#page=8)

### Mathematical discovery and kernels

Mathematical search uses Pro for ten rounds. Table 1 has **one win, one tie and one loss** against the controlled fixed baseline:

| Objective | Direction | Fixed | Dream-RSI |
|---|---|---:|---:|
| Sum-Difference | Higher | 1.144047 | 1.145427 |
| Autocorrelation | Lower | 1.456001 | 1.456375 |
| Circle Packing | Higher | 2.635983 | 2.635983 |

SimpleTES's autocorrelation value is better still (1.453675). Thus a broad reading that all math tasks match or exceed strong baselines is too strong. The paper reports fewer than 1,000 generations for its approach but does not provide per-task totals in Table 1. Appendix A defines multiple circle-packing sizes and autocorrelation objectives without mapping every variant to a separate reported main-table column. [PDF pp. 9-10, 17-18](https://arxiv.org/pdf/2609.14858v1#page=9)

For four KernelBench tasks, Figure 4 reports 2.43×/1.79× fewer generations to comparable VGG16/LayerNorm performance, and 2.09×/1.44× higher inverse-runtime scores at comparable ConvDiv/ConvMax budgets. These are two different comparisons, not four final-score improvements or measured latency speedups of the entire discovery service. Kernels must pass reference-correctness checks. [PDF pp. 10-11](https://arxiv.org/pdf/2609.14858v1#page=10)

### Analyses and their scope

On ConvDiv, injecting directional semantic guidance worsens both methods' plotted trajectories. This is evidence about that guidance and task, not a general rejection of memory or skill retrieval. The same task's effort falls from 110 to 50 attempts before rising to 92 as progress flattens; this shows adaptive allocation, not causal attribution to one controller rule. Independent-run variation and confidence intervals are not reported in these figures. [PDF §5, p. 11](https://arxiv.org/pdf/2609.14858v1#page=11)

## 5. Limitations and Future Work

1. **Replay support is finite.** Recorded returns permit cheap policy comparisons only over stored continuations. There is no learned transition model extrapolating new outcomes and no demonstrated unbiased off-policy-value estimator. Prefix-only access prevents one kind of direct leakage; it does not establish representative coverage or control adaptive selection overfitting. [PDF pp. 5-6, 21-23](https://arxiv.org/pdf/2609.14858v1#page=6)
2. **Reordering can change live context.** The discovery prompt asks the agent to read all available historical proposals, scores and failures across branches. Our inference: if an alternative controller changes that history, a stored child need not equal the outcome of rerunning the agent under the new context. The paper's exact replay transition should not be interpreted as an exact causal counterfactual simulator of arbitrary online schedules. [PDF pp. 5-6, 18-19](https://arxiv.org/pdf/2609.14858v1#page=19)
3. **Selection and deployment are different tests.** All recorded worlds participate in adaptive controller development and selection; the main method does not specify an untouched replay-world test split. Lasso's held-out datasets assess solver transfer, not transfer of a frozen controller or developer into a new domain. New live discovery provides empirical deployment evidence without a monotonicity guarantee. [PDF pp. 5-8](https://arxiv.org/pdf/2609.14858v1#page=7)
4. **Budget and reproducibility gaps remain.** Match complete proposer, discovery, evaluator and replay costs; report hardware, timing repetitions, independent searches, beta/lambda settings and policy-version counts. Those details are not sufficiently specified to reconstruct all reported results from the main protocol plus prompts alone. Reconcile the objective and batching descriptions before treating Equation 1 as the exact implemented selection rule. [PDF pp. 6-11, 19-23](https://arxiv.org/pdf/2609.14858v1#page=19)
5. **The recursive scope is limited.** Controller code changes, but the developer, fixed prompts/rules, evaluator and base model do not learn. No skill-library co-training, learned controller-development algorithm or cross-domain frozen-controller experiment is established. [PDF pp. 4-7, 19-23](https://arxiv.org/pdf/2609.14858v1#page=4)

These are qualifications and proposed controls derived from the reported protocol; they are not claims that additional experiments have been run or that the observed gains are invalid.

## 6. Related Work

Paper page: [reviewed paper draft](zheng-2026-dream-rsi-recursive-self-improvement.paper.md). [[overviews/self-improving-llm-agents]] places replay-selected exploration beside harness search. [[concepts/procedural-self-improvement]] distinguishes the changing controller from the fixed controller-development procedure; [[concepts/evaluating-self-improvement]] separates replay selection, live deployment and transfer.

The [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]] question remains open. Dream-RSI motivates a replay-selected controller baseline under a fixed developer before attributing benefits to a learned/self-editable editor. It does not itself combine Hyperagents with CoSkill. AutoSaddler's existing note concerns fresh development re-execution; Dream-RSI's stored-outcome replay provides a useful operational distinction, not a head-to-head comparison.

## 7. Glossary

| Term | Meaning and boundary |
|---|---|
| Discovery tree | Recorded workspaces, candidate programs, evaluation feedback and primary-parent relationships |
| Replay world | Fixed realized tree exposed incrementally; no new outcomes generated |
| Exploration policy | Executable rule for branch allocation, batching, continuation and stopping |
| Policy developer | Fixed LLM agent editing exploration code from replay feedback |
| Prefix-observable | Decisions use revealed outcomes and permitted structural information |
| Replay promotion | Selecting the best historical-pool score with the incumbent eligible |
| Discovery-agent calls | Published cost unit; excludes an all-in accounting of the improvement loop |
