---
id: 20260511-archives-readme
title: Wiki Archives
type: reference
category: kb-operations
status: active
created: 2026-05-11
updated: 2026-05-11
tags:
  - kb/archive
aliases:
  - Archives
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
summary: Rules for archiving obsolete wiki notes without deleting useful context.
links:
  skills:
    - skills/wiki-lint
    - skills/wiki-rebuild
---

# Wiki Archives

`wiki/_archives/` stores obsolete, superseded, or intentionally retired knowledge that should no longer appear in normal navigation.

## Archive when

- A note is superseded by a better synthesis.
- A project is closed and no longer active.
- A framework is obsolete but historically useful.
- A reference is stale and should not guide decisions.

## Rules

- Prefer updating stale notes before archiving.
- Preserve provenance and links when archiving.
- Add an archive reason near the top of the archived note.
- Remove archived notes from [[hot]] and active index sections.

Related: [[skills/wiki-lint]], [[skills/wiki-rebuild]].
