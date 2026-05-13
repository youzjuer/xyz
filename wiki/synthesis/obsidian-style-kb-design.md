---
id: 20260505-obsidian-style-kb-design
title: Obsidian-style Knowledge Base Design
type: synthesis
category: kb-design
status: active
created: 2026-05-05
updated: 2026-05-11
tags:
  - kb/design
  - tool/obsidian
  - pattern/llm-wiki
aliases:
  - 知识库设计
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
provenance:
  - reference: https://github.com/Ar9av/obsidian-wiki
  - agent-assisted: Claude
  - date: 2026-05-05
  - updated: 2026-05-11 LLM Wiki restructuring
confidence:
  base: high
  notes: Local design decision for this repository's wiki structure.
lifecycle:
  stage: active
  review: quarterly
summary: Design rationale for keeping wiki as durable knowledge source separate from projects, rag, and memory.
links:
  skills:
    - skills/knowledge-ingest-workflow
    - skills/wiki-status
    - skills/wiki-ingest
  projects:
    - projects/proj2-stock-recommendation
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
