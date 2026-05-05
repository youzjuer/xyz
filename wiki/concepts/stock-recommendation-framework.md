---
id: 20260505-stock-recommendation-framework
title: Stock Recommendation Framework
type: concept
status: active
created: 2026-05-05
updated: 2026-05-05
tags:
  - domain/investing
  - market/a-share
  - framework/scoring
aliases:
  - 股票推荐框架
source: self
provenance:
  - agent-assisted: Claude
  - date: 2026-05-05
  - basis: proj2 framework files
---

# Stock Recommendation Framework

## Summary

The stock recommendation system has two layers:

1. A general multi-factor framework for medium-term or balanced recommendations.
2. An A-share short-term sentiment/policy framework for one-month elasticity trades.

## Framework versions

### v1: multi-factor / balanced

Source: `projects/proj2/runs/task-001/recommendation-framework-v1.md`

Best for:

- medium-term recommendations;
- avoiding low-quality companies;
- comparing fundamental quality, valuation, growth, price behavior, sentiment, catalysts, and risk.

### v2: A-share short-term sentiment/policy

Source: `projects/proj2/runs/task-007/a-share-sentiment-framework-v2.md`

Best for:

- A-share one-month trades;
- 5%-15% target elasticity;
- policy, event, capital flow, and market sentiment driven opportunities.

## Related concepts

- [[concepts/a-share-sentiment-market]]
- [[projects/proj2-stock-recommendation]]

## Rule

When the user asks for a one-month A-share recommendation, default to v2 unless they explicitly ask for fundamental or long-term analysis.
