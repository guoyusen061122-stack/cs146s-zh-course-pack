# 质量抽检报告

> 自动生成于 2026-09-25T12:38:07+08:00 ｜ 由 `src/s10_qa.py` 产出 ｜ 检查项对应 `TRANSLATION_SPEC.md` 的 R1–R10

## 一、总览

| 指标 | 数值 | 判定 |
|---|---:|---|
| 已译份数 | 110/110 | — |
| 段级结构对齐 | 5858/5697 | ✅ |
| 空译 | 0 | ✅ |
| 漏译/截断 | 0 | ✅ |
| 疑似未译英文 | 0 | ✅ |
| 代码块被改动 | 0 | ✅ |
| 链接丢失 | 0 | ✅ |
| 结构不一致 | 0 | ✅ |
| 中英文缺空格 | 0 | ✅ |
| 术语一致率 | 100.0% | ✅ |

- 术语命中 **4513** 次 / 违规 **0** 次 / 术语缺失（提示性）**68** 处

> **关于质检口径的一条取舍**：本报告刻意**不做**无法可靠判定的检查。
> 例如 `prompt` 的名词义必须译「提示词」，但动名词义（prompting）在中文里正当译法就是「提示」
> ——「零样本提示」「思维链提示」「角色提示」。曾用正则 `提示(?!词|工程|…)` 去拦，
> 结果 26 条命中里没有一条是错的。**一条误报会让二十条真报一起被忽略**，
> 所以该规则被撤掉，改为用「术语缺失」这一提示性指标间接观察。

## 二、逐份结果

