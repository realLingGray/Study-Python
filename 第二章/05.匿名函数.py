# 方法：lambda 参数: 函数体
# 比如：lambda x, y : print(x+y)
# lambda函数无需return，他会自动return
# lambda x, y : x + y
# 可以用一个变量 接受
# aaa = lambda : sdadasds
def out_line():
    print("------------------------------------------")
line = lambda : print("------------------------------------------")
line()

add = lambda x,y : x + y
print(add(10, 30))



data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)
# sort()有一个key参数，对于sort()函数工作时，会把每一项item放进key
# 函数中进行获取数值，而根据这个数值进行排序
# 匿名函数的典型应用 ： 通常作为高阶函数的参数
data_list.sort(key = lambda item: len(item))
print(data_list)
