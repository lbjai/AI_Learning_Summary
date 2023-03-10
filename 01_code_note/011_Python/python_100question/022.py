#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:19 
"""
【程序 22】
题目：两个乒乓球队进行比赛，各出三人。甲队为 a,b,c 三人，乙队为 x,y,z 三人。已
抽签决定比赛名单。 有人向队员打听比赛的名单。 a 说他不和 x 比，c 说他不和 x,z 比，
请编程序找出三队赛手的名单。
"""
one = ["a","b","c"]
two = ["x","y","z"]
#
print("方案一:暴力法")
resv = []
for i in two:
    for j in two:
        for k in two:
            if i!=j and i!=k and j!=k:
                resv.append((i,j,k))
for i in resv:
    if i[0] != 'x' and i[2] != 'x' and i[2] != 'z':
        for j,k in zip(i,one):
            print("%s VS %s"%(k,j))


print("方案二:采用标准库")
import itertools

for i in itertools.permutations('xyz'):
    # print(i)
    if i[0] != 'x' and i[2] != 'x' and i[2] != 'z':
        print('a VS %s, b VS %s, c VS %s' % (i[0], i[1], i[2]))