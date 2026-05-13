---
id: 20260511-hot
title: Hot Knowledge
type: index
category: navigation
status: active
created: 2026-05-11
updated: 2026-05-13
tags:
  - kb/navigation
  - kb/hot
aliases:
  - Hot
  - 当前重点知识
source: self
sources: []
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
confidence:
  base: high
  notes: Curated navigation page for active knowledge.
lifecycle:
  stage: active
  review: weekly
summary: Current high-priority wiki pages for agent and user workflows.
links:
  concepts:
    - concepts/stock-recommendation-framework
    - concepts/a-share-sentiment-market
  references:
    - references/microsoft-qlib-financial-quant-platform
    - references/anthropic-financial-services
  synthesis:
    - synthesis/financial-services-agent-architecture
  projects:
    - projects/proj2-stock-recommendation
---

# Hot Knowledge

当前高频使用的知识入口。Agent 查询投资、ETF、量化、知识库结构时优先从这里开始。

## Investing and ETF analysis

- [[concepts/stock-recommendation-framework]] — 股票/ETF 推荐与仓位管理框架，包含 ETF 资金流分析。
- [[concepts/a-share-sentiment-market]] — A 股短期情绪/政策市判断模型。
- [[projects/proj2-stock-recommendation]] — 股票推荐项目知识地图。

## Financial quant and agent architecture

- [[references/microsoft-qlib-financial-quant-platform]] — Microsoft Qlib 金融量化研究平台调研。
- [[references/anthropic-financial-services]] — Anthropic 金融服务 Agent / 插件 / Managed Agent 参考仓库调研。
- [[synthesis/financial-services-agent-architecture]] — 金融分析 Agent 的可审计架构模式。

## Knowledge base operations

- [[skills/knowledge-ingest-workflow]] — 知识入库主流程。
- [[skills/wiki-status]] — 检查 wiki 健康状态。
- [[skills/wiki-ingest]] — 原始材料入库流程。
- [[skills/wiki-query]] — 查询 wiki 的流程。
- [[skills/wiki-lint]] — 检查断链、元数据和过期内容。
- [[skills/wiki-rebuild]] — 重建索引、hot 和 manifest。
