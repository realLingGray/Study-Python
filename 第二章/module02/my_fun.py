# __all__这个变量是python内置的变量，就是设置其他py文件导入此文件
# 时，当使用 * 来导入时，有哪些函数就会被导入
# 注意：all只影响 * 导入时的函数数量，不影响其他的导入
__all__ = ["log_seoa1", "log_seoa2", "log_seoa3"]


# 常量（一般不会发生变化的量）  全大写
PI = 3.14159
NAME = "LingGray"

def log_seoa1():
    print("+ " * 30)
def log_seoa2():
    print("- " * 30)
def log_seoa3():
    print("* " * 30)
def log_seoa4():
    print("/ " * 30)
# __name__：这个是python的内置变量 如果此时直接运行这个py
# 此时的__name__会 = "__main__"，当导入时，__name__是模块的名称
# 就是说不是__main__，因为在测试
print(__name__)
# 因此，为了防止导入包的时候，运行了代码，可以加入类似于C++的主函数的功能
# 如果执行当前文件则会执行下面代码，否则不会执行
if __name__ == "__main__":
    log_seoa4()