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

### Node.js + pnpm
- **用途**：前端与工具链的运行时 + 包管理器。
- **推荐理由**：Node 18+ 内置 `fetch`，写脚本/CLI 零依赖；pnpm 装包快、省磁盘。
- **官网**：[nodejs.org](https://nodejs.org/) · [pnpm.io](https://pnpm.io/)

### Git + GitHub Desktop
- **用途**：版本控制与协作。
- **推荐理由**：命令行处理复杂操作，GitHub Desktop 看 diff、处理冲突更直观。
- **官网**：[git-scm.com](https://git-scm.com/) · [desktop.github.com](https://desktop.github.com/)

### Docker Desktop
- **用途**：容器化开发与部署（配合 WSL2）。
- **推荐理由**：本地复现服务器环境、部署微信云托管等项目都用得上。
- **官网**：[docker.com](https://www.docker.com/products/docker-desktop/)

### Hugo
- **用途**：本博客的静态站点生成器。
- **推荐理由**：单二进制、秒级构建，Markdown 写文章 + GitHub Pages 免费托管。
- **官网**：[gohugo.io](https://gohugo.io/)

## 编辑器与插件

### Visual Studio Code
- **用途**：主力代码编辑器。
- **官网**：[code.visualstudio.com](https://code.visualstudio.com/)

**我实际在用的插件（有特点的）：**

| 插件 | 用途 |
| --- | --- |
| Python + Pylance + debugpy | Python 开发三件套：补全、类型检查、调试 |
| Jupyter (ms-toolsai) | 直接在 VSCode 里跑 .ipynb，配合数据分析和量化研究 |
| Vue (Volar) | Vue 3 官方语言支持，写小程序/前端项目必备 |
| Java 扩展包（redhat.java + vscjava） | Java 全家桶：编译、调试、Maven、Gradle、测试 |
| 微信小程序开发助手（minapp-vscode） | 小程序 wxml/wxss 语法高亮与补全 |
| GitLens | 看代码 blame、提交历史、分支关系 |
| Dev Containers | 一键进入 Docker 容器开发环境 |
| Rainbow CSV | CSV 文件按列着色，数据文件一目了然 |
| Live Server | 静态页面实时预览，改完即刷新 |
| ChatGPT 官方 | 在编辑器里直接问 AI，不用切窗口 |
| One Candy Dark | 深色主题，看代码更舒服 |
| markdownlint + Prettier + ESLint | 文档/代码规范与格式化 |
| PDF 预览 | 编辑器里直接看 PDF，不用另开阅读器 |

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

### WorldQuant BRAIN
- **用途**：量化研究平台，免费练习 Alpha 研究。
- **推荐理由**：对量化入门友好，无需实盘资金也能积累研究经验。
- **官网**：[platform.worldquantbrain.com](https://platform.worldquantbrain.com/)

## 联系方式

- **CSDN**：[blog.csdn.net/2402_87488142](https://blog.csdn.net/2402_87488142)（技术笔记与文章）
- **GitHub**：[github.com/Zi-Yi-Ming](https://github.com/Zi-Yi-Ming)（开源项目，如 cnb-npc-skill）
- **QQ**：3125727661
- **邮箱**：[ziyim2026@gmail.com](mailto:ziyim2026@gmail.com)
