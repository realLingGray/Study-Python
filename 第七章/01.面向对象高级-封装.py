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


if __name__ == '__main__':
    car = Car('宝马', 'X5', '红色', '张三')
    print(car.model)
    print(car.color)
    print(car.brand)
    car.start()
    car.run()
    car.stop()

