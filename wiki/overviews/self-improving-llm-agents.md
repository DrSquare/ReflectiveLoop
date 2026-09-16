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
Five legacy paper records in this wiki each attack a different piece of
that idea. Their comparisons below remain abstract-based pending separate
PDF upgrades. The sixth entry, Stellar Colosseum, is grounded in an exact
PDF and adds an inference-time orchestration comparator.

## PDF-grounded comparator: research-state refinement

[[self-improving-agents/lin-2026-stellar-colosseum-a-many-agent]] adds a designed
workflow that improves the current proof and its supporting research state:
strategy readiness gates precede dependency-aware decomposition, candidate
critiques survive overlapping aggregation, and localized verifier findings
support section repair or renewed exploration. A knowledge directory retains
useful results and failed routes with evidence and caveats. This broadens the
comparison beyond changing harness code or weights; refining an artifact is
not itself evidence of a learned or self-editable improvement procedure.
[PDF §§4.1-4.3, pp. 6-9](https://arxiv.org/pdf/2609.15983v2#page=6)

Its 71.0% TCS-Bench result uses selection between two harness runs, with a
reference-assisted automated grader. Its proof-to-Codeforces adaptation adds
a terminal C++ implementation task and execution probe, obtaining 218/222
accepted programs against hidden final tests. These are different validation
regimes, and neither comparison isolates orchestration benefits at matched
compute. Adaptive allocation and model training from validated trajectories
are proposed future work. Thus the paper strengthens the case for retaining
structured negative feedback during long tasks, while leaving the
[[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]]
question unanswered.
[PDF §§6-8, pp. 13-17](https://arxiv.org/pdf/2609.15983v2#page=13)

## Legacy papers surveyed from abstracts

- [[self-improving-agents/lee-2026-meta-harness-end-to-end]]
  (Meta-Harness) — optimizes the harness alone via an agentic proposer
  with full historical context (source, scores, execution traces),
  showing harness choice alone can swing performance up to 6x.
- [[self-improving-agents/park-2026-autosaddler-automatic-harness-optimization-with]]
  (AutoSaddler) — attacks the same harness axis as Meta-Harness but
  offline: it diagnoses failure traces in mini-batches, emits structured
  code patches to the harness, and keeps only validation-approved
  updates, reporting +9.0/+9.6/+10.0 points on GAIA2, SWE-Bench Pro, and
  Terminal-Bench 2.0.
- [[self-improving-agents/zhang-2026-hyperagents]] (Hyperagents /
  DGM-Hyperagents) — goes one level up, making the *meta-level
  modification procedure itself* modifiable by fusing task agent and
  meta-agent into one self-editing program, generalizing recursive
  self-improvement beyond coding.
- [[self-improving-agents/hebbar-2026-sia-self-improving-ai]] (SIA) —
  combines harness revision with model *weight* updates (RL + LoRA) in one
  loop, via a Meta-Agent/Task-Agent/Feedback-Agent split, showing the two
  update types are complementary rather than substitutes.
- [[self-improving-agents/feng-2026-coskill-joint-reinforcement]]
  (CoSkill) — applies the same "stop freezing the meta-level component"
  idea to hierarchical skill libraries, jointly training a learnable
  Meta-Skill Agent with a Reasoning Agent under RL.

## Legacy cross-cutting observations (awaiting PDF upgrades)
- All five treat some component that is conventionally hand-designed once
  and left static (harness, meta-modification procedure, or skill
  workflow) as an object that should itself be optimized during training
  or deployment.
- AutoSaddler sits on the same harness axis as Meta-Harness and
  strengthens rather than contradicts its claim that harness optimization
  alone buys large gains; it adds that the update signal should come from
  diagnosed failure traces and be gated on validation so it generalizes.
  It narrows Meta-Harness's emphasis on very large in-context histories,
  reporting comparable-magnitude gains from offline mini-batch updates
  instead. No existing claim in this wiki is replaced.
- Meta-Harness and the harness-revision arm of SIA are directly
  comparable: SIA's results suggest that adding weight updates on top of
  harness optimization gives further gains beyond what harness search
  alone (à la Meta-Harness) achieves.
- Hyperagents' contribution is one level more abstract than the other
  four: instead of picking *which* component to make learnable (harness,
  weights, or skill library), it makes the *procedure that decides how to
  self-modify* itself modifiable, which is compatible with pairing it with
  any of Meta-Harness/SIA/CoSkill's specific update mechanisms.
- None of the five papers report results against each other directly —
  the synthesis above is this wiki's own comparison drawn from ingesting
  their abstracts/summaries, so it should be revisited once the full PDFs
  are ingested.

## Open questions
- Would combining Hyperagents' fully self-editable meta-procedure with
  CoSkill's joint skill-library RL training outperform either alone? See
  [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]]
  once written.
