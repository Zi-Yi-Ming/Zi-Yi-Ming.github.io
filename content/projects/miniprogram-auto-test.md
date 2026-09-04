---
title: "miniprogram-auto-test"
date: 2026-08-31
weight: 15
featured: 5
description: "微信小程序自动化测试：让 AI 读 WXML+JS 直接生成可运行的测试脚本，附已发布 npm 适配层 miniprogram-automator-next，修掉官方 SDK 在新 DevTools / Node 上的两处坑。"
tech: ["微信小程序", "Node.js", "自动化测试", "AI Agent", "开源"]
status: "开源 · MIT · npm 已发布"
github: "https://github.com/Zi-Yi-Ming/miniprogram-auto-test"
---

微信小程序的自动化测试很难写：官方的 `miniprogram-automator` 是裸 SDK，每个用例都要手写「选元素、点击、断言」，而且 2023-11 之后就没再更新。这个项目做了两件事：

- **skill**：一个 Claude Code skill，让 AI 读懂页面的 WXML + JS，按一句话需求生成能直接跑的 `*.test.js`
- **miniprogram-automator-next**：[npm 包](https://www.npmjs.com/package/miniprogram-automator-next)（v0.1.1，已发布），官方 SDK 的适配层，修了两处实测坏掉的东西

两个实测结论（DevTools 2.01 / 基础库 3.17 / Node v24 / Windows 11）：

1. 官方文档主推的 `Page.*` 命令族（`page.$()` / `setData` / `callMethod` 等）在新版开发者工具上**整族超时失效**，只能靠 `miniProgram.evaluate()` 跑运行时代码——修复包把元素层整个重建在 `evaluate` 之上
2. Node ≥18.20 修掉 CVE-2024-27980（BatBadBut）后，官方 Launcher `spawn()` 一个 `.bat` 会直接抛 `EINVAL`，还把它错报成「cliPath 路径错误」——修复包改为直接 spawn 同目录的 `node.exe`，绕开 `.bat`，也不需要重新打开 `shell:true` 那个注入面

仓库里配了 CI、smoke 测试和 skill 的 evals 评测套件。
