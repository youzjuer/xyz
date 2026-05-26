import csv
import json
import math
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


START = "20260425"
END = "20260525"
FETCH_START = "20260301"
COST_BPS = 8
MAX_WORKERS = 12
BATCH_SIZE = 40
OUT_DIR = Path(__file__).resolve().parent
FALLBACK_DAILY_CACHE_DIR = OUT_DIR.parent / "backtest-2026-04-25-to-2026-05-22" / "cache"
DAILY_CACHE_DIR = FALLBACK_DAILY_CACHE_DIR if FALLBACK_DAILY_CACHE_DIR.exists() else OUT_DIR / "cache"
INTRADAY_CACHE_DIR = OUT_DIR / "intraday_cache"


def urlopen_json(url, timeout=15):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://quote.eastmoney.com/",
        },
    )
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8", "ignore"))
        except Exception as exc:
            last_error = exc
            time.sleep(0.4 * (attempt + 1))
    raise last_error


def secid_for(code):
    if code.startswith(("600", "601", "603", "605", "688", "689")):
        return "1." + code
    return "0." + code


def market_for(code):
    return "SH" if secid_for(code).startswith("1.") else "SZ"


def urlopen_text(url, timeout=20, referer="https://www.sse.com.cn/"):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": referer,
        },
    )
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", "ignore")
        except Exception as exc:
            last_error = exc
            time.sleep(0.5 * (attempt + 1))
    raise last_error


def fetch_sse_codes():
    codes = {}
    page = 1
    while True:
        params = {
            "jsonCallBack": "myJsonCallback",
            "STOCK_TYPE": "1",
            "REG_PROVINCE": "",
            "CSRC_CODE": "",
            "STOCK_CODE": "",
            "sqlId": "COMMON_SSE_CP_GPJCTPZ_GPLB_GP_L",
            "type": "inParams",
            "isPagination": "true",
            "pageHelp.cacheSize": "1",
            "pageHelp.beginPage": str(page),
            "pageHelp.pageSize": "200",
            "pageHelp.pageNo": str(page),
            "pageHelp.endPage": str(page),
            "_": "1770000000000",
        }
        url = "https://query.sse.com.cn/sseQuery/commonQuery.do?" + urllib.parse.urlencode(params)
        text = urlopen_text(url, referer="https://www.sse.com.cn/")
        match = re.search(r"myJsonCallback\((.*)\)$", text)
        if not match:
            break
        data = json.loads(match.group(1))
        page_help = data.get("pageHelp", {})
        rows = page_help.get("data") or []
        for row in rows:
            code = row.get("A_STOCK_CODE")
            name = row.get("SEC_NAME_CN") or row.get("COMPANY_ABBR") or ""
            if code and row.get("DELIST_DATE") == "-" and row.get("STATE_CODE") == "2":
                codes[code] = name
        if page >= int(page_help.get("pageCount") or page):
            break
        page += 1
    return codes


def fetch_szse_codes():
    codes = {}
    page = 1
    while True:
        params = {
            "SHOWTYPE": "JSON",
            "CATALOGID": "1110",
            "TABKEY": "tab1",
            "PAGENO": str(page),
            "random": str(time.time()),
        }
        url = "https://www.szse.cn/api/report/ShowReport/data?" + urllib.parse.urlencode(params)
        data = json.loads(urlopen_text(url, referer="https://www.szse.cn/"))
        if not data:
            break
        block = data[0]
        meta = block.get("metadata", {})
        rows = block.get("data") or []
        for row in rows:
            code = row.get("agdm") or row.get("zqdm") or row.get("A股代码")
            name = row.get("agjc") or row.get("zqjc") or row.get("A股简称") or ""
            if code and len(code) == 6 and code[0] in "023":
                codes[code] = re.sub(r"<[^>]+>", "", name)
        if page >= int(meta.get("pagecount") or page):
            break
        time.sleep(0.08)
        page += 1
    return codes


def code_candidates():
    codes = {}
    try:
        codes.update(fetch_sse_codes())
    except Exception as exc:
        print(f"warn=sse_list_failed error={exc}", flush=True)
    try:
        codes.update(fetch_szse_codes())
    except Exception as exc:
        print(f"warn=szse_list_failed error={exc}", flush=True)
        for prefix in ("000", "001", "002", "003", "300", "301"):
            for i in range(1000):
                code = f"{prefix}{i:03d}"
                codes.setdefault(code, code)
    for prefix in ("688", "689"):
        for i in range(1000):
            code = f"{prefix}{i:03d}"
            codes.setdefault(code, code)
    return sorted(codes)


