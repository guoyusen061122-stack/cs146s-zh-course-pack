# 第 1 周 — 提示词技巧

你将通过编写提示词来完成特定任务，从而练习多种提示词技巧。每个任务的说明就在其对应源文件的开头。

## 安装
请确认你已经完成顶层 `README.md` 中描述的安装。 

## 安装 Ollama
我们将使用一个名为 [Ollama](https://ollama.com/) 的工具，在你的机器上本地运行各类前沿大语言模型（LLM）。请任选以下方法之一：

- macOS（Homebrew）：
  ```bash
  brew install --cask ollama 
  ollama serve
  ```

- Linux（推荐）：
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- Windows：
  从 [ollama.com/download](https://ollama.com/download) 下载并运行安装程序。

验证安装：
```bash
ollama -v
```

在运行测试脚本之前，请确认已拉取以下模型。这只需做一次（除非你之后删除了这些模型）：
```bash
ollama run mistral-nemo:12b
ollama run llama3.1:8b
```

## 技巧与源文件
- K 样本提示词 — `week1/k_shot_prompting.py`
- 思维链 — `week1/chain_of_thought.py`
- 工具调用 — `week1/tool_calling.py`
- 自洽性提示词 — `week1/self_consistency_prompting.py`
- RAG（检索增强生成） — `week1/rag.py`
- 反思（Reflexion） — `week1/reflexion.py`

## 交付物
- 阅读每个文件中的任务说明。
- 设计并运行提示词（找出代码中所有标注 `TODO` 的位置）。这应当是你唯一需要改动的地方（也就是说，不要去折腾模型）。 
- 反复迭代改进结果，直到测试脚本通过。
- 保存每种技巧的最终提示词与输出。
- 务必在提交中包含每个提示词技巧文件的完整代码。***请再核对一遍所有 `TODO` 都已解决。***

## 评分标准（总分 60 分）
- 6 种不同的提示词技巧，每完成一个提示词得 10 分