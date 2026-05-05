---
id: 20260505-a-share-sentiment-market
title: A-share Sentiment and Policy Market
type: concept
status: active
created: 2026-05-05
updated: 2026-05-05
tags:
  - market/a-share
  - domain/investing
  - concept/sentiment
aliases:
  - A股情绪市
  - A股政策市
source: self
provenance:
  - user-stated: A股可能对于基本面的参考没有美股大，更可能是情绪市场和政策市场
  - date: 2026-05-05
  - agent-assisted: Claude
---

# A-share Sentiment and Policy Market

## Summary

For short A-share timeframes, especially around one month, price movement may be driven more by policy expectations, theme strength, capital flows, and sentiment than by fundamental valuation alone.

## Practical implication

For one-month A-share stock recommendations:

- policy/event catalysts should carry high weight;
- capital flow and volume behavior should carry high weight;
- theme position and narrative spread matter;
- fundamentals should still be used as a risk filter;
- valuation should be a risk-control factor, not the sole decision driver.

## Recommended weights

See `projects/proj2/runs/task-007/a-share-sentiment-framework-v2.md`.

Core weights:

- policy/event catalyst: 20%
- capital sentiment: 20%
- price-volume behavior: 20%
- theme strength: 15%
- industry growth: 10%
- fundamental risk filter: 10%
- valuation/risk control: 5%

## Caution

Do not recommend a stock merely because the user mentioned it. User-provided tickers are candidates to test, not preferences to satisfy.

## Related

- [[concepts/stock-recommendation-framework]]
- [[projects/proj2-stock-recommendation]]
