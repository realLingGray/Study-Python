class Car:
    def __init__(self,brand, model, color, owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner =  owner # 约定的私有属性


    def __control(self):  # 约定的私有方法
        print(f"{self.brand} {self.model}正在被{self.__owner}控制")


    def start(self):
        print(f"{self.brand} {self.model}正在启动")
        self.__control()

    def run(self):
        print(f"{self.brand} {self.model}正在运行")

    def stop(self):
        print(f"{self.brand} {self.model}正在停止")

# Huawei智能驾驶
class HuaweiAIDriving:
    def __init__(self, version = '1.0.0'):
        self.version = version
    def run(self):
        print(f"Huawei AI Driving {self.version} is running")

class WenjieCar(Car, HuaweiAIDriving):
    def __init__(self,brand, model, color, owner,version = '1.0.0'):
        # 因为先继承的Car类 因此调用super是调用的Car类的__init__方法
        super().__init__(brand, model, color, owner)
        # 如果要调用第二个爹 那么要用类名.函数的方法去做
        HuaweiAIDriving.__init__(self, version)


# 多继承的MRO（Method Resolution Order）准则：优先使用第一个父类去初始化
if __name__ == '__main__':
    c = WenjieCar('BMW','X5','red','Xiaoming','1.20.0')
    print(c.__dict__)

    
    # 查看多继承的MRO顺序
    # print(WenjieCar.__mro__)
    # print(WenjieCar.mro())

    # MRO原则 先运行Car方法
    c.run()
