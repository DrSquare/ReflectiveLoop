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
This is a proposed experiment, not a finding from the four papers.

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
