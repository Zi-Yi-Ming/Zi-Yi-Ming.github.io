---
title: "desktop-for-step-code"
date: 2026-10-10
weight: 10
featured: 2
description: "Step Code 的社区 Windows 桌面客户端（Electron + React + TypeScript，17★）：两人团队二号贡献者，21 个 PR 已合入，主攻构建发布链路与 CI 一致性。"
tech: ["Electron", "React", "TypeScript", "Windows"]
status: "核心贡献者 · 21 PR 已合入"
github: "https://github.com/7oMB2006/desktop-for-step-code"
---

[desktop-for-step-code](https://github.com/7oMB2006/desktop-for-step-code) 是 [Step Code](https://github.com/stepfun-ai/Step-Code) 的社区 Windows 桌面客户端：在官方桌面端缺位时，用 Electron + React + TypeScript 把工作区、会话管理和流式对话跑起来，Step Code 负责底层的 agent 执行。MIT 协议，17★。

我是这个两人团队的二号贡献者：43 个提交、21 个 PR 合入，方向集中在构建与发布链路——

- 集成补丁的 npm 构建支持三级降级，构建失败时能逐级回退而不是直接断掉
- 把 CI 工作流里的上游钉点也纳入一致性检查，杜绝“本地能构建、CI 悄悄漂移”
- 修正构建说明里的上游钉点与补丁应用方式，文档和实际流程对齐
- 回合撤销记录的批量采集与不可重建轮的冲突表达
- 变更来源断言的等待标签修复

产品侧的能力面：流式对话与思考深度选择、项目工作区与会话（排序 / 置顶 / 归档 / 分支）、并发会话与排队发送、steering、工具审批与 subagent 状态、摘要 / 上下文 / diff 检视、内置终端与文件预览、Step 账号登录与 MCP 配置、中英文界面与明暗主题、GitHub 更新检查。
