class Person(object):

    def __init__(self):
        self.__age = 0

    def set_age(self,new_age):
        self.__my_print('set_age')
        if new_age > 18:
            self.__age = new_age
        else:
            print('年龄不能小于0')

    def get_age(self):
        self.__my_print("get_age")
        return self.__age

    def __my_print(self,msg):
        print("Person说：开始执行 "+msg)

zs = Person()
zs.set_age(100)
zs.get_age()
