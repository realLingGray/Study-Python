# def 函数名(参数) ***** return(返回值)
def print_line():
    print('-----------------------------')

# 使用：函数名()
print_line()

# 参数可以有多个，返回值也可以有多个，用逗号隔开：
def multFun(c1, c2):
    """
    练习两个返回值专门设置的函数 
    :param c1: 变量1
    :param c2:变量2
    :return: 为了方便测试，特意返回两个数值
    """
    return c1*c2, c1+c2
c = multFun(2,3)
print(c)
# 此时返回值是一个元组，可以利用索引[]去获取元素
print(c[0])
print(c[1])
# round()：此函数可以设定保留几位，比如(3.111111111111111111111111,1)
# 则此时就是3.1
PI = 3.1415926
print(PI * 6 * 6)
print(round(PI * 6 * 6, 1))