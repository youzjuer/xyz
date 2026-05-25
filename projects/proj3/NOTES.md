# Proj3 Notes

## 2026-05-24

Initialized quant trading system project workspace.

Updated project objective: this is specifically an **A-share next-day surge prediction system**. The system predicts on T which stocks are most likely to rise more than 5% on T+1, buys on T+1, exits on T+1, and learns from failed trades through post-mortems.

Highest constraint: **monthly return > 15%**.

Updated trading protocol: buy time is **14:30 on T+1**. The system also needs a macro/market crash-warning module; when a broad-market sharp drop risk is detected, the system should warn early and block or reduce trades.

Important principle: the target is aggressive, so the system must distinguish real tradable edge from backtest artifacts such as unbuyable limit-up opens, illiquid names, unrealistic fills, and overfitted event patterns.
