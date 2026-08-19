---
title: "自用清单"
description: "自己用着顺手的工具、插件与资源推荐，持续更新"
---

这里记录我自己在用的工具清单，都是亲测好用的东西，持续更新中。

## 开发环境

### Miniconda
- **用途**：Python 环境管理，比 Anaconda 更轻量，按项目隔离环境。
- **推荐理由**：装 Miniconda 而不是 Anaconda，启动快、体积小，`conda create -n xxx python=3.x` 一条命令搞定环境。
- **官网**：[docs.conda.io/miniconda](https://docs.conda.io/en/latest/miniconda.html)
- **备注**：配合清华镜像源使用，下载快很多。

## 编辑器与插件

### Visual Studio Code
- **用途**：主力代码编辑器。
- **官网**：[code.visualstudio.com](https://code.visualstudio.com/)

**好用插件推荐：**

| 插件 | 用途 |
| --- | --- |
| Chinese (Simplified) Language Pack | 中文界面 |
| Python + Pylance | Python 开发体验最佳组合 |
| GitLens | 查看代码历史、blame 信息 |
| Material Icon Theme | 更清晰的文件图标 |
| Error Lens | 错误信息直接显示在代码行尾 |
| Prettier | 代码格式化 |

## 效率工具

### Everything
- **用途**：Windows 本地文件秒级搜索。
- **推荐理由**：比资源管理器自带的搜索快几个数量级，装完就离不开。
- **官网**：[voidtools.com](https://www.voidtools.com/zh-cn/)

### Snipaste
- **用途**：截图 + 贴图，截图后可以钉在屏幕上对照。
- **推荐理由**：写代码、写文档时的效率神器。
- **官网**：[snipaste.com](https://www.snipaste.com/)

## AI 工具

### cnb-npc-skill（自研）
- **用途**：让 CNB 的 CodeBuddy NPC 替自己上班——一句话派发任务，云端 AI 在仓库里自主完成开发并提交 PR，我只需验收。
- **推荐理由**：把"建仓库→推代码→@CodeBuddy→等结果"的繁琐流程封装成一条命令；不占主力 agent 上下文、不占模型并发、当前免费；实测 240 秒内 NPC 提交 PR。
- **GitHub**：[Zi-Yi-Ming/cnb-npc-skill](https://github.com/Zi-Yi-Ming/cnb-npc-skill)
- **相关笔记**：[让 CNB CodeBuddy NPC 替我上班：cnb-npc-skill 项目实践](/notes/cnb-npc-skill/)

## 学习与资源

### WorldQuant BRAIN
- **用途**：量化研究平台，免费练习 Alpha 研究。
- **推荐理由**：对量化入门友好，无需实盘资金也能积累研究经验。
- **官网**：[platform.worldquantbrain.com](https://platform.worldquantbrain.com/)
- **相关笔记**：[WorldQuant BRAIN 平台介绍](https://blog.csdn.net/2402_87488142/article/details/162426839)
