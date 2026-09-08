# Seed-paper PDF upgrade: claim-change record

Review date: **2026-09-08**. Base: merged PR #1 at
`260f94c21522218251db531843566bc5d2fee6c5`. Scope: the four admitted seed
papers, their eight source/wiki notes, and the existing overview/question.
No additional papers or broad novelty search were added.

## Coverage and provenance

- **4 / 4** exact PDFs retrieved; **8 / 8** notes upgraded from
  abstract summaries to PDF-grounded methods, results, and limitations.
- Version pins: Meta-Harness **2603.28052v1** (26 pages), Hyperagents
  **2603.19461v1** (60), SIA **2605.27276v2** (15), CoSkill
  **2609.04865v1** (25). These are the versions available at retrieval.
- Canonical files, SHA-256 digests, byte/page counts, and extraction details:
  [PDF inventory](../../papers/README.md), [manifest](../../papers/manifest.json).
- Text extracted with `pdftotext -layout`; key rendered result pages
  visually checked: Meta-Harness p. 9, Hyperagents p. 13, SIA p. 11,
  CoSkill pp. 7 and 20. Poppler reported path/font warnings on extraction;
  extraction completed for all PDFs and reviewed pages rendered legibly.
- Citations identify version, PDF page, and section/table where useful.
  Values are paper-reported unless explicitly marked as calculated or
  inferred. No experiment or author-code reproduction was performed.

## Changes justified by the full text

| Earlier interpretation | Full-text correction | Evidence | Effect |
|---|---|---|---|
| Meta-Harness reads the full history, up to 10M tokens per step | It selects files from a persisted history; 10M denotes generated diagnostics, not necessarily consumed context. Median 82 file reads/iteration in the audited run. | [§3, p. 4; Appendix A.1, p. 15](https://arxiv.org/pdf/2603.28052v1#page=15) | Correct both notes and overview. |
| Meta-Harness demonstrates a 6x gap and surpasses all hand-designed coding harnesses | 6x is cited motivation. Haiku is best in the reported table; Opus 76.4% is below reported ForgeCode 81.8%. | [pp. 1, 9, Table 7](https://arxiv.org/pdf/2603.28052v1#page=9) | Remove overbroad attribution/ranking. |
| Math transfer is across five held-out models; coding shows generalization | Five models are evaluated, but GPT-OSS-20B was used during search; four are additional unseen models. TerminalBench search/final evaluation use the same 89 tasks. | [§§4.2-4.3, pp. 8-9](https://arxiv.org/pdf/2603.28052v1#page=8) | Distinguish model/problem transfer from benchmark optimization. |
| Hyperagents is fully self-editable and outperforms DGM across all settings | Main parent-selection/evaluation rules are fixed. Coding gains are comparable to DGM, not superior. DGM-custom test comparisons are not significant. | [§3, p. 5; §5.1, pp. 7-9; §7, p. 14](https://arxiv.org/pdf/2603.19461v1#page=5) | Bound the recursive-improvement claim. |
| Hyperagents transfers across coding, review, robotics, and grading and compounds gains | Specific transfer is joint review/robotics to grading, carrying both task and meta implementations; the meta component is frozen during imp@50. The 200-step 0.640 vs 0.610 comparison has p>0.05. | [§§5.2-5.3, pp. 9-13](https://arxiv.org/pdf/2603.19461v1#page=9) | Narrow overview and research-question analogy. |
| SIA beats harness or weights alone | It reports initial, harness-only, and combined conditions, without a weight-only ablation. Selector learning is future work. | [Table 3, p. 11; §9, p. 13](https://arxiv.org/pdf/2605.27276v2#page=11) | Retain incremental improvement, remove universal complementarity. |
| SIA LawBench describes direct charge prediction by an adapted LLM | Rollouts are generated solution scripts; harness search includes TF-IDF/LinearSVC, and RL uses script execution scores from the test split. | [§6.3.1, p. 9](https://arxiv.org/pdf/2605.27276v2#page=9) | Correct the training target and flag lack of untouched-test evidence. |
| SIA reduces runtime from the initial 12,483 μs and gives 502% denoising improvement | 12,483 μs is harness-only. Denoising 0.048/0.241/0.289 yields about +502% vs initial but +19.9% vs harness-only. The metric is higher-is-better `mse_norm`. | [§6.3.2, p. 10; Table 3, p. 11](https://arxiv.org/pdf/2605.27276v2#page=11) | Correct baselines, units, and percentage denominators. |
| The four papers have no direct comparisons; SIA and Meta-Harness are directly comparable | SIA discusses Meta-Harness/Hyperagents and reports prior comparator scores. A matched empirical head-to-head is not established; LawBench descriptions differ (191 vs 215 classes, code generation vs online classification). | [SIA §§4.1, 6, pp. 4, 8-9](https://arxiv.org/pdf/2605.27276v2#page=4); [Meta-Harness §4.1, p. 6](https://arxiv.org/pdf/2603.28052v1#page=6) | Replace blanket statements with protocol-specific comparison limits. |
| CoSkill learns a meta-skill workflow rather than doing weight updates | One shared actor is trained for reasoning and editing. Edit actions, replay reward, promotion, and GiGPO remain fixed; library edits are staged before verification. | [§3, pp. 3-6; Algorithm 2, p. 18](https://arxiv.org/pdf/2609.04865v1#page=3) | Clarify learned policy vs editable procedure. |
| CoSkill's headline gains describe a uniform, independently replicated comparison | Baselines largely come from prior tables; headline and ablation results differ; validation settings are not fully reconciled. No cross-environment editor transfer is tested. | [Tables 1-2, pp. 7-8; Appendices E-F, pp. 19-20](https://arxiv.org/pdf/2609.04865v1#page=7) | Bound comparative and transfer claims. |

## What remains intact

The overview's central organizing idea is unchanged: agent harnesses,
meta-agent programs, and skill libraries can be optimization targets.
Meta-Harness's trace-access advantage, Hyperagents' specific transferred
agent-generation result, SIA's incremental gains after harness search,
and CoSkill's within-environment co-training ablations remain supported
within their stated protocols.

The Hyperagents–CoSkill combination remains an **unanswered question**.
Full text does not supply a result for that combination or justify a
broader novelty claim. The revised question distinguishes editing the
improvement procedure from changing the RL objective, and identifies
controls needed to isolate transferred editor capability.

## Unresolved paper-level reporting issues

These are preserved as limitations, not silently repaired:

- Meta-Harness calls five math models held out in some prose even though
  §4.2 uses one of them in search.
- SIA's freely interleaved conceptual loop exceeds the coarse schedule
  described for the reported experiments; test-split reward exposure
  prevents treating its LawBench result as established independent testing.
- CoSkill's Appendix E and Table 3 differ on validation size and schedule;
  Table 1 calls the ALFWorld aggregate a macro average but displays
  category values averaging about 98.33%, while reporting 98.4%.

See the individual [source notes](../../sources/) for precise citations
and further limitations. These findings arise from the PDFs; the authors'
code, raw runs, and private evaluation data were outside this ingest.

## Validation

The repository checks cover PDF signatures/page counts/hashes, matching
metadata in each source/wiki pair, required sections, all relative and
wiki links, bidirectional overview connections, citation page bounds,
absence of abstract-only metadata in active notes, and regeneration of
the catalog. Historical fallback records remain intact.
