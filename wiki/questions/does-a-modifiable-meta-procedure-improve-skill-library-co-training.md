---
title: "Does a modifiable meta-procedure improve skill-library co-training?"
category: questions
tags: [self-improving-agents, harness, skill-library]
---

## Question
Would combining Hyperagents' editable meta-agent
procedure with CoSkill's joint Meta-Skill-Agent/Reasoning-Agent RL
training outperform either approach alone?

## Sharper follow-up
Specifically: would an editable procedure for proposing, diagnosing, or
selecting CoSkill-style skill edits improve adaptation to an unseen
skill-library environment under a matched budget? Changing the RL
objective itself is a separate, stronger intervention, not something
required by Hyperagents' reported mechanism. Hold external scoring and
test selection fixed to isolate the benefit of the editable procedure.
This is a proposed experiment, not an established finding in this wiki.

## What the knowledge base holds
- [[overviews/self-improving-llm-agents]] — [[zhang-2026-hyperagents]]
  tests transfer from joint paper-review/robotics runs to math grading.
  During imp@50, the transferred meta-agent is fixed while it generates
  new task agents. Both task and meta implementations are transferred,
  and main parent-selection/evaluation rules remain fixed. This is not
  an all-pairs transfer experiment or a self-rewriting RL optimizer.
  [§§3, 5.2, pp. 5, 9-11](https://arxiv.org/pdf/2603.19461v1#page=9)
- [[feng-2026-coskill-joint-reinforcement]] jointly trains reasoning and
  editing roles in one shared actor. Its fixed protocol stages local
  edits, verifies them by task replay, and updates weights with GiGPO.
  Removing editor RL removes its objective, not all shared-weight
  adaptation. Separate ALFWorld/WebShop runs do not test editor transfer.
  [§§3-4 and Appendix G, pp. 3-9, 20](https://arxiv.org/pdf/2609.04865v1#page=3)
- Neither paper evaluates the other's setting, so there is no direct
  evidence in this wiki either way.

## Tentative answer
Unknown — no paper in this wiki tests this combination directly. This is a
candidate direction to flag if/when a paper explicitly combining
self-editable meta-procedures with skill-library co-training is ingested.

The full text narrows the analogy without resolving the question.
Hyperagents provides evidence for transferred agent-generation ability,
but its 200-iteration compounding endpoint is not significantly better
than initialization without transfer. CoSkill provides within-environment
co-training ablations, not cross-domain evidence. A clean test would
separately transfer the editor/procedure while holding task initialization,
total training and verification budgets, and test exposure constant.
These controls are this wiki's inference from the reported limitations.
[Hyperagents, §§5.2-5.3, pp. 10-13](https://arxiv.org/pdf/2603.19461v1#page=10);
[CoSkill, Table 2/Appendix F, pp. 8, 20](https://arxiv.org/pdf/2609.04865v1#page=8)

## September 11, 2026 UTC evidence update

The answer to the exact joint-training question remains unknown, but the novelty boundary is narrower:

- [[self-improving-agents/ye-2026-meta-context-engineering-via-agentic]] already evolves a reusable context-building procedure with a base executor and fixed model weights. Any claim of first learning the procedure behind skill/context construction must account for it. [pp. 5-7](https://arxiv.org/pdf/2601.21557v2#page=5)
- [[self-improving-agents/yang-2026-skillforge-evolving-verifiable-skills-for]] makes invocation observable and maintains skills using outcomes, but its teacher/editor is fixed. This does not establish the proposed jointly learned meta-procedure. [SkillForge, pp. 4-6](https://arxiv.org/pdf/2608.24747v1#page=4)
- [[self-improving-agents/fu-2026-self-play-meets-skill-evolution]] adds an especially useful evaluation control: the same learned solver with memory disabled versus enabled. This separates deployment retrieval from gains carried in weights, although it does not alone isolate all training mechanisms. [p. 6](https://arxiv.org/pdf/2607.29468v1#page=6)
- [[self-improving-agents/li-2026-skilladam-stable-and-efficient-skill]] offers a strong fixed stateful editor, and [[self-improving-agents/fu-2026-se-gos-self-evolving-graph]] offers a retrieval-only adaptation control. Both are relevant alternatives to changing the learned editing policy. [SkillAdam, pp. 6-7](https://arxiv.org/pdf/2609.08944v1#page=6); [SE-GoS, pp. 5-7](https://arxiv.org/pdf/2609.08228v1#page=5)

A sharper proposed experiment compares a fixed learned procedure, a fixed stateful editor, an evolving procedure, and CoSkill-style joint training under matched total budgets. Transfer the editor separately from the skill bank and solver weights into a disjoint environment. Keep final task scores out of edit selection, measure negative transfer and repeated-update degradation, and include memory-off evaluation. These are research-design inferences from [[concepts/procedural-self-improvement]] and [[concepts/evaluating-self-improvement]], not claims that the combination is novel across all unreviewed literature.
