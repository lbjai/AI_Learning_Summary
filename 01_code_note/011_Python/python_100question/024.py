#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
题目：有一分数序列： 2/1 ，3/2 ，5/3 ，8/5 ，13/8 ，21/13... 求出这个数列的前 20 项
之和。
分析:分子分母为一个常见的数列
"""

num1 = 1
num2 = 1
num_sum = 0.0
for i in range(20):
    num2,num1 = num1+num2,num2
    num_sum += num2/num1
    # print("第%-2s个分数结果是：%s"%(i+1,num_sum))
print(num_sum)
