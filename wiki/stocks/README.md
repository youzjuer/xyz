---
id: 20260513-stocks-index
title: Stock Analysis Repository
type: index
category: investing-research
status: active
created: 2026-05-13
updated: 2026-05-14
tags:
  - domain/investing
  - kb/navigation
  - stock-research
aliases:
  - 个股长期分析仓库
  - Stocks
source: self
sources: []
provenance:
  - agent-assisted: Claude
  - date: 2026-05-13
  - basis: user requested a long-term repository for individual stock analysis
confidence:
  base: high
  notes: Navigation page for stock-specific long-term analysis notes.
lifecycle:
  stage: active
  review: monthly
summary: Entry point for durable long-term individual stock analysis folders.
links:
  stocks:
    - stocks/byd/index
    - stocks/nhwa-pharma/index
  concepts:
    - concepts/stock-recommendation-framework
    - concepts/dynamic-stock-pricing-analysis
  projects:
    - projects/proj2-stock-recommendation
---

# Stock Analysis Repository

这是个股长期分析仓库。每个股票使用独立子目录，沉淀长期跟踪逻辑、估值区间、买点、风险线、历史判断和来源证据。

## Stocks

- [[stocks/byd/index]] — 比亚迪 / BYD / 002594.SZ / 1211.HK
- [[stocks/nhwa-pharma/index]] — 恩华药业 / Nhwa Pharma / 002262.SZ

## Folder convention

```text
wiki/stocks/<slug>/
  index.md                # 个股主档案
  valuation-buy-zones.md  # 估值与买点区间
  thesis.md               # 长期逻辑和反证条件，可选
  updates/                # 后续季度或事件更新，可选
```

## Use rules

- 区分事实、判断和操作建议。
- 先判断市场已经 pricing 什么、核心分歧是什么，再给价格。
- 买点必须区分现实首买区、加仓区、压力情景机会区，不能只给一个静态低价。
- 对每个买点判断其出现概率：基准情景、负面叠加情景，还是恐慌情景。
- 记录数据来源、捕获日期和估值口径。
- 个股档案用于长期复用；临时交易想法放入项目 run 或 journal。

## Related

- [[concepts/stock-recommendation-framework]]
- [[concepts/dynamic-stock-pricing-analysis]]
- [[projects/proj2-stock-recommendation]]