def payload_from_sohu_item(code, item):
    if item.get("status") != 0 or not item.get("hq"):
        return None
    klines = []
    for hq in reversed(item["hq"]):
        # date, open, close, change, pct, low, high, volume(lot), amount(10k RMB), turnover
        pct = hq[4].replace("%", "")
        turnover = hq[9].replace("%", "") if len(hq) > 9 else "0"
        klines.append(
            ",".join(
                [
                    hq[0],
                    hq[1],
                    hq[2],
                    hq[6],
                    hq[5],
                    hq[7],
                    str(float(hq[8]) * 10000),
                    "0",
                    pct,
                    hq[3],
                    turnover,
                ]
            )
        )
    return {
        "code": code,
        "name": code,
        "market": market_for(code),
        "klines": klines,
    }


def fetch_daily_batch(codes):
    uncached = []
    payloads = []
    for code in codes:
        cache_file = DAILY_CACHE_DIR / f"{code}.json"
        if cache_file.exists():
            try:
                payloads.append(json.loads(cache_file.read_text(encoding="utf-8")))
                continue
            except Exception:
                pass
        uncached.append(code)
    if not uncached:
        return payloads
    try:
        params = {
            "code": ",".join("cn_" + code for code in uncached),
            "start": FETCH_START,
            "end": END,
            "stat": "1",
            "order": "D",
            "period": "d",
            "callback": "historySearchHandler",
            "rt": "jsonp",
        }
        url = "https://q.stock.sohu.com/hisHq?" + urllib.parse.urlencode(params)
        text = urlopen_text(url, referer="https://q.stock.sohu.com/")
        match = re.search(r"historySearchHandler\((.*)\)$", text, re.S)
        if not match:
            return payloads
        data = json.loads(match.group(1))
        for item in data:
            raw_code = item.get("code", "")
            code = raw_code.split("_")[-1] if "_" in raw_code else raw_code
            result = payload_from_sohu_item(code, item)
            if result:
                (DAILY_CACHE_DIR / f"{code}.json").write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
                payloads.append(result)
        return payloads
    except Exception:
        return payloads


def sina_symbol(code):
    return ("sh" if market_for(code) == "SH" else "sz") + code


def fetch_intraday_30m(code):
    INTRADAY_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = INTRADAY_CACHE_DIR / f"{code}.json"
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    params = {
        "symbol": sina_symbol(code),
        "scale": "30",
        "ma": "5",
        "datalen": "1023",
    }
    url = (
        "https://quotes.sina.cn/cn/api/jsonp_v2.php/var=/"
        "CN_MarketDataService.getKLineData?"
        + urllib.parse.urlencode(params)
    )
    text = urlopen_text(url, referer="https://finance.sina.com.cn/")
    match = re.search(r"var=\((\[.*\])\);", text, re.S)
    if not match:
        return []
    rows = json.loads(match.group(1))
    cache_file.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
    return rows


def intraday_execution(code, t1_date):
    t1 = t1_date.replace("-", "")
    try:
        rows = fetch_intraday_30m(code)
    except Exception:
        return None
    day_rows = [r for r in rows if r.get("day", "").startswith(t1_date)]
    if not day_rows:
        return None
    by_time = {r.get("day", "")[-8:]: r for r in day_rows}
    entry_bar = by_time.get("14:30:00")
    exit_bar = by_time.get("15:00:00")
    if not entry_bar or not exit_bar:
        return None
    try:
        entry = float(entry_bar["close"])
        exit_px = float(exit_bar["close"])
        post_entry_high = max(float(r["high"]) for r in day_rows if r.get("day", "")[-8:] in ("14:30:00", "15:00:00"))
        entry_amount = float(entry_bar.get("amount") or 0)
    except (KeyError, ValueError):
        return None
    if entry <= 0 or exit_px <= 0:
        return None
    return {
        "entry_proxy": entry,
        "exit_close": exit_px,
        "t1_high": post_entry_high,
        "entry_bar_amount": entry_amount,
        "entry_time": f"{t1[:4]}-{t1[4:6]}-{t1[6:]} 14:30:00",
        "exit_time": f"{t1[:4]}-{t1[4:6]}-{t1[6:]} 15:00:00",
    }


def parse_rows(payload):
    rows = []
    for line in payload["klines"]:
        parts = line.split(",")
        if len(parts) < 11:
            continue
        try:
            rows.append(
                {
                    "date": parts[0],
                    "open": float(parts[1]),
                    "close": float(parts[2]),
                    "high": float(parts[3]),
                    "low": float(parts[4]),
                    "volume": float(parts[5]),
                    "amount": float(parts[6]),
                    "amplitude": float(parts[7]),
                    "pct": float(parts[8]),
                    "change": float(parts[9]),
                    "turnover": float(parts[10]),
                }
            )
        except ValueError:
            continue
    return rows


