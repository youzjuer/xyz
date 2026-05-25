# Proj3 Tasks

Task files for the A-share next-day surge quant system.

Suggested first tasks:

1. Define the exact trading protocol:
   - prediction timing on T;
   - fixed buy time: **14:30 on T+1**;
   - 14:30 execution price assumption;
   - T+1 sell rule;
   - max holdings per day;
   - position sizing;
   - liquidity and limit-up/limit-down handling;
   - macro/market warning gate behavior.
2. Define tradable universe and exclusion rules:
   - ST;
   - suspended stocks;
   - illiquid names;
   - STAR/ChiNext inclusion decision;
   - one-word limit-up boards and unbuyable opens.
3. Choose data source and schema:
   - OHLCV;
   - adjustment factors;
   - limit-up/limit-down prices;
   - suspension status;
   - sector/theme mapping;
   - intraday 14:30 price or minute-bar data;
   - macro/market warning indicators;
   - capital-flow/event proxies if available.
4. Build label set:
   - T+1 return >5%;
   - T+1 intraday high >5%;
   - buyable >5% winners;
   - false-positive failures;
   - missed winners.
5. Build backtest engine with A-share execution constraints, 14:30 entry, costs, and market-warning gate.
6. Build macro/market sharp-drop warning module:
   - index trend/drawdown;
   - market breadth;
   - limit-down count;
   - volatility/turnover expansion;
   - sector-wide selloff;
   - capital-flow shock proxies.
7. Implement baseline strategy:
   - simple rule-based theme/momentum/turnover model;
   - compare against random/liquidity/sector baselines.
8. Build daily failure post-mortem template.
9. Evaluate whether monthly return >15% is plausible after costs, slippage, warning-gate blocks, and drawdowns.
