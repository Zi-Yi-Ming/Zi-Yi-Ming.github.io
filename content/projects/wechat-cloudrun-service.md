---
title: "微信小程序云托管服务"
date: 2026-08-21
weight: 30
description: "基于微信云托管部署的 Spring Boot 后端服务：登录鉴权、开放接口调用，踩过 Docker CA 证书、HTTPS 握手、云调用鉴权等一系列坑，全流程梳理成排错笔记。"
tech: ["Spring Boot", "微信云托管", "Docker", "HTTPS"]
status: "线上运行"
csdn: "https://blog.csdn.net/2402_87488142/article/details/163927946"
---

用微信云托管部署 Spring Boot 服务，为小程序提供后端接口，处理登录鉴权与开放接口调用。

- 迁移后接口全报「内容含违规信息」：根因是旁挂组件改写调用规则，改用 HTTP 云调用免鉴权 + `X-WX-OPENID` 头登录完成重构
- Docker 容器缺 CA 证书导致 `SSLHandshakeException`：补齐 Java trustStore 配置解决
- 排错记录：[迁移排查](https://blog.csdn.net/2402_87488142/article/details/163927946) · [SSL 握手排查](https://blog.csdn.net/2402_87488142/article/details/163451759)
