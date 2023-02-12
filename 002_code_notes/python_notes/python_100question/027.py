#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
【程序 27】
题目：利用递归函数调用方式，将所输入的 5 个字符，以相反顺序打印出来。
难点
"""
"""
理解递归
def f(x):
    if x == 最小值:
        return 最小值对应的值或无关紧要的值
    else:
        return 一个函数，表达式中要设下 f(x-1) 的套
"""


def fun(s,length):
    """
    相反顺序打印出来
    :param s: 字符
    :param length:字符长度
    :return:
    """
    if length == 0:
        return ""
    # print(s[length-1],end="")
    res = ""
    res += s[length-1]

    return res + fun(s,length-1)

str_ocr = "qwert"
print(fun(str_ocr, len(str_ocr)))


