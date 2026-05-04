# Cron examples

这些示例使用自然语言描述，便于迁移到具体 Hermes cron 命令。执行前先确认本机 Hermes 的 cron 语法。

## 每日 AI 摘要

```text
Every day around 09:05, run skills/content-curator.md.
Topic: AI agent, Claude Code, Hermes, OpenClaw.
Time range: last 24 hours.
Write output to logs/daily-ai-brief-{{date}}.md.
If nothing important happened, reply [SILENT].
```

## 每周记忆维护

```text
Every Sunday around 20:10, run skills/memory-maintainer.md.
Review logs/ and runs/ from the last 7 days.
Propose memory updates before writing them.
If there are no useful long-term memories, reply [SILENT].
```

## 服务健康检查

```text
Every 30 minutes, check the configured service health endpoints.
If all checks pass, reply [SILENT].
If any check fails twice in a row, send a short alert to Home Channel with endpoint, error, and suggested next action.
Write logs to logs/health/{{date}}.md.
```

## 内容流水线

```text
Every weekday around 08:45, run:
1. skills/content-curator.md
2. skills/writing-cloner.md if voice profile is missing or stale
3. skills/publish-pipeline.md
Do not publish externally without human confirmation.
Write all artifacts to runs/{{date}}-content-pipeline/.
```

## 安静模式规则

- 正常、无变化、低价值结果：回复 `[SILENT]`。
- 需要用户决策、失败、异常、发现高价值信息：发送摘要。
- 摘要必须包含：发生了什么、为什么重要、建议动作。
