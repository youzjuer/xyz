---
id: 20260511-wiki-query
title: Wiki Query Workflow
type: skill
category: kb-operations
status: active
created: 2026-05-11
updated: 2026-05-11
tags:
  - kb/workflow
  - skill/wiki-query
aliases:
  - wiki-query
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
  - basis: Ar9av/obsidian-wiki workflow pattern
confidence:
  base: high
  notes: Local workflow adapted from upstream query pattern.
lifecycle:
  stage: active
  review: monthly
summary: Answer questions from existing wiki knowledge before doing fresh research.
links:
  related:
    - hot
    - index
    - skills/wiki-status
---

# Wiki Query Workflow

## Goal

Use the wiki as the first source for durable project knowledge.

## Inputs

- User question.
- Current [[hot]] pages.
- Relevant pages from `index.md` and linked notes.

## Process

1. Start from [[hot]] for active topics.
2. Use [[index]] for broad navigation.
3. Follow wikilinks from relevant notes.
4. Distinguish:
   - facts recorded in wiki;
   - interpretations from synthesis notes;
   - stale or unverified claims.
5. If the answer depends on current market/code state, verify with live sources or current files.
6. If the query reveals missing durable knowledge, create a follow-up ingest task.

## Output

A concise answer that includes:

- relevant wiki sources;
- whether current verification is needed;
- suggested next action if knowledge is missing.

## Rules

- Do not treat old wiki notes as live market data.
- Do not cite memory as proof of current state.
- Prefer linked notes over disconnected raw files.

## Related

- [[skills/wiki-ingest]]
- [[skills/wiki-status]]
