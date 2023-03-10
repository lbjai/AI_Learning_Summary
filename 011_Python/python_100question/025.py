#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
【程序 25】
题目：求 1+2!+3!+...+20! 的和
"""
sum = 0
for i in range(1,20+1):
    # print("%-2s 的阶层"%i,end="")
    isum = 1
    # 计算阶层
    for num in range(1,i+1):
        isum *= num
    # print("是：%s"%isum)
    sum += isum
print("总和是:%s"%sum)

