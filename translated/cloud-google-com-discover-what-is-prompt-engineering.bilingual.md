# Prompt Engineering Overview

# 提示工程概览

# Prompt engineering: overview and guide

# 提示工程：概览与指南

*Last Updated: 05/04/2026*

*最后更新：05/04/2026*

The rise of large language models (LLMs) has brought forth exciting possibilities for human-computer interaction. However, harnessing the full potential of these powerful AI models requires a crucial skill: prompt engineering. This burgeoning field focuses on crafting effective prompts that unlock the [capabilities of LLMs](https://cloud.google.com/ai/llms), enabling them to understand intent, follow instructions, and generate desired outputs. As we increasingly interact with AI in various applications, prompt engineering plays a vital role in ensuring accurate, relevant, and safe interactions.

大语言模型（LLM）的兴起为人机交互带来了令人兴奋的可能性。然而，要充分发挥这些强大 AI 模型的潜力，需要一项关键技能：提示工程。这一新兴领域专注于精心设计有效的提示词，从而开启 [LLM 的能力](https://cloud.google.com/ai/llms)，让模型能够理解意图、遵循指令并生成期望的输出。随着我们在各类应用中与 AI 的互动日益增多，提示工程在确保准确、相关且安全的交互方面发挥着至关重要的作用。

Get started for free<https://console.cloud.google.com/freetrial/?redirectPath=/agent-platform/overview>

免费开始使用<https://console.cloud.google.com/freetrial/?redirectPath=/agent-platform/overview>

[![prompt engineer](https://www.gstatic.com/bricks/image/MUr6Af94qU6gNwxBGhqRbRtFxnQEWtGi3kRcV9hPlNLT-YkIjpO1aD_HriuhwwzR0OilQTK8m497.png)1:53](https://www.youtube.com/watch?v=RywP7cCYUWE)

[![提示工程师](https://www.gstatic.com/bricks/image/MUr6Af94qU6gNwxBGhqRbRtFxnQEWtGi3kRcV9hPlNLT-YkIjpO1aD_HriuhwwzR0OilQTK8m497.png)1:53](https://www.youtube.com/watch?v=RywP7cCYUWE)

Tips to becoming a world-class Prompt Engineer

成为世界级提示工程师的技巧

## What is prompt engineering?

## 什么是提示工程？

Prompt engineering is the art and science of designing and optimizing prompts to guide AI models, particularly LLMs, towards generating the desired responses. By carefully crafting prompts, you provide the model with context, instructions, and examples that help it understand your intent and respond in a meaningful way. Think of it as providing a roadmap for the AI, steering it towards the specific output you have in mind.

提示工程是设计与优化提示词的艺术与科学，目的是引导 AI 模型（尤其是 LLM）生成期望的回复。通过精心设计提示词，你为模型提供上下文、指令与示例，帮助它理解你的意图并以有意义的方式回应。可以把它理解为给 AI 提供一张路线图，把它引向你心中所想的特定输出。

To dive deeper into the world of prompt design and explore its applications, check out the [Introduction to Prompt Design](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/introduction-prompt-design) on Google Cloud.

若想深入了解提示设计的世界并探索其应用，可以查看 Google Cloud 上的[提示设计入门](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/introduction-prompt-design)。

Ready to experiment with LLMs and prompt engineering firsthand? Try the [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) free trial and experience the power of this technology.

准备好亲手试用 LLM 与提示工程了吗？试试 [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) 免费试用版，体验这项技术的力量。

## What is a prompt for AI?

## 什么是 AI 的提示词？

In the [context of AI](https://cloud.google.com/learn/what-is-artificial-intelligence), a prompt is the input you provide to the model to elicit a specific response. This can take various forms, ranging from simple questions or keywords to complex instructions, code snippets, or even creative writing samples. The effectiveness of your prompt directly influences the quality and relevance of the AI's output.

在 [AI 的上下文](https://cloud.google.com/learn/what-is-artificial-intelligence)下，提示词是你提供给模型的输入，用以引出特定的回复。它可以有多种形式，从简单的问题或关键词，到复杂的指令、代码片段，甚至创意写作样本。提示词的有效性直接影响 AI 输出的质量与相关性。

## What do you need for prompt engineering?

## 做好提示工程需要什么？

Several key elements contribute to effective prompt engineering. Mastering these allows you to communicate effectively with AI models and unlock their full potential.

有几个关键要素有助于实现有效的提示工程。掌握它们，你就能与 AI 模型有效沟通，并释放其全部潜力。

### Prompt format

### 提示词格式

The structure and style of your prompt play a significant role in guiding the AI's response. Different models may respond better to specific formats, such as:

提示词的结构与风格在引导 AI 回复方面起着重要作用。不同模型可能对特定格式反应更好，例如：

The format of your prompt plays a significant role in how the AI interprets your request. Different models may respond better to specific formats, such as [natural language questions](https://cloud.google.com/learn/what-is-natural-language-processing), direct commands, or structured inputs with specific fields. Understanding the model's capabilities and preferred format is essential for crafting effective prompts.

提示词的格式在很大程度上决定了 AI 如何理解你的请求。不同模型可能对特定格式反应更好，例如[自然语言问题](https://cloud.google.com/learn/what-is-natural-language-processing)、直接命令，或带特定字段的结构化输入。理解模型的能力与偏好格式，对设计有效的提示词至关重要。

### Context and examples

### 上下文与示例

Providing context and relevant examples within your prompt helps the AI understand the desired task and generate more accurate and relevant outputs. For instance, if you're looking for a creative story, including a few sentences describing the desired tone or theme can significantly improve the results.

在提示词中提供上下文与相关示例，有助于 AI 理解目标任务，并生成更准确、更相关的输出。例如，如果你想要一个创意故事，在提示词里加入几句描述期望语调或主题的话，就能显著改善结果。

### Fine-tuning and adapting

### 微调与适配

Fine-tuning the AI model on specific tasks or domains using tailored prompts can enhance its performance. Additionally, adapting prompts based on user feedback or model outputs can further improve the model's responses over time.

用专门定制的提示词在特定任务或领域上微调 AI 模型，可以提升其表现。此外，根据用户反馈或模型输出调整提示词，能随着时间推移进一步改善模型的回复。

### Multi-turn conversations

### 多轮对话

Designing prompts for multi-turn conversations allows users to engage in continuous and context-aware interactions with the AI model, enhancing the overall user experience.

为多轮对话设计提示词，能让用户与 AI 模型进行持续的、感知上下文的交互，从而提升整体用户体验。

## Types of prompts

## 提示词的类型

There are various types of prompts used in AI, each serving a specific purpose:

AI 中使用的提示词有多种类型，每一种都有特定用途：

### Direct prompts (Zero-shot)

### 直接提示（零样本）

Zero-shot prompting involves providing the model with a direct instruction or question without any additional context or examples.

零样本提示指直接给模型一条指令或一个问题，不提供任何额外的上下文或示例。

An example of this is idea generation, where the model is prompted to generate creative ideas or brainstorming solutions. Another example is summarization, or translation, where the model is asked to summarize or translate some piece of content.

一个例子是创意生成：提示模型产出创意想法或头脑风暴方案。另一个例子是摘要或翻译：要求模型对某段内容做摘要或翻译。

### One-, few- and multi-shot prompts

### 单样本、少样本与多样本提示

This method involves providing the model with one or more examples of the desired input-output pairs before presenting the actual prompt. This can help the model better understand the task and generate more accurate responses.

这种方法是在给出真正的提示词之前，先向模型提供一对或多对期望的输入-输出示例。这能帮助模型更好地理解任务，并生成更准确的回复。

### Chain of Thought Prompts

### 思维链提示

CoT prompting encourages the model to break down complex reasoning into a series of intermediate steps, leading to a more comprehensive and well-structured final output.

思维链（CoT）提示鼓励模型把复杂推理拆解为一系列中间步骤，从而得到更全面、结构更清晰的最终输出。

### Zero-shot CoT Prompts

### 零样本思维链提示

Combines chain of thought prompting with zero-shot prompting by asking the model to perform reasoning steps, which may often produce better output.

把思维链提示与零样本提示结合起来，要求模型执行推理步骤，这样往往能产出更好的结果。

## Use cases and examples of prompt engineering

## 提示工程的用例与示例

Here are some specific examples and use cases showing how prompt engineering helps produce customized and relevant output.

以下是一些具体示例与用例，展示提示工程如何帮助产出定制化且相关的输出。

### Language and Text Generation

### 语言与文本生成

**Scenario**

**场景**

**Instructions**

**指令**

**Example Prompt**

**示例提示词**

Creative Writing

创意写作

Craft prompts that specify genre, tone, style, and plot points to guide the AI in generating engaging narratives.

设计提示词，明确体裁、语调、风格与情节要点，引导 AI 生成引人入胜的叙事。

"Write a short story about a young woman who discovers a magical portal in her attic."

"写一个短篇故事，讲一位年轻女子在自家阁楼里发现了一道魔法传送门。"

Summarization

摘要生成

Provide the AI with text and instruct it to generate concise summaries that capture key information.

把文本交给 AI，并指示它生成抓住关键信息的简洁摘要。

“Summarize the main points of the following news article on climate change."

“总结下面这篇关于气候变化的新闻文章的要点。"

Translation

翻译

Specify the source and target languages to enable the AI to accurately translate text while preserving meaning and context.

指明源语言与目标语言，使 AI 能准确翻译文本，同时保留含义与上下文。

"Translate the following text from English to Spanish: 'The quick brown fox jumps over the lazy dog.'"

"把下面这段文字从英语翻译成西班牙语：'敏捷的棕色狐狸跳过了那只懒狗。'"

Dialogue

对话

Design prompts that simulate conversations, allowing the AI to generate responses that mimic human interaction and maintain context.

设计能模拟对话的提示词，让 AI 生成模仿人类互动并维持上下文的回复。

"You are a friendly chatbot helping users troubleshoot their computer problems. Respond to the user's query: 'My computer won't turn on.'"

"你是一个友好的聊天机器人，帮助用户排查电脑问题。请回复用户的提问：'My computer won't turn on.'"

### Question Answering

### 问答

Open-Ended Questions

开放式问题

Formulate prompts that encourage the AI to provide comprehensive and informative answers based on its knowledge base.

设计提示词，鼓励 AI 基于自身知识库给出全面且信息充分的回答。

"Explain the concept of quantum computing and its potential impact on the future of technology."

"解释量子计算的概念及其对未来技术的潜在影响。"

Specific Questions

具体问题

Design prompts that target specific information, enabling the AI to retrieve precise answers from the provided context or its internal knowledge base.

设计针对特定信息的提示词，使 AI 能从提供的上下文或内部知识库中检索出精确答案。

"What is the capital of France?" or "According to the provided text, what are the main causes of deforestation?"

"法国的首都是哪里？"或"根据所提供的文本，导致森林砍伐的主要原因有哪些？"

Multiple Choice Questions

多项选择题

Present prompts with options, prompting the AI to analyze and select the most appropriate answer based on its understanding of the context.

给出带选项的提示词，促使 AI 基于对上下文的理解分析并选出最合适的答案。

"Who wrote the Harry Potter series? A) J.R.R. Tolkien, B) J.K. Rowling, C) Stephen King"

"《哈利·波特》系列是谁写的？A) J.R.R. Tolkien, B) J.K. Rowling, C) Stephen King"

Hypothetical Questions

假设性问题

Craft prompts that explore hypothetical situations, allowing the AI to reason, speculate, and provide potential outcomes or solutions.

设计探讨假设情景的提示词，让 AI 进行推理、推测，并给出可能的结果或解决方案。

"What would happen if humans could travel at the speed of light?"

"如果人类能以光速旅行，会发生什么？"

Opinion-Based Questions

观点类问题

Design prompts that elicit the AI's perspective or opinion on a specific topic, encouraging it to provide reasoning and justification for its stance.

设计能引出 AI 对特定话题看法或观点的提示词，鼓励它为自身立场给出推理与论证。

"Do you believe that artificial intelligence will eventually surpass human intelligence? Why or why not?"

"你认为人工智能最终会超越人类智能吗？为什么？"

### Code Generation

### 代码生成

Code Completion

代码补全

Provide the AI with a partial code snippet and prompt it to suggest or complete the remaining code based on the context and programming language.

给 AI 一段不完整的代码片段，提示它根据上下文与编程语言建议或补全其余代码。

"Write a Python function to calculate the factorial of a given number."

"写一个 Python 函数，计算给定数字的阶乘。"

Code Translation

代码翻译

Specify the source and target programming languages to enable the AI to translate code while preserving functionality and syntax.

指明源编程语言与目标编程语言，使 AI 能在保留功能与语法的前提下翻译代码。

"Translate the following Python code to JavaScript: def greet(name): print('Hello,', name)"

"把下面的 Python 代码翻译成 JavaScript：def greet(name): print('Hello,', name)"

Code Optimization

代码优化

Prompt the AI to analyze existing code and suggest improvements for efficiency, readability, or performance.

提示 AI 分析现有代码，并针对效率、可读性或性能提出改进建议。

"Optimize the following Python code to reduce its execution time."

"优化下面的 Python 代码，缩短其执行时间。"

Code Debugging

代码调试

Provide the AI with code containing errors and prompt it to identify and suggest potential solutions for the identified issues.

给 AI 一段含错误的代码，提示它找出问题并给出可能的解决方案。

"Debug the following Java code and explain why it is throwing a NullPointerException."

"调试下面的 Java 代码，并解释它为什么会抛出 NullPointerException。"

### Image Generation

### 图像生成

Photorealistic Images

照片级真实感图像

Craft prompts that describe the desired image in detail, including objects, scenery, lighting, and style, to generate realistic and high-quality images.

设计详细描述期望图像的提示词，涵盖对象、场景、光照与风格，以生成逼真且高质量的图像。

"A photorealistic image of a sunset over the ocean with palm trees silhouetted against the sky."

"一幅照片级真实感的图像：夕阳落在海面上，棕榈树的剪影映在天空中。"

Artistic Images

艺术风格图像

Design prompts that specify art styles, techniques, and subject matter to guide the AI in creating images that mimic specific artistic movements or evoke certain emotions.

设计明确艺术风格、技法与题材的提示词，引导 AI 创作模仿特定艺术流派或唤起特定情绪的图像。

"An impressionist painting of a bustling city street with people walking under umbrellas in the rain."

"一幅印象派油画：熙熙攘攘的城市街道，人们在雨中打着伞行走。"

Abstract Images

抽象图像

Formulate prompts that encourage the AI to generate images that are open to interpretation, utilizing shapes, colors, and textures to evoke feelings or concepts.

设计鼓励 AI 生成可多义解读图像的提示词，利用形状、色彩与质感唤起某种感受或概念。

"An abstract image representing the concept of hope, using bright colors and flowing shapes."

"一幅表达希望这一概念的抽象图像，使用明亮的色彩与流动的形状。"

Image Editing

图像编辑

Provide the AI with an existing image and specify desired modifications, enabling it to edit and enhance the image according to the given instructions.

给 AI 一张现有图像并指明期望的修改，让它按给定指令编辑并增强图像。

"Change the background of this photo to a starry night sky and add a full moon." or "Remove the person from this image and replace them with a cat."

"把这张照片的背景换成都市夜空，并添加一轮满月。"或"把这张图里的人去掉，换成一只猫。"

## Strategies for writing better prompts

## 写出更好提示词的策略

Developing effective prompts requires a strategic approach. Consider these strategies to enhance your prompt engineering skills:

写有效的提示词需要策略性的方法。可以参考以下策略来提升你的提示工程能力：

### 1. Set Clear Goals and Objectives:

### 1. 设定清晰的目标与目的：

**Tactic**

**策略**

**Prompt Example**

**提示词示例**

Use action verbs to specify the desired action

用动作动词指明期望的动作

"Write a bulleted list that summarizes the key findings of the attached research paper"

"写一份要点列表，总结所附研究论文的主要发现"

Define the desired length and format of the output

定义期望的输出长度与格式

"Compose a 500-word essay discussing the impact of climate change on coastal communities."

"写一篇 500 字的文章，讨论气候变化对沿海社区的影响"

Specify the target audience

指明目标受众

"Write a product description for a new line of organic skincare products, targeting young adults concerned with sustainability."

"为一条新的有机护肤品产品线写产品描述，目标受众是关注可持续性的年轻人"

### 2. Provide Context and Background Information:

### 2. 提供上下文与背景信息：

Include relevant facts and data

纳入相关事实与数据

"Given that global temperatures have risen by 1 degree Celsius since the pre-industrial era, discuss the potential consequences for sea level rise."

"鉴于自前工业化时代以来全球气温已上升 1 摄氏度，讨论海平面上升可能带来的后果。"

Reference specific sources or documents

引用具体来源或文档

"Based on the attached financial report, analyze the company's profitability over the past five years."

"根据所附财务报告，分析该公司过去五年的盈利能力。"

Define key terms and concepts

界定关键术语与概念

"Explain the concept of quantum computing in simple terms, suitable for a non-technical audience."

"用通俗的语言解释量子计算的概念，适合非技术背景的读者。"

### 3. Use Few-Shot Prompting:

### 3. 使用少样本提示：

Provide a few examples of desired input-output pairs

提供几对期望的输入-输出示例

Input: "Cat" Output: "A small furry mammal with whiskers." Input: "Dog" Output: "A domesticated canine known for its loyalty." Prompt: "Elephant"

输入："猫" 输出："一种长着胡须、毛茸茸的小型哺乳动物。" 输入："狗" 输出："一种以忠诚著称的驯养犬科动物。" 提示词："大象"

Demonstrate the desired style or tone

展示期望的风格或语调

Example 1 (humorous): "The politician's speech was so dull, it could cure insomnia." Example 2 (formal): "The dignitary delivered an address that was both informative and engaging." Prompt: "Write a sentence describing the comedian's stand-up routine."

示例 1（幽默）："那位政客的演讲乏味得能治好失眠。" 示例 2（正式）："那位要人发表了一场既富有信息量又引人入胜的演讲。" 提示词："写一句话描述这位喜剧演员的脱口秀表演。"

Show the desired level of detail

展示期望的细节程度

Example 1 (brief): "The movie was about a young boy who befriends an alien." Example 2 (detailed): "The science fiction film follows the story of Elliot, a lonely boy who discovers and forms a unique bond with an extraterrestrial stranded on Earth." Prompt: "Summarize the plot of the novel you just finished reading."

示例 1（简略）："这部电影讲的是一个男孩和一名外星人成为朋友。" 示例 2（详细）："这部科幻片讲述了孤独男孩 Elliot 的故事，他发现了一名困在地球上的外星来客，并与它建立起独特的纽带。" 提示词："总结你刚读完的那本小说的情节。"

### 4. Be Specific:

### 4. 要具体：

Use precise language and avoid ambiguity

使用精确的语言，避免歧义

Instead of: "Write something about climate change," use: "Write a persuasive essay arguing for the implementation of stricter carbon emission regulations."

不要写："写点关于气候变化的东西"，而应写："写一篇有说服力的文章，论证应当实施更严格的碳排放法规。"

Quantify your requests whenever possible

尽可能量化你的要求

Instead of: "Write a long poem," use: "Write a sonnet with 14 lines that explores themes of love and loss."

不要写："写一首长诗"，而应写："写一首 14 行的十四行诗，探讨爱与失去的主题。"

Break down complex tasks into smaller steps

把复杂任务拆成更小的步骤

Instead of: "Create a marketing plan," use: "1. Identify the target audience. 2. Develop key marketing messages. 3. Choose appropriate marketing channels."

不要写："做一份营销计划"，而应写："1. 确定目标受众。2. 制定核心营销信息。3. 选择合适的营销渠道。"

### 5. Iterate and Experiment:

### 5. 迭代与试验：

**Action**

**动作**

Try different phrasings and keywords

尝试不同的措辞与关键词

Rephrase your prompt using synonyms or alternative sentence structures.

用同义词或不同的句式改写你的提示词。

Adjust the level of detail and specificity

调整细节程度与具体程度

Add or remove information to fine-tune the output.

增加或删减信息，以微调输出。

Test different prompt lengths

测试不同的提示词长度

Experiment with both shorter and longer prompts to find the optimal balance.

既试较短的提示词，也试较长的提示词，找到最佳平衡点。

### 6. Leverage Chain of Thought Prompting:

### 6. 借助思维链提示：

Encourage step-by-step reasoning

鼓励逐步推理

"Solve this problem step-by-step: John has 5 apples, he eats 2. How many apples does he have left? Step 1: John starts with 5 apples. Step 2: He eats 2 apples, so we need to subtract 2 from 5. Step 3: 5 - 2 = 3. Answer: John has 3 apples left."

"一步一步解这道题：John 有 5 个苹果，他吃了 2 个。他还剩几个苹果？第 1 步：John 一开始有 5 个苹果。第 2 步：他吃了 2 个苹果，所以要从 5 中减去 2。第 3 步：5 - 2 = 3。答案：John 还剩 3 个苹果。"

Ask the model to explain its reasoning process

要求模型解释其推理过程

"Explain your thought process in determining the sentiment of this movie review: 'The acting was superb, but the plot was predictable.'"

"解释你判断这条影评情感倾向的思考过程：'表演非常出色，但情节一猜就中。'"

Guide the model through a logical sequence of thought

引导模型走完一条合乎逻辑的思考序列

"To classify this email as spam or not spam, consider the following: 1. Is the sender known? 2. Does the subject line contain suspicious keywords? 3. Is the email offering something too good to be true?"

"要把这封邮件分类为垃圾邮件或非垃圾邮件，请考虑以下几点：1. 发件人是否已知？2. 主题行是否含有可疑关键词？3. 邮件是否在提供好得不像真的东西？"

For further guidance on prompt engineering best practices, explore the [Five Best Practices for Prompt Engineering](https://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineering) on Google Cloud.

关于提示工程最佳实践的更多指导，可查看 Google Cloud 上的[提示工程五大最佳实践](https://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineering)。

## Benefits of prompt engineering

## 提示工程的收益

Effective prompt engineering offers numerous benefits, enhancing the capabilities and usability of AI models:

有效的提示工程带来诸多收益，能增强 AI 模型的能力与可用性：

### Improved model performance

### 提升模型表现

Well-crafted prompts lead to more accurate, relevant, and informative outputs from AI models, as they provide clear instructions and context.

精心设计的提示词能带来更准确、更相关、信息更充分的 AI 模型输出，因为它们提供了清晰的指令与上下文。

### Reduced bias and harmful responses

### 减少偏见与有害回复

By carefully controlling the input and guiding the AI's focus, prompt engineering helps mitigate bias and minimize the risk of generating inappropriate or offensive content.

通过谨慎控制输入并引导 AI 的关注点，提示工程有助于减轻偏见，并降低生成不当或冒犯性内容的风险。

### Increased control and predictability

### 增强控制力与可预测性

Prompt engineering empowers you to influence the AI's behavior and ensure consistent and predictable responses aligned with your desired outcomes.

提示工程让你能够影响 AI 的行为，确保回复一致、可预测，并与你期望的结果相符。

### Enhanced user experience

### 改善用户体验

Clear and concise prompts make it easier for users to interact effectively with AI models, leading to more intuitive and satisfying experiences.

清晰简洁的提示词让用户更容易与 AI 模型有效互动，从而带来更直观、更令人满意的体验。

### Start your AI journey with Google Cloud

### 用 Google Cloud 开启你的 AI 之旅

New customers get $300 in free credits to spend on Google Cloud.

新客户可获得 300 美元免费赠金，用于 Google Cloud。

Get started<https://console.cloud.google.com/freetrial/?redirectPath=/vertex-ai/>

开始使用<https://console.cloud.google.com/freetrial/?redirectPath=/vertex-ai/>

Talk to a Google Cloud sales specialist to discuss your unique challenge in more detail.

与 Google Cloud 销售专员交流，更详细地讨论你面临的独特挑战。

Contact us<https://cloud.google.com/contact>

联系我们<https://cloud.google.com/contact>

#### Additional learning resources to get started

#### 更多入门学习资源

New to Google Cloud or generative AI? New customers get [$300 in free credits](https://cloud.google.com/free/docs/free-cloud-features) to run, test, and deploy workloads.

刚接触 Google Cloud 或生成式 AI？新客户可获得 [300 美元免费赠金](https://cloud.google.com/free/docs/free-cloud-features)，用于运行、测试与部署工作负载。

- [Training: No cost generative AI fundamentals course](https://www.cloudskillsboost.google/paths/118)
- [Documentation: Introduction to prompt design](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/introduction-prompt-design)
- [Documentation: General prompt design strategies](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/prompt-design-strategies)
- [Documentation: Generative AI prompt samples](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/prompt-samples)

- [培训：免费的生成式 AI 基础课程](https://www.cloudskillsboost.google/paths/118)
- [文档：提示设计入门](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/introduction-prompt-design)
- [文档：通用提示设计策略](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/prompt-design-strategies)
- [文档：生成式 AI 提示词示例](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/prompt-samples)

#### Take the next step

#### 采取下一步

Start building on Google Cloud with $300 in free credits and 20+ always free products.

用 300 美元免费赠金和 20 多款永久免费产品，开始在 Google Cloud 上构建。

Get started for free<https://console.cloud.google.com/freetrial/>

免费开始使用<https://console.cloud.google.com/freetrial/>

- Need help getting started?[Contact sales](https://cloud.google.com/contact/)
- Work with a trusted partner[Find a partner](https://cloud.google.com/find-a-partner/)
- Continue browsing[See all products](https://cloud.google.com/products/)

- 需要入门帮助？[联系销售](https://cloud.google.com/contact/)
- 与值得信赖的合作伙伴合作[寻找合作伙伴](https://cloud.google.com/find-a-partner/)
- 继续浏览[查看全部产品](https://cloud.google.com/products/)
