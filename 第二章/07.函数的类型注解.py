# 函数的类型注解的格式：def 函数名(a: 类型) ->  类型 :
#                          函数体
def calc_data(sources: list[int]) -> tuple[int, int, float]:
    min_data = min(sources)
    max_data = max(sources)
    avg_data = sum(sources) / len(sources)
    return min_data, max_data, avg_data
def calc_data2(sources: list[int]):
    min_data = min(sources)
    max_data = max(sources)
    # 此时因为加了c: float，因此编译器会知道这个函数返回float，此时可以
    # 不用定义，此为函数的自动类型注解
    avg_data:float = sum(sources) / len(sources)
    return avg_data
a = calc_data([1, 2, 3, 4])
print(a)
b = calc_data([1, 2, 3, 99.63])
# 依旧是只会报错
c: list[int] = [0]
print(c)
c = calc_data([1, 2, 3, 4])
# 此时返回值也会提示
print(c)
# 但虽然会提示，不耽误编译运行，依旧可以运行
# 会提前发现错误
d: int = calc_data2([1, 2, 3, 4])
# 此时也会提示有误，因为这是编辑器自动知道返回值为float



