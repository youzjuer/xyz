---
id: 20260505-index
title: Knowledge Base Index
type: index
category: navigation
status: active
created: 2026-05-05
updated: 2026-05-24
tags:
  - kb/navigation
aliases:
  - Wiki Index
  - 知识库入口
source: self
sources:
  - https://github.com/Ar9av/obsidian-wiki
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
provenance:
  - agent-assisted: Claude
  - date: 2026-05-11
  - basis: Ar9av/obsidian-wiki and Karpathy LLM Wiki pattern
confidence:
  base: high
  notes: Main navigation page maintained by agent.
lifecycle:
  stage: active
  review: weekly
summary: Main entry point for the Obsidian-style LLM Wiki.
links:
  hot:
    - hot
  stocks:
    - stocks/README
    - stocks/byd/index
    - stocks/nhwa-pharma/index
  concepts:
    - concepts/dynamic-stock-pricing-analysis
  operations:
    - skills/wiki-status
    - skills/wiki-ingest
    - skills/wiki-query
    - skills/wiki-lint
    - skills/wiki-rebuild
---

# Knowledge Base Index

这是当前仓库的 Obsidian / LLM Wiki 入口。结构参考 `Ar9av/obsidian-wiki` 和 Karpathy 的 LLM Wiki 模式：原始资料进入 `_raw/`，Agent 将其编译为带 provenance 的 Markdown 知识页，并维护 `index`、`hot`、`log` 和 manifest。

## Start here

- [[hot]] — 当前重点知识入口。
- [[log]] — 知识库变更记录。
- [[skills/knowledge-ingest-workflow]] — 知识入库主流程。
- [[synthesis/obsidian-style-kb-design]] — 本仓库知识库设计说明。

## Current focus

- [[projects/proj2-stock-recommendation]] — 股票推荐项目知识地图。
- [[projects/proj3-quant-trading-system]] — 量化交易系统项目知识地图。
- [[concepts/stock-recommendation-framework]] — 股票/ETF 推荐框架，包含 ETF 仓位与资金流分析。
- [[concepts/dynamic-stock-pricing-analysis]] — 动态个股定价方法：市场预期、场景概率和现实买点。
- [[stocks/byd/index]] — 比亚迪长期个股分析档案与买点框架。
- [[stocks/nhwa-pharma/index]] — 恩华药业长期个股分析档案与买点框架。
- [[references/microsoft-qlib-financial-quant-platform]] — Microsoft Qlib 金融量化研究平台调研。
- [[references/anthropic-financial-services]] — Anthropic 金融服务 Agent / 插件 / Managed Agent 参考仓库调研。
- [[synthesis/financial-services-agent-architecture]] — 金融分析 Agent 的可审计架构模式。
- [[concepts/a-share-sentiment-market]] — A 股短期情绪/政策市框架。

## Areas

- `concepts/`：长期概念、框架、模型。
- `entities/`：公司、股票、ETF、人物、组织、工具等实体。
- `skills/`：可复用知识工作流。
- `references/`：带来源的文章、报告、网页、书籍、论文笔记。
- `synthesis/`：综合判断、决策 memo、知识地图。
- `journal/`：日期型观察、临时记录、阶段性市场记录。
- `stocks/`：个股长期分析仓库，每个股票独立子目录。
- `projects/`：项目知识地图，链接到 `projects/<project>/`。
- `_raw/`：未加工输入，仅放安全、轻量、可提交材料。
- `_archives/`：过期或废弃知识。
- `templates/`：新笔记模板。

## Wiki workflows

- [[skills/wiki-status]] — 检查 wiki 健康状态。
- [[skills/wiki-ingest]] — 把新资料整理进 wiki。
- [[skills/wiki-query]] — 查询已有知识。
- [[skills/wiki-lint]] — 检查断链、缺字段、过期内容。
- [[skills/wiki-rebuild]] — 重建索引、hot 和 manifest。

## Boundaries

- `wiki/` 是长期知识库源头。
- `projects/` 是项目执行和任务产物空间。
- `rag/` 是检索、索引和导出产物空间，不是知识库本体。
- `MEMORY.md` 是 Agent 长期记忆索引，不保存完整知识内容。

## Maintenance

新增重要笔记后：

1. 使用当前模板 schema。
2. 写清 provenance 和 confidence。
3. 添加 Obsidian wikilinks。
4. 必要时更新 [[hot]]。
5. 在 [[log]] 记录一条简短变更。
