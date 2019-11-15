#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 22:28
# @Author  : Lone
# @Site    : 
# @File    : 1.1.8dict_operation.py
# @Software: PyCharm
from typing import Tuple

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
          }
# 获取最大值 最小值
max_price = max(zip(prices.values(), prices.keys()))
min_price = min(zip(prices.values(), prices.keys()))
print(max_price)
print(min_price)
price_sorted = sorted(zip(prices.values(), prices.keys()))
print(price_sorted)
# zip将多个列表压缩成一个列表
for v in zip(prices.values(), prices.keys()):
    print(v)

# values最低值
print(min(prices.values()))
print(prices.keys())
print(prices.values())
