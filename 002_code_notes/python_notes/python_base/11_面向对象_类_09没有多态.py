"""
多态：
不同的 子类对象调用 相同 父类方法，产生不同的执行结果，增加代码调用的灵活度。
"""
class DrugDog(object):
    def track_drug(self):
        print("追查毒品！")

class ArmyDog(object):
    def bite_enemy(self):
        print("追击敌人！")

class XiaoTianDog(object):
    def eat_moon(self):
        print("哮天犬把月亮吃了！")

class Person(object):

    def work_with_army(self,dog):
        dog.bite_enemy()

    def work_with_drug(self,dog):
        dog.track_drug()

    def work_with_xiaotian(self,dog):
        dog.eat_moon()


p = Person()
p.work_with_army(ArmyDog())
p.work_with_drug(DrugDog())
p.work_with_xiaotian(XiaoTianDog())


