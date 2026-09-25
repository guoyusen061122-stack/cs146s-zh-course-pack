# Code Reviews: Just Do It

# 代码评审：尽管去做

In [Humanizing Peer Reviews](https://web.archive.org/web/20060315135514/http://www.processimpact.com/articles/humanizing_reviews.html), Karl Wiegers starts with a powerful pronouncement:

在 [Humanizing Peer Reviews](https://web.archive.org/web/20060315135514/http://www.processimpact.com/articles/humanizing_reviews.html) 一文中， Karl Wiegers 开篇就给出了一句有力的论断：

> Peer review – an activity in which people other than the author of a software deliverable examine it for defects and improvement opportunities – is one of the most powerful software quality tools available. Peer review methods include inspections, walkthroughs, peer desk checks, and other similar activities. After experiencing the benefits of peer reviews for nearly fifteen years, I would never work in a team that did not perform them.

> 同行评审 —— 一种由软件交付物作者之外的人检查该交付物、寻找缺陷与改进机会的活动 —— 是现有最强大的软件质量工具之一。同行评审的方法包括审查、走查、同行桌面检查以及其他类似活动。在体验了同行评审的好处近十五年之后，我绝不会在一支不开展同行评审的团队里工作。

After participating in code reviews for a while here at Vertigo, I believe that **peer code reviews are the single biggest thing you can do to improve your code.** If you’re not doing code reviews *right now* with another developer, you’re missing a lot of bugs in your code and cheating yourself out of some key professional development opportunities. As far as I’m concerned, my code isn’t done until I’ve gone over it with a fellow developer.

在 Vertigo 参与了一段时间的代码评审之后，我相信**同行代码评审是你为改进代码所能做的最大的一件事。** 如果你*现在*还没有和另一位开发者一起做代码评审，那么你的代码里正漏掉大量 bug ，你也白白错过了许多关键的专业成长机会。在我看来，只要还没和一位开发者同伴一起过一遍，我的代码就不算完成。

But don’t take my word for it. McConnell provides plenty of evidence for the efficacy of code reviews in [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670):

但别只听我说。 McConnell 在 [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670) 中为代码评审的有效性提供了大量证据：

> … software testing alone has limited effectiveness – the average defect detection rate is only 25 percent for unit testing, 35 percent for function testing, and 45 percent for integration testing. In contrast, **the average effectiveness of design and code inspections are 55 and 60 percent**. Case studies of review results have been impressive: In a software-maintenance organization, 55 percent of one-line maintenance changes were in error before code reviews were introduced. After reviews were introduced, only 2 percent of the changes were in error. When all changes were considered, 95 percent were correct the first time after reviews were introduced. Before reviews were introduced, under 20 percent were correct the first time. / In a group of 11 programs developed by the same group of people, the first 5 were developed without reviews. The remaining 6 were developed with reviews. After all the programs were released to production, the first 5 had an average of 4.5 errors per 100 lines of code. The 6 that had been inspected had an average of only 0.82 errors per 100. Reviews cut the errors by over 80 percent. / The Aetna Insurance Company found 82 percent of the errors in a program by using inspections and was able to decrease its development resources by 20 percent. / IBM’s 500,000 line Orbit project used 11 levels of inspections. It was delivered early and had only about 1 percent of the errors that would normally be expected. / A study of an organization at AT&T with more than 200 people reported a 14 percent increase in productivity and a 90 percent decrease in defects after the organization introduced reviews. / Jet Propulsion Laboratories estimates that it saves about $25,000 per inspection by finding and fixing defects at an early stage.

> ……仅靠软件测试的效果有限 —— 单元测试的平均缺陷检出率只有 25%，功能测试为 35%，集成测试为 45%。相比之下，**设计评审与代码评审的平均有效性分别为 55% 和 60%**。评审结果的案例研究令人印象深刻：在一家软件维护机构，引入代码评审之前，单行维护性改动中有 55% 是错误的。引入评审之后，只有 2% 的改动是错误的。把所有改动合计来看，引入评审之后有 95% 的改动一次就正确。而在引入评审之前，一次就正确的不足 20%。/ 在一组由同一批人开发的 11 个程序中，前 5 个是在没有评审的情况下开发的，其余 6 个是在有评审的情况下开发的。所有程序都发布到生产环境之后，前 5 个平均每 100 行代码有 4.5 个错误，而经过检查的 6 个平均每 100 行只有 0.82 个错误。评审把错误减少了 80% 以上。/ Aetna 保险公司通过使用审查在一个程序中发现了 82% 的错误，并得以把开发资源削减 20%。/ IBM 那个 50 万行的 Orbit 项目采用了 11 层审查。它提前交付，而且错误只有通常预期的大约 1%。/ 一项针对 AT&T 某机构 200 多人的研究报道称，该机构引入评审之后生产率提高了 14%，缺陷减少了 90%。/ 喷气推进实验室估计，通过在早期阶段发现并修复缺陷，每次审查大约可节省 25,000 美元。

The only hurdle to a code review is finding a developer you respect to do it, and making the time to perform the review. Once you get started, I think you’ll quickly find that every minute you spend in a code review is paid back tenfold.

代码评审唯一的障碍，是找到一位你尊重的开发者来做这件事，并腾出做评审的时间。一旦开始，我想你很快就会发现，你在代码评审上花的每一分钟都会得到十倍的回报。

If your organization is new to code reviews, I highly recommend Karl’s book, [Peer Reviews in Software](http://www.amazon.com/exec/obidos/ASIN/0201734850): A Practical Guide. The [sample chapters](https://web.archive.org/web/20060315135046/http://www.processimpact.com/reviews_book/reviews_book_toc.shtml) Karl provides on his website are a great primer, too.

如果你的组织对代码评审还很陌生，我强烈推荐 Karl 的书 [Peer Reviews in Software](http://www.amazon.com/exec/obidos/ASIN/0201734850)： A Practical Guide 。 Karl 在自己网站上提供的[样章 ](https://web.archive.org/web/20060315135046/http://www.processimpact.com/reviews_book/reviews_book_toc.shtml)也是很棒的入门材料。
