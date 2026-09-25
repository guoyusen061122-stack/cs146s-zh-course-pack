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
