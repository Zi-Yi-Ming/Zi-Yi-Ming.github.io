---
title: "Toolbox"
description: "记录我在开发、研究与写作中实际使用的工具"
ShowReadingTime: false
ShowWordCount: false
hideAuthor: true
hideMeta: true
---

记录我在开发、研究与写作中实际使用的工具与插件，随工作环境的变化持续更新。常规必备的就不占篇幅了；自己写的会标（自研）。

## 开发环境

### [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Python 环境管理。主要用于不同项目和实验之间的环境隔离。

## VS Code 插件

| 工具 | 用途 | 保留原因 |
| --- | --- | --- |
| [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) + [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) + [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) | 文档与代码规范、格式化 | 写 Markdown 和代码时保持一致的格式标准 |
| [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) | CSV 按列着色 | 看回测数据等表格文件时结构一目了然 |
| [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) | 容器化开发环境 | 需要复现项目环境时比手动配置更可靠 |
| [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) | Git 历史、blame、分支关系 | 查看代码演进时比命令行更直观 |
| [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) | Notebook 与数据分析 | 量化研究和数据实验时直接使用 |

## 笔记软件

### [Obsidian](https://obsidian.md/)

本地 Markdown 知识库，用 Git 做版本管理。笔记全部落在自己手里，不依赖某个云端服务的锁定。

| 插件 | 用途 | 保留原因 |
| --- | --- | --- |
| obsidian-git | 用 GitHub 仓库同步笔记与版本管理 | 笔记的每次改动都有迹可循 |
| obsidian-enhancing-export | 导出 PDF / HTML | 需要分享或归档时一键转出 |
| obsidian-custom-attachment-location | 自定义附件存放位置 | 保持笔记库结构整齐 |

## 效率工具

### [Everything](https://www.voidtools.com/zh-cn/)

Windows 文件名搜索。基本替代了资源管理器自带的搜索。

### [Snipaste](https://www.snipaste.com/)

截图 + 贴图。截图可以钉在屏幕上，写代码、对文档时对照着看。

### [Geek Uninstaller](https://geekuninstaller.com/)

卸载工具。绿色单文件，卸载时连同残留文件和注册表项一起清理。

## AI 工具

### [ZCode](https://zcode.ai/)

桌面端 AI 助手。目前在用，偶尔会有点 bug，但已经留在日常流程里。

### [AtomCode](https://atomcode.atomgit.com/)

终端里的 AI 编码助手。缓存命中率高，也更适配国内生态。

### [Claude Code](https://www.anthropic.com/claude-code)

啥都能干。AI 编程最高的山，最长的河。

### cnb-npc-skill（自研）

让 CNB 的 CodeBuddy NPC 在云端替我干活：一句话派发任务，它在仓库里执行完、提交 PR（或只读评审出报告），我只管验收。不占主力 Agent 的上下文和模型并发，实测 240 秒内提交 PR。

[cnb-npc-skill](https://github.com/Zi-Yi-Ming/cnb-npc-skill) · [项目实践（CSDN）](https://blog.csdn.net/2402_87488142/article/details/164303415)

## 学习与资源

### [GitHub](https://github.com/)

日常开发、开源协作和项目托管。

### [Google Skills](https://skills.google/)

Google 的官方学习平台。用于补充云、AI 等方向的实践知识。

### [WorldQuant BRAIN](https://platform.worldquantbrain.com/)

量化研究平台。用于 Alpha Research 和回测实验。
