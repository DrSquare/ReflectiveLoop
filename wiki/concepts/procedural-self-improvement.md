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

These are wiki inferences from the ingested papers:

- Compare a fixed human procedure, a fixed learned procedure, an externally evolving procedure, and a jointly trained editor before attributing a gain to recursive improvement.
- Cross editor/procedure transfer with skill-bank transfer and solver-weight transfer. Moving all three together cannot identify which transfer worked.
- Evaluate a trained solver with and without its final memory, following SESA's controlled On/Off design; separately account for training-path differences against other solvers.
- Include bank size, retrieval tokens, teacher/proposer cost, verification cost, and regressions alongside task success.

See [[overviews/self-improving-llm-agents]], [[concepts/evaluating-self-improvement]], and [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].
