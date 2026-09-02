---
title: "vLLM Semantic Router 上游贡献"
date: 2026-09-02
weight: 5
description: "给 vllm-project/semantic-router（5.5k★）合入的 PR：让 install.sh 识别已装的 Podman 而不是重复装 Docker，运行时写入 runtime.env 自动生效。目前 DE 组成员申请中。"
tech: ["vLLM", "Shell", "容器", "开源贡献"]
status: "上游已合并 · DE 组申请中"
---

给 [vLLM Semantic Router](https://github.com/vllm-project/semantic-router)（vLLM 生态的模型路由层，5.5k★）提的修复：它的 `install.sh` 只检测 Docker，机器上明明已经装好 Podman，安装脚本还是会再装一套 Docker——和代码里把 Podman 当一等公民的 `container_runtime.py` 自相矛盾。

提交的 [PR #3294](https://github.com/vllm-project/semantic-router/pull/3294)（承接 [issue #3286](https://github.com/vllm-project/semantic-router/issues/3286)，wg/developer-experience-ecosystem 认领）做了三件事：

- 新增 `podman_ready()`，`detect_existing_runtime()` 现在能识别已装的 Podman
- 检测到 Podman 时跳过 Docker 安装
- 把检测到的运行时写入 `runtime.env`，`vllm-sr serve` 自动拾取

2026-09-02 由维护者 Xunzhuo 合并进 `vllm-project:main`（6 个 commits，含完整 Test Plan），目前正在申请该组（Developer Experience & Ecosystem）的成员资格。
