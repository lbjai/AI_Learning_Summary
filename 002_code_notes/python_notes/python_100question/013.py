#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 15:39 

"""
题目：打印出所有的“水仙花数”,所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
例如： 153 是一个“水仙花数” ，因为 153=1 的三次方＋5 的三次方
＋3的三次方。
"""

def Narcissistic_number(n):

    if n < 100 and n >= 1000:
        return "请输入一个三位数！"
    g = n%10          # 个位数
    s = int(n/10)%10  # 十位数
    b = int(n/100)    # 百位数
    if n == pow(g,3) + pow(s,3) + pow(b,3):
        return n
    return None

res = []
for n in range(100,1000):
    if Narcissistic_number(n):
        res.append(Narcissistic_number(n))
print("100-1000之间的水仙花数共有%s个：%s"%(len(res),res))