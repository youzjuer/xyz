---
id: 20260524-proj3-quant-trading-system
title: Proj3 A-share Next-day Surge Quant System
type: project
category: quant-trading-project
status: active
created: 2026-05-24
updated: 2026-05-24
tags:
  - project/proj3
  - domain/investing
  - domain/quant
  - market/a-share
  - system/trading
  - framework/backtesting
  - strategy/ultra-short
aliases:
  - 量化交易系统
  - A股次日上涨预测系统
  - Next-day Surge System
source: self
sources:
  - projects/proj3/PROJECT.md
  - projects/proj3/NOTES.md
  - projects/proj3/docs/strategy-problem-definition.md
  - projects/proj3/tasks/
  - projects/proj3/runs/
provenance:
  - user-requested: 新建一个proj，这是一个量化交易系统
  - user-specified: 在A股中挑选出第二天最有可能上涨超过5%的股票，T日预测，T+1买入并卖出；失败后复盘原因；最高约束是月收益率超过15%
  - user-specified: buy time is 14:30 on T+1; the system must monitor macro/market indicators and warn before possible broad-market sharp drops
  - date: 2026-05-24
  - agent-assisted: Claude
confidence:
  base: high
  notes: Objective and highest constraint are user-specified; implementation details and feasibility require data/backtest validation.
lifecycle:
  stage: active
  review: weekly
summary: A-share ultra-short quant project for predicting stocks likely to rise more than 5% on T+1, trading T+1, and learning through failure postmortems with monthly return >15% as the highest constraint.
links:
  references:
    - references/microsoft-qlib-financial-quant-platform
  concepts:
    - concepts/stock-recommendation-framework
    - concepts/dynamic-stock-pricing-analysis
    - concepts/a-share-sentiment-market
  synthesis:
    - synthesis/financial-services-agent-architecture
---

# Proj3 A-share Next-day Surge Quant System

## Summary

Proj3 is an A-share ultra-short quant trading project. The system predicts on day **T** which stock(s) are most likely to rise more than **5% on T+1**, buys selected stock(s) at **14:30 on T+1**, sells on **T+1**, and uses every failed trade to diagnose and improve the strategy.

## Highest constraint

**Monthly return > 15%** is the highest project constraint.

All design choices must be evaluated against this target, while avoiding fake performance from overfitting, untradeable limit-up entries, unrealistic fills, and missing risk controls.

## Repo project

- Project file: `projects/proj3/PROJECT.md`
- Notes: `projects/proj3/NOTES.md`
- Problem definition: `projects/proj3/docs/strategy-problem-definition.md`
- Task files: `projects/proj3/tasks/`
- Run outputs: `projects/proj3/runs/`
- Failure postmortem template: `projects/proj3/runs/failure-postmortem-template.md`

## Trading problem

- Market: A-shares.
- Prediction: T day.
- Target: T+1 return greater than 5%.
- Action: buy selected stock(s) at **14:30 on T+1**.
- Exit: sell on T+1 under the defined ultra-short rule after the 14:30 entry.
- Pre-trade risk gate: macro/market warning module must detect possible broad-market sharp drops and issue early warnings, block trades, or reduce exposure.
- Learning loop: if a trade fails, identify whether the cause was data, feature design, market regime, signal logic, execution, risk control, or event/news changes.

## Knowledge map

- [[references/microsoft-qlib-financial-quant-platform]] — possible research/backtest infrastructure reference.
- [[concepts/stock-recommendation-framework]] — discretionary framework to convert into short-term measurable factors.
- [[concepts/dynamic-stock-pricing-analysis]] — market-expectations and scenario framework for labeling/feature ideas.
- [[concepts/a-share-sentiment-market]] — A-share short-term sentiment/policy market logic.
- [[synthesis/financial-services-agent-architecture]] — auditable research workflow and artifact pattern.

## Current operating principles

1. The system is designed for A-share ultra-short opportunity capture, not long-term value investing.
2. The likely edge comes from sentiment, theme rotation, capital flow, price/volume behavior, event catalysts, and A-share microstructure.
3. Backtests must model A-share constraints: limit-up buyability, limit-down sellability, suspension, ST stocks, liquidity, costs, and slippage.
4. Any strategy that reaches high return only through unrealistic fills or ignoring broad-market crash risk is invalid.
5. Every false positive and missed winner should feed the failure-review loop.
6. The macro/market warning gate is a first-class risk control, not an optional dashboard.
7. Live trading remains out of scope until out-of-sample performance and risk controls prove the edge.

## Candidate architecture

```text
data source -> tradable universe filters -> macro/market warning gate -> labels -> short-term features -> model/rules -> ranked candidates -> 14:30 execution simulator -> backtest report -> failure postmortem -> strategy update
```

## Candidate feature groups

- Price/volume momentum and reversal.
- Turnover expansion and liquidity acceleration.
- Limit-up history, failed limit-up, 连板/断板 behavior.
- Sector/theme heat and rotation.
- Relative strength versus index and sector.
- Northbound/main-fund/capital-flow proxies if reliable.
- News, announcement, policy, and event proxies.
- Macro/market warning indicators: index trend, intraday drawdown, market breadth, limit-down count, volatility expansion, sector-wide selloff, northbound/large-fund flow, policy/geopolitical/overseas-market shock proxies.
- Exclusion filters: ST, suspension, illiquidity, unbuyable one-word limit-up boards, obvious liquidity traps.

## First milestone

Build a minimum viable research loop:

1. Define exact T/T+1 trading protocol, including 14:30 entry.
2. Define tradable universe and exclusion rules.
3. Choose data source and schema, including intraday 14:30 price and macro/market warning data.
4. Generate next-day >5% labels.
5. Build A-share constraint-aware backtest with 14:30 entry.
6. Build macro/market sharp-drop warning gate.
7. Implement a simple baseline strategy.
8. Compare with benchmark/random baselines.
9. Produce standard evaluation report and failure postmortems.

## Open questions

- Is entry exactly 14:30 price, 14:30-14:35 VWAP, limit order, or first executable price after 14:30?
- Is exit on T+1 close, take-profit, stop-loss, trailing, or rule-based?
- Hold one stock or a basket per day?
- Include ChiNext/STAR Market or exclude them initially?
- Which data source can reliably provide limit-up/limit-down, suspension, adjustment, sector/theme data, intraday 14:30 prices, and macro/market warning indicators?
- What max daily loss and max drawdown are acceptable while targeting monthly return >15%?
