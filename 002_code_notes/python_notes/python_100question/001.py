#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 1:25 
"""
题目：
有 1、2、3、4 个数字，能组成多少个互不相同且无重复数字的三位数？都是多
少？
"""

data = [1,2,3,4]
num = 1
for i in data:
    for j in data:
        for k in data:
            if i != j and i != k and j != k:
                res = 100*i + 10*j + k
                print("第%s个不同数据：%s"%(num,res))
                num += 1