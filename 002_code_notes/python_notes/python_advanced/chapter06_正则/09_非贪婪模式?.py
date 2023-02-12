# [^字符]这个是固定的一个语法,这个意思就是非
# 场景oldyang@163.com oldyang@163.com,我们想取到第一个邮箱
import re

#  多字符匹配后?这个非贪婪模式

print(re.match("(.*?)@163\.com", "oldyang@163.com oldyang@163.com").group())
