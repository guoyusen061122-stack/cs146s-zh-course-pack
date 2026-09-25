# 第 2 周 – 行动项提取器

本周，我们将扩展一个极简的 FastAPI + SQLite 应用，它能把自由形式的笔记转换成逐条列出的行动项。

***我们建议你在开始之前先通读整份文档。***

提示：预览这个 markdown 文件的方法
- 在 Mac 上，按 `Command (⌘) + Shift + V`
- 在 Windows/Linux 上，按 `Ctrl + Shift + V`


## 开始上手

### Cursor 设置
按照以下说明设置 Cursor 并打开你的项目：
1. 兑换 Cursor Pro 的免费一年使用权：https://cursor.com/students
2. 下载 Cursor：https://cursor.com/download
3. 要启用 Cursor 命令行工具，Mac 用户打开 Cursor 并按 `Command (⌘) + Shift+ P`（非 Mac 用户按 `Ctrl + Shift + P`）打开命令面板。输入：`Shell Command: Install 'cursor' command`。选中它并按回车。
4. 打开一个新的终端窗口，进入你的项目根目录，然后运行：`cursor .`

### 当前应用
以下是启动当前起始应用的方法： 
1. 激活你的 conda 环境。
```
conda activate cs146s 
```
2. 在项目根目录下运行服务器：
```
poetry run uvicorn week2.app.main:app --reload
```
3. 打开浏览器并访问 http://127.0.0.1:8000/。
4. 熟悉该应用的当前状态。确认你能成功输入笔记并生成提取出的行动项清单。 

## 练习
对每个练习，都使用 Cursor 帮助你完成对当前行动项提取器应用的指定改进。

在做作业的过程中，用 `writeup.md` 记录你的进展。务必包含你使用的提示词，以及你或 Cursor 做出的任何改动。我们将根据书面报告的内容评分。另外，请在你的代码中随处加上注释，说明你的改动。 

### TODO 1：为新功能搭脚手架

分析 `week2/app/services/extract.py` 中现有的 `extract_action_items()` 函数，它目前使用预定义的启发式规则提取行动项。

你的任务是实现一个**由 LLM 驱动**的替代方案 `extract_action_items_llm()`，它利用 Ollama 通过大语言模型完成行动项提取。

一些提示：
- 要生成结构化输出（即字符串组成的 JSON 数组），请参考这份文档：https://ollama.com/blog/structured-outputs 
- 要浏览可用的 Ollama 模型，请参考这份文档：https://ollama.com/library。注意，更大的模型会占用更多资源，所以从小模型开始。拉取并运行模型：`ollama run {MODEL_NAME}`

### TODO 2：添加单元测试 

在 `week2/tests/test_extract.py` 中为 `extract_action_items_llm()` 编写单元测试，覆盖多种输入（例如项目符号列表、带关键词前缀的行、空输入）。

### TODO 3：为提升清晰度重构现有代码

对后端的代码进行一次重构，尤其关注定义良好的 API 契约/schema、数据库层清理、应用生命周期/配置、错误处理。 

### TODO 4：用智能体模式自动化小任务

1. 把 LLM 驱动的提取功能集成为一个新端点。更新前端，添加一个 "Extract LLM" 按钮，点击后通过新端点触发提取过程。

2. 暴露最后一个端点，用于获取所有笔记。更新前端，添加一个 "List Notes" 按钮，点击后获取并显示这些笔记。

### TODO 5：从代码库生成 README

***学习目标：***
*学生将了解 AI 如何审视代码库并自动生成文档，从而展示 Cursor 解析代码上下文并将其转化为人类可读形式的能力。*

使用 Cursor 分析当前代码库，生成一份结构良好的 `README.md` 文件。该 README 至少应包含：
- 项目的简要概述
- 如何搭建并运行该项目
- API 端点与功能
- 运行测试套件的说明

## 交付物
按照给出的说明填写 `week2/writeup.md`。确保你的所有改动都在代码库中有记录。 

## 评分标准（总分 100 分）
- 第 1–5 部分每部分 20 分（生成的代码 10 分，每个提示词 10 分）。