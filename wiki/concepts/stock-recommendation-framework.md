---
id: 20260505-stock-recommendation-framework
title: Stock Recommendation Framework
type: concept
category: investing-framework
status: active
created: 2026-05-05
updated: 2026-05-13
tags:
  - domain/investing
  - market/a-share
  - framework/scoring
  - instrument/etf
  - factor/capital-flow
  - framework/position-management
aliases:
  - 股票推荐框架
source: self
sources:
  - projects/proj2/runs/task-001/recommendation-framework-v1.md
  - projects/proj2/runs/task-007/a-share-sentiment-framework-v2.md
  - projects/proj2/runs/task-008/chip-etf-159995-position-plan.md
provenance:
  - agent-assisted: Claude
  - date: 2026-05-05
  - basis: proj2 framework files
  - updated: 2026-05-11 LLM Wiki metadata normalization
confidence:
  base: medium
  notes: Framework derived from project work and live analysis conversations; verify market data before acting.
lifecycle:
  stage: active
  review: monthly
summary: Multi-layer stock and ETF recommendation framework covering fundamentals, A-share sentiment, ETF position management, and capital flow.
links:
  concepts:
    - concepts/a-share-sentiment-market
  synthesis:
    - synthesis/financial-services-agent-architecture
  references:
    - references/anthropic-financial-services
  projects:
    - projects/proj2-stock-recommendation
---

# Stock Recommendation Framework

## Summary

The stock recommendation system has four layers:

1. A general multi-factor framework for medium-term or balanced recommendations.
2. An A-share short-term sentiment/policy framework for one-month elasticity trades.
3. An ETF position-management framework that combines holdings, valuation, policy/international context, and capital flow.
4. A financial-agent architecture layer for making research workflows auditable: reusable skills, explicit source hierarchy, artifact contracts, and human review gates.

## Framework versions

### v3: ETF position / short-term flow framework

Source: conversation analysis on 513980 and 159995, with `projects/proj2/runs/task-008/chip-etf-159995-position-plan.md` as the first task artifact.

Best for:

- ETF holding decisions, especially when the user already has a cost basis and position weight;
- short-term operation plans where valuation, policy, international conditions, and capital flow all matter;
- deciding hold / reduce / add / avoid with explicit trigger lines.

Core workflow:

1. Identify the ETF exactly: full name, manager, exchange code, tracked index, fee level, latest scale, liquidity, and premium/discount.
2. Classify the exposure: broad index, sector, theme, cross-border, commodity, bond, or high-beta product.
3. Decompose the tracked index and top holdings: concentration, industry exposure, and whether the ETF actually matches the user's intended theme.
4. Separate long-term thesis from current price: policy support, industry cycle, international constraints, domestic substitution logic, and whether valuation already prices these in.
5. Anchor the analysis to the user's position: cost basis, current price, unrealized gain/loss, required return to break even, and position weight in total assets.
6. Add short-term capital-flow checks:
   - ETF share changes and net subscription/redemption;
   - recent turnover and trading value;
   - 5/10/20-day net inflow or outflow;
   - whether price rises while ETF shares are being redeemed;
   - peer ETF inflow/outflow and product rotation;
   - whether core constituents receive synchronized inflows;
   - margin financing balance or leveraged sentiment when available.
7. Convert the evidence into an operation plan:
   - define current action: hold, reduce, add, or wait;
   - define target position after action;
   - define upside take-profit zone and downside defense line;
   - define flow triggers that confirm or invalidate the plan;
   - avoid adding simply because policy is favorable.

Capital-flow interpretation:

- Price rising + share growth or net inflow: healthier trend confirmation.
- Price rising + share decline or net redemption: likely profit-taking or存量博弈; short-term risk increases.
- Price falling + share growth: possible dip-buying, but confirm whether core holdings stabilize.
- Price falling + share redemption: weak signal; avoid aggressive averaging down.

Position-size rules:

- Light position: hold or add only in small batches after pullbacks or trend confirmation.
- Medium position: hold first, add only if capital flow and trend improve.
- Heavy position with profit: reduce part of the position and keep a底仓.
- Heavy position with loss: stop adding first; wait for rebound, then lower risk.

159995 application rule:

- Treat it as a high-volatility semiconductor theme ETF, not a core broad-market holding.
- If the user has meaningful profit and position weight near 20%, default to reducing exposure before discussing additional upside.
- If capital flow shows sustained net redemption while price rises, treat the move as a profit-taking window rather than a clean accumulation signal.
- For a 20% portfolio position with roughly 30%+ unrealized gain, reducing 25%-35% of the ETF holding is the default risk-controlled action unless the user explicitly wants aggressive exposure.

513980 application rule:

- Treat it as a Hong Kong technology/growth beta tool, not a pure AI ETF.
- If the user is underwater but position weight is not high, holding is acceptable; avoid blind averaging down unless valuation, capital flow, and portfolio weight all support it.

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
- [[synthesis/financial-services-agent-architecture]]
- [[references/anthropic-financial-services]]
- [[projects/proj2-stock-recommendation]]

## Rule

When the user asks for a one-month A-share recommendation, default to v2 unless they explicitly ask for fundamental or long-term analysis.
