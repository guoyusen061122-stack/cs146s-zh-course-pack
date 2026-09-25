# Week 2 – Action Item Extractor

# 第 2 周 – 行动项提取器

This week, we will be expanding upon a minimal FastAPI + SQLite app that converts free‑form notes into enumerated action items.

本周，我们将扩展一个极简的 FastAPI + SQLite 应用，它能把自由形式的笔记转换成逐条列出的行动项。

***We recommend reading this entire document before getting started.***

***我们建议你在开始之前先通读整份文档。***

Tip: To preview this markdown file

提示：预览这个 markdown 文件的方法

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

- 在 Mac 上，按 `Command (⌘) + Shift + V`
- 在 Windows/Linux 上，按 `Ctrl + Shift + V`

## Getting Started

## 开始上手

### Cursor Set Up

### Cursor 设置

Follow these instructions to set up Cursor and open your project:

按照以下说明设置 Cursor 并打开你的项目：

1. Redeem your free year of Cursor Pro: https://cursor.com/students
1. Download Cursor: https://cursor.com/download
1. To enable the Cursor command line tool, open Cursor and press `Command (⌘) + Shift+ P` for Mac users (or `Ctrl + Shift + P` for non-Mac users) to open the Command Palette. Type: `Shell Command: Install 'cursor' command`. Select it and hit Enter.
1. Open a new terminal window, navigate to your project root, and run: `cursor .`

1. 兑换 Cursor Pro 的免费一年使用权：https://cursor.com/students
1. 下载 Cursor：https://cursor.com/download
1. 要启用 Cursor 命令行工具，Mac 用户打开 Cursor 并按 `Command (⌘) + Shift+ P`（非 Mac 用户按 `Ctrl + Shift + P`）打开命令面板。输入：`Shell Command: Install 'cursor' command`。选中它并按回车。
1. 打开一个新的终端窗口，进入你的项目根目录，然后运行：`cursor .`

### Current Application

### 当前应用

Here's how you can start running the current starter application:

以下是启动当前起始应用的方法：

1. Activate your conda environment.

1. 激活你的 conda 环境。

```
conda activate cs146s 
```

1. From the project root, run the server:

1. 在项目根目录下运行服务器：

```
poetry run uvicorn week2.app.main:app --reload
```

1. Open a web browser and navigate to http://127.0.0.1:8000/.
1. Familiarize yourself with the current state of the application. Make sure you can successfully input notes and produce the extracted action item checklist.

1. 打开浏览器并访问 http://127.0.0.1:8000/。
1. 熟悉该应用的当前状态。确认你能成功输入笔记并生成提取出的行动项清单。

## Exercises

## 练习

For each exercise, use Cursor to help you implement the specified improvements to the current action item extractor application.

对每个练习，都使用 Cursor 帮助你完成对当前行动项提取器应用的指定改进。

As you work through the assignment, use `writeup.md` to document your progress. Be sure to include the prompts you use, as well as any changes made by you or Cursor. We will be grading based on the contents of the write-up. Please also include comments throughout your code to document your changes.

在做作业的过程中，用 `writeup.md` 记录你的进展。务必包含你使用的提示词，以及你或 Cursor 做出的任何改动。我们将根据书面报告的内容评分。另外，请在你的代码中随处加上注释，说明你的改动。

### TODO 1: Scaffold a New Feature

### TODO 1：为新功能搭脚手架

Analyze the existing `extract_action_items()` function in `week2/app/services/extract.py`, which currently extracts action items using predefined heuristics.

分析 `week2/app/services/extract.py` 中现有的 `extract_action_items()` 函数，它目前使用预定义的启发式规则提取行动项。

Your task is to implement an **LLM-powered** alternative, `extract_action_items_llm()`, that utilizes Ollama to perform action item extraction via a large language model.

你的任务是实现一个**由 LLM 驱动**的替代方案 `extract_action_items_llm()`，它利用 Ollama 通过大语言模型完成行动项提取。

Some  tips:

一些提示：

- To produce structured outputs (i.e. JSON array of strings), refer to this documentation: https://ollama.com/blog/structured-outputs
- To browse available Ollama models, refer to this documentation: https://ollama.com/library. Note that larger models will be more resource-intensive, so start small. To pull and run a model: `ollama run {MODEL_NAME}`

- 要生成结构化输出（即字符串组成的 JSON 数组），请参考这份文档：https://ollama.com/blog/structured-outputs
- 要浏览可用的 Ollama 模型，请参考这份文档：https://ollama.com/library。注意，更大的模型会占用更多资源，所以从小模型开始。拉取并运行模型：`ollama run {MODEL_NAME}`

### TODO 2: Add Unit Tests

### TODO 2：添加单元测试

Write unit tests for `extract_action_items_llm()` covering multiple inputs (e.g., bullet lists, keyword-prefixed lines, empty input) in `week2/tests/test_extract.py`.

在 `week2/tests/test_extract.py` 中为 `extract_action_items_llm()` 编写单元测试，覆盖多种输入（例如项目符号列表、带关键词前缀的行、空输入）。

### TODO 3: Refactor Existing Code for Clarity

### TODO 3：为提升清晰度重构现有代码

Perform a refactor of the code in the backend, focusing in particular on well-defined API contracts/schemas, database layer cleanup, app lifecycle/configuration, error handling.

对后端的代码进行一次重构，尤其关注定义良好的 API 契约/schema、数据库层清理、应用生命周期/配置、错误处理。

### TODO 4: Use Agentic Mode to Automate Small Tasks

### TODO 4：用智能体模式自动化小任务

1. Integrate the LLM-powered extraction as a new endpoint. Update the frontend to include an "Extract LLM" button that, when clicked, triggers the extraction process via the new endpoint.

1. 把 LLM 驱动的提取功能集成为一个新端点。更新前端，添加一个 "Extract LLM" 按钮，点击后通过新端点触发提取过程。

1. Expose one final endpoint to retrieve all notes. Update the frontend to include a "List Notes" button that, when clicked, fetches and displays them.

1. 暴露最后一个端点，用于获取所有笔记。更新前端，添加一个 "List Notes" 按钮，点击后获取并显示这些笔记。

### TODO 5: Generate a README from the Codebase

### TODO 5：从代码库生成 README

***Learning Goal:*** *Students learn how AI can introspect a codebase and produce documentation automatically, showcasing Cursor’s ability to parse code context and translate it into human‑readable form.*

***学习目标：*** *学生将了解 AI 如何审视代码库并自动生成文档，从而展示 Cursor 解析代码上下文并将其转化为人类可读形式的能力。*

Use Cursor to analyze the current codebase and generate a well-structured `README.md` file. The README should include, at a minimum:

使用 Cursor 分析当前代码库，生成一份结构良好的 `README.md` 文件。该 README 至少应包含：

- A brief overview of the project
- How to set up and run the project
- API endpoints and functionality
- Instructions for running the test suite

- 项目的简要概述
- 如何搭建并运行该项目
- API 端点与功能
- 运行测试套件的说明

## Deliverables

## 交付物

Fill out `week2/writeup.md` according to the instructions provided. Make sure all your changes are documented in your codebase.

按照给出的说明填写 `week2/writeup.md`。确保你的所有改动都在代码库中有记录。

## Evaluation rubric (100 pts total)

## 评分标准（总分 100 分）

- 20 points per part 1-5 (10 for the generated code and 10 for each prompt).

- 第 1–5 部分每部分 20 分（生成的代码 10 分，每个提示词 10 分）。
