#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 11:14 
"""
题目:输入三个整数 x，y，z，请把这三个数由小到大输出。
"""
x = int(input("请输入第1个整数:"))
y = int(input("请输入第2个整数:"))
z = int(input("请输入第3个整数:"))
res_list = [x,y,z]
res_list.sort()

print(res_list)

