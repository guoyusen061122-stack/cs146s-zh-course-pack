# Week 8 – Multi-Stack AI-Accelerated Web App Build

# 第 8 周 – 多技术栈 AI 加速的 Web 应用构建

## Demo Day Confirmation

## 演示日确认

Please navigate to this [form](https://forms.gle/J3R3PSRqnFAJxhjG8) for details about our class demo day.

请访问这份[表单](https://forms.gle/J3R3PSRqnFAJxhjG8)，了解我们课堂演示日的详细信息。

## Assignment Overview

## 作业概述

Build the same functional web application in 3 distinct technology stacks. At least one version must be created using [`bolt.new`](https://bolt.new/), an AI app generation platform. At least one version must use a non-JavaScript language for either the frontend or backend (e.g., Django, Ruby on Rails).

用 3 种不同的技术栈构建同一个功能完整的 Web 应用。至少有一个版本必须使用 AI 应用生成平台 [`bolt.new`](https://bolt.new/) 创建。至少有一个版本必须在前端或后端中使用非 JavaScript 语言（例如 Django、Ruby on Rails）。

You may reuse the app from previous weeks (the "developer control center") or create a new app of your choosing, as long as it meets the [minimum functional scope](#minimum-functional-scope). The app should be end-to-end functional (frontend + backend + persistence where applicable) and demonstrate a coherent feature set.

你可以复用前几周的应用（“开发者控制中心”），也可以自选创建一个新应用，只要它满足[最小功能范围](#minimum-functional-scope)。应用应端到端可用（前端 + 后端 + 在适用处包含持久化），并展示一组连贯的功能。

## Minimum Functional Scope

## 最小功能范围

- User can create, read, update, and delete a primary resource (e.g., notes, tasks, posts).
- Persistent storage (database or file-based) where appropriate for the stack.
- Basic validation and error handling.
- Simple but functional UI that surfaces the main flows.
- Clear instructions to run each version locally (and deploy links if you deploy).

- 用户可以创建、读取、更新和删除某个主要资源（例如笔记、任务、帖子）。
- 在该技术栈适用的地方使用持久化存储（数据库或基于文件）。
- 基本的校验与错误处理。
- 简单但可用的 UI，能呈现主要流程。
- 清晰的本地运行说明（如果部署了，还要提供部署链接）。

## Stack Requirements

## 技术栈要求

Build 3 separate versions of the same app, each of which use a distinct stack. Examples:

构建同一个应用的 3 个独立版本，每个版本使用不同的技术栈。示例：

- MERN (MongoDB, Express, React, Node.js)
- MEVN (MongoDB, Express, Vue.js, Node.js)
- Django + React (or Vue)
- Flask + Vanilla JS (or React)
- Next.js + Node (or NestJS)
- Ruby on Rails (full-stack)

- MERN（MongoDB、Express、React、Node.js）
- MEVN（MongoDB、Express、Vue.js、Node.js）
- Django + React（或 Vue）
- Flask + Vanilla JS（或 React）
- Next.js + Node（或 NestJS）
- Ruby on Rails（全栈）

Reminder that at least one version must include a non-JavaScript language for either frontend or backend (e.g., Python/Django, Ruby/Rails).

提醒一下，至少有一个版本必须在前端或后端中包含非 JavaScript 语言（例如 Python/Django、Ruby/Rails）。

At least one version must be built using the AI app generation platform **[`bolt.new`](https://bolt.new/)**, but feel free to explore other app generation platforms (e.g. Lovable, Figma Make) for the other versions.

至少有一个版本必须使用 AI 应用生成平台 **[`bolt.new`](https://bolt.new/)** 构建，但其他版本欢迎尝试别的应用生成平台（例如 Lovable、Figma Make）。

## Learn about Bolt

## 了解 Bolt

Bolt is an AI-assisted development platform that generates websites, web apps, and mobile apps from natural language prompts. Users can describe their idea in plain text, and Bolt produces a functional prototype—ranging from landing pages and e-commerce sites to CRMs and mobile tools—within minutes. Learn more [here](https://support.bolt.new/building/intro-bolt).

Bolt 是一个 AI 辅助开发平台，能从自然语言提示词生成网站、Web 应用和移动应用。用户可以用纯文本描述自己的想法，Bolt 会在几分钟内产出一个可用的原型——从落地页、电商网站到 CRM 和移动工具都行。在[这里](https://support.bolt.new/building/intro-bolt)了解更多。

### Claim your Bolt Credits:

### 领取你的 Bolt 额度：

1. Locate the unique Bolt promotion code that we've emailed to you.
1. Navigate to [bolt.new](bolt.new) and create an account.
1. In Personal Settings > Subscriptions & Tokens, in the Upgrade to Pro block, click the blue "Upgrade" button.
1. Select "Add promotion code" and paste your unqiue promotion code into this field.
1. You’ll receive 3 months of Bolt Pro for free. A credit card is required to activate the trial. **Remember to cancel before the 3-month period ends to avoid automatic billing if you don’t plan to continue your subscription.**

1. 找到我们通过电子邮件发给你的专属 Bolt 优惠码。
1. 访问 [bolt.new](bolt.new) 并创建一个账号。
1. 在 Personal Settings > Subscriptions & Tokens 中，在 Upgrade to Pro 区块里点击蓝色的 "Upgrade" 按钮。
1. 选择 "Add promotion code"，把你的专属优惠码粘贴到这个字段中。
1. 你将免费获得 3 个月的 Bolt Pro。激活试用需要信用卡。**如果你不打算继续订阅，请记得在 3 个月期限结束前取消，以免自动扣费。**

## Tips for Usage of AI App Generators

## 使用 AI 应用生成器的技巧

- App generators like Bolt are best-suited for modern full-stack technologies, which you will get by default when using them without specifying specific frameworks.
- Prefer starting from a clean prompt describing your app concept, entities, routes, and UI flows.
- Clearly describe data models and relationships in your prompts.
- Iteratively refine prompts for data models, CRUD endpoints, auth (if used), and frontend components.
- Keep each version isolated to avoid dependency conflicts.
- Export or sync generated code and commit it as a standalone project folder for that stack.

- 像 Bolt 这样的应用生成器最适合现代全栈技术，在不指定具体框架时，它们默认就会采用这些技术。
- 最好从一个干净的提示词开始，描述你的应用概念、实体、路由和 UI 流程。
- 在提示词中清楚描述数据模型及其关系。
- 针对数据模型、CRUD 端点、认证（如果用到）和前端组件，迭代地优化提示词。
- 让每个版本相互隔离，避免依赖冲突。
- 导出或同步生成的代码，并把它作为一个独立的项目文件夹提交到该技术栈下。

## Deliverables

## 交付物

1. **THREE** project folders (one per version) within the `week8/` folder, each including:
1. Source code
1. `README.md` with prerequisites, installation/set-up instructions, run, and env configuration
1. Notes on deviations, known issues, and any manual fixes after generation
1. Completed `writeup.md` file:
1. App Concept
1. 3 App Descriptions (1 per version)

1. `week8/` 文件夹内的 **三个**项目文件夹（每个版本一个），各自包含：
1. 源代码
1. `README.md`，包含前置条件、安装/搭建说明、运行方式和环境配置
1. 关于偏差、已知问题以及生成后任何手动修复的说明
1. 已完成的 `writeup.md` 文件：
1. 应用概念
1. 3 份应用描述（每个版本 1 份）

## Grading Rubric (100 points)

## 评分标准（100 分）

- App concept meets minimum functional scope (10 pts)
- Three distinct tech stacks (10 pts)
- Usage of Bolt in at least one version (10 pts)
- Usage of a non-JS language in at least one version (10 pts)
- Three version of the app (20 pts **each**):
- Source code provided in a folder in `week8/`(5pts)
- README.md: prerequisites, installation/set-up instructions, run, and env configuration (5 pts)
- App functionality (5 pts)
- Complete version description detailed in `writeup.md` (5 pts)

- 应用概念满足最小功能范围（10 分）
- 三种不同的技术栈（10 分）
- 至少一个版本使用了 Bolt（10 分）
- 至少一个版本使用了非 JS 语言（10 分）
- 应用的三个版本（**每个** 20 分）：
- 源代码放在 `week8/` 下的文件夹中（5 分）
- README.md：前置条件、安装/搭建说明、运行方式和环境配置（5 分）
- 应用功能（5 分）
- 在 `writeup.md` 中详细说明的完整版本描述（5 分）
