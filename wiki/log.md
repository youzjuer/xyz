---
id: 20260505-log
title: Knowledge Base Log
type: journal
category: kb-operations
status: active
created: 2026-05-05
updated: 2026-05-24
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

### 2026-05-24

- Added [[projects/proj3-quant-trading-system]] and `projects/proj3/` as the workspace for a quant trading system project.
- Refined [[projects/proj3-quant-trading-system]] into an A-share T/T+1 ultra-short system: predict stocks likely to rise more than 5% on T+1, trade on T+1, and use failed trades for postmortems.
- Recorded proj3's highest constraint: monthly return >15%.
- Updated proj3 trading protocol: buy selected stock(s) at 14:30 on T+1.
- Added macro/market sharp-drop warning as a first-class pre-trade risk gate for proj3.
- Initialized proj3 operating principles: research-first, data-quality-first, no live trading until reproducible backtests and risk controls are proven.
- Linked proj3 into [[index]], [[hot]], and `.manifest.json` active focus.

### 2026-05-14

- Added [[concepts/dynamic-stock-pricing-analysis]] to capture the corrected stock-analysis method: market expectations, scenario probability, realistic buy zones, and execution plans rather than static conservative PE targets.
- Updated [[concepts/stock-recommendation-framework]], [[stocks/README]], and [[stocks/byd/valuation-buy-zones]] so future individual-stock analysis distinguishes realistic first buy zones from stress-case opportunity prices.

### 2026-05-13

- Added [[references/anthropic-financial-services]] after reviewing Anthropic's financial-services repo at commit `853f755a61f7bbb045c681327f46b354419030a1`.
- Added [[synthesis/financial-services-agent-architecture]] to capture reusable patterns for auditable financial analysis agents, skills, MCP connectors, artifact contracts, and human review gates.
- Linked the new financial-services agent notes into [[hot]], [[index]], [[projects/proj2-stock-recommendation]], and [[concepts/stock-recommendation-framework]].
- Added `wiki/stocks/` as a long-term individual stock analysis repository.
- Added [[stocks/byd/index]] and [[stocks/byd/valuation-buy-zones]] to preserve the BYD analysis, buy zones, triggers, and caveats from the 2026-05-13 discussion.
- Added [[stocks/nhwa-pharma/index]] and [[stocks/nhwa-pharma/valuation-buy-zones]] to preserve the Nhwa Pharma analysis, valuation zones, policy risks, and review triggers from the 2026-05-13 discussion.

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
