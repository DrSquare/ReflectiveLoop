# papers/

Canonical PDFs are copied here, never symlinked. Existing seed stems are
preserved so source/wiki links remain stable. All four PDFs were retrieved
from the versioned arXiv links below on September 8, 2026 and validated by
PDF signature, extraction, page count, and SHA-256.

## Retrieved seed PDFs: 4 / 4

| Paper | Versioned source | Local PDF | Pages |
|---|---|---|---:|
| Meta-Harness | [2603.28052v1](https://arxiv.org/pdf/2603.28052v1) | [lee-2026-meta-harness-end-to-end.pdf](lee-2026-meta-harness-end-to-end.pdf) | 26 |
| Hyperagents | [2603.19461v1](https://arxiv.org/pdf/2603.19461v1) | [zhang-2026-hyperagents.pdf](zhang-2026-hyperagents.pdf) | 60 |
| SIA | [2605.27276v2](https://arxiv.org/pdf/2605.27276v2) | [hebbar-2026-sia-self-improving-ai.pdf](hebbar-2026-sia-self-improving-ai.pdf) | 15 |
| CoSkill | [2609.04865v1](https://arxiv.org/pdf/2609.04865v1) | [feng-2026-coskill-joint-reinforcement.pdf](feng-2026-coskill-joint-reinforcement.pdf) | 25 |

Exact hashes, byte counts, extraction method, and visually inspected pages
are recorded in [manifest.json](manifest.json). Citations in the notes use
1-based PDF page numbers, which match the printed numbering in these
versions. Extraction used `pdftotext -layout`; original PDFs are unchanged.
The source notes are analytical summaries, not redistributed full-text
transcriptions.

## Missing-PDF list

None: **0 / 4** seed PDFs are missing. All eight source/wiki pages now use
`source_format: pdf` and `text_extractor: pdftotext-layout`.
The September 7 fallback remains documented in the historical ADR and log.

See the [claim-change record](../logs/reports/2026-09-08-seed-pdf-upgrade.md)
for corrections and the limits of this full-text review.
