#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 15:50
"""
题目：将一个正整数分解质因数。例如：输入 90, 打印出 90=2*3*3*5 。
"""

print("方案一:")
res_list = []
num = 90
num1 = num
print('%s='%num,end='')
for i in range(2,num):
    while True:
        if num%i == 0:
            res_list.append(i)
            num /= i
            if num == 1:
                print("%s"%i,end="")
            else:
                print("%s*"%i,end="")
        else:
            break

print()
print("方案二:")
res_list = []
num = 90
for i in range(2,num):
    while True:
        if num%i == 0:
            res_list.append(i)
            num /= i
        else:
            break
res = "*".join([str(i) for i in res_list])
print("%s=%s"%(num1,res))
