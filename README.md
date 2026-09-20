# Zi-Yi-Ming · 个人作品集

个人作品集站点，基于 **Hugo + PaperMod 主题**自定制「Night Archive 暗色档案风」设计系统，托管在 **GitHub Pages**（免费，无需自定义域名），由 GitHub Actions 自动构建部署。另镜像到 Gitee。

## 克隆与初始化

```bash
git clone --recurse-submodules https://github.com/Zi-Yi-Ming/Zi-Yi-Ming.github.io.git
```

## 站点特性

- **Night Archive 设计系统**：暗色档案库 + editorial 排版、紫色 accent、像素夜景背景层（星点/月亮/雾气，见 `layouts/partials/bg.html`）；CSS Variables 驱动，亮色主题 token 已预留、暂未开放
- **档案式首页**：身份区 + Selected Works / Recent Notes 双栏编号索引 + About 摘要（`layouts/index.html`）
- **搜索双通道**：`/search/` 页面（PaperMod fastsearch + Fuse）+ 全站 ⌘K/Ctrl+K 命令面板（`layouts/partials/cmdk.html`），均消费首页输出的 `index.json`
- **文章页三栏**：元信息 rail + 正文 + TOC（`layouts/_default/single.html`），无 JS 框架，图标内联 SVG
- **SEO**：og/twitter/JSON-LD 标签、sitemap、RSS、`hasCJKLanguage` 中文计数均已配置

## 目录结构

```
├── hugo.toml                 # 站点配置（标题、菜单、主题参数）
├── content/
│   ├── projects/             # 项目页（作品集核心；front matter 支持 featured/tech/status/github/csdn）
│   ├── notes/                # 笔记（摘要 + CSDN 外链，externalUrl 字段）
│   ├── about.md              # 关于页面
│   ├── toolbox.md            # 自用清单
│   └── search.md             # 搜索页面（layout: search）
├── layouts/                  # 主题模板覆盖（首页、列表页、og/twitter 标签、cmdk、sitemap 等）
├── assets/
│   ├── css/extended/         # 主题定制样式（Night Archive 设计系统，约 2100 行）
│   └── img/                  # 头像源图（Hugo 管线压缩为 webp 后发布）
├── static/
│   ├── bg/                   # 全站夜景背景图
│   ├── fonts/                # 自托管标题字体 Manrope（woff2）
│   └── *.png/*.ico/*.svg     # 站点图标、默认 og 图
├── i18n/                     # 中文本地化文案（仅保留实际使用的条目）
├── scripts/start-preview.cmd # Windows 双击本地预览（端口 1399）
└── themes/papermod/          # 主题（git submodule）
```

> 标题使用自托管 Manrope 字体（`static/fonts/manrope-latin.woff2`），中文回退系统字体；无字体生成脚本。

## 写文章

- **项目页**：在 `content/projects/` 下新建 `.md`（front matter 可含 `tech`、`status`、`github`/`csdn` 外链字段；`featured: N` 控制首页精选排序）。
- **笔记**：在 `content/notes/` 下新建 `.md`；完整文章在 CSDN，本站放摘要，用 `externalUrl` 指向原文。

```markdown
---
title: "文章标题"
date: 2026-08-18
tags: ["标签1", "标签2"]
description: "摘要，会显示在列表页"
---
```

> 内容维护约定：涉及版本号、测试数量等时效性数字时，注明「截至 YYYY-MM」，避免过期后误导。

## 本地预览

```bash
hugo server                                    # 浏览器打开 http://localhost:1313
start scripts\start-preview.cmd                # Windows 双击：http://localhost:1399（禁 live reload）
```

## 发布

推送到 `main` 分支即可，`.github/workflows/hugo.yaml` 会自动构建并部署到 GitHub Pages（约 1 分钟后生效）；`mirror-to-gitee.yml` 同步镜像到 Gitee。

```bash
git add . && git commit -m "..." && git push
```

## 常用命令

| 命令 | 说明 |
|------|------|
| `hugo new content projects/项目名.md` | 新建项目页草稿 |
| `hugo server` | 本地预览 |
| `hugo --gc --minify` | 本地生成生产构建到 `public/` |
| `git submodule update --init --recursive` | 克隆后初始化主题 |

## 主题更新

```bash
git submodule update --remote themes/papermod
```
