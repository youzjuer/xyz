# OpenClaw to Hermes migration checklist

## 迁移前

- 备份 OpenClaw 配置目录。
- 列出现有：人格文件、长期记忆、技能、模型配置、权限、常用命令。
- 标记不能自动迁移的内容：会话历史、Cron 任务、外部平台 token。

## 预览迁移

```bash
hermes claw migrate --dry-run
```

检查输出：

- 哪些文件会被复制
- 哪些文件会被覆盖
- 哪些配置无法识别
- 是否包含敏感信息

## 执行迁移

```bash
hermes claw migrate
```

迁移后检查：

- `SOUL.md` 是否仍然简洁、有观点、无客服腔。
- `MEMORY.md` 是否只保留长期有用内容。
- Skills 是否仍能独立运行。
- 模型配置是否符合当前预算和速度需求。

## 手动重建

这些通常需要手动处理：

- Cron 定时任务
- Gateway/Home Channel
- 当前会话历史
- 外部平台授权
- 本机路径差异

## 回滚策略

- 保留迁移前备份。
- 先在测试目录试跑。
- 不确认输出前，不覆盖正式配置。
