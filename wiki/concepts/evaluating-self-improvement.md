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

1. Reserve final tasks from proposal feedback, score-based selection, early stopping, and regression acceptance. Report selection-exposed results separately.
2. For online task streams, score each task before its feedback changes later behavior. Test different stream orders and clean restarts; report adaptation as such.
3. Distinguish transferred artifacts from transferred algorithms. Preserve an unchanged evaluator and task distribution while estimating an editor's learning-to-improve ability.
4. Match total expenditure, including failed proposals, teachers, replay verification, and descendant agents. Report quality-cost curves when one scalar budget cannot match all resources.
5. Record harmful updates and uncertainty across independent searches or training runs, not just the best candidate's benchmark score.

The existing seed review already identifies related limits in [[self-improving-agents/lee-2026-meta-harness-end-to-end]], [[self-improving-agents/hebbar-2026-sia-self-improving-ai]], and [[self-improving-agents/zhang-2026-hyperagents]]. See [[overviews/self-improving-llm-agents]] and [[concepts/procedural-self-improvement]] for the mechanism comparison.
