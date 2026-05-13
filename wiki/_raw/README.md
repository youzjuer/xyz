---
id: 20260511-raw-readme
title: Raw Source Staging
type: reference
category: kb-operations
status: active
created: 2026-05-11
updated: 2026-05-11
tags:
  - kb/raw
  - kb/ingest
aliases:
  - Raw staging
source: self
sources: []
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
confidence:
  base: high
  notes: Operational rule page.
lifecycle:
  stage: active
  review: quarterly
summary: Rules for storing raw materials before they are compiled into wiki notes.
links:
  skills:
    - skills/wiki-ingest
    - skills/knowledge-ingest-workflow
---

# Raw Source Staging

`wiki/_raw/` is only for safe, lightweight, commit-appropriate source material that still needs to be compiled into durable wiki notes.

## Allowed

- Public URLs summarized as Markdown.
- Small excerpts from public reports with source links.
- Short user-provided notes that are meant to become durable knowledge.
- Non-sensitive CSV/JSON snippets used for knowledge extraction.

## Not allowed

- Secrets, credentials, cookies, tokens, API keys, account exports.
- Large binaries or private documents.
- Brokerage account data or personally sensitive financial records.
- Temporary task logs that belong in `projects/` or `runs/`.

## Workflow

1. Place source material here only when it is safe and useful.
2. Create a `references/` note with provenance.
3. Extract stable ideas into `concepts/`, `entities/`, or `synthesis/`.
4. Link the derived notes back to the source.
5. Archive or delete raw staging material when no longer needed.

Related: [[skills/wiki-ingest]], [[skills/knowledge-ingest-workflow]].
