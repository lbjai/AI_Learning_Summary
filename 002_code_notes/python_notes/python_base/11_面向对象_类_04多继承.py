class Ma(object):
    def run(self):
        print("马跑的快!")

    def walk(self):
        print("马走的慢！")

class Lv(object):
    def walk(self):
        print('驴走的远！')

class LuoZi(Ma,Lv):
    pass

luozi = LuoZi()

# 根据 mro 算法确定调用父类的顺苏
print(LuoZi.__mro__)

# 当父类有同名方法则需要强制指定 调用哪个父类的方法。
Ma.walk(luozi)  # 父类名.父类方法（子类对象）
