class SingleInstance(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        # 实例化对象之前执行
        if cls.instance == None:
            # 只有 instance 为 None 才创建新对象
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self,name):
        self.name = name


SI1 = SingleInstance('zs')
SI2 = SingleInstance('ls')
print(SI1,id(SI1),SI1.name)
print(SI2,id(SI2),SI2.name)