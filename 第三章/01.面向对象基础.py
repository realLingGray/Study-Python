# 不推荐 ------->这种动态添加属性的方式
# 定义类
class Car:
    pass
c1 = Car()
# 动态的为对象添加属性,与C++/Java不一样的是
c1.brand = "BMW"
c1.name = "X5"
c1.price = 150000

print(c1)
# 直接输出是内存地址,还有是哪个类的对象
# __dict__这个是py的内建变量,是列出这个对象的所有属性,此时是字典类型
print(c1.__dict__)
# 列出某一个属性
print(c1.brand)
