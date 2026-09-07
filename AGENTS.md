# ReflectiveLoop — LLM Wiki (Literature Review)

A personal knowledge base of self-improving-agent / LLM-agent research papers,
following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285):

```
Original PDF → sources/*.md → wiki/{category}/*.md → wiki/overviews/ + wiki/concepts/
```

Language policy: all wiki content is in English. Conversation can be in any language.

This file is the single source of truth for how agents work in this folder.
Claude Code and Codex both read it — keep `CLAUDE.md` as a symlink to this file
(`ln -s AGENTS.md CLAUDE.md`) and keep the wording agent-neutral.

---

## Startup checklist

At the start of every session in this folder, before acting on any ingest,
search, or synthesis request:

1. Re-read this file.
2. Re-read `index.md` and `indexes/` before assuming what is already covered.
3. Do not rely on memory from a previous session for anything that moves.

---

## The rules

### The four core rules

1. No web search. Never use `WebSearch` or `WebFetch` to fill a gap. Every
   answer must be grounded in papers actually present here. Use them only
   when the user explicitly asks, for that one task.
2. Answer from the wiki first. `sources/` and `wiki/` are the only sources
   of truth.
3. If the wiki is insufficient, re-read the original PDF in `papers/` and
   extract more detail. Then update the wiki so the next question does not
   need the PDF.
4. If no paper exists on the topic, say so: "I don't have a paper on this —
   please give me the PDF." Do not improvise.

These apply to every response, overview pages included: cite only papers
that exist in this wiki.

### Five more rules

5. A paper is not ingested until it is connected to the synthesis layer.
   See "The synthesis requirement" below.
6. No tiers, no placeholder pages. Every admitted paper meets the same
   standard: concrete methods, results, limitations, and synthesis links.
   Never create a page from only a filename.
7. Exhaustive means exhaustive. When asked for all of something, process
   the whole set before reporting. State the denominator and the numerator.
8. Confidential material stays out of `wiki/`. Unpublished manuscripts,
   drafts under review, and embargoed work must not appear in `wiki/` at
   all. Those notes go in `agenda/`. Published work with a DOI/arXiv id is
   ordinary wiki content.
9. PDFs only. The canonical full text of a paper is an exact PDF in
   `papers/`. If an exact PDF cannot be obtained (for example, network
   access to `arxiv.org` is blocked from the working environment), keep
   the paper on the missing-PDF list in `papers/README.md` instead of
   silently ingesting a degraded copy, and record the limitation in the
   day's log. A source/wiki page built from a publicly reported
   abstract/summary instead of the PDF must say so explicitly in its
   `text_extractor` field (`abstract-summary`) rather than claim a PDF
   extraction that did not happen.

Also: correction, erratum, and retraction notices are not papers.

---

## Repository structure

```
ReflectiveLoop/
├── AGENTS.md               # This file. CLAUDE.md is a symlink to it
├── index.md                # Generated catalog: categories, page counts, synthesis coverage
├── indexes/                # Generated per-category page listings
├── logs/                   # Daily work logs — the narrative record
│   ├── {YYYY-MM-DD}-{agent}-{host}.md
│   └── reports/            #   audit reports written for a person to read
├── scripts/                # Extraction, validation, index and log builders
├── papers/                 # Original PDFs, canonical storage, + missing-PDF list
├── sources/                # PDF/abstract summaries, English
├── wiki/                   # Knowledge layer, English
│   ├── {category}/
│   ├── concepts/
│   ├── overviews/
│   └── questions/
├── agenda/                 # Project execution notes, plans, handoffs, unpublished work
└── materials/              # Non-paper reference material
```

### The three synthesis layers

- `overviews/` — encyclopedic topic pages. Declarative noun-phrase titles.
  Never a question title.
- `concepts/` — stable definitions, methods, mechanisms. Written once,
  pointed at by many paper pages.
- `questions/` — paper-anchored research questions. The title is a
  question; the body has `## Question`, `## Sharper follow-up`,
  `## What the knowledge base holds`, `## Tentative answer`.

### `agenda/`

`agenda/{project-or-context}/` holds work-facing notes: execution plans,
handoff documents, decision records. Durable decisions about how this wiki
operates live in `agenda/llm-wiki-ops/` as short ADR-style notes.

---

## File naming convention

All tiers (PDF, source, wiki) share one stem:

```
{first-author-lastname}-{year}-{first-5-title-tokens}.{ext}
```

- Tokens, not words. Lowercase the title, then take runs of alphanumerics.
- Year is 4 digits.
- Example: `hebbar-2026-sia-self-improving-ai`

---

## Categories

| Category | Includes |
|---|---|
| `self-improving-agents` | Agent harnesses/scaffolds, meta-agents, and weight/skill updates that let an agentic system improve itself over time |
| `concepts` | Methods, mechanisms, reusable definitions |
| `overviews` | Encyclopedic synthesis pages |
| `questions` | Paper-anchored research-question pages |
| `other` | Cross-cutting, miscellaneous |

---

## Adding a paper

1. Locate the PDF (in `papers/`, copied never symlinked) or, when the PDF
   cannot be fetched from this environment, add it to the missing-PDF list
   in `papers/README.md`.
2. Write `sources/{stem}.md` with the standard frontmatter and sections:
   `One-line Summary`, `1. Document Information`, `2. Key Contributions`,
   `3. Methodology and Architecture`, `4. Key Results and Benchmarks`,
   `5. Limitations and Future Work`, `6. Related Work`, `7. Glossary`.
3. Write `wiki/{category}/{stem}.md` with `Summary`, `Key Contributions`,
   `Methodology and Architecture`, `Results`, `Related Papers`.
4. Connect the new page to the synthesis layer (see below) — mandatory.
5. Log it in `logs/{YYYY-MM-DD}-{agent}-{host}.md`, then regenerate the
   catalog:
   ```bash
   python3 scripts/build_index.py --apply
   ```

## The synthesis requirement

A source/wiki pair with no link into `overviews/` or `concepts/` is a
synthesis-orphan. Every ingest must end with:

1. At least one bidirectional link between the new page and the single
   most relevant existing overview/concept page.
2. One sentence in that synthesis page's body placing the paper in
   context.
3. A supersede check: does the paper strengthen, narrow, contradict, or
   replace an existing claim? Record it in the day's log if so.
4. If no overview/concept covers the topic yet, create the anchor.

---

## Logs

One Markdown file per day, per agent, per machine:
`logs/{YYYY-MM-DD}-{agent}-{host}.md`. Frontmatter (`date`, `agent`, `host`,
`model`), then append-only entries, oldest first, headed:

```
## [YYYY-MM-DD] ingest | {topic} | Paper or batch title
## [YYYY-MM-DD] maintenance | {topic} | Task
## [YYYY-MM-DD] query-to-wiki | {topic} | Result page
```
