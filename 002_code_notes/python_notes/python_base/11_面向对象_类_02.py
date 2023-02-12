"""
类
1.我们目前学习的对象，比如字典，都是python内置对象
对象，简单理解就像 盒子
类，就是对象的图纸
对象是类的实例(instance)
多个对象是通过一个类创建的，则这些类是一类对象。
"""
# a = int(10)
# b = str('hello')
# print(a,type(a))

class MyClass():
    pass

print(MyClass)  # <class '__main__.MyClass'>
mc = MyClass() # 实例对象
print(mc,type(mc))  # <__main__.MyClass object at 0x000002937E68EF48> <class '__main__.MyClass'>

res = isinstance(mc,MyClass)
print("判断对象是否属于该类：",res)  # True

print("="*20)
"""
类也是对象，
判断某个对象是不是对象：
    对象的标识：id
    对象的类型：type
    对象的值：value
Myclass：
变量名:MyClass
id:0X00
value:空对象
type：MyClass
"""

"""
创建对象的流程
1.创建一个变量 mc
2.在内存中创建一个新对象
3.将对象的id赋值给变量
"""

print("="*20,"\n 对象的属性：")
"""
属性：
    对象中的变量称为属性
给对象添加属性：
    对象.属性名= 属性值
"""
mc.name = '孙悟空'
print(mc.name)
