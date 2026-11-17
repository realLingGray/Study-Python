# 类属性就是所有对象共有的，属于static属性，而对象属性就是属于对象自己的属性
# 查找：优先查对象属性 如果对象属性没有就查类属性
# 对象属性：对象.属性
# 类属性：类名.属性
class Car:
    # 类属性 所有对象共享的
    wheel = 4 #轮胎数量
    tax_rate = 0.1 #购税税率

    # __init__():初始化的方法,对对象设置一些属性,py内建
    # self:当前创建的实例对象,就是this,定义时,先写self
    # 然后写参数,但是调用的时候不需要写self
    def __init__(self,cname,cprice,ccolor,cbrand):
        self.name=cname
        self.price=cprice
        self.color=ccolor
        self.brand=cbrand
        self.wheel = 2
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
    print(c1.brand)
    print(c1.wheel)  #先找对象属性然后再找类属性

    print(Car.wheel) #而一般是通过类名去访问类属性