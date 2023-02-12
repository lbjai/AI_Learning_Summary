#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/21 13:41 
"""
【程序 20】
题目：一球从 100 米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
第 10 次落地时，共经过多少米？第 10 次反弹多高？
"""

def function(num):
    """
    num:次数
    :param num:
    :return:
    """
    h = 100
    dis = 0
    for i in range(1, num+1):
        if i == 1:
            # 第一次落地高度
            dis += 100
            # print("第%s次下落路程%s米" % (i, dis))
        else:
            # 第二次下落高度
            dis += h * 2
            # print("第%s次下落路程%s米" % (i, dis))

        h /= 2

        if i == num:
            # print("第%s次反弹%s米" % (i, h))
            return h, dis

print(function(10))