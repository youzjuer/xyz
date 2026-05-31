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
- Recommendation rule: use the mechanical top-ranked strategy output. Do not replace it with discretionary "less extreme" candidates unless that replacement rule has passed a backtest against the same benchmark.

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

## Major Decision Factors

The stock signal must not be evaluated in isolation. Before using the mechanical stock pick, the strategy should judge whether the market environment supports next-day continuation.

The major decision layer should answer:

- Is the market in an incremental-liquidity phase or only a stock-fund rotation phase?
- Is broad risk appetite improving or deteriorating?
- Are overseas markets supporting or suppressing A-share risk appetite?
- Is the selected sector receiving fresh capital, or is it only yesterday's crowded trade?
- Is the candidate still likely to have T+1 afternoon buying demand?

If the major decision layer is negative, the strategy should downgrade the signal to observation or skip the trade, even if the individual stock ranks first mechanically.

## Overseas Market Risk Gate

US market changes should be included as a pre-trade environment filter. They should not replace A-share stock selection, but they can affect whether a high-momentum A-share signal is tradable.

Main transmission channels:

- US risk appetite: Nasdaq and S&P 500 declines can pressure A-share growth and technology names.
- US Treasury yields: rising 10-year yields tend to pressure high-valuation growth stocks.
- US dollar and offshore RMB: USD strength and CNH weakness can reduce foreign-risk appetite toward China assets.
- US semiconductor and AI leaders: moves in Nvidia, the Philadelphia Semiconductor Index, and major AI names can affect A-share semiconductor, computing-power, electronics, and robotics themes.
- China ADRs and Hong Kong technology names: weakness there can spill into related A-share sentiment.

Daily overseas inputs to record before trading:

- Nasdaq Composite or Nasdaq 100 daily change.
- S&P 500 daily change.
- Philadelphia Semiconductor Index daily change.
- China ADR / Golden Dragon China Index daily change where available.
- US 10-year Treasury yield change.
- US Dollar Index or USD/CNH direction.
- Hang Seng Tech opening behavior.

Suggested gate:

- If US equities are sharply weaker, US yields are rising, and CNH is weakening, reduce position or skip high-valuation growth and technology momentum signals.
- If Nasdaq/semiconductors are strong and CNH is stable, technology-growth signals may be allowed, subject to A-share liquidity and sector confirmation.
- If overseas signals are mixed, default to A-share internal liquidity, breadth, and sector rotation conditions.

This gate is especially important for the current strategy because the v3 signal chases short-term strength. In a weak global-risk environment, T-day strength can become T+1 profit-taking rather than continuation.

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

## Rejected / Research-Only: Multi-Day Acceleration Filter

A second failure mode appeared after the 301071 力量钻石 pick for 2026-05-27.

301071 was not a near-20cm single-day climax, but it had already accelerated for several days:

- 2026-05-22: +8.83%.
- 2026-05-25: +14.86%.
- 2026-05-26: +7.43%.
- 3-day return at signal time: +34.28%.
- 5-day return at signal time: +38.14%.

On 2026-05-27 it opened weak and closed down -8.75%. This shows that the previous focused exhaustion filter was too narrow. It caught near-20cm climax bars, but missed multi-day acceleration exhaustion.

Hypothesis tested:

- Exclude candidates with 3-day return >= 30% and 5-day return >= 35%.
- Exclude candidates when the last 3 trading days are all positive and their total return >= 28%.
- If 3-day return >= 25%, require T+1 intraday confirmation before entry:
  - Skip if T+1 opens below previous close by more than 2.5%.
  - Skip if price does not reclaim previous close or VWAP before 10:30.

Backtest result:

- A broad v5 version using non-linear momentum sweet spots plus acceleration filters performed worse than the v3 benchmark.
- Window: 2026-04-25 to 2026-05-27.
- v3 extended benchmark: 19 trades, +2.74% total net return, max drawdown -3.32%.
- v5 confirmation strategy: 17 trades, -8.54% total net return, max drawdown -13.38%.
- v7 top-1 skip gate: 8 trades, -3.09% total net return.

Conclusion:

The multi-day acceleration idea explains the 301071 failure, but the tested broad filters are not accepted as the current strategy because they reduced overall performance. This remains a research hypothesis, not a production rule.

## Current Backtest Result

Latest comparable run:

- Path: `projects/proj3/runs/backtest-2026-04-25-to-2026-05-27-v3-extended/`
- Window requested: 2026-04-25 to 2026-05-27.
- Effective trading window: 20260425 to 20260527.
- Trades: 19.
- Total net return: 2.74%.
- Hit rate: 63.16%.
- T+1 post-entry high >= 5% hit rate: 0.00%.
- Average win: 0.81%.
- Average loss: -0.99%.
- Profit factor: 1.40.
- Max drawdown: -3.32%.

Interpretation:

The current model is not close to the target monthly return greater than 15%. It is a baseline signal that can identify some afternoon continuation, but it has not shown the ability to consistently capture post-14:30 gains above 5%. Attempts to add broad discretionary filters must be rejected unless they beat this benchmark.

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

## Known Failure: 301071

Failure case:

- Signal date: 2026-05-26.
- Target date: 2026-05-27.
- Stock: 301071 力量钻石.
- T-day pct: +7.43%.
- 3-day return: +34.28%.
- 5-day return: +38.14%.
- T+1 open: 76.29, about -4.82% versus prior close.
- T+1 close: 73.14.
- T+1 daily return: -8.75%.

Diagnosis:

301071 was not the mechanical v3 top-ranked pick for 2026-05-26. It was a discretionary override chosen because it looked less extreme than the raw top candidate. That override was not backtested and failed. The immediate process failure is that manual candidate substitution was allowed without validation.

The market-pattern diagnosis is still useful: 301071 was a multi-day acceleration candidate that opened weak the next day. But broad filters based on this observation failed in v5/v7 backtests, so they are not accepted as current strategy rules.

Detailed postmortem:

- `projects/proj3/history/2026-05-27-review-301071.md`

Accepted process change:

- No discretionary override of the mechanical top-ranked output.
- Any proposed replacement, filter, or intraday gate must be backtested against the current v3 benchmark before it can be used for recommendations.
- Failed hypotheses should be kept in history, not silently merged into the strategy.

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
