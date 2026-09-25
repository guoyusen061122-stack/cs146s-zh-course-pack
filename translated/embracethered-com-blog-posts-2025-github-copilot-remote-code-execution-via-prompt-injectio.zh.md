# 借助提示注入实现 Copilot 远程代码执行

这篇文章讲的是一个重要但也令人不安的提示注入发现，它会导致 [GitHub Copilot 和 VS Code](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53773) 中开发者机器被完全攻陷。

**它的实现方式是修改项目的 `settings.json` 文件，把 Copilot 置于 YOLO 模式。**

[![vscode episode 18](/blog/images/2025/episode12-yt.png)](/blog/images/2025/episode12-yt.png)

正如前几天在 [Amp](/blog/posts/2025/amp-agents-that-modify-system-configuration-and-escape/) 一文中所描述的，智能体身上一个容易被忽视的漏洞模式是：如果智能体能写文件并修改自身配置、或更新与安全相关的设置，就可能导致远程代码执行。这种情况并不罕见，做安全评审时应始终留意。

## 背景研究

在观察 VS Code 和 GitHub Copilot Agent Mode 时，我注意到一个奇怪的行为……它无需用户批准就能在工作区中创建并写入文件。

这些编辑会立即持久化，它们不是供评审的内存中的差异（diff）。修改会直接写入磁盘。

[![vscode 中能够修改自身设置的智能体](/blog/images/2025/agents-that-can.png)](/blog/images/2025/agents-that-can.png)

作为红队成员，你知道这类事情大概不是什么好事……于是我开始探究它能否被用来提权并执行代码。

### **YOLO 模式**

于是接下来我研究了 VS Code 中那些依赖项目／工作区文件夹内设置的功能，很快找到了一个有意思的目标。

[![vscode-exp-yolo-mode](/blog/images/2025/vscode-documentation-settings-json.png)](/blog/images/2025/vscode-documentation-settings-json.png)

原来在 `.vscode/settings.json` 文件里可以添加下面这一行：

`"chat.tools.autoApprove": true`

**这会把 GitHub Copilot 置于 YOLO 模式。**

它会禁用所有用户确认，于是我们能运行 shell 命令、浏览网页等等！

有意思的是，这是一个实验性功能，但它默认就存在。我并没有下载特殊版本，也没有把 VS Code 整体设为实验模式。

而且，它在 Windows、macOS 以及 Linux 上都能用。

## 利用链详解

劫持 Copilot 并提权的概念验证利用链如下：

1. 攻击始于植入源代码文件、网页、GitHub issue、工具调用响应或其他内容中的提示注入……有效载荷也可以把不可见文本当作指令使用。
1. 提示注入会先向 `~/.vscode/settings.json` 文件添加一行 **“chat.tools.autoApprove”: true**。如果文件夹和文件尚不存在，就会被创建出来。
1. **GitHub Copilot 立即进入 YOLO 模式！**
1. 攻击会运行一条终端命令。**而借助条件提示注入，我们实际上可以根据操作系统来决定运行什么。**
1. 我们实现了由提示注入驱动的远程代码执行。

下面这张截图展示了带有提示注入的演示文件、开发者在右侧聊天框中与该文件交互，以及弹出计算器的画面！

[![vscode-e2e-calc](/blog/images/2025/copilot-chat-result.png)](/blog/images/2025/copilot-chat-result.png)

当然，任何其他投递提示注入的手段，比如网页或 MCP 服务器返回的数据，都是攻击角度。我只是把它用在源代码文件里，因为这样最容易测试。

## 视频演示

### 简短演示

下面这段演示视频展示了在 Windows 上的代码执行。

这一段是在 macOS 上：

### 完整演示

下面这段较长的视频详细讲解了该发现与利用（漏洞）过程：

**能自己设置权限和配置的 AI 太疯狂了！**

## 把工作站接入僵尸网络 —— ZombAI

当然，这意味着我们可以把开发者的机器作为一个 **ZombAI** 接入僵尸网络。

另外，为了好玩，我们还可以修改 `settings.json` 文件，把 VS Code 切换成 `Red` 配色方案之类。

但事情不止于此！这还意味着我们可以构造一个真正的 AI 病毒，它附着在文件上，随着开发者下载并与被感染的文件交互而传播。

