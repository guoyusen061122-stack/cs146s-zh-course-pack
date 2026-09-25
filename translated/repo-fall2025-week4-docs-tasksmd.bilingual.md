# Tasks for Repo

# 仓库任务

## 1) Enable pre-commit and fix the repo

## 1) 启用提交前钩子并修复仓库

- Install hooks: `pre-commit install`
- Run: `pre-commit run --all-files`
- Fix any formatting/lint issues (black/ruff)

- 安装钩子：`pre-commit install`
- 运行：`pre-commit run --all-files`
- 修复所有格式化/静态检查问题（black/ruff）

## 2) Add search endpoint for notes

## 2) 为笔记添加检索端点

- Add/extend `GET /notes/search?q=...` (case-insensitive) using SQLAlchemy filters
- Update `frontend/app.js` to use the search query
- Add tests in `backend/tests/test_notes.py`

- 用 SQLAlchemy 过滤器添加/扩展 `GET /notes/search?q=...`（不区分大小写）
- 更新 `frontend/app.js` 以使用该检索查询
- 在 `backend/tests/test_notes.py` 中添加测试

## 3) Complete action item flow

## 3) 补全行动项流程

- Implement `PUT /action-items/{id}/complete` (already scaffolded)
- Update UI to reflect completion (already wired) and extend test coverage

- 实现 `PUT /action-items/{id}/complete`（脚手架已就绪）
- 更新界面以反映完成状态（接线已完成），并扩展测试覆盖

## 4) Improve extraction logic

## 4) 改进抽取逻辑

- Extend `backend/app/services/extract.py` to parse tags like `#tag` and return them
- Add tests for the new parsing behavior
- (Optional) Expose `POST /notes/{id}/extract` that turns notes into action items

- 扩展 `backend/app/services/extract.py`，解析 `#tag` 这类标签并返回
- 为新的解析行为添加测试
- （可选）暴露 `POST /notes/{id}/extract`，把笔记转换为行动项

## 5) Notes CRUD enhancements

## 5) 笔记 CRUD 增强

- Add `PUT /notes/{id}` to edit a note (title/content)
- Add `DELETE /notes/{id}` to delete a note
- Update `frontend/app.js` to support edit/delete; add tests

- 添加 `PUT /notes/{id}` 以编辑笔记（标题/内容）
- 添加 `DELETE /notes/{id}` 以删除笔记
- 更新 `frontend/app.js` 以支持编辑/删除；并添加测试

## 6) Request validation and error handling

## 6) 请求校验与错误处理

- Add simple validation rules (e.g., min lengths) to `schemas.py`
- Return informative 400/404 errors where appropriate; add tests for validation failures

- 在 `schemas.py` 中添加简单的校验规则（例如最小长度）
- 在合适的位置返回带说明的 400/404 错误；为校验失败添加测试

## 7) Docs drift check (manual for now)

## 7) 文档漂移检查（目前手工进行）

- Create/maintain a simple `API.md` describing endpoints and payloads
- After each change, verify docs match actual OpenAPI (`/openapi.json`)

- 创建/维护一份简单的 `API.md`，描述各端点与载荷
- 每次改动后，核对文档是否与实际 OpenAPI（`/openapi.json`）一致
