# -----------------------------------------------------
# 不定长参数：参数的长度不一定，使用 函数名(*args)来指定
# 1、位置传参
# 不一定是agrs，也可以是其他名字，比如(*a)
# 此时会封装在一个元组里面，此时的args就是元组
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data,1)

print(calc_data(2,97,9,10,56,899))

print(calc_data(2,97,9,10,56,899,100,56,11,-89,99,88888))


# 2、关键字传参
# 使用(** kwargs)来进行传参，此时，封装为字典类型

# 此时加个需求，可以自定义round的参数，不一定非得保留一位小数
# 也可以print参数，如果print = True，则要打印出来，否则只返回
def _calc_data(*args, **kwargs):
    '''
    根据传入的数据，计算最大值，最小值，平均值
    :param args:不定长数据
    :param kwargs:不定长关键字参数
        round: 保留的位数
        print: 是否打印输出
    :return:最小值，最大值，平均值
    '''
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print"):
        print(min_data, max_data, avg_data)
    return min_data, max_data, avg_data

print(_calc_data(2,97,9,10,56,899, round = 5, print = True))
print(_calc_data(2,97,9,10,56,899,100,56,11,-89,99,88888, round = 1, print = False))

