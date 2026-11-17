# 此时虽然没有继承关系 但是这个类也继承了一个类：(object)
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

# 油车
class OilCar(Car):
#    pass
    def __init__(self,brand, model, color, owner, oil):
        super().__init__(brand, model, color, owner)
        self.oil = oil

    def start(self):
        print(f"{self.brand} {self.model}正在启动，需要加油")
        super().start()

    def run(self):
        print(f"{self.brand} {self.model}正在运行，油耗为{self.oil}")

    def stop(self):
        print(f"{self.brand} {self.model}正在停止")
    def __control(self):
        print(f"{self.brand} {self.model}正在被{self.__owner}控制")

# 电车
class ElectricCar(Car):
#    pass
    def __init__(self,brand, model, color, owner, battery):
        super().__init__(brand, model, color, owner)
        self.battery = battery

    def start(self):
        print(f"{self.brand} {self.model}正在启动，需要充电")
        super().start()

    def run(self):
        print(f"{self.brand} {self.model}正在运行，电池续航为{self.battery}")

    def stop(self):
        print(f"{self.brand} {self.model}正在停止")
    def __control(self):
        print(f"{self.brand} {self.model}正在被{self.__owner}控制")

if __name__ == '__main__':
    oil_car = OilCar('宝马', 'X5', '红色', '张三', 80)
    oil_car.start()
    oil_car.run()
    oil_car.stop()
    electric_car = ElectricCar('特斯拉', 'Model S', '白色', '李四', 100)
    electric_car.start()
    electric_car.run()
    electric_car.stop()
