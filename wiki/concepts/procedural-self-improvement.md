---
title: "Procedural Self-Improvement: Skills, Editors, and Harnesses"
category: concepts
tags: [skill-library, meta-agent, harness, self-improvement]
---

## Definition

Procedural self-improvement persists changes to how an agent solves later tasks. Distinguish the **artifact being changed**, the **procedure proposing the change**, and the **external selection/evaluation rule**. Updating a skill document does not imply that its editor learns; editing an agent's code does not imply that its evaluator or outer search loop changes.

## Mechanisms in this wiki

| Paper | Persistent object | Improvement mechanism | Boundary |
|---|---|---|---|
| [[self-improving-agents/zhang-2025-darwin-godel-machine-open-ended]] | Coding-agent implementation | Self-modifying agents and an archive | Foundation weights, archive rules, and parent selection remain fixed |
| [[self-improving-agents/ye-2026-meta-context-engineering-via-agentic]] | Context-engineering skills and resulting context functions | A meta-agent evolves the procedure; a base agent executes it | Fixed outer orchestration; frozen models; online setting uses a fixed skill |
| [[self-improving-agents/wei-2026-evo-harness-context-to-harness]] | General and task-type guidance | Failure reflection followed by consolidation | Frozen solver; the evaluated guidance is natural language |
| [[self-improving-agents/yang-2026-skillforge-evolving-verifiable-skills-for]] | Callable skills and solver weights | Explicit calls, outcome tracking, teacher revision, GRPO | Observable invocation is not causal skill attribution |
| [[self-improving-agents/fu-2026-self-play-meets-skill-evolution]] | Skill bank, challenger and solver weights | Curriculum-memory-policy feedback loop | Fixed distillation, reward, and bank-maintenance procedures |

DGM provides the coding-specific predecessor to Hyperagents; retaining lower-scoring stepping stones differs from monotonic edit promotion. MCE is especially close to the wiki's meta-skill research question because it optimizes a **procedure for constructing context**, not only the resulting memory. Neither paper demonstrates joint RL training of an editable meta-procedure and a CoSkill-style reasoning role. [DGM, p. 4](https://arxiv.org/pdf/2505.22954v1#page=4); [MCE, pp. 5-7](https://arxiv.org/pdf/2601.21557v2#page=5)

