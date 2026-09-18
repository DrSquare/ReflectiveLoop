---
title: "Self-Improving LLM Agents: Harnesses, Meta-Agents, and Skill Libraries"
category: overviews
tags: [self-improving-agents, harness, meta-agent, skill-library]
---

## Summary
A growing line of work argues that a large fraction of an LLM
agent's usable capability lives outside the frozen model weights — in the
harness/scaffold, the meta-level procedure that modifies the agent, or the
skill library it draws on — and that these components should themselves be
learned or searched over, rather than hand-engineered once and frozen.
Twenty-one papers currently in this wiki cover different parts of that idea,
including the September 11 scans, the September 12 additions of Auto-RecSys and
Ecdysis, and the September 16 addition of Stellar Colosseum.

Seed full-text review: September 8, 2026; all four seed PDFs are present.
Expanded review: September 11, 2026 UTC; all ten new PDFs are present. The
revisions below replace only interpretations changed or qualified by the
full text. See the [claim-change record](../../logs/reports/2026-09-08-seed-pdf-upgrade.md).

## Research-state refinement as an inference-time comparator

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

## Seed papers

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

## Cross-cutting observations from the seed review
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

## Expanded literature: harnesses, skills, and systems

This is a curated expansion, not an exhaustive survey. Each linked page identifies its pinned PDF version, method, reported results, evaluation boundary, and implementation provenance. Recent additions appear first.

| Paper | First submission | What it adds |
|---|---|---|
| [[self-improving-agents/li-2026-skilladam-stable-and-efficient-skill]] (SkillAdam) | 2026-09-08 | SkillAdam uses persistent issue history and an adaptive edit budget to stabilize optimization of natural-language skill documents around frozen models. |
| [[self-improving-agents/fu-2026-se-gos-self-evolving-graph]] (SE-GoS) | 2026-09-08 | SE-GoS evolves the graph and descriptions used to retrieve existing skills, while preserving skill content, model weights, and the retrieval algorithm. |
| [[self-improving-agents/yang-2026-skillforge-evolving-verifiable-skills-for]] (SkillForge) | 2026-08-25 | SkillForge makes skill invocation explicit in agent trajectories and revises skills using usage outcomes while training the policy with GRPO. |
| [[self-improving-agents/karten-2026-prime-agent-a-self-improving]] (Prime Agent) | 2026-08-24 | Prime Agent packages a persistent REPL, recursive agent sessions, and versioned harness state into a runtime for long-horizon reasoning and execution. |
| [[self-improving-agents/wei-2026-evo-harness-context-to-harness]] (Evo-Harness) | 2026-08-15 | Evo-Harness compiles failed one-shot task executions into reusable general and task-type guidance for a frozen solver operating on a task stream. |
| [[self-improving-agents/fu-2026-self-play-meets-skill-evolution]] (SESA) | 2026-07-31 | SESA couples search self-play to an evolving skill bank, allowing skill-conditioned learning to improve both model parameters and optional inference-time memory. |
| [[self-improving-agents/zhang-2026-self-harness-harnesses-that-improve]] (Self-Harness) | 2026-06-08 | Self-Harness uses the same frozen model to solve tasks and propose bounded changes to its own harness, with regression scores deciding which edits survive. |
| [[self-improving-agents/xu-2026-adapting-the-interface-not-the]] (Life-Harness) | 2026-05-21 | Life-Harness turns training-trajectory failures into reusable runtime interventions and freezes the resulting harness for held-out evaluation across model backbones. |
| [[self-improving-agents/ye-2026-meta-context-engineering-via-agentic]] (MCE) | 2026-01-29 | MCE evolves the instructions and code that build context, then executes those skills to produce context artifacts, while keeping model weights frozen. |
| [[self-improving-agents/zhang-2025-darwin-godel-machine-open-ended]] (Darwin Godel Machine) | 2025-05-29 | The Darwin Godel Machine evolves a population of coding agents that modify their own implementations, retaining useful stepping stones under empirical evaluation. |

## Interpretations changed by the expansion

