# 仓库任务 

## 1) 将前端迁移到 Vite + React（复杂）
- 在 `week5/frontend/`（或 `week5/frontend/ui/` 这样的子文件夹）中搭建一个 Vite + React 应用。
- 用由 FastAPI 提供的构建产物替换当前的静态资源：
 - 构建输出到 `week5/frontend/dist/`。
 - 更新 FastAPI 的静态挂载，让它提供 `dist`，并把根路径（`/`）指向 `dist` 中的 `index.html`。
- 在 React 中接入现有端点：
 - 笔记的列表、创建、删除、编辑。
 - 行动项的列表、创建、完成。
- 在 `Makefile` 中添加目标：`web-install`、`web-dev`、`web-build`，并确保 `make run` 能自动构建 Web 产物（或记录该工作流）。
- 至少为两个组件添加组件/单元测试（React Testing Library），并在 `backend/tests` 中为 API 兼容性添加集成测试。

## 2) 带分页与排序的笔记检索（中等）
- 实现 `GET /notes/search?q=...&page=1&page_size=10&sort=created_desc|title_asc`。
- 对标题/内容使用大小写不敏感的匹配。
- 返回包含 `items`、`total`、`page`、`page_size` 的负载。
- 为过滤、排序和分页添加 SQLAlchemy 查询组合。
- 更新 React UI，加上检索输入框、结果计数以及上一页/下一页分页控件。
- 在 `backend/tests/test_notes.py` 中为查询边界情况和分页添加测试。

## 3) 带乐观 UI 更新的完整笔记 CRUD（中等）
- 添加 `PUT /notes/{id}` 和 `DELETE /notes/{id}`。
- 在前端乐观地更新状态，同时处理出错时的回滚。
- 在 `schemas.py` 中校验负载（最小长度，以及在合理处限制最大长度）。
- 为成功与校验错误添加测试。

## 4) 行动项：过滤与批量完成（中等）
- 添加 `GET /action-items?completed=true|false` 以按完成状态过滤。
- 添加 `POST /action-items/bulk-complete`，它接受一组 ID，并在一个事务中把它们标记为已完成。
- 更新前端，加上过滤开关和批量操作 UI。
- 添加测试，覆盖过滤、批量行为以及出错时的事务回滚。

## 5) 具备多对多关系的标签功能（复杂）
- 添加 `Tag` 模型和一张连接表 `note_tags`（`Note` 与 `Tag` 之间的多对多）。
- 端点：
 - `GET /tags`、`POST /tags`、`DELETE /tags/{id}`
 - `POST /notes/{id}/tags` 用于附加，`DELETE /notes/{id}/tags/{tag_id}` 用于解除
- 更新提取逻辑（见下一个任务），从 `#hashtags` 自动创建/附加标签。
- 更新 UI，把标签显示为标签片（chip），并支持按标签过滤笔记。
- 为模型关系与端点行为添加测试。

## 6) 改进提取逻辑与端点（中等）
- 扩展 `backend/app/services/extract.py` 以解析：
 - `#hashtags` → 标签
 - `- [ ] task text` → 行动项
- 添加 `POST /notes/{id}/extract`：
 - 返回结构化的提取结果，并在 `apply=true` 时可选地持久化新的标签/行动项。
- 为提取解析和 `apply=true` 的持久化路径添加测试。

## 7) 健壮的错误处理与响应信封（简单–中等）
- 用 Pydantic 模型添加校验（最小长度约束、非空字符串）。
- 添加全局异常处理器，返回一致的 JSON 信封：
 - `{ "ok": false, "error": { "code": "NOT_FOUND", "message": "..." } }`
 - 成功响应：`{ "ok": true, "data": ... }`
- 更新测试，对成功与错误两种情况都断言信封结构。

## 8) 为所有集合的列表端点添加分页（简单）
- 为 `GET /notes` 和 `GET /action-items` 添加 `page` 与 `page_size`。
- 每个都返回 `items` 与 `total`。
- 更新前端以对列表分页；为边界情况（最后一页为空、page size 过大）添加测试。

## 9) 查询性能与索引（简单–中等）
- 在有益处添加 SQLite 索引（例如 `notes.title`、标签的连接表）。
- 验证查询计划得到改善，并通过灌入更大数据集的测试确保没有回归。

## 10) 提升测试覆盖率（简单）
- 添加测试，覆盖：
 - 每个端点的 400/404 场景
 - 批量操作的并发/事务行为
 - 针对检索、分页和乐观更新的前端集成测试（可以用 mock，或做得轻量）

## 11) 可部署到 Vercel（中等–复杂）
- 前端使用 Vite + React：
 - 添加带有 `build` 和 `preview` 脚本的 `package.json`，并配置 Vite 输出到 `frontend/dist`（或 `frontend/ui/dist`）。
 - 添加 `vercel.json`，把项目根目录设为 `week5/frontend`，把 `outputDirectory` 设为 `dist`。
 - 在构建时注入 `VITE_API_BASE_URL`，指向该 API。
- API 部署在 Vercel（方案 A，无服务器 FastAPI）：
 - 创建 `week5/api/index.py`，从 `backend/app/main.py` 导入 FastAPI 的 `app`。
 - 确保 Vercel 能获取 Python 依赖（为该函数使用 `pyproject.toml` 或 `requirements.txt`）。
 - 配置 CORS，允许 Vercel 前端的源（origin）。
 - 更新 `vercel.json`，把 `/api/*` 路由到该 Python 函数，其他路由提供 React 应用。
- API 部署在别处（方案 B）：
 - 把后端部署到 Fly.io 或 Render 这类服务上。
 - 配置 Vercel 前端通过 `VITE_API_BASE_URL` 使用这个外部 API，并设置所需的任何重写/反向代理。
- 在 `README.md` 中添加一份简短的部署指南，包括环境变量、构建命令和回滚。
