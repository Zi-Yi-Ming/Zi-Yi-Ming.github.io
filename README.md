# 我的博客

个人静态博客，基于 **Hugo + PaperMod 主题**，托管在 **GitHub Pages**（免费，无需自定义域名）。

## 目录结构

```
myblog/
├── hugo.toml            # 站点配置（标题、菜单、主题参数）
├── assets/css/extended/ # 主题定制样式（配色、字体）
├── content/
│   ├── posts/           # 文章目录，写 Markdown 放这里
│   ├── search.md        # 搜索页面
│   └── about.md         # 关于页面
└── themes/papermod/     # 主题（git submodule）
```

## 写文章

在 `content/posts/` 下新建 `.md` 文件（参考 `hello-world.md` 的格式）：

```markdown
---
title: "文章标题"
date: 2026-08-18
tags: ["标签1", "标签2"]
---

正文内容，支持标准 Markdown。
```

## 本地预览

```bash
hugo server
# 浏览器打开 http://localhost:1313
```

## 发布到 GitHub Pages

> ⚠️ 第一步先做：把 `hugo.toml` 里的 `baseURL` 改成你的地址
> `https://你的GitHub用户名.github.io/`

### 方式一：GitHub Actions 自动构建（推荐）

1. 在 GitHub 新建仓库，命名为 `你的用户名.github.io`（必须是这个名字），选 Public；
2. 在本地推送：

   ```bash
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/你的用户名/你的用户名.github.io.git
   git push -u origin main
   ```

3. 到仓库 **Settings → Pages → Build and deployment**，把 **Source** 选成 **GitHub Actions**；
4. 在仓库新建文件 `.github/workflows/hugo.yaml`，内容用 Hugo 官方部署模板（仓库里放一份也可以，见下方步骤 5）；
5. 更简单的方式：本地执行 `hugo` 生成 `public/` 目录，然后 **Settings → Pages → Source 选 "Deploy from a branch" → 分支选 main → 目录选 /docs**，把 `public` 内容拷贝到 `docs/` 再推送。

### 方式二：直接推 public（最简单）

```bash
hugo          # 生成 public/ 目录
git add . && git commit -m "deploy" && git push
```

然后 Settings → Pages → Source 选 **Deploy from a branch**，分支选 `main`，目录选 `/ (root)` 或 `/docs`。

> 推上去后等 1~10 分钟，访问 `https://你的用户名.github.io/` 就能看到你的博客。

## 常用命令

| 命令 | 说明 |
|------|------|
| `hugo new content posts/文章名.md` | 新建文章草稿 |
| `hugo server` | 本地预览 |
| `hugo` | 生成静态文件到 public/ |
| `git submodule update --init --recursive` | 克隆后初始化主题 |

## 主题更新

```bash
git submodule update --remote themes/papermod
```
