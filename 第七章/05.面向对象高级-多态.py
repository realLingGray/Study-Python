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

    def charge(self):
        print(f"Car的charge函数调用中")

class ElectricCar(Car):
    def __init__(self,brand, model, color, owner, battery):
        super().__init__(brand, model, color, owner)
        self.battery = battery
    def charge(self):
        print(f"{self.brand} {self.model}正在充电")
class FuelCar(Car):
    def __init__(self,brand, model, color, owner, fuel):
        super().__init__(brand, model, color, owner)
        self.fuel = fuel
    def charge(self):
        print(f"{self.brand} {self.model}正在加油")
def handel_car(c:Car):  # 指定的是父类型，可以传入任何子类型，实现多态
    c.charge()


if __name__ == '__main__':
    e = ElectricCar('Tesla','Model S','white','Xiaoming',100)
    f = FuelCar('Tesla','Model S','white','Xiaoming',100)
    handel_car(e)
    handel_car(f)
