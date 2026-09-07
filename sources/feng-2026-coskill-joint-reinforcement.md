---
title: "CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution"
authors: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu
year: 2026
doi: arXiv:2609.04865
category: [self-improving-agents]
pdf_path: /papers/feng-2026-coskill-joint-reinforcement.pdf
pdf_filename: feng-2026-coskill-joint-reinforcement.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
---

## One-line Summary
CoSkill jointly trains a learnable Meta-Skill Agent and a Reasoning Agent
in a unified multi-agent RL framework, turning a previously static
meta-skill workflow into something that co-adapts with the reasoning
policy, instead of treating skill libraries as passive, frozen artifacts.

## 1. Document Information
- arXiv: 2609.04865, submitted September 2026.

## 2. Key Contributions
- Identifies that prior skill-library approaches either keep skill
  evolution separate from policy optimization, or treat meta-skills as
  fixed/unchangeable workflows — limiting adaptability.
- Introduces a unified multi-agent RL framework where the meta-skill
  workflow becomes a learnable Meta-Skill Agent.
- Jointly trains the Meta-Skill Agent and a Reasoning Agent against a
  hierarchical skill library, enabling end-to-end co-adaptation.

## 3. Methodology and Architecture
Two agents are trained together under RL: a Reasoning Agent that solves
tasks, and a Meta-Skill Agent that maintains and evolves a hierarchical
skill library used by the Reasoning Agent. Because the Meta-Skill Agent is
itself learnable (rather than a fixed workflow), the skill library can
co-adapt with the reasoning policy during training.

## 4. Key Results and Benchmarks
- ALFWorld: 98.4% success rate (+3.5 points over baselines).
- WebShop: 90.6% success rate (+6.2 points over baselines).
- Reports superior early-stage sample efficiency, better final
  performance, and faster wall-clock efficiency than prior skill-based and
  RL baselines.

## 5. Limitations and Future Work
- Evaluated on ALFWorld and WebShop; generalization to broader classes of
  embodied/web agent tasks is not yet demonstrated.
- Joint training of two agents adds RL optimization complexity relative to
  single-agent baselines.

## 6. Related Work
- Complements [[zhang-2026-hyperagents]] (Hyperagents) and
  [[hebbar-2026-sia-self-improving-ai]] (SIA): all three move a
  traditionally fixed component (meta-level procedure, harness, or skill
  workflow) into something learnable/self-modifying, but CoSkill applies
  this specifically to hierarchical skill libraries via joint multi-agent
  RL rather than harness or weight rewriting.

## 7. Glossary
- **Meta-Skill Agent**: A learnable agent responsible for maintaining and
  evolving a hierarchical library of reusable skills.
- **Hierarchical skill library**: A structured collection of reusable
  procedural knowledge that a Reasoning Agent can draw on.
