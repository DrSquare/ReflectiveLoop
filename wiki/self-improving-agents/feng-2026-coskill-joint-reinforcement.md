---
title: "CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution"
authors: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu
year: 2026
doi: arXiv:2609.04865
source: feng-2026-coskill-joint-reinforcement.md
category: [self-improving-agents]
pdf_path: /papers/feng-2026-coskill-joint-reinforcement.pdf
pdf_filename: feng-2026-coskill-joint-reinforcement.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
tags: [skill-library, multi-agent-rl, hierarchical-skills]
---

## Summary
CoSkill jointly trains a learnable Meta-Skill Agent and a Reasoning Agent
under a unified multi-agent RL framework, turning a previously static
meta-skill workflow into something that co-adapts with the reasoning
policy over a hierarchical skill library.

## Key Contributions
- Prior skill-library methods keep skill evolution separate from policy
  optimization, or freeze meta-skills as fixed workflows.
- Introduces a Meta-Skill Agent that is itself learnable and trained
  jointly with the Reasoning Agent, enabling end-to-end co-adaptation.

## Methodology and Architecture
Two agents trained together with RL: a Reasoning Agent that solves tasks,
and a Meta-Skill Agent that maintains and evolves a hierarchical skill
library the Reasoning Agent draws on.

## Results
- ALFWorld: 98.4% success rate (+3.5 points over baselines).
- WebShop: 90.6% success rate (+6.2 points over baselines).
- Better early-stage sample efficiency and wall-clock efficiency than
  prior skill-based/RL baselines.

## Related Papers
- [[overviews/self-improving-llm-agents]] — surveyed alongside
  Meta-Harness, Hyperagents, and SIA.
- [[zhang-2026-hyperagents]] and [[hebbar-2026-sia-self-improving-ai]] —
  all three move a previously fixed component (meta-level procedure,
  harness, or skill workflow) into something learnable, but CoSkill applies
  this to hierarchical skill libraries via joint multi-agent RL.
