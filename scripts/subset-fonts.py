#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成站内用到的 Noto Serif SC 子集字体（woff2），供首页/正文标题使用。

为什么：
  - Google Fonts 在国内不可达，@import 会阻塞渲染且观感随网络波动；
  - 自托管完整 CJK 字体体积过大（单字重 ~10MB+）；
  - 本博客文字量小，按「站内实际出现的字符 + 通用标点 + ASCII」做子集，
    单字重可压到几百 KB，设计观感与 Google Fonts 一致且永远可用。

用法：
  1. 准备源字体（Google Fonts 官方仓库的 Noto Serif SC 变量字体）：
       curl -L -o /tmp/notoserifsc.ttf \
         "https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/NotoSerifSC%5Bwght%5D.ttf"
  2. 运行本脚本（需要 python3 + fonttools + brotli）：
       py -3 scripts/subset-fonts.py /tmp/notoserifsc.ttf
  3. 输出 static/fonts/noto-serif-sc-w{600,700}.woff2

注意：新增文章含子集外的新字符时，重跑一次即可（脚本从 content/layouts/i18n 收集字形）。
"""
import os
import re
import sys

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAN_DIRS = ["content", "layouts", "i18n", "archetypes", "data"]
EXTRA_FILES = ["hugo.toml"]
# 通用中文标点/全角符号（即使当前正文没出现也保留，避免排版意外缺字）
COMMON_PUNCT = "，。、；：？！《》〈〉【】（）「」『』“”‘’—…·～　﹒．,.;:!?()[]{}<>-_*#&@$%+=\\/|~^`'\""

RE_WS = re.compile(r"\s")


def collect_chars() -> str:
    chars = set(COMMON_PUNCT)
    files = []
    for d in SCAN_DIRS:
        base = os.path.join(REPO, d)
        if not os.path.isdir(base):
            continue
        for root, _dirs, names in os.walk(base):
            for n in names:
                if n.endswith((".md", ".html", ".yaml", ".yml", ".toml", ".json")):
                    files.append(os.path.join(root, n))
    for f in EXTRA_FILES:
        p = os.path.join(REPO, f)
        if os.path.isfile(p):
            files.append(p)
    for f in files:
        try:
            with open(f, encoding="utf-8") as fh:
                chars.update(RE_WS.sub("", fh.read()))
        except (OSError, UnicodeDecodeError):
            pass
    return "".join(sorted(chars))


def main() -> None:
    src = sys.argv[1] if len(sys.argv) > 1 else "/tmp/notoserifsc.ttf"
    out_dir = os.path.join(REPO, "static", "fonts")
    os.makedirs(out_dir, exist_ok=True)
    text = collect_chars()
    print(f"charset size: {len(text)} unique chars")

    for wght in (600, 700):
        font = TTFont(src, lazy=True)
        print(f"instancing wght={wght} ...")
        instantiateVariableFont(font, {"wght": wght}, inplace=True)
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.hinting = False
        opts.desubroutinize = True
        opts.name_IDs = ["*"]
        opts.name_legacy = True
        opts.name_languages = ["*"]
        opts.layout_features = ["*"]
        opts.notdef_outline = True
        opts.recalc_bounds = True
        subsetter = subset.Subsetter(options=opts)
        subsetter.populate(text=text)
        print(f"subsetting wght={wght} ...")
        subsetter.subset(font)
        out = os.path.join(out_dir, f"noto-serif-sc-w{wght}.woff2")
        font.save(out)
        size = os.path.getsize(out) / 1024
        print(f"saved {out} ({size:.0f} KB)")
        font.close()


if __name__ == "__main__":
    main()
