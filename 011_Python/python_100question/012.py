#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 15:17 

"""
题目：判断101-200之间有多少个素数，并输出所有素数。
"""
"""
分析:
素数：质数
"""
from math import sqrt

def prime(n):
    """
    判断n是否是素数
    :param n:
    :return: 素数
    """
    if n == 1:
        return n

    for i in range(2,int(sqrt(n))+1):
        # print(i)
        if n%i == 0:
            return None
    return n

res = []
for n in range(101,201):
    if prime(n):
        res.append(prime(n))
print("101-200之间有%s个素数：%s"%(len(res),res))







