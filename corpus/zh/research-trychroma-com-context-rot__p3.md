更广泛地说，我们的发现指出了上下文工程的重要性：即对模型上下文窗口的精心构建与管理。信息在模型上下文中呈现的位置与方式，会强烈影响任务表现，这使上下文工程成为优化模型表现的一个有意义的研究方向。

# 结论#

通过我们的实验，我们证明了大语言模型（LLM）并不能在输入长度变化时保持一致的表现。即便在非词汇检索或文本复述这类简单任务上，随着输入长度增长，我们也能看到表现的不均匀性不断增加。

我们的结果凸显出，需要在当前基准测试之外开展更严格的长上下文评测，同时也凸显出上下文工程的重要性。模型上下文中是否存在相关信息，并不是唯一重要的事；更重要的是这些信息如何呈现。我们证明，即便能力最强的模型也对这一点敏感，因此有效的上下文工程对可靠的表现不可或缺。

# 脚注#

[1]（2025 年 7 月 16 日）Latent List 相关见解由 Kiran Vodrahalli（Google Deepmind）补充，并做了若干澄清。

[2] 示例的原始来源：[https://arxiv.org/pdf/2410.10813](https://arxiv.org/pdf/2410.10813)

# 参考文献#

[1] Kamradt, G. (2023). Needle In A Haystack - Pressure Testing LLMs [GitHub Repository]. [Link](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

[2] Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., and Yu, D. (2025). LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. arXiv 预印本 arXiv:2410.10813. [Link](https://arxiv.org/abs/2410.10813)

[3] Gemini Team, Georgiev, P., Lei, V. I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S., et al. (2024). Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv 预印本 arXiv:2403.05530. [Link](https://arxiv.org/abs/2403.05530)

[4] OpenAI, Kumar, A., Yu, J., Hallman, J., Pokrass, M., Goucher, A., Ganesh, A., Cheng, B., McKinzie, B., Zhang, B., Koch, C., et al. (2025). Introducing GPT-4.1 in the API. [Link](https://openai.com/index/gpt-4-1/)

[5] Meta AI, (2025). The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation. [Link](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

[6] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R. A., Yoon, S., and Schütze, H. (2025). NoLiMa: Long-Context Evaluation Beyond Literal Matching. arXiv 预印本 arXiv:2502.05167. [Link](https://arxiv.org/abs/2502.05167)

[7] Fu, H. Y., Shrivastava, A., Moore, J., West, P., Tan, C., and Holtzman, A. (2025). AbsenceBench: Language Models Can't Tell What's Missing. arXiv 预印本 arXiv:2506.11440. [Link](https://arxiv.org/abs/2506.11440)

[8] Vodrahalli, K., Ontanon, S., Tripuraneni, N., Xu, K., Jain, S., Shivanna, R., Hui, J., Dikkala, N., Kazemi, M., Fatemi, B., et al. (2024). Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries. arXiv 预印本 arXiv:2409.12640. [Link](https://arxiv.org/abs/2409.12640)

[9] openai. (2025). mrcr [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/mrcr)

[10] openai. (2025). graphwalks [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/graphwalks)

[11] Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., and Zhou, D. (2023). Large Language Models Can Be Easily Distracted by Irrelevant Context. arXiv 预印本 arXiv:2302.00093. [Link](https://arxiv.org/abs/2302.00093)

[12] jamescalam. (2024). ai-arxiv2 [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/jamescalam/ai-arxiv2)

[13] Peng, B., Quesnelle, J., Fan, H., and Shippole, E. (2023). YaRN: Efficient Context Window Extension of Large Language Models. arXiv 预印本 arXiv:2309.00071. [Link](https://arxiv.org/abs/2309.00071)

[14] McInnes, L., Healy, J., and Melville, J. (2020). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv 预印本 arXiv:1802.03426. [Link](https://arxiv.org/abs/1802.03426)

[15] Campello, R. J. G. B., Moulavi, D., and Sander, J. (2013). Density-Based Clustering Based on Hierarchical Density Estimates. In Pei, J., Tseng, V. S., Cao, L., Motoda, H., and Xu, G. (Eds.), Advances in Knowledge Discovery and Data Mining（PAKDD 2013）, Lecture Notes in Computer Science, vol 7819. Springer, Berlin, Heidelberg. [Link](https://doi.org/10.1007/978-3-642-37456-2_14)

# 附录#

清理后的 LongMemEval 数据集，以及所使用的针与干扰项，可从[这里](https://drive.google.com/drive/folders/1FuOysriSotnYasJUbZJzn31SWt85_3yf)下载。

## LLM 评判器对齐：#

我们使用 LLM 评判器来评估 NIAH 与 LongMemEval 实验的输出。这些评判器通过以下流程与人类判断校准：

## 测试的模型#

由于上下文窗口或 thinking_budget 的限制，并非所有 18 个模型都出现在每个实验中。

### Anthropic#

- Claude Opus 4
- Claude Sonnet 4
- Claude Sonnet 3.7
- Claude Sonnet 3.5
- Claude Haiku 3.5

### OpenAI#

- o3
- GPT-4.1
- GPT-4.1 mini
- GPT-4.1 nano
- GPT-4o
- GPT-4 Turbo
- GPT-3.5 Turbo

### Google#

- Gemini 2.5 Pro
- Gemini 2.5 Flash
- Gemini 2.0 Flash

### Alibaba#

- Qwen3-235B-A22B
- Qwen3-32B
- Qwen3-8B

## 使用的嵌入模型#

- text-embedding-3-small
- text-embedding-3-large
- jina-embeddings-v3 (input_type='text-matching')
- voyage-3-large (input_type=None)
- all-MiniLM-L6-v2

注意：同一模型的思考模式与非思考模式分别对待

针与问题的相似度 - PG 文章针堆/PG 文章针

正如我们在针与针堆相似度结果中提到的，我们注意到这一处现象：模型的表现相比其他针与针堆组合异常地好。单看这一处，似乎高性能模型的表现是一致的。但这类模型的一致性在其他实验中并不成立。

干扰项的影响：按干扰项数量统计的表现 - arXiv 针堆/arXiv 针

干扰项的影响：按单个干扰项统计的表现 - arXiv 针堆/arXiv 针

干扰项的影响：按干扰项数量统计的表现 - PG 文章针堆/PG 文章针

干扰项的影响：按单个干扰项统计的表现 - PG 文章针堆/PG 文章针

干扰项的影响：按干扰项数量统计的表现 - PG 文章针堆/arXiv 针

干扰项的影响：按单个干扰项统计的表现 - PG 文章针堆/arXiv 针

干扰项的影响：失败分析 - arXiv 针堆/arXiv 针

干扰项的影响：失败分析 - PG 文章针堆/PG 文章针

干扰项的影响：失败分析 - PG 文章针堆/arXiv 针
