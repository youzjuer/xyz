---
id: 20260511-wiki-lint
title: Wiki Lint Workflow
type: skill
category: kb-operations
status: active
created: 2026-05-11
updated: 2026-05-11
tags:
  - kb/workflow
  - skill/wiki-lint
aliases:
  - wiki-lint
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
  - basis: Ar9av/obsidian-wiki workflow pattern
confidence:
  base: high
  notes: Local lint workflow.
lifecycle:
  stage: active
  review: monthly
summary: Audit wiki notes for missing metadata, broken structure, stale pages, and navigation gaps.
links:
  related:
    - skills/wiki-status
    - skills/wiki-rebuild
---

# Wiki Lint Workflow

## Goal

Keep the wiki coherent, navigable, and safe for agent use.

## Checks

1. Frontmatter exists on every non-template Markdown note.
2. Required fields are present:
   - `id`
   - `title`
   - `type`
   - `category`
   - `status`
   - `created`
   - `updated`
   - `tags`
   - `source`
   - `provenance`
   - `confidence`
   - `lifecycle`
   - `summary`
   - `links`
3. `references/` notes include external source URLs.
4. Active notes are reachable from [[index]], [[hot]], or another active note.
5. Archived notes are not listed as active focus.
6. No secrets or sensitive private data appear under `_raw/`.
7. Stale notes are flagged for update or archive.

## Output

```text
Lint result: pass / warnings / fail
Missing metadata:
Potential broken links:
Stale notes:
Unsafe raw files:
Recommended fixes:
```

## Related

- [[skills/wiki-status]]
- [[skills/wiki-rebuild]]
