import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://my-blog-wyhef.vercel.app',
  integrations: [mdx(), sitemap()],
  markdown: {
    shikiConfig: {
      // 代码高亮主题
      theme: 'github-dark',
      // 启用行号
      wrap: true
    }
  }
});

