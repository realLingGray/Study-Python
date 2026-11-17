# 所谓的魔法方法，就是__aaa__方法，由python自己调用，无需我们调用
# 比如_init__
# __eq__：equal   __str__：to string
# 学几个魔法方法__lt__：less than  __le__：less than or equal
# __gt__：greater than  __ge__：greater than or equal


# 命名:大驼峰命名法
class Car:
    # __init__():初始化的方法,对对象设置一些属性,py内建
    # self:当前创建的实例对象,就是this,定义时,先写self
    # 然后写参数,但是调用的时候不需要写self
    def __init__(self,cname,cprice,ccolor,cbrand):
        self.name=cname
        self.price=cprice
        self.color=ccolor
        self.brand=cbrand
        print("初始化完毕")
    def running(self):
        print(f"车辆{self.name}品牌为:{self.brand}正在高速行驶...")
    def total_cost(self, discount, rate):
        """
        计算总花费
        :param discount: 折扣
        :param rate:税率
        :return:总花费
        """
        return self.price * discount + self.price * rate
    # 魔法方法
    def __eq__(self,other):
        return self.name == other.name and self.price == other.price and self.color == other.color and self.brand == other.brand
    def __str__(self):
        return f"{self.color}-{self.name}-{self.price}-{self.brand} "
    def __lt__(self,other):
        return self.price < other.price
    def __gt__(self,other):
        return self.price > other.price


if __name__ == '__main__':
    c1 = Car("X5",150000,"red","BMW")
    c2 = Car("X7", 300000, "black", "BMW")
    print(c1.__dict__)
    c1.running()
    print(f"请付款CN￥{c1.total_cost(0.9,0.05)}")
    # 此时再直接print c1就不是地址了
    print(c1)
    print(c1 == c2)
    print(c1 > c2)
    print(c1 < c2)