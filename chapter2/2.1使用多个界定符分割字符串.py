#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 2.1使用多个界定符分割字符串.py
@Time    : 2019/11/15 16:22
@Author  : Lone
@Email   : fanml@neusoft.com
"""

"""
问题
    你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定
的。
"""
"""
解决方案
    string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有
多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，
最好使用 re.split() 方法：
"""
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
line_split = re.split(r'[;,\s]\s*', line)
print(line_split)
"""
当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括
号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。比如，
观察一下这段代码运行后的结果
"""
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
# 恢复字符串
print(''.join(v+d for v, d in zip(values, delimiters)))
"""
如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则
表达式的话，确保你的分组是非捕获分组，形如 (?:...) 。比如：
"""
fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)
