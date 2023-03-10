"""
多态：
不同的 子类对象调用 相同 父类方法，产生不同的执行结果，增加代码调用的灵活度。
"""
class Dog(object):
    def work(self):
        pass

class DrugDog(Dog):
    def work(self):
        print("追查毒品！")

class ArmyDog(Dog):
    def work(self):
        print("追击敌人！")

class XiaoTianDog(Dog):
    def work(self):
        print("哮天犬把月亮吃了！")

class Person(object):

    def work_with_dog(self,dog):
        # 但凡父类能工作的地方，子类都能干活。
        dog.work()


# 多态的好处：提高代码调用灵活性
# 实现多态：
# 1.定义一个父类，并提供要在子类使用的方法
# 2.定义子类，并重写父类方法
# 3.把子类对象传递给调用者，调用处可以产生不同的执行效果

p = Person()
p.work_with_dog(ArmyDog())
p.work_with_dog(DrugDog())
p.work_with_dog(XiaoTianDog())


