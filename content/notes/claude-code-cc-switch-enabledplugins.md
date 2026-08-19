---
title: 'Windows下Claude Code插件消失？CC Switch无法保留 enabledPlugins 的排查与修复'
date: 2026-08-09
draft: false
description: 'Windows 上使用 CC Switch 配置 Claude Code，重启本地路由后官方插件全部消失的排查与修复。'
externalUrl: 'https://blog.csdn.net/2402_87488142/article/details/163611151'
tags: ["Claude Code", "CC Switch", "Windows", "排错"]
---

> 原文发布在 [CSDN](https://blog.csdn.net/2402_87488142/article/details/163611151)。

Windows 上使用 Claude Code + CC Switch 时，重启本地路由会导致官方插件"消失"。排查发现插件文件与安装记录都正常，问题根源是 CC Switch 通用配置中的 `enabledPlugins` 字段未被正确持久化，手动合并该字段即可彻底解决。
