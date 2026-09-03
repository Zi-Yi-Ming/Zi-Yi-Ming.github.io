---
title: "step-pilot"
date: 2026-09-03
weight: 40
description: "基于 pi 系开源项目（pi-tui）构建的终端 Coding Agent CLI：上游探索分支问题较多、且偏通用大模型，本项目 fork 后针对 Step 3.7 Flash 等小模型深度优化——精简 system prompt、收紧上下文预算、提前压缩，并修复一批上游遗留问题，独立演进发布。"
tech: ["TypeScript", "pi-tui", "CLI", "AI Agent", "小模型优化"]
status: "开源 · MIT · v0.1.5 活跃开发"
github: "https://github.com/Zi-Yi-Ming/step-pilot"
---

[step-pilot](https://github.com/Zi-Yi-Ming/step-pilot) 是一个终端 Coding Agent CLI，血统上基于 pi 系开源项目——TUI/agent 壳构建在 [`@earendil-works/pi-tui`](https://github.com/earendil-works/pi)（pi 仓库的 `packages/tui`）之上，同时兼容 Anthropic Messages / OpenAI Chat / OpenAI Responses 三种协议。

为什么会有这个 fork：我参考的**上游探索分支问题较多**（stepfun 的 `step-code-explore-pi` 自己都标注 explore），且默认策略是为通用大模型设计的。我的目标是把小模型用起来，所以做了这些：

- **精简 system prompt 到 ~2000 字符**：去掉冗余运行时自述，提升小模型的指令遵循稳定性
- **收紧上下文预算**：工具结果上限、压缩触发阈值、保留消息数都按小模型重新调过
- **修复一批上游遗留问题**：pickers 的 Windows Enter 路径、`/compact` 手动与自动不一致、摘要质量闸门误判等（已列入 CHANGELOG）
- **MCP 增强**：支持 streamable http 远程 server、调用超时防护、超长结果的语义预处理

开发状态：v0.1.5，201 个测试文件 / 2778 个用例全绿，CI 跑 Ubuntu / Windows / macOS 三平台，附中英双语文档与 Releases 单文件可执行版。安装与使用见 [README](https://github.com/Zi-Yi-Ming/step-pilot#readme)。
