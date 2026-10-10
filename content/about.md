---
title: "About"
description: "AI Infra 与 Agent 开发：vLLM Semantic Router 核心贡献者（即将成为 Collaborator）、desktop-for-step-code 二号贡献者"
ShowReadingTime: false
ShowWordCount: false
hideAuthor: true
hideMeta: true
showToc: false
---

你好，我是 ZiY1Ming。

一个做 AI Infra 与 Agent 开发的软件工程开发者。方向已经收敛：往上是模型推理基础设施（vLLM Semantic Router），往下是 Agent 运行时与工具（桌面端、自动化）——前者是社区协作，后者是自己从 0 搭的东西。

## 关于本站

这里是作品集，记做过的项目、踩过的坑。完整的技术文章发在 [CSDN](https://blog.csdn.net/2402_87488142)，项目清单在[项目页](/projects/)。

内容不保证成体系。很多是某个问题折腾了很久之后留下的记录。比起写一篇“完美的教程”，我更希望这里能保留真实的过程，以后翻回来看，能想起当时是怎么一步步试过来的。

## 主线一：AI Infra —— vLLM Semantic Router

给 [vLLM Semantic Router](https://community.vllm-sr.ai/)（6k★ 开源项目）持续贡献上游代码：DE&E 组核心成员，即将以 Collaborator 身份进入维护团队；按 GitHub 贡献者榜，近三个月的提交量进入前 10（不计 merge 机器人）。方向集中在安装与容器运行时、官网与文档、Dashboard——代表作是让安装脚本识别已有 Podman 的 [#3294](https://github.com/vllm-project/semantic-router/pull/3294)，以及后续一组 runtime 改进。详情在[项目页](/projects/vllm-semantic-router-contribution/)。

## 主线二：Agent 开发 —— desktop-for-step-code

[desktop-for-step-code](https://github.com/7oMB2006/desktop-for-step-code) 是 Step Code 的社区 Windows 桌面客户端（Electron + React + TypeScript），我是两人团队的二号贡献者：43 个提交、21 个 PR 合入，主攻构建发布链路与 CI 一致性。同一条线上还有自己做的 [cnb-npc-skill](https://github.com/Zi-Yi-Ming/cnb-npc-skill)：把“派发任务 → 云端 AI 执行 → PR / 评审报告”压成一条命令，不占主力 Agent 的上下文——这是我对 Agent 自动化的理解方式。

## 更早的积累：量化研究

在 WorldQuant BRAIN 上做过相当长时间的 Alpha 研究：一万多次回测、50+ 因子、国内排名进过前 30。主业已经不在这，但它留给我一个习惯——任何想法都要回测完再下结论。

<div class="stat-strip" aria-label="量化研究数据">

<span class="stat-item"><strong>10,000+</strong> 次回测</span><span class="stat-item"><strong>50+</strong> 个 Alpha 因子</span><span class="stat-item">中国大陆最高排名 <strong>30+</strong></span>

</div>

## 当前关注

AI Infra 侧：模型决策层、推理路由、安装与容器运行时这类“让模型可靠跑起来”的工程链路。Agent 侧：运行时、桌面端、工具调用与自动化审批。两个方向的共同点——把 AI 能力变成基础设施，而不是 demo。

## 联系方式

<section class="contact-index" aria-label="联系方式">

<a class="contact-index__item" href="https://github.com/Zi-Yi-Ming" target="_blank" rel="noopener noreferrer">
  <span class="contact-index__icon" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg></span>
  <span class="contact-index__body">
    <span class="contact-index__label">GitHub</span>
    <span class="contact-index__value">ZiY1Ming</span>
  </span>
</a>

<a class="contact-index__item" href="https://blog.csdn.net/2402_87488142" target="_blank" rel="noopener noreferrer">
  <span class="contact-index__icon" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M4.693 13.638c-.497.568-1.363.63-1.712.63-.648 0-1.144-.164-1.474-.488-.313-.307-.478-.76-.489-1.346-.025-1.358.744-2.762 2.074-2.762.635 0 1.124.455 1.311.644a.337.337 0 0 0 .282.099.38.38 0 0 0 .241-.159c.068-.087.135-.237.138-.401s-.057-.344-.243-.49a2.642 2.642 0 0 0-1.668-.591c-.819 0-1.627.376-2.218 1.033-.621.691-.953 1.63-.935 2.646.015.815.282 1.5.773 1.982.528.518 1.3.791 2.235.791 1.097 0 1.776-.325 2.154-.597a.584.584 0 0 0 .24-.456.702.702 0 0 0-.208-.497c-.23-.248-.448-.101-.503-.037ZM9.663 11.488a7.471 7.471 0 0 0-.698-.248c-.157-.048-.309-.091-.45-.131-.922-.26-1.027-.5-1.017-.68.022-.363.515-.853 1.352-.792.607.045 1.015.509 1.205.781.149.214.371.135.434.095a.602.602 0 0 0 .309-.514.626.626 0 0 0-.209-.488 2.654 2.654 0 0 0-3.347-.273c-.456.323-.744.772-.77 1.202-.064 1.061 1.015 1.366 1.803 1.588.214.061.429.127.667.202 1.14.357 1.173.717 1.092 1.267-.082.556-.696.834-1.685.761-1.029-.076-1.464-.61-1.612-.901-.05-.098-.205-.248-.413-.156-.514.229-.473.731-.26.993.339.416 1.15 1.035 2.667 1.035 1.734 0 2.255-.875 2.378-1.64.092-.572-.022-1.028-.348-1.396-.236-.267-.592-.495-1.101-.706ZM16.44 9.323c-.598-.431-1.393-.61-2.36-.532-.712.058-1.274.243-1.335.263l-.006.002a.437.437 0 0 0-.297.379l-.47 5.201a.337.337 0 0 0 .247.35l.072.02.066.018.086.021a7.914 7.914 0 0 0 1.64.183c.972 0 1.765-.23 2.36-.684.764-.583 1.141-1.5 1.118-2.725-.021-1.135-.398-1.974-1.121-2.495Zm-.662 4.461c-.836.639-2.09.562-2.677.481a.128.128 0 0 1-.109-.137l.397-4.248a.113.113 0 0 1 .086-.1c.999-.241 1.777-.168 2.312.218.189.137.348.331.471.568.176.339.277.765.286 1.234.017.916-.24 1.583-.765 1.984ZM23.967 10.41a1.92 1.92 0 0 0-.432-.919c-.399-.465-1.029-.689-1.848-.689-.734 0-1.372.228-1.947.799.007-.086.019-.159.018-.223s-.017-.116-.066-.163c-.048-.045-.077-.067-.127-.077-.05-.01-.122-.008-.256-.006a.587.587 0 0 0-.589.54s-.325 3.874-.428 5.165a.308.308 0 0 0 .073.228.36.36 0 0 0 .26.131h.387a.224.224 0 0 0 .226-.205l.273-2.929.014-.147a1.902 1.902 0 0 1 .082-.412c.014-.045.03-.092.047-.14.245-.694.803-1.72 1.971-1.694.84.018 1.449.455 1.385 1.114-.101 1.034-.266 3.1-.358 4.14-.019.209.182.273.252.273h.304a.442.442 0 0 0 .444-.404s.185-2.127.294-3.352l.048-.532a1.959 1.959 0 0 0-.026-.5Z"/></svg></span>
  <span class="contact-index__body">
    <span class="contact-index__label">CSDN</span>
    <span class="contact-index__value">2402_87488142</span>
  </span>
</a>

<span class="contact-index__item contact-index__item--plain">
  <span class="contact-index__icon" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M21.395 15.035a40 40 0 0 0-.803-2.264l-1.079-2.695c.001-.032.014-.562.014-.836C19.526 4.632 17.351 0 12 0S4.474 4.632 4.474 9.241c0 .274.013.804.014.836l-1.08 2.695a39 39 0 0 0-.802 2.264c-1.021 3.283-.69 4.643-.438 4.673.54.065 2.103-2.472 2.103-2.472 0 1.469.756 3.387 2.394 4.771-.612.188-1.363.479-1.845.835-.434.32-.379.646-.301.778.343.578 5.883.369 7.482.189 1.6.18 7.14.389 7.483-.189.078-.132.132-.458-.301-.778-.483-.356-1.233-.646-1.846-.836 1.637-1.384 2.393-3.302 2.393-4.771 0 0 1.563 2.537 2.103 2.472.251-.03.581-1.39-.438-4.673"/></svg></span>
  <span class="contact-index__body">
    <span class="contact-index__label">QQ</span>
    <span class="contact-index__value">3125727661</span>
  </span>
</span>

<a class="contact-index__item" href="mailto:ziyim2026@gmail.com">
  <span class="contact-index__icon" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 21" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></span>
  <span class="contact-index__body">
    <span class="contact-index__label">Email</span>
    <span class="contact-index__value">ziyim2026@gmail.com</span>
  </span>
</a>

</section>
