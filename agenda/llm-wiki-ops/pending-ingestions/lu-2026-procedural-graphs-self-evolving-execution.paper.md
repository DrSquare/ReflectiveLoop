# Procedural Graphs — reviewed paper draft, not admitted

Reviewed from the exact 36-page PDF on September 20, 2026. Binary publication failed; this is a review checkpoint outside the admitted source/wiki layers. The [complete bundle](lu-2026-procedural-graphs-self-evolving-execution.json) preserves canonical frontmatter, proposed README and synthesis changes, provenance, and restore guards.

## Summary

Procedural Graphs (PG) improve a frozen agent by persisting an editable graph of execution steps, conditions, advice, and pitfalls. A guidance call turns a local neighborhood into next-step advice; a fixed refiner edits the graph between training batches and accepts candidates through structural and validation checks. This changes the execution representation without learning the editor or enforcing a hard state machine. [§3, PDF pp. 3–6](https://arxiv.org/pdf/2609.09153v1#page=3)

Reviewed September 20, 2026 from [the exact 36-page v1 PDF](https://arxiv.org/pdf/2609.09153v1), submitted September 8. The [source note](lu-2026-procedural-graphs-self-evolving-execution.source.md) preserves detailed protocols, provenance, negative results, and reporting caveats. No official implementation repository was verified; Appendix B contains algorithm and prompt details. No benchmark reproduction was performed.

## Key Contributions

- **Execution topology as persistent memory:** directed procedure-to-procedure transitions describe how actions, reasoning steps, skills, and states connect. Edges carry textual conditions, guidance, and pitfalls. [§3.1, PDF pp. 3–4](https://arxiv.org/pdf/2609.09153v1#page=3)
- **Local, situational guidance:** the graph supplies connected context for the next step while preserving the solver's freedom to generate actions. [§3.2, PDF pp. 4–5](https://arxiv.org/pdf/2609.09153v1#page=4)
- **Self-evolving graph under fixed rules:** success/failure traces support structural and attribute edits; rejected proposals are retained as negative evidence. Scratch construction and repair of a flawed expert prior are evaluated separately from main benchmark comparisons. [§§3.3, 5.3, PDF pp. 5–6, 9](https://arxiv.org/pdf/2609.09153v1#page=5)

## Methodology and Architecture

At inference, match the previous procedure to a node and extract its outgoing **two-hop** neighborhood. If matching fails, use the full graph. A guidance model combines this context with the query and **three recent trajectory steps**, then appends advice to the ReAct solver prompt. The graph is fixed during the episode and test evaluation. Solver, guide, and refiner use the same underlying frozen model in each configuration. [§§3.2–4, PDF pp. 4–6](https://arxiv.org/pdf/2609.09153v1#page=4)

Between training batches, contrast high- and low-scoring traces; propose node/edge additions and deletions, including attribute changes through delete-and-re-add. Structural checks validate schema, endpoints, cycle policy, and terminal reachability. A valid candidate survives when its measured validation score matches or exceeds the retained graph's cached score; ties are accepted. Rejected edits and their diagnostic context feed the next proposal. This is stateful optimization by a fixed refiner. [Eq. 5 and Algorithm 1, PDF pp. 5–6, 24](https://arxiv.org/pdf/2609.09153v1#page=24)

The structural validator does not independently enforce membership in the tool catalog, and terminal reachability need not lead to the particular node named `End`. The example serializer omits relation labels even though the stored graph is typed. These implementation details limit claims of executable safety or a demonstrated benefit from relation types alone. [Appendix B.5–B.6, PDF pp. 22–24](https://arxiv.org/pdf/2609.09153v1#page=22)

## Results

| Study | Reported result | Protocol boundary |
|---|---|---|
| Six benchmarks × four models | Best/joint best in 21/24 settings; 19 wins, two ties, three losses against strongest baseline per cell | Shared ReAct/tool interfaces; model-specific systems, not graph transfer |
| BFCL / Gemini 3.5 Flash | 67.00% vs strongest baseline 58.00% | 100 base-category multi-turn test tasks |
| GDPval / Gemini 3.1 Pro | 78.78 vs 71.37 | Rubric score on 44 tasks; not binary accuracy |
| HotpotQA construction / Flash | Scratch evolution 66.30 EM / 78.79 F1 vs unguided 58.80 / 71.21 | 1,000 train, 1,000 validation, 1,000 test; different metric from main judged accuracy |
| MultiChallenge construction / Flash | Expert graph 58.93%, one-shot update 53.57%, iterative expert refinement 92.86%; unguided 87.50% | 100 train, 100 validation, 56 test; main table uses 166 test items |
| EnterpriseArena evolution / Flash | Returned graph 85% test survival vs unguided 0%; 90% validation survival | 20 episodes per split, up to 132 months; 95% intermediate test result was not the returned endpoint |

Results and denominators: [Tables 1–2, PDF pp. 7–9](https://arxiv.org/pdf/2609.09153v1#page=7), [Table 5/metrics, PDF pp. 19–20](https://arxiv.org/pdf/2609.09153v1#page=19), [Appendix D.3 and Table 11, PDF pp. 31–32](https://arxiv.org/pdf/2609.09153v1#page=31). The main comparison loses to the strongest baseline on Claude/HotpotQA and Grok/ALFWorld and τ-bench. The paper's sign test across main cells and Fisher test for the final survival endpoint do not establish significance for every graph promotion.

The fixed-graph usage ablation favors local generation over full-graph generation, but its cost is higher than no graph. Local guidance improves GDPval/ALFWorld scores while using **33.4% / 55.4% more tokens** than the unguided baseline. Full-graph generation actually lowers ALFWorld success from 72.58% to 54.48%; localization reaches 81.53%. Fewer solver steps or tool calls therefore must not be reported as lower total compute. [Table 3, PDF p. 10; Appendix E.1, PDF p. 32](https://arxiv.org/pdf/2609.09153v1#page=10)

## Limitations

Validation reuse, cached-score comparison, and five-point increments from 20 episodes make individual promotion decisions noisy. The returned 85% test result is the appropriate endpoint; choosing the observed 95% checkpoint would select on test. In Table 11, Round 5's displayed values carry over a rejected candidate's measurements after structural failure, not a new validation run or a change to retained state. [PDF pp. 10, 24, 32–33](https://arxiv.org/pdf/2609.09153v1#page=32)

Mode comparisons jointly change iteration, fresh feedback, and gating. The usage ablation lacks a raw-local-subgraph arm; the benefits of topology, advice, extra inference calls, and rejection memory are not fully isolated at matched budgets. Cross-solver/tool-interface reuse and reducing guidance overhead remain future work. Frozen models with evolving graphs do not demonstrate a self-modifying editor or CoSkill-style co-training. [PDF pp. 9–11, 30–31](https://arxiv.org/pdf/2609.09153v1#page=9)

## Related Papers

- [[self-improving-agents/fu-2026-se-gos-self-evolving-graph]] evolves retrieval structure for unchanged skills; PG evolves execution transitions and their step-level guidance.
- [[self-improving-agents/li-2026-skilladam-stable-and-efficient-skill]] is another fixed stateful editor, acting on skill documents rather than execution graphs.
- [[self-improving-agents/yue-2026-ecdysis-efficient-and-effective-training]] provides a diagnostic code-editing comparator with frozen-harness cross-model tests; PG has not demonstrated equivalent graph transfer.
- [[self-improving-agents/zhang-2026-hyperagents]] and [[self-improving-agents/feng-2026-coskill-joint-reinforcement]] distinguish editable meta-procedures from shared-model editing/reasoning training. PG supplies neither combination nor a direct answer to that research question.

These are synthesis comparisons, not matched experiments. Context: [[overviews/self-improving-llm-agents]], [[concepts/procedural-self-improvement]], and [[concepts/evaluating-self-improvement]].
