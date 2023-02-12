#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 11:35 
"""
题目：输出9*9口诀表。
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s=%-3s"%(j,i,i*j),end="")
    print()