---
id: 20260511-wiki-rebuild
title: Wiki Rebuild Workflow
type: skill
category: kb-operations
status: active
created: 2026-05-11
updated: 2026-05-11
tags:
  - kb/workflow
  - skill/wiki-rebuild
aliases:
  - wiki-rebuild
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
  - basis: Ar9av/obsidian-wiki workflow pattern
confidence:
  base: high
  notes: Local rebuild workflow.
lifecycle:
  stage: active
  review: monthly
summary: Rebuild navigation, hot knowledge, and manifest after structural changes.
links:
  related:
    - index
    - hot
    - log
    - skills/wiki-lint
---

# Wiki Rebuild Workflow

## Goal

Refresh the wiki's navigation and metadata after significant changes.

## Inputs

- All Markdown notes under `wiki/`.
- `wiki/.manifest.json`.
- Current user/project focus.

## Process

1. Run [[skills/wiki-lint]] checks conceptually.
2. Update [[index]] to reflect active knowledge areas.
3. Update [[hot]] with current high-priority notes.
4. Update `.manifest.json` with folders, required fields, workflow names, and important notes.
5. Archive obsolete notes if needed, with explicit archive reason.
6. Add a [[log]] entry summarizing the rebuild.

## Rules

- Do not delete knowledge during rebuild unless explicitly requested.
- Prefer archiving to deletion.
- Do not move files if it would break existing wikilinks unless links are updated too.
- Preserve provenance.

## Output

- Updated `index.md`.
- Updated `hot.md`.
- Updated `.manifest.json`.
- Log entry.

## Related

- [[skills/wiki-lint]]
- [[skills/wiki-status]]
