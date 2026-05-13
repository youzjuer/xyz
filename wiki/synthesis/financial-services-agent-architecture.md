---
id: 20260513-financial-services-agent-architecture
title: Financial Services Agent Architecture
type: synthesis
category: ai-agent-architecture
status: active
created: 2026-05-13
updated: 2026-05-13
tags:
  - domain/financial-services
  - domain/investing
  - framework/agent
  - framework/mcp
  - framework/human-in-loop
aliases:
  - 金融服务 Agent 架构
  - Financial agent architecture
source: self
sources:
  - references/anthropic-financial-services
  - https://github.com/anthropics/financial-services
provenance:
  - agent-assisted: Claude
  - date: 2026-05-13
  - basis: synthesis of Anthropic financial-services repository at commit 853f755a61f7bbb045c681327f46b354419030a1
confidence:
  base: medium
  notes: Architecture patterns are derived from a reference repo and should be adapted to local data availability, regulation, and A-share market structure.
lifecycle:
  stage: active
  review: quarterly
summary: Reusable architecture patterns from Anthropic's financial-services repo for building auditable, human-reviewed financial analysis agents.
links:
  concepts:
    - concepts/stock-recommendation-framework
    - concepts/a-share-sentiment-market
  references:
    - references/anthropic-financial-services
  projects:
    - projects/proj2-stock-recommendation
---

# Financial Services Agent Architecture

## Summary

Anthropic's financial-services repo suggests a practical architecture for serious financial analysis agents:

```text
canonical agent prompt
+ reusable vertical skills
+ governed data connectors
+ explicit artifact contracts
+ specialist leaf workers
+ human review checkpoints
= auditable financial work product
```

The most important idea is not any single valuation method. It is the separation between **analysis production** and **decision authority**: agents draft models, memos, notes, reconciliations, and reports; humans approve, publish, trade, post, or onboard.

## Claim

For [[projects/proj2-stock-recommendation]], the best reuse is to evolve from a single stock-picking prompt into a small set of auditable research workflows with source hierarchy, intermediate artifacts, and explicit approval gates.

## Evidence

From [[references/anthropic-financial-services]]:

- The repo packages workflows as named agents such as `market-researcher`, `earnings-reviewer`, `model-builder`, `pitch-agent`, and `gl-reconciler`.
- The same canonical agent prompt and skills can run as a Claude plugin or as a Claude Managed Agent cookbook.
- Vertical skills are the source of truth; agent plugins bundle synced copies for self-contained installation.
- `financial-analysis/.mcp.json` centralizes institutional data connectors.
- Agent prompts repeatedly require sourced numbers, human review, and no external distribution or execution.
- Managed Agent cookbooks isolate tools: orchestrators coordinate; leaf workers hold narrowly scoped tools; usually only one leaf worker has `Write`.
- `comps-analysis` prioritizes verified MCP/institutional data over web search for financial/trading information.
- `xlsx-author` defines a concrete output contract and spreadsheet audit conventions.

## Reasoning

### 1. Build workflows, not generic chat

A stock recommendation request should decompose into repeatable steps:

1. Universe and mandate clarification.
2. Data collection with source priority.
3. Candidate screening.
4. Thesis and catalyst analysis.
5. Valuation / price-position analysis.
6. Capital-flow and sentiment analysis.
7. Risk and invalidation line.
8. Final recommendation and operation plan.

This is closer to `market-researcher` + `earnings-reviewer` + `model-builder` than to a generic chatbot answer.

### 2. Separate reusable skills from workflow agents

Reusable skills for this repo could become:

- A-share sentiment scan.
- ETF position / capital-flow analysis.
- Earnings catalyst review.
- Peer-comps and relative valuation.
- Risk line and position-sizing plan.
- Source-quality audit.

Workflow agents could then compose those skills:

- One-month A-share opportunity researcher.
- ETF holding/reduce/add advisor.
- Earnings-event reviewer.
- Sector/theme market researcher.

### 3. Treat data provenance as part of the output

Financial agents should not only answer “buy/hold/sell”. They should show:

- which data source was used;
- whether the source is live, delayed, manual, or web-derived;
- what period the data covers;
- which figures are estimated;
- what would change the conclusion.

The `comps-analysis` skill's institutional data hierarchy is not directly portable to A-shares, but the principle is: prefer auditable market/filing/data-provider sources over generic search snippets.

### 4. Make artifacts auditable

When generating spreadsheets or reports:

- raw inputs should be separate from calculations;
- calculation cells should be formulas, not hardcoded numbers;
- source comments or notes should exist for hardcoded inputs;
- output paths and formats should be explicit;
- the final message should point to generated artifacts.

This matters for any future backtest workbook, ETF rotation dashboard, or recommendation scorecard.

### 5. Use human-in-the-loop gates at decision boundaries

The financial-services repo places review gates after major artifacts and keeps regulated actions outside the agent. For this project, useful gates are:

- after candidate shortlist, before deep analysis;
- after data collection, before conclusion;
- before acting on a trade plan;
- before publishing or sharing any recommendation externally.

This does not mean every conversation must be slow. It means high-consequence transitions should be explicit.

### 6. Isolate tools and untrusted inputs

Third-party reports, PDFs, issuer material, broker notes, and web pages should be treated as untrusted data. They can be summarized or cited, but should not provide operational instructions to the agent.

If the project later gains connectors or broker/execution tools, they should not be available to the same worker that reads untrusted documents.

## Implications for this wiki

The current [[concepts/stock-recommendation-framework]] already has A-share sentiment and ETF position-management layers. The next architecture step is to split it into reusable operational skills rather than expanding one long framework page indefinitely.

Potential future pages:

- `skills/a-share-opportunity-research`
- `skills/etf-position-review`
- `skills/financial-source-audit`
- `synthesis/a-share-research-agent-design`

Do not copy Anthropic's US institutional workflows mechanically. Reuse the architecture, not the market assumptions.

## Counterpoints

- The repo assumes access to institutional MCP data providers such as FactSet, Daloopa, Morningstar, S&P Global, or LSEG; this project may rely on delayed public A-share data.
- A-share short-term trades are more sensitive to policy, liquidity, retail sentiment, daily limit mechanics, and theme rotation than US-style valuation workflows.
- Multi-agent orchestration may be overkill until the data pipeline and recommendation criteria are stable.
- Human review gates can reduce speed if placed after every small step; use them at risk boundaries, not for every minor calculation.

## Practical adoption path

1. Keep [[concepts/stock-recommendation-framework]] as the master analytical framework.
2. Extract one concrete skill first: ETF position review, because the current framework already defines holdings, valuation, capital flow, and position triggers.
3. Add a source-quality section to every recommendation output.
4. For generated spreadsheets, follow the `xlsx-author` idea: `Inputs`, calculations, checks, and clear output path.
5. Only after the workflow stabilizes, consider separate agents for researcher, scorer, critic, and report-writer.

## Related

- [[references/anthropic-financial-services]]
- [[concepts/stock-recommendation-framework]]
- [[concepts/a-share-sentiment-market]]
- [[projects/proj2-stock-recommendation]]
