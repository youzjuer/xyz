# Project workspace

这个仓库采用 `project/task` 分层：

- `projects/`：每个独立目标一个项目目录，例如 `projects/proj1/`。
- `projects/<project>/tasks/`：项目内的可执行任务。
- `runs/<project>/<task>/`：任务运行产物。
- `logs/`：长期日志。

## 约定

- 新目标先建项目，再拆任务。
- 任务必须隶属于某个项目。
- 任务产物写进对应 `runs/<project>/<task>/`。
- 公共模板放仓库根部，项目专属内容放项目目录。

## 示例结构

```text
projects/
  proj1/
    PROJECT.md
    tasks/
      task-001.md
      task-002.md
    runs/
      task-001/
      task-002/
```

## 使用方式

1. 先在 `projects/proj1/PROJECT.md` 写清目标。
2. 再在 `projects/proj1/tasks/` 下拆任务。
3. 每个任务单独推进、单独产出、单独记录。
