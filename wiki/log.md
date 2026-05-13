---
id: 20260505-log
title: Knowledge Base Log
type: journal
category: kb-operations
status: active
created: 2026-05-05
updated: 2026-05-13
tags:
  - kb/log
aliases:
  - Wiki Log
  - 知识库日志
source: self
sources: []
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
confidence:
  base: high
  notes: Operational change log.
lifecycle:
  stage: active
  review: weekly
summary: Chronological log of important wiki changes.
links:
  related:
    - index
    - hot
---

# Knowledge Base Log

## 2026-05

### 2026-05-13

- Added [[references/anthropic-financial-services]] after reviewing Anthropic's financial-services repo at commit `853f755a61f7bbb045c681327f46b354419030a1`.
- Added [[synthesis/financial-services-agent-architecture]] to capture reusable patterns for auditable financial analysis agents, skills, MCP connectors, artifact contracts, and human review gates.
- Linked the new financial-services agent notes into [[hot]], [[index]], [[projects/proj2-stock-recommendation]], and [[concepts/stock-recommendation-framework]].

### 2026-05-11

- Restructured `wiki/` toward an Agent-maintained LLM Wiki pattern inspired by `Ar9av/obsidian-wiki` and Karpathy's LLM Wiki.
- Added [[hot]], `_raw/README`, `_archives/README`, `entities/`, and `journal/` scaffolding.
- Added wiki operation workflows: [[skills/wiki-status]], [[skills/wiki-ingest]], [[skills/wiki-query]], [[skills/wiki-lint]], and [[skills/wiki-rebuild]].
- Upgraded templates with category, sources, confidence, lifecycle, summary, and links fields.
- Added [[references/microsoft-qlib-financial-quant-platform]] as a structured note on Microsoft Qlib for financial quant research.

### 2026-05-08

- Added ETF position / short-term capital-flow analysis framework to [[concepts/stock-recommendation-framework]], based on 513980 and 159995 cases.
- Updated [[index]] to highlight the ETF-aware stock recommendation framework.

### 2026-05-05

- Initialized `wiki/` as the Obsidian-style knowledge base.
- Added folder taxonomy, templates, and initial seed notes for `proj2` stock recommendation work.
