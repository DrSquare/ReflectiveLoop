---
title: "Does a modifiable meta-procedure improve skill-library co-training?"
category: questions
tags: [self-improving-agents, harness, skill-library]
---

## Question
Would combining Hyperagents' fully self-editable meta-modification
procedure with CoSkill's joint Meta-Skill-Agent/Reasoning-Agent RL
training outperform either approach alone?

## Sharper follow-up
Specifically: if CoSkill's Meta-Skill Agent were itself allowed to rewrite
its own update rule (Hyperagents-style), rather than being trained with a
fixed RL objective, would the resulting system show the same kind of
cross-domain transfer that DGM-Hyperagents reports for coding, peer
review, robotics reward design, and math grading — but for skill-library
tasks like ALFWorld/WebShop?

## What the knowledge base holds
- [[overviews/self-improving-llm-agents]] — [[zhang-2026-hyperagents]]
  makes the meta-level modification procedure itself modifiable, and
  reports transfer across coding, peer review, robotics reward design, and
  math grading.
- [[feng-2026-coskill-joint-reinforcement]] jointly trains a learnable
  Meta-Skill Agent with a Reasoning Agent via RL, but the Meta-Skill
  Agent's own update rule is fixed by the RL training procedure, not
  self-editable.
- Neither paper evaluates the other's setting, so there is no direct
  evidence in this wiki either way.

## Tentative answer
Unknown — no paper in this wiki tests this combination directly. This is a
candidate direction to flag if/when a paper explicitly combining
self-editable meta-procedures with skill-library co-training is ingested.
