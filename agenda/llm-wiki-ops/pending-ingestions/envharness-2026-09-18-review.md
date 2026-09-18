# EnvHarness — reviewed addition awaiting PDF publication

The requested paper is **EnvHarness: Awakening Static Worlds for Agent Learning**, [arXiv:2608.19880v1](https://arxiv.org/abs/2608.19880v1), linked by [google-research/envharness](https://github.com/google-research/envharness). It is not yet admitted on this branch.

## Reviewed contribution

EnvHarness adapts the environment that supplies training experience. A fixed EnvRigger loop diagnoses policy traces, prepares reachable starting states and transforms interactions while reusing native task verifiers. Skills and separate RL policies are evaluated on original held-out tasks. The draft adds a concept page on reset and verifier boundaries and a control for the existing meta-procedure/skill-co-training question; it does not claim that question is answered. [PDF pp. 4-10, 19, 21-23](https://arxiv.org/pdf/2608.19880v1#page=6)

The source draft covers splits, models, rollout budgets, main-table three-run variation, chain composition, scaling, cost and implementation assumptions. It preserves negative results: RL ALFWorld OOD success falls 89.6 to 88.8%; held-out heat-task success falls 61.1 to 52.4%. Cross-model experiments rerun adaptation rather than transfer a frozen skill bank. [PDF pp. 10, 34-35](https://arxiv.org/pdf/2608.19880v1#page=35)

## Complete preserved changes

The [reviewed draft bundle](huang-2026-envharness-awakening-static-worlds-for.json) contains exact text for the source and wiki notes, new environment-adaptation concept, overview/question connections, root README entry/count, PDF inventory, manifest and regenerated catalog. It includes base-blob guards and hashes. Apply these only with the exact PDF present; reconcile any intervening changes rather than overwrite them.

The complete local addition passed the repository validator: **22 PDF/source/wiki triples and 27 wiki pages**, catalog current, local links and bidirectional synthesis valid. README coverage, links and counts passed additional checks. The published checkpoint retains **21 admitted papers**; root README, manifest and catalog are unchanged because the PDF is not published.

## Exact blocker and retry

The exact [versioned PDF](https://arxiv.org/pdf/2608.19880v1) is 2,510,495 bytes and 41 pages. SHA-256: `3859eed3337e0324ef94f38ca21f69cc6daa15b5a78497680370959223d51fd4`; Git blob: `6c77627830248ad9baeead15859ca6d1ae72912b`. Poppler warnings were recorded; extraction, independent parsing and inspection of result pages succeeded without modifying the bytes.

Shell Git has no push authentication. The supported Git Data API binary upload stalled; the expected blob still returns 404. The approximately 3.35 MB base64 request is below the connector's 16 MiB limit, so this is a transport failure, not a size-limit rejection. No placeholder source/wiki entry was published. Browser fallback requires confirmation under the control-browser skill after a supported connector operation fails; it has not been attempted.

Publication and merge remain incomplete. The recurring scan watermark is unchanged. Revisit this reviewed candidate before ordinary backlog processing.
