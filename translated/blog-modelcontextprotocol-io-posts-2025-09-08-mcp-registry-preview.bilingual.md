# MCP Registry

# MCP 注册表

Today, we’re launching the Model Context Protocol (MCP) Registry—an open catalog and API for publicly available MCP servers to improve discoverability and implementation. By standardizing how servers are distributed and discovered, we’re expanding their reach while making it easier for clients to get connected.

今天，我们推出模型上下文协议（MCP）注册表（Registry）——一个面向公开可用 MCP 服务器的开放目录与 API，用于改善可发现性与落地实现。通过统一服务器的分发与发现方式，我们既扩大了服务器的覆盖范围，也让客户端更容易完成对接。

The MCP Registry is now available in preview. To get started:

MCP 注册表现已开放预览。要开始使用：

- **Add your server** by following our guide on [Adding Servers to the MCP Registry](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx) (for server maintainers)
- **Access server data** by following our guide on [Accessing MCP Registry Data](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx) (for client maintainers)

- **添加你的服务器**，请参照我们的指南[将服务器添加到 MCP 注册表](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx)（面向服务器维护者）
- **访问服务器数据**，请参照我们的指南[访问 MCP 注册表数据](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx)（面向客户端维护者）

# Single source of truth for MCP servers

# MCP 服务器的唯一事实来源

