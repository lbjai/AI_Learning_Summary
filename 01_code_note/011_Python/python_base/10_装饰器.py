def add(a,b):
    r = a + b
    return r

def mul(a,b):
    r = a*b
    return r

# 实现：
# r = add(111,222)
# print(r)

# 装饰器解决问题：
# 1.如果不使用装饰器，修改起来比较麻烦，而且不方便后期的维护
# 2.OCP:开闭原则
# 要求开发对程序的扩展，要关闭对程序的修改

def fn():
    print('我是fn函数。。。')

def fn1():
    print('函数开始执行、、、')
    fn()
    print('函数执行并结束、、、')

# fn1()

# 对加法扩展
def new_add(a,b):
    print("函数开始执行、、、")
    r = add(a,b)
    print("函数结束执行、、、")
    return r

# print(new_add(111, 222))

# 通用扩展
def begin_end(old):
    """
    用来对其他函数进行扩展
    :return:
    """
    def new_function(*args,**kwargs):
        print("函数开始执行、、、=")
        # 调用被扩展的函数
        res = old(*args,**kwargs)
        print("函数结束执行、、、=")
        return res

    return new_function

f = begin_end(add)
r = f(111,1)
print(r)
print(len(" "))
