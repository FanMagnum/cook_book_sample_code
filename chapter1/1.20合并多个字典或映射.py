#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.20合并多个字典或映射.py
@Time    : 2019/11/15 15:00
@Author  : Lone
@Email   : fanml@neusoft.com
"""

"""
问题
   现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某
些操作，比如查找值或者检查某些键是否存在。
"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'], c['y'], c['z'])
print(len(c), list(c.keys()), list(c.values()))
# 对于字典的更新或删除操作总是影响的是列表中第一个字典。比如：
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y'] KeyError: "Key not found in the first mapping: 'y'"
