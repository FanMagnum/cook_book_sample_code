#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 2.3用Shell通配符匹配字符串.py
@Time    : 2019/11/15 17:14
@Author  : Lone
@Email   : fanml@neusoft.com
"""

"""
问题
    你想使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文
本字符串
"""
"""
解决方案
    fnmatch 模块提供了两个函数——fnmatch() 和 fnmatchcase() ，可以用来实现
这样的匹配。
"""
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
