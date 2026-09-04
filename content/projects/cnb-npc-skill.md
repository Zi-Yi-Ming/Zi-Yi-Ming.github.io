---
title: "cnb-npc-skill"
date: 2026-08-19
weight: 10
featured: 4
description: "零依赖 Node.js CLI：把「建仓库→推代码→@CodeBuddy→等 PR」全链路封装成一条命令，双模式——工作模式让云端 AI 写代码提 PR（实测 240 秒），只读模式做代码评审/方案分析。"
tech: ["Node.js", "CLI", "AI Agent", "自动化", "开源"]
status: "开源 · MIT"
github: "https://github.com/Zi-Yi-Ming/cnb-npc-skill"
---

把 CNB 平台 CodeBuddy NPC 的完整工作流（建组织仓库、推送代码、@CodeBuddy 开启工作模式、轮询 PR）封装成一条命令：

```bash
# 工作模式：建仓库 → 推代码 → 开 Issue(@CodeBuddy) → 轮询 → 汇报 PR
node bin/cnb-npc.js run "写一个 Python 脚本 hello.py，输出 Hello, CodeBuddy NPC!"

# 只读模式：NPC 只读分析并出报告，不改代码（代码评审/方案分析）
node bin/cnb-npc.js run "评审一下这个模块的设计" --no-work-mode
```

- 双模式：默认工作模式提 PR；`--no-work-mode` 只读评审，配套 `comments --wait` 收报告、`comment` 多轮追问、`api` 通用透传
- 零依赖、MIT 协议，内置 SKILL.md，可被 AI 助手直接调用，带 evals 评测套件与 CI
- 实测 **240 秒内** NPC 提交 PR（[Issue/PR 实录](https://cnb.cool/ziyim/hello-npc)）
- 完整技术拆解发布在 CSDN：[cnb-npc-skill 项目实践](https://blog.csdn.net/2402_87488142/article/details/164303415)
