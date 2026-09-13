---
title: "AutoHarness: improving LLM agents by automatically synthesizing a code harness"
authors: "Xinghua Lou; Miguel Lazaro-Gredilla; Antoine Dedieu; Carter Wendelken; Wolfgang Lehrach; Kevin P. Murphy"
year: 2026
doi: "arXiv:2603.03329"
category: ["self-improving-agents"]
pdf_path: "/papers/lou-2026-autoharness-improving-llm-agents-by.pdf"
pdf_filename: "lou-2026-autoharness-improving-llm-agents-by.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2603.03329v1"
pdf_url: "https://arxiv.org/pdf/2603.03329v1"
pdf_pages: 21
pdf_sha256: "8399c0a6a76a38c1a96804c88d0bac69286fe52ba3f255cba9175e3882fecf19"
---

## Summary

AutoHarness uses feedback-guided program search to synthesize game-specific action verifiers or complete Python policies, improving legal action execution without updating model weights.

## Key Contributions

Separates harness-as-action-filter, harness-as-action-verifier, and harness-as-policy. Programmatic action constraints can remove a failure mode that a larger reasoning model still exhibits, while a complete compiled policy removes runtime LLM calls. The work is a fixed-search baseline, not demonstrated recursive policy/editor co-training. [PDF pp. 2-3, 6](https://arxiv.org/pdf/2603.03329v1#page=2)

## Methodology and Architecture

A tree stores candidate programs. Thompson sampling chooses a node to refine using legal-action accuracy; Gemini-2.5-Flash mutates code using execution errors and critic feedback. The verifier rejects an invalid LLM proposal and retries with an illegal-action warning. Training uses ten parallel environments, up to 1,000 steps, and at most five failed steps for feedback. It stops at legality score 1.0 or timeout. New-seed rollouts test legality. [PDF pp. 2-3](https://arxiv.org/pdf/2603.03329v1#page=2)

The 145-game pool excludes nine free-form dialogue games; some available-move hints are manually removed. Actual game-performance evaluation is on 16 one-player and 16 two-player games. The full-code-policy variant instead optimizes a reward-sensitive heuristic, with up to 256 synthesis iterations (89.4 average), and no LLM calls during execution. Each environment gets a separate harness. [PDF pp. 3-6](https://arxiv.org/pdf/2603.03329v1#page=3)

## Results

The authors report 100% legal-action success on tested new rollouts across 145 games, not a formal all-states correctness proof. On 16 one-player games the verifier agent averages reward 0.745 versus Flash 0.673 and Pro 0.707. Two-player aggregate wins against Pro are reported as 56.3% versus 38.2% for Pro; 40 matches per game balance player order. [PDF pp. 3-4](https://arxiv.org/pdf/2603.03329v1#page=3)

The separate pure-code-policy variant averages reward 0.870 versus GPT-5.2-High 0.844 across 16 one-player games. It beats that comparator on only 3 games, loses on 5, and ties on 8. Trial counts differ: typically 20 per game, but GPT-5.2 uses 10 and GPT-5.2-High 5. [PDF p. 5](https://arxiv.org/pdf/2603.03329v1#page=5)

## Limitations

Legality and task reward have different denominators: 145 environments versus the 32-game strategic subset, and 16 games for code-policy. Finite successful legality rollouts do not guarantee safety on unseen states. The legality section's 14.5-iteration average is followed by a 19/32 statistic without fully reconciling that subset with the 145-game claim. The paper's near-zero test-time cost excludes synthesis and still entails program execution. Unequal evaluation repetitions and no reported confidence intervals limit interpretation of the 0.026 code-policy reward advantage. [PDF pp. 3-5](https://arxiv.org/pdf/2603.03329v1#page=3)

Harnesses are generated separately per environment; transfer of a reusable library or distillation into the base model is future work. The title page says March 5, 2026 while the arXiv version banner and metadata give February 10; preserve the pinned ID and note this date discrepancy. This research paper is not the unrelated governance/skill software also named AutoHarness. [PDF pp. 1, 6](https://arxiv.org/pdf/2603.03329v1#page=1)

## Related Papers

[[xu-2026-adapting-the-interface-not-the]]; [[zhang-2025-darwin-godel-machine-open-ended]]; [[gao-2026-experience-funnel-a-state-policy]]. Synthesis: [[concepts/procedural-self-improvement]] and [[concepts/evaluating-self-improvement]]. Detailed provenance: [source note](../../sources/lou-2026-autoharness-improving-llm-agents-by.md); [PDF](../../papers/lou-2026-autoharness-improving-llm-agents-by.pdf).
