#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.18映射名称到序列元素.py
@Time    : 2019/11/15 11:01
@Author  : Lone
@Email   : fanml@neusoft.com
"""

'''
问题
   你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的
代码难以阅读，于是你想通过名称来访问元素。

解决方案
 collections.namedtuple() 函数通过使用一个普通的元组对象来帮你解决这个问
题。这个函数实际上是一个返回 Python 中标准元组类型子类的一个工厂方法。你需要
传递一个类型名和你需要的字段给它，然后它就会返回一个类，你可以初始化这个类，
为你定义的字段传递值等。代码示例：
'''

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)