# 调用层层往下，而fun3出现异常则不断上报，直到到main
def fun1():
    print("fun1 is running")
    fun2()
def fun2():
    print("fun2 is running")
    fun3()
def fun3():
    print("fun3 is running")
    print(abc)
if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print(f"程序出错，请联系管理员，错误信息：{e}")