#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
题目：打印出如下图案（菱形）
   *
  ***
 *****
*******
 *****
  ***
   *
"""
for i in range(4):
    print(" "*(3-i),end="")
    print("*"*(2*i+1))
for i in range(1,4):
    print(" "*i,end="")
    print("*"*(7-2*i))