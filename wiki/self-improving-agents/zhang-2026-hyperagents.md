---
title: "Hyperagents"
authors: Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, Tatiana Shavrina
year: 2026
doi: arXiv:2603.19461
source: zhang-2026-hyperagents.md
category: [self-improving-agents]
pdf_path: /papers/zhang-2026-hyperagents.pdf
pdf_filename: zhang-2026-hyperagents.pdf
source_collection: arxiv
source_format: abstract
text_extractor: abstract-summary
text_extracted_date: 2026-09-07
tags: [self-referential-agents, darwin-godel-machine, recursive-self-improvement]
---

## Summary
Hyperagents unify a task agent and a meta-agent into one fully editable
program, making the meta-level modification procedure itself modifiable.
DGM-Hyperagents (DGM-H) extends the Darwin Gödel Machine with this framing
to enable cross-domain recursive self-improvement beyond coding.

## Key Contributions
- Prior self-improving systems (e.g. DGM) use fixed, handcrafted
  meta-level mechanisms tied closely to coding.
- Hyperagents enable metacognitive self-modification: improving the
  process that generates future improvements, not just the solutions.
- DGM-H removes the assumption that domain task-performance gains
  automatically translate into better self-modification ability.

## Methodology and Architecture
A single self-referential program contains both the task-solving component
and the meta component that rewrites the task agent and itself, so
improvements to the "how do I improve" process can compound across
domains.

## Results
DGM-H outperforms baselines (including the original DGM) over time across
coding, peer review, robotics reward design, and Olympiad-level math
grading, accumulating transferable meta-level improvements (e.g.
persistent memory, performance tracking).

## Related Papers
- [[overviews/self-improving-llm-agents]] — surveyed alongside
  Meta-Harness, SIA, and CoSkill as approaches that make a traditionally
  fixed agent component learnable/self-modifying.
- [[lee-2026-meta-harness-end-to-end]] — also treats an agent's own
  scaffold as an optimization target, but without unifying task and meta
  agent into one self-editing program.
