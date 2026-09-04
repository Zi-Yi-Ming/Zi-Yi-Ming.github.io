---
title: "本站 · Night Archive 个人网站"
date: 2026-08-22
weight: 50
description: "这个网站本身：Hugo + PaperMod 深度定制的 Night Archive 设计——暗色档案库 + editorial 排版、紫色 accent、像素夜景背景语言，自定义 homepage 与项目/笔记档案页，GitHub Pages 自动部署。"
tech: ["Hugo", "PaperMod", "CSS", "SVG", "GitHub Pages"]
status: "持续迭代"
github: "https://github.com/Zi-Yi-Ming/Zi-Yi-Ming.github.io"
---

本站由 Hugo 静态站点生成器构建，在 PaperMod 之上做了深度自定义，视觉方向叫「Night Archive」：

- **Night Archive / dark archive**：全站按档案库组织——编号索引、细分隔线、editorial 排版；About / Toolbox 这类页面走 doc 档案模式，Projects / Notes 是连续编号的条目列表
- **日夜双主题，CSS Variables 驱动**：暗色是「夜晚开发者空间」——深蓝黑底、紫色 accent、像素夜空背景（星点、月亮）；亮色是清爽的白天工作台；两套共用同一套设计 token
- **像素夜景视觉语言**：直接取自头像场景（夜晚城市、月亮、星点、紫色），背景作为环境层存在，不做成装饰堆砌
- **首页与文章页全自定义布局**：homepage 是非对称的档案首页（身份区 + Selected Works / Recent Notes 索引 + About 摘要），文章页是三栏（元信息 rail + 正文 + TOC），无 JS 框架，图标内联 SVG
- GitHub Actions + GitHub Pages 自动构建部署
