# 高级提示

读到这一步应该已经很明显：改进提示词能在不同任务上取得更好的结果。这正是提示工程的核心思路。

前面那些例子固然有趣，但在进入更高级的概念之前，我们先更正式地梳理几个概念。

主题：

- [Zero-shot Prompting](#zero-shot-prompting)
- [Few-shot Prompting](#few-shot-prompting)
- [Chain-of-Thought Prompting](#chain-of-thought-prompting)
- [Zero-shot CoT](#zero-shot-cot)
- [Self-Consistency](#self-consistency)
- [Generate Knowledge Prompting](#generated-knowledge-prompting)
- [Automatic Prompt Engineer](#automatic-prompt-engineer-ape)

---
## 零样本提示
如今的 LLM 在海量数据上训练、并经过遵循指令的调优，能够零样本完成任务。上一节我们试过几个零样本的例子。下面是我们用过的一个例子：

*提示词：*
```
Classify the text into neutral, negative, or positive. 

Text: I think the vacation is okay.
Sentiment:
```

*输出：*
```
Neutral
```

注意，在上面的提示词中我们没有给模型提供任何示例 —— 这正是零样本能力在起作用。当零样本不起作用时，建议在提示词中给出示范或示例。下面我们讨论被称为少样本提示的做法。

---
## 少样本提示

尽管大语言模型已经展现出惊人的零样本能力，但在更复杂的任务上使用零样本设置时仍显不足。为改善这一点，少样本提示被用作一种实现上下文学习的技术：我们在提示词中提供示范，引导模型取得更好的表现。这些示范为后续我们希望模型生成回答的示例提供了条件。

我们用一个来自 [Brown et al. 2020](https://arxiv.org/abs/2005.14165) 的例子来演示少样本提示。在该例中，任务是正确地在一个句子里使用一个新词。

*提示词：*
```
A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses
the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.
To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses
the word farduddle is:
```

*输出：*
```
When we won the game, we all started to farduddle in celebration.
```

可以看到，只提供一个示例（即 1-shot），模型就不知怎么学会了完成该任务。对更困难的任务，我们可以试着增加示范数量（例如 3-shot、5-shot、10-shot 等）。

按照 [Min et al. (2022)](https://arxiv.org/abs/2202.12837) 的发现，做少样本提示时关于示范/范例还有几点提示：

- 「示范所指定的标签空间与输入文本的分布都很重要（无论这些标签对各个输入是否正确）」
- 你使用的格式也对性能起关键作用；即使只用随机标签，也比完全不给标签好得多。
- 其他结果还显示，从真实的标签分布（而不是均匀分布）中随机抽取标签也有帮助。

我们来试几个例子。先试一个使用随机标签的例子（也就是说，Negative 与 Positive 这两个标签是随机分配给输入的）：

*提示词：*
```
This is awesome! // Negative
This is bad! // Positive
Wow that movie was rad! // Positive
What a horrible show! //
```

*输出：*
```
Negative
```

尽管标签被打乱了，我们仍然得到正确答案。注意我们同时保留了格式，这也有帮助。事实上，进一步实验后发现，我们试验的较新 GPT 模型对即便随机的格式也变得更加稳健。例如：

*提示词：*
```
Positive This is awesome! 
This is bad! Negative
Wow that movie was rad!
Positive
What a horrible show! --
```

*输出：*
```
Negative
```

上面的格式并不一致，但模型仍然预测出了正确标签。我们必须做更彻底的分析，才能确认这一点是否适用于其他更复杂的任务，包括提示词的各种变体。

### 少样本提示的局限

标准的少样本提示在许多任务上表现良好，但仍不是完美的技术，处理更复杂的推理任务时尤其如此。我们来演示为什么会这样。你还记得前面我们给出下面这个任务的例子吗：

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 

A: 
```

如果再试一次，模型会输出：

```
Yes, the odd numbers in this group add up to 107, which is an even number.
```

这不是正确的回答，它不仅凸显了这些系统的局限，也说明需要更高级的提示工程。

我们试着加一些示例，看看少样本提示能否改善结果。

*提示词：*
```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: The answer is False.

The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: The answer is True.

The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: The answer is True.

The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A: 
```

*输出：*
```
The answer is True.
```

没有奏效。看来对这类推理问题，少样本提示不足以获得可靠回答。上面的例子只提供了任务的基本信息。细看会发现，我们引入的任务类型还涉及更多推理步骤。换句话说，如果把问题拆解成步骤并向模型演示，可能会有帮助。更近期，[思维链（CoT）提示](https://arxiv.org/abs/2201.11903) 被推广开来，用以处理更复杂的算术、常识与符号推理任务。

总体来看，提供示例对解决某些任务是有用的。当零样本提示与少样本提示都不够用时，可能意味着模型学到的东西不足以在该任务上表现良好。此时建议开始考虑微调模型，或尝试更高级的提示技术。接下来我们讨论一种广受欢迎的提示技术 —— 思维链提示。

---

## 思维链提示

思维链提示由 [Wei et al. (2022)](https://arxiv.org/abs/2201.11903) 提出，通过中间的推理步骤实现复杂的推理能力。你可以把它与少样本提示结合，在需要先推理再作答的更复杂任务上取得更好结果。

*提示词：*
```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: Adding all the odd numbers (17, 19) gives 36. The answer is True.

The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: Adding all the odd numbers (11, 13) gives 24. The answer is True.

The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:
```

*输出：*
```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
```

很好！当我们给出推理步骤后，结果堪称完美。我们甚至可以用更少的示例来解决这个任务，也就是说，只给一个示例似乎就够了：

*提示词：*
```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:
```

*输出：*
```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
```

请记住，作者声称这是足够大的语言模型才会涌现出的能力。

---

## 零样本 CoT

近期出现的一个新想法是[零样本 CoT](https://arxiv.org/abs/2205.11916)（Kojima et al. 2022），本质上就是在原始提示词后加上「Let's think step by step」。我们来试一个简单问题，看看模型表现如何：

*提示词：*
```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?
```

*输出：*
```
11 apples
```

答案是错的！现在我们用那个特殊的提示词再试一次。

*提示词：*
```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?

Let's think step by step.
```

*输出：*
```
First, you started with 10 apples.
You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.
Then you bought 5 more apples, so now you had 11 apples.
Finally, you ate 1 apple, so you would remain with 10 apples.
```

这个简单的提示词在该任务上如此有效，令人印象深刻。当你没有太多示例可用在提示词里时，这一点尤其有用。

---

## 自洽性

提示工程中较为高级的技术之一大概是自洽性。它由 [Wang et al. (2022)](https://arxiv.org/pdf/2203.11171.pdf) 提出，目标是「取代思维链提示中所用的朴素贪心解码」。其思路是通过少样本 CoT 采样出多条不同的推理路径，再利用这些生成结果选出最一致的答案。这有助于提升 CoT 提示在涉及算术与常识推理任务上的表现。

我们来看下面这个算术推理的例子：

*提示词：*
```
When I was 6 my sister was half my age. Now
I’m 70 how old is my sister?
```

*输出：*
```
35
```

输出是错的！我们如何用自洽性改进它？来试一下。我们将使用 Wang et al. 2022（表 17）中的少样本范例：

*提示词：*
```
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done,
there will be 21 trees. How many trees did the grove workers plant today?
A: We start with 15 trees. Later we have 21 trees. The difference must be the number of trees they planted.
So, they must have planted 21 - 15 = 6 trees. The answer is 6.

Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.

Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Leah had 32 chocolates and Leah’s sister had 42. That means there were originally 32 + 42 = 74
chocolates. 35 have been eaten. So in total they still have 74 - 35 = 39 chocolates. The answer is 39.

Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops
did Jason give to Denny?
A: Jason had 20 lollipops. Since he only has 12 now, he must have given the rest to Denny. The number of
lollipops he has given to Denny must have been 20 - 12 = 8 lollipops. The answer is 8.

Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does
he have now?
A: He has 5 toys. He got 2 from mom, so after that he has 5 + 2 = 7 toys. Then he got 2 more from dad, so
in total he has 7 + 2 = 9 toys. The answer is 9.

Q: There were nine computers in the server room. Five more computers were installed each day, from
monday to thursday. How many computers are now in the server room?
A: There are 4 days from monday to thursday. 5 computers were added each day. That means in total 4 * 5 =
20 computers were added. There were 9 computers in the beginning, so now there are 9 + 20 = 29 computers.
The answer is 29.

Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many
golf balls did he have at the end of wednesday?
A: Michael initially had 58 balls. He lost 23 on Tuesday, so after that he has 58 - 23 = 35 balls. On
Wednesday he lost 2 more so now he has 35 - 2 = 33 balls. The answer is 33.

Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: She bought 5 bagels for $3 each. This means she spent 5

Q: When I was 6 my sister was half my age. Now I’m 70 how old is my sister?
A:
```

*输出 1：*
```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70 - 3 = 67. The answer is 67.
```

*输出 2：*
```
When the narrator was 6, his sister was half his age, which is 3. Now that the narrator is 70, his sister would be 70 - 3 = 67 years old. The answer is 67.
```

*输出 3：*
```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70/2 = 35. The answer is 35.
```

计算最终答案需要几个步骤（细节请看论文），但为简单起见，可以看到已经浮现出一个多数答案，它基本上就会成为最终答案。

---
## 生成知识提示

LLM 一直在持续改进，其中一个流行技术是让模型能够纳入知识或信息，从而做出更准确的预测。

沿用类似思路，能否也让模型在做出预测之前先生成知识？[Liu et al. 2022](https://arxiv.org/pdf/2110.08387.pdf) 的论文正是这样的尝试 —— 生成知识并把它作为提示词的一部分。具体来说，这对常识推理之类的任务有多大帮助？

我们来试一个简单的提示词：

*提示词：*
```
Part of golf is trying to get a higher point total than others. Yes or No?
```

*输出：*
```
Yes.
```

这类错误暴露出 LLM 在完成需要更多世界知识的任务时的局限。我们如何用知识生成来改善它？

首先，我们生成一些「知识」：

*提示词：*
```
Input: Greece is larger than mexico.
Knowledge: Greece is approximately 131,957 sq km, while Mexico is approximately 1,964,375 sq km, making Mexico 1,389% larger than Greece.

Input: Glasses always fog up.
Knowledge: Condensation occurs on eyeglass lenses when water vapor from your sweat, breath, and ambient humidity lands on a cold surface, cools, and then changes into tiny drops of liquid, forming a film that you see as fog. Your lenses will be relatively cool compared to your breath, especially when the outside air is cold.

Input: A fish is capable of thinking.
Knowledge: Fish are more intelligent than they appear. In many areas, such as memory, their cognitive powers match or exceed those of ’higher’ vertebrates including non-human primates. Fish’s long-term memories help them keep track of complex social relationships.

Input: A common effect of smoking lots of cigarettes in one’s lifetime is a higher than normal chance of getting lung cancer.
Knowledge: Those who consistently averaged less than one cigarette per day over their lifetime had nine times the risk of dying from lung cancer than never smokers. Among people who smoked between one and 10 cigarettes per day, the risk of dying from lung cancer was nearly 12 times higher than that of never smokers.

Input: A rock is the same size as a pebble.
Knowledge: A pebble is a clast of rock with a particle size of 4 to 64 millimetres based on the Udden-Wentworth scale of sedimentology. Pebbles are generally considered larger than granules (2 to 4 millimetres diameter) and smaller than cobbles (64 to 256 millimetres diameter).

Input: Part of golf is trying to get a higher point total than others.
Knowledge:
```

*知识 1：*
```
The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.
```

*知识 2：*
```
Golf is a precision club-and-ball sport in which competing players (or golfers) use many types of clubs to hit balls into a series of holes on a course using the fewest number of strokes. The goal is to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.
```

我们使用的是 [Liu et al. 2022](https://arxiv.org/pdf/2110.08387.pdf) 论文中给出的提示词。

下一步是把知识整合进来并得到预测。我把问题改写成 QA 格式，以引导答案的格式。

*提示词：*
```
Question: Part of golf is trying to get a higher point total than others. Yes or No?

Knowledge: The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.

Explain and Answer: 
```

*答案 1（置信度非常高）：*
```
No, the objective of golf is not to get a higher point total than others. Rather, the objective is to play a set of holes in the least number of strokes. The total number of strokes is used to determine the winner of the game, not the total number of points.
```


```
Question: Part of golf is trying to get a higher point total than others. Yes or No?

Knowledge: Golf is a precision club-and-ball sport in which competing players (or golfers) use many types of clubs to hit balls into a series of holes on a course using the fewest number of strokes. The goal is to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.

Explain and Answer:
```

*答案 2（置信度低得多）：*
```
Yes, part of golf is trying to get a higher point total than others. Each player tries to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.
```

这个例子出现了一些很有意思的现象。在第一个答案中模型非常自信，而在第二个答案中就没那么自信了。为便于演示，我简化了这个过程，但在得出最终答案时还有不少细节需要考虑。更多内容请看论文。

---

## 自动提示工程师（APE）

![](../img/APE.png)

[Zhou et al., (2022)](https://arxiv.org/abs/2211.01910) 提出自动提示工程师（APE），一个用于自动生成与选择指令的框架。指令生成问题被表述为自然语言合成，并当作黑盒优化问题来处理：用 LLM 生成候选解并在其中搜索。

第一步涉及一个大语言模型（作为推理模型），给它输出示范，让它为某个任务生成候选指令。这些候选解将引导搜索过程。指令用目标模型来执行，然后根据计算出的评估分数选出最合适的指令。

APE 发现了比人工设计的「Let's think step by step」提示词（Kojima et al., 2022）更好的零样本 CoT 提示词。

「Let's work this out step by step」这一提示词能引出思维链推理，并提升在 MultiArith 与 GSM8K 基准测试上的表现：

![](../img/ape-zero-shot-cot.png)

这篇论文触及了与提示工程相关的一个重要主题，即自动优化提示词的想法。虽然本指南不深入这一主题，但如果你感兴趣，这里有几篇关键论文：

- [AutoPrompt](https://arxiv.org/abs/2010.15980) —— 提出一种基于梯度引导搜索，为各类任务自动创建提示词的做法。
- [Prefix Tuning](https://arxiv.org/abs/2101.00190) —— 微调的轻量替代方案，为 NLG 任务前置一段可训练的连续前缀。
- [Prompt Tuning](https://arxiv.org/abs/2104.08691) —— 提出一种通过反向传播学习软提示词的机制。

---
[上一节（基础提示）](./prompts-basic-usage.md)

[下一节（应用）](./prompts-applications.md)
