# Procedural Graphs — reviewed source draft, not admitted

Reviewed from the exact 36-page PDF on September 20, 2026. Binary publication failed; this is a review checkpoint outside the admitted source/wiki layers. The [complete bundle](lu-2026-procedural-graphs-self-evolving-execution.json) preserves canonical frontmatter, proposed README and synthesis changes, provenance, and restore guards.

## One-line Summary

Procedural Graphs persist editable execution transitions and advice around a frozen solver, combining local graph-conditioned guidance with a fixed, validation-gated graph-refinement loop. [§3, PDF pp. 3–6](https://arxiv.org/pdf/2609.09153v1#page=3)

## 1. Document Information

- **Authors and institutions:** Yuxing Lu, Yicheng Chen, Shanchan Wu, Sercan Ö. Arık; Google, Georgia Institute of Technology, and Peking University. [PDF p. 1](https://arxiv.org/pdf/2609.09153v1#page=1)
- **Version:** [arXiv:2609.09153v1](https://arxiv.org/abs/2609.09153v1), submitted September 8, 2026; reviewed September 20, 2026. This is a preprint-specific analysis.
- **Canonical full text:** [exact local PDF](https://arxiv.org/pdf/2609.09153v1), 36 pages, 5,653,711 bytes. Page citations use physical PDF pages, which match the printed numbering after the title page. Extraction completed with a font-type warning; independent parsing recovered all pages, and Tables 1, 3, and 11 were visually checked. Bytes were not rewritten.
- **Implementation:** Appendix B provides prompts, serialization details, and an algorithm. No official implementation repository was verified; neither the exact PDF nor its arXiv landing page supplies a code link. No benchmarks were reproduced for this ingestion. [Appendix B, PDF pp. 19–24](https://arxiv.org/pdf/2609.09153v1#page=19)
- **Wiki:** [reviewed paper draft](lu-2026-procedural-graphs-self-evolving-execution.paper.md).

## 2. Key Contributions

1. **A persistent execution representation.** Nodes can denote actions, skills, reasoning steps, or statuses. Directed triplets connect procedures through relations, with textual conditions, guidance, and pitfalls. This externalizes sequencing knowledge without updating model weights. [§§3.1–3.2, PDF pp. 3–5](https://arxiv.org/pdf/2609.09153v1#page=3)
2. **Guidance generated from local structure.** A separate call translates a connected neighborhood and recent trajectory into advice for the next solver step. The graph influences generation through the prompt rather than enforcing transitions as executable constraints. [§3.2, PDF pp. 4–5](https://arxiv.org/pdf/2609.09153v1#page=4)
3. **Gated graph evolution with rejection history.** Training outcomes drive edits to topology and attributes; structural screening precedes validation, and rejected candidates inform future proposals. The evolving object is the graph, not the refiner's weights, prompt, or outer acceptance algorithm. [§3.3 and Algorithm 1, PDF pp. 5–6, 24](https://arxiv.org/pdf/2609.09153v1#page=5)
4. **Separate evidence for usefulness, construction, and cost.** The paper compares memory mechanisms across models, tests recovery from an unsuitable expert graph, and separates local guidance from full-graph consumption. These studies have different splits and metrics and should not be pooled. [§5, PDF pp. 7–10](https://arxiv.org/pdf/2609.09153v1#page=7)

## 3. Methodology and Architecture

### Online execution

The retained graph is frozen within an episode and during testing. At each step, match the previous procedure to a graph node; start at `Start`. Retrieve the outgoing two-hop neighborhood, or fall back to the entire graph if matching fails. The guidance model receives that structure, the task query, and the last three trajectory steps. Its generated advice is appended to the solver prompt, while the solver receives its full history and chooses the next action. Solver, guide, and offline refiner use the same underlying model in each experimental configuration, with temperature zero. [§§3.2–4, PDF pp. 4–6](https://arxiv.org/pdf/2609.09153v1#page=4)

The four reported relation types are `LEADS_TO`, `TRIGGERS`, `PROVIDES_INPUT_FOR`, and `CONVERGES_TO`. Most main-study graphs have 7–17 nodes and 7–27 triplets; BFCL uses 131 nodes and 265 triplets. The example local serializer groups edges by hop and includes edge advice, but omits stored relation labels. Thus a benefit specifically attributable to the relation vocabulary is not isolated by the reported implementation. [Appendices B.4–B.5, PDF pp. 21–22](https://arxiv.org/pdf/2609.09153v1#page=21)

### Offline graph updates

For each training batch, collect trajectories and final scores using the current retained graph. The refiner contrasts stronger and weaker trajectories and proposes JSON additions/deletions of nodes and edges; an attribute revision deletes and re-adds an edge. Deletions apply before additions, and an edge deletion removes all relations sharing its endpoints. Oversized diagnostic context retains its final tokens. [§3.3 and Appendix B.5, PDF pp. 5–6, 23](https://arxiv.org/pdf/2609.09153v1#page=5)

Apply edits to a copy. Reject malformed edits, invalid types, or missing endpoints. If cycles are disallowed, remove detected cycle-closing edges and check acyclicity; if allowed, skip that repair/check. Require a path from each node to some zero-outdegree terminal, not necessarily the node named `End`. Tool-catalog membership is a prompt requirement, not independently enforced by the generic structural validator. Structural validity therefore neither proves tool validity nor ensures compliant runtime actions. [Algorithm 1 and preparation checks, PDF p. 24](https://arxiv.org/pdf/2609.09153v1#page=24)

Evaluate structurally valid candidates on a separate validation set. Accept when the measured mean score is **at least** the retained graph's cached score, including ties; otherwise retain the earlier graph and score. Rejection memory contains failed edits, candidate information, trajectories, scores or structural diagnostics. This guarantees nondecrease only of the cached selection statistic, not true expected performance. No isolated rejection-memory ablation or statistical acceptance test is established here. [Eq. 5, PDF p. 5; Algorithm 1, PDF p. 24](https://arxiv.org/pdf/2609.09153v1#page=24)

### Construction controls

Mode 1 uses a fixed expert graph; Mode 2 performs one ungated update of it; Mode 3 incrementally evolves it with validation. Mode 4 builds once, without gating, from `Start → End`; Mode 5 incrementally evolves that skeleton with validation. The term *online evolution* in the mode names means changes **between training batches**, not updates during test episodes. The construction experiments use frozen Gemini 3.5 Flash, strides of 100 HotpotQA or 20 MultiChallenge examples, and maximum output lengths of 2,048 solver and 8,192 refiner tokens. [Appendix D.2–D.3, PDF pp. 30–31](https://arxiv.org/pdf/2609.09153v1#page=30)

## 4. Key Results and Benchmarks

### Main comparison and its denominators

Seven baselines share the ReAct solver and tool interface: vanilla, MemoryBank, RAP, ExpeL, AutoGuide, AWM, and KnowAgent. The paper states that learning-based comparators receive the same training trajectories. Four model configurations are Claude Sonnet 4.6, Gemini 3.1 Pro, Gemini 3.5 Flash, and Grok 4.1 Fast. These are separate model-specific systems, not a frozen-graph transfer experiment. [§4 and Appendix B.3, PDF pp. 6, 20–21](https://arxiv.org/pdf/2609.09153v1#page=6)

| Benchmark | Train / test | Reported main metric and boundary |
|---|---:|---|
| HotpotQA | 1,000 / 1,000 | Gemini 3.1 Pro-judged answer equivalence; disjoint question IDs from the official validation pool |
| MultiChallenge | 100 / 166 | Gemini 3.1 Pro-judged overall success; construction study instead uses 56 test items |
| GDPval | 88 / 44 | Mean per-task rubric score; deterministic occupation split |
| ALFWorld | 238 / 134 | Task success; standard unseen split after library filtering |
| τ-bench | 500 / 115 | Pass@1 final-state match; retail-domain test |
| BFCL v3 | 100 / 100 | Official base-category multi-turn accuracy |
| EnterpriseArena | 50 / 50 | Disjoint simulator seeds; separate evolution study uses 20 / 20 / 20 train/validation/test |

These denominators and metrics come from Table 5 and Appendix B.2. The construction validation sets contain a further 1,000 HotpotQA and 100 MultiChallenge items, disjoint from test. [PDF pp. 19–20, 31](https://arxiv.org/pdf/2609.09153v1#page=19)

On the six-benchmark main table, PG is best or joint best in **21/24** model–benchmark cells: 19 wins, two ties, three losses against the strongest comparator per cell. The paper reports a one-sided sign-test p-value of 4.3 × 10⁻⁴, excluding ties. Selected comparisons are BFCL/Flash **67.00 vs 58.00**, GDPval/Pro **78.78 vs 71.37**, and τ-bench/Pro **80.00 vs 73.04**. Losses include HotpotQA/Claude **74.50 vs 75.40**, ALFWorld/Grok **39.55 vs 42.54**, and τ-bench/Grok **67.83 vs 68.70**. Table 1 supplies 95% intervals; a collection of cell wins does not demonstrate universal improvement or independent replicated optimization. [Table 1, PDF p. 7](https://arxiv.org/pdf/2609.09153v1#page=7)

### Construction and evolution

On the separate Flash construction study, scratch evolution reaches HotpotQA **66.30 EM / 78.79 F1**, versus **58.80 / 71.21** unguided. These are string metrics, not the main table's judged accuracy. MultiChallenge's 56-item test goes from **87.50%** unguided to **58.93%** with the unsuitable expert prior, **53.57%** after its one-shot update, and **92.86%** with iterative expert refinement; scratch evolution reaches **91.07%**. The mode comparison changes fresh feedback, iteration, and gating together, so it does not isolate the causal contribution of each. [Table 2, PDF p. 9; Appendix D, PDF pp. 29–31](https://arxiv.org/pdf/2609.09153v1#page=9)

EnterpriseArena simulates up to 132 monthly decisions with three hidden scheduled crises and fundraising delays. In the **20-episode-per-split** evolution experiment, the returned Round 9 graph obtains **85% test survival versus 0%** unguided; the paper reports Fisher's exact p = 2.6 × 10⁻⁸. Round 7's **95%** is an intermediate observed test result, not the returned result. Validation reaches 90%, and Round 10 is rejected. Accepted changes include a forecast-before-financing backbone, memory recall, branch pruning, and a bypass that avoids advancing the month twice. [§§5.2, 5.4, PDF pp. 8–10; Table 11 and Appendix E, PDF pp. 32–34](https://arxiv.org/pdf/2609.09153v1#page=32)

Round 5 fails structural checks before rollout. Its displayed “Validate (R04)” row repeats the rejected Round 4 candidate's statistics, rather than evaluating a new candidate or replacing the retained Round 2 score. Read the table together with Algorithm 1 and the explicit carry-forward explanation; it is not evidence that a rejected candidate became the retained state. Figure 5's generation/round labels also differ from the adjacent prose; use Table 11 and the prose for accepted-round chronology. [PDF pp. 24, 32–34](https://arxiv.org/pdf/2609.09153v1#page=32)

### Inference cost and guidance ablation

On fixed subsets with the same Flash solver prompt and graph, local generative guidance scores **89.31 / 63.99 / 81.53** on MultiChallenge/GDPval/ALFWorld, versus **80.27 / 54.80 / 72.58** without a graph. Full-graph generative guidance lowers ALFWorld success to **54.48**, showing that adding more graph context can hurt. [Table 3, PDF p. 10](https://arxiv.org/pdf/2609.09153v1#page=10)

Local guidance reduces tokens against full-graph generation, but costs **33.4% more tokens on GDPval** and **55.4% more on ALFWorld** than no graph, despite reducing solver steps. MultiChallenge tokens rise from **6,629 to 12,295**, while steps rise from **3.87 to 4.22**. These are inference costs, not an all-in cost accounting of graph evolution. The EnterpriseArena tool-call reduction likewise excludes unrecorded monthly token counts. [PDF pp. 10, 32](https://arxiv.org/pdf/2609.09153v1#page=10)

## 5. Limitations and Future Work

- **Selection stability:** a 20-episode validation set moves in five-point increments. Ties are accepted against a cached score, and successive candidate proposals reuse validation feedback. The authors caution that individual promotions are a stochastic search trace, not significance tests. The 85% returned test endpoint is stronger evidence than selecting the best observed 95%, but independent evolution repeats remain needed. [PDF pp. 5, 10, 24, 32](https://arxiv.org/pdf/2609.09153v1#page=10)
- **Causal attribution and budgets:** the main comparison bundles representation, localization, guide calls, and construction. Table 3 has no raw-local-subgraph arm, while construction modes jointly vary iteration, feedback, and gating. Neither comparison establishes an isolated rejection-memory effect or equal total compute. [PDF pp. 9–10, 30–31](https://arxiv.org/pdf/2609.09153v1#page=9)
- **Transfer and recursion:** applicability across four model families and seven domains is not reuse of one learned graph across them. The refiner/guide/solver weights and outer algorithm remain fixed. Transfer across solvers and tool interfaces is proposed future work, as is selective or reusable guidance to reduce token overhead. [PDF pp. 6, 11](https://arxiv.org/pdf/2609.09153v1#page=11)
- **Validation is not enforcement:** reachability, schema checks, and prompt instructions do not prove correct tool names, appropriate actions, or successful completion. The local serializer also omits relation labels, limiting attribution to explicitly typed edge semantics. [PDF pp. 22–24](https://arxiv.org/pdf/2609.09153v1#page=22)
- **Evaluation comparability:** preserve judge-based versus string-based HotpotQA metrics, 166 versus 56 MultiChallenge items, and 50 versus 20 EnterpriseArena test episodes. Table 3 describes fixed subsets without a full split reconciliation to Table 1. Reported intervals and zero-temperature calls do not remove environment or API stochasticity. [PDF pp. 7–10, 19–20, 31–32](https://arxiv.org/pdf/2609.09153v1#page=19)

## 6. Related Work

- [[self-improving-agents/fu-2026-se-gos-self-evolving-graph]] changes a graph for retrieving existing skills. PG instead changes execution transitions and the advice generated at individual steps. Both keep model weights fixed; their graph objects and evaluation protocols differ.
- [[self-improving-agents/li-2026-skilladam-stable-and-efficient-skill]] supplies a fixed stateful editor comparator. PG's rejection history is another optimizer-state mechanism, without evidence that the editing algorithm itself learns.
- [[self-improving-agents/yue-2026-ecdysis-efficient-and-effective-training]] uses cross-task diagnosis before code edits and provides frozen-harness model-transfer tests; PG provides an explicit graph-edit interface and local guidance, with cross-solver graph transfer still future work.
- [[self-improving-agents/zhang-2026-hyperagents]] and [[self-improving-agents/feng-2026-coskill-joint-reinforcement]] address editable meta-code and jointly trained editing/reasoning roles, respectively. PG adds a fixed-editor execution-graph control, not a direct test of their combination.

These are wiki comparisons of admitted papers, not head-to-head experiments. See [[concepts/procedural-self-improvement]], [[concepts/evaluating-self-improvement]], and [[overviews/self-improving-llm-agents]] for contextual evidence and reciprocal links.

## 7. Glossary

- **Procedural graph:** directed, attributed transitions between abstract execution steps.
- **Local guidance:** generated next-step advice from a matched node's neighborhood and recent trajectory.
- **Retained graph:** the current accepted graph, preserved after candidate rejection.
- **Rejection memory:** failed proposal/context/diagnostic history supplied to the fixed refiner.
- **Validation gate:** an empirical promotion rule; its cached nondecreasing score is not a guarantee of monotonic test improvement.
- **Online evolution (construction modes):** incremental updates between training batches; the graph remains frozen within each episode and at test time.
