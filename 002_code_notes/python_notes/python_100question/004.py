#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/20 11:03 
"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
"""
import datetime
def function(year,month,day):
    date = datetime.date(year,month,day)
    # %j十进制表示的每年的第几天
    res = date.strftime('%j')
    return int(res)

print(function(2016,1,2))