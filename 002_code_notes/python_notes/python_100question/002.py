#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 1:34 

"""
企业发放的奖金根据利润提成。利润 (I) ：
+ 低于或等于 10 万元时，奖金可提 10%；
+ 高于 10 万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于10万元的部分，可提成 7.5%；
+ 20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；
+ 40 万到 60 万之间时，高于 40 万元的部分，可提成 3%；
+ 60 万到 100 万之间时，高于 60 万元的部分，可提成 1.5%，
+ 高于 100 万元时， 超过 100 万元的部分按 1%提成
"""
Iin = int(input("请输入月利润(万元)："))
xIin = [0,10,20,40,60,100]  # 利润
xIin.reverse()
yIin = [10,7.5,5,3,1.5,1]  # 提成
yIin.reverse()
res = 0.0
for i in range(len(xIin)):
    if Iin > xIin[i]:
        res1 = (Iin-xIin[i])*yIin[i]/100
        print("第%s次，利润:[%0.3s,%3s]，提成:%4s，奖金数:%s万元"%(i,xIin[i],xIin[i-1],yIin[i],res1))
        res += res1
        Iin = xIin[i]

print("总利润:%s万元"%res)


