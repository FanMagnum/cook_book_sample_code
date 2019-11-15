#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.19转换并同时计算数据.py
@Time    : 2019/11/15 14:40
@Author  : Lone
@Email   : fanml@neusoft.com
"""

"""
问题
  你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ），但是首先你需
要先转换或者过滤数据

解决方案
   一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。比
如，如果你想计算平方和，可以像下面这样做：
"""
nums = [1, 2, 3, 4, 5]
s = [x * x for x in nums]
print(s)

# Determine if any .py files exist in a directory
import os
files = os.listdir('./')
print(files)
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [{'name': 'GOOG', 'shares': 50},
             {'name': 'YHOO', 'shares': 75},
             {'name': 'AOL', 'shares': 20},
             {'name': 'SCOX', 'shares': 65}]
min_shares = min(s['shares'] for s in portfolio)
# 上面的示例向你演示了当生成器表达式作为一个单独参数传递给函数时候的巧妙
# 语法（你并不需要多加一个括号）
print(min_shares)
from operator import itemgetter
print(min(portfolio, key=itemgetter('shares')))