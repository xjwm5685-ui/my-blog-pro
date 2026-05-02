"""
微信公众号文章批量转换脚本
HTML → Markdown + 图片迁移
"""

import os
import re
import shutil
from pathlib import Path
from bs4 import BeautifulSoup
import html2text

# 路径配置
EXPORT_DIR = Path("导出文章")
BLOG_DIR = Path("src/content/blog")
IMAGES_DIR = Path("public/images")

# 分类映射（根据关键词自动分类）
CATEGORY_KEYWORDS = {
    "tech": ["Python", "代码", "编程", "开发", "技术", "WSL", "Pycharm", "OpenClaw", "Hermes", "MIMO", "AI", "豆包", "断点", "调试"],
    "travel": ["游记", "旅行", "南昌", "绍兴", "重庆", "泰兰德", "夏天", "镜头"],
    "notes": ["笔记", "总结", "学习"],
}


def detect_category(title: str) -> str:
    """根据标题关键词自动检测分类"""
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in title:
                return category
    return "notes"  # 默认分类


def clean_filename(title: str) -> str:
    """将标题转为合法的文件名 slug"""
    # 移除特殊字符，保留中文、英文、数字、连字符
    slug = re.sub(r'[^\w一-鿿-]', '-', title)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug.lower()


def extract_article(html_path: Path) -> dict:
    """从 HTML 提取文章信息"""
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # 提取标题
    title_tag = soup.find("span", class_="js_title_inner")
    title = title_tag.get_text(strip=True) if title_tag else "未命名"

    # 提取日期
    date_tag = soup.find("em", id="publish_time")
    date_str = date_tag.get_text(strip=True) if date_tag else ""
    # 解析 "2025年11月17日 22:11" 格式
    date_match = re.search(r"(\d{4})年(\d{1,2})月(\d{1,2})日", date_str)
    if date_match:
        year, month, day = date_match.groups()
        pub_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    else:
        pub_date = "2025-01-01"

    # 提取正文
    content_div = soup.find("div", id="js_content")
    if not content_div:
        content_div = soup.find("div", class_="rich_media_content")

    return {
        "title": title,
        "pub_date": pub_date,
        "content_html": str(content_div) if content_div else "",
        "soup": soup,
    }


def convert_html_to_markdown(html_content: str) -> str:
    """将 HTML 正文转为 Markdown"""
    h = html2text.HTML2Text()
    h.body_width = 0  # 不自动换行
    h.protect_links = True
    h.unicode_snob = True
    h.wrap_links = False
    h.skip_internal_links = False

    md = h.handle(html_content)

    # 清理多余的空行
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def process_article(article_dir: Path) -> dict | None:
    """处理单篇文章"""
    html_path = article_dir / "index.html"
    assets_dir = article_dir / "assets"

    if not html_path.exists():
        return None

    # 提取文章信息
    article = extract_article(html_path)
    title = article["title"]
    pub_date = article["pub_date"]
    content_html = article["content_html"]

    if not content_html:
        return None

    # 转换为 Markdown
    markdown = convert_html_to_markdown(content_html)

    # 处理图片：复制到 public/images/ 并替换路径
    image_count = 0
    if assets_dir.exists():
        slug = clean_filename(title)
        for img_file in assets_dir.iterdir():
            if img_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"]:
                image_count += 1
                # 新文件名：slug-序号.扩展名
                new_name = f"{slug}-{image_count}{img_file.suffix}"
                dest_path = IMAGES_DIR / new_name

                # 复制图片
                shutil.copy2(img_file, dest_path)

                # 替换 Markdown 中的图片路径
                old_ref = f"./assets/{img_file.name}"
                new_ref = f"/images/{new_name}"
                markdown = markdown.replace(old_ref, new_ref)

                # 也处理 HTML 中可能的其他引用格式
                markdown = markdown.replace(img_file.name, new_name)

    # 生成 frontmatter
    category = detect_category(title)
    frontmatter = f"""---
title: '{title}'
description: '{title}'
pubDate: {pub_date}
category: '{category}'
tags: []
draft: false
---

"""

    return {
        "slug": clean_filename(title),
        "content": frontmatter + markdown,
        "title": title,
        "pub_date": pub_date,
        "category": category,
        "image_count": image_count,
    }


def main():
    """主函数"""
    # 确保目录存在
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # 遍历所有文章目录
    article_dirs = [d for d in EXPORT_DIR.iterdir() if d.is_dir()]
    print(f"找到 {len(article_dirs)} 篇文章\n")

    success_count = 0
    for article_dir in sorted(article_dirs):
        print(f"处理: {article_dir.name}")
        result = process_article(article_dir)

        if result:
            # 写入 Markdown 文件
            md_path = BLOG_DIR / f"{result['slug']}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(result["content"])

            print(f"  -> {md_path}")
            print(f"     日期: {result['pub_date']} | 分类: {result['category']} | 图片: {result['image_count']}张")
            success_count += 1
        else:
            print(f"  -> 跳过（无法解析）")

    print(f"\n完成！成功转换 {success_count}/{len(article_dirs)} 篇文章")
    print(f"文章目录: {BLOG_DIR}")
    print(f"图片目录: {IMAGES_DIR}")


if __name__ == "__main__":
    main()
