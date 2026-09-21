---
title: "Evaluating Self-Improvement: Feedback, Selection, and Transfer"
category: concepts
tags: [evaluation, transfer, harness, self-improvement]
---

## What must be separated

An improvement loop can improve development scores, generalize to new tasks, transfer between models, or improve the procedure that generates future improvements. These are separate claims. The relevant experimental unit may be a candidate harness, a task, a stream, a continuous episode, or an independently trained system.

## Evidence boundaries

| Paper | What the protocol supports | What it does not establish |
|---|---|---|
| [[self-improving-agents/xu-2026-adapting-the-interface-not-the]] | Training-derived environment harnesses frozen for held-out tasks and reused across 17 additional models | Transfer to an entirely new environment, or a learned editor |
| [[self-improving-agents/zhang-2026-self-harness-harnesses-that-improve]] | Same-model edit generation with two-split regression gates | Untouched-test generalization: the held-out score participates in edit acceptance |
| [[self-improving-agents/karten-2026-prime-agent-a-self-improving]] | Persistent runtime operation and mixed within-model end-to-end comparisons | A causal attribution of the external ARC headline comparison to self-improvement alone |

Life-Harness makes the training/test boundary explicit: final interventions are frozen, although the runtime still reacts to the current episode. Its cross-model evidence is within the learned environment interfaces. [pp. 2, 7](https://arxiv.org/pdf/2605.22166v1#page=7)

Self-Harness hides regression tasks from the proposer but repeatedly uses their scores in its promotion gate. The gate is part of the optimizer. Its reported 40.5% to 61.9% MiniMax result therefore concerns a selection-exposed split, even though the authors call it held out. A third untouched test would assess selection generalization. [Algorithm 1, p. 4; Section 3.4, p. 7; Figure 4, p. 9](https://arxiv.org/pdf/2606.09498v1#page=4)

Prime Agent explicitly describes ARC reference scores as external, since its own native-harness reruns underperformed published scores. The headline comparison combines different evaluation configurations. Table 1 also contains losses and no uncertainty intervals. These limitations matter when using the system as evidence for a learned refinement mechanism. [p. 7](https://arxiv.org/pdf/2608.23552v1#page=7)

## Recommendations derived from the papers

### Additional full-text controls

[[self-improving-agents/gao-2026-experience-funnel-a-state-policy]] separates training, selection validation, and test reporting, and measures consolidated policies with full, residual, or no state. It does not demonstrate a single learned procedure transferred between environments. Its main SearchQA value (62.4%) differs from the ablation value (63.6%), without a clear protocol reconciliation; repeated-run uncertainty is promised but absent from displayed final tables. Preserve these discrepancies rather than pool the figures. [PDF pp. 5-7](https://arxiv.org/pdf/2609.08919v1#page=5)

[[self-improving-agents/zhang-2026-harnesscompass-guiding-automatic-harness-evolution]] has 50 evolution tasks and 450 untouched tasks; 54% to 66% is the evolution-set headline, whereas the held-out comparison is 51.6% to 60.4%. The cumulative feedback ablation regresses on held-out tasks before merging recovers it. Five versus twenty search turns is not an equal-compute result because each turn can involve different candidate and feedback work. [PDF pp. 5-6](https://arxiv.org/pdf/2608.01918v1#page=5)

[[self-improving-agents/lou-2026-autoharness-improving-llm-agents-by]] separates legal-action testing over 145 environments from strategic performance on 32 games and complete code-policy evaluation on 16 games. Its generated policies are environment-specific, and finite rollout legality is not a proof of universal validity. [PDF pp. 3-6](https://arxiv.org/pdf/2603.03329v1#page=3)

[[self-improving-agents/park-2026-autosaddler-automatic-harness-optimization-with]] provides group-disjoint evaluation for GAIA2 and SWE-Bench Pro, but only random task holdout for Terminal-Bench 2.0. Three test executions are not three optimizer runs. Its tables imply base gains of 9.0/9.6/10.0 points, while Section 5.2 contains arithmetic mistakes; retain table endpoints and recompute deltas explicitly. [PDF pp. 7-8, 20-21](https://arxiv.org/pdf/2608.23041v1#page=7)

1. Reserve final tasks from proposal feedback, score-based selection, early stopping, and regression acceptance. Report selection-exposed results separately.
2. For online task streams, score each task before its feedback changes later behavior. Test different stream orders and clean restarts; report adaptation as such.
3. Distinguish transferred artifacts from transferred algorithms. Preserve an unchanged evaluator and task distribution while estimating an editor's learning-to-improve ability.
4. Match total expenditure, including failed proposals, teachers, replay verification, and descendant agents. Report quality-cost curves when one scalar budget cannot match all resources.
5. Record harmful updates and uncertainty across independent searches or training runs, not just the best candidate's benchmark score.

## Post-training compatibility controls

[[self-improving-agents/yu-2026-co-evolving-harnesses-and-models]] shows why a harness-transfer result cannot substitute for evaluating post-training under that harness. Whole-trajectory expert imitation harms all seven Qwen tasks despite upward harness reuse by the teacher. Localized corrections recover most of the loss, but +1.7 aggregate points includes two small regressions and lacks a reported paired significance test. Evaluate the same model update under both base and evolved harnesses; then compare matched student-state and whole-trajectory supervision. These are design inferences, not universal guarantees. [Table 1, PDF p. 5](https://arxiv.org/pdf/2609.09134v1#page=5)

Its LLM-judge planning-defect shares are conditioned on failed rollouts, and the prose overall failure rates have an unreconciled denominator relative to task means. Keep outcome scores, failure composition and causal mechanism claims separate. An under-one-hour SFT run is not total adaptation cost. [Table 3 and Appendices B-D, PDF pp. 6-10](https://arxiv.org/pdf/2609.09134v1#page=6)

## Operational adaptation and diagnostic evidence

[[self-improving-agents/li-2026-auto-recsys-harnessing-autonomous-research]] reports a 31-iteration, one-model trajectory: operational fixes fall 4.0 → 1.3, rise after a baseline change, then recover to 0.5 with 5/6 late iterations requiring no operational fix. Implementation debugging is excluded. No controlled component ablation separates playbook maturation from human assistance, task mix, or infrastructure changes. Human-attention savings and a longest autonomous session are observations, not a controlled scientific-quality result. [PDF pp. 10–13](https://arxiv.org/pdf/2609.10922v1#page=10)

[[self-improving-agents/yue-2026-ecdysis-efficient-and-effective-training]] uses training-only acceptance followed by frozen evaluation on 20 test tasks per τ² subset, each with three reset trials, and reuses evolved harnesses across five models. Its 18.56% headline is relative improvement across three datasets (58.67% → 69.56%); the two-τ²-domain mean is 46.67% → 59.33%. Full FDCR's maximum 1.84× training speedup is distinct from aggregation-only's 3.23×. The quarter-data example has lower accuracy and Pass^3 than full data despite much lower reported cost. [PDF pp. 6–9, 12, 18–19](https://arxiv.org/pdf/2609.11677v1#page=6)

Additional controls suggested by these papers are to count human interventions and operational fixes separately from task/scientific success, distinguish transferred templates from transferred contents or algorithms, and test failure-attribution labels with counterfactual repairs. Report repeated independent optimization runs as well as repeated task trials. A fresh rollout on a training task remains selection evidence; an ungated memory update remains ungated even when stored through deterministic code. These are wiki recommendations, not experiments performed by either paper.

The existing seed review already identifies related limits in [[self-improving-agents/lee-2026-meta-harness-end-to-end]], [[self-improving-agents/hebbar-2026-sia-self-improving-ai]], and [[self-improving-agents/zhang-2026-hyperagents]]. See [[overviews/self-improving-llm-agents]] and [[concepts/procedural-self-improvement]] for the mechanism comparison.
