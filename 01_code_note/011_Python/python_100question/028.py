#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
【程序 28】
题目：有 5 个人坐在一起，问第五个人多少岁？他说比第 4 个人大 2 岁。问第 4 个人岁
数，他说比第 3 个人大 2 岁。问第三个人，又说比第 2 人大两岁。问第 2 个人，说比第
一个人大两岁。最后问第一个人，他说是 10 岁。请问第五个人多大？
"""


def compareage(n):

    if n == 1:
        return 10
    return compareage(n-1)+2


print(compareage(5))


