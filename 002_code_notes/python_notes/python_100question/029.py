#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
【程序 29】
题目：给一个不多于 5 位的正整数，要求：一、求它是几位数，二、逆序打印出各位数
字。
"""

num = input("请输入一个小于5位数的正整数：")

if len(num) > 5 :
    print("输入位数不对")

if ("."or"-") in num:
    print("请输入正整数")

print("%s是%s位数，逆序:%s"%(num,len(num),num[::-1]))