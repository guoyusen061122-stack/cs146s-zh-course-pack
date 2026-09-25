AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Manushree Vijayvergiya et al.
URL, we inspected its best practice document and determined (1) the best-practice type (section ) and (2) whether a linter that detects a corresponding violation exists or can be easily built. Specifically, three authors, each with over years of experience in building static analysis tools, read the documentation and independently categorized the URLs. There were no disagreements on the best- practice type, but there were disagreements on whether a linter can be easily built for about 15% of URLs. The three authors re- solved these disagreements through majority vote and discussion.
Disagreements stemmed from ambiguous best practices, and those with multiple guidelines. For example, while checking the pres- ence of code documentation is relatively straightforward, reasoning about justified exceptions and clarity of content may not.
Figure shows the distribution of the sampled URLs, broken down by type and whether violations can be detected by a linter.
For 33/50 (66%) of these best practices, violation detection is beyond the scope of traditional static analysis.
LESSONS LEARNED
BasedonourexperiencedevelopinganddeployingAutoCommenter, we summarize a few key lessons learned:
- 
Complementing traditional analyses
: AutoCommenter’s
LLM-backed approach generates comments for 68% of best practices frequently referenced by human reviewers. Many of these are out of scope for traditional static analyses.
- 
Intrinsic evaluation vs. real-world performance
: Intrin- sic evaluations and real-world performance can diverge sig- nificantly: our intrinsic evaluation, using a dataset of real- world human comments together with a state of the art model architecture and training process, indicated a promis- ing model, but our extrinsic evaluations and system improve- ments proved essential for a successful deployment.
- 
Monitoring user acceptance is critical
: Even a few nega- tive user experiences can erode trust in an automated system.
Continuously monitoring and analyzing real-world feedback was crucial in detecting such instances and identifying reme- dies. In the case of AutoCommenter, a simple suppression mechanism was sufficient to strongly improve user accep- tance to over 80% without major sacrifices in efficacy.
RELATED WORK
Johnson [ those years, a considerable body of research on automated static analysis was produced: a recent literature review by Heckman and
Williams [ developers interact with static analysis. Johnson et al
. [ explore challenges developers face when trying to use static analysis. The results of their study highlights the importance of good integration into existing developer workflows and the importance of develop- ing and maintaining trust in the tool. Vassallo et al
. [ explore how developers interact with static analysis in different contexts, including coding and code review. They too find that integration into existing workflows plays a major role in developers willing- ness to use the tools and that high quality of results is extremely important. Beller et al
. [ studied usage of static code analysis in a large number of open source projects. Among other findings, they highlight that how automated analysis is and should be used varies based on the programming language.
In contrast, using machine learning for code analysis is a compar- atively new and less understood field. A number of recent publica- tions(e.g.,Hongetal
.[
,Lietal
.[
,Lietal
.[
,Thongtanunam et al
. [
, Tufano et al
. [
, and Tufano et al
. [
) report on model evaluations and propose tools for automated code review. While these models and the review comment generation task are very sim- ilar to the model presented in this paper, evaluations largely focused on historical datasets. As discussed in section 3.3.1 an intrinsic eval- uation on only historical comments is somewhat limited and can sometimes fail to predict real-world performance. Another recent publication by Frömmgen et al
. [ presents an evaluation of a live system, but for the opposite task: creating code from comments rather than comments from code.
CONCLUSION
Verifying that code adheres to best practices is a common task in modern code review processes. While some best practices can be automatically verified with traditional tools such as linters, many require the knowledge and judgement of experienced developers, which requires time and effort.
This paper reports on our experience developing, deploying, and evaluating AutoCommenter, an LLM-backed code review assistant system. Specifically, it lays out the entire process from task and model design, over intrinsic evaluations and system calibrations, to a staged roll out and end-user evaluation.
The evaluation results show that it is feasible to develop an end-to-end system with capabilities well beyond traditional tools while achieving a high degree of end-user acceptance. These results are a promising first step towards the deployment of sophisticated code-review assistants and automated code reviews.
Our priority was to ensure a positive developer experience by designingAutoCommentertohaveveryhighprecision.Whilerecall was not the primary focus, we recognize its significance and plan to explore what changes in the model and system architecture can improve recall. For example, the model we used in was state of the art at the time. However, it has a limited context window of tokens which suffices for only around lines of code. Current state of the art models have context windows of tens of thousands of tokens during training and over a million tokens during inference.
This leap opens up opportunities for new features and significant improvement in existing ones.
ACKNOWLEDGEMENTS
This work is the result of years of collaboration between teams in
Google Core Systems and Google DeepMind. We are grateful for the support and advice of all our team members and leadership, includ- ing Alberto Elizondo, Alexander Frömmgen, Ballie Sandhu, Chandu
Thekkath, Chris Gorgolewski, David Tattersall, Ilya Cherny, Jacob
Austin, Katja Grünwedel, Kristóf Molnár, Lera Kharatyan, Luka Ri- manić, Madhura Dudhgaonkar, Marc Brockschmidt, Marcus Revaj,
Maxim Tabachnyk, Nina Chen, Niranjan Tulpule, Nitya Ramani,
Paige Bailey, Pavel Sychev, Pierre-Antoine Manzagol, Quinn Madi- son, Roger Fleig, Satish Chandra, Savinee Dancs, Stoyan Nikolov,
Subhodeep Moitra, and Vaibhav Tulsyan.

## Page 9

AI-Assisted Assessment of Coding Practices in Modern Code Review AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
REFERENCES
[1]
Google Style Guides. https://google.github.io/styleguide/. Accessed:
2024-03-15.
[2]
Linux kernel coding style. https://www.kernel.org/doc/html/v4.10/process/ coding-style.html. Accessed: 2024-03-15.
[3]
PEP – Style Guide for Python Code. https://peps.python.org/pep-0008/.
Accessed: 2024-03-15.
[4]
Rust Style Guide. https://doc.rust-lang.org/nightly/style-guide/. Accessed:
2024-03-15.
[5]
Alberto Bacchelli and Christian Bird. Expectations, outcomes, and chal- lenges of modern code review. In
35th International Conference on Software
Engineering (ICSE)
. 712–721. https://doi.org/10.1109/ICSE.2013.6606617
[6]
Moritz Beller, Radjino Bholanath, Shane McIntosh, and Andy Zaidman.
Analyzing the state of static analysis: A large-scale evaluation in open source soft- ware. In
IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering (SANER)
, Vol. IEEE, 470–481.
[7]
Zimin Chen, Małgorzata Salawa, Manushree Vijayvergiya, Goran Petrović, Marko
Ivanković, and René Just. MuRS: Mutant Ranking and Suppression using
Identifier Templates. In
Proceedings of the Symposium on the Foundations of
Software Engineering (FSE)
. 1798–1808.
[8]
M. E. Fagan. Design and code inspections to reduce errors in program development.
IBM Systems Journal
15, (1976), 182–211. https://doi.org/10.1147/ sj.153.0182
[9]
Alexander Frömmgen, Jacob Austin, Peter Choy, Nimesh Ghelani, Lera Kharatyan,
GabrielaSurita,ElenaKhrapko,PascalLamblin,Pierre-AntoineManzagol,Marcus
Revaj, Maxim Tabachnyk, Daniel Tarlow, Kevin Villela, Daniel Zheng, Satish
Chandra, and Petros Maniatis. Resolving Code Review Comments with
Machine Learning. In
International Conference on Software Engineering: Software
Engineering in Practice (ICSE-SEIP)
.
[10]
Sarah Heckman and Laurie Williams. A systematic literature review of actionable alert identification techniques for automated static code analysis.
Information and Software Technology
53, (2011), 363–387. https://doi.org/10.
1016/j.infsof.2010.12.007 Special section: Software Engineering track of the 24th
Annual Symposium on Applied Computing.
[11]
Yang Hong, Chakkrit Tantithamthavorn, Patanamon Thongtanunam, and Aldeida
Aleti. Commentfinder: a simpler, faster, more accurate code review com- ments recommendation. In
Proceedings of the Joint Meeting of the European Soft- ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE)
. 507–519.
[12]
Marko Ivanković, Goran Petrović, René Just, and Gordon Fraser. Code
Coverage at Google. In
Proceedings of the Joint Meeting of the European Soft- ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE)
. 955–963.
[13]
Marko Ivanković, Goran Petrović, Yana Kulizhskaya, Mateusz Lewko, Luka Kali- novčić, René Just, and Gordon Fraser. Productive Coverage: Improving the Actionability of Code Coverage. In
International Conference on Software
Engineering: Software Engineering in Practice (ICSE-SEIP)
.
[14]
Brittany Johnson, Yoonki Song, Emerson Murphy-Hill, and Robert Bowdidge.
Why don’t software developers use static analysis tools to find bugs?. In
35th International Conference on Software Engineering (ICSE)
. IEEE, 672–681.
[15]
Stephen C Johnson.
Lint, a C program checker
. Bell Telephone Laboratories
Murray Hill.
[16]
Lingwei Li, Li Yang, Huaxi Jiang, Jun Yan, Tiejian Luo, Zihan Hua, Geng Liang, and Chun Zuo. Auger: Automatically generating review comments with pre-training models. In
Proceedings of the Joint Meeting of the European Soft- ware Engineering Conference and the Symposium on the Foundations of Software
Engineering (ESEC/FSE)
. 1009–1021.
[17]
Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep
Majumder, Jared Green, Alexey Svyatkovskiy, Shengyu Fu, and Neel Sundaresan.
Automatingcodereviewactivitiesbylarge-scalepre-training.In
Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
(<conf-loc>, <city>Singapore</city>,
<country>Singapore</country>, </conf-loc>)
(ESEC/FSE 2022)
. Association for
Computing Machinery, New York, NY, USA, 1035–1047. https://doi.org/10.1145/
[18]
Goran Petrović, Marko Ivanković, Gordon Fraser, and René Just. Please fix this mutant: How do developers resolve mutants surfaced during code review?. In
International Conference on Software Engineering: Software Engineering in Practice
(ICSE-SEIP)
. 150–161.
[19]
Rachel Potvin and Josh Levenberg. Why Google Stores Billions of Lines of Code in a Single Repository.
Communications of the ACM (CACM)
(2016),
78–87. http://dl.acm.org/citation.cfm?id=2854146
[20]
Peter Rigby, Brendan Cleary, Frederic Painchaud, Margaret-Anne Storey, and
Daniel German. Contemporary Peer Review in Action: Lessons from Open
Source Development.
IEEE Software
29, (2012), 56–61. https://doi.org/10.1109/
MS.2012.24
[21]
Peter C. Rigby and Christian Bird. Convergent contemporary software peer review practices. In
Proceedings of the 9th Joint Meeting on Foundations of
Software Engineering
(Saint Petersburg, Russia)
(ESEC/FSE 2013)
. Association for
Computing Machinery, New York, NY, USA, 202–212. https://doi.org/10.1145/
[22]
Adam Roberts, Hyung Won Chung, Gaurav Mishra, Anselm Levskaya, James
Bradbury, Daniel Andor, Sharan Narang, Brian Lester, Colin Gaffney, Afroz
Mohiuddin, et al
.
Scaling up models and data with t5x and seqio.
Journal of Machine Learning Research
24, (2023), 1–8.
[23]
Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko, and Alberto
Bacchelli. Modern Code Review: A Case Study at Google. In
International
Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP)
.
181–190.
[24]
Patanamon Thongtanunam, Chanathip Pornprasit, and Chakkrit Tantithamtha- vorn. Autotransform: Automated code transformation to support modern code review process. In
Proceedings of the International Conference on Software
Engineering (ICSE)
. 237–248.
[25]
Rosalia Tufano, Ozren Dabić, Antonio Mastropaolo, Matteo Ciniselli, and Gabriele
Bavota. Code Review Automation: Strengths and Weaknesses of the State of the Art.
IEEE Transactions on Software Engineering (TSE)
(2024).
[26]
Rosalia Tufano, Simone Masiero, Antonio Mastropaolo, Luca Pascarella, Denys
Poshyvanyk, and Gabriele Bavota. Using pre-trained models to boost code review automation. In
Proceedings of the International Conference on Software
Engineering (ICSE)
. 2291–2302.
[27]
Carmine Vassallo, Sebastiano Panichella, Fabio Palomba, Sebastian Proksch, Har- ald C Gall, and Andy Zaidman. How developers engage with static analysis tools in different contexts.
Empirical Software Engineering
(2020), 1419–1457.
[28]
T. Winters, T. Manshreck, and H. Wright.
Software Engineering at Google:
Lessons Learned from Programming Over Time
. O’Reilly Media. https://books.
google.ch/books?id=TyIrywEACAAJ
Received 2024-04-05; accepted 2024-05-04
