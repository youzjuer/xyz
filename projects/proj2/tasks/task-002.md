# Task

## Task

- ID: `task-002`
- Project: `proj2`
- Title: 建立第一版候选股票池和筛选指标
- Status: pending
- Owner: Claude

## Goal

- 根据用户确认的市场和偏好，建立第一版候选股票池。

## Inputs

- `runs/task-001/` 的推荐框架
- 用户确认的市场范围、周期、风险偏好
- 行情、财报、新闻或其他数据来源

## Steps

1. 根据框架确定筛选条件。
2. 收集候选标的。
3. 按指标做初筛。
4. 输出候选池和排除理由。

## Output

- 文件路径：`runs/task-002/`
- 结果说明：候选股票池、筛选指标、初筛结果

## Done when

- 候选池能支持生成第一版推荐/观察名单。
