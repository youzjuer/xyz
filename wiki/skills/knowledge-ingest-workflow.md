---
id: 20260505-knowledge-ingest-workflow
title: Knowledge Ingest Workflow
type: skill
category: kb-operations
status: active
created: 2026-05-05
updated: 2026-05-11
tags:
  - kb/workflow
  - skill/knowledge-management
aliases:
  - 知识入库流程
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
provenance:
  - agent-assisted: Claude
  - date: 2026-05-05
  - basis: obsidian-wiki inspired workflow
  - updated: 2026-05-11 LLM Wiki metadata normalization
confidence:
  base: high
  notes: Operational workflow for durable knowledge ingestion.
lifecycle:
  stage: active
  review: monthly
summary: Main workflow for turning raw information into durable, linked, sourced wiki knowledge.
links:
  synthesis:
    - synthesis/obsidian-style-kb-design
  skills:
    - skills/wiki-ingest
    - skills/wiki-query
    - skills/wiki-lint
---

# Knowledge Ingest Workflow

## Goal

Turn raw information into durable, linked, sourced knowledge.

## Steps

1. Put raw source in `wiki/_raw/` only if it is safe, lightweight, and commit-appropriate.
2. Create a `wiki/references/` note for external articles, reports, papers, webpages, or books.
3. Record source URL, captured date, and provenance.
4. Extract durable ideas into `wiki/concepts/`.
5. Create or update relevant `wiki/entities/` pages.
6. Write conclusions or decision memos in `wiki/synthesis/`.
7. Link notes with Obsidian wikilinks.
8. Add a short entry to [[log]].

## Rules

- Do not put secrets, credentials, cookies, tokens, account data, or large private files in `_raw/`.
- Important claims need sources.
- `references/` notes must include provenance.
- `synthesis/` should separate claim, reasoning, counterpoints, and implications.

## Related

- [[synthesis/obsidian-style-kb-design]]
