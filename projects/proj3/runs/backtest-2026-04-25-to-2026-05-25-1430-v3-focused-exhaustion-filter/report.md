# Backtest Report

- Window requested: 2026-04-25 to 2026-05-25; effective trading window: 20260425 to 20260525.
- Data source: Sohu historical daily K-line API for signals; Sina 30-minute K-line API for T+1 14:30 execution.
- Universe: exchange list where available plus standard A-share code ranges, validated by available K-line data; valid names: 2401.
- Filters: ST-name filter, minimum 40 daily bars in fetch window, T-day amount >= RMB 150m, T-day non-limit-up, price > RMB 2.
- Signal adjustment: focused exhaustion filter excludes 20cm names with near-limit T-day climax after large 3-day and 5-day runs.
- Execution approximation: T-day signal, T+1 14:30 30-minute bar close entry, T+1 15:00 30-minute bar close exit; cost: 8 bps round trip.
- Important limitation: this uses 30-minute bars, not exact 14:30 tick/VWAP fills; limit-order queue, slippage, and suspension/limit buyability still require stricter modeling.

## Summary

- Trades: 17
- Total net return: 1.33%
- Hit rate: 58.82%
- T+1 high >= 5% hit rate: 0.00%
- Average win: 0.75%
- Average loss: -0.87%
- Profit factor: 1.23
- Max drawdown: -3.43%

## Trades

| T | T+1 | Pick | Score | 14:30 Entry | 15:00 Exit | Net Ret | Post-entry High Ret | Equity |
|---|---|---|---:|---:|---:|---:|---:|---:|
| 2026-04-27 | 2026-04-28 | 688268 688268 | 101.85 | 211.96 | 208.27 | -1.82% | 0.52% | 0.9818 |
| 2026-04-28 | 2026-04-29 | 688268 688268 | 126.18 | 188.71 | 190.23 | 0.73% | 1.74% | 0.9889 |
| 2026-04-29 | 2026-04-30 | 603318 603318 | 93.39 | 14.39 | 14.26 | -0.98% | 1.39% | 0.9792 |
| 2026-04-30 | 2026-05-06 | 688515 688515 | 77.06 | 166.21 | 166.73 | 0.23% | 1.52% | 0.9815 |
| 2026-05-06 | 2026-05-07 | 688531 688531 | 106.21 | 128.71 | 128.00 | -0.63% | 0.97% | 0.9753 |
| 2026-05-07 | 2026-05-08 | 300571 300571 | 107.62 | 57.66 | 58.00 | 0.51% | 0.83% | 0.9802 |
| 2026-05-08 | 2026-05-11 | 300819 300819 | 90.45 | 84.97 | 85.74 | 0.83% | 2.39% | 0.9883 |
| 2026-05-11 | 2026-05-12 | 300819 300819 | 94.73 | 83.35 | 82.91 | -0.61% | 0.08% | 0.9823 |
| 2026-05-12 | 2026-05-13 | 300983 300983 | 85.18 | 48.43 | 48.27 | -0.41% | 0.25% | 0.9783 |
| 2026-05-13 | 2026-05-14 | 300449 300449 | 102.06 | 11.01 | 11.05 | 0.28% | 0.91% | 0.9811 |
| 2026-05-14 | 2026-05-15 | 300965 300965 | 119.73 | 79.19 | 78.01 | -1.57% | 2.10% | 0.9657 |
| 2026-05-15 | 2026-05-18 | 688146 688146 | 121.90 | 133.49 | 135.90 | 1.73% | 1.81% | 0.9823 |
| 2026-05-18 | 2026-05-19 | 300959 300959 | 128.77 | 175.09 | 176.38 | 0.66% | 0.82% | 0.9888 |
| 2026-05-19 | 2026-05-20 | 688507 688507 | 127.13 | 155.16 | 155.30 | 0.01% | 1.11% | 0.9889 |
| 2026-05-20 | 2026-05-21 | 688143 688143 | 116.64 | 130.66 | 132.00 | 0.95% | 3.23% | 0.9982 |
| 2026-05-21 | 2026-05-22 | 001259 001259 | 104.23 | 79.20 | 79.20 | -0.08% | 0.00% | 0.9974 |
| 2026-05-22 | 2026-05-25 | 688610 688610 | 86.78 | 198.95 | 202.28 | 1.59% | 1.67% | 1.0133 |
