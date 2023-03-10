# [^字符]这个是固定的一个语法,这个意思就是非
# 场景oldyang@163.com oldyang@163.com,我们想取到第一个邮箱
# 如果写字符串有可能会有错,他会去匹配一个字符串出错
import re

print(re.match(".{4,20}@163\.com", "oldyang@163.com oldyang@163.com").group())
print(re.match("[^@]+@163\.com", "oldyang@163.com oldyang@163.com").group())

# [^字符]字符
# [^@]@
