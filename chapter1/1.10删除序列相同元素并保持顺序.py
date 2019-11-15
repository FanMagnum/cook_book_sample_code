#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.10del_the_same_and_keep_the_order.py
@Time    : 2019/11/15 9:00
@Author  : Lone
@Email   : fanml@neusoft.com
"""

a = [1, 5, 2, 1, 9, 1, 5, 10]

# 我的解法
tmpDict = {}
for i in a:
    tmpDict[i] = 0
print(list(tmpDict.keys()))


# 书 适用于hashable的序列
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


print(list(dedupe(a)))


# 适用于不可hashable序列
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, lambda d: (d['x'], d['y']))))
print(list(dedupe(a, lambda d: (d['x']))))
