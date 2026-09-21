---
title: "Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails"
authors: "Zhou Yu et al."
year: 2026
doi: "arXiv:2609.09134"
category: self-improving-agents
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-21"
arxiv_version: "2609.09134v1"
pdf_pages: 10
pdf_sha256: "ae8b8973f7964fca32b192fe3166ac66edb1afb78ad2b5212ec33b892a25cc34"
---

## Summary

Harness and weight adaptation can interfere: copying an expert's complete trajectories degrades a weaker agent under its evolved harness, while expert correction of localized student mistakes largely preserves harness gains. This is a compatibility result for sequential adaptation, not evidence that a learned self-editing controller compounds indefinitely. [PDF §§3-4, pp. 4-7](https://arxiv.org/pdf/2609.09134v1#page=4)

[Source review](../../sources/yu-2026-co-evolving-harnesses-and-models.md) · [Exact PDF](../../papers/yu-2026-co-evolving-harnesses-and-models.pdf). No official implementation repository verified; no benchmark reproduced.

## Key Contributions

- Separates stronger-model use of a weaker model's harness from the weaker model's ability to imitate that expert.
- Demonstrates an interaction: the imitation recipe improves a baseline harness's mean but harms the evolved harness on every Qwen task.
- Proposes student-state, single-turn expert corrections before LoRA SFT, retaining the student's surrounding trajectory. The mechanism preserves supervision locality; it is not policy-gradient RL. [PDF pp. 4-7, 10](https://arxiv.org/pdf/2609.09134v1#page=6)

## Methodology and Architecture

A Gemini meta-agent proposes validation-gated edits to prompts, tools, hooks, context management and subagent configuration. Qwen3-Coder-30B-A3B executes seven enterprise task types. Following harness evolution, an MLE agent localizes failing student turns; Gemini generates three corrections and a judge selects one. Corrected trajectories and self-successes train LoRA adapters. Final tests are held out from harness optimization. The task environments forbid direct database writes where MCP use is required and expose tool errors, so absolute scores are not automatically comparable with the antecedent suite. [§3.1 and Appendix B, PDF pp. 4, 9-10](https://arxiv.org/pdf/2609.09134v1#page=4)

## Results

Across seven tasks, Table 1 reports Qwen mean test success of 29.2% with the base harness, 78.0% with the evolved harness, 63.1% after imitation under the evolved harness, and 79.7% after localized correction. Baseline-harness imitation instead reaches 35.5%. Reported SEMs concern three runs, not evidence of independent repeated harness searches. Correction gains on five tasks and slightly regresses payroll/budget; +1.7 points is not established as a statistically significant paired gain. [Table 1, PDF p. 5](https://arxiv.org/pdf/2609.09134v1#page=5)

Gemma replication covers only WebArena: 46.7% base, 55.6% evolved, 41.1% after imitation. Gemini's Qwen-harness transfer improves its mean from 84.4% to 93.6%, but two tasks decline versus its own baseline. Do not summarize either result as uniform cross-model/domain transfer. [PDF pp. 4-5](https://arxiv.org/pdf/2609.09134v1#page=5)

Planning-defect labels rise from 1.1% to 14.6% of failures with imitation and remain 1.8% with correction. These judge-labeled, failure-conditioned shares and case studies support a planning-fit hypothesis, not a causal mechanism estimate. Section 3.4's 28.9%/26.8% overall failure rates do not match complements of Table 1's means; denominators remain unresolved. An under-one-hour fine-tune excludes end-to-end teacher/search costs. Repeated co-evolution and joint optimization remain proposed extensions. [Table 3, §4, Appendices B-D, PDF pp. 6-10](https://arxiv.org/pdf/2609.09134v1#page=6)

## Related Papers

[[hebbar-2026-sia-self-improving-ai]] and [[gao-2026-experience-funnel-a-state-policy]] provide joint/alternating adaptation comparators; this paper adds a negative composition control. [[xu-2026-adapting-the-interface-not-the]] and [[yue-2026-ecdysis-efficient-and-effective-training]] transfer or repair harnesses without this subsequent student-weight intervention. [[feng-2026-coskill-joint-reinforcement]] trains an editing role; this fixed correction procedure does not answer the learned-editor question.

Connected synthesis: [[overviews/self-improving-llm-agents]], [[concepts/procedural-self-improvement]], [[concepts/evaluating-self-improvement]], and [[questions/does-a-modifiable-meta-procedure-improve-skill-library-co-training]].
