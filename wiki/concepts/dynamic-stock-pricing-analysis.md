---
id: 20260514-dynamic-stock-pricing-analysis
title: Dynamic Stock Pricing Analysis
type: concept
category: investing-framework
status: active
created: 2026-05-14
updated: 2026-05-14
tags:
  - domain/investing
  - framework/stock-analysis
  - framework/valuation
  - framework/market-expectations
  - market/a-share
aliases:
  - 动态个股定价分析
  - 深度个股分析方法
  - 市场预期定价框架
source: self
sources:
  - stocks/byd/valuation-buy-zones
provenance:
  - user-correction: 对比亚迪的分析太保守了，当下比亚迪可能到80块么？我需要的是深刻有洞察里的分析，而不是流于表面的我都能看出来的分析
  - date: 2026-05-14
  - agent-assisted: Claude
confidence:
  base: high
  notes: Methodology reflects explicit user feedback and should guide future stock analysis outputs.
lifecycle:
  stage: active
  review: monthly
summary: Framework for replacing static conservative PE buy zones with probability-weighted, expectation-aware stock analysis.
links:
  concepts:
    - concepts/stock-recommendation-framework
    - concepts/a-share-sentiment-market
  stocks:
    - stocks/byd/index
    - stocks/byd/valuation-buy-zones
  projects:
    - projects/proj2-stock-recommendation
---

# Dynamic Stock Pricing Analysis

## Summary

When analyzing individual stocks, do not stop at static PE tables or overly conservative buy zones. The analysis must answer the real investment question:

```text
What is the market already pricing, what scenario would actually move the stock, and how likely is the attractive buy price to appear?
```

A good stock analysis should combine fundamentals, valuation, market expectations, industry structure, capital preference, probability-weighted scenarios, and practical execution.

## Why this exists

The BYD analysis initially gave a mechanically conservative A-share buy zone around RMB 75-80. The user correctly challenged this: for a global EV leader with export optionality and strong market attention, asking only “what price gives enough margin of safety” misses the more important question: **is that price realistic under the current market narrative?**

## Core principles

### 1. Static valuation is only the floor, not the answer

PE, PB, EV/EBITDA, and historical percentile are useful, but they do not determine the trading path alone. For stocks with strong narrative, leadership, scarcity, policy exposure, or global optionality, static valuation can be too conservative.

Always separate:

- **fair value from a spreadsheet**;
- **realistic market trading range**;
- **panic price that requires negative scenario stacking**;
- **execution price that an investor can actually expect to get.**

### 2. Analyze what the market already knows

A price target or buy zone is weak if it treats known bad news as if the market has not priced it.

Ask:

- Is the negative factor already public?
- Has the stock already de-rated for it?
- What incremental evidence would force another de-rating?
- What evidence would make the market look through it?

For BYD, Q1 profit weakness and sales slowdown were already partly visible. A fall from about RMB 98 to RMB 80 would require more than known weakness; it would require additional negative confirmation.

### 3. Use scenario probability, not just scenario price

Every buy-zone note should distinguish:

| Scenario type | Meaning |
|---|---|
| Base case | Most likely path under current evidence |
| Bull case | What creates upside or lets the stock trade at a higher acceptable buy price |
| Bear case | What makes the original lower buy zone realistic |
| Stress case | What creates true panic price or deep-value opportunity |

The analysis should state whether an attractive price is **realistic**, **low-probability**, or **only available in a stress case**.

### 4. Identify the real market disagreement

Do not only ask “is the company good?” Good companies can be bad buys and bad companies can rally.

Find the central disagreement:

- Is this company a long-duration growth platform or a cyclical value trap?
- Is the current problem temporary margin pressure or structural deterioration?
- Is the policy risk priced or still underestimated?
- Is the market buying earnings, market share, optionality, dividend, or theme beta?

For BYD, the real disagreement is not whether BYD is strong. It is whether BYD is still a global EV platform with export optionality, or becoming a low-margin scale automaker trapped in domestic price war.

### 5. Tie buy zones to catalysts and data triggers

A useful buy-zone framework needs two prices:

1. **Reality-adjusted first buy zone**: where the investor should start if they want exposure and the base case remains intact.
2. **Deep safety zone**: where the stock becomes highly attractive, but may require a negative shock and may not appear.

For each zone, define what data justifies buying:

- earnings acceleration or deterioration;
- monthly sales or order data;
- margin inflection;
- policy/risk clarification;
- capital-flow or sector sentiment;
- major support/resistance or volume confirmation.

### 6. Avoid false precision

Do not present one low price as “the buy point” unless the path to that price is plausible. A better answer is often a staged execution plan:

```text
first buy zone -> add zone -> stress opportunity zone
```

Then explain how much probability and what evidence attach to each zone.

### 7. For leaders, optionality matters

Market leaders often trade above what static valuation suggests because they carry option value:

- global expansion;
- product-cycle recovery;
- technology platform potential;
- policy support;
- index/ETF allocation;
- brand scarcity;
- institutional “must-own” status.

A deep buy zone for such stocks may be theoretically attractive but practically rare.

## Required output structure for future stock analysis

When the user asks for a serious individual stock view, include these sections:

1. **One-line conclusion**: buy / wait / hold / reduce, with reason.
2. **What the market is pricing**: current consensus and embedded assumptions.
3. **Real disagreement**: what bulls and bears actually disagree on.
4. **Base / bull / bear / stress scenarios**: include rough probability or at least likelihood ranking.
5. **Reality-adjusted buy zones**: first buy, add, deep opportunity; say which are realistic versus low-probability.
6. **Data triggers**: what raises or lowers buy zones.
7. **Execution plan**: staged position sizing, not just a price table.
8. **What would prove the thesis wrong**.

## BYD correction example

Initial static view:

- A-share below RMB 80 starts to be attractive.
- RMB 70 is comfortable.

Corrected dynamic view:

- RMB 80 is attractive but may not be realistic as a base-case buy point.
- RMB 88-92 is a more practical first buy zone if the investor wants exposure.
- RMB 82-86 is a strong buy zone that likely needs additional negative pressure.
- RMB 80 or below is a stress/opportunity zone, not the baseline expectation.

Reasoning:

- Known Q1 weakness was already partly priced.
- BYD still has leader premium and export optionality.
- A drop to RMB 80 requires negative scenario stacking: weak Q2 profit, weak monthly sales, ongoing price war, sector de-rating, or export shock.

## Anti-patterns

Avoid:

- giving only PE tables;
- saying “估值不便宜，等更低” without discussing probability;
- ignoring what the market already knows;
- treating all stocks like static value stocks;
- missing narrative/optionality for leaders;
- using a low price that is attractive but unlikely as the only actionable answer;
- giving facts the user can see without adding insight.

## Related

- [[concepts/stock-recommendation-framework]]
- [[stocks/byd/valuation-buy-zones]]
- [[projects/proj2-stock-recommendation]]