Evo-Harness learns guidance across tasks. Its reported regression with self-generated feedback prevents a blanket claim that persisted experience necessarily improves performance. [Evo-Harness, p. 8](https://arxiv.org/pdf/2608.15071v1#page=8)

SkillForge adds explicit invocation and outcome-based maintenance, while SESA lets skill-guided solving alter the future self-play curriculum. These mechanisms are distinct from the learned shared-model editing role in CoSkill. [SkillForge, pp. 4-6](https://arxiv.org/pdf/2608.24747v1#page=4); [SESA, pp. 3-5](https://arxiv.org/pdf/2607.29468v1#page=3); [[self-improving-agents/feng-2026-coskill-joint-reinforcement]]

## Retrieval and optimizer state

[[self-improving-agents/fu-2026-se-gos-self-evolving-graph]] expands the substrate taxonomy: the skill bodies and retrieval code remain unchanged while execution traces alter the graph that retrieval consumes. Its held-out gain remains inside the paper's stated noise band, and its repeated-update experiment shows a later decline. [SE-GoS, pp. 5-7, 10](https://arxiv.org/pdf/2609.08228v1#page=5)

[[self-improving-agents/li-2026-skilladam-stable-and-efficient-skill]] introduces persistent problem/attempt history and a volatility-controlled edit budget. It changes the skill under a fixed update algorithm, whereas MCE evolves a context-building procedure. SkillAdam's cross-model test transfers the final document, not its optimizer state or update algorithm. [SkillAdam, pp. 5-7, 11](https://arxiv.org/pdf/2609.08944v1#page=5)

## Experiment implications

### Consolidation and constrained search

| Paper | Persistent object | Improvement mechanism | Boundary |
|---|---|---|---|
| [[self-improving-agents/gao-2026-experience-funnel-a-state-policy]] | Textual state and policy weights | Validation-gated state updates plus selective distillation into a state-free policy | Fixed selection/consolidation rules; editor learning and cross-domain transfer are not established |
| [[self-improving-agents/zhang-2026-harnesscompass-guiding-automatic-harness-evolution]] | Runtime structure and guidance | Task-agnostic constraints, trace-grounded self-feedback, separate tracks and R3 merging | Fixed outer rules; cross-model reuse within one coding benchmark |
| [[self-improving-agents/lou-2026-autoharness-improving-llm-agents-by]] | Per-game verifier or executable policy | Thompson-sampling program search with environment feedback | A distinct program per game; recursive weight distillation is future work |
| [[self-improving-agents/park-2026-autosaddler-automatic-harness-optimization-with]] | Prompts, tools and middleware | Mini-batch re-execution, structured patching, EvoDAG recombination and development selection | Task-agent memory/skill curation excluded; offline refers to development time |

Experience Funnel already studies the cycle from editable experience to policy consolidation and back to state revision. Thus, simply alternating external skills and policy learning is not a sufficient novelty claim. Its transition-selection mechanism is a useful comparator, but 01+11 filtering alone reduces to updated-state success in the paper's binary analysis. A stronger experiment must distinguish transition-history credit from ordinary success filtering. [PDF pp. 3-7](https://arxiv.org/pdf/2609.08919v1#page=3)

HarnessCompass and AutoSaddler provide designed search procedures that constrain edits and test generalization, distinct from learning the improvement procedure itself. AutoSaddler re-runs candidates; its offline framing must not be read as fixed-log learning. AutoHarness provides the complementary alternative of compiling action constraints or a policy into code instead of modifying model weights. [HarnessCompass pp. 3-6](https://arxiv.org/pdf/2608.01918v1#page=3); [AutoSaddler pp. 4-6](https://arxiv.org/pdf/2608.23041v1#page=4); [AutoHarness pp. 2-6](https://arxiv.org/pdf/2603.03329v1#page=2)

These are wiki inferences from the ingested papers:

- Compare a fixed human procedure, a fixed learned procedure, an externally evolving procedure, and a jointly trained editor before attributing a gain to recursive improvement.
- Cross editor/procedure transfer with skill-bank transfer and solver-weight transfer. Moving all three together cannot identify which transfer worked.
- Evaluate a trained solver with and without its final memory, following SESA's controlled On/Off design; separately account for training-path differences against other solvers.
- Include bank size, retrieval tokens, teacher/proposer cost, verification cost, and regressions alongside task success.

## Operational playbooks and cross-task diagnosis

[[self-improving-agents/li-2026-auto-recsys-harnessing-autonomous-research]] extends procedural memory to multi-day industrial experiments. Execution trajectories revise model-specific playbooks, while experiment outcomes update research history; structured state and shared logs make both usable after session/server failures. Its transfer mechanism reuses playbook organization with interactive filling of new model-specific contents. An observed monitor-code rewrite shows that adaptation can reach orchestration, but does not establish a generally improving meta-procedure. Playbook changes are accepted without a formal validation gate. [PDF pp. 5–10, 12, 14](https://arxiv.org/pdf/2609.10922v1#page=5)

[[self-improving-agents/yue-2026-ecdysis-efficient-and-effective-training]] instead concentrates on the decision before editing: recurring cross-task failures inform sequential diagnostic roles, a consolidated specification, and one coding invocation per nonempty round. A strict aggregate training-score gate precedes frozen evaluation. Singleton failures remain auxiliary evidence, and recurrence is explicitly a heuristic rather than causal proof of a harness defect. The task model, role procedure, and evaluator remain fixed. [PDF pp. 3–7](https://arxiv.org/pdf/2609.11677v1#page=3)

Together these papers strengthen the distinction between **state integrity**, **diagnostic plausibility**, and **empirical promotion**. Atomic writes protect experiment records; recurring failures improve the evidence for a proposed change; a training-score gate tests aggregate behavior. None alone verifies a memory entry's causal explanation or proves transfer of an improvement algorithm. This is a wiki synthesis, not a head-to-head result.

See [[overviews/self-improving-llm-agents]], [[concepts/evaluating-self-improvement]], and [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].
