# Backtest Report

- Window requested: 2026-04-25 to 2026-05-25; effective trading window: 20260425 to 20260525.
- Data source: Sohu historical daily K-line API, fetched at runtime.
- Universe: exchange list where available plus standard A-share code ranges, validated by available K-line data; valid names: 2401.
- Filters: ST-name filter, minimum 40 daily bars in fetch window, T-day amount >= RMB 150m, T-day non-limit-up, price > RMB 2.
- Execution approximation: T-day signal, T+1 open entry proxy, T+1 close exit; cost: 8 bps round trip.
- Important limitation: no 14:30 minute bars in this run, so this is a daily-bar approximation, not the final production backtest.

## Summary

- Trades: 17
- Total net return: -10.87%
- Hit rate: 41.18%
- T+1 high >= 5% hit rate: 29.41%
- Average win: 4.03%
- Average loss: -3.77%
- Profit factor: 0.75
- Max drawdown: -19.96%

## Trades

| T | T+1 | Pick | Score | Net Ret | T+1 High Ret | Equity |
|---|---|---|---:|---:|---:|---:|
| 2026-04-27 | 2026-04-28 | 688268 688268 | 101.85 | 10.12% | 12.74% | 1.1012 |
| 2026-04-28 | 2026-04-29 | 688268 688268 | 126.18 | -3.52% | 0.00% | 1.0624 |
| 2026-04-29 | 2026-04-30 | 603318 603318 | 93.39 | -2.94% | 2.86% | 1.0312 |
| 2026-04-30 | 2026-05-06 | 688515 688515 | 77.06 | -3.62% | 0.90% | 0.9939 |
| 2026-05-06 | 2026-05-07 | 688531 688531 | 106.21 | 3.99% | 8.40% | 1.0335 |
| 2026-05-07 | 2026-05-08 | 300571 300571 | 107.62 | 1.94% | 3.76% | 1.0535 |
| 2026-05-08 | 2026-05-11 | 300819 300819 | 90.45 | 4.07% | 8.11% | 1.0965 |
| 2026-05-11 | 2026-05-12 | 300819 300819 | 94.73 | -1.49% | 1.06% | 1.0801 |
| 2026-05-12 | 2026-05-13 | 300983 300983 | 85.18 | 0.48% | 4.08% | 1.0853 |
| 2026-05-13 | 2026-05-14 | 300449 300449 | 102.06 | -6.59% | 1.95% | 1.0137 |
| 2026-05-14 | 2026-05-15 | 300965 300965 | 119.73 | -9.36% | 2.22% | 0.9188 |
| 2026-05-15 | 2026-05-18 | 688146 688146 | 121.90 | -3.94% | 4.44% | 0.8826 |
| 2026-05-18 | 2026-05-19 | 300959 300959 | 128.77 | -0.14% | 1.43% | 0.8814 |
| 2026-05-19 | 2026-05-20 | 688507 688507 | 127.13 | 7.02% | 9.66% | 0.9433 |
| 2026-05-20 | 2026-05-21 | 688143 688143 | 116.64 | -6.01% | 0.58% | 0.8866 |
| 2026-05-21 | 2026-05-22 | 001259 001259 | 104.23 | -0.08% | 13.64% | 0.8859 |
| 2026-05-22 | 2026-05-25 | 688610 688610 | 86.78 | 0.61% | 0.69% | 0.8913 |
