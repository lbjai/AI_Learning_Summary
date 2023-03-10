#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/21 13:37 
"""
题目：利用条件运算符的嵌套来完成此题：学习成绩 >=90 分的同学用 A表示， 60-89 分
之间的用 B表示， 60 分以下的用 C表示。
"""

print("方案一:if嵌套")
score = float(input("请输入成绩："))
if score >= 90:
    print("成绩为:%s" % ("A"))
elif score >= 60:
    print("成绩为:%s" % ("B"))
elif score >= 0:
    print("成绩为:%s" % ("C"))
else:
    print("分数不在0-100之间，请重新输入：")

print("方案二：运算符")
score = float(input("请输入成绩："))
grade = "A" if score > 90 else  ('C' if score < 60 else 'B')

print("成绩为:%s" % grade)
