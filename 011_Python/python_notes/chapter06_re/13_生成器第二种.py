# 他是一种特殊的迭代器

# 只要函数中加了yield这个是我们的生成器
import re


def test():
	print("值")
	yield 1


print(test())

for temp in test():
	print(temp)

print(re.match(r'[^@]+@163\.com', "oldyang@163.com").group())
