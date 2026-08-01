---
name: knowledge_keeper
description: Knowledge-base retrieval and capture for papers and external sources. Load when the user asks to search literature, look up a paper, summarize a paper into the knowledge base, or reuse previously found references. Enforces local-first retrieval, a query log, and mandatory capture to avoid repeated API searches.
requires: research_manager
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写"尚未验证"或"我推测"，不给每句话机械加 fact/speculation 标签。
- 一段能说清就不用表格；独立要点用列表；只有横向比较才用表格。
- 不写套话、廉价肯定、重复总结和固定收尾。

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

Search method, beyond plain keywords: find the direction's acknowledged strong works or mature teams, chase their references backward and citing papers forward, then add the closest recent work. A search report returns candidates with roles, not a flat list of N papers.

## 3. Mandatory Capture

Any paper actually used (cited in a reply or document) must be saved immediately as `knowledge/papers/author-year-title.md`. Deduplicate by arXiv ID or DOI; if a note exists, update it instead of creating a copy. Searching without capturing is forbidden — that is what causes repeated searches and API bans.

Note template — paper-centric, not question-centric:

```
# Title — Authors (Year)
link: <url or arXiv ID>   pdf: <pdfs/... or "not cached">
added: <YYYY-MM-DD>   source-query: "<the query that found it>"
publication: <venue / preprint>   review-status: published | preprint | unknown
assessment-depth: metadata | abstract | full | code | reproduced
quality: strong | usable | weak | unassessed   quality-updated: <YYYY-MM-DD>

## Verdict
One plain sentence: is it worth following as an anchor, and why.
Include the single most valuable point and the biggest problem.

## Summary
What the paper itself does: problem, method, core conclusion, evidence
strength. 3-5 sentences, independent of any use case.

## Key details
- Method essentials / datasets / main numeric results / experimental
  setup, one bullet each.
- Bar: a future reader with a *different* question should rarely need
  to re-fetch the original.

## External signals
Venue/CCF level, author track record on this specific problem, adoption
by others (with query date). Auxiliary only; never overrides full reading.

## Limitations
- Weaknesses and unverified claims. Mark speculation as [speculation].

## Relevance log
- <YYYY-MM-DD>  <direction/proposal>: role (anchor | competitor |
  adjacent | background) + how it was used
```

Rules:

- **Summary and Key details describe the paper, not the current question.** Notes written only for today's question force re-retrieval when the question changes — that defeats the knowledge base.
- The Relevance log is append-only: when an existing note serves a new direction, add one line; never create a duplicate note.
- Do not paste the abstract verbatim; write in plain language.

## 4. Paper Quality Assessment

Retrieval is not a relevance list. Every paper that a direction actually depends on gets a per-paper quality judgment: role, quality, and reading depth (the three fields in the note header). Judge by the three layers in `paper-quality.md` — real relevance, intrinsic soundness (insight, evidence, theory), then external signals (venue/CCF, author track record, adoption) as auxiliary only.

Rules:

- Depth bounds the claim: from an abstract you may say "worth reading", never "solid experiments".
- Venue or famous authors cannot rescue weak evidence; unknown authors or preprints do not imply weak work.
- A quality judgment is updateable: record `quality-updated` and the reason when it changes.
- Load `paper-quality.md` when making or revising these judgments.

## 5. Index

Create or update `knowledge/papers/00-overview.md` once the directory holds more than five notes (per `research_manager` section 4). Index entries: one line per paper — citation, quality field, one-sentence takeaway, linked direction.

## 6. Boundaries

- `knowledge_keeper` retrieves, captures, indexes, and judges single-paper quality. It does not judge whether a literature gap is real or whether a direction is worth doing — that verdict belongs to `research_progress`.
- Actually call arXiv / Semantic Scholar APIs when a search is needed; never fabricate papers or citations.
- File writes only after user confirmation.
