class Person(object):
    def __new__(cls, *args, **kwargs):
        """
        创建对象时执行
        :param args:
        :param kwargs:
        :return:
        """
        obj = object.__new__(cls)  # 当重写了 __new__ 之后，如果还要创建新对象，则需要调用 object 来处理
        print('new---', obj)
        return obj  # 创建好的对象必须使用 return 返回


    def __init__(self):
        """创建对象之后执行"""
        pass

zs = Person()
print(zs)