# Python的参数有很多，其中有一个比较特殊：函数
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
# 此时的oper是函数名，传递函数名进行传递函数，使用时必须oper()
def calc(x, y, oper):
    return oper(x, y)
print(calc(10,20,mul))