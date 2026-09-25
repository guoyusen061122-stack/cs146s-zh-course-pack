# 仓库任务

## 1) 启用提交前钩子并修复仓库
- 安装钩子：`pre-commit install`
- 运行：`pre-commit run --all-files`
- 修复所有格式化/静态检查问题（black/ruff）

## 2) 为笔记添加检索端点
- 用 SQLAlchemy 过滤器添加/扩展 `GET /notes/search?q=...`（不区分大小写）
- 更新 `frontend/app.js` 以使用该检索查询
- 在 `backend/tests/test_notes.py` 中添加测试

## 3) 补全行动项流程
- 实现 `PUT /action-items/{id}/complete`（脚手架已就绪）
- 更新界面以反映完成状态（接线已完成），并扩展测试覆盖

## 4) 改进抽取逻辑
- 扩展 `backend/app/services/extract.py`，解析 `#tag` 这类标签并返回
- 为新的解析行为添加测试
- （可选）暴露 `POST /notes/{id}/extract`，把笔记转换为行动项

## 5) 笔记 CRUD 增强
- 添加 `PUT /notes/{id}` 以编辑笔记（标题/内容）
- 添加 `DELETE /notes/{id}` 以删除笔记
- 更新 `frontend/app.js` 以支持编辑/删除；并添加测试

## 6) 请求校验与错误处理
- 在 `schemas.py` 中添加简单的校验规则（例如最小长度）
- 在合适的位置返回带说明的 400/404 错误；为校验失败添加测试

## 7) 文档漂移检查（目前手工进行）
- 创建/维护一份简单的 `API.md`，描述各端点与载荷
- 每次改动后，核对文档是否与实际 OpenAPI（`/openapi.json`）一致
