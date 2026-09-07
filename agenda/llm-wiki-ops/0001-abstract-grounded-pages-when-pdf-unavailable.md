# ADR 0001: Abstract-grounded pages when PDF access is unavailable

Date: 2026-09-07

## Context
`AGENTS.md` rule 9 requires the canonical full text of a paper to be an
exact PDF in `papers/`. The sandbox this repository was initially set up
in has no network access to `arxiv.org`, so the four seed papers'
PDFs could not be downloaded.

## Decision
Rather than skip the papers entirely or fabricate PDF content, their
`sources/` and `wiki/` pages were written from publicly reported
abstracts/summaries, with `text_extractor: abstract-summary` recorded in
frontmatter so this is never confused with a real PDF extraction. The
papers were also added to the missing-PDF table in `papers/README.md`.

## Consequences
- Section depth (methodology detail, exact numbers, glossary) is limited
  to what is publicly summarized, not full-paper depth.
- Once a machine with `arxiv.org` access downloads the real PDFs, they
  should be dropped into `papers/`, re-ingested per the `AGENTS.md` steps,
  and the missing-PDF table entries removed.