In March 2025, we shared that we wanted to build a central registry for the MCP ecosystem. Today we are announcing that we’ve launched [https://registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io) as the official MCP Registry. As part of the MCP project, the MCP Registry, as well as a parent [OpenAPI specification](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/official-registry-api.md), are open source—allowing everyone to build a compatible sub-registry.

2025 年 3 月，我们曾提出要为 MCP 生态构建一个中央注册表。今天我们宣布，已上线 [https://registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io) 作为官方 MCP 注册表。作为 MCP 项目的一部分，MCP 注册表以及上层的 [OpenAPI 规格](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/official-registry-api.md)都是开源的，任何人都可以据此构建兼容的子注册表。

Our goal is to standardize how servers are distributed and discovered, providing a primary source of truth that sub-registries can build upon. In turn, this will expand server reach and help clients find servers more easily across the MCP ecosystem.

我们的目标是统一服务器的分发与发现方式，提供一个子注册表可以据以构建的唯一事实来源。这反过来会扩大服务器覆盖范围，帮助客户端更轻松地在整个 MCP 生态中找到服务器。

## Public and private sub-registries

## 公共与私有子注册表

In building a central registry, it was important to us not to take away from existing registries that the community and companies have built. The MCP Registry serves as a primary source of truth for publicly available MCP servers, and organizations can choose to [create sub-registries](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx) based on custom criteria. For example:

在构建中央注册表时，我们很重视不削弱社区和公司已经建成的现有注册表。MCP 注册表是公开可用 MCP 服务器的唯一事实来源，组织可以按自定义标准[创建子注册表](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx)。例如：

**Public subregistries** like opinionated “MCP marketplaces” associated with each MCP client are free to augment and enhance data they ingest from the upstream MCP Registry. Every MCP end-user persona will have different needs, and it is up to the MCP client marketplaces to properly serve their end-users in opinionated ways.

**公共子注册表**，比如与各个 MCP 客户端关联的、有明确取向的“MCP 应用市场”，可以自由扩充和增强其从上游 MCP 注册表获取的数据。每一类 MCP 终端用户都会有不同需求，理应由 MCP 客户端应用市场以有明确取向的方式服务好自己的终端用户。

**Private subregistries** will exist within enterprises that have strict privacy and security requirements, but the MCP Registry gives these enterprises a single upstream data source they can build upon. At a minimum, we aim to share API schemas with these private implementations so that associated SDKs and tooling can be shared across the ecosystem.

**私有子注册表**将存在于有严格隐私与安全要求的企业内部，而 MCP 注册表为这些企业提供了一个可以据以构建的上游数据源。我们至少会与这些私有实现共享 API schema，以便相关的 SDK 与工具能在整个生态中复用。

In both cases, the MCP Registry is the starting point – it’s the centralized location where MCP server maintainers publish and maintain their self-reported information for these downstream consumers to massage and deliver to their end-users.

无论哪种情况，MCP 注册表都是起点——它是 MCP 服务器维护者发布和维护其自述信息的中心位置，供这些下游消费方加工并交付给各自的终端用户。

## Community-driven mechanism for moderation

## 社区驱动的审核机制

The MCP Registry is an official MCP project maintained by the registry working group and permissively licensed. Community members can submit issues to flag servers that violate the MCP [moderation guidelines](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/moderation-policy.mdx)—such as those containing spam, malicious code, or impersonating legitimate services. Registry maintainers can then denylist these entries and retroactively remove them from public access.

MCP 注册表是官方 MCP 项目，由注册表工作组维护，采用宽松许可。社区成员可以提交 issue 来标记违反 MCP [审核准则](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/moderation-policy.mdx)的服务器，例如包含垃圾信息、恶意代码或冒充合法服务的服务器。注册表维护者随后可以将这些条目列入拒绝名单，并追溯性地将其从公开访问中移除。

# Getting started

# 开始使用

To get started:

要开始使用：

- **Add your server** by following our guide on [Adding Servers to the MCP Registry](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx) (for server maintainers)
- **Access server data** by following our guide on [Accessing MCP Registry Data](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx) (for client maintainers)

- **添加你的服务器**，请参照我们的指南[将服务器添加到 MCP 注册表](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx)（面向服务器维护者）
- **访问服务器数据**，请参照我们的指南[访问 MCP 注册表数据](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/registry-aggregators.mdx)（面向客户端维护者）

This preview of the MCP Registry is meant to help us improve the user experience before general availability and does not provide data durability guarantees or other warranties. We advise MCP adopters to watch development closely as breaking changes may occur before the registry is made generally available.

MCP 注册表的这个预览版旨在帮助我们在正式发布前改善用户体验，它不提供数据持久性保证或其他担保。我们建议采用 MCP 的各方密切关注开发进展，因为在注册表正式发布之前可能会出现破坏性变更。

As we continue to develop the registry, we encourage feedback and contributions on the [modelcontextprotocol/registry GitHub repository](https://github.com/modelcontextprotocol/registry): Discussion, Issues, and Pull Requests are all welcome.

随着注册表持续开发，我们欢迎在 [modelcontextprotocol/registry GitHub 仓库](https://github.com/modelcontextprotocol/registry)上提出反馈和贡献：Discussion、Issue 和拉取请求都欢迎。

# Thanks to the MCP community

# 感谢 MCP 社区

The MCP Registry has been a collaborative effort from the beginning and we are incredibly grateful for the enthusiasm and support from the broader developer community.

MCP 注册表从一开始就是协作的产物，我们非常感谢广大开发者社区的热情与支持。

In February 2025, it began as a grassroots project when MCP creators [David Soria Parra](https://github.com/dsp-ant) and [Justin Spahr-Summers](https://github.com/jspahrsummers) asked the [PulseMCP](https://www.pulsemcp.com/) and [Goose](https://block.github.io/goose/) teams to help build a centralized community registry. Registry Maintainer [Tadas Antanavicius](https://github.com/tadasant) from [PulseMCP](https://www.pulsemcp.com/) spearheaded the initial effort in collaboration with [Alex Hancock](https://github.com/alexhancock) from [Block](https://block.xyz/). They were soon joined by Registry Maintainer [Toby Padilla](https://github.com/toby), Head of MCP at [GitHub](https://github.com/), and more recently, [Adam Jones](https://github.com/domdomegg) from [Anthropic](https://www.anthropic.com/) joined as Registry Maintainer to drive the project towards the launch today. The [initial announcement](https://github.com/modelcontextprotocol/registry/discussions/11) of the MCP Registry’s development lists 16 contributing individuals from at least 9 different companies.

2025 年 2 月，它从草根项目起步：MCP 的创建者 [David Soria Parra](https://github.com/dsp-ant) 和 [Justin Spahr-Summers](https://github.com/jspahrsummers) 邀请 [PulseMCP](https://www.pulsemcp.com/) 与 [Goose](https://block.github.io/goose/) 团队协助构建一个中心化的社区注册表。来自 [PulseMCP](https://www.pulsemcp.com/) 的注册表维护者 [Tadas Antanavicius](https://github.com/tadasant) 与来自 [Block](https://block.xyz/) 的 [Alex Hancock](https://github.com/alexhancock) 共同牵头了最初的工作。随后，来自 [GitHub](https://github.com/) 的 MCP 负责人、注册表维护者 [Toby Padilla](https://github.com/toby) 加入，最近来自 [Anthropic](https://www.anthropic.com/) 的 [Adam Jones](https://github.com/domdomegg) 也作为注册表维护者加入，推动项目走到今天的发布。[MCP 注册表开发工作的最初公告](https://github.com/modelcontextprotocol/registry/discussions/11)列出了来自至少 9 家不同公司的 16 位贡献者。

Many others made crucial contributions to bring this project to life: [Radoslav Dimitrov](https://github.com/rdimitrov) from [Stacklok](https://stacklok.com/), [Avinash Sridhar](https://github.com/sridharavinash) from [GitHub](https://github.com/), [Connor Peet](https://github.com/connor4312) from [VS Code](https://code.visualstudio.com/), [Joel Verhagen](https://github.com/joelverhagen) from [NuGet](https://www.nuget.org/), [Preeti Dewani](https://github.com/pree-dew) from [Last9](https://last9.io/), [Avish Porwal](https://github.com/Avish34) from [Microsoft](https://www.microsoft.com/), [Jonathan Hefner](https://github.com/jonathanhefner), and many Anthropic and GitHub employees that provided code reviews and development support. We are also grateful to everyone on the [Registry’s contributors log](https://github.com/modelcontextprotocol/registry/graphs/contributors) and those who participated in [discussions and issues](https://github.com/modelcontextprotocol/registry).

还有许多人为让这个项目落地做出了关键贡献：来自 [Stacklok](https://stacklok.com/) 的 [Radoslav Dimitrov](https://github.com/rdimitrov)、来自 [GitHub](https://github.com/) 的 [Avinash Sridhar](https://github.com/sridharavinash)、来自 [VS Code](https://code.visualstudio.com/) 的 [Connor Peet](https://github.com/connor4312)、来自 [NuGet](https://www.nuget.org/) 的 [Joel Verhagen](https://github.com/joelverhagen)、来自 [Last9](https://last9.io/) 的 [Preeti Dewani](https://github.com/pree-dew)、来自 [Microsoft](https://www.microsoft.com/) 的 [Avish Porwal](https://github.com/Avish34)、[Jonathan Hefner](https://github.com/jonathanhefner)，以及许多提供代码评审与开发支持的 Anthropic 和 GitHub 员工。我们也感谢[注册表贡献者名单](https://github.com/modelcontextprotocol/registry/graphs/contributors)上的每一位，以及参与[讨论与 issue](https://github.com/modelcontextprotocol/registry)的各位。

We deeply appreciate everyone investing in this foundational open source infrastructure. Together, we’re helping developers and organizations worldwide to build more reliable, context-aware AI applications. On behalf of the MCP community, thank you.

我们深深感谢每一位为这套基础性开源基础设施投入心力的人。我们正在共同帮助全球的开发者和组织构建更可靠、具备上下文感知能力的 AI 应用。谨代表 MCP 社区，谢谢大家。
