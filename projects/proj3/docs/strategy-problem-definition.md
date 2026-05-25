# Strategy Problem Definition

## Objective

Predict on day T which A-share stock(s) are most likely to rise more than 5% on T+1, buy at **14:30 on T+1**, sell on T+1, and iterate based on trade failures.

## Highest constraint

Monthly return must exceed 15%.

## Label candidates

- `next_day_close_return_gt_5`: T+1 close return > 5% versus 14:30 entry price.
- `next_day_high_return_gt_5`: T+1 post-entry intraday high return > 5% versus 14:30 entry price.
- `tradable_next_day_winner`: T+1 >5% winner that was realistically buyable at/around 14:30.
- `false_positive`: selected stock that failed to reach threshold or triggered stop/risk exit.
- `missed_winner`: stock that matched objective but was not selected.

## Execution constraints to model

- A-share T+1 mechanics.
- 14:30 entry price or executable 14:30 window.
- Limit-up buyability.
- Limit-down sellability.
- Suspension and special treatment stocks.
- Slippage and transaction costs.
- Liquidity and market impact.
- Opening gap risk.
- Broad-market sharp-drop risk and macro warning gate.

## Macro / market warning gate

Before allowing the 14:30 trade, the system must evaluate whether a broad-market sharp drop risk is present. If warning conditions trigger, it should issue an early warning and either block trades, reduce position size, or switch to defensive mode.

Candidate warning inputs:

- Major index trend and intraday drawdown.
- Market breadth: rising/falling ratio, limit-down count, high-decline count.
- Volatility expansion and abnormal turnover.
- Sector-wide synchronized selloff.
- Northbound/large-fund flow if reliable.
- Policy, geopolitical, overseas market, commodity, or FX shock proxies.

## Evaluation metrics

- Monthly return.
- Hit rate.
- Average win / average loss.
- Profit factor.
- Max drawdown.
- Daily return distribution.
- Turnover.
- Number of trades.
- Capacity and liquidity limits.
- Out-of-sample performance.
- Failure category distribution.
