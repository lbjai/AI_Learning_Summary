a = 0
b = 1
c = 3

# and 运算，只要有一个为0则结果为0；否则结果为最后一个非0数字
print(a and b)
print(b and c)
print(c and a)
print(c and b)

# or 运算，只有所有值都为 0 结果才为 0 ，否则结果为第一个非0数字
print("or", a or a)
print(a or b)
print(b or a)
print(b or c)

print("a and b or c:",a and b or c)