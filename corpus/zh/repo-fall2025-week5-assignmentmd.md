# 第 5 周 — 使用 Warp 进行智能体化开发

把 `week5/` 中的应用当作你的练习场。本周与上一次作业相似，但更强调 Warp 智能体化开发环境与多智能体工作流。

## 了解 Warp
- Warp 智能体化开发环境：[warp.dev](https://www.warp.dev/)
- [Warp University](https://www.warp.dev/university?slug=university)


## 探索起始应用
极简的全栈起始应用。
- 带 SQLite（SQLAlchemy）的 FastAPI 后端
- 静态前端（无需 Node 工具链）
- 极简测试（pytest）
- pre-commit（black + ruff）
- 用于练习智能体驱动工作流的任务

把这个应用当作你的练习场，试验你构建的 Warp 自动化。

### 结构

```
backend/                # FastAPI app
frontend/               # Static UI served by FastAPI
data/                   # SQLite DB + seed
docs/                   # TASKS for agent-driven workflows
```

### 快速上手

1) 激活你的 conda 环境。

```bash
conda activate cs146s
```

2) （可选）安装 pre-commit 钩子

```bash
pre-commit install
```

3) 运行应用（在 `week5/` 目录下）

```bash
make run
```

4) 打开 `http://localhost:8000` 查看前端，打开 `http://localhost:8000/docs` 查看 API 文档。

5) 试用一下这个起始应用，感受它当前的功能与特性。


### 测试
运行测试（在 `week5/` 目录下）
```bash
make test
```

### 格式化/静态检查
```bash
make format
make lint
```

## 第一部分：构建你的自动化（选择 2 个或更多） 
从 `week5/docs/TASKS.md` 中选择要实现的任务。你的实现必须以下面两种方式利用 Warp（详见下文）：

- A) 使用 Warp Drive 功能——例如保存的提示词、规则或 MCP 服务器。
- (B) 在 Warp 中引入多智能体工作流。

让你的改动集中在 `week5/` 内的后端、前端、逻辑或测试上。
对每个选定的任务，注明其难度等级。


### A) Warp Drive 保存的提示词、规则、MCP 服务器（必需：至少一项）
创建一个或多个可共享的 Warp Drive 提示词、规则或 MCP 服务器集成，并针对本仓库定制。示例：
- 测试运行器：带覆盖率统计，并支持不稳定测试重跑
- 文档同步：从 `/openapi.json` 生成/更新 `docs/API.md`，列出路由变更
- 重构脚手架：重命名模块、更新导入、运行静态检查/测试
- 发布助手：递增版本号、运行检查、准备变更日志片段
- 集成 Git MCP 服务器，让 Warp 自主与 Git 交互（创建分支、提交、PR 说明等）

>*提示：让工作流保持聚焦、传递参数、使其幂等，并尽量采用无人值守/非交互式的步骤。*

### B) Warp 中的多智能体工作流（必需：至少一项）
运行一次多智能体会话，让不同 Warp 标签页中的多个独立智能体并发处理互不相关的任务。 
- 在多个 Warp 标签页中用并发的智能体完成 `TASKS.md` 中多个自成一体的任务。挑战：你能让多少个智能体同时工作？

>*提示：[git worktree](https://git-scm.com/docs/git-worktree) 在这里可能有用，可以避免智能体之间互相覆盖。*


## 第二部分：让你的自动化投入工作 
既然你已经构建了 2 个以上的自动化，那就把它们用起来！在 `writeup.md` 的 *"How you used the automation (what pain point it resolves or accelerates)"* 一节中，描述你如何利用每一项自动化来改进某个工作流。

## 约束与范围
严格在 `week5/` 中工作（后端、前端、逻辑、测试）。除非自动化明确要求且你记录了原因，否则避免改动其他周的内容。


## 交付物
1) 两个或更多 Warp 自动化，其中可包括：
 - Warp Drive 工作流/规则（分享链接和/或导出的定义）以及任何辅助脚本
 - 用于协调多个智能体的任何补充提示词/操作手册

2) 一份放在 `week5/` 下的书面报告 `writeup.md`，其中包含：
 - 每项自动化的设计，包括目标、输入/输出、步骤
 - 前后对比（即人工工作流 vs. 自动化工作流）
 - 每个已完成任务所使用的自主性级别（使用了哪些代码权限、为什么，以及你如何监督）
 - （如适用）多智能体说明：角色、协调策略，以及并发的收益/风险/失败
 - 你如何使用该自动化（它解决了或加速了哪个痛点）



## 提交说明
1. 确保所有改动都已推送到用于评分的远程仓库。
2. **确保你已将 brentju 和 febielin 都添加为作业仓库的协作者。**
2. 通过 Gradescope 提交。 

