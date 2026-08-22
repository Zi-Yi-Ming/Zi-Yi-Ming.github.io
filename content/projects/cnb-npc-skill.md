---
title: "cnb-npc-skill"
date: 2026-08-19
weight: 10
description: "零依赖 Node.js CLI：把「建仓库→推代码→@CodeBuddy→等 PR」全链路封装成一条命令，让 CNB 云端的 AI 智能体在仓库里自主完成开发任务，实测 240 秒内提交 PR。"
tech: ["Node.js", "CLI", "AI Agent", "自动化", "开源"]
status: "开源 · MIT"
github: "https://github.com/Zi-Yi-Ming/cnb-npc-skill"
---

把 CNB 平台 CodeBuddy NPC 的完整工作流（建组织仓库、推送代码、@CodeBuddy 开启工作模式、轮询 PR）封装成一条命令：

```bash
node bin/cnb-npc.js run "写一个 Python 脚本 hello.py，输出 Hello, CodeBuddy NPC!"
```

- 零依赖、MIT 协议，内置 SKILL.md，可被 AI 助手直接调用
- 实测 **240 秒内** NPC 提交 PR（[Issue/PR 实录](https://cnb.cool/ziyim/hello-npc)）
- 完整技术拆解见笔记：[cnb-npc-skill 项目实践](/notes/cnb-npc-skill/)
