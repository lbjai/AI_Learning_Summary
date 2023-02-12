#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 11:42 
"""
题目：要求输出国际象棋棋盘。
"""
# 国际象棋是8*8的，i(0~7)代表行，j(0~7)代表列。当i+j为奇数的时候，是黑色格子，反之，白色格子。
for i in range(8):
    for j in range(8):
        if (i+j)%2 != 0:
            # 黑色格子
            print(chr(219), end='')
        else:
            # 白色格子
            print(" ", end='')
    print("")