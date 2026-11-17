# 异常处理
# NameError
try:
    print("--------------------")
    print(my_name)
    # NameError: name 'my_name' is not defined
    print("--------------------")
except NameError as E3001:
    print(f"程序出错，请联系管理员！错误代码：E3001 错误信息：{E3001}")

# ZeroDivisionError
try:
    print("--------------------")
    print(1 / 0)
    # NameError: name 'my_name' is not defined
    print("--------------------")
except ZeroDivisionError as E3002:
    print(f"程序出错，请联系管理员！错误代码：E3002 错误信息：{E3002}")

# IndexError
try:
    print("--------------------")
    print("ABC".hhh)
    print("ABC"[10])

    # NameError: name 'my_name' is not defined
    print("--------------------")
except IndexError as E3003:
    print(f"程序出错，请联系管理员！错误代码：E3003 错误信息：{E3003}")
except Exception as E3004:
    # except Exception 表示捕获所有的异常，因为Exception是这些异常的
    # 父类
    print(f"程序运行出错  错误代码：E3004 错误信息：{E3004}")
finally:
    # 一般都是资源释放代码
    # 无论是否出错，都会执行
    print("资源释放")