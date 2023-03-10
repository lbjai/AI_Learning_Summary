#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 10:52 

"""
题目：一个整数，它加上 100 后是一个完全平方数，再加上 168 又是一个完全平方数，
请问该数是多少？
"""

xlist = []
for i in range(10000):
    x = pow(i,2)-100
    xlist.append(x)
ylist = []
for i in range(1000):
    x = pow(i,2)-168-100
    ylist.append(x)

for x in xlist:
    for y in ylist:
        if x == y:
            print(x)


