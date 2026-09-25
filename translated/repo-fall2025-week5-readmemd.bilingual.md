# Week 5

# 第 5 周

Minimal full‑stack starter for experimenting with autonomous coding agents.

用于试验自主编码智能体的最小全栈起手项目。

- FastAPI backend with SQLite (SQLAlchemy)
- Static frontend (no Node toolchain needed)
- Minimal tests (pytest)
- Pre-commit (black + ruff)
- Tasks to practice agent-driven workflows

- FastAPI 后端搭配 SQLite（SQLAlchemy）
- 静态前端（无需 Node 工具链）
- 最小化测试（pytest）
- 提交前钩子（black + ruff）
- 用于练习智能体驱动工作流的任务

## Quickstart

## 快速开始

1. Create and activate a virtualenv, then install dependencies

1. 创建并激活虚拟环境，然后安装依赖

```bash
cd /Users/mihaileric/Documents/code/modern-software-dev-assignments
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
```

1. (Optional) Install pre-commit hooks

1. （可选）安装提交前钩子

```bash
pre-commit install
```

1. Run the app (from `week5/`)

1. 运行应用（在 `week5/` 目录下）

```bash
cd week5 && make run
```

Open `http://localhost:8000` for the frontend and `http://localhost:8000/docs` for the API docs.

前端请打开 `http://localhost:8000`，API 文档请打开 `http://localhost:8000/docs`。

## Structure

## 结构

```
backend/                # FastAPI app
frontend/               # Static UI served by FastAPI
data/                   # SQLite DB + seed
docs/                   # TASKS for agent-driven workflows
```

## Tests

## 测试

```bash
cd week5 && make test
```

## Formatting/Linting

## 格式化/静态检查

```bash
cd week5 && make format
cd week5 && make lint
```

## Configuration

## 配置

Copy `.env.example` to `.env` (in `week5/`) to override defaults like the database path.

把 `.env.example` 复制为 `.env`（位于 `week5/`），即可覆盖数据库路径等默认值。
