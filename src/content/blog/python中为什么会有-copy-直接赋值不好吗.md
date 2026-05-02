---
title: 'Python中为什么会有.copy()？直接赋值不好吗？'
description: 'Python中为什么会有.copy()？直接赋值不好吗？'
pubDate: 2025-11-10
category: 'tech'
tags: []
draft: false
---

笔者最近调程序一直结果不符合预期，最后排查到原因发现自己真是数据结构没学好，真是应了那句“你数据结构怎么学的”。![](/images/python中为什么会有-copy-直接赋值不好吗-2.png)两个例子就看懂了。【例1】

  *   *   *   *   *   * 

    
    
    a = [1,2,3,4]print(a)b = ab.pop(0)print(a)print(b)

![](/images/python中为什么会有-copy-直接赋值不好吗-3.png)【例2】

  *   *   *   *   *   * 

    
    
    a = [1,2,3,4]print(a)b = a.copy()b.pop(0)print(a)print(b)

![](/images/python中为什么会有-copy-直接赋值不好吗-4.png)总结：在 Python 中，对于列表这类**可变对象** ，直接赋值（如 `b = a`），赋值的是**“地址”（引用）** ，而非复制列表的内容。