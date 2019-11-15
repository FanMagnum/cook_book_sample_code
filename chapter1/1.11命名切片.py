#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.11命名切片.py
@Time    : 2019/11/15 9:29
@Author  : Lone
@Email   : fanml@neusoft.com
"""

#         0123456789012345678901234567890123456789012345678901234567890
record = '....................100 .......513.25 ..........'
# 硬编码切片不易理解
cost = int(record[20:23]) * float(record[31:37])
# 命名切片 使得你的代码更加清晰可读了
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# 如果你有一个切片对象 a，你可以分别调用它的 a.start , a.stop , a.step 属性
# 来获取更多的信息。比如：
a = slice(5, 50, 2)
print(a.start, a.stop, a.step)
# 你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序
# 列上，这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以
# 满足边界限制，从而使用的时候避免出现 IndexError 异常。比如：
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
