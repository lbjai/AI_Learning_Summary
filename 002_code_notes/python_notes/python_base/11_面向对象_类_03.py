class Cat():
    def __init__(self,new_name):
        self.name = new_name
        print("__init__ 执行了",self)

    def __str__(self):
        """必须有返回值，返回值必须是字符串"""
        return "%s是他的名字"%self.name

    def __del__(self):
        print("del 执行了")
        pass

xiaohei = Cat('xiaohei')

del xiaohei
print("程序结束")



