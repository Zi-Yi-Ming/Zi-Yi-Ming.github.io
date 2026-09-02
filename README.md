# Zi-Yi-Ming · 个人作品集

个人作品集站点，基于 **Hugo + PaperMod 主题**自定制「inkline 纸墨编辑风」设计系统，托管在 **GitHub Pages**（免费，无需自定义域名），由 GitHub Actions 自动构建部署。

## 克隆与初始化

> ⚠️ 主题是 git submodule，**必须带 `--recurse-submodules` 克隆**，否则构建会静默降级（缺主题模板，搜索页 `index.json` 不生成、页面样式丢失）。已经克隆过的补一句 `git submodule update --init --recursive` 即可。

```bash
git clone --recurse-submodules https://github.com/Zi-Yi-Ming/Zi-Yi-Ming.github.io.git
```

## 目录结构

```
├── hugo.toml                 # 站点配置（标题、菜单、主题参数）
├── content/
│   ├── projects/             # 项目页（作品集核心）
│   ├── notes/                # 笔记（摘要 + CSDN 外链）
│   ├── about.md              # 关于页面
│   ├── toolbox.md            # 自用清单
│   └── search.md             # 搜索页面
├── layouts/                  # 主题模板覆盖（首页、列表页、og 标签等）
├── assets/css/extended/      # 主题定制样式（inkline 配色、首页布局）
├── static/                   # 站点图标、默认 og 图、自托管标题字体（static/fonts）
├── i18n/                     # 中文本地化文案
└── themes/papermod/          # 主题（git submodule）

> 标题用 Noto Serif SC 子集字体（`static/fonts/`，由 `scripts/subset-fonts.py` 按站内文字生成）。新增文章含新汉字时，`py -3 scripts/subset-fonts.py <NotoSerifSC.ttf>` 重跑即可。
```

## 写文章

- **项目页**：在 `content/projects/` 下新建 `.md`（front matter 可含 `tech`、`status`、`github`/`csdn` 外链字段）。
- **笔记**：在 `content/notes/` 下新建 `.md`；完整文章在 CSDN，本站放摘要，用 `externalUrl` 指向原文。

```markdown
---
title: "文章标题"
date: 2026-08-18
tags: ["标签1", "标签2"]
description: "摘要，会显示在列表页"
---
```

## 本地预览

```bash
hugo server          # 浏览器打开 http://localhost:1313
```

## 发布

推送到 `main` 分支即可，`.github/workflows/hugo.yaml` 会自动构建并部署到 GitHub Pages（约 1 分钟后生效）。

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
