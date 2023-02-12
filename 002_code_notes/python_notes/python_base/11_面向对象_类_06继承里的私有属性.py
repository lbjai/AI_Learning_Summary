class Animal(object):

    def __init__(self):
        self.__age = 5

    def get_age(self):
        return self.__age


class Cat(Animal):
    def catch(self):
        print('猫今年%d岁了，能抓老鼠'%self.get_age())

cat = Cat()
cat.catch()