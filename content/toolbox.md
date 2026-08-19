---
title: "自用清单"
description: "自己用着顺手的工具、插件与资源推荐，持续更新"
ShowReadingTime: false
ShowWordCount: false
hideAuthor: true
hideMeta: true
---

这里只列我实际用过、觉得值得留档的工具和插件，持续更新；常规必备的（浏览器、输入法这类人手一个的）就不占篇幅了。

## 开发环境

### Miniconda
- **用途**：Python 环境管理，按项目隔离环境。
- **推荐理由**：装 Miniconda 而不是 Anaconda，启动快、体积小，`conda create -n xxx python=3.x` 一条命令搞定环境。
- **官网**：[docs.conda.io/miniconda](https://docs.conda.io/en/latest/miniconda.html)

## 编辑器与插件

### Visual Studio Code
- **用途**：主力代码编辑器。
- **官网**：[code.visualstudio.com](https://code.visualstudio.com/)

**好用插件推荐：**

| 插件 | 用途 |
| --- | --- |
| markdownlint + Prettier + ESLint | 文档与代码规范、格式化 |
| Rainbow CSV | CSV 文件按列着色，数据文件一目了然 |
| Dev Containers | 一键进入 Docker 容器开发环境 |
| GitLens | 查看代码 blame、提交历史、分支关系 |
| Jupyter | 直接在 VSCode 里跑 .ipynb，配合数据分析与量化研究 |

## 笔记软件

### Obsidian
- **用途**：本地 Markdown 笔记库，双链笔记。
- **推荐理由**：搭配 `obsidian-git` 插件可以用 GitHub 远程仓库同步，效果不比官方付费的 Obsidian Sync 差，免费且数据完全自持。
- **官网**：[obsidian.md](https://obsidian.md/)

**必装插件：**

| 插件 | 用途 |
| --- | --- |
| obsidian-git | 用 GitHub 仓库做笔记同步与版本管理 |
| obsidian-enhancing-export | 增强导出，笔记一键转 PDF / HTML |
| obsidian-custom-attachment-location | 自定义附件存放位置，保持笔记库整洁 |

## 效率工具

### Everything
- **用途**：Windows 本地文件秒级搜索。
- **推荐理由**：比资源管理器自带的搜索快几个数量级，装完就离不开。
- **官网**：[voidtools.com](https://www.voidtools.com/zh-cn/)

### Snipaste
- **用途**：截图 + 贴图，截图后可以钉在屏幕上对照。
- **推荐理由**：写代码、写文档时的效率神器。
- **官网**：[snipaste.com](https://www.snipaste.com/)

### Geek Uninstaller
- **用途**：强力卸载软件，连残留文件和注册表项一起清。
- **推荐理由**：绿色单文件免安装，卸载完不留垃圾；对付卸载不干净的软件很管用。
- **官网**：[geekuninstaller.com](https://geekuninstaller.com/)

## AI 工具

### ZCode
- **用途**：桌面端 AI 助手。
- **推荐理由**：目前使用体验最好的桌面端 AI 助手。
- **官网**：[zcode.ai](https://zcode.ai/)

### AtomCode
- **用途**：终端里的 AI 编码助手。
- **推荐理由**：缓存命中率高，比较推荐刚开始用终端助手开发的小白用。
- **官网**：[atomcode.atomgit.com](https://atomcode.atomgit.com/)

### Claude Code
- **用途**：终端里的 AI 编程助手，配合本博客写文章、改代码。
- **推荐理由**：上下文管理强，适合在项目目录里直接干活。
- **官网**：[anthropic.com/claude-code](https://www.anthropic.com/claude-code)

### cnb-npc-skill（自研）
- **用途**：让 CNB 的 CodeBuddy NPC 替自己上班——一句话派发任务，云端 AI 在仓库里自主完成开发并提交 PR，我只需验收。
- **推荐理由**：把"建仓库→推代码→@CodeBuddy→等结果"的繁琐流程封装成一条命令；不占主力 agent 上下文、不占模型并发、当前免费；实测 240 秒内 NPC 提交 PR。
- **GitHub**：[Zi-Yi-Ming/cnb-npc-skill](https://github.com/Zi-Yi-Ming/cnb-npc-skill)
- **相关笔记**：[让 CNB CodeBuddy NPC 替我上班：cnb-npc-skill 项目实践](/notes/cnb-npc-skill/)

## 学习与资源

### GitHub
- **用途**：开源社区与代码托管。
- **推荐理由**：唯一真神。强烈建议有教育邮箱的都去申一个 GitHub Student Developer Pack 学生认证，免费额度与资源非常多。
- **官网**：[github.com](https://github.com/)

### Google Skills
- **用途**：Google 官方技能学习平台。
- **推荐理由**：免费学习 AI、编程、数字营销等技能，完成课程可拿证书。
- **官网**：[skills.google](https://www.skills.google/)

### WorldQuant BRAIN
- **用途**：量化研究平台，免费练习 Alpha 研究。
- **推荐理由**：对量化入门友好，无需实盘资金也能积累研究经验。
- **官网**：[platform.worldquantbrain.com](https://platform.worldquantbrain.com/)
