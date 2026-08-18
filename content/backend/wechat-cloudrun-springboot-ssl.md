---
title: '微信小程序云托管 Spring Boot 登录失败排查：Docker CA 证书导致 SSLHandshakeException'
date: 2026-08-03
draft: false
description: 'HTTPS 请求并不是直接发送 HTTP 数据，而是先建立可信的 TLS 加密连接。'
tags: ["微信小程序", "Spring Boot", "Docker", "SSL", "云托管"]
categories: ["前后端"]
---

> 本文原发布于 [CSDN](https://blog.csdn.net/2402_87488142)，迁移自个人博客。

### 二、SSLHandshakeException 到底是什么？


HTTPS 请求并不是直接发送 HTTP 数据，而是先建立可信的 TLS 加密连接。





本质不是“微信接口不通”，而是：


> Java 容器无法确认微信服务器证书链是否可信，因此拒绝建立 HTTPS 连接。


本地电脑与云端容器的证书环境不同，是这类问题常见的原因。精简运行镜像中，系统 CA、Java CA 信任库及二者同步关系可能不完整或不一致。


---


### 三、真实排查过程：从 TLS 握手失败到微信业务错误


这次排查过程很有代表性：





修复证书后，日志变成：


```text
WeChat code2Session returned errcode=40163

```


这个错误并不表示证书修复失败。`40163` 表示微信登录临时 `code` 已经使用过。


这反而说明 HTTPS 请求已经成功到达微信服务器，问题从“网络/TLS 层”进入了“微信业务层”。


处理方式是重新调用：


```ts
wx.login()

```


拿到新的临时 code 后再次登录。


---


### 四、Dockerfile 修复方案


我的后端运行时镜像使用 Java 17：


```dockerfile
FROM eclipse-temurin:17-jre

```


修复后，在运行时镜像中加入：


```dockerfile
FROM maven:3.9.9-eclipse-temurin-17 AS build

WORKDIR /workspace

COPY pom.xml ./
RUN mvn -B -q -DskipTests dependency:go-offline

COPY src ./src
RUN mvn -B -q -DskipTests package

FROM eclipse-temurin:17-jre

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       ca-certificates-java \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_TOOL_OPTIONS="-Djavax.net.ssl.trustStore=/etc/ssl/certs/java/cacerts"

WORKDIR /app
COPY --from=build /workspace/target/*.jar /app/app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app/app.jar"]

```


完整含义如下：


 | 
 | 配置 |  | 作用 |  | 
 | `ca-certificates` |  | 安装 Linux 系统可信根证书 | 
 | `ca-certificates-java` |  | 将系统证书同步为 Java 可识别的信任库 | 
 | `update-ca-certificates` |  | 更新系统证书与 Java 证书库 | 
 | `JAVA_TOOL_OPTIONS` |  | 显式指定 JVM 使用的 trustStore 路径 |

镜像结构可以理解为：





---


### 五、为什么只安装 ca-certificates 还不够？


一开始我只考虑安装系统证书：


```dockerfile
apt-get install -y ca-certificates

```


但 Java 发起 HTTPS 请求时，主要依赖 JVM 的信任库，而不是一定直接读取 Linux 系统的 PEM 证书文件。


因此更稳妥的链路是：


```text
Linux 系统 CA 证书
        ↓
ca-certificates-java 同步
        ↓
Java cacerts 信任库
        ↓
Java HttpClient 校验微信 HTTPS 证书

```


所以最终需要同时完成：


```text
ca-certificates
+ ca-certificates-java
+ update-ca-certificates
+ 指定 JVM trustStore

```


---


### 六、针对确认属于偶发握手失败场景增加有限重试


证书环境修复后，我还给微信 `code2Session` 请求增加了轻量保护：


```text
首次出现 TLS 握手异常
        ↓
等待 250ms
        ↓
重试一次
        ↓
仍失败则返回“微信登录服务暂不可用”

```


这里的重点是：


- 只对 TLS 握手异常重试；
- 只重试一次；
- 不无限重试；
- 不记录 AppSecret、完整请求 URL 等敏感信息。


重试只是提升偶发网络抖动下的成功率，不能替代正确的证书配置。


---


### 七、修复前后对比


 | 
 | 项目 |  | 修复前 |  | 修复后 |  | 
 | 容器证书环境 |  | 未显式准备 |  | 安装系统 CA 与 Java CA | 
 | Java trustStore |  | 使用默认行为 |  | 显式指定 `/etc/ssl/certs/java/cacerts` | 
 | 微信 HTTPS 调用 |  | `SSLHandshakeException` |  | 能到达微信业务接口 | 
 | 后续报错 |  | TLS 失败 |  | 可识别 `40163` 等微信业务错误 | 
 | 最终登录 |  | 失败 |  | 获取 openid 并签发 JWT |

---


### 八、常见错误与正确处理方式


 | 
 | 现象 |  | 可能原因 |  | 正确处理 |  | 
 | `SSLHandshakeException` |  | 容器 CA / Java trustStore 异常 |  | 修复 Docker 镜像证书环境 | 
 | `40125` |  | AppSecret 配置错误 |  | 仅在云端环境变量中检查配置 | 
 | `40163` |  | 登录 code 已被使用 |  | 重新执行 `wx.login()` 获取新 code | 
 | `40029` |  | code 无效 |  | 检查前端传参并重新登录 | 
 | `/api/hello` 正常但登录失败 |  | 容器能启动，不代表能访问微信 HTTPS |  | 必须实际验证登录链路 |

不要采用以下做法：


- 关闭 SSL 校验；
- 跳过 HTTPS 主机名校验；
- 将 AppSecret 写入 Dockerfile；
- 在日志中输出完整微信请求 URL；
- 看到 `40163` 后反复提交同一个 code。


---


### 九、如何验证修复成功？


不要只测试：


```text
GET /api/hello

```


它只能证明 Spring Boot 已启动。


正确验证步骤：


- 推送 Dockerfile 修改，等待云托管重新构建部署；
- 在微信开发者工具重新编译小程序；
- 清除本地登录态或点击“重新登录”；
- 触发新的 `wx.login()`；
- 查看云端日志，确认不再出现 `SSLHandshakeException`；
- 确认后端成功返回登录结果，小程序进入正常页面。


最终链路如下：





---


### 十、总结


这次问题并不是微信接口不可用，而是云托管 Docker 容器中 Java HTTPS 信任链配置不完整或不一致。


最终解决方案：


```text
系统 CA 证书
+ Java CA 证书同步
+ 更新证书库
+ 显式指定 JVM trustStore
+ TLS 异常有限重试

```


这类问题不仅会出现在微信登录中。只要 Java Docker 容器需要访问 AI 服务、对象存储、支付接口或其他 HTTPS 第三方服务，都值得提前检查 CA 与 Java trustStore 配置。


### 十一、这次踩坑得到的经验


-  
本地正常 ≠ Docker环境正常

-  
HTTP接口正常 ≠ HTTPS第三方调用正常

-  
SSL错误不要第一时间关闭校验

-  
业务错误码出现，反而说明网络链路已经恢复
