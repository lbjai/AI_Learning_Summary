#  ^ 以什么开始 python语言的match是自动添加的,其他语言不是这样,所以必须添加
# $以什么结尾
# 匹配变量名是否有效
# 匹配规则: 字母_开头, 匹配的数据: names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "------"]

# [a-zA-Z_].*
# 以字母或者_开头,后面随便.
import re

#
# names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "------"]
#
# # 从循环里面一个一个去匹配
# for temp in names:
# 	# 匹配
# 	# 匹配后的对象
# 	result = re.match("[a-zA-Z_].*", temp)
# 	# 判断对象
# 	if result:
# 		# 匹配到了
# 		print("匹配到了",result.group())
# 	else:
# 		# 没有匹配
# 		print("没有匹配到",temp)


# 正则的变量定义
# 以字母或者_开头,后面可以写数据字母_

# [a-zA-Z_][a-zA-Z_0-9]*

names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "------"]

# $这个是我们一定要匹配到最后
# ^ 这个从头开始匹配
# 从循环里面一个一个去匹配
for temp in names:
	# 匹配
	# 匹配后的对象
	result = re.match("[a-zA-Z_][a-zA-Z_\d]*$", temp)
	# 判断对象
	if result:
		# 匹配到了
		print("匹配到了", result.group())
	else:
		# 没有匹配
		print("没有匹配到", temp)

print(re.match("[\d]", "9").group())
print(re.match("[a\d]", "a").group())
