---
title: "Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender Systems"
authors: "Ming Li; Dai Li; Xuying Ning; Bo Sun; Rui Li; Yi Zhang; Silvia Gong; Xuan Cao; Rui Li; Cornelia Carapcea; Qunshu Zhang; Zhigang Wang; Yinglong Xia; Xue Feng; Andy Wang"
year: 2026
doi: "arXiv:2609.10922"
category: ["self-improving-agents"]
pdf_path: "/papers/li-2026-auto-recsys-harnessing-autonomous-research.pdf"
pdf_filename: "li-2026-auto-recsys-harnessing-autonomous-research.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-12"
arxiv_version: "2609.10922v1"
pdf_url: "https://arxiv.org/pdf/2609.10922v1"
pdf_pages: 16
pdf_sha256: "f4a5656658f30151b8399cb7e06826cea95b8a62162527682a37a19697b6bbf9"
---

## Summary

Auto-RecSys is Meta's persistent research-agent harness for recommendation experiments whose training takes hours or days. It evolves operational playbooks and research history while coordinating concurrent jobs across sessions and servers. Its main evidence is observational improvement in operational reliability, with narrower support for scientific-quality improvement or transfer.

## Key Contributions

It connects two kinds of persistent experience: execution trajectories update model-specific procedures, while experimental outcomes guide future hypotheses. Natural-language skills support reasoning; deterministic scripts protect exact state and infrastructure interactions. This makes recoverable execution a concrete part of the self-improvement substrate. [§§2–6, PDF pp. 3–10](https://arxiv.org/pdf/2609.10922v1#page=3)

## Methodology and Architecture

Each idea has an independent state machine for implementation, validation, training, analysis, and debugging, coordinated by a shared registry. Shared histories, session trajectories, and draft code changes support recovery on a different server. A general orchestrator skill, model playbooks, and per-iteration state separate reusable procedures from transient details. [PDF pp. 4–5, 9–10, 13](https://arxiv.org/pdf/2609.10922v1#page=4)

The execution loop distills failures with fixes, successful command sequences, and submission settings into playbooks. Human-assisted bootstrapping precedes more autonomous operation. What transfers to another model is the mature playbook's **structure**, populated interactively with new files, commands, and constraints; its contents then evolve independently. [§4, PDF pp. 5–7](https://arxiv.org/pdf/2609.10922v1#page=5)

The idea loop proposes and ranks experiments from researcher inputs, literature, and architectural context, then records baseline-relative outcomes to avoid repeats and develop later hypotheses. Per-model baseline alignment concerns recommendation experiments, not an ablation of the agent mechanism. [§5, PDF pp. 7–9](https://arxiv.org/pdf/2609.10922v1#page=7)

## Results

Across **31 unique iterations on one model**, average major operational fixes fall from **4.0** in bootstrap iterations 1–4 to **1.3** in iterations 5–20. A baseline change causes renewed failures in iterations 21–25; iterations 26–31 recover to **0.5**, with **5/6** requiring no operational fix. Ordinary code-implementation debugging is excluded from this metric. This is an adaptation trajectory, not a controlled causal estimate of playbook benefit. [Figure 4 and §7.2, PDF pp. 10–11](https://arxiv.org/pdf/2609.10922v1#page=10)

The authors describe hands-on effort falling from hours/days to minutes, but supply no detailed controlled timing study; training remains multi-day. Qualitative examples include recovering code on another server, 110 tool calls without intervention in the most autonomous session, and an agent replacing a context-overflowing monitor with cron-driven fresh sessions. The last example changes orchestration code, but does not establish general learning-to-improve ability. [§§7.1–7.3, PDF pp. 10, 12–13](https://arxiv.org/pdf/2609.10922v1#page=10)

## Limitations

- No component ablations, independent replicated adaptation runs, uncertainty intervals, or controlled scientific-quality gains. Human help and changing tasks/infrastructure are potential confounds. Agent-model configuration and a runnable public implementation were not identified in the reviewed primary sources. [§7, PDF pp. 10–13](https://arxiv.org/pdf/2609.10922v1#page=10)
- Playbook edits have **no formal validation gate**: agent judgment promotes them. Schema-valid state writes do not establish correct or appropriately scoped memory. A past failure can be real while its inferred cause or generalization is wrong; this qualification is a wiki inference. [§9, PDF p. 14](https://arxiv.org/pdf/2609.10922v1#page=14)
- Template transfer with interactive filling differs from cross-model scientific-insight transfer, which remains future work. There is no joint LLM/editor training or controlled transfer of an evolving meta-procedure. Team-scale coordination also remains future work. [PDF pp. 6–7, 14–15](https://arxiv.org/pdf/2609.10922v1#page=6)
- Preserve reporting distinctions: four versus two interactive checkpoints; 31 iterations/transcripts versus 46 sessions; 19 dead-end table entries versus 49 accumulated dead ends. Their mappings are not fully specified. The source note also records PDF/arXiv title and author-list differences. [PDF pp. 3, 10, 12](https://arxiv.org/pdf/2609.10922v1#page=10)

## Related Papers

[[lee-2026-meta-harness-end-to-end]] for trace-informed search; [[karten-2026-prime-agent-a-self-improving]] for persistent systems; [[park-2026-autosaddler-automatic-harness-optimization-with]] for development-time candidate re-execution and selection; [[zhang-2026-hyperagents]] for a modifiable meta-procedure; [[feng-2026-coskill-joint-reinforcement]] for jointly trained skill-editing and reasoning roles. These are mechanism comparisons, not a shared performance ranking.

Synthesis: [[concepts/procedural-self-improvement]], [[concepts/evaluating-self-improvement]], and [[overviews/self-improving-llm-agents]]. Full provenance, protocol, and ambiguities: [source note](../../sources/li-2026-auto-recsys-harnessing-autonomous-research.md); [exact PDF](../../papers/li-2026-auto-recsys-harnessing-autonomous-research.pdf).
