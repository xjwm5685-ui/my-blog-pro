# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 常用命令

```bash
npm install          # 安装依赖
npm run dev          # 启动开发服务器 (localhost:4321)
npm run build        # 构建生产版本到 dist/
npm run preview      # 预览生产版本
```

## 技术栈

- **框架**: Astro 4.x (静态站点生成)
- **语言**: TypeScript (strict 模式)
- **内容**: Markdown + MDX (Astro Content Collections)
- **样式**: CSS Variables，支持暗色模式 (`html.dark` 类切换)
- **部署**: Vercel (主要)

## 架构概览

三栏布局设计：
- **左侧边栏** (`LeftSidebar.astro`): 文章导航，280px 固定宽度
- **TOC 侧边栏** (`TableOfContents.astro`): 文章目录，240px，仅文章详情页显示
- **主内容区**: 自适应宽度，文章详情页限制 900px 最大宽度

布局在 `BaseLayout.astro` 中组合，通过 `hasTOC` 控制 TOC 栏显示。

## 路径别名

```typescript
@/*           -> src/*
@components/* -> src/components/*
@layouts/*    -> src/layouts/*
@utils/*      -> src/utils/*
```

## 内容管理

博客文章存放在 `src/content/blog/`，使用 Astro Content Collections。

**Frontmatter Schema** (`src/content/config.ts`):
```typescript
{
  title: string;           // 必需
  description: string;     // 必需
  pubDate: Date;           // 必需，YYYY-MM-DD 格式
  updatedDate?: Date;      // 可选
  category: 'tech' | 'notes' | 'travel';  // 必需
  tags?: string[];         // 可选，默认 []
  cover?: string;          // 可选，封面图路径
  draft?: boolean;         // 可选，默认 false
}
```

**工具函数** (`src/utils/post.ts`):
- `getAllPosts()` - 获取所有文章，按日期降序
- `getPostsByCategory(category)` - 按分类筛选
- `getPostsByTag(tag)` - 按标签筛选
- `getAdjacentPosts(slug)` - 获取上/下篇文章

## 站点配置

核心配置在 `src/config.ts` 的 `SITE_CONFIG` 对象中，包含站点信息、分类定义、导航链接等。

## CSS 主题系统

全局样式在 `src/styles/global.css`，使用 CSS 变量：
- `:root` 定义亮色主题
- `html.dark` 定义暗色主题
- `--article-font-size` 控制文章正文字号（默认 17px）
- ThemeToggle 组件负责切换

## SEO

SEO 工具在 `src/utils/seo.ts`，`BaseLayout.astro` 自动处理 Open Graph 和 Twitter Card 标签。