def ma(values):
    return sum(values) / len(values) if values else math.nan


def limit_rate(code):
    if code.startswith(("300", "301", "688", "689")):
        return 19.5
    return 9.5


def score_at(code, name, rows, idx):
    row = rows[idx]
    prev = rows[: idx + 1]
    if idx < 10:
        return None
    if name.upper().startswith(("ST", "*ST")) or "ST" in name.upper():
        return None
    if row["close"] <= 2 or row["amount"] < 150_000_000:
        return None
    if row["pct"] >= limit_rate(code):
        return None
    if row["pct"] <= -8:
        return None

    r1 = row["pct"]
    r3 = row["close"] / prev[-4]["close"] - 1 if idx >= 3 and prev[-4]["close"] else 0
    r5 = row["close"] / prev[-6]["close"] - 1 if idx >= 5 and prev[-6]["close"] else 0
    amt5 = ma([x["amount"] for x in prev[-6:-1]])
    vol_ratio = row["amount"] / amt5 if amt5 and not math.isnan(amt5) else 1
    turn = row["turnover"]
    range_pos = (row["close"] - row["low"]) / (row["high"] - row["low"]) if row["high"] > row["low"] else 0.5
    ma5 = ma([x["close"] for x in prev[-5:]])
    ma10 = ma([x["close"] for x in prev[-10:]])
    trend = (ma5 / ma10 - 1) if ma10 else 0
    intraday_strength = (row["close"] / row["open"] - 1) if row["open"] else 0

    # Baseline "current model": momentum + volume confirmation + close strength,
    # with penalties for one-day exhaustion and thin liquidity.
    score = 0.0
    score += 1.40 * r1
    score += 0.95 * r3 * 100
    score += 0.55 * r5 * 100
    score += 1.80 * min(max(vol_ratio - 1, -0.5), 3.0)
    score += 2.40 * (range_pos - 0.5)
    score += 90.0 * trend
    score += 70.0 * intraday_strength
    score += 0.12 * min(turn, 25)
    if r1 > 7.5:
        score -= (r1 - 7.5) * 1.2
    if vol_ratio > 4.5:
        score -= (vol_ratio - 4.5) * 0.8

    return {
        "code": code,
        "name": name,
        "market": market_for(code),
        "score": score,
        "t_pct": r1,
        "t_amount": row["amount"],
        "t_turnover": turn,
        "t_vol_ratio": vol_ratio,
        "t_close": row["close"],
    }


def build_universe(cached_only=False):
    DAILY_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    payloads = []
    if cached_only:
        for cache_file in sorted(DAILY_CACHE_DIR.glob("*.json")):
            try:
                payload = json.loads(cache_file.read_text(encoding="utf-8"))
                rows = parse_rows(payload)
                if len(rows) >= 40:
                    payload["rows"] = rows
                    payloads.append(payload)
            except Exception:
                continue
        return payloads

    codes = list(code_candidates())
    print(f"official_codes={len(codes)}", flush=True)
    started = time.time()
    batches = [codes[i : i + BATCH_SIZE] for i in range(0, len(codes), BATCH_SIZE)]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(fetch_daily_batch, batch): batch for batch in batches}
        for n, fut in enumerate(as_completed(futures), 1):
            batch_payloads = fut.result()
            for payload in batch_payloads:
                rows = parse_rows(payload)
                if len(rows) >= 40:
                    payload["rows"] = rows
                    payloads.append(payload)
            if n % 20 == 0:
                print(f"checked_batches={n}/{len(batches)} valid={len(payloads)} elapsed={time.time() - started:.1f}s", flush=True)
    return payloads


def backtest(payloads):
    by_date = {}
    for payload in payloads:
        rows = payload["rows"]
        for idx, row in enumerate(rows[:-1]):
            nxt = rows[idx + 1]
            if START <= row["date"].replace("-", "") and nxt["date"].replace("-", "") <= END:
                by_date.setdefault(row["date"], []).append((payload, idx))

    trades = []
    equity = 1.0
    no_intraday = 0
    for date in sorted(by_date):
        candidates = []
        for payload, idx in by_date[date]:
            rows = payload["rows"]
            nxt = rows[idx + 1]
            if nxt["date"] <= date:
                continue
            s = score_at(payload["code"], payload["name"], rows, idx)
            if s is None:
                continue
            s["t1_date"] = nxt["date"]
            candidates.append(s)
        if not candidates:
            continue
        candidates.sort(key=lambda x: x["score"], reverse=True)
        pick = None
        for candidate in candidates:
            execution = intraday_execution(candidate["code"], candidate["t1_date"])
            if execution is None:
                no_intraday += 1
                continue
            candidate.update(execution)
            candidate["gross_return"] = candidate["exit_close"] / candidate["entry_proxy"] - 1
            candidate["high_return"] = candidate["t1_high"] / candidate["entry_proxy"] - 1
            pick = candidate
            break
        if pick is None:
            continue
        pick["rank"] = 1
        pick["date"] = date
        pick["net_return"] = pick["gross_return"] - COST_BPS / 10000
        equity *= 1 + pick["net_return"]
        pick["equity"] = equity
        pick["n_candidates"] = len(candidates)
        pick["no_intraday_before_pick"] = no_intraday
        trades.append(pick)
    return trades


