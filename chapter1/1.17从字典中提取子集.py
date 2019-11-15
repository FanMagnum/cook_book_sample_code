#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.17从字典中提取子集.py
@Time    : 2019/11/15 10:56
@Author  : Lone
@Email   : fanml@neusoft.com
"""

"""
问题
    你想构造一个字典，它是另外一个字典的子集。
"""
# 最简单的方式是使用字典推导。比如：
prices = {
    'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {k: v for k, v in prices.items() if k in tech_names}
print(p2)
