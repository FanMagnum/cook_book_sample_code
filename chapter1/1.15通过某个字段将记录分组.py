#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.15通过某个字段将记录分组.py
@Time    : 2019/11/15 10:21
@Author  : Lone
@Email   : fanml@neusoft.com
"""

"""
    问题
        你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭
    代访问。
"""
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(" ", i)

# 如果你仅仅只是想根据 date 字段将数据分组到一个大的数据结构中去，并且允许
# 随机访问，那么你最好使用 defaultdict() 来构建一个多值字典，关于多值字典已经
# 在 1.6 小节有过详细的介绍。比如：
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/04/2012']:
    print(r)