| 语料 | 分组 | 块数 | 问题数 | 术语一致率 |
|---|---|---:|---:|---:|
| `arxiv-org-pdf-2405-13565__p1` | reading | 44/44 | 0 | 100.0% |
| `arxiv-org-pdf-2405-13565__p2` | reading | 8/8 | 0 | 100.0% |
| `arxiv-org-pdf-2405-13565__p3` | reading | 9/9 | 0 | 100.0% |
| `blakesmith-me-2015-02-09-code-review-essentials-for-` | reading | 39/39 | 0 | 100.0% |
| `blog-codinghorror-com-code-reviews-just-do-it` | reading | 8/8 | 0 | 100.0% |
| `blog-modelcontextprotocol-io-posts-2025-09-08-mcp-re` | reading | 24/24 | 0 | 100.0% |
| `blog-ravi-mehta-com-p-specs-are-the-new-source-code` | reading | 10/10 | 0 | 100.0% |
| `blog-stockapp-com-good-context-good-code` | reading | 42/42 | 0 | 100.0% |
| `cdn-openai-com-pdf-6a2631dc-783e-479b-b1a4-af0cfbd38` | reading | 25/25 | 0 | 100.0% |
| `cloud-google-com-discover-what-is-prompt-engineering` | reading | 165/165 | 0 | 100.0% |
| `developers-cloudflare-com-agents-guides-remote-mcp-s` | reading | 121/121 | 0 | 100.0% |
| `devin-ai-agents101` | reading | 89/89 | 0 | 100.0% |
| `embracethered-com-blog-posts-2025-github-copilot-rem` | reading | 61/61 | 0 | 100.0% |
| `fall2025-w01-fri9-26-power-prompting-for-llms` | media | 166/166 | 0 | 100.0% |
| `fall2025-w01-mon9-22-introduction-and-how-an-llm-is-` | media | 189/189 | 0 | 100.0% |
| `fall2025-w02-fri10-3-building-a-custom-mcp-server` | media | 85/85 | 0 | 100.0% |
| `fall2025-w02-mon9-29-building-a-coding-agent-from-sc` | media | 53/53 | 0 | 100.0% |
| `fall2025-w03-fri10-10-silas-alberti-head-of-research` | media | 70/70 | 0 | 100.0% |
| `fall2025-w03-mon10-6-from-first-prompt-to-optimal-id` | media | 54/54 | 0 | 100.0% |
| `fall2025-w03-mon10-6-from-first-prompt-to-optimal-id` | media | 143/143 | 0 | 100.0% |
| `fall2025-w04-fri10-17-boris-cherney-creator-of-claud` | media | 121/121 | 0 | 100.0% |
| `fall2025-w04-mon10-13-how-to-be-an-agent-manager` | media | 122/122 | 0 | 100.0% |
| `fall2025-w05-mon10-20-how-to-build-a-breakout-ai-dev` | media | 105/105 | 0 | 100.0% |
| `fall2025-w06-mon10-27-ai-qa-sast-dast-and-beyond` | media | 186/186 | 0 | 100.0% |
| `fall2025-w07-fri11-7-tomas-reimers-cpo-graphite` | media | 74/74 | 0 | 100.0% |
| `fall2025-w07-mon11-3-ai-code-review` | media | 108/108 | 0 | 100.0% |
| `fall2025-w08-mon11-10-end-to-end-apps-with-a-single-` | media | 81/81 | 0 | 100.0% |
| `fall2025-w09-fri11-21-mayank-agarwal-cto-resolve-and` | media | 121/121 | 0 | 100.0% |
| `fall2025-w09-mon11-17-incident-response-and-devops` | media | 134/134 | 0 | 100.0% |
| `fall2026-w01-tue9-22-course-intro-build-claude-code-` | media | 123/123 | 0 | 100.0% |
| `github-blog-developer-skills-github-how-to-review-co` | reading | 91/91 | 0 | 100.0% |
| `github-com-SeanHeelan-o3-finds-cve-2025-37899-blob-m` | reading | 5/5 | 0 | 100.0% |
| `github-com-humanlayer-advanced-context-engineering-f` | reading | 173/173 | 0 | 100.0% |
| `github-com-modelcontextprotocol-typescript-sdk-tree-` | reading | 52/52 | 0 | 100.0% |
| `graphite-dev-guides-ai-code-review-implementation-be` | reading | 82/82 | 0 | 100.0% |
| `last9-io-blog-traces-spans-observability-basics` | reading | 81/81 | 0 | 100.0% |
| `medium-com-outsightai-peeking-under-the-hood-of-clau` | reading | 64/64 | 0 | 100.0% |
| `notion-warp-dev-How-Warp-uses-Warp-to-build-Warp-216` | reading | 2/2 | 0 | 100.0% |
| `owasp-org-www-project-top-ten` | reading | 6/6 | 0 | 100.0% |
| `repo-fall2025-readmemd` | repo | 8/8 | 0 | 100.0% |
| `repo-fall2025-week1-assignmentmd` | repo | 19/19 | 0 | 100.0% |
| `repo-fall2025-week1-data-api-docstxt` | repo | 6/6 | 0 | 100.0% |
| `repo-fall2025-week1-readmemd` | repo | 2/2 | 0 | 100.0% |
| `repo-fall2025-week2-assignmentmd` | repo | 39/39 | 0 | 100.0% |
| `repo-fall2025-week2-writeupmd` | repo | 37/37 | 0 | 100.0% |
| `repo-fall2025-week3-assignmentmd` | repo | 16/16 | 0 | 100.0% |
| `repo-fall2025-week4-assignmentmd` | repo | 55/55 | 0 | 100.0% |
| `repo-fall2025-week4-docs-tasksmd` | repo | 15/15 | 0 | 100.0% |
| `repo-fall2025-week4-writeupmd` | repo | 43/43 | 0 | 100.0% |
| `repo-fall2025-week5-assignmentmd` | repo | 45/45 | 0 | 100.0% |
| `repo-fall2025-week5-docs-tasksmd` | repo | 23/23 | 0 | 100.0% |
| `repo-fall2025-week5-readmemd` | repo | 19/19 | 0 | 100.0% |
| `repo-fall2025-week5-writeupmd` | repo | 42/42 | 0 | 100.0% |
| `repo-fall2025-week6-assignmentmd` | repo | 27/27 | 0 | 100.0% |
| `repo-fall2025-week6-requirementstxt` | repo | 2/2 | 0 | 100.0% |
| `repo-fall2025-week6-writeupmd` | repo | 43/43 | 0 | 100.0% |
| `repo-fall2025-week7-assignmentmd` | repo | 17/17 | 0 | 100.0% |
| `repo-fall2025-week7-docs-tasksmd` | repo | 9/9 | 0 | 100.0% |
| `repo-fall2025-week7-readmemd` | repo | 19/19 | 0 | 100.0% |
| `repo-fall2025-week7-writeupmd` | repo | 45/45 | 0 | 100.0% |
| `repo-fall2025-week8-assignmentmd` | repo | 23/23 | 0 | 100.0% |
| `repo-fall2025-week8-writeupmd` | repo | 16/16 | 0 | 100.0% |
| `repo-master-readmemd` | repo | 8/8 | 0 | 100.0% |
| `repo-master-week1-assignmentmd` | repo | 51/51 | 0 | 100.0% |
| `repo-master-week1-writeupmd` | repo | 54/54 | 0 | 100.0% |
| `research-trychroma-com-context-rot__p1` | reading | 99/99 | 0 | 100.0% |
| `research-trychroma-com-context-rot__p2` | reading | 95/95 | 0 | 100.0% |
| `research-trychroma-com-context-rot__p3` | reading | 51/51 | 0 | 100.0% |
| `resolve-ai-blog-Top-5-Benefits` | reading | 44/44 | 0 | 100.0% |
| `resolve-ai-blog-kubernetes-troubleshooting-in-resolv` | reading | 55/55 | 0 | 100.0% |
| `resolve-ai-blog-product-deep-dive` | reading | 51/51 | 0 | 100.0% |
| `resolve-ai-blog-role-of-multi-agent-systems-AI-nativ` | reading | 49/49 | 0 | 100.0% |
| `semgrep-dev-blog-2025-finding-vulnerabilities-in-mod` | reading | 50/50 | 0 | 100.0% |
| `site-fall2025-faq` | site | 15/15 | 0 | 100.0% |
| `site-fall2025-grading` | site | 2/2 | 0 | 100.0% |
| `site-fall2025-overview` | site | 24/24 | 0 | 100.0% |
| `site-fall2025-syllabus` | site | 83/83 | 0 | 100.0% |
| `site-fall2026-faq` | site | 15/15 | 0 | 100.0% |
| `site-fall2026-grading` | site | 2/2 | 0 | 100.0% |
| `site-fall2026-overview` | site | 31/31 | 0 | 100.0% |
| `site-fall2026-syllabus` | site | 53/53 | 0 | 100.0% |
| `sre-google-sre-book-introduction` | reading | 68/68 | 0 | 100.0% |
| `stytch-com-blog-model-context-protocol-introduction_` | reading | 55/55 | 0 | 100.0% |
| `stytch-com-blog-model-context-protocol-introduction_` | reading | 51/51 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p1` | reading | 45/45 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p10` | reading | 1/1 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p11` | reading | 69/69 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p12` | reading | 106/106 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p2` | reading | 23/23 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p3` | reading | 8/8 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p4` | reading | 8/8 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p5` | reading | 9/9 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p6` | reading | 1/1 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p7` | reading | 16/16 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p8` | reading | 21/21 | 0 | 100.0% |
| `unit42-paloaltonetworks-com-agentic-ai-threats__p9` | reading | 1/1 | 0 | 100.0% |
| `www-anthropic-com-engineering-claude-code-best-pract` | reading | 89/89 | 0 | 100.0% |
| `www-anthropic-com-engineering-claude-code-best-pract` | reading | 99/99 | 0 | 100.0% |
| `www-anthropic-com-engineering-claude-code-best-pract` | reading | 1/1 | 0 | 100.0% |
| `www-anthropic-com-engineering-writing-tools-for-agen` | reading | 104/104 | 0 | 100.0% |
| `www-cdn-anthropic-com-58284b19e702b49db9302d5b6f135a` | reading | 16/16 | 0 | 100.0% |
| `www-cdn-anthropic-com-58284b19e702b49db9302d5b6f135a` | reading | 14/14 | 0 | 100.0% |
| `www-cdn-anthropic-com-58284b19e702b49db9302d5b6f135a` | reading | 12/12 | 0 | 100.0% |
| `www-cdn-anthropic-com-58284b19e702b49db9302d5b6f135a` | reading | 11/11 | 0 | 100.0% |
| `www-dbreunig-com-2025-06-22-how-contexts-fail-and-ho` | reading | 59/59 | 0 | 100.0% |
| `www-promptingguide-ai-techniques` | reading | 132/132 | 0 | 100.0% |
| `www-reillywood-com-blog-apis-dont-make-good-mcp-tool` | reading | 27/27 | 0 | 100.0% |
| `www-splunk-com-en-us-blog-learn-sast-vs-dast` | reading | 164/164 | 0 | 100.0% |
| `www-warp-dev-university-getting-started-warp-vs-clau` | reading | 55/55 | 0 | 100.0% |
| `www-warp-dev-university` | reading | 55/55 | 0 | 100.0% |
