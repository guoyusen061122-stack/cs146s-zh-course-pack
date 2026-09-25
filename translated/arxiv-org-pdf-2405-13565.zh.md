# 现代代码评审中编码实践的 AI 辅助评估

## Page 2

AIware ’24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
Manushree Vijayvergiya 等
除了评审（并了解）代码贡献及其影响之外。
诸如 linter 这样的静态分析工具 [ 会确保代码遵循某些最佳实践（例如格式规则），有些工具甚至能自动修复违规。然而，带有细微差别或存在例外的指南很难被完整地自动验证（例如命名规范，以及遗留代码中有正当理由的偏离），还有一些指南根本无法用精确规则来表达（例如代码注释的清晰度与具体性）
并且依赖人的判断与开发者的集体知识。
因此，通常期望由人类评审者检查代码改动是否违反最佳实践。
代码评审流程最大的成本是所需的时间，尤其是资深开发者投入的时间。即便已有大量自动化，且流程尽可能轻量，一名开发者每天也很容易在这项任务上花掉几个小时 []。
机器学习近来的进展，尤其是大语言模型（LLM）的能力，表明 LLM 适合用于代码评审自动化（例如 [
,
,
,
–
]）。然而，围绕规模化部署端到端系统所面临的软件工程挑战仍未被探索。同样，关于这类系统在整体效果与用户接受度上的外部评测也仍然缺失。
本文研究是否可能部分自动化代码评审流程，特别是最佳实践违规的检测，从而为代码作者提供及时反馈，并让评审者专注于整体功能。
具体而言，本文报告我们在 Google 的工业环境中开发、部署并评测 AutoCommenter（一个自动化代码评审助手）的经验；目前每天有数以万计的开发者在使用它。
概括而言，本文的贡献包括：
- 
一个基于 LLM 的代码评审助手系统的总体架构（第 节）。
- 
工具校准以及向数以万计开发者部署的说明（第 节）。
- 
对系统的评测（第 节）。
- 
经验教训的总结与讨论（第 节）。BACKGROUND AutoCommenter 是在大型工业环境中开发的
BACKGROUND
AutoCommenter 是在大型工业环境中开发的
Google 的现代代码评审实践与其他工业项目和开源项目类似 []。
代码评审流程
Google 的代码评审流程成熟完备，以改动为单位，并有工具辅助。Ivanković 等
。[ 以及 Petrović 等
。
[ 对该流程做了详细总结。对代码库的每一处改动都必须至少由另一位开发者评审。每天有数以万计的改动走完评审流程，数以万计的开发者以代码作者和评审者的双重身份参与其中。
作者与评审者通过代码评审系统交换评论，一次评审会经历改动所涉及文件的一个个快照。每条评审评论都附着在某个文件快照中特定的行列范围上。要解决一条评论，作者通常会在本地副本中修改文件
图 1：由人类评审者发表的示例评论。
并导出新的快照，进入下一轮代码评审。
当作者与所有评审者都满意、且没有自动化分析阻止合并时，代码就会被合并进代码库。
代码评审流程中最昂贵的部分，是代码作者与评审者「护送」一次改动所花的时间（从最初编码，到回应评审者评论、确保所有自动化分析通过，直到最终把改动合并进代码库）。尽管该流程已通过自动化系统在评审前分析代码而得到优化（尤其是无需人工介入的自动代码格式化），代码评审每年仍要耗费数千开发者年。因此，哪怕只节省个位数百分比的成本，也会带来可观的业务影响。
最佳实践
最佳实践是指某种被认为更优的编程语言具体用法，而最佳实践文档会说明它应如何应用、能带来什么收益。
最佳实践 URL 指一份最佳实践文档或其中特定的一节，最佳实践违规指某段不遵循最佳实践、但可以改到遵循的代码。如果从上文可以看清，我们会用
URL 和违规来分别指代最佳实践
URL 和最佳实践违规。
Google 的中心代码仓库包含多种语言的代码，其中 C++、Java、Python 和 Go 各自都超过百万行 [
]。针对不同语言，都有所有开发者可随时查阅的正式风格指南。其中许多语言还配有额外的语言入门材料、核心库文档，以及「每周提示」式的通讯。这类材料虽不像风格指南那样被严格强制，却常在代码评审中被引用。有些语言的这类文档多达数百页。代码作者与评审者都被期望核实代码遵循了所有最佳实践。
十多年前引入的一项正式机制叫「readability」，它确保最佳实践被一致地遵循。
某种语言上专门的风格专家被称为「readability 导师」，他们引导经验不足的开发者逐步精通该语言 [
]。readability 导师通常用几句话概括一条最佳实践，并在评论末尾附上 URL，供改动作者参考。图中给出了由 readability 导师发表的一条示例评论。

## Page 3

现代代码评审中编码实践的 AI 辅助评估 AIware ’24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
图 2：模型训练流水线的架构。
readability 流程有一些缺点。对作者来说，额外的评审轮次增加了开发时间。对 readability 导师来说，这可能变成单调而耗时的任务。它要求掌握数百条不断演进的最佳实践，包括识别并废弃过时规则，以及把它们（连同相关链接）记录到代码评审系统中。此外，它还需要跟踪——有时要经过多轮迭代——确保所有违规都已被修正。
APPROACH
针对 节与 节所述的挑战，我们开发了 AutoCommenter：一个自动检测最佳实践违规的代码分析工具。它旨在为代码作者提供及时反馈，并减少人工做最佳实践评审的需要，从而让评审者专注于代码功能。
模型与任务定义
自动化最佳实践分析需要一个能表示源代码、定位违规位置并识别所违反最佳实践的模型。我们采用基于 T5 的传统 transformer 方案做文本到文本的转换，并使用 T5X []。
最佳实践分析是多任务大序列模型中的一项任务。除了 T5 的标准预训练任务——跨度去噪（预测被掩码的 token）——之外，用于训练该模型的其他任务还包括代码评审评论消解、下一次编辑预测、变量重命名和构建错误修复 [
]。训练语料由超过十亿个样本组成，其中最佳实践分析数据集贡献了约 80 万个样本。模型使用这类模型标准的交叉熵损失训练，并以最大化序列准确率指标为目标进行调优，即为每个样本预测出完全正确的目标文本。
对最佳实践分析而言，模型的输入是任务提示词与源代码，目标是源代码位置以及一条指向最佳实践违规的 URL。任务提示词被格式化为固定文本的代码注释，使用该编程语言合适的注释风格。它用自然语言描述任务，并置于源代码之前，而源代码是某个文件的直接文本表示。如果输入超出模型的上下文窗口，就会被截断。位置是源代码中的字节偏移，URL 指向被违反的最佳实践。目标格式由一套领域特定语言定义；一个特例是「空」目标，即不存在违规。除了目标，模型还会输出一个置信度分数，范围从 到
来看下面这个 Go 语言的输入/目标示例。
Input
/ / [
∗
/ / Package addition provides Add package addition
/ / Return a sum func
Add( value , value int
)
int
{ return value + value
}
Target
INSERT COMMENT https :
/ / go . dev / doc / comment# func
输入的第一行是固定文本的任务提示词；其余部分是源代码。目标给出了位置（字节偏移对应
Add 函数的起点）以及一个 go.dev 的
URL，它指向 Go 语言风格指南中被该函数注释违反的确切部分（在本例中，是注释应以函数名开头的惯例）。注意，目标可能包含零个、一个或多个（拼接的）位置-URL 对，取决于源代码中违规的数量。
模型训练
图中给出了模型训练流水线的架构，它由三部分组成。我们把数据集创建拆成两步（预处理与整理），因为第一步要处理的数据量大得多，成本也显著更高。预处理步骤的输出与模型的输入/目标表示无关。这种拆分提升了功能迭代速度，使我们可以快速迭代样本表示以及其他样本层面的调整。预处理步骤使用容错调度系统，并定期抽取相关代码评论，以确保新数据随时可用。
3.2.1 大规模预处理。
训练样本来自真实的代码评审数据，但并非所有代码评论都适合用于模型训练。因此，预处理步骤会识别出相关代码评论
——由人撰写、且包含指向最佳实践文档的 URL 的评论。对每条评论，预处理步骤随后收集对应的源代码与相关元数据，包括该评论在源代码中的位置及其创建时间。这一步的输出是一组相关代码评论，每条都带有整理模型训练样本所需的全部数据。

## Page 4

AIware ’24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
Manushree Vijayvergiya 等
3.2.2 数据集整理。
数据集整理是单个按需执行的处理步骤，以 Beam 流水线实现。它依据 节所述的输入/目标格式，把每条相关代码评论转换成标准的 TensorFlow
Example 数据结构。
3.2.3 训练与微调。
整理好的样本直接用于模型训练与评测。我们使用 T5X 框架 [ 步，并用 Tensorboard 监控训练。
模型选择
在历史数据上的两次内在评测，为我们选择模型检查点、置信度阈值和解码策略提供了依据。
第一，在验证集与测试集上的评测给出按文件计的精确率与召回率估计。第二，在完整历史代码评审上的评测给出每次代码评审的评论总数估计，从而反映开发者与 AutoCommenter 交互的频率。
3.3.1 在验证集与测试集上的评测。
我们按时间切分数据集，以确保模型没有在验证集与测试集中那些代码评论的未来代码评审快照上训练过。在我们的数据集中，85% 的文件恰好有一条相关代码评论，11% 有两条，4% 有三条或更多。
如果预测的代码位置与 URL 与期望值匹配，我们就认为该预测正确，不考虑顺序。
回顾一下，模型会为每个预测给出置信度分数，这引入了另一个参数：如果某个预测的置信度分数低于某个阈值，就可以将其抑制

。我们定义

表示置信度分数高于某个阈值的正确预测数量，除以
置信度分数高于同一个阈值的全部预测数量

；我们定义

类似地。这些定义让我们可以估计有多少（不）正确的结果会展示给用户，作为

。

和

会用于训练期间的模型检查点比较。
虽然这种评测避免了数据泄漏，也让我们能自动评测模型表现，但它有一个局限：虽然可以合理假设某份代码评审快照上的人类评论是正确的，但这些评论并不完整。换句话说，某份代码评审快照中的代码可能依据多条最佳实践都有改进空间，而人类评审者并没有为所有这些最佳实践都发表（带 URL 的）评论。
出现这种情况可能有几个原因：
- 
缺少引用
：评审者可能对某个问题发表了评论，但没有附上 URL 作为参考。
- 
选择性评论
：评审者可能只对某个问题评论一次，期望作者在整体上应用同样的修复。
- 
专长或关注点不同
：评审者可能并不熟悉所有最佳实践，或者在某次代码评审中只是选择不对某个问题发表评论（例如只关注改动的代码）。
虽然我们数据集中的大多数文件只有一条相关评论，但基于人工检查「不正确」预测的零散证据表明，由于上述原因，通常可能存在多条最佳实践评论。鉴于我们的标准答案数据并不完整，我们的精确率与召回率指标是有噪声的。
https://beam.apache.org/
因此，我们采用下一节所述的一种补充评测，以提高对模型整体表现的信心。
3.3.2 在完整历史代码评审上的评测。
为了准确估计线上环境中的评论量，我们在
AutoCommenter 上评测一组历史代码评审，使用特定的模型检查点与阈值。预测出的评论不会追溯性地发布到代码评审系统中，而是记录到数据库里以供分析。这使我们能够估计预期的发布频率——既可按文件粒度，也可按每次代码评审的粒度。
由于开发者会针对一整组需要代码评审的代码改动与 AutoCommenter 交互，这一步评测是上线生产之前的重要环节。额外的好处是，这一步还能带来进一步的优化，并评估不同用户群体、不同编程语言等的发布频率。
推理基础设施
AutoCommenter 的核心是一个中心化的最佳实践分析服务。该服务接收一个或多个源文件作为分析输入。
对每个文件，它构造模型输入（第 节），将其编码为标准的 TensorFlow
Example 数据结构，并查询模型。模型本身由一个模型服务提供，该服务使用
TensorFlow 的
Example 数据结构作为与领域无关的输入输出格式。最后，最佳实践分析服务执行一系列过滤步骤（第 节），抑制低质量预测，并返回其余预测。
IDE 与代码评审集成
开发者通过两种方式与 AutoCommenter 的分析服务交互——直接使用 IDE 插件，或间接经由代码评审系统。Google 的所有开发者都在使用代码评审系统，几乎所有开发者都在使用该 IDE。
AutoCommenter 的评论在 IDE 中显示为诊断信息，用蓝色波浪下划线标出，覆盖相关的代码片段。把鼠标悬停在下划线的代码上，会显示完整评论以及该最佳实践的简要概括，其中包括指向相关最佳实践文档的可点击链接。这些内嵌信息免去了开发者为不熟悉的最佳实践在 IDE 与浏览器之间来回切换的需要，从而简化了工作流。由于 IDE 中的评论需要实时生成，我们的目标是把生成评论的延迟控制在亚秒级。
在代码评审系统中，AutoCommenter 在每次更新后运行（即针对每个新的代码评审快照），一旦检测到违规就自动发布评论。自动化工具产生的评论在视觉上与人类发布的评论相似，但背景颜色不同。
图中给出了由
AutoCommenter 在代码评审系统中生成并发布的一条示例评论。注意右侧的点赞与点踩按钮，作者与评审者如果觉得某条评论特别有用或没用，就可以点击它们。还要注意左侧的「Please fix」按钮，它对评审者可见。如果点击它，系统会生成一条新评论，表明该评审者认为这条评论很重要，必须在代码合并进代码库之前处理。这些反馈按钮是代码评审系统的标准配置，出现在自动化工具生成的所有评论上（例如 [
,
]），并为工具的用户接受度提供了信号。IDE 也提供类似的反馈机制。

## Page 5

现代代码评审中编码实践的 AI 辅助评估 AIware ’24，2024 年 7 月 15–16 日，巴西 Porto de Galinhas
图 3：由 AutoCommenter 发表的示例评论。
DEPLOYMENT
我们在 2023 年 7 月至 10 月期间，分阶段把 AutoCommenter 部署给 Google 的所有开发者：
- 
直到 2022 年 7 月——teamfooding
：本文的作者。
- 
2022 年 7 月——早期采用者
：约千名志愿者。
- 
2023 年 7 月——A/B 实验
：约一半的开发者。
- 
自 2023 年 10 月起——正式可用
：所有开发者。
请注意，出于工业保密原因，我们无法披露代码评审、开发者、文件、评论的绝对数量，也无法披露代码评审时长的分布。在适当的情况下，我们报告相对指标与相关趋势。
我们持续评测并改进
AutoCommenter 的表现，采用迭代式改进方法：
- 
在历史数据上的评测（第 节），以获得模型在该任务上表现如何的方向性认识，并据此定义阈值、选择解码策略。
- 
监控并分析用户交互，以及通过反馈按钮和 issue 报告得到的直接反馈。
- 
基于其他评测步骤中观察到的模式，做有针对性的人工评估。
图中给出了随时间的推移，已发布的代码评审评论与 IDE 诊断上开发者正面反馈与负面反馈的比例。虚线表示开发者每月提供的反馈点击数。正如预期，在早期采用者阶段这个数字低得多。此外，由于我们在这一阶段持续改进 AutoCommenter，波动也更大。
回顾代码评审系统中的三个反馈按钮
（图 ），它们让开发者可以对已发布的评论表达正面或负面情绪。我们把获得点赞或「Please fix」的评论视为正面，把获得点踩的评论视为负面；我们把有用率定义为正面评论占所有有反馈评论的比例。
本节余下部分描述我们在部署期间做出的具体观察与相应改进。
选择阈值与解码策略
4.1.1 阈值。
在初始部署期间，我们想谨慎地管理开发者对 AutoCommenter 的信任，因此从一个较高的置信度阈值开始，即

=
.
. 我们人工抽样了
图 4：部署期间的开发者反馈。
数百条结果，并观察到阈值以下约 80% 的预测其实仍然是正确的 —— 也就是说，假阴性率非常高，达到

=
.
. 此外，我们观察到 Python 中的预测呈现出明显不同的置信度分数分布，并且受阈值化方式的影响不成比例。我们推测，训练数据集的构成
（不同 URL 的数量与 URL 频次）以及最佳实践文档的具体程度是原因所在，但把更深入的调查留作未来工作。尝试按语言分别设置阈值被证明无效，因为每种语言仍然只有一个阈值，无法充分体现模型正确预测数百条各异最佳实践的能力。这导致预测出的
URL 缺乏多样性，因为模型往往对某些 URL 给出更高的分数，而不管预测是否正确。这些观察带来了对 AutoCommenter 的第一项重大改动：按 URL 设置阈值，阈
值基于在验证数据集上的内在评测计算得出。
4.1.2 解码。
在完整历史代码评审上使用按 URL 阈值配合贪心解码的评测显示，Auto-
Commenter 能检测出所有已更改文件中 6% 的违规。然而，
80% 的评论会落在作者并未修改的代码行上。开发者通常不会对未改动的代码采取行动。因此，AutoCommenter 会过滤掉针对未改动代码行生成的评论，把已更改文件中的评论比例降到 1.3%。为了提高这一比例，我们试验了不同的解码策略：贪心（默认）、束搜索、top-k 和 top-p 采样。我们最终选定束搜索
（生成

= 个候选回复），它把发布频率提高到原来的三倍，达到 3.9%。它还带来了明显更高的 URL 多
样性：发布最频繁的 URL 占全部评论的 41%，而贪心搜索时这一比例是 80%。
在为部署选择解码策略时，延迟是另一个重要方面。虽然束搜索提高了发布频率和多样性，但推理明显变慢（中
位延迟为秒级）。考虑到这种延迟对 IDE 中的交互式使用来说过于高，我们最终决定在代码评审系统中使用束搜索，在 IDE 中使用贪心搜索。

## Page 6

AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Manushree Vijayvergiya et al.
抑制过时的最佳实践
在把 AutoCommenter 发布给约千名自愿参与的早期采用者之后，我们注意到用户几天内就提交了大量 issue。其中许多都指向同一个
URL
，它描述的是与 Python 导入相关的最佳实践。
然而，某些类型名的规范来源在 Python 3.9 中已经改变，而该最佳实践也在 early 发生了改变。由于我们的训练数据覆盖 2022 年之前，其中包含了许多已不再适用的最佳实践评论。我们意识到这是一个反复出现的模式：随着语言演进，或者引入新的库，最佳实践也会变化。缓解这个问题的一种办法是过滤掉这类数据（每当规则变化时），并重新训练模型。但这既耗时又耗资源：它需要完整地重新生成数据、重新训练模型、评测并上线。与此同时，「过时」的模型要么必须关掉，造成系统停机，要么必须抑制受影响的预测。否则，系统可能很快失去开发者的信任。我们选择抑制特定的最佳实践预测，使用条件过滤（对源代码做正则表达式匹配），原因有两个。第一，它可以动态部署并立即生效。第二，它允许对预测做细粒度过滤。
对选定评论的独立评分
在早期使用几个月后，我们观察到有用比例在约 54% 处停滞。为了理解原因、找出改进方向并为更大范围部署做准备，我们在 2023 年 4 月开展了一项独立的人工评分研究，分析了在早期采用者部署阶段收到开发者反馈的约若干条已发布评论的样本。
为了收集关于评论有用性的多元视角，我们招募了评分者 —— 来自合作团队的开发者。我们请他们对收到明确用户反馈的 AutoCommenter 评论打分。我们没有向评分者展示原始的用户反馈，以避免影响他们的判断。评分者根据所引用的最佳实践和周边代码来评估每条评论的有用性。我们要求他们关注评论的正确性，同时也要关注这条评论作为作者是否可操作
（例如，他们是否会去解决一条技术上正确但在具体场景下似乎不值得解决的评论）。我们鼓励他们对每条评论给出自由形式的反馈。
评分者评测得出的有用比例是 60%，略高于同批评论上开发者反馈给出的 54%，但远低于我们为更大范围部署设定的 80% 目标。
这项研究最有趣的发现是，无用评论存在明显的模式。以下是几个例子：
主题过多或主题复杂：
例如，某个 URL 指向一节内容，其中描述了与 Python linter 交互的多条准则，包括它经常触发的情形以及抑制它的方法。作者可能很难理解一条已发布评论具体指哪条准则，以及该如何解决。
类似地，关于在
C++ 中编写良好函数文档的指引是整整一页密集的文字。评分者经常指出，最佳实践（以及 AutoCommenter 的简明摘要）
与实际代码之间存在脱节，即使代码确实包含了相关违规。
https://github.com/google/styleguide/blob/gh-pages/pyguide.md#22-imports
高质量摘要的重要性：
评分者常常发现，AutoCommenter 的摘要（通过抓取文档源生成，有时还会缺失）没能充分说明所引用的准则与评论/代码之间的关联。
主观且可能引起争议的主题：
一个例子是避免在库代码中使用 flag。在库里使用 flag 可能引发问题，但有些库本身就是设计成通过 flag 提供大量可配置功能的。此外，遗留代码可能并不遵循这条准则，评审者也不会强制执行。
模型没有学到这些细微差别，有时会在作者给已有库新增一个 flag 时就预测违规。
某些准则上的系统性模型错误：
一个有趣的例子是某条准则提倡在 C++ vector 上优先使用成员函数 push_back 而不是 emplace_back，因为当两个函数可以用相同参数达到同样效果时应当如此。
模型已经学会预测这一点，但它也会在 emplace_back 确实更合适的情况下做出预测，甚至在某个不相关的类型恰好有一个名为 push_back 的成员函数时也做出预测
。
正确但价值很低的评论：
代码注释中句末缺少句号，人类评审者通常是容忍的。虽然技术上正确，但要求作者回到 IDE 去修正这个问题，净价值可能是负的。
评分者研究带来的洞察促成了 Auto-
Commenter 的两项改动。第一，评分者研究识别出了不可操作的 URL，抑制这些 URL 后，历史有用比例在
开发者反馈上从 54% 提升到 66%，在评分者反馈上从 60% 提升到 74%。
我们进一步分析了与类似但未被评分的 URL 关联的评论，又抑制了额外一批。第二，我们复查并手工更新了所有高频发布 URL 的摘要。这些改动加在一起，足以让我们达到下一阶段部署所需的 80% 有用比例目标。
A/B 实验
2023 年 7 月，我们在一次 A/B 实验的框架下，把 AutoCommenter 部署给了约一半的开发者。我们随机把开发者分配到实验组（启用 AutoCommenter）
和对照组（禁用 AutoCommenter）。我们依据开发者邮箱地址的 SHA256 哈希的最后几位进行随机分配，并验证了两组在规模和构成上没有差异，包括任职年限、职级、编程语言和业务部门的分布。我们还确认，实验开始前，实验期间要测量的变量在对照组和实验组之间没有差异。实验期间的评论发布频率符合预期（见 section ）。
我们没有检测到以下任何指标发生统计上显著的变化：代码评审的总时长、开发者主动投入代码评审的时间、作者与评审者之间评论-回复的轮次数。不过，我们确实检测到编码速度略有提升。我们推测，转向文档的上下文切换减少带来了这一正面效果。更深入的调查留作未来工作。
基于这些结果，我们得出结论：不存在不利影响，并于 10 月把 AutoCommenter 部署给了全部开发者。

## Page 7

AI-Assisted Assessment of Coding Practices in Modern Code Review AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
图 5：生产中 AutoCommenter 生成的自动评论与训练数据中人类评论的每 URL 评论数累积分布。
评测
基于 2023 年 3 月以来收集的有用比例和用户反馈，我们得出结论：开发者总体上对 AutoCommenter 生成的评论是满意的。我们通过分析用户反馈，持续改进数据集准备、阈值、URL 抑制和摘要，以确保 AutoCommenter 对开发者工作流产生高度的正面影响。
除了开发者满意度之外，在面向全 Google 广泛发布几个月后，我们还评测了
AutoCommenter 表现的另外三个方面：
（1）
评论解决情况：
开发者多久会修改自己的代码来解决 AutoCommenter 发布的评论？
（2）
AutoCommenter 与人类评论：
AutoCommenter 的评论在多大程度上覆盖了人类评审者在评论中引用的最佳实践文档？
（3）
AutoCommenter 与 linter：
Auto-
Commenter 的产出在多大程度上超出了传统静态分析工具的能力？
评论解决情况
开发者很少通过点击代码评审系统和 IDE 中的赞/踩按钮，以及代码评审系统中的「Please fix」按钮，对 AutoCommenter 的评论给出明确反馈（见图 ）：代码评审系统中约 10% 的自动评论、IDE 中 2% 的诊断收到了明
确反馈，这与 Google 其他自动化分析的情况相当。与此同时，开发者会悬停在约 50% 的 AutoCommenter IDE 诊断上，而先前的工作表明，开发者经常在没有明确反馈的情况下就解决了自动评论 [
]。为了评估开发者多久会解决 AutoCom-
menter 的评论，我们做了一项离线分析，估计由后续代码改动解决掉的评论比例。
为了分析评论解决情况，我们提取了聚焦于带有 AutoCommenter 自动评论的文件的历史改动。
对每一次改动，我们提取了评论被发布时的初始快照，以及开发者最终合并进代码库的快照。每条评论覆盖特定的行范围。我们使用一种基于 AST 的自动化行映射方法 [ 对这些快照进行处理，以识别出模型最初
图 6：预测频率最高的前 50 个 URL 按类型分类。Linter 表示是否存在能够检测违规的 linter，或者能否较容易地构建一个。
在第一个快照上预测出、但在合并后的快照上不再预测的评论。这类快照对表明，某条评论可能已被解决，但也存在另一种可能：不相关的代码改动导致某条评论不再被预测。
对快照对的自动分析显示，在
50% 的情况下，评论在提交的快照中已不出现在它最初发布的行上。我们人工抽查了此类快照对的随机样本。我们发现，在 80% 的情况下，作者所做的改动直接解决了已发布评论所描述的问题。因此，我们估计评论解决率约为 40%，这显著高于有明确正面反馈的评论占全部评论的比例。
AutoCommenter 与人类评论
图 比较了生产中 AutoCommenter 生成的自动评论与训练数据中人类评论的每 URL 评论数（针对最佳实践文档的每个唯一 URL）累积分布。横轴是 URL 的排名，即把自动评论中曾用过的所有 URL 按频次排序后的名次。例如，最常使用的 URL 排名第 1，它占全部自动评论的 9.9%。同一个 URL 出现在训练数据中人类创建的评论的 4.3% 里。总体而言，AutoCommenter 已经为若干
个不同 URL 生成过评论。AutoCommenter 使用的 URL 集合覆盖了带有最佳实践 URL 的历史人类评论的 68%。这是个好结果：它表明 AutoCommenter 并没有专注于评审者极少引用的冷门最佳实践。
另一方面，尽管使用了束搜索，URL 多样性仍然相对较低。前 85 个 URL 构成了 AutoCommenter 创建评论的 90%。同一组 URL 覆盖了带有最佳实践 URL 的人类评论的 35%。在保持准确率和低延迟的同时，提高自动评论中 URL 的多样性和最佳实践的覆盖面，是我们的首要任务之一。
AutoCommenter 与 linter
为了理解 AutoCommenter 在多大程度上提供了超越 linter 的价值（linter 能高效且精确地检查部分最佳实践），我们抽样了预测频率最高的前 50 个违规 —— 即图 中的前 50 个 URL。对每个抽样到的

## Page 8

AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Manushree Vijayvergiya et al.
URL，我们查阅了其最佳实践文档，并确定了（1）最佳实践的类型（见 section ），以及（2）是否存在能够检测相应违规的 linter，或者是否能较容易地构建这样一个 linter。具体来说，三位作者各自拥有超过数年的静态分析工具构建经验，他们阅读了这些文档，并独立地对这些 URL 进行了分类。在最佳实践类型上没有出现分歧，但对于约 15% 的 URL，在「能否较容易地为它构建一个 linter」这一点上存在分歧。三位作者通过多数投票和讨论解决了这些分歧。
分歧源于最佳实践本身含义含糊，以及那些包含多条准则的最佳实践。例如，检查代码文档是否存在相对直接，但要判断例外情况是否正当、内容是否清晰，可能就没那么容易了。
图 中展示了抽样 URL 的分布情况，按类型以及违规能否被 linter 检测进行细分。
在这 50 条最佳实践中有 33 条（66%），其违规检测超出了传统静态分析的范围。
经验教训
基于我们开发和部署 AutoCommenter 的经验，我们总结出几条关键教训：

- 
补充传统分析
：AutoCommenter 的
基于大语言模型的方法为人类评审者频繁引用的 68% 的最佳实践生成了评论。其中许多都超出了传统静态分析的范围。
- 
内在评测与实际表现
：内在评测与实际表现可能相差
很大：我们的内在评测使用了一个由真实人类评论构成的数据集，并采用了当时最先进的模型架构和训练流程，结果显示模型很有前景，但我们的外在评测以及系统层面的改进，对成功部署而言是不可或缺的。
- 
监控用户接受度至关重要
：哪怕只有少数几次负面
用户体验，也会侵蚀人们对自动化系统的信任。
持续监控并分析真实反馈，对于发现这类情况并找出补救办法至关重要。就 AutoCommenter 而言，一个简单的抑制机制就足以将用户接受度大幅提升到 80% 以上，而效果上的损失并不大。
相关工作
Johnson [ 在那些年里，围绕自动化静态分析产生了相当多的研究：Heckman 和
Williams [ 最近的一篇文献综述探讨了开发者如何与静态分析交互。Johnson 等人
. [ 探究了开发者在使用静态分析时面临的挑战。他们的研究结果凸显了良好地集成到既有开发者工作流中的重要性，以及建立并维持对工具信任的重要性。Vassallo 等人
. [ 探究了开发者在不同上下文下（包括编码和代码评审）如何与静态分析交互。他们也发现，集成到既有工作流中对开发者是否愿意使用这些工具有很大影响，而结果的高质量极为重要。Beller 等人
. [ 研究了静态代码分析在大量开源项目中的使用情况。除其他发现外，他们指出自动化分析应当如何使用、以及实际如何使用，会因编程语言的不同而不同。
相比之下，用机器学习做代码分析是一个相对较新、理解也较少的领域。近期有不少论
文（例如 Hong 等人
.[
，Li 等人
.[
，Li 等人
.[
，Thongtanunam 等人
. [
，Tufano 等人
. [
，以及 Tufano 等人
. [
）报告了模型评测结果，并提出了用于自动化代码评审的工具。尽管这些模型与评审评论生成任务和本文提出的模型非常相似，但其评测大多集中于历史数据集。正如 3.3.1 节所讨论的，仅基于历史评论做内在评测有一定局限，有时无法预测实际表现。Frömmgen 等人
. [ 的另一篇近期论文给出了一个线上系统的评测，但任务恰好相反：从评论生成代码，而不是从代码生成评论。
结论
验证代码是否符合最佳实践，是现代代码评审流程中的常见任务。有些最佳实践可以用 linter 之类的传统工具自动验证，但许多最佳实践需要经验丰富的开发者凭知识和判断来处理，这既费时又费力。
本文报告了我们开发、部署和评测 AutoCommenter 的经验，这是一个由大语言模型支撑的代码评审助手系统。具体来说，它完整呈现了从任务与模型设计、到内在评测与系统校准、再到分阶段上线与最终用户评测的全过程。
评测结果表明，构建一个能力远超传统工具的端到端系统是可行的，同时还能取得很高的最终用户接受度。这些结果是迈向部署复杂代码评审助手和自动化代码评审的、令人鼓舞的第一步。
我们的首要目标是确保良好的开发者体验，为此我们在设计 AutoCommenter 时让它具备极高的精确率。虽然召回率不是主要关注点，但我们认可它的重要性，并计划探索模型与系统架构上可以做哪些改动来提升召回率。例如，我们当时使用的模型在当时是最先进的。然而它的上下文窗口有限，只有若干 token，仅够处理大约若干行代码。当前最先进的模型在训练时上下文窗口可达数万 token，在推理时超过一百万 token。
这一跃升为新增功能以及现有功能的大幅改进打开了空间。
致谢
本工作是 Google Core Systems 与 Google DeepMind 两个团队多年协作的成果。我们感谢全体团队成员和领导层的支持与建议，包括 Alberto Elizondo、Alexander Frömmgen、Ballie Sandhu、Chandu
Thekkath、Chris Gorgolewski、David Tattersall、Ilya Cherny、Jacob
Austin、Katja Grünwedel、Kristóf Molnár、Lera Kharatyan、Luka Ri-
manić、Madhura Dudhgaonkar、Marc Brockschmidt、Marcus Revaj、
Maxim Tabachnyk、Nina Chen、Niranjan Tulpule、Nitya Ramani、
Paige Bailey、Pavel Sychev、Pierre-Antoine Manzagol、Quinn Madi-
son、Roger Fleig、Satish Chandra、Savinee Dancs、Stoyan Nikolov、
Subhodeep Moitra，以及 Vaibhav Tulsyan。

## Page 9

AI-Assisted Assessment of Coding Practices in Modern Code Review AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
参考文献
[1]
Google Style Guides。https://google.github.io/styleguide/。访问日期：
2024-03-15。
[2]
Linux kernel coding style。https://www.kernel.org/doc/html/v4.10/process/ coding-style.html。访问日期：2024-03-15。
[3]
PEP – Style Guide for Python Code。https://peps.python.org/pep-0008/。
访问日期：2024-03-15。
[4]
Rust Style Guide。https://doc.rust-lang.org/nightly/style-guide/。访问日期：
2024-03-15。
[5]
Alberto Bacchelli 与 Christian Bird。《Expectations, outcomes, and chal-
lenges of modern code review》。载于
35th International Conference on Software
Engineering (ICSE)
。712–721。https://doi.org/10.1109/ICSE.2013.6606617
[6]
Moritz Beller、Radjino Bholanath、Shane McIntosh 与 Andy Zaidman。
《Analyzing the state of static analysis: A large-scale evaluation in open source soft-
ware》。载于
IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering (SANER)
，卷 IEEE，470–481。
[7]
Zimin Chen、Małgorzata Salawa、Manushree Vijayvergiya、Goran Petrović、Marko
Ivanković 与 René Just。《MuRS: Mutant Ranking and Suppression using
Identifier Templates》。载于
Proceedings of the Symposium on the Foundations of
Software Engineering (FSE)
。1798–1808。
[8]
M. E. Fagan。《Design and code inspections to reduce errors in program development》。
IBM Systems Journal
15，（1976），182–211。https://doi.org/10.1147/ sj.153.0182
[9]
Alexander Frömmgen、Jacob Austin、Peter Choy、Nimesh Ghelani、Lera Kharatyan、
GabrielaSurita、ElenaKhrapko、PascalLamblin、Pierre-AntoineManzagol、Marcus
Revaj、Maxim Tabachnyk、Daniel Tarlow、Kevin Villela、Daniel Zheng、Satish
Chandra 与 Petros Maniatis。《Resolving Code Review Comments with
Machine Learning》。载于
International Conference on Software Engineering: Software
Engineering in Practice (ICSE-SEIP)
。
[10]
Sarah Heckman 与 Laurie Williams。《A systematic literature review of actionable alert identification techniques for automated static code analysis》。
Information and Software Technology
53，（2011），363–387。https://doi.org/10.
1016/j.infsof.2010.12.007 专题栏目：第 24 届
Annual Symposium on Applied Computing 的软件工程方向。
[11]
Yang Hong、Chakkrit Tantithamthavorn、Patanamon Thongtanunam 与 Aldeida
Aleti。《Commentfinder: a simpler, faster, more accurate code review com-
ments recommendation》。载于
Proceedings of the Joint Meeting of the European Soft-
ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE)
。507–519。
[12]
Marko Ivanković、Goran Petrović、René Just 与 Gordon Fraser。《Code
Coverage at Google》。载于
Proceedings of the Joint Meeting of the European Soft-
ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE)
。955–963。
[13]
Marko Ivanković、Goran Petrović、Yana Kulizhskaya、Mateusz Lewko、Luka Kali-
novčić、René Just 与 Gordon Fraser。《Productive Coverage: Improving the Actionability of Code Coverage》。载于
International Conference on Software
Engineering: Software Engineering in Practice (ICSE-SEIP)
。
[14]
Brittany Johnson、Yoonki Song、Emerson Murphy-Hill 与 Robert Bowdidge。
《Why don’t software developers use static analysis tools to find bugs?》。载于
35th International Conference on Software Engineering (ICSE)
。IEEE，672–681。
[15]
Stephen C Johnson。
《Lint, a C program checker》
。Bell Telephone Laboratories
Murray Hill。
[16]
Lingwei Li、Li Yang、Huaxi Jiang、Jun Yan、Tiejian Luo、Zihan Hua、Geng Liang 与 Chun Zuo。《Auger: Automatically generating review comments with pre-training models》。载于
Proceedings of the Joint Meeting of the European Soft-
ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE)
。1009–1021。
[17]
Zhiyu Li、Shuai Lu、Daya Guo、Nan Duan、Shailesh Jannu、Grant Jenks、Deep
Majumder、Jared Green、Alexey Svyatkovskiy、Shengyu Fu 与 Neel Sundaresan。
《Automatingcodereviewactivitiesbylarge-scalepre-training》。载于
Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
（<conf-loc>、<city>Singapore</city>、
<country>Singapore</country>、</conf-loc>）
（ESEC/FSE 2022）
。Association for
Computing Machinery，New York, NY, USA，1035–1047。https://doi.org/10.1145/
[18]
Goran Petrović、Marko Ivanković、Gordon Fraser 与 René Just。《Please fix this mutant: How do developers resolve mutants surfaced during code review?》。载于
International Conference on Software Engineering: Software Engineering in Practice
(ICSE-SEIP)
。150–161。
[19]
Rachel Potvin 与 Josh Levenberg。《Why Google Stores Billions of Lines of Code in a Single Repository》。
Communications of the ACM (CACM)
（2016），
78–87。http://dl.acm.org/citation.cfm?id=2854146
[20]
Peter Rigby、Brendan Cleary、Frederic Painchaud、Margaret-Anne Storey 与
Daniel German。《Contemporary Peer Review in Action: Lessons from Open
Source Development》。
IEEE Software
29，（2012），56–61。https://doi.org/10.1109/
MS.2012.24
[21]
Peter C. Rigby 与 Christian Bird。《Convergent contemporary software peer review practices》。载于
Proceedings of the 9th Joint Meeting on Foundations of
Software Engineering
（Saint Petersburg, Russia）
（ESEC/FSE 2013）
。Association for
Computing Machinery，New York, NY, USA，202–212。https://doi.org/10.1145/
[22]
Adam Roberts、Hyung Won Chung、Gaurav Mishra、Anselm Levskaya、James
Bradbury、Daniel Andor、Sharan Narang、Brian Lester、Colin Gaffney、Afroz
Mohiuddin 等
。
《Scaling up models and data with t5x and seqio》。
Journal of Machine Learning Research
24，（2023），1–8。
[23]
Caitlin Sadowski、Emma Söderberg、Luke Church、Michal Sipko 与 Alberto
Bacchelli。《Modern Code Review: A Case Study at Google》。载于
International
Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)
。
181–190。
[24]
Patanamon Thongtanunam、Chanathip Pornprasit 与 Chakkrit Tantithamtha-
vorn。《Autotransform: Automated code transformation to support modern code review process》。载于
Proceedings of the International Conference on Software
Engineering (ICSE)
。237–248。
[25]
Rosalia Tufano、Ozren Dabić、Antonio Mastropaolo、Matteo Ciniselli 与 Gabriele
Bavota。《Code Review Automation: Strengths and Weaknesses of the State of the Art》。
IEEE Transactions on Software Engineering (TSE)
（2024）。
[26]
Rosalia Tufano、Simone Masiero、Antonio Mastropaolo、Luca Pascarella、Denys
Poshyvanyk 与 Gabriele Bavota。《Using pre-trained models to boost code review automation》。载于
Proceedings of the International Conference on Software
Engineering (ICSE)
。2291–2302。
[27]
Carmine Vassallo、Sebastiano Panichella、Fabio Palomba、Sebastian Proksch、Har-
ald C Gall 与 Andy Zaidman。《How developers engage with static analysis tools in different contexts》。
Empirical Software Engineering
（2020），1419–1457。
[28]
T. Winters、T. Manshreck 与 H. Wright。
《Software Engineering at Google:
Lessons Learned from Programming Over Time》
。O’Reilly Media。https://books.
google.ch/books?id=TyIrywEACAAJ
收稿 2024-04-05；录用 2024-05-04
