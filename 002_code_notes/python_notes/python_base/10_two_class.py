"""
存放家具分析
"""
class Home(object):
    """房间类"""
    def __init__(self,area):
        self.ares = area
        self.item = None # 床的信息
    def __str__(self):
        return "房间的大小为%s平米,存放的床有%s平米"%(self.ares,self.item)

    def add_item(self,item):
        """添加一张床"""
        self.item = item

        pass

class Bed:
    """床类"""
    def __init__(self,name,area):
        """初始化床的信息"""
        self.name = name
        self.area = area

    def __str__(self):
        return "{}的大小为{}平米".format(self.name,self.area)

    pass

# 房子
home = Home(300)
print(home)

# 床
xms = Bed("席梦思",4)
print(xms)

# 把床放到房间内
home.add_item(xms)
print(home)