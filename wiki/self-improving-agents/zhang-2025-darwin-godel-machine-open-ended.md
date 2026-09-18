---
title: "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents"
authors: "Zhang, Jenny; Hu, Shengran; Lu, Cong; Lange, Robert; Clune, Jeff"
year: 2025
doi: "arXiv:2505.22954"
category: ["self-improving-agents"]
pdf_path: "/papers/zhang-2025-darwin-godel-machine-open-ended.pdf"
pdf_filename: "zhang-2025-darwin-godel-machine-open-ended.pdf"
source_collection: "arxiv"
source_format: "pdf"
text_extractor: "pdftotext-layout"
text_extracted_date: "2026-09-11"
arxiv_version: "2505.22954v1"
pdf_url: "https://arxiv.org/pdf/2505.22954v1"
pdf_pages: 64
pdf_sha256: "217c1ac0884312b897648027bdfd6745f4b790b522cab8a61fea32faf0752943"
full_text_reviewed_date: "2026-09-11"
---

## Summary

The Darwin Godel Machine evolves a population of coding agents that modify their own implementations, retaining useful stepping stones under empirical evaluation.

## Key Contributions

Replaces proof of improvement with benchmark evidence and explores an archive instead of only the latest or best agent. The coding agent both solves external tasks and implements changes to itself. This is a direct predecessor to Hyperagents, with a coding-specific alignment between solving and self-modifying. [PDF p. 4](https://arxiv.org/pdf/2505.22954v1#page=4)

## Methodology and Architecture

Select a parent from an archive, inspect its evaluation logs, propose a feature, and let the parent implement it. Admit executable agents that retain code-editing ability, including candidates below their parent's score. Foundation-model weights, archive maintenance, and parent selection stay fixed. The reported searches run 80 iterations with staged benchmark evaluation and more evaluation for promising candidates. [PDF p. 4](https://arxiv.org/pdf/2505.22954v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2505.22954v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2505.22954v1#page=6)

## Results

In this version, SWE-bench Verified evaluation improves from 20.0% to 50.0% on the study's 200-task evaluation subset, not the entire 500-task set. Polyglot improves from 14.0% to 38.0% on the 50-task search subset, versus 14.2% to 30.7% on the full benchmark. The study uses pass@1, unlike the cited Polyglot leaderboard's pass@2. Archive and fixed-initial-editor ablations support the value of both mechanisms in these runs. [PDF p. 5](https://arxiv.org/pdf/2505.22954v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2505.22954v1#page=6)

## Limitations

Search feedback and staged selection expose benchmark subsets; the full Polyglot evaluation includes search tasks and is not wholly untouched. Coding performance is an imperfect proxy for the quality of future modifications, especially outside coding. Open-ended search is a method description, not proof of unbounded or accelerating progress. This ingest intentionally preserves v1 as the historical baseline; later versions are a revision-review backlog item. [PDF p. 4](https://arxiv.org/pdf/2505.22954v1#page=4) [PDF p. 5](https://arxiv.org/pdf/2505.22954v1#page=5) [PDF p. 6](https://arxiv.org/pdf/2505.22954v1#page=6)

## Related Papers

[[zhang-2026-hyperagents]]; [[lee-2026-meta-harness-end-to-end]]. Synthesis: [[concepts/procedural-self-improvement]] and [[overviews/self-improving-llm-agents]]. Detailed provenance: [source note](../../sources/zhang-2025-darwin-godel-machine-open-ended.md); [PDF](../../papers/zhang-2025-darwin-godel-machine-open-ended.pdf).
