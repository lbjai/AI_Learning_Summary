# | 相当于python中的or
# 	案例:匹配出163或者126的邮箱
import re

# ()还可以单独取出匹配的某一部分数据
# 	案例:取出邮箱的类型(只要163,126),后期可以编计用户那个邮箱用的多

# print(re.match(".{4,20}@163\.com", "python16@163.com").group())
# print(re.match(".{4,20}@126\.com", "python16@126.com").group())
#
#
# print(re.match(".{4,20}@(126|163)\.com", "python16@126.com").group())
# print(re.match(".{4,20}@(126|163)\.com", "python16@163.com").group())


# group()得到匹配的结果,group(1)
# print(re.match(".{4,20}@(126|163)\.com", "python16@163.com").group(1))
# print(re.match("(.{4,20})@(126|163)\.com", "python16@126.com").group(1))
# print(re.match("(.{4,20})@(126|163)\.com", "python16@126.com").group(2))
# # print(re.match("(.{4,20})@(126|163)\.com", "python16@126.com").group(3))




# \num用来取第几组用()包裹的数据  \1取第一个内部的括号位置的值
# 格式(xxx)\1 :\1表示获取(xxx)的值
# 案例<html>hh</html>  # 这个一定是有字母,开始跟结束的字母必须一样

# re_str = "<([a-zA-Z]+)>.*</[a-zA-Z]+>"
re_str = "<([a-zA-Z]+)>.*</\\1>"
# print(re.match(re_str, "<html>hh</html>").group())
# print(re.match(re_str, "<abcd>hh</abc>").group())
# print(re.match(re_str, "<abcd>hh</abcd>").group(1))
# print(re.match(re_str, "<html>hh</html>").group(1))
#



# 案例<html><body>hh</body></html>

# print(re.match("<([a-zA-Z]+)><([a-zA-Z]+)>.*</\\2></\\1>", "<htmlq><body>hh</body></html>").group())
#


# 使用别名给分组取别名,了解一下
# 格式:(?P<别名>xxx)(?P=别名)
# 案例<html><body>hh</body></html>
# 提示问题没错
print(re.match("<(?P<name1>[a-zA-Z]+)><(?P<name2>[a-zA-Z]+)>.*</(?P=name2)></(?P=name1)>",
               "<html><body>hh</body></html>").group())
