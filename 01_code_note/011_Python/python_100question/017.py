#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/21 13:38 
"""
【程序 17】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

data = input("请输入一行字符:")
cn_letters = 0
en_letters = 0
space=0
digit=0
others=0

for i in data:
    if '\u4e00' <= i <= '\u9fa5':
        # 中文字符数目
        cn_letters += 1

    elif i.isalpha():
        # 英文字符数目
        en_letters += 1

    elif i.isspace():
        # 空格数目
        space += 1

    elif i.isdigit():
        # 数字个数
        digit += 1

    else:
        # 其它字符的个数
        others += 1

print("中文字符数目:%s,英文字符数目:%s,空格数目:%s,数字数目:%s,其它字符数目:%s"%(
    cn_letters,en_letters,space,digit,others))
