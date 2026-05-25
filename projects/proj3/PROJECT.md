# Proj3 A-share Next-day Surge Quant System

## Goal

Build a quant trading system for A-shares that predicts on trading day **T** which stocks are most likely to rise more than **5% on T+1**, buys the selected stock(s) at **14:30 on T+1**, and exits on **T+1** under an ultra-short holding period.

The system must continuously learn from failed trades by diagnosing whether the error came from data, features, market regime, signal design, execution, risk control, or post-signal event changes.

## Highest constraint

**Final required objective: monthly return > 15%.**

This is the highest project constraint. All architecture, data, strategy, risk control, and review choices must be judged against whether they improve the probability of reaching this objective without relying on unmeasured luck.

## Trading problem definition

- Market: A-shares.
- Prediction time: T day after data is available.
- Target: identify stocks likely to rise **>5% on T+1**.
- Action: buy selected stock(s) at **14:30 on T+1**.
- Exit: sell on T+1 according to the ultra-short plan after the 14:30 entry.
- Pre-trade risk gate: monitor macro/market indicators; if a broad-market sharp drop risk is detected, issue an early warning and block or reduce trades.
- Style: high-conviction, short-horizon, event/sentiment/capital-flow driven.
- Primary evaluation: realized monthly return, hit rate, average win/loss, max drawdown, turnover, slippage sensitivity, and failure diagnosis quality.

## Required learning loop

Every failed trade must produce a post-mortem:

1. What did the model predict?
2. What actually happened on T+1?
3. Was the failure due to market-wide regime, sector rotation, individual stock news, liquidity, execution, false signal, or risk filter failure?
4. Which feature or rule was misleading?
5. What rule, feature, filter, or position-sizing change should be tested next?
6. Does the failure reveal overfitting or a structural weakness?

## Initial scope

1. Define A-share tradable universe and exclusions.
2. Build a daily data pipeline with prices, volume, turnover, limit-up/limit-down status, market/sector data, and event/news proxies where available.
3. Build labels for next-day return >5% and related variants.
4. Build a backtest that respects A-share trading constraints, including 14:30 entry, limit-up buyability, limit-down sellability, suspension, liquidity, transaction costs, and slippage.
5. Build a macro/market crash-warning module that can issue warnings before broad-market sharp declines and act as a pre-trade risk gate.
6. Implement baseline strategies and models for next-day surge prediction.
7. Add a review system for failed predictions and missed winners.
8. Evaluate whether the strategy can plausibly target monthly return >15% after costs and drawdowns.

## Current assumptions

- This is not a long-term value strategy; it is an A-share ultra-short strategy.
- The edge is likely to come from sentiment, capital flow, theme rotation, event catalysts, microstructure, and crowd behavior rather than slow fundamental factors.
- Backtest correctness is critical because T+1 >5% signals are easy to overfit.
- Live trading remains out of scope until simulated results survive strict out-of-sample and failure-review tests.
- Any strategy that reaches high return only through untradeable limit-up entries, illiquid names, unrealistic fills, or ignoring broad-market crash risk is invalid.

## Architecture candidates

- Data ingestion and storage.
- Tradable-universe and exclusion engine.
- Label generation for next-day surge events.
- Feature/factor pipeline focused on short-term A-share behavior.
- Model/rule engine for ranking candidates on T.
- Execution simulator for 14:30 T+1 entry and T+1 exit.
- Backtest engine with A-share constraints.
- Macro/market crash-warning module as a pre-trade risk gate.
- Risk control and position sizing.
- Failure post-mortem system.
- Experiment registry and daily review report.

## Candidate feature groups

- Price/volume momentum and reversal.
- Turnover expansion and liquidity acceleration.
- Limit-up history, failed limit-up, board height, 连板/断板 behavior.
- Sector/theme heat and rotation.
- Relative strength versus index and sector.
- Intraday shape if intraday data becomes available.
- Northbound/main-fund/capital-flow proxies if reliable.
- News, announcements, policy, and event proxies.
- Macro and market-risk indicators: index trend, index drawdown, market breadth, limit-down count, volatility expansion, northbound/large-fund flow, sector-wide selloff, policy/geopolitical shock proxies.
- Exclusion filters: ST, suspended, illiquid, near-limit unbuyable, obvious one-word-board traps.

## Open questions

- Which stock universe first: full A-share, only main board, exclude STAR/ChiNext, or include all non-ST liquid names?
- How exactly is “buy at 14:30 on T+1” executed: exact 14:30 price, 14:30-14:35 VWAP, limit order, or strategy-specific trigger?
- How exactly is “sell on T+1” defined: close, take-profit, stop-loss, trailing, or time-based exit?
- How many stocks can be held per day?
- Max single-stock position size and max daily loss?
- What data source can reliably support limit-up/limit-down, suspension-aware backtests, 14:30 intraday prices, market breadth, and macro/market warning indicators?
- Should the first baseline be rule-based, ML ranking, or hybrid?
