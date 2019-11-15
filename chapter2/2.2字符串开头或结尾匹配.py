#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 2.2字符串开头或结尾匹配.py
@Time    : 2019/11/15 16:47
@Author  : Lone
@Email   : fanml@neusoft.com
"""

"""
问题
    你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL
Scheme 等等。
"""
"""
解决方案
    检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.
endswith() 方法。
"""
filename = 'spam.txt'
print(filename.startswith('file'))
print(filename.endswith('.txt'))
"""
    如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
给 startswith() 或者 endswith() 方法
"""
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
c_and_h = [name for name in filenames if name.endswith(('.c', '.h'))]
print(c_and_h)
print(any(name.endswith('.py') for name in filenames))

