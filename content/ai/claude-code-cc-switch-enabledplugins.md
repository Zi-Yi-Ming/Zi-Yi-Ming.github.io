---
title: 'Windows下Claude Code插件消失？CC Switch无法保留 enabledPlugins 的排查与修复'
date: 2026-08-09
draft: false
description: '最近在 Windows 上使用 Claude Code，并通过 CC Switch 配置自定义模型和本地路由。'
tags: ["Claude Code", "CC Switch", "插件", "Windows", "排错"]
categories: ["人工智能"]
---

> 本文原发布于 [CSDN](https://blog.csdn.net/2402_87488142)，迁移自个人博客。

### 一、问题背景


最近在 Windows 上使用 Claude Code，并通过 CC Switch 配置自定义模型和本地路由。


安装 Claude Code 官方插件后，第一次使用一切正常，但重启 CC Switch 本地路由后，之前安装的官方插件又全部“消失”了。


奇怪的是，手动安装到：


```text
~/.claude/skills/ui-ux-pro-max

```


下的 Skill 一直可以正常使用。


经过排查后发现：


> 插件文件没有丢失，GitHub 也没有问题，结合本次环境和复现结果，最终确认问题出在 CC Switch 通用配置没有正确保留/注入 `enabledPlugins`。


---


### 二、开发环境


- Windows11
- Claude Code：2.1.225
- CC Switch：3.16.3（开启本地路由）
- Git：2.50.0.rc1.windows.1
- Node.js：v24.12.0
- npm：11.6.2


官方插件包括：


```text
frontend-design
superpowers
code-review
context7
skill-creator
code-simplifier
github
···

```


正常情况下，在 Claude Code 中执行：


```text
/plugin

```


即可查看已安装插件。


---


### 三、问题表现


#### 1. 第一次安装插件


插件可以正常下载并使用。


#### 2. 重启 Claude Code


如果只是关闭并重新打开 Claude Code，插件仍然存在。


#### 3. 重启 CC Switch 本地路由


问题出现：执行 `/plugin` 后，官方插件无法正常加载，看起来像是没有安装。


但是检查本地文件后发现：


- 插件目录仍然存在；
- 插件安装记录仍然存在；
- Marketplace 目录仍然存在。


---


### 四、检查插件目录


首先检查插件缓存目录：


```powershell
Get-ChildItem "$env:USERPROFILE\.claude\plugins\cache\claude-plugins-official" -Directory

```


可以看到：


![图片](https://i-blog.csdnimg.cn/direct/3614bee4e9f74fb1873dff7039d42498.png)


再检查插件安装记录：


```powershell
Get-Content "$env:USERPROFILE\.claude\plugins\installed_plugins.json"

```


*此处只展示部分记录：*


![图片](https://i-blog.csdnimg.cn/direct/f4338b22d43344f1b0e0ac14b74ce351.png)


这说明：


```text
插件文件存在
        ↓
安装记录存在
        ↓
Claude Code 启动
        ↓
插件没有被正确启用

```


因此问题不是插件被删除，而更像是插件加载配置没有生效。


---


### 五、检查 Marketplace


Claude Code 官方插件来自：


```text
anthropics/claude-plugins-official

```


检查 Marketplace 配置：


```powershell
Get-Content "$env:USERPROFILE\.claude\plugins\known_marketplaces.json"

```


![图片](https://i-blog.csdnimg.cn/direct/638e4d800f2444d58835b44cfbe05a86.png)


检查目录是否存在：


```powershell
Test-Path "$env:USERPROFILE\.claude\plugins\marketplaces\claude-plugins-official"

```


返回：`true`


![图片](https://i-blog.csdnimg.cn/direct/f799a29e467745e8b0d7cf5ade69d120.png)


说明 Marketplace 本身没有丢失。


---


### 六、排查 GitHub 网络问题


由于之前遇到过：


```text
Failed to clone marketplace repository
fatal: unable to access github.com

```


所以一开始怀疑是 GitHub 网络问题。


测试 GitHub：


```powershell
curl.exe -I https://github.com

```


测试 Git：


```powershell
git ls-remote https://github.com/anthropics/claude-plugins-official.git HEAD

```


如果能正常返回 commit：


```text
ef0067b219f80fa33dc9b6e2f290906d45f5e351        HEAD

```


则可以基本排除当前环境下的：


- GitHub 服务不可访问；
- Git HTTPS 连接失败；
- Git 网络环境配置导致的访问失败。


---


### 七、检查 CC Switch 本地路由


由于问题发生在 CC Switch 本地路由重启之后，因此接下来检查 CC Switch 的网络配置。


这里有一个比较容易产生误判的地方。


CC Switch 的设置中存在「全局出站网络转发」配置项，例如：


![图片](https://i-blog.csdnimg.cn/direct/2bf36940987e422d8d4becfcb25c35af.png)


需要注意的是，截图中的：


```text
http://127.0.0.1:xxxx / ://127.0.0.1:xxxx

```


只是网络配置示例，并不代表 CC Switch 本地路由一定使用这两个端口。


本次排查时，我的全局出站网络配置实际上是留空状态，因此相关外部网络请求使用的是直连，并没有经过额外的网络中转。


为了排除"本地路由占用这些端口"的误判，可以检查相关端口是否正在监听：


```powershell
Test-NetConnection 127.0.0.1 -Port xxxx
Test-NetConnection 127.0.0.1 -Port xxxx

```


本次测试结果：


![图片](https://i-blog.csdnimg.cn/direct/786d6775e34942bb99c196bf5470db17.png)


相关端口均无法连接。


但这并不能说明 CC Switch 本地路由异常，因为这里检查的是全局出站网络中转所使用的端口，而不是 CC Switch 本地路由本身的监听端口。同时，本地路由本身运行正常，外部请求可正常转发。


同时，通过前面的 GitHub 测试：


```powershell
git ls-remote https://github.com/anthropics/claude-plugins-official.git HEAD

```


可以正常获取：


```text
ef0067b219f80fa33dc9b6e2f290906d45f5e351        HEAD

```


因此可以确认，在本次环境下：


- CC Switch 全局出站网络配置为空；
- 外部网络请求使用直连；
- 相关端口没有监听属于正常现象；
- GitHub 可以正常访问；
- 插件缓存和插件安装记录均存在。


所以可以进一步排除网络中转配置和 GitHub 网络连接导致插件消失的可能。


> **注意**：CC Switch 的「本地路由」与「全局出站网络配置」是两个不同层面的配置。全局出站网络配置留空，并不代表本地路由没有运行；同样，相关端口没有监听，也不能直接说明 CC Switch 本地路由异常。


---


### 八、最终定位：`enabledPlugins` 未正确配置


经过前面排查已确认本地文件与网络均无异常，接下来检查 CC Switch 的 Claude Code 通用配置。通过对比修改前后的表现并进行重启复现，确认问题出在 **`enabledPlugins`** 没有被正确保留。


第一次安装后插件能够使用，说明安装过程中 Claude Code 可能通过会话级机制启用了这些插件；但 CC Switch 重启本地路由后，通用配置中的 `enabledPlugins` 未被持久化保留，导致插件失效。


解决方式是在通用配置中加入：


```json
{
  "enabledPlugins": {
    "frontend-design@claude-plugins-official": true,
    "superpowers@claude-plugins-official": true,
    "code-review@claude-plugins-official": true,
    "context7@claude-plugins-official": true,
    "skill-creator@claude-plugins-official": true,
    "code-simplifier@claude-plugins-official": true,
    "github@claude-plugins-official": true
  }
}

```


如果原本已经存在其他配置，**不要直接覆盖原配置**，而是将 `enabledPlugins` 合并进去：


```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "...",
    "ANTHROPIC_BASE_URL": "...",
    "ANTHROPIC_MODEL": "..."
  },
  "model": "opus",
  "enabledPlugins": {
    "frontend-design@claude-plugins-official": true,
    "superpowers@claude-plugins-official": true,
    "code-review@claude-plugins-official": true,
    "context7@claude-plugins-official": true,
    "skill-creator@claude-plugins-official": true,
    "code-simplifier@claude-plugins-official": true,
    "github@claude-plugins-official": true
  }
}

```


配置完成后：


- 重启 CC Switch；
- 重启 Claude Code；
- 执行：


```text
/plugin

```


确认官方插件已经恢复。


然后可以再次重启 CC Switch 本地路由进行验证。如果重启后官方插件仍然可以正常加载，说明问题已经得到彻底解决。


---


### 九、为什么 ui-ux-pro-max 没有受到影响？


我手动安装的是：


```text
C:\Users\Lenovo\.claude\skills\ui-ux-pro-max

```


这个目录与官方插件属于两种不同的管理方式。


#### Claude Code 插件提供的 Skill


```text
Plugin
  ↓
Marketplace
  ↓
Plugin
  ↓
Skills

```


例如：`frontend-design`、`superpowers` 等，它们依赖 Claude Code 插件系统和 `enabledPlugins` 配置。


#### 独立 Skill 目录


```text
~/.claude/skills/ui-ux-pro-max/SKILL.md

```


它属于 Claude Code 的独立 Skill 目录，不依赖：


- `claude-plugins-official`
- Marketplace
- `enabledPlugins`


所以 CC Switch 重启本地路由后：


```text
官方插件 Skill
        ↓
可能没有启用

独立 Skill
        ↓
仍然正常加载

```


这就是两者表现不同的原因。


---


### 十、不要把插件缓存直接复制到 skills


排查过程中，可能会想到把插件缓存目录复制到：


```text
~/.claude\skills

```


例如：


```text
~/.claude\skills\frontend-design
~/.claude\skills\superpowers

```


**不建议这样做。**


官方插件通常具有类似结构：


```text
frontend-design
└── 
    └── skills
        └── frontend-design
            └── SKILL.md

```


它与普通的：


```text
~/.claude\skills\\SKILL.md

```


并不是完全相同的管理机制。更重要的是，Claude Code 的插件系统依赖 `installed_plugins.json` 的注册记录和 `enabledPlugins` 的启用配置，单纯复制文件不会被插件系统识别。


正确做法是：


> 让 Claude Code 插件系统管理官方插件，而不是手动复制插件缓存。


---


### 十一、完整验证流程 (SOP)


#### 1. 检查插件缓存


```powershell
Get-ChildItem "$env:USERPROFILE\.claude\plugins\cache\claude-plugins-official" -Directory

```


#### 2. 检查安装记录


```powershell
Get-Content "$env:USERPROFILE\.claude\plugins\installed_plugins.json"

```


#### 3. 检查 Marketplace


```powershell
Get-Content "$env:USERPROFILE\.claude\plugins\known_marketplaces.json"

```


#### 4. 检查 enabledPlugins


确认 CC Switch 通用配置中包含：


```json
"enabledPlugins": {
  "frontend-design@claude-plugins-official": true,
  "superpowers@claude-plugins-official": true,
  "code-review@claude-plugins-official": true,
  "context7@claude-plugins-official": true,
  "skill-creator@claude-plugins-official": true,
  "code-simplifier@claude-plugins-official": true,
  "github@claude-plugins-official": true
}

```


#### 5. 重启并验证


依次执行：


```text
重启 CC Switch
重启 Claude Code
/plugin

```


然后再重启一次 CC Switch 本地路由，确认插件仍然存在。


---


### 十二、排错思路总结


这次问题可以拆分成四层：


```text
网络层
  ↓
GitHub 能否访问

Marketplace 层
  ↓
官方插件仓库是否存在

插件安装层
  ↓
插件缓存和安装记录是否存在

插件启用层
  ↓
enabledPlugins 是否正确

```


以下操作**都不是根治方案**：


- 反复重新安装插件；
- 重新 clone Marketplace；
- 强制 reload plugins；
- 手动复制插件缓存目录。


真正需要修复的是：


> CC Switch 通用配置中的 `enabledPlugins`。


---


### 十三、最终结论


如果在 Windows + CC Switch + Claude Code 环境中遇到 `/plugin` 显示官方插件加载失败，或者重启 CC Switch 本地路由后插件消失，**不要第一时间重复安装**。


建议按以下顺序排查：


```text
/plugin
  ↓
检查 GitHub 网络
  ↓
检查插件缓存
  ↓
检查 installed_plugins.json
  ↓
检查 known_marketplaces.json
  ↓
检查 enabledPlugins
  ↓
重启 CC Switch
  ↓
重启 Claude Code
  ↓
再次执行 /plugin

```


这次问题的根因是：


> 插件没有丢失，GitHub 没有问题，Marketplace 也没有损坏，结合本次环境和复现结果，最终确认问题是 CC Switch 通用配置中的 **`enabledPlugins`** 没有被正确保留。


添加 `enabledPlugins` 后，重启 CC Switch 本地路由也能够保持插件正常加载。


---


### 十四、踩坑总结


这次排查过程中有几个比较容易误判的地方：


- **插件文件存在 ≠ 插件一定会被加载**
 `installed_plugins.json` 和插件缓存都存在，只能说明插件已经安装，不能说明当前 Claude Code 会话一定启用了这些插件。
- **`/reload-plugins --force` 不是根治方案**
 如果底层的 `enabledPlugins` 配置没有正确保留，重新加载只能暂时解决当前会话的问题。
- **常见网络中转端口（如xxxx等）不是 CC Switch 本地路由端口**
 无论全局出站网络中转是否配置，这些端口都不属于 CC Switch 本地路由本身的监听端口，因此不能据此判断本地路由异常。
- **不要看到插件消失就重新安装**
 如果插件缓存、`installed_plugins.json` 和 Marketplace 都还存在，优先检查插件启用配置。
- **独立 Skill 和插件 Skill 是两套机制**
 `~/.claude/skills` 下的 Skill 与 Marketplace 插件不完全相同，因此一个正常并不能证明另一个也一定正常。
