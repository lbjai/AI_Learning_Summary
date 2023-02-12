#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/21 13:40 
"""
【程序 19】
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数” 。例如 6=1＋2＋3。编
程找出 1000 以内的所有完数。
"""

# 完数
res = list()
for num in range(1,1000+1):
    res_list = [1]
    for i in range(2,num):
        if num%i == 0:
            res_list.append(i)
    if sum(res_list) == num:
        res.append(num)
        print("完数:%s,因子:%s"%(num,res_list))


