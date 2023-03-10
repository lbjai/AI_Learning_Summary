#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/21 13:39 
"""
【程序 18】
题 目 ： 求 s=a + aa + aaa + aaaa + aa...a 的 值 ， 其 中 a 是 一 个 数 字 。 例 如
2+22+222+2222+22222(此时，共有 5 个数相加 ) ，几个数相加有键盘控制。
"""

num = int(input("请输入一个0-9数字:"))
count = int(input("请输入迭代次数："))
res = []
ans = 0
for i in range(1,count+1):
    res.append(str(num)*i)
    ans += int(str(num)*i)
res = "+".join(res)
print("%s=%s"%(res,ans))