#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 11:51 
"""
题目：打印楼梯，同时在楼梯上方打印两个笑脸。
"""
import sys

sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
for i in range(10):
    for j in range(i):
        print("===",end="")

    print("")
