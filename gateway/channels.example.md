# Gateway channels example

用于规划 Hermes 的移动端和通知渠道。不要把真实 token 写进本文件。

## Home Channel

Home Channel 是主动通知的默认目的地：Cron 结果、告警、日报、长期任务状态都发到这里。

```yaml
home_channel:
  platform: telegram
  target: "<chat-id-or-channel-name>"
  silent_keyword: "[SILENT]"
```

## 渠道模板

```yaml
channels:
  telegram:
    enabled: false
    token_env: HERMES_TELEGRAM_BOT_TOKEN
    default_target: "<chat-id>"

  slack:
    enabled: false
    token_env: HERMES_SLACK_BOT_TOKEN
    default_target: "#agent-home"

  discord:
    enabled: false
    token_env: HERMES_DISCORD_BOT_TOKEN
    default_target: "<channel-id>"
```

## 通知规则

- 告警类：失败、异常、需要人工决策。
- 摘要类：日报、周报、研究结果。
- 静默类：健康检查通过、无新内容、低价值重复结果。

## 安全规则

- token 只放环境变量或密钥管理器。
- 不在公共频道发送密钥、日志原文、客户数据。
- 对外发布内容必须人工确认。
- 先把通知发到测试频道，稳定后再接正式频道。
