---
title: "Self-Improving LLM Agents: Harnesses, Meta-Agents, and Skill Libraries"
category: overviews
tags: [self-improving-agents, harness, meta-agent, skill-library]
---

## Summary
A growing line of 2026 work argues that a large fraction of an LLM
agent's usable capability lives outside the frozen model weights — in the
harness/scaffold, the meta-level procedure that modifies the agent, or the
skill library it draws on — and that these components should themselves be
learned or searched over, rather than hand-engineered once and frozen.
Four papers currently in this wiki each attack a different piece of that
idea.

Full-text review: September 8, 2026; all four seed PDFs are present. The
revisions below replace only interpretations changed or qualified by the
full text. See the [claim-change record](../../logs/reports/2026-09-08-seed-pdf-upgrade.md).

## Papers surveyed here

- [[self-improving-agents/lee-2026-meta-harness-end-to-end]]
  (Meta-Harness) — optimizes the harness alone via an agentic proposer
  with selective access to historical source, scores, and execution traces.
  Its trace-access ablation supports this interface; the introductory 6x
  harness gap is cited motivation, not its own experiment. The 10M-token
  diagnostic store is not a single consumed context.
  [§3, pp. 4-5; Table 3, p. 7](https://arxiv.org/pdf/2603.28052v1#page=4)
- [[self-improving-agents/zhang-2026-hyperagents]] (Hyperagents /
  DGM-Hyperagents) — makes the *meta-level
  modification procedure itself* modifiable by fusing task agent and
  meta-agent into one self-editing program. Main experiments retain fixed
  foundation models, parent selection, and evaluation; transfer is tested
  from joint paper-review/robotics runs to math grading, not among all
  four domains. [§§3, 5.2, pp. 5, 9-11](https://arxiv.org/pdf/2603.19461v1#page=9)
- [[self-improving-agents/hebbar-2026-sia-self-improving-ai]] (SIA) —
  combines harness revision with model *weight* updates (RL + LoRA) in one
  loop, via a Meta-Agent/Task-Agent/Feedback-Agent split. Adding weight
  updates after harness search improves the three reported tasks; no
  weight-only control establishes that the combination beats either
  lever alone. The selector remains a frozen LLM.
  [Table 3, p. 11; §9, p. 13](https://arxiv.org/pdf/2605.27276v2#page=11)
- [[self-improving-agents/feng-2026-coskill-joint-reinforcement]]
  (CoSkill) — applies the same "stop freezing the meta-level component"
  idea to hierarchical skill libraries, jointly training Meta-Skill and
  Reasoning roles in a shared model. Staged edits are verified through
  task re-execution before promotion; edit operations, verification, and
  the GiGPO objective remain fixed. CoSkill includes weight updates.
  [§3, pp. 3-6](https://arxiv.org/pdf/2609.04865v1#page=3)

## Cross-cutting observations
- All four treat some component that is conventionally hand-designed once
  and left static (harness, meta-modification procedure, or skill
  workflow) as an object that should itself be optimized during training
  or deployment.
- Meta-Harness and SIA are mechanistically related, but not a matched
  head-to-head experiment. SIA explicitly discusses Meta-Harness and
  Hyperagents and reports prior comparator scores. Yet its LawBench
  setup describes 191 classes and solution-script rollouts, versus
  Meta-Harness's 215-class description. SIA also describes using test-split
  scores as RL feedback. Its incremental gains therefore do not establish
  independent generalization superiority over Meta-Harness.
  [SIA, §§4.1, 6.1-6.3, pp. 4, 8-9](https://arxiv.org/pdf/2605.27276v2#page=9);
  [Meta-Harness, §4.1, p. 6](https://arxiv.org/pdf/2603.28052v1#page=6)
- Hyperagents and CoSkill expose different improvement mechanisms:
  editable meta-agent code versus a learned skill-editing policy under
  fixed training rules. Combining them is a plausible research hypothesis,
  not demonstrated compatibility or superiority. Hyperagents' transferred
  meta-agent is frozen during imp@50, and both task and meta code are
  carried over. Its 200-iteration transfer advantage (0.640 vs 0.610) is
  not statistically significant. CoSkill reports separate environment
  training, not cross-environment editor transfer.
  [Hyperagents, §§5.2-5.3, pp. 9-13](https://arxiv.org/pdf/2603.19461v1#page=9);
  [CoSkill, §4, pp. 6-9](https://arxiv.org/pdf/2609.04865v1#page=6)
- Evidence of transfer must be separated from optimization against a
  benchmark: Meta-Harness holds out classification/math problems, but
  uses the same 89 TerminalBench-2 tasks for search and final evaluation.
  Its math experiment evaluates five models, only four of which were
  absent from search. CoSkill's main baselines largely use prior reported
  values, with protocol ambiguities documented in its source note. The
  four papers do not support a common controlled performance ranking.
  [Meta-Harness, §§4.2-4.3, pp. 8-9](https://arxiv.org/pdf/2603.28052v1#page=8);
  [CoSkill, Table 1 and Appendices E-F, pp. 7, 19-20](https://arxiv.org/pdf/2609.04865v1#page=7)

## Open questions
- Would combining Hyperagents' editable meta-agent procedure with
  CoSkill's joint skill-library RL training outperform either alone? See
  [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]]
  for the PDF-grounded scope and remaining uncertainty.
