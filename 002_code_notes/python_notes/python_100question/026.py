#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
【程序 26】
题目：利用递归方法求 5! 。
"""

"""
方案一:调用math函数
"""
def Fun1(n):

    from math import factorial
    if n >= 0:
        return factorial(n)
    else:
        print('出错')
    return None

print(Fun1(5))

"""
方案二:函数递归
"""
def Fun2(n):
    if n < 0 or isinstance(n,float):
        print("出错了，请输入一个正整数")
    if n == 0:
        return 1
    else:
        return n*Fun2(n-1)
print(Fun2(1))