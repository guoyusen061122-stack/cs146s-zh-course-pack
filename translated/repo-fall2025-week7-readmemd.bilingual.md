# Week 7

# 第 7 周

Slightly enhanced full‑stack starter (copied from Week 5) with a few backend improvements.

略微增强的全栈起手项目（复制自第 5 周），并做了若干后端改进。

- FastAPI backend with SQLite (SQLAlchemy)
- Static frontend (no Node toolchain needed)
- Minimal tests (pytest)
- Pre-commit (black + ruff)
- Enhancements over Week 5:
- Timestamps on models (`created_at`, `updated_at`)
- Pagination and sorting for list endpoints
- Optional filters (e.g., filter action items by completion)
- PATCH endpoints for partial updates

- FastAPI 后端搭配 SQLite（SQLAlchemy）
- 静态前端（无需 Node 工具链）
- 最小化测试（pytest）
- 提交前钩子（black + ruff）
- 相对第 5 周的增强：
- 模型上的时间戳（`created_at`、`updated_at`）
- 列表端点的分页与排序
- 可选过滤器（例如按完成状态筛选行动项）
- 用于部分更新的 PATCH 端点

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

1. Run the app (from `week6/`)

1. 运行应用（在 `week6/` 目录下）

```bash
cd week7 && make run
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
cd week7 && make test
```

## Formatting/Linting

## 格式化/静态检查

```bash
cd week7 && make format
cd week7 && make lint
```

## Configuration

## 配置

Copy `.env.example` to `.env` (in `week7/`) to override defaults like the database path.

把 `.env.example` 复制为 `.env`（位于 `week7/`），即可覆盖数据库路径等默认值。
