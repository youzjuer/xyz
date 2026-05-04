# Task

## Task

- ID: `task-003`
- Project: `proj2`
- Title: 生成首次股票推荐或观察名单
- Status: pending
- Owner: Claude

## Goal

- 基于候选池生成第一版可复盘的股票推荐或观察名单。

## Inputs

- `runs/task-001/` 的推荐框架
- `runs/task-002/` 的候选股票池
- 最新可用市场信息

## Steps

1. 选择推荐标的或观察标的。
2. 写明推荐逻辑、风险和失效条件。
3. 标注适用周期和复盘时间。
4. 输出推荐/观察名单。

## Output

- 文件路径：`runs/task-003/`
- 结果说明：首次推荐清单、观察名单、风险提示、复盘计划

## Done when

- 用户可以直接阅读并决定是否继续深入研究某个标的。
