---
name: knowledge_keeper
description: Knowledge-base retrieval and capture for papers and external sources. Load when the user asks to search literature, look up a paper, summarize a paper into the knowledge base, or reuse previously found references. Enforces local-first retrieval, a query log, and mandatory capture to avoid repeated API searches.
requires: research_manager
---

## Output Contract

- Label every claim as **fact** (with source) or **speculation** (explicitly marked, e.g. `[speculation]`). Never state speculation as fact — this is a hard red line.
- Plain language: conclusion first; explain any jargon in one short sentence on first use; no filler phrases or padding; prefer tables or lists when they aid scanning.

# Knowledge Keeper — Search Once, Capture Always

The knowledge base lives in the project's `.kilo/knowledge/papers/`. Its purpose: never pay twice for the same search.

## 1. Local-First Protocol

Before any API or web call:

1. Grep `.kilo/knowledge/papers/` note files for the topic.
2. Check `knowledge/papers/00-query-log.md` for a similar past query.

On a local hit, answer from the cached notes and say the source is the local knowledge base. Do not call the API again.

## 2. Query Log

`knowledge/papers/00-query-log.md` records every external query:

| Date | Query terms | Source | Hits | Notes created |
|---|---|---|---|---|

- A query identical or highly similar to a logged one within **7 days** (adjustable) must not be re-run; reuse the logged results and state the original search date.
- Update the log on every external search, including searches that return nothing — empty results are also worth caching.

## 3. Mandatory Capture

Any paper actually used (cited in a reply or document) must be saved immediately as `knowledge/papers/author-year-title.md`. Deduplicate by arXiv ID or DOI; if a note exists, update it instead of creating a copy. Searching without capturing is forbidden — that is what causes repeated searches and API bans.

Note template (minimal fields):

```
# Title — Authors (Year)
link: <url or arXiv ID>
relevance: <which direction/proposal this serves>

## Takeaway
One paragraph: the conclusion, and how strong the evidence is.

## Reusable points
- Method / dataset / result worth reusing, one bullet each.

## Caveats
- Limitations or untested claims. Mark speculation as [speculation].
```

Do not paste the abstract verbatim; write the takeaway in plain language.

## 4. Index

Create or update `knowledge/papers/00-overview.md` once the directory holds more than five notes (per `research_manager` section 4). Index entries: one line per paper — citation, one-sentence takeaway, linked direction.

## 5. Boundaries

- `knowledge_keeper` retrieves, captures, and indexes. It does not judge whether a literature gap is real — that verdict belongs to `research_progress`.
- Actually call arXiv / Semantic Scholar APIs when a search is needed; never fabricate papers or citations.
- File writes only after user confirmation.
