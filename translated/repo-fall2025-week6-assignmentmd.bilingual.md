# Week 6 — Scan and Fix Vulnerabilities with Semgrep

# 第 6 周 — 用 Semgrep 扫描并修复漏洞

## Assignment Overview

## 作业概述

Run static analysis against the provided app in `week6/` using **Semgrep**. Triage findings and remediate a minimum of 3 security issues. In your write-up, explain what issues Semgrep surfaced and how you fixed them.

用 **Semgrep** 对 `week6/` 中提供的应用运行静态分析。对发现结果做分级判断，并修复至少 3 个安全问题。在书面报告中，说明 Semgrep 暴露了哪些问题，以及你是如何修复它们的。

## Learn about Semgrep

## 了解 Semgrep

Semgrep is an open-source, static analysis tool that searches code, finds bugs, and enforces secure guardrails and coding standards.

Semgrep 是一款开源的静态分析工具，可以检索代码、发现 bug，并强制执行安全护栏与编码标准。

1. Click [here](https://github.com/semgrep/semgrep/blob/develop/README.md) to learn about Semgrep.

1. 点击[这里](https://github.com/semgrep/semgrep/blob/develop/README.md)了解 Semgrep。

1. Follow the installation instructions in the link above. It is up to you whether you prefer to use the **Semgrep Appsec Platform** or the **CLI tool**.

1. 按照上文链接中的安装说明操作。你更愿意使用 **Semgrep Appsec Platform** 还是 **CLI 工具**，由你自己决定。

## Scan tasks

## 扫描任务

### What you will scan

### 你要扫描的内容

- Backend Python (FastAPI): `week6/backend/`
- Frontend JavaScript: `week6/frontend/`
- Dependencies: `week6/requirements.txt`
- Config/env (for secrets): files within `week6/`

- 后端 Python（FastAPI）：`week6/backend/`
- 前端 JavaScript：`week6/frontend/`
- 依赖：`week6/requirements.txt`
- 配置/环境文件（用于查找密钥）：`week6/` 内的文件

### Run a general security scan plus focused scans for secrets and dependencies.

### 运行一次通用安全扫描，外加针对密钥与依赖的专项扫描。

From the **assignment repository root**, run the following command to apply a curated CI-style bundle that includes both code and secrets rules:

在**作业仓库根目录**下，运行以下命令以应用一套精选的 CI 风格规则包，其中同时包含代码规则与密钥规则：

```bash
semgrep ci --subdir week6
```

## Task

## 任务

1. Pick any 3 issues identified by Semgrep and fix them using an AI coding tool of your choice.

1. 从 Semgrep 识别出的问题中任选 3 个，用你自选的 AI 编码工具修复它们。

1. Show precise edits and explain the mitigation (e.g., parameterized SQL, safer APIs, stronger crypto, sanitized DOM writes, restricted CORS, dependency upgrades).

1. 展示精确的改动，并解释缓解措施（例如参数化 SQL、更安全的 API、更强的加密、净化后的 DOM 写入、受限的 CORS、依赖升级）。

1. Important: Ensure the app still runs and tests still pass after your fixes.

1. 重要：确保修复之后应用仍能运行，测试仍能通过。

## Deliverables

## 交付物

### 1. Brief findings overview

### 1. 主要发现概述

- Summarize the categories Semgrep reported (SAST/Secrets/SCA).
- Note any false positives or noisy rules you chose to ignore and why.

- 总结 Semgrep 报告的问题类别（SAST/密钥/SCA）。
- 记录你选择忽略的误报或噪声规则，并说明原因。

### 2. Three fixes (before → after)

### 2. 三处修复（修复前 → 修复后）

For each fixed issue:

对每个修复的问题：

- File and line(s)
- Rule/category Semgrep flagged
- Brief risk description
- Your change (short code diff or explanation, AI coding tool usage)
- Why this mitigates the issue

- 文件与行号
- Semgrep 标记的规则/类别
- 风险简要描述
- 你的改动（简短代码差异（diff）或说明，AI 编码工具的使用）
- 该改动为何能缓解此问题

## Tips

## 小技巧

- Prefer minimal, targeted changes that address the root cause.
- Re‑run Semgrep after each fix to confirm the finding is resolved and no new ones were introduced.
- For dependencies, document upgraded versions and link to advisories if you used supply-chain scanning.

- 优先选择最小、有针对性的改动，直击根因。
- 每次修复后重新运行 Semgrep，确认该发现已解决，且没有引入新的发现。
- 对于依赖，记录升级后的版本；如果你使用了供应链扫描，请附上公告链接。

## Submission Instructions

## 提交说明

1. Make sure you have all changes pushed to your remote repository for grading.
1. Make sure you've added both brentju and febielin as collaborators on your assignment repository.
1. Submit via Gradescope.

1. 确保所有改动都已推送到你的远程仓库以便评分。
1. 确保你已将 brentju 和 febielin 都添加为作业仓库的协作者。
1. 通过 Gradescope 提交。
