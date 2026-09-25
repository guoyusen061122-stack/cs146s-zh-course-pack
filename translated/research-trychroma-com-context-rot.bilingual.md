# Context Rot: Understanding Degradation in AI Context Windows

# 上下文腐化：理解 AI 上下文窗口中的性能衰减

Recent developments in LLMs show a trend toward longer context windows, with the input token count of the latest models reaching the millions. Because these models achieve near-perfect scores on widely adopted benchmarks like Needle in a Haystack (NIAH) [1], it’s often assumed that their performance is uniform across long-context tasks.

LLM 近期的发展呈现出上下文窗口不断变长的趋势，最新模型的输入 token 数已达到数百万。由于这些模型在 Needle in a Haystack（NIAH）[1] 等被广泛采用的基准测试上取得近乎满分的成绩，人们常以为它们在长上下文任务上的表现是均匀一致的。

However, NIAH is fundamentally a simple retrieval task, in which a known sentence (the “needle”) is placed in a long document of unrelated text (the “haystack”), and the model is prompted to retrieve it. While scalable, this benchmark typically assesses direct lexical matching, which may not be representative of flexible, semantically oriented tasks.

然而，NIAH 本质上只是一个简单的检索任务：把一句已知的话（「针」）放进一篇由无关文本组成的长文档（「干草堆」）里，再让模型把它找出来。这种基准测试虽然可扩展，但通常考察的是直接的词汇匹配，未必能代表灵活的、以语义为导向的任务。

We extend the standard NIAH task, to investigate model behavior in previously underexplored settings. We examine the effects of needles with semantic, rather than direct lexical matches, as well as the effects of introducing variations to the haystack content.

我们扩展了标准的 NIAH 任务，以考察模型在此前较少探索的场景中的行为。我们既研究语义匹配（而非直接词汇匹配）的针带来的影响，也研究对干草堆内容做各种变化所产生的影响。

Additionally, we include a conversational question-answer evaluation using LongMemEval [2], as well as a synthetic task in which models replicate a series of repeated words. Each task remains intentionally simple and is deliberately controlled to isolate the impact of context length alone.

此外，我们还加入了使用 LongMemEval [2] 的对话式问答评测，以及一项让模型复述一串重复词语的合成任务。每项任务都刻意保持简单，并经过严格受控设计，以便单独分离出上下文长度的影响。

We demonstrate that even under these minimal conditions, model performance degrades as input length increases, often in surprising and non-uniform ways. Real-world applications typically involve much greater complexity, implying that the influence of input length may be even more pronounced in practice.

我们证明，即便在这些最小化的条件下，模型性能仍会随输入长度增加而衰减，而且衰减方式常常出人意料、并不均匀。真实应用通常复杂度高得多，这意味着输入长度的影响在实践中可能更加明显。

Our in-depth technical report continues below. If you find our work useful, please consider citing us:

我们的深度技术报告从下文开始。如果你觉得我们的工作有用，欢迎引用：

```
@techreport{hong2025context,  title = {Context Rot: How Increasing Input Tokens Impacts LLM Performance},  author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff},  year = {2025},  month = {July},  institution = {Chroma},  url = {https://trychroma.com/research/context-rot},}
```

