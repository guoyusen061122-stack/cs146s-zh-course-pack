# 第 5 周

用于试验自主编码智能体的最小全栈起手项目。

- FastAPI 后端搭配 SQLite（SQLAlchemy）
- 静态前端（无需 Node 工具链）
- 最小化测试（pytest）
- 提交前钩子（black + ruff）
- 用于练习智能体驱动工作流的任务

## 快速开始

1) 创建并激活虚拟环境，然后安装依赖

```bash
cd /Users/mihaileric/Documents/code/modern-software-dev-assignments
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
```

2) （可选）安装提交前钩子

```bash
pre-commit install
```

3) 运行应用（在 `week5/` 目录下）

```bash
cd week5 && make run
```

前端请打开 `http://localhost:8000`，API 文档请打开 `http://localhost:8000/docs`。

## 结构

```
backend/                # FastAPI app
frontend/               # Static UI served by FastAPI
data/                   # SQLite DB + seed
docs/                   # TASKS for agent-driven workflows
```

## 测试

```bash
cd week5 && make test
```

## 格式化/静态检查

```bash
cd week5 && make format
cd week5 && make lint
```

## 配置

把 `.env.example` 复制为 `.env`（位于 `week5/`），即可覆盖数据库路径等默认值。