**Learning the procedure is already a concrete research direction.** MCE evolves the skill that constructs context, and DGM lets coding agents improve their own implementations. The broad proposal to optimize an improvement procedure is therefore insufficient as a novelty claim. The remaining question concerns what joint editor/reasoner training and controlled cross-environment transfer add beyond these mechanisms. [MCE, pp. 5-7](https://arxiv.org/pdf/2601.21557v2#page=5); [DGM, p. 4](https://arxiv.org/pdf/2505.22954v1#page=4)

**Persistent improvement has several substrates.** SkillForge and SESA change skills alongside trained policies. SE-GoS instead changes retrieval topology, weights, and descriptions without editing the skill bodies. SkillAdam changes a skill document under a fixed stateful optimization rule. These should occupy separate cells in an experimental design. [SkillForge, pp. 4-6](https://arxiv.org/pdf/2608.24747v1#page=4); [SESA, pp. 3-5](https://arxiv.org/pdf/2607.29468v1#page=3); [SE-GoS, pp. 5-7](https://arxiv.org/pdf/2609.08228v1#page=5); [SkillAdam, pp. 5-7](https://arxiv.org/pdf/2609.08944v1#page=5)

**Continued editing can hurt.** Evo-Harness reports degradation with self-generated feedback; SE-GoS drops after additional evolution rounds. SkillAdam's memory and bounded edits address a related stability problem, but its Adam analogy does not establish convergence. [Evo-Harness, p. 8](https://arxiv.org/pdf/2608.15071v1#page=8); [SE-GoS, p. 10](https://arxiv.org/pdf/2609.08228v1#page=10); [SkillAdam, pp. 6-7](https://arxiv.org/pdf/2609.08944v1#page=6)

**Transfer evidence has different strengths.** Life-Harness freezes training-derived interventions before testing additional models. Self-Harness uses its held-out scores in edit selection. SE-GoS provides a disjoint split but explicitly places its +5.4-point gain inside the noise band. Prime Agent's external ARC reference comparison is not a controlled harness-effect estimate. The expanded literature does not support a single performance ranking. [Life-Harness, p. 7](https://arxiv.org/pdf/2605.22166v1#page=7); [Self-Harness, p. 7](https://arxiv.org/pdf/2606.09498v1#page=7); [SE-GoS, p. 10](https://arxiv.org/pdf/2609.08228v1#page=10); [Prime Agent, p. 7](https://arxiv.org/pdf/2608.23552v1#page=7)

See [[concepts/procedural-self-improvement]] for mechanism definitions, [[concepts/evaluating-self-improvement]] for evaluation requirements, and [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]] for the narrowed research question.

## Additional evidence from the September 11 scan

| Paper | Contribution to the synthesis | Important boundary |
|---|---|---|
| [[self-improving-agents/gao-2026-experience-funnel-a-state-policy]] | Alternates textual experience and selective policy consolidation | Does not establish learned-editor transfer; main and ablation scores need reconciliation |
| [[self-improving-agents/zhang-2026-harnesscompass-guiding-automatic-harness-evolution]] | Constrained changes and separate component tracks improve a frozen harness | Search-set headline differs from held-out evidence; cumulative feedback ablation can regress |
| [[self-improving-agents/lou-2026-autoharness-improving-llm-agents-by]] | Compiles action legality or entire policies into programs | Each game gets a separate harness; finite legality testing is not a proof |
| [[self-improving-agents/park-2026-autosaddler-automatic-harness-optimization-with]] | Development-time mini-batch patch search with historical recombination | Re-executes candidates; task-agent skill curation is excluded; narrative deltas contain arithmetic errors |

Experience Funnel narrows novelty further: alternating editable state with parametric consolidation is already demonstrated as a proposed method on the target classes of environments. The remaining research question must isolate the learned editor, transition-specific credit, and separately transferred components. The paper does not establish cross-domain transfer merely by training in several domains. [PDF pp. 3-7](https://arxiv.org/pdf/2609.08919v1#page=3)

HarnessCompass supplies 450 untouched coding tasks and frozen cross-model reuse; AutoSaddler supplies group-disjoint GAIA2 and repository-disjoint SWE-Bench Pro tests. These are stronger controls than repeatedly selecting on a nominal held-out score, but neither learns the evaluator or proves arbitrary domain transfer. AutoHarness instead synthesizes a domain-specific executable constraint or policy; distillation into model weights is future work. [HarnessCompass pp. 5-6](https://arxiv.org/pdf/2608.01918v1#page=5); [AutoSaddler pp. 7, 20](https://arxiv.org/pdf/2608.23041v1#page=20); [AutoHarness pp. 3-6](https://arxiv.org/pdf/2603.03329v1#page=3)

The AutoSaddler full text replaces the abstract-only interpretation on main: offline means development-time optimization with fresh executions, not fixed-log training. Its stated search space excludes task-agent memory and skill curation. Table endpoints imply gains of 9.0, 9.6, and 10.0 points over base harnesses; Section 5.2's inconsistent arithmetic is not propagated. [PDF pp. 4-8, 44](https://arxiv.org/pdf/2608.23041v1#page=4)

## September 12 additions: persistent research and failure diagnosis

[[self-improving-agents/li-2026-auto-recsys-harnessing-autonomous-research]] (Auto-RecSys; September 10 submission) connects evolving execution playbooks and research history to persistent multi-server experimentation. It adds evidence for reduced operational recovery over 31 iterations on one model, including regression after a baseline change and subsequent recovery. Reusing a playbook template with human-assisted filling differs from cross-model insight transfer; formal playbook validation and scientific-quality attribution remain open. [PDF pp. 6–7, 10–14](https://arxiv.org/pdf/2609.10922v1#page=10)

[[self-improving-agents/yue-2026-ecdysis-efficient-and-effective-training]] (Ecdysis; September 10 submission) groups failures across tasks, uses diagnostic roles before code edits, and accepts aggregate training improvements before frozen held-out/model-transfer evaluation. It supports aggregation as a useful designed improvement procedure under a common Life-Harness initialization. Its 18.56% gain is relative across three datasets; its data-reduction claim is a single-cell tradeoff, and cross-task recurrence does not prove causal attribution. [PDF pp. 3–9, 19](https://arxiv.org/pdf/2609.11677v1#page=3)

These papers broaden operational and diagnostic controls without resolving the Hyperagents/CoSkill joint-training question. Auto-RecSys supplies an observed orchestration rewrite; Ecdysis fixes the diagnostic roles and task weights. Neither demonstrates joint training of a modifiable improvement procedure and skill-editing/reasoning roles with controlled cross-domain transfer. See the updated mechanism and evaluation concepts for the distinct evidence boundaries.
