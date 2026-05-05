---
id: 20260505-obsidian-style-kb-design
title: Obsidian-style Knowledge Base Design
type: synthesis
status: active
created: 2026-05-05
updated: 2026-05-05
tags:
  - kb/design
  - tool/obsidian
aliases:
  - 知识库设计
source: self
provenance:
  - reference: https://github.com/Ar9av/obsidian-wiki
  - agent-assisted: Claude
  - date: 2026-05-05
---

# Obsidian-style Knowledge Base Design

## Claim

This repo should use `wiki/` as the human-readable source of truth for durable knowledge, while keeping `projects/`, `rag/`, and `MEMORY.md` separate.

## Reasoning

- `projects/` tracks execution and task outputs.
- `wiki/` tracks reusable knowledge, concepts, entities, sources, and synthesis.
- `rag/` can later index selected wiki exports, but should not become the canonical knowledge source.
- `MEMORY.md` is for compact agent memory and stable preferences, not full notes.

## Structure

The vault uses folders inspired by Ar9av's Obsidian wiki pattern:

- `concepts/`
- `entities/`
- `skills/`
- `references/`
- `synthesis/`
- `journal/`
- `projects/`
- `_raw/`
- `_archives/`
- `templates/`

## Implications

New durable knowledge should go into `wiki/`, not into project run outputs. Project outputs can be linked from wiki pages when they contain reusable conclusions.

## Related

- [[skills/knowledge-ingest-workflow]]
- [[projects/proj2-stock-recommendation]]
