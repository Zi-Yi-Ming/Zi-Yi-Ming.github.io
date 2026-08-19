---
title: '微信小程序云托管 Spring Boot 登录失败排查：Docker CA 证书导致 SSLHandshakeException'
date: 2026-08-03
draft: false
description: '本地正常、云端 502：Docker 容器缺少 CA 证书与 Java trustStore 配置导致 HTTPS 握手失败的完整排查。'
externalUrl: 'https://blog.csdn.net/2402_87488142/article/details/163451759'
tags: ["微信小程序", "Spring Boot", "Docker", "SSL"]
---

> 原文发布在 [CSDN](https://blog.csdn.net/2402_87488142/article/details/163451759)。

微信小程序登录接口部署到云托管后出现 502，本地却一切正常。通过分析发现是 Docker 容器缺少 CA 证书和 Java trustStore 配置导致 HTTPS 握手失败，修复方案包括：Dockerfile 安装系统 CA 证书、同步 Java 信任库、显式指定 JVM 信任库路径。
