---
title: "自用清单"
description: "自己用着顺手的工具、插件与资源推荐，持续更新"
ShowReadingTime: false
ShowWordCount: false
hideAuthor: true
hideMeta: true
---

这里只列我实际用过、觉得值得留档的工具和插件，会持续更新；常规必备的就不占篇幅了。

## 开发环境

### Miniconda

Python 环境管理用。推荐 Miniconda 而不是 Anaconda，启动快、体积小，按项目隔离环境就一条命令：

```bash
conda create -n xxx python=3.x
```

[官网](https://docs.conda.io/en/latest/miniconda.html)

## VS Code 插件

| 插件 | 用途 |
| --- | --- |
| [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) + [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) + [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) | 文档与代码规范、格式化 |
| [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) | CSV 文件按列着色，数据文件一目了然 |
| [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) | 一键进入 Docker 容器开发环境 |
| [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) | 看代码 blame、提交历史、分支关系 |
| [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) | 直接在 VS Code 里跑 .ipynb，配合数据分析与量化研究 |

## 笔记软件

### Obsidian

本地 Markdown 笔记库。搭配 `obsidian-git` 用 GitHub 仓库同步，相当于免费的 Obsidian Sync，数据全在自己手里。[官网](https://obsidian.md/)

必装插件：

| 插件 | 用途 |
| --- | --- |
| obsidian-git | 用 GitHub 仓库做笔记同步与版本管理 |
| obsidian-enhancing-export | 增强导出，笔记一键转 PDF / HTML |
| obsidian-custom-attachment-location | 自定义附件存放位置，保持笔记库整洁 |

## 效率工具

### Everything

Windows 上按文件名搜文件，基本秒出，比资源管理器自带的搜索好用太多，装上就回不去了。[官网](https://www.voidtools.com/zh-cn/)

### Snipaste

截图 + 贴图，截图可以钉在屏幕上，写代码、对文档的时候对照着看很方便。[官网](https://www.snipaste.com/)

### Geek Uninstaller

卸载软件用。绿色单文件免安装，卸载时会连残留文件和注册表项一起清掉，对付卸不干净的软件很管用。[官网](https://geekuninstaller.com/)

## AI 工具

### ZCode

桌面端 AI 助手，目前用着最顺手的，偶尔会有点 bug。[官网](https://zcode.ai/)

### AtomCode

终端里的 AI 编码助手，缓存命中率高，也更适配国内生态。刚开始用终端助手的话可以试试。[官网](https://atomcode.atomgit.com/)

### Claude Code

啥都能干。AI 编程最高的山，最长的河。[官网](https://www.anthropic.com/claude-code)

### cnb-npc-skill（自研）

让 CNB 的 CodeBuddy NPC 替我上班：一句话派发任务，云端 AI 在仓库里把活干完、提 PR（或只读评审出报告），我只管验收。把“建仓库→推代码→@CodeBuddy→等结果”这套手工流程压缩成一条命令，不占主力 agent 的上下文和模型并发，目前免费，实测 240 秒内 NPC 提交 PR。

[GitHub](https://github.com/Zi-Yi-Ming/cnb-npc-skill) · [项目笔记](/notes/cnb-npc-skill/)

## 学习与资源

### GitHub

开源社区，有教育邮箱的建议申一个 Student Developer Pack，免费资源很多，还在持续更新。[官网](https://github.com/)

### Google Skills

Google 官方的技能学习平台，AI、编程这些课免费学，学完能拿证书。[官网](https://skills.google/)

### WorldQuant BRAIN

量化研究平台，练 Alpha 不用实盘资金，对入门挺友好。[官网](https://platform.worldquantbrain.com/)
