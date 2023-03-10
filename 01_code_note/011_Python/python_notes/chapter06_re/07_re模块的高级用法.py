# 查询结果
# 	search 不会从头开始匹配,只要匹配到数据就结束
# 	案例:匹配出文章阅读的次数中的次数
# 	数据:"阅读次数为 9999"
import re

# 匹配的结果返回,不是从头开始,一个一个去匹配
# print(re.search("\d+", "阅读次数为 999 sdf;lasdkfj asdfa;lsdkfjasl;dfjk asld f123").group())


# 查询结果集
# findall
# 案例: 统计出python、c、c + +相应文章阅读的次数
# 数据: "python = 9999, c = 7890, c++ = 12345"

# 得到一个结果集
# result_list = re.findall("\d+", "python = 9999, c = 7890, c++ = 12345")
# print(result_list)


# 字符串切割
# split
# 切割字符串“info:xiaoZhang 33 shandong”, 根据:或者空格
print(re.split("\s", "“info:xiaoZhang 33 shandong”"))
print(re.split(":", "“info:xiaoZhang 33 shandong”"))


# 替换数据
# sub
# 案例: 将匹配到的阅读次数换成998
# 数据: "python = 997"
# re.sub("匹配的规则","想要替换成的字符串","被替换的原始数据")
# 生成一个替换后的字符串
# new_str = re.sub("\d+", "8374", "python = 997")
# print(new_str)

# sub会把匹配的对象传入
def count(match):
	# 得到997
	value = match.group()
	value_int = int(value)
	value_int += 100
	# 返回结果
	return str(value_int)  # 返回必须是字符串


# 新字符串
new_str = re.sub("\d+", count, "python=997")
print(new_str)
