---
id: 20260505-proj2-stock-recommendation
title: Proj2 Stock Recommendation
type: project
status: active
created: 2026-05-05
updated: 2026-05-05
tags:
  - project/proj2
  - domain/investing
  - market/a-share
aliases:
  - 股票推荐项目
source: self
provenance:
  - agent-assisted: Claude
  - date: 2026-05-05
  - basis: repo project files and user discussion
---

# Proj2 Stock Recommendation

## Repo project

- Project file: `projects/proj2/PROJECT.md`
- Notes: `projects/proj2/NOTES.md`
- Task files: `projects/proj2/tasks/`
- Run outputs: `projects/proj2/runs/`

## Knowledge map

- [[concepts/stock-recommendation-framework]]
- [[concepts/a-share-sentiment-market]]

## Current operating principle

For A-share short-term recommendations, do not mechanically copy US-style fundamental weighting. Use the A-share short-term sentiment/policy framework when the target is around one month and the user is seeking 5%-15% elasticity.

## Related project outputs

- `projects/proj2/runs/task-001/recommendation-framework-v1.md`
- `projects/proj2/runs/task-007/a-share-sentiment-framework-v2.md`
- `projects/proj2/runs/task-007/short-term-reevaluation.md`

## Open questions

- Should the stock universe exclude STAR Market, ChiNext, or only specific risk profiles?
- Should future recommendations use live market data, or only public delayed web data?
- What maximum drawdown is acceptable for a one-month elasticity trade?