最后同样重要的是，为了证明我们完全控制了开发者的主机，我们展示了 Copilot 可以被劫持去下载恶意软件，并接入一个远程命令与控制服务器。

[![vscode-zombai-deployment](/blog/images/2025/github-agent-e2e-zombai.png)](/blog/images/2025/github-agent-e2e-zombai.png)

这意味着恶意软件、勒索软件、信息窃取程序等的大门已经打开。

真可怕。

## 构造 AI 病毒

看到这里，人们会注意到这基本上允许制造病毒。攻击者可以嵌入指令，一旦获得代码执行，其他恶意软件就能攻陷别的 Git 项目（以及 RAG 来源）以嵌入恶意指令，并提交更改、甚至强制推送到上游。

随着其他开发者在不知情的情况下传播被感染的代码，这会进一步扩散。

**最后，我们还需要谈谈不可见指令！**

## 使用不可见指令

有人可能会说，如果指令是以注释形式嵌入的，很快就会被发现。所以为了让事情更有意思一点，我继续构造了一个不可见的有效载荷，它能完成整条攻击链，但用户看不见。这种方式的可靠性没那么高，但它仍然生效了：

**注意：** 虽然这里使用不可见指令的演示在我这里多次成功，但使用不可见指令往往会让利用（漏洞）非常不可靠，而且通常也会被模型拒绝，此外 VS Code 一般还会显示一个关于 Unicode 字符的视觉提示。不过，攻击（以及模型）会随时间变得更强。同样值得指出的是，并非所有模型都容易受到这类不可见提示注入攻击的影响。

## 建议与修复

除了我分享的 YOLO 模式这个例子，实际上还有更多攻击角度。当 Microsoft 问我是否还有更多信息时，我又多看了看，注意到还有其他有问题的地方，例如 AI 可以写入的 `.vscode/tasks.json`，或者添加伪造的恶意 MCP 服务器等等，这些都可能导致代码执行。此外，AI 还能重新配置项目的用户界面和配置设置。

**最近我注意到开发者经常使用多个智能体，因此也存在覆盖其他智能体配置文件的威胁（把 bash 命令加入允许列表、添加 MCP 服务器……），因为这些文件通常也放在项目文件夹中。**

理想情况下，未经人类事先批准，AI 不应能够修改文件。许多其他编辑器确实会显示差异（diff），然后由开发者批准。

## 负责任披露

在 2025 年 6 月 29 日报告该漏洞后，Microsoft 确认了复现步骤并提出了一些后续问题。几周后，MSRC 指出这是他们早就在跟踪的问题，并会在 8 月前完成修补。随着 8 月的补丁星期二发布，该问题现已修复。

感谢来自 [Persistent Security](https://persistent-security.net/) 的 [Markus Vervier](https://x.com/marver)，他也发现并向 Microsoft 报告了这个漏洞。你可以在这里找到他们的[书面总结](https://www.persistent-security.net/post/part-iii-vscode-copilot-wormable-command-execution-via-prompt-injection)。还要感谢 [Ari Marzuk](https://x.com/Ari_MaccariTA)，他似乎也并行发现了这个问题。

感谢 MSRC 和产品团队的成员在缓解该问题过程中提供的帮助。

## 结论

这是又一个例子，说明 AI 智能体可能不会老实待在自己的盒子里！通过修改自身环境，GitHub Copilot 可以提权并执行代码，从而攻陷开发者的机器。正如我所发现的，这是智能体系统中并不少见的设计缺陷。

请持续留意这类设计缺陷，在威胁建模期间它们应该很容易被抓住。

祝好。

## 参考资料

- [Month of AI Bugs 2025](https://monthofaibugs.com)
- [Amp Code：借助提示注入实现任意命令执行（已修复）](/blog/posts/2025/amp-agents-that-modify-system-configuration-and-escape/)
- [Copilot 设置](https://code.visualstudio.com/docs/copilot/reference/copilot-settings)
- [CVE-2025-53773：GitHub Copilot 与 Visual Studio 远程代码执行漏洞](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53773)
- [Persistent Security 书面总结](https://www.persistent-security.net/post/part-iii-vscode-copilot-wormable-command-execution-via-prompt-injection)
- [Persistent Security](https://persistent-security.net/)
