# Current Trading Strategy

## Objective

This is an A-share T+1 ultra-short momentum strategy.

The strategy generates a stock pick after trading day T data is available, buys the selected stock on T+1 at around 14:30, and exits near the T+1 close.

The project-level target remains monthly return greater than 15%, but the current strategy is only a baseline plus one failure-driven filter. It is not yet production-ready.

## Trading Protocol

- Prediction time: after T-day daily data is available.
- Entry: T+1 14:30.
- Current backtest entry proxy: Sina 30-minute K-line 14:30 bar close.
- Exit: T+1 near close.
- Current backtest exit proxy: Sina 30-minute K-line 15:00 bar close.
- Position count: one top-ranked stock per trading day.
- Transaction cost: 8 bps round trip.

## Universe And Basic Filters

The current stock universe is broad A-share coverage based on exchange lists where available plus standard A-share code ranges, validated by available daily K-line data.

Basic filters:

- Exclude ST and `*ST` names.
- Require at least 40 daily bars in the fetch window.
- Require T-day amount >= RMB 150 million.
- Require T-day close > RMB 2.
- Exclude T-day limit-up or near formal limit-up by board limit rules.
- Exclude T-day daily drop <= -8%.

Current limitations:

- Suspension handling is not strict enough.
- Limit-up buyability and limit-down sellability are not fully modeled.
- Slippage and order queue effects are not modeled.
- Sector/theme and event/news validation are not yet included.

## Baseline Signal

The main model is a rule-based ranking score. It favors short-term strength and liquidity expansion.

Positive inputs:

- T-day percentage gain.
- 3-day momentum.
- 5-day momentum.
- T-day amount expansion versus previous 5-day average amount.
- Close position inside the T-day high-low range.
- MA5 versus MA10 trend.
- T-day close versus open intraday strength.
- Turnover, capped to avoid unlimited reward for extreme turnover.

Penalties:

- T-day gain above 7.5% is penalized.
- Volume ratio above 4.5 is penalized.
- Formal limit-up candidates are excluded.

## Focused Exhaustion Filter

A focused filter was added after the 688981 中芯国际 failure on 2026-05-25.

Reason:

The old baseline treated a near-20cm surge as bullish continuation. For a T+1 14:30 entry strategy, this can be wrong because by the next afternoon the trade may already be in profit-taking mode.

The filter applies to 20cm names:

- `300`
- `301`
- `688`
- `689`

Exclude the signal when all of the following are true:

- T-day pct >= 17.5%.
- 3-day return >= 14%.
- 5-day return >= 24%.
- T-day close/open intraday strength >= 9%.
- T-day close is in the top 15% of the daily high-low range.

This filter specifically excludes climax-chasing setups such as 688981 on 2026-05-25.

## Current Backtest Result

Latest comparable run:

- Path: `projects/proj3/runs/backtest-2026-04-25-to-2026-05-25-1430-v3-focused-exhaustion-filter/`
- Window requested: 2026-04-25 to 2026-05-25.
- Effective trading window: 20260425 to 20260525.
- Trades: 17.
- Total net return: 1.33%.
- Hit rate: 58.82%.
- T+1 post-entry high >= 5% hit rate: 0.00%.
- Average win: 0.75%.
- Average loss: -0.87%.
- Profit factor: 1.23.
- Max drawdown: -3.43%.

Interpretation:

The current model is not close to the target monthly return greater than 15%. It is a baseline signal that can identify some afternoon continuation, but it has not shown the ability to consistently capture post-14:30 gains above 5%.

## Known Failure: 688981

Failure case:

- T date: 2026-05-25.
- T+1 date: 2026-05-26.
- Stock: 688981 中芯国际.
- T-day pct: +18.78%.
- 3-day return: +16.58%.
- 5-day return: +32.63%.
- Close position in daily range: 92.59%.
- Close/open intraday strength: +14.71%.
- T+1 daily return: -4.37%.

Diagnosis:

The model confused climax momentum with tradable continuation. The new focused exhaustion filter is designed to prevent this specific failure mode.

Detailed postmortem:

- `projects/proj3/runs/failure-688981-2026-05-25.md`

## Next Required Improvements

To move beyond a baseline, the strategy needs:

- Exact 1-minute or tick-level 14:30 execution modeling.
- 14:30 to close VWAP/slippage assumptions.
- Strict limit-up buyability and limit-down sellability modeling.
- Suspension and special trading-state handling.
- Market-wide crash-warning gate.
- Sector/theme heat and rotation features.
- Missed-winner review, not only failed-pick review.
- Longer out-of-sample testing across multiple market regimes.
- Comparison against random, liquidity-only, and sector-only baselines.

