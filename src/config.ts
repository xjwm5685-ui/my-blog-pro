// 博客配置文件
export const SITE_CONFIG = {
  title: '吴煜凡的博客',
  description: '记录技术、学习和生活',
  author: '吴煜凡',
  avatar: '/images/python-断点调试总结-2.png',
  email: 'wyf1992570@163.com',
  github: 'https://github.com/WYHEF',
  bilibili: 'https://space.bilibili.com/631363348',
  wechat: '五氧化二钒不是废钒',
  
  // 分类配置
  categories: {
    tech: { name: 'Tech', displayName: '技术', description: '技术文章和教程' },
    notes: { name: 'Notes', displayName: '笔记', description: '学习笔记和总结' },
    travel: { name: 'Travel', displayName: '游记', description: '旅行见闻' }
  },
  
  // 每页显示文章数
  postsPerPage: 10,
  
  // 导航链接
  navLinks: [
    { name: '首页', path: '/' },
    { name: '技术', path: '/category/tech' },
    { name: '笔记', path: '/category/notes' },
    { name: '游记', path: '/category/travel' },
    { name: '视频教程', path: '/videos' },
    { name: '成品项目', path: '/projects' },
    { name: '标签', path: '/tags' },
    { name: '关于', path: '/about' }
  ]
};

export type Category = keyof typeof SITE_CONFIG.categories;

