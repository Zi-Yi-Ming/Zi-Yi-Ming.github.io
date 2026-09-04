---
title: "ProjectForge"
date: 2026-09-04
weight: 5
featured: 3
description: "AI 驱动的工程项目教练与实现引擎：从 JD 出发做项目规划、生成任务图，再在明确约束下执行实现，并对结果做验证与再规划。"
tech: ["AI", "工程自动化", "任务图"]
status: "开源 · 活跃开发"
github: "https://github.com/Zi-Yi-Ming/ProjectForge"
---

ProjectForge 是我当前的核心个人项目：一个 AI 驱动的工程项目教练与实现引擎。它把「一段 JD / 一份需求」推进成可执行、可验证的工程实现，链路大致是：

- **JD-driven engineering**：从职位/项目描述里解析出要构建什么、验收标准是什么，而不是从一句空泛的需求开始
- **AI project planning**：基于解析结果生成项目规划，明确阶段、交付物与约束
- **task graph**：把规划拆成任务图，用节点与依赖表达执行单元，避免靠「顺序对话」硬推长任务
- **constrained execution**：让模型在明确边界（技术栈、文件范围、接口契约）内实现，而不是自由发挥
- **validation / replan**：对执行结果做验证，不通过就带着失败信息回到规划层再走一轮

状态：开源、活跃开发中。仓库与文档随开发推进持续更新，当前阶段侧重把「规划 → 执行 → 验证」这条链路跑稳。
