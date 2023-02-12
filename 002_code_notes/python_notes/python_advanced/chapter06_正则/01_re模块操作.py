# re.match用来匹配数据
# re.group用来获取匹配的数据

# 场景:匹配以itcast开头的语句,被匹配的语句itcast.cn

# if str.startswith("itcast"):
# 	print("这个是itcast开头的")
#
# if str.endswith(".cn"):
# 	print("这个以.cn结尾的")

# 正则使用
# 导入模块re
import re

# re.match("匹配规则","要被匹配的数据") # 返回一个匹配的对象

# print(re.match("1itcast", str)) # 如果返回了none这个说明没有匹配


str = "itcast.cn"
# 匹配后的对象
result = re.match("itcast", str)
print(result)
# 对匹配后的对象进行判断
if result:
	# 查看匹配到的数据
	value = result.group()
	# 匹配到了
	print("匹配了", value)
else:
	print("没有匹配到")
