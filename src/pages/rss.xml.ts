import rss from '@astrojs/rss';
import { getAllPosts } from '../utils/post';
import { SITE_CONFIG } from '../config';

export async function GET(context: any) {
  const blog = await getAllPosts();
  
  return rss({
    title: SITE_CONFIG.title,
    description: SITE_CONFIG.description,
    site: context.site,
    items: blog.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      // 自定义 RSS 内容链接
      link: `/blog/${post.slug}/`,
    })),
    // (可选) 注入自定义 XML
    customData: `<language>zh-cn</language>`,
    stylesheet: '/rss-style.xsl',
  });
}
