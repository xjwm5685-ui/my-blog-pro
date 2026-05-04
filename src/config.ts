// 博客配置文件
export const SITE_CONFIG = {
  title: '吴煜凡的博客',
  shortTitle: 'WYHEF',
  wordmark: 'WYHEF', // 用于 Hero 巨型字标
  subtitle: '记录技术 · 学习 · 远方',
  description: '记录技术、学习和生活',
  author: '吴煜凡',
  authorEn: 'WYHEF',
  avatar: '/images/python-断点调试总结-2.png',
  email: 'wyf1992570@163.com',
  github: 'https://github.com/WYHEF',
  bilibili: 'https://space.bilibili.com/631363348',
  wechat: '五氧化二钒不是废钒',

  // 分类配置
  categories: {
    tech: {
      name: 'Tech',
      displayName: '技术',
      description: '工程实践 · 调试笔记 · AI/全栈/工具',
      tagline: 'Engineering field notes'
    },
    notes: {
      name: 'Notes',
      displayName: '笔记',
      description: '阅读、学习与思考的整理',
      tagline: 'Notes on what I learn'
    },
    travel: {
      name: 'Travel',
      displayName: '游记',
      description: '镜头下的城市与远方',
      tagline: 'Cities through a lens'
    }
  },

  // 每页显示文章数
  postsPerPage: 10,

  // 主导航 — englishName 用于 x.ai 风格的等宽全大写字标
  navLinks: [
    { name: '首页',     englishName: 'HOME',     path: '/' },
    { name: '技术',     englishName: 'TECH',     path: '/category/tech' },
    { name: '笔记',     englishName: 'NOTES',    path: '/category/notes' },
    { name: '游记',     englishName: 'TRAVEL',   path: '/category/travel' },
    { name: '视频',     englishName: 'VIDEOS',   path: '/videos' },
    { name: '项目',     englishName: 'PROJECTS', path: '/projects' },
    { name: '标签',     englishName: 'TAGS',     path: '/tags' },
    { name: '关于',     englishName: 'ABOUT',    path: '/about' }
  ]
};

export type Category = keyof typeof SITE_CONFIG.categories;
