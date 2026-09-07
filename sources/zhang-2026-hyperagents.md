---
title: "Hyperagents"
authors: Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina
year: 2026
doi: arXiv:2603.19461
category: [self-improving-agents]
pdf_path: /papers/zhang-2026-hyperagents.pdf
pdf_filename: zhang-2026-hyperagents.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
---

## One-line Summary
Hyperagents unify a task agent (solves the given problem) and a meta-agent
(modifies itself and the task agent) into a single, fully self-editable
program, so that the meta-level modification procedure itself is
modifiable — enabling recursive self-improvement that generalizes beyond
coding.

## 1. Document Information
- arXiv: 2603.19461, submitted March 2026.
- Code: https://github.com/facebookresearch/Hyperagents

## 2. Key Contributions
- Observes that prior self-improving systems (e.g. the Darwin Gödel
  Machine, DGM) use fixed, handcrafted meta-level mechanisms, and their
  gains are tied closely to coding tasks.
- Introduces "hyperagents": self-referential agents that fuse a task agent
  and a meta-agent into one editable program, enabling metacognitive
  self-modification — improving not just problem-solving but the very
  process that generates future improvements.
- Extends DGM into DGM-Hyperagents (DGM-H), removing the assumption that
  task-performance gains automatically translate into better
  self-modification ability.

## 3. Methodology and Architecture
A hyperagent is a single program containing both a task-solving component
and a meta component that can rewrite the task agent and itself. Because
the meta-level modification procedure is itself part of what can be
modified, improvements can compound across domains rather than being
limited to the domain the system was originally tuned for (coding, for
DGM).

## 4. Key Results and Benchmarks
- DGM-H outperforms baselines (including the original DGM) over time
  across diverse domains: coding, peer review, robotics reward design, and
  Olympiad-level math grading.
- Accumulates meta-level improvements (e.g. persistent memory, performance
  tracking) that transfer across domains and persist across repeated runs.

## 5. Limitations and Future Work
- Broader safety and oversight considerations are called out as important
  given the open-ended, cross-domain self-modification setting.
- Evaluated on a fixed set of domains; scaling to fully open-ended task
  distributions is future work.

## 6. Related Work
- Builds directly on the Darwin Gödel Machine (DGM) line of work.
- Related to [[lee-2026-meta-harness-end-to-end]] (Meta-Harness), which
  similarly treats an agent's own scaffold as an optimization target, but
  without the unified task/meta-agent self-editing framing.

## 7. Glossary
- **Hyperagent**: A self-referential agent combining a task agent and a
  meta-agent in one fully editable program.
- **Metacognitive self-modification**: Improving the process by which
  future improvements are generated, not just the solutions themselves.
- **DGM-Hyperagents (DGM-H)**: The Darwin Gödel Machine extended with the
  hyperagent framing.
