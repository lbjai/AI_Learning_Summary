# 创建一个类实现两个魔法方法一个iter,一个next
class MyList(object):
	def __init__(self):
		# 实例属性初始化一个值
		self.num = 0

	# 只要类实现了这个方法 ,我们可以称这个对象为可迭代的对象
	# 这里返回我们的迭代器对象,以后工作通常只返回self
	def __iter__(self):
		return self

	# 迭代器还必须实现next方法,这个方法的作用是用来迭代的(循环遍历)的过程返回的值
	def __next__(self):
		# 加一个停止迭代的判断条件,条件也有自己去写
		if self.num > 100:
			raise StopIteration  # 停止迭代
		else:

			# 以后如果自己想写一个迭代器,那么可以把这里的算法改一下
			self.num += 1

			return self.num


# 作用可以像list一样用for..in..去循环遍历
# 实例对象创建,他就是一个迭代器对象了
my_list = MyList()

for temp in my_list:
	print(temp)
