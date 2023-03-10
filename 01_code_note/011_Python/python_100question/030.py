#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:21 
"""
【程序 30】
题目：一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位
与千位相同。
"""




def fun(num):

    if len(num) != 5:
        return "请输入5位数"

    res_list = []
    for i in range(len(num)):

        if num[i] == num[len(num) - i - 1]:
            ish = 1
        else:
            ish = 0
        res_list.append(ish)

    if 0 in res_list:
        print("%s不是回文数"%num)
        return None
    print("%s是回文数字"%num)
    return num



num = input("请输入一个5位数：")
fun(num)