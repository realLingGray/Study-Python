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


if __name__ == '__main__':
    c1 = Car("X5",150000,"red","BMW")
    print(c1.__dict__)
    c1.running()
    print(f"请付款CN￥{c1.total_cost(0.9,0.05)}")
