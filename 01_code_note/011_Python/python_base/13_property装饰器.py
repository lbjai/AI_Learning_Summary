class Person(object):
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        print("调用name方法啦！！！，作用与 self.get_name 方法一样！")
        return self.__name

    def get_name(self):
        print("调用get_name方法啦")
        return self.__name

    def set_name(self,name):
        """设置属性值"""
        print("调用 set_name 方法啦！！！")
        self.__name = name
        return self.__name

    @name.setter
    def name(self,name):
        print("调用 setter 方法啦")
        self.__name = name

p = Person("孙悟空")
print("======================获取属性"+"======================")
print(p.get_name())
print("-"*30)
print(p.name)


print("======================设置属性"+"======================")
# print(p.set_name("猪八戒"))
p.name = '猪八戒'
print(p.name)

