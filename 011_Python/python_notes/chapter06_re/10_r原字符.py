# 原字符的作业就是让我们少写\\的转转义
import re

print("c:\\")
print("c:\\d\\")

print(re.match('c:\\\\d\\\\e', "c:\\d\\e").group())
print(re.match('c:\\\\d\\\\e', "c:\\d\\e").group())

# r就是原字符,原始的字符串是怎么样,现在还是怎么写
print(re.match(r'c:\\d\\e', "c:\\d\\e").group())

# 原字符的\\\\转成\
