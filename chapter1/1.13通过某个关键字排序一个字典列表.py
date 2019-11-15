#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.13通过某个关键字排序一个字典列表.py
@Time    : 2019/11/15 10:07
@Author  : Lone
@Email   : fanml@neusoft.com
"""
from operator import itemgetter

# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表
rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
# itemgetter() 函数也支持多个 keys，比如下面的代码
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# itemgetter() 有时候也可以用 lambda 表达式代替
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_fname)
print(rows_by_lfname)

# 最后，不要忘了这节中展示的技术也同样适用于 min() 和 max() 等函数。比如：
min_uid = min(rows, key=itemgetter('uid'))
max_uid = max(rows, key=itemgetter('uid'))
print(min_uid)
print(max_uid)