def max_drawdown(equities):
    peak = 1.0
    mdd = 0.0
    for e in equities:
        peak = max(peak, e)
        mdd = min(mdd, e / peak - 1)
    return mdd


def write_outputs(payloads, trades):
    fields = [
        "date",
        "t1_date",
        "code",
        "name",
        "market",
        "score",
        "t_pct",
        "t_amount",
        "t_turnover",
        "t_vol_ratio",
        "t_close",
        "entry_proxy",
        "entry_time",
        "exit_close",
        "exit_time",
        "t1_high",
        "entry_bar_amount",
        "gross_return",
        "high_return",
        "net_return",
        "equity",
        "n_candidates",
        "no_intraday_before_pick",
    ]
    with (OUT_DIR / "trades.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for t in trades:
            writer.writerow({k: t.get(k) for k in fields})

    returns = [t["net_return"] for t in trades]
    wins = [r for r in returns if r > 0]
    losses = [r for r in returns if r <= 0]
    hit_5 = [t for t in trades if t["high_return"] >= 0.05]
    total = trades[-1]["equity"] - 1 if trades else 0
    mdd = max_drawdown([t["equity"] for t in trades])
    avg_win = sum(wins) / len(wins) if wins else 0
    avg_loss = sum(losses) / len(losses) if losses else 0
    profit_factor = sum(wins) / abs(sum(losses)) if losses else math.inf

    lines = [
        "# Backtest Report",
        "",
        f"- Window requested: 2026-04-25 to 2026-05-25; effective trading window: {START} to {END}.",
        f"- Data source: Sohu historical daily K-line API for signals; Sina 30-minute K-line API for T+1 14:30 execution.",
        f"- Universe: exchange list where available plus standard A-share code ranges, validated by available K-line data; valid names: {len(payloads)}.",
        f"- Filters: ST-name filter, minimum 40 daily bars in fetch window, T-day amount >= RMB 150m, T-day non-limit-up, price > RMB 2.",
        f"- Execution approximation: T-day signal, T+1 14:30 30-minute bar close entry, T+1 15:00 30-minute bar close exit; cost: {COST_BPS} bps round trip.",
        f"- Important limitation: this uses 30-minute bars, not exact 14:30 tick/VWAP fills; limit-order queue, slippage, and suspension/limit buyability still require stricter modeling.",
        "",
        "## Summary",
        "",
        f"- Trades: {len(trades)}",
        f"- Total net return: {total:.2%}",
        f"- Hit rate: {(len(wins) / len(returns) if returns else 0):.2%}",
        f"- T+1 high >= 5% hit rate: {(len(hit_5) / len(trades) if trades else 0):.2%}",
        f"- Average win: {avg_win:.2%}",
        f"- Average loss: {avg_loss:.2%}",
        f"- Profit factor: {profit_factor:.2f}",
        f"- Max drawdown: {mdd:.2%}",
        "",
        "## Trades",
        "",
        "| T | T+1 | Pick | Score | 14:30 Entry | 15:00 Exit | Net Ret | Post-entry High Ret | Equity |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for t in trades:
        lines.append(
            f"| {t['date']} | {t['t1_date']} | {t['name']} {t['code']} | "
            f"{t['score']:.2f} | {t['entry_proxy']:.2f} | {t['exit_close']:.2f} | "
            f"{t['net_return']:.2%} | {t['high_return']:.2%} | {t['equity']:.4f} |"
        )
    (OUT_DIR / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    cached_only = "--cached-only" in sys.argv
    payloads = build_universe(cached_only=cached_only)
    trades = backtest(payloads)
    write_outputs(payloads, trades)
    print(f"valid_universe={len(payloads)} trades={len(trades)}")
    if trades:
        print(f"total_net_return={trades[-1]['equity'] - 1:.4%}")
        print(f"report={OUT_DIR / 'report.md'}")


if __name__ == "__main__":
    main()