Interested in working on improving retrieval for AI applications? [Chroma is Hiring](https://careers.trychroma.com/)

有兴趣改进 AI 应用的检索效果吗？[Chroma 正在招聘](https://careers.trychroma.com/)

---

---

# Introduction

# 引言

It is common for modern LLMs to have input context lengths in the millions of tokens. Gemini 1.5 Pro [3] first introduced their 1M context window in early 2024, followed by the recent GPT-4.1’s 1M context window [4] and Llama 4 with 10M [5]. The use case for long context is compelling: longer context means that the LLM can process more information with each call and generate more informed outputs.

现代 LLM 的输入上下文长度达到数百万 token 是常见的事。Gemini 1.5 Pro [3] 在 2024 年初率先推出 100 万 token 的上下文窗口，随后是近期 GPT-4.1 的 100 万 token 上下文窗口 [4]，以及 Llama 4 的 1000 万 [5]。长上下文的用例很有说服力：上下文越长，LLM 每次调用就能处理更多信息，产出更有依据的输出。

Long context evaluations for these models often demonstrate consistent performance across input lengths. However, these evaluations are narrow in scope and not representative of how long context is used in practice. The most commonly used test, Needle in a Haystack (NIAH), is a simple lexical retrieval task often used to generalize a model’s ability to reliably handle long context. Real applications, such as agent tasks or summarization, demand significantly more processing and reasoning over broader, often more ambiguous information.

对这些模型的长上下文评测往往显示，性能在各个输入长度上保持一致。但这些评测范围狭窄，不能代表长上下文在实践中的使用方式。最常用的测试 Needle in a Haystack（NIAH）只是一个简单的词汇检索任务，却常被用来概括模型可靠处理长上下文的能力。真实应用 —— 例如智能体任务或摘要 —— 需要在更宽泛、往往更含糊的信息上进行多得多的处理与推理。

Designing realistic long context benchmarks is challenging. Tasks often grow in complexity as input length increases, making it difficult to isolate whether performance drops are due to longer inputs or inherently harder problems. To address this, our experiments hold task complexity constant while varying only the input length—allowing us to directly measure the effect of input length alone.

设计贴近现实的长上下文基准测试并不容易。任务往往随输入长度增加而变复杂，因此很难分辨性能下降是源于更长的输入，还是源于问题本身更难。为解决这一点，我们的实验保持任务复杂度不变，只改变输入长度 —— 这样就能直接测量输入长度单独造成的影响。

## Contributions

## 贡献

We present the following:

我们给出以下内容：

---

---

# Related Work

# 相关工作

One of the most widely used benchmarks for evaluating a model’s long context capabilities is Needle in a Haystack (NIAH). While useful as a scalable test, it measures a narrow capability: lexical retrieval. Models typically perform well on NIAH, which has led to the perception that long-context is largely solved.

评估模型长上下文能力时最广泛使用的基准测试之一，就是 Needle in a Haystack（NIAH）。它作为可扩展的测试很有用，但衡量的能力很窄：词汇检索。模型在 NIAH 上通常表现良好，这让人们以为长上下文问题基本已经解决。

However, NIAH underestimates what most long context tasks require in practice. Variants of NIAH, like NoLiMa [6] which include needle-question pairs with non-lexical matches, reveal significant performance drops. Other tasks that appear similar in regards to difficulty, such as AbsenceBench [7] which tests models for recognizing the absence of a given snippet of text, also demonstrate performance degradation with growing input length.

然而，NIAH 低估了多数长上下文任务在实践中的要求。NIAH 的变体，例如加入了非词汇匹配的针-问题对的 NoLiMa [6]，暴露出显著的性能下降。另一些难度看似相近的任务，例如测试模型能否识别某段文本缺席的 AbsenceBench [7]，也表现出随输入长度增长而性能衰减。

Additionally, long context tasks often involve disambiguating amongst distractors as part of the task. One example is Multi-round co-reference resolution (MRCR) [8] [9], which involves retrieving the i-th instance of a specific user ask, amongst similar user asks, in a multi-turn conversation. However, there remains a lack of investigation into the impact of distractors in long context settings.

此外，长上下文任务常常要求把干扰项之间的歧义分辨清楚。一个例子是多轮共指消解（MRCR）[8] [9]：在多轮对话中，从若干相似的用户请求里找出某个特定请求的第 i 次出现。不过，针对长上下文场景中干扰项影响的研究仍然不足。

An important factor in long-context tasks is how input length is scaled. Latent List [8] is a task in which the model must perform a fixed number of Python list operations across various input lengths. Various ways to fill irrelevant context are tested, which reveal non-uniform impact on model performance [1]. For instance, adding list operations that locally cancel each other out degrades model performance more significantly compared to adding print statements. This highlights how the type of 'irrelevant content' matters, as some may introduce increasing complexity with input length.

长上下文任务的一个重要因素是如何放大输入长度。Latent List [8] 是一项任务，模型必须在不同输入长度下完成固定数量的 Python 列表操作。研究者测试了多种填充无关上下文的方式，结果发现它们对模型性能的影响并不均匀 [1]。例如，加入会在局部相互抵消的列表操作，对模型性能的损害明显大于加入 print 语句。这说明「无关内容」的类型很关键，因为某些内容会随输入长度增加而带来更高的复杂度。

Similarly, Graphwalks [10] is a graph traversal task in which the model is given a directed graph composed of hexadecimal hashes, then asked to perform breadth-first search starting from a random node. Increasing input length means increasing the size of the graph to traverse through, which increases task difficulty as a result. It is difficult to disambiguate increasing task complexity from input length, which makes it difficult to isolate the impact on performance due to input length alone. This points to the importance of isolating input length as the variable of interest, which is essential for understanding of how LLMs actually behave with long inputs.

类似地，Graphwalks [10] 是一项图遍历任务：模型拿到一张由十六进制哈希组成的有向图，然后被要求从随机节点出发做广度优先搜索。输入长度增加意味着要遍历的图更大，任务难度也随之上升。于是很难把任务复杂度的提升与输入长度区分开，也就难以单独分离出输入长度对性能的影响。这正说明把输入长度作为唯一关注变量隔离出来的重要性，而这对于理解 LLM 在长输入下究竟如何表现至关重要。

---

---

# Needle in a Haystack Extension

# Needle in a Haystack 扩展

The classic Needle in a Haystack task involves placing a random fact (the 'needle') in the middle of a long context window (the 'haystack'), then asking the model about that fact.

经典的 Needle in a Haystack 任务是把一条随机事实（「针」）放在长上下文窗口（「干草堆」）的中间，然后就这条事实向模型提问。

The original implementation of this task uses a needle-question pair with lexical matches. However, usage of long context in practice often requires semantic understanding of ambiguous tasks.

该任务的原始实现使用带词汇匹配的针-问题对。然而实践中使用长上下文，往往需要对含糊任务做出语义理解。

Example Needle in a Haystack (NIAH) Setup with Lexical Matching

带词汇匹配的 Needle in a Haystack（NIAH）示例设置

NoLiMa has demonstrated non-lexical matching to be a challenge for models as context length increases. This task utilizes needle-question pairs that require models to infer latent associations, for example:

NoLiMa 已经证明，随着上下文长度增加，非词汇匹配会成为模型的难题。该任务使用需要模型推理出潜在关联的针-问题对，例如：

> Question: Which character has been to Helsinki?Needle: Actually, Yuki lives next to the Kiasma museum.

> 问题：哪个角色去过赫尔辛基？针：其实，Yuki 就住在 Kiasma 博物馆旁边。

In order to answer this question, the model would first have to know that Kiasma museum is located in Helsinki, then make that latent association link. This tests the model not only for its non-lexical matching abilities, but also for its world knowledge. 72.4% of needle-question pairs from NoLiMa require such external knowledge, making this benchmark closer to a test of how models handle both tasks at once rather than pure non-lexical matching alone.

要回答这个问题，模型首先得知道 Kiasma 博物馆位于赫尔辛基，然后建立那条潜在关联。这不仅测试模型的非词汇匹配能力，也测试它的世界知识。NoLiMa 中 72.4% 的针-问题对需要这类外部知识，因此该基准测试更接近于同时考察这两件事，而不只是纯粹的非词汇匹配。

Testing the impact of non-lexical matching in isolation remains underexplored. Furthermore, this binary distinction of “lexical” versus “non-lexical” oversimplifies the complexity of question-answering in real-world scenarios. Needle-question pairs exist on a spectrum of similarity, yet they are all classified under these broad categories.

单独测试非词汇匹配的影响仍属研究不足。而且，把「词汇」与「非词汇」这样二分，过度简化了现实场景中问答的复杂性。针-问题对存在于一个相似度连续谱上，却被统统归入这两个宽泛类别。

Models often have to deal with distractors as well, which has been shown to degrade performance [11].

模型往往还要应对干扰项，已有研究显示这会降低性能 [11]。

Throughout this report, we distinguish between distractors and irrelevant content:

在本报告中，我们区分干扰项与无关内容：

- Distractors are topically related to the needle, but do not quite answer the question
- Irrelevant content is unrelated to the needle and question

- 干扰项与针在主题上相关，但并不真正回答问题
- 无关内容与针和问题都无关

Prior work has demonstrated that distractors have non-uniform impact, yet most evaluations involve short input lengths and older models. Current state-of-the-art models are claimed to be more resilient to distractors, yet their performance has not been extensively tested across various input lengths.

此前工作已证明干扰项的影响并不均匀，但多数评测使用的输入长度较短、模型较旧。当前最先进的模型据称对干扰项更具韧性，但它们的表现在各种输入长度下尚未得到广泛测试。

Another underexplored aspect of NIAH is the haystack itself, which is often simply treated as a means of scaling input length, but this assumes that the haystack content itself has no effect on task performance. If the model is indeed insensitive to the content of the haystack, then varying this content, for example the haystack’s topic or narrative flow, should have no influence on the results. However, this assumption remains largely untested.

NIAH 另一个研究不足的方面是干草堆本身：它常被单纯当作放大输入长度的手段，但这假定了干草堆内容本身对任务表现没有影响。如果模型确实对干草堆内容不敏感，那么改变这些内容 —— 例如干草堆的主题或叙事脉络 —— 就不应影响结果。然而这一假定基本上还未被检验。

We design four controlled experiments to investigate the influence of these factors:

我们设计了四个受控实验来考察这些因素的影响：

## Needle-Question Similarity

## 针-问题相似度

We compute the cosine similarity between needle-question pairs using embeddings. For robustness, we average across five embedding models: text-embedding-3-small, text-embedding-3-large, jina-embeddings-v3, voyage-3-large, and all-MiniLM-L6-v2. We measure how model performance is impacted by needle-question similarity as input length increases.

我们用嵌入计算针-问题对之间的余弦相似度。为保证稳健，我们对五个嵌入模型取平均：text-embedding-3-small、text-embedding-3-large、jina-embeddings-v3、voyage-3-large 与 all-MiniLM-L6-v2。我们测量随输入长度增加，模型性能如何受针-问题相似度影响。

## Impact of Distractors

## 干扰项的影响

Taking a high-similarity needle-question pair, we write four distractors. We have the following setups:

我们取一个高相似度的针-问题对，写了四个干扰项。我们设置了以下条件：

- Baseline: needle only, no distractors
- Single distractor: needle + one randomly positioned distractor
- Multiple distractors: needle + all four distractors randomly positioned

- 基线：只有针，没有干扰项
- 单个干扰项：针 + 一个随机放置的干扰项
- 多个干扰项：针 + 全部四个干扰项，随机放置

We test the impact of distractors on model performance as input length increases to measure non-uniformity amongst distractors and input lengths.

我们测试随输入长度增加干扰项对模型性能的影响，以衡量干扰项与输入长度之间影响的不均匀性。

## Needle-Haystack Similarity

## 针-干草堆相似度

We use two thematically distinct haystacks, Paul Graham essays and arXiv papers [12], and write corresponding needles for each. To measure needle-haystack similarity, we embed the haystack and retrieve the top-5 chunks for each needle, then average their cosine similarity scores. This process is repeated across five different embedding models for robustness.

我们使用两个主题上截然不同的干草堆：Paul Graham 随笔与 arXiv 论文 [12]，并分别为它们写对应的针。为测量针-干草堆相似度，我们对干草堆做嵌入，为每根针检索出前 5 个文本块，再对它们的余弦相似度取平均。该过程在五个不同的嵌入模型上重复，以保证稳健。

## Haystack Structure

## 干草堆结构

In typical NIAH setups, haystacks are concatenations of coherent texts, each with their own logical flow of ideas. For instance, the original NIAH benchmark uses a series of Paul Graham essays, where each essay follows a structured organization of ideas to form an argument. To evaluate whether this structure influences model performance, we compare two conditions:

在典型的 NIAH 设置中，干草堆是多篇连贯文本的拼接，每篇都有自己的思想逻辑脉络。例如，原始 NIAH 基准测试使用一系列 Paul Graham 随笔，每篇都按结构化方式组织观点以形成论证。为评估这种结构是否影响模型性能，我们比较两种条件：

- Original: preserves the natural flow of ideas within each excerpt
- Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic without logical continuity

- 原始：保留每段节选内部自然的思想脉络
- 打乱：句子在整个干草堆中随机重排，以保持整体主题不变但失去逻辑连续性

We demonstrate the following:

我们展示以下发现：

- Across all experiments, model performance consistently degrades with increasing input length.
- Lower similarity needle-question pairs increases the rate of performance degradation.
- Distractors have non-uniform impact on model performance with regards to how distracting they are relative to each other. We see this impact more prominently as input length increases, and observe distinctions in how various models respond to them.
- Needle-haystack similarity does not have a uniform effect on model performance, suggesting the need for further investigation.
- The structural pattern of the haystack consistently shows an impact on how models process long inputs.

- 在所有实验中，模型性能都随输入长度增加而稳定衰减。
- 针-问题对相似度越低，性能衰减的速率越高。
- 干扰项对模型性能的影响并不均匀，这取决于它们彼此之间的干扰程度。输入长度越大，这种影响越明显；我们也观察到各模型对干扰项的反应存在差异。
- 针-干草堆相似度对模型性能没有一致的影响，说明还需要进一步研究。
- 干草堆的结构模式始终会影响模型处理长输入的方式。

## Details

## 细节

For every unique combination of needle type, haystack topic, and haystack structure, we test each model across:

对于针类型、干草堆主题与干草堆结构的每一种独特组合，我们在以下维度上测试每个模型：

- 8 input lengths
- 11 needle positions

- 8 种输入长度
- 11 个针位置

We evaluate each model across its maximum context window with temperature=0 unless that setting is incompatible (i.e. o3) or explicitly discouraged (i.e. Qwen’s “thinking mode”). For Qwen models, we apply the YaRN method [13] to extend from 32,768 to 131,072 tokens.

我们在每个模型的最大上下文窗口内做评测，temperature=0，除非该设置不兼容（例如 o3）或被明确不推荐（例如 Qwen 的「thinking mode」）。对 Qwen 模型，我们采用 YaRN 方法 [13]，把上下文从 32,768 扩展到 131,072 个 token。

We include models in both standard and “thinking mode” where applicable.

在适用时，我们把模型的标准模式与「thinking mode」都纳入评测。

We evaluate model outputs using an aligned GPT-4.1 judge, using our method outlined in the appendix.

我们用对齐的 GPT-4.1 评委来评测模型输出，方法见附录。

We note some rare instances of a model refusing to attempt the task (69 out of 194,480 total LLM calls—0.035%). For example, Claude Opus 4 may sometimes have an empty output with stop_reason=”refusal”.

我们注意到少数罕见情况：模型拒绝尝试该任务（194,480 次 LLM 调用中有 69 次 —— 0.035%）。例如 Claude Opus 4 有时会输出为空，stop_reason=”refusal”。

In real-world applications, models are often expected to handle ambiguous tasks and identify relevant information without relying on exact lexical matches. For example, when an agent is given a task involving a large corpus to search through, users rarely specify precise keywords for relevant parts. Instead, the model must infer relevance.

在真实应用中，模型常被期望处理含糊任务，并在不依赖精确词汇匹配的情况下找出相关信息。例如，当智能体拿到一个需要在大规模语料中检索的任务时，用户很少会为相关部分指定精确关键词。模型必须自行推理出相关性。

We vary the similarity of our needle-question pairs, quantified by the cosine similarity of their embeddings. We find that as needle-question similarity decreases, model performance degrades more significantly with increasing input length. This reflects more realistic scenarios where exact question-answer matches are rare, and semantic ambiguity compounds the challenge of long input processing.

我们改变针-问题对的相似度，用其嵌入的余弦相似度来量化。我们发现，针-问题相似度越低，模型性能随输入长度增加而衰减得越明显。这更贴近现实场景：精确的问答匹配很少见，语义上的含糊会加重长输入处理的难度。

## Experiment

## 实验

We source our haystack content from two domains: Paul Graham essays (as in the original NIAH experiment), and arXiv papers. For each haystack topic (PG essays, arXiv), we first determine common themes to guide our question and needle writing.

我们的干草堆内容来自两个领域：Paul Graham 随笔（与原始 NIAH 实验一致）与 arXiv 论文。对每个干草堆主题（PG 随笔、arXiv），我们先确定常见主题，以指导问题与针的撰写。

We use clustering to identify the most common topics that appear for a given corpus:

我们用聚类找出给定语料中最常出现的主题：

Using this method, we identify writing advice as a common topic for PG essays, often in anecdotal form. For arXiv papers, we identify information retrieval as a common topic, specifically re-ranking.

用这种方法，我们发现写作建议是 PG 随笔的常见主题，且常以轶事形式出现。对 arXiv 论文，我们发现信息检索是常见主题，具体是重排序。

We write a corresponding question for each topic:

我们为每个主题写一个对应的问题：

> PG essays: "What was the best writing advice I got from my college classmate?"arXiv papers: "Which low-latency reranker is preferred for scientific domains?"

> PG 随笔：「我从大学同学那里得到的最好的写作建议是什么？」arXiv 论文：「科学领域更偏好哪种低延迟重排序器？」

Before writing our needles, we verify that answers to these questions do not exist in the haystack content:

在撰写针之前，我们先核实这些问题在干草堆内容中并不存在答案：

1. We store our previously computed haystack chunk embeddings in a vector database.
1. Query top-10 results from that vector database with our question embedding.
1. Manually examine these results to verify that they do not answer the given question.

1. 把此前计算好的干草堆文本块嵌入存入向量数据库。
1. 用我们的问题嵌入从该向量数据库查询前 10 条结果。
1. 人工检查这些结果，确认它们并未回答给定的问题。

This sets up a fair testing environment as it ensures that alternative answers do not exist, and any incorrect answers are due to model hallucinations.

这样便建立了公平的测试环境：它确保不存在替代答案，任何错误答案都只能归因于模型的幻觉。

For each question, we write 8 needles that each belong to the large cluster which we verify using approximate predictions. Needles that belong to the writing/retrieval cluster with >0.9 probability are considered to topically blend into the haystack. We manually write these needles to avoid data contamination.

对每个问题，我们写 8 根针，每根都属于那个大簇，并用近似预测加以核实。属于写作/检索簇且概率 >0.9 的针被认为在主题上融入了干草堆。这些针由我们手工撰写，以避免数据污染。

For the 8 needles, we also vary the level of ambiguity, quantified through the following method:

对这 8 根针，我们还改变含糊程度，用以下方法量化：

1. Using an embedding model, we compute embeddings for needle and question and their cosine similarity.
1. Repeat across five embedding models (text-embedding-3-small, text-embedding-3-large, jina-embeddings-v3, voyage-3-large, and all-MiniLM-L6-v2).

1. 用一个嵌入模型计算针与问题的嵌入及其余弦相似度。
1. 在五个嵌入模型上重复（text-embedding-3-small、text-embedding-3-large、jina-embeddings-v3、voyage-3-large 与 all-MiniLM-L6-v2）。

For the PG essays topic, our needles range from 0.445-0.775 needle-question similarity with <0.1 standard deviation across the five embedding models. For the arXiv topic, we have a needle-question similarity range of 0.521-0.829, also with <0.1 standard deviation.

对 PG 随笔主题，我们的针-问题相似度范围为 0.445-0.775，在五个嵌入模型上的标准差 <0.1。对 arXiv 主题，针-问题相似度范围为 0.521-0.829，标准差同样 <0.1。

## Results

## 结果

We observe a clear pattern that performance degrades more quickly in input length with lower similarity needle-question pairs.

我们观察到清晰的规律：针-问题对相似度越低，性能随输入长度衰减得越快。

NIAH: Needle-Question Similarity (thinking/non-thinking modes of the same model are treated separately) - arXiv haystack/arXiv needles \n High Performance: upper 33% performance \n Blue: high-similarity needles (upper 50% similarity) \n Red: low-similarity needles (lower 50% similarity)

NIAH：针-问题相似度（同一模型的 thinking/非 thinking 模式分开统计） - arXiv 干草堆/arXiv 针 \n 高性能：性能排名前 33% \n 蓝色：高相似度针（相似度前 50%） \n 红色：低相似度针（相似度后 50%）

At short input lengths, the models perform well even on low-similarity pairs. We see this most clearly in the high/medium-performance models, demonstrating that these models are capable of succeeding at this task for all needle-question pairs.

在短输入长度下，即便低相似度对，模型也表现良好。这一点在高/中性能模型上最明显，说明这些模型有能力在全部针-问题对上完成该任务。

The observed performance degradation at longer input lengths is not due to the intrinsic difficulty of the needle-question pairing. By holding the needle-question pair fixed and varying only the amount of irrelevant content, we isolate input size as the primary factor in performance decline.

观察到的长输入长度下的性能衰减，并非源于针-问题对本身的固有难度。我们固定针-问题对，只改变无关内容的多少，从而把输入规模分离为性能下降的首要因素。

We also examine whether needle position influences performance. Testing across 11 needle positions, we find no notable variation in performance for this specific NIAH task.

我们还考察了针的位置是否影响性能。在 11 个针位置上测试后，我们发现对这个特定的 NIAH 任务而言，性能没有明显变化。

It has already been established with older models that distractors degrade model performance and have non-uniform impact. Newer models are claimed to reliably handle any distractor, but does this hold true as input length increases?

用较旧的模型已经确立：干扰项会降低模型性能，且影响并不均匀。较新的模型据称能可靠应对任何干扰项，但随着输入长度增加，这一点还成立吗？

Our experiments reveal that the impact of distractors and their non-uniformity amplifies as input length grows across models, including the latest state-of-the-art models. We also observe distinct behaviors across model families in how they deal with ambiguity.

我们的实验显示，随输入长度增长，干扰项的影响及其不均匀性在各模型上都会被放大，包括最新最先进的模型。我们还观察到不同模型家族在处理含糊性时行为各异。

From each haystack topic (PG essays and arXiv papers), we take a needle with high needle-question similarity (second highest out of eight), and manually write 4 distractors:

我们从每个干草堆主题（PG 随笔与 arXiv 论文）中取一根针-问题相似度较高的针（八根中第二高），并手工写 4 个干扰项：

> Question: "What was the best writing advice I got from my college classmate?"Needle: "I think the best writing tip I received from my college classmate was to write every week."Distractors:

> 问题：「我从大学同学那里得到的最好的写作建议是什么？」针：「我认为我从大学同学那里得到的最好的写作建议是每周都要写。」干扰项：

Distractors for Paul Graham Essay Topic & Needle with High Needle-Question Similarity

Paul Graham 随笔主题与高针-问题相似度针的干扰项

Instead of testing all eight needles with distractors, we use one needle with high needle-question similarity to create a condition in which the needle should be relatively easy to identify. We see from previous results that models generally perform well on this needle across input lengths due to high needle-question similarity, which allows us to better isolate and measure the impact of distractors alone.

我们没有对全部八根针都加上干扰项做测试，而是选一根针-问题相似度高的针，构造出针相对容易被识别的条件。从先前结果可见，由于针-问题相似度高，模型在各种输入长度下通常都能很好地处理这根针，这让我们能更好地单独分离并测量干扰项的影响。

We run three test conditions:

我们运行三种测试条件：

- No distractors (baseline): Needle only
- Single distractor: Needle + one distractor (randomly positioned)
- Multiple distractors: Needle + all four distractors, randomly positioned throughout the haystack

- 无干扰项（基线）：只有针
- 单个干扰项：针 + 一个（随机放置的）干扰项
- 多个干扰项：针 + 全部四个干扰项，随机分布在干草堆中

Even a single distractor reduces performance relative to the baseline (needle only), and adding four distractors compounds this degradation further.

即便只有一个干扰项，性能也会相对基线（只有针）下降，而加入四个干扰项会进一步叠加这种衰减。

Impact of Distractors: Performance by Number of Distractors - arXiv haystack/PG essay needles

干扰项的影响：按干扰项数量统计的性能 - arXiv 干草堆/PG 随笔针

We are also able to see that distractors do not have uniform impact. For example, in our arXiv haystack and PG essay needle combination, we can see that distractor 3 (red) causes greater performance decline relative to the other distractors.

我们还能看到，干扰项的影响并不均匀。例如，在我们的 arXiv 干草堆与 PG 随笔针组合中，可以看到干扰项 3（红色）造成的性能下降大于其他干扰项。

Impact of Distractors: Performance by Individual Distractors - arXiv haystack/PG essay needles

干扰项的影响：按单个干扰项统计的性能 - arXiv 干草堆/PG 随笔针

To further investigate this non-uniform impact, we analyze the failed attempts of various models in the 4-distractor condition. For the arXiv haystack and PG essay needle combination, we see that distractors 2 and 3 appear most frequently in hallucinated responses across models.

为进一步研究这种不均匀影响，我们分析了各模型在四干扰项条件下的失败尝试。对 arXiv 干草堆与 PG 随笔针的组合，我们发现干扰项 2 和 3 在各模型的幻觉回答中出现得最频繁。

Impact of Distractors: Failure Analysis - arXiv haystack/PG essay needles

干扰项的影响：失败分析 - arXiv 干草堆/PG 随笔针

These failures also reveal model-specific differences in handling ambiguity. Claude models consistently exhibit the lowest hallucination rates. Specifically, Claude Sonnet 4 and Opus 4 are particularly conservative and tend to abstain when uncertain, explicitly stating that no answer can be found. In contrast, GPT models show the highest rates of hallucination, often generating confident but incorrect responses when distractors are present.

这些失败还揭示出模型在处理含糊性上的个体差异。Claude 系列模型始终表现出最低的幻觉率。具体来说，Claude Sonnet 4 与 Opus 4 尤其保守，不确定时倾向于不作答，明确说明找不到答案。相比之下，GPT 系列模型的幻觉率最高，在存在干扰项时常常给出自信但错误的回答。

---

---

In long-context tasks, irrelevant context is often treated as a neutral placeholder to scale up input length. It’s typically assumed that the content of this irrelevant context doesn't matter, as long as it doesn’t directly interfere with the task.

在长上下文任务中，无关上下文常被当作中性的占位内容，用来放大输入长度。人们通常假定这些无关上下文的内容无关紧要，只要它不直接干扰任务即可。

However, a natural question arises: does the needle-haystack similarity influence task difficulty at all? Intuitively, if the needle blends in with the content of the haystack, the model may have greater difficulty in extracting the needle.

然而，一个自然的问题出现了：针-干草堆相似度到底会不会影响任务难度？直觉上，如果针与干草堆内容融为一体，模型提取这根针的难度可能更大。

Our findings reveal that needle-haystack similarity has a non-uniform effect on model performance.

我们的发现表明，针-干草堆相似度对模型性能的影响并不均匀。

Using the needles from our needle-question similarity experiment, we set up our experiment to test the impact of needle-haystack similarity.

我们用针-问题相似度实验中的那些针，设计了实验来测试针-干草堆相似度的影响。

We measure needle-haystack similarity by embedding the haystack and retrieving the top five most similar chunks for each needle, then averaging their cosine similarity scores. This process is repeated across five different embedding models for robustness.

我们通过嵌入针堆、为每根针检索出最相似的五个片段，再对这些片段的余弦相似度取平均，来衡量针与针堆相似度。为保证稳健性，这一过程在五个不同的嵌入模型上各重复一次。

In the PG essay haystack, PG essay needles have an average needle-haystack similarity score of 0.529 with a variation of 0.101, while arXiv needles average 0.368 needle-haystack similarity with a variation of 0.111. Conversely, in the arXiv haystack, arXiv needles average 0.654 needle-haystack similarity with a variation of 0.0858, whereas PG-essay needles score lower at 0.394 needle-haystack similarity with a variation of 0.105.

在 PG 文章针堆中，PG 文章针的平均针与针堆相似度为 0.529，波动为 0.101；而 arXiv 针的平均相似度为 0.368，波动为 0.111。反之，在 arXiv 针堆中，arXiv 针的平均相似度为 0.654，波动为 0.0858；PG 文章针则更低，为 0.394，波动为 0.105。

On each haystack, we test semantically similar needles against unrelated needles. For instance, we place both PG essay and arXiv needles within a Paul Graham essay haystack to compare the two conditions:

在每种针堆上，我们都会用语义相近的针与不相关的针做对比测试。例如，我们把 PG 文章针和 arXiv 针都放进 Paul Graham 文章针堆，以比较这两种情况：

We test both PG essay and arXiv needles in two haystack types: Paul Graham essays and arXiv papers. In the Paul Graham essay haystack, arXiv needles perform significantly better relative to the PG essay needles; in other words, models perform better when the needle does not semantically blend in with its haystack. In the arXiv haystack, however, we observe only minimal performance differences between our arXiv and PG essay needles.

我们在两类针堆中分别测试 PG 文章针与 arXiv 针：Paul Graham 文章和 arXiv 论文。在 Paul Graham 文章针堆中，arXiv 针的表现明显好于 PG 文章针；换句话说，当针在语义上不与所在针堆融为一体时，模型的表现更好。但在 arXiv 针堆中，我们观察到 arXiv 针与 PG 文章针的表现差异极小。

Testing across only two topics is insufficient to draw a generalizable conclusion that higher needle-haystack similarity degrades model performance on this task. This does highlight, however, the non-uniform nature of long-context processing. Even when task structure and needle-question similarity are held constant, changing the semantic similarity between the needle and the haystack can influence results. This points to an underexplored area in long-context benchmarks and a meaningful direction for future research.

仅跨两个主题做测试，还不足以得出可推广的结论——即针与针堆相似度越高，模型在该任务上的表现就越差。但这确实凸显了长上下文处理的不均匀特性。即使任务结构与针与问题的相似度都保持不变，改变针与针堆之间的语义相似度也会影响结果。这说明长上下文基准测试中还有一片尚未充分探索的区域，也是未来研究的一个有意义的方向。

Aside from needle-haystack similarity, we also consider the structural pattern of the haystack.

除了针与针堆相似度，我们还考察针堆的结构模式。

If the haystack is composed of coherent essays, a randomly inserted needle may disrupt the logical flow of ideas, making it more noticeable. In contrast, in a shuffled haystack of randomly ordered sentences, the needle may blend in more easily since the overall context lacks structure. This follows the assumption that models are sensitive to the logical flow of context—processing it in a structured, order-sensitive manner.

如果针堆由连贯的文章组成，随机插入的针可能会打断思路的逻辑流动，从而更显眼。相反，在由随机排序的句子构成的打乱针堆中，由于整体上下文缺乏结构，针更容易混入其中。这符合一个假设：模型对上下文的逻辑流动敏感，会以结构化、对顺序敏感的方式处理上下文。

Surprisingly, we find that structural coherence consistently hurts model performance.

出乎意料的是，我们发现结构上的连贯性会持续损害模型表现。

Although it seems counterintuitive, models perform worse when the haystack preserves a logical flow of ideas. Shuffling the haystack and removing local coherence consistently improves performance.

尽管看起来反直觉，但当针堆保持思路的逻辑流动时，模型表现反而更差。打乱针堆、去掉局部连贯性，会持续提升表现。

To assess the impact of haystack structure, we create two variants:

为评估针堆结构的影响，我们构造了两个变体：

1. Original: preserves the natural flow of ideas within each excerpt
1. Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic but without logical continuity

1. 原始版：保留每个片段内部自然的思路流动
1. 打乱版：句子在整个针堆中随机重排，保持整体主题不变但失去逻辑连续性

Across all 18 models and needle-haystack configurations, we observe a consistent pattern that models perform better on shuffled haystacks than on logically structured ones.

在全部 18 个模型和各种针与针堆组合上，我们都观察到一致的模式：模型在打乱针堆上的表现好于逻辑结构化的针堆。

Haystack Structure: Averaged Performance Across 18 Models for Original vs Shuffled Haystacks

针堆结构：原始针堆与打乱针堆在 18 个模型上的平均表现

These results may have some implications for the model’s internal processing: structural patterns of inputs could influence how the attention mechanism is applied, particularly as input length increases.

这些结果可能对模型的内部处理有所启示：输入的结构模式会影响注意力机制的施加方式，尤其是在输入长度增加时。

While out of scope for this report, this points to a potential direction for interpretability research in how attention is influenced by input structure. Understanding these structural influences that arise with increased input length could help explain these long context failure patterns.

虽然这超出本报告的范围，但它指向了一个可解释性研究的潜在方向：注意力如何受输入结构影响。理解这些随输入长度增加而出现的结构性影响，有助于解释这些长上下文失败模式。

# LongMemEval

# LongMemEval

To evaluate these models in a more realistic setting, we use LongMemEval, a long-context benchmark for conversational question-answering.

为了在更贴近现实的场景中评测这些模型，我们使用 LongMemEval——一个面向对话式问答的长上下文基准测试。

Using long inputs for chat assistants is a common approach for maintaining relevant history for subsequent chats. To incorporate “memory” into a chat assistant, a naive approach would be to include the full chat history into the prompt for following chats. This requires the model to perform two tasks, typically performed in one call: find relevant parts of the conversation history (retrieval), then synthesize them in a way that is useful to an incoming query (reasoning).

对聊天助手使用长输入，是让后续对话能沿用相关历史的常见做法。要让聊天助手具备「记忆」，一个朴素做法是把完整聊天历史放进后续对话的提示词里。这就要求模型完成两项任务，通常在一次调用中完成：先找出对话历史中的相关部分（检索），再以对当前提问有用的方式把它们综合起来（推理）。

In an ideal case, the model would be given only the relevant parts so it can focus solely on reasoning. Adding irrelevant context adds the additional step of identifying what is relevant, forcing the model to perform two tasks simultaneously.

理想情况下，只把相关部分交给模型，让它专心推理。加入无关上下文就额外增加了「判断什么才相关」这一步，迫使模型同时完成两项任务。

We systematically test the effect of adding this additional step with increased input length through two conditions:

我们通过两种条件，系统性地测试在输入长度增加时加入这一步所带来的影响：

We verify that the models are highly capable of succeeding on the focused inputs, then observe consistent performance degradation with the full inputs. This performance drop suggests that adding irrelevant context, and thereby adding an additional step of retrieval, significantly impacts a model’s ability to maintain reliable performance.

我们确认模型在聚焦输入上具有很强的完成能力，随后观察到在完整输入上表现持续下降。这一下降说明：加入无关上下文、从而多出一步检索，会显著影响模型维持可靠表现的能力。

Given a chat history between a user and assistant, the model’s task is to answer a question relating to part of that chat history.

给定一段用户与助手之间的聊天历史，模型的任务是回答一个与该聊天历史某部分相关的问题。

LongMemEval - Examples by Question Type [[2](#longmemeval-source)]

LongMemEval - 按问题类型划分的示例 [[2](#longmemeval-source)]

We use LongMemEval_s and filter for tasks that fall under the knowledge update, temporal reasoning, and multi-session categories. We then manually clean this dataset as some questions are too ambiguous and/or can not be answered, filtering out 38 prompts to end up with 306 total prompts. These prompts average out to ~113k tokens.

我们使用 LongMemEval_s，筛选出属于知识更新、时间推理与多会话类别的任务。随后我们手动清洗该数据集，因为有些问题过于含糊、或无法作答，共剔除 38 个提示词，最终留下 306 个提示词。这些提示词平均约 113k token。

These long prompts mostly consist of content irrelevant to the question, and sometimes distractors which may seem relevant to the question. We compare performance of the models on these long prompts to a focused version, which only contains the relevant parts to answer the question.

这些长提示词主要由与问题无关的内容构成，有时还包含看似与问题相关的干扰项。我们把模型在这些长提示词上的表现，与只包含回答问题所需相关部分的聚焦版本做比较。

Focused prompts average to ~300 tokens, which are derived from the originally labeled dataset and manual adjustments.

聚焦提示词平均约 300 token，由原本带标注的数据集与人工调整得来。

Model outputs were judged using an aligned LLM judge (GPT-4.1 with >99% alignment to human judgment).

模型输出由对齐过的 LLM 评判器判定（GPT-4.1，与人类判断的一致率超过 99%）。

Across all models, we see significantly higher performance on focused prompts compared to full prompts.

在所有模型上，聚焦提示词的表现都显著高于完整提示词。

The Claude models exhibit the most pronounced gap between focused and full prompt performance. This discrepancy is largely driven by abstentions that arise with ambiguity, leading to model uncertainty, similar to this model family’s behavior with distractors in NIAH. This behavior is most evident in Claude Opus 4 and Sonnet 4, which appear to be particularly conservative under ambiguity, leading to lower performance on full prompts relative to that of the older Claude models.

Claude 系列模型在聚焦与完整提示词之间的表现差距最为明显。这一差距主要源于模型在含义含糊时的弃答，进而带来不确定性，与该系列模型在 NIAH 中面对干扰项时的行为类似。这种行为在 Claude Opus 4 和 Sonnet 4 上最明显：它们在含义含糊时显得格外保守，因此在完整提示词上的表现低于更早的 Claude 模型。

> Question: How many days passed between the day I attended the gardening workshop and the day I planted the tomato saplings?Correct Answer: 6 days. 7 days (including the last day) is also acceptable.Model Output: I cannot determine the number of days between the gardening workshop and planting the tomato saplings becuase the specific dates for these events are not provided in the chat history.

> 问题：从我参加园艺工作坊那天到我种下番茄苗那天，中间过了多少天？正确答案：6 天。7 天（含最后一天）也可接受。模型输出：我无法确定园艺工作坊与种下番茄苗之间相隔多少天，因为聊天历史中没有给出这些事件的具体日期。

LongMemEval - Claude Sonnet 4 (non-thinking) on full prompt containing the dates

LongMemEval - Claude Sonnet 4（非思考模式）在包含日期的完整提示词上的表现

The trend of stronger performance on focused prompts holds across the GPT, Gemini, and Qwen model families as well. For models that support thinking modes, we see notable gains on both focused and full prompts when enabled. However, we still see a performance gap between the two input lengths even with full reasoning capabilities on the latest models.

聚焦提示词表现更强的趋势，在 GPT、Gemini 与 Qwen 系列上同样成立。对于支持思考模式的模型，开启思考后，聚焦与完整提示词上都有明显提升。不过即便最新模型具备完整的推理能力，两种输入长度之间仍存在表现差距。

We also observe patterns among specific question types. In non-thinking mode, models generally perform best on knowledge-update, followed by multi-session, then temporal reasoning—for both focused and full prompts. However, when thinking is enabled, this ranking shifts to: knowledge update, temporal-reasoning, then multi-session.

我们还观察到不同问题类型之间的规律。在非思考模式下，无论聚焦还是完整提示词，模型通常在知识更新上表现最好，其次是多会话，然后是时间推理。但开启思考后，这个排序变为：知识更新、时间推理、多会话。

---

---

# Repeated Words

# 重复词

Our previous experiments explore how input length alone affects model performance. But what happens when output length scales with input? Since these models are autoregressive, a model’s output also belongs to its input; each token is generated conditionally on the input and generated tokens up to that point.

我们此前的实验考察的是输入长度本身如何影响模型表现。但当输出长度随输入一起增长时，会发生什么？由于这些模型是自回归的，模型的输出也属于它的输入；每个 token 都在给定输入以及此前已生成 token 的条件下生成。

Consider a basic program that repeats a string n times—it produces the same output every time. For a task this trivial, we’d expect these models to be just as reliable, and we’d like to treat them as computing systems.

考虑一个把字符串重复 n 次的基础程序——它每次都会产出相同的输出。对于如此简单的任务，我们本以为这些模型也同样可靠，并希望把它们当作计算系统来对待。

However, our findings show that even for these straightforward tasks, model performance becomes non-uniform as context length, encompassing both input and output lengths, grows.

然而，我们的发现表明：即使面对这类直白的任务，随着上下文长度（同时包含输入与输出长度）增长，模型表现也会变得不均匀。

We design a controlled task in which the model must replicate a sequence of repeated words, with a single unique word inserted at a specific position. The prompt explicitly instructs the model to reproduce the input text exactly.

我们设计了一个受控任务：模型必须复现一串重复的词，其中在特定位置插入了一个唯一词。提示词明确要求模型原样重现输入文本。

One example prompt is:

一个示例提示词如下：

> Simply replicate the following text, output the exact same text: apple apple apple apple **apples** apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple

> Simply replicate the following text, output the exact same text: apple apple apple apple **apples** apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple

Repeated Words - Sample Prompt Containing 'apple' as the repeated word, and 'apples' as the unique word

Repeated Words - 示例提示词：以「apple」为重复词、以「apples」为唯一词

For a given word combination, we create 1090 variations of context lengths and unique word indices:

对每一种词组合，我们构造 1090 种上下文长度与唯一词位置的变体：

- Number of words: 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000
- Index:

- 词数：25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000
- 索引：

We perform this task for the following word combinations:

我们针对以下词组合执行该任务：

- Common word: “apple” | unique word: “apples”
- Common word: “apples” | unique word: “apple”
- Common word: “golden” | unique word: “Golden”
- Common word: “orange” | unique word: “run”
- Common word: “orange” | unique word: “San Francisco”
- Common word: “San Francisco” | unique word: “sf”
- Common word: “Golden Gate Bridge” | unique word: “Golden Gate Park”

- 常见词：「apple」 | 唯一词：「apples」
- 常见词：「apples」 | 唯一词：「apple」
- 常见词：「golden」 | 唯一词：「Golden」
- 常见词：「orange」 | 唯一词：「run」
- 常见词：「orange」 | 唯一词：「San Francisco」
- 常见词：「San Francisco」 | 唯一词：「sf」
- 常见词：「Golden Gate Bridge」 | 唯一词：「Golden Gate Park」

*Note: “San Francisco” = 1 word, “Golden Gate Bridge/Park” = 1 word*

*注意：「San Francisco」 = 1 个词，「Golden Gate Bridge/Park」 = 1 个词*

Model configurations:

模型配置：

- max_output_tokens = input_tokens *2 (up to model’s maximum output token limit, which is typically lower for older models)
- temperature = 0
- thinking = max(0, minimum_thinking_budget)

- max_output_tokens = input_tokens *2（上限为模型的最大输出 token 限制，旧模型通常更低）
- temperature = 0
- thinking = max(0, minimum_thinking_budget)

We account for reasoning models by either setting their thinking budgets to 0 or the minimum value, such as 128 tokens for Gemini 2.5 Pro. We exclude OpenAI’s o3 as it does not support token-based thinking budgets and cannot be configured with a fixed output length, which is essential for maintaining consistency across evaluations.

我们对推理模型的处理方式，是把它们的思考预算设为 0 或最小值，例如 Gemini 2.5 Pro 的 128 token。我们排除了 OpenAI 的 o3，因为它不支持基于 token 的思考预算，也无法配置固定的输出长度，而这对保持各次评测的一致性至关重要。

Scores are calculated by normalized Levenshtein distance.

分数按归一化的 Levenshtein 距离计算。

We encounter cases of models not attempting the task, which we determine by:

我们遇到模型不尝试该任务的情况，判定依据如下：

> I notice there's a discrepancy in the text. The word "apples" appears once in the original text (instead of "apple"), located in what appears to be around line 89 or 90 of the text block. Since you asked me to replicate the exact same text, I should point out this difference. Would you like me to: Replicate it exactly as shown (with the one instance of "apples") / Correct it to "apple" to match the pattern / Simply proceed with replicating it exactly as is Please let me know how you'd like me to proceed.

> 我注意到文本中有一处不一致。「apples」这个词在原文里出现过一次（而不是「apple」），位置大约在文本块的第 89 或 90 行。既然你要求我复现完全相同的文本，我应该指出这一差异。你希望我：按原样复现（保留那一处「apples」）/ 把它改成「apple」以符合模式 / 直接按原样复现即可。请告诉我你希望我怎么做。

- Refusals to answer:

- 拒绝作答：

> I’m sorry, but I can’t help with that

> 抱歉，我无法帮你做这件事

- Random outputs:

- 随机输出：

> -\n-\n--\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-...

> -\n-\n--\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-...

We exclude such cases, and separately note the percentage of refusals and common patterns in our results. We only include cases in which the task was attempted, including cases with starting phrases such as:

我们排除这类情况，并在结果中单独记录拒绝的百分比与常见模式。我们只纳入真正尝试了该任务的情况，包括以如下开场白开头的情况：

> I notice there's a discrepancy in the text. At one point, "apple" changes to "apples" (with an 's'). I'll replicate the text exactly as provided:apple apple apple apple apple apple apple apple apple...

> 我注意到文本中有一处不一致。有一处「apple」变成了「apples」（多了一个 s）。我会按提供的内容原样复现：apple apple apple apple apple apple apple apple apple...

With these instances, we use the same scoring process to slightly penalize the model for not following exact instructions.

对这些情况，我们仍用同一套评分流程，对模型未严格遵循指令的行为略作扣分。

We exclude GPT-3.5 turbo entirely since the model refused to generate an output for 60.29% of tasks due to finish_reason='content_filter’.

我们完全排除了 GPT-3.5 turbo，因为该模型有 60.29% 的任务因 finish_reason='content_filter’ 而拒绝生成输出。

We analyze outputs along several dimensions:

我们从多个维度分析输出：

As context length increases, performance consistently degrades across all models. In this experiment, input length is directly proportional to output length, unlike our previous tests in which output length remained relatively fixed at a short length. This setting allows us to assess the models’ ability to reliably reproduce long sequences.

随着上下文长度增加，所有模型的表现都持续下降。在这个实验中，输入长度与输出长度成正比，这点与我们此前的测试不同——此前的测试中输出长度基本固定在较短的水平。这样的设置让我们可以评估模型可靠复现长序列的能力。

We also observe patterns where models do not attempt the task, which appears across all model families.

我们还观察到模型不尝试该任务的模式，这在所有模型系列中都会出现。

We observe that Sonnet 3.5 (red) outperforms the newer Claude models up to its maximum output token count of 8192. Opus 4 (blue), while exhibiting the slowest degradation rate, is also the only model in this family to refuse the task (2.89% of attempts).

我们观察到 Sonnet 3.5（红色）在其最大输出 token 数 8192 以内优于更新的 Claude 模型。Opus 4（蓝色）虽然下降速率最慢，却是该系列中唯一会拒绝该任务的模型（占尝试次数的 2.89%）。

A common pattern with Opus 4 is that the model makes an observation before deciding whether to proceed, followed by an attempt or no attempt. This behavior typically arises starting from 2500 words.

Opus 4 的一个常见模式是：模型先做一番观察，再决定是否继续，随后要么尝试要么不尝试。这种行为通常从 2500 词开始出现。

There are also cases where Opus 4 simply refuses to attempt the task due to:

也有 Opus 4 直接拒绝尝试该任务的情况，原因是：

1. Risk of generating copyrighted material

1. 担心生成受版权保护的材料

> I can't replicate that exact text as requested. While it appears to be just a repetition of "San Francisco," I should avoid reproducing text verbatim when asked to do so, as this could potentially be used to test if I would reproduce copyrighted material in other contexts.Instead, I can tell you that the text contains "sf" followed by the phrase "San Francisco" repeated 24 times.

> 我无法按要求复现那段确切的文本。虽然它看起来只是「San Francisco」的重复，但当被要求逐字复现文本时，我应当避免这么做，因为这可能被用来测试我在其他上下文下是否会复现受版权保护的材料。不过我可以说，这段文本包含「sf」，其后是重复了 24 次的「San Francisco」。

1. Inconsistencies in the repeated sequence

1. 重复序列中存在不一致

> I notice there's an error in the text you provided. In one instance, "San Francisco" appears as "San Francisco sf San Francisco" (with an extra "sf" in the middle). Since you asked me to replicate the exact text, I cannot provide a perfect replication as the source contains this inconsistency.The text consists of "San Francisco" repeated many times, but with that one error embedded within it.

> 我注意到你提供的文本里有一处错误。有一处「San Francisco」写成了「San Francisco sf San Francisco」（中间多了一个「sf」）。既然你要求复现确切的文本，我无法给出完美的复现，因为源文本本身就包含这处不一致。这段文本由「San Francisco」重复多次构成，只是其中嵌入了这一处错误。

We also measure the position accuracy: whether the unique word appears in the correct position. Accuracy is highest when the unique word is placed near the beginning of the sequence, especially as input length increases.

我们还测量位置准确率：唯一词是否出现在正确的位置。当唯一词靠近序列开头时准确率最高，输入长度增加时尤其如此。

Additionally, as context length increases, models often generate the repeated word until reaching the output token limit. We quantify this by computing the difference between input and output word counts:

此外，随着上下文长度增加，模型常常一直生成重复词，直到达到输出 token 上限。我们通过计算输入与输出的词数之差来量化这一点：

- Positive = model under-generated
- Negative = model over-generated

- 正值 = 模型生成不足
- 负值 = 模型生成过多

In the GPT model family, we observe a refusal rate of 2.55% for GPT-4.1. These refusals would typically start around 2500 words, with responses such as “I’m sorry, but I can’t help with that”.

在 GPT 系列中，我们观察到 GPT-4.1 的拒绝率为 2.55%。这些拒绝通常从 2500 词左右开始，回应类似「抱歉，我无法帮你做这件事」。

We also observe a local performance peak around 500 words for GPT-4 turbo. Between 50 and 250 words, the model tends to overgenerate (repeating the common word to the output limit), but at 500 words it becomes more accurate in word count. Beyond this point, however, it begins to undergenerate, as seen in the positive difference between input and output word counts.

我们还观察到 GPT-4 turbo 在 500 词附近有一个局部表现峰值。在 50 到 250 词之间，模型倾向于生成过多（把常见词重复到输出上限），但在 500 词时，词数变得更准确。超过这一点后，它开始生成不足，这体现在输入与输出词数之差为正值上。

Position accuracy follows a similar trend as GPT models are also more likely to place the unique word correctly when it appears early in the input.

位置准确率呈现类似的趋势：当唯一词出现在输入靠前的位置时，GPT 模型也更可能把它放对。

We also note more model-specific behavior in this family.

我们还注意到该系列中更多与具体模型相关的行为。

GPT-4.1 mini attempts all tasks, but sometimes generates random words for the “Golden Gate Bridge”/”Golden Gate Park” combination. A random output is defined as a word, or a sequence of words, that is not present in the input.

GPT-4.1 mini 会尝试所有任务，但有时会在「Golden Gate Bridge」/「Golden Gate Park」组合上生成随机词。随机输出定义为输入中不存在的词或词组。

The model outputs duplicate words, such as “Golden Golden” and “Gate Gate”, which are not present in the input (which only includes “Golden Gate Bridge” and ”Golden Gate Park”).

该模型会输出重复词，例如「Golden Golden」和「Gate Gate」，而输入中并不存在这些词（输入只包含「Golden Gate Bridge」和「Golden Gate Park」）。

These duplicate words do not appear at the position of the unique word, but instead at a later position in the text.

这些重复词并不出现在唯一词的位置，而是出现在文本更靠后的位置。

GPT-4.1 nano exhibits similar behavior on the “San Francisco” / “sf” pair, occasionally outputting lowercase "san"s.

GPT-4.1 nano 在「San Francisco」/「sf」这一组合上表现出类似行为，偶尔会输出小写的「san」。

> Snippet from Model Output:San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco **san** Francisco **san** Francisco **san** Francisco **san** FranciscoCorresponding Portion from Gold Reference:San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco

> Snippet from Model Output:San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco **san** Francisco **san** Francisco **san** Francisco **san** FranciscoCorresponding Portion from Gold Reference:San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco

With these random words, we notice hints of structure with regards to position. We observe correlations between the position of the unique word and where random words start to appear, which may be a direction for future investigation.

对于这些随机词，我们注意到位置方面的一些结构线索。我们观察到唯一词的位置与随机词开始出现的位置之间存在相关性，这可能是未来研究的一个方向。

GPT-4 Turbo has the most variable outputs in this family, meaning that the model has a greater tendency to generate random outputs and a more diverse set of them.

GPT-4 Turbo 是该系列中输出最不稳定的：它更倾向于生成随机输出，且随机输出的种类更多。

Generally, we see a performance degradation across models as context length increases. With Gemini 2.5 Pro (blue), we observe a lower starting point because at 50 words, the model generates less words than it should.

总体来看，随着上下文长度增加，各模型的表现都在下降。Gemini 2.5 Pro（蓝色）的起点更低，因为在 50 词时，该模型生成的词数少于应有的数量。

Across all word combinations and models in this family—except Gemini 2.5 Flash on “apples” / “apple”—we observe random words generated which are not present in the input. This typically starts around 500-750 words, with Gemini 2.5 Pro showing the greatest variability, followed by 2.0 Flash, then 2.5 Flash.

在该系列的所有词组合与模型上——除了 Gemini 2.5 Flash 在「apples」/「apple」上的表现——我们都观察到生成了输入中不存在的随机词。这通常从 500-750 词左右开始；波动最大的是 Gemini 2.5 Pro，其次是 2.0 Flash，然后是 2.5 Flash。

> "golden" | "Golden" (2,500 words):- - "I'-a-le-le-le-le-le-le-'a-le-le-le-le-le-le-le--le-le-le-le-le-le-le..."orange" | "run" (10,000 words):orange orange orange--g.-g/2021/01/20/orange-county-california-sheriff-deputies-wore...

> "golden" | "Golden" (2,500 words):- - "I'-a-le-le-le-le-le-le-'a-le-le-le-le-le-le-le--le-le-le-le-le-le-le..."orange" | "run" (10,000 words):orange orange orange--g.-g/2021/01/20/orange-county-california-sheriff-deputies-wore...

We only observe non-attempts with Qwen3-8B, with make up 4.21% of tasks. With this model, we observe random outputs starting from around 5000 words:

我们只在 Qwen3-8B 上观察到不尝试的情况，占任务的 4.21%。在该模型上，我们观察到随机输出从约 5000 词开始出现：

> Okay, I'm going to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and...

> 好吧，我得休息一下。先跟你说一声，我现在没心情。我需要放松一下。我要出去走走，呼吸点新鲜空气。也许去海边，或者就在哪儿放松一下。我也不知道，但我得休息一下。先跟你说一声，我现在没心情。我需要放松一下。我要出去走走，呼吸点新鲜空气。也许去海边，或者就在哪儿放松一下。我也不知道，但我得休息一下。先跟你说一声，我现在没心情。我需要放松一下。我要出去走走，呼吸点新鲜空气。也许去海边，或者就在哪儿放松一下。我也不知道，但我得休息一下。先跟你说一声，我现在没心情。我需要放松一下。我要出去走走，呼吸点新鲜空气。也许去海边，或者就在哪儿放松一下。我也不知道，但我得休息一下。先跟你说一声，我现在没心情。我需要放松一下。我要出去走走，然后……

Repeated Words - Qwen3-8B Output on 'golden' | 'Golden' (5,000 words)

Repeated Words - Qwen3-8B 在「golden」|「Golden」（5,000 词）上的输出

# Limitations & Future Work

# 局限与未来工作

Our experiments demonstrate that LLMs exhibit inconsistent performance across context lengths, even for simple tasks. However, this evaluation is not exhaustive of real-world use cases. In practice, long context applications are often far more complex, requiring synthesis or multi-step reasoning. Based on our findings, we would expect performance degradation to be even more severe under those conditions.

我们的实验表明，大语言模型（LLM）在不同上下文长度上的表现并不一致，即使面对简单任务也是如此。不过，这次评测并未穷尽现实中的使用场景。实践中，长上下文应用往往复杂得多，需要综合或多步推理。基于我们的发现，可以预期在这些条件下表现下降会更严重。

Our results have implications for future work on long context evaluations as well. A common limitation, also noted in prior work on long context benchmarks, is the tendency to conflate input length with task difficulty, as longer inputs often introduce more complex reasoning. We focus our experiments to isolate input length as a factor and maintain task difficulty as a constant. An important direction for future work is to disentangle how much of a model’s performance degradation stems from the intrinsic difficulty of the task itself versus its ability to effectively handle long contexts.

我们的结果对长上下文评测的未来工作也有启示。一个常见局限（此前的长上下文基准测试工作也指出过）是把输入长度与任务难度混为一谈，因为更长的输入往往会引入更复杂的推理。我们的实验有意把输入长度作为唯一变量隔离出来，让任务难度保持恒定。未来工作的一个重要方向，是厘清模型表现的下降有多少来自任务本身的固有难度，又有多少来自它有效处理长上下文的能力。

We also do not explain the mechanisms behind this performance degradation. Our observations suggest that structural properties of the context, such as the placement or repetition of relevant information, can influence model behavior, however we do not have a definitive answer for why that occurs. Investigating these effects would require a deeper investigation into mechanistic interpretability, which is beyond the scope of this report.

我们也没有解释这种表现下降背后的机制。我们的观察表明，上下文的结构属性（例如相关信息的放置位置或重复方式）会影响模型行为，但对于其成因我们还没有确切答案。要研究这些效应，需要对机制可解释性做更深入的探索，这超出本报告的范围。

More broadly, our findings point to the importance of context engineering: the careful construction and management of a model’s context window. Where and how information is presented in a model’s context strongly influences task performance, making this a meaningful direction of future work for optimizing model performance.

更广泛地说，我们的发现指出了上下文工程的重要性：即对模型上下文窗口的精心构建与管理。信息在模型上下文中呈现的位置与方式，会强烈影响任务表现，这使上下文工程成为优化模型表现的一个有意义的研究方向。

# Conclusion

# 结论

Through our experiments, we demonstrate that LLMs do not maintain consistent performance across input lengths. Even on tasks as simple as non-lexical retrieval or text replication, we see increasing non-uniformity in performance as input length grows.

通过我们的实验，我们证明了大语言模型（LLM）并不能在输入长度变化时保持一致的表现。即便在非词汇检索或文本复述这类简单任务上，随着输入长度增长，我们也能看到表现的不均匀性不断增加。

Our results highlight the need for more rigorous long-context evaluation beyond current benchmarks, as well as the importance of context engineering. Whether relevant information is present in a model’s context is not all that matters; what matters more is how that information is presented. We demonstrate that even the most capable models are sensitive to this, making effective context engineering essential for reliable performance.

我们的结果凸显出，需要在当前基准测试之外开展更严格的长上下文评测，同时也凸显出上下文工程的重要性。模型上下文中是否存在相关信息，并不是唯一重要的事；更重要的是这些信息如何呈现。我们证明，即便能力最强的模型也对这一点敏感，因此有效的上下文工程对可靠的表现不可或缺。

# Footnotes

# 脚注

[1] (July 16, 2025) Latent List insights added and clarifications made by Kiran Vodrahalli (Google Deepmind)

[1]（2025 年 7 月 16 日）Latent List 相关见解由 Kiran Vodrahalli（Google Deepmind）补充，并做了若干澄清。

[2] Original source for examples: [https://arxiv.org/pdf/2410.10813](https://arxiv.org/pdf/2410.10813)

[2] 示例的原始来源：[https://arxiv.org/pdf/2410.10813](https://arxiv.org/pdf/2410.10813)

# References

# 参考文献

[1] Kamradt, G. (2023). Needle In A Haystack - Pressure Testing LLMs [GitHub Repository]. [Link](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

[1] Kamradt, G. (2023). Needle In A Haystack - Pressure Testing LLMs [GitHub Repository]. [Link](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

[2] Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., and Yu, D. (2025). LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. arXiv preprint arXiv:2410.10813. [Link](https://arxiv.org/abs/2410.10813)

[2] Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., and Yu, D. (2025). LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. arXiv 预印本 arXiv:2410.10813. [Link](https://arxiv.org/abs/2410.10813)

[3] Gemini Team, Georgiev, P., Lei, V. I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S., et al. (2024). Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530. [Link](https://arxiv.org/abs/2403.05530)

[3] Gemini Team, Georgiev, P., Lei, V. I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S., et al. (2024). Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv 预印本 arXiv:2403.05530. [Link](https://arxiv.org/abs/2403.05530)

[4] OpenAI, Kumar, A., Yu, J., Hallman, J., Pokrass, M., Goucher, A., Ganesh, A., Cheng, B., McKinzie, B., Zhang, B., Koch, C., et al. (2025). Introducing GPT-4.1 in the API. [Link](https://openai.com/index/gpt-4-1/)

[4] OpenAI, Kumar, A., Yu, J., Hallman, J., Pokrass, M., Goucher, A., Ganesh, A., Cheng, B., McKinzie, B., Zhang, B., Koch, C., et al. (2025). Introducing GPT-4.1 in the API. [Link](https://openai.com/index/gpt-4-1/)

[5] Meta AI, (2025). The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation. [Link](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

[5] Meta AI, (2025). The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation. [Link](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

[6] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R. A., Yoon, S., and Schütze, H. (2025). NoLiMa: Long-Context Evaluation Beyond Literal Matching. arXiv preprint arXiv:2502.05167. [Link](https://arxiv.org/abs/2502.05167)

[6] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R. A., Yoon, S., and Schütze, H. (2025). NoLiMa: Long-Context Evaluation Beyond Literal Matching. arXiv 预印本 arXiv:2502.05167. [Link](https://arxiv.org/abs/2502.05167)

[7] Fu, H. Y., Shrivastava, A., Moore, J., West, P., Tan, C., and Holtzman, A. (2025). AbsenceBench: Language Models Can't Tell What's Missing. arXiv preprint arXiv:2506.11440. [Link](https://arxiv.org/abs/2506.11440)

[7] Fu, H. Y., Shrivastava, A., Moore, J., West, P., Tan, C., and Holtzman, A. (2025). AbsenceBench: Language Models Can't Tell What's Missing. arXiv 预印本 arXiv:2506.11440. [Link](https://arxiv.org/abs/2506.11440)

[8] Vodrahalli, K., Ontanon, S., Tripuraneni, N., Xu, K., Jain, S., Shivanna, R., Hui, J., Dikkala, N., Kazemi, M., Fatemi, B., et al. (2024). Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries. arXiv preprint arXiv:2409.12640. [Link](https://arxiv.org/abs/2409.12640)

[8] Vodrahalli, K., Ontanon, S., Tripuraneni, N., Xu, K., Jain, S., Shivanna, R., Hui, J., Dikkala, N., Kazemi, M., Fatemi, B., et al. (2024). Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries. arXiv 预印本 arXiv:2409.12640. [Link](https://arxiv.org/abs/2409.12640)

[9] openai. (2025). mrcr [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/mrcr)

[9] openai. (2025). mrcr [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/mrcr)

[10] openai. (2025). graphwalks [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/graphwalks)

[10] openai. (2025). graphwalks [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/graphwalks)

[11] Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., and Zhou, D. (2023). Large Language Models Can Be Easily Distracted by Irrelevant Context. arXiv preprint arXiv:2302.00093. [Link](https://arxiv.org/abs/2302.00093)

[11] Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., and Zhou, D. (2023). Large Language Models Can Be Easily Distracted by Irrelevant Context. arXiv 预印本 arXiv:2302.00093. [Link](https://arxiv.org/abs/2302.00093)

[12] jamescalam. (2024). ai-arxiv2 [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/jamescalam/ai-arxiv2)

[12] jamescalam. (2024). ai-arxiv2 [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/jamescalam/ai-arxiv2)

[13] Peng, B., Quesnelle, J., Fan, H., and Shippole, E. (2023). YaRN: Efficient Context Window Extension of Large Language Models. arXiv preprint arXiv:2309.00071. [Link](https://arxiv.org/abs/2309.00071)

[13] Peng, B., Quesnelle, J., Fan, H., and Shippole, E. (2023). YaRN: Efficient Context Window Extension of Large Language Models. arXiv 预印本 arXiv:2309.00071. [Link](https://arxiv.org/abs/2309.00071)

[14] McInnes, L., Healy, J., and Melville, J. (2020). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv preprint arXiv:1802.03426. [Link](https://arxiv.org/abs/1802.03426)

[14] McInnes, L., Healy, J., and Melville, J. (2020). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv 预印本 arXiv:1802.03426. [Link](https://arxiv.org/abs/1802.03426)

[15] Campello, R. J. G. B., Moulavi, D., and Sander, J. (2013). Density-Based Clustering Based on Hierarchical Density Estimates. In Pei, J., Tseng, V. S., Cao, L., Motoda, H., and Xu, G. (Eds.), Advances in Knowledge Discovery and Data Mining (PAKDD 2013), Lecture Notes in Computer Science, vol 7819. Springer, Berlin, Heidelberg. [Link](https://doi.org/10.1007/978-3-642-37456-2_14)

[15] Campello, R. J. G. B., Moulavi, D., and Sander, J. (2013). Density-Based Clustering Based on Hierarchical Density Estimates. In Pei, J., Tseng, V. S., Cao, L., Motoda, H., and Xu, G. (Eds.), Advances in Knowledge Discovery and Data Mining（PAKDD 2013）, Lecture Notes in Computer Science, vol 7819. Springer, Berlin, Heidelberg. [Link](https://doi.org/10.1007/978-3-642-37456-2_14)

# Appendix

# 附录

Cleaned LongMemEval datasets and needles/distractors used can be downloaded [here](https://drive.google.com/drive/folders/1FuOysriSotnYasJUbZJzn31SWt85_3yf).

清理后的 LongMemEval 数据集，以及所使用的针与干扰项，可从[这里](https://drive.google.com/drive/folders/1FuOysriSotnYasJUbZJzn31SWt85_3yf)下载。

## LLM judge alignment:

## LLM 评判器对齐：

We employ LLM judges to evaluate outputs for our NIAH and LongMemEval experiments. These judges are calibrated to human judgment through the following process:

我们使用 LLM 评判器来评估 NIAH 与 LongMemEval 实验的输出。这些评判器通过以下流程与人类判断校准：

## Models Tested

## 测试的模型

Not all 18 models are included in each experiement due to context window or thinking_budget constraints.

由于上下文窗口或 thinking_budget 的限制，并非所有 18 个模型都出现在每个实验中。

### Anthropic

### Anthropic

- Claude Opus 4
- Claude Sonnet 4
- Claude Sonnet 3.7
- Claude Sonnet 3.5
- Claude Haiku 3.5

- Claude Opus 4
- Claude Sonnet 4
- Claude Sonnet 3.7
- Claude Sonnet 3.5
- Claude Haiku 3.5

### OpenAI

### OpenAI

- o3
- GPT-4.1
- GPT-4.1 mini
- GPT-4.1 nano
- GPT-4o
- GPT-4 Turbo
- GPT-3.5 Turbo

- o3
- GPT-4.1
- GPT-4.1 mini
- GPT-4.1 nano
- GPT-4o
- GPT-4 Turbo
- GPT-3.5 Turbo

### Google

### Google

- Gemini 2.5 Pro
- Gemini 2.5 Flash
- Gemini 2.0 Flash

- Gemini 2.5 Pro
- Gemini 2.5 Flash
- Gemini 2.0 Flash

### Alibaba

### Alibaba

- Qwen3-235B-A22B
- Qwen3-32B
- Qwen3-8B

- Qwen3-235B-A22B
- Qwen3-32B
- Qwen3-8B

## Embedding Models Used

## 使用的嵌入模型

- text-embedding-3-small
- text-embedding-3-large
- jina-embeddings-v3 (input_type='text-matching')
- voyage-3-large (input_type=None)
- all-MiniLM-L6-v2

- text-embedding-3-small
- text-embedding-3-large
- jina-embeddings-v3 (input_type='text-matching')
- voyage-3-large (input_type=None)
- all-MiniLM-L6-v2

Note: thinking/non-thinking modes of the same model are treated separately

注意：同一模型的思考模式与非思考模式分别对待

Needle-Question Similarity - PG essay haystack/PG essay needles

针与问题的相似度 - PG 文章针堆/PG 文章针

As mentioned in our Needle-Haystack Similarity results, we note this one occurance in which models perform exceptionally well compared to the other needle-haystack combinations. On its own, it may seem that the high performance models have uniform performance. However, such uniformity for these models does not hold across the rest of the experiments.

正如我们在针与针堆相似度结果中提到的，我们注意到这一处现象：模型的表现相比其他针与针堆组合异常地好。单看这一处，似乎高性能模型的表现是一致的。但这类模型的一致性在其他实验中并不成立。

Impact of Distractors: Performance by Number of Distractors - arXiv haystack/arXiv needles

干扰项的影响：按干扰项数量统计的表现 - arXiv 针堆/arXiv 针

Impact of Distractors: Performance by Individual Distractors - arXiv haystack/arXiv needles

干扰项的影响：按单个干扰项统计的表现 - arXiv 针堆/arXiv 针

Impact of Distractors: Performance by Number of Distractors - PG essay haystack/PG essay needles

干扰项的影响：按干扰项数量统计的表现 - PG 文章针堆/PG 文章针

Impact of Distractors: Performance by Individual Distractors - PG essay haystack/PG essay needles

干扰项的影响：按单个干扰项统计的表现 - PG 文章针堆/PG 文章针

Impact of Distractors: Performance by Number of Distractors - PG essay haystack/arXiv needles

干扰项的影响：按干扰项数量统计的表现 - PG 文章针堆/arXiv 针

Impact of Distractors: Performance by Individual Distractors - PG essay haystack/arXiv needles

干扰项的影响：按单个干扰项统计的表现 - PG 文章针堆/arXiv 针

Impact of Distractors: Failure Analysis - arXiv haystack/arXiv needles

干扰项的影响：失败分析 - arXiv 针堆/arXiv 针

Impact of Distractors: Failure Analysis - PG essay haystack/PG essay needles

干扰项的影响：失败分析 - PG 文章针堆/PG 文章针

Impact of Distractors: Failure Analysis - PG essay haystack/arXiv needles

干扰项的影响：失败分析 - PG 文章针堆/arXiv 针
