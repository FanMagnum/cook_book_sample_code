#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    : 1.12序列中出现次数最多的元素.py
@Time    : 2019/11/15 9:55
@Author  : Lone
@Email   : fanml@neusoft.com
"""
# 怎样找出一个序列中出现次数最多的元素呢？

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the',
    'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
    'around', 'the', 'eyes', "don't", 'look', 'around',
    'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
print(type(word_counts))
# top 3
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
print(word_counts['eyes'])

# Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。
a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
d = a - b
print(d)
