---
id: 20260511-wiki-status
title: Wiki Status Workflow
type: skill
category: kb-operations
status: active
created: 2026-05-11
updated: 2026-05-11
tags:
  - kb/workflow
  - skill/wiki-status
aliases:
  - wiki-status
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
  - basis: Ar9av/obsidian-wiki workflow pattern
confidence:
  base: high
  notes: Local workflow adapted from the upstream pattern.
lifecycle:
  stage: active
  review: monthly
summary: Check wiki health, active focus, missing metadata, and stale notes.
links:
  related:
    - hot
    - log
    - skills/wiki-lint
---

# Wiki Status Workflow

## Goal

Give a fast health report for the wiki before adding or changing knowledge.

## Inputs

- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
- `wiki/.manifest.json`
- Target folders under `wiki/`

## Checks

1. Confirm core files exist: `index.md`, `hot.md`, `log.md`, `.manifest.json`.
2. Confirm core folders exist: `concepts`, `entities`, `references`, `synthesis`, `journal`, `projects`, `skills`, `templates`, `_raw`, `_archives`.
3. Identify active focus pages from [[hot]].
4. Check whether new or changed notes have frontmatter.
5. Flag missing provenance for `references/` notes.
6. Flag stale notes whose `updated` date is old relative to their lifecycle.
7. Report unlinked important notes that should be reachable from [[index]] or [[hot]].

## Output

A concise report:

```text
Wiki status: healthy / needs attention
Missing files:
Stale notes:
Notes missing metadata:
Suggested next actions:
```

## Related

- [[skills/wiki-lint]]
- [[skills/wiki-rebuild]]
