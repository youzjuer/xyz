---
id: 20260511-wiki-ingest
title: Wiki Ingest Workflow
type: skill
category: kb-operations
status: active
created: 2026-05-11
updated: 2026-05-11
tags:
  - kb/workflow
  - skill/wiki-ingest
aliases:
  - wiki-ingest
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
  - basis: Karpathy LLM Wiki and Ar9av/obsidian-wiki patterns
confidence:
  base: high
  notes: Operational workflow for this repository.
lifecycle:
  stage: active
  review: monthly
summary: Convert raw or external information into durable, sourced, linked wiki notes.
links:
  related:
    - _raw/README
    - skills/knowledge-ingest-workflow
    - skills/wiki-query
---

# Wiki Ingest Workflow

## Goal

Turn raw information into durable, linked, sourced knowledge.

## Inputs

- User request.
- URLs, PDFs, reports, code repositories, screenshots, or local files.
- Existing notes in `wiki/`.

## Process

1. Determine the destination type:
   - `references/` for external sources.
   - `concepts/` for reusable ideas and frameworks.
   - `entities/` for companies, funds, people, tools, and organizations.
   - `synthesis/` for integrated judgments or decision memos.
   - `projects/` for project knowledge maps.
   - `journal/` for time-bound observations.
2. If raw material must be staged, place only safe lightweight material under `_raw/`.
3. Create or update the target note using the current template schema.
4. Include source URLs and captured date for external claims.
5. Separate facts, interpretation, and open questions.
6. Add Obsidian wikilinks to related notes.
7. Update [[hot]] if the note becomes current focus.
8. Add a short entry to [[log]].

## Quality bar

- Durable knowledge only; avoid temporary task chatter.
- No secrets or private account data.
- Important claims need provenance.
- Prefer updating an existing note over duplicating it.

## Output

- New or updated wiki note.
- Log entry.
- Optional hot/index update.

## Related

- [[skills/knowledge-ingest-workflow]]
- [[skills/wiki-query]]
- [[skills/wiki-lint]]
