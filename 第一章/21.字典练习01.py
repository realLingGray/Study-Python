"""
案例：
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。
系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。

具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称，以及该商品的价格、数量，
       保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入
       该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为：
       "商品名称：xxx，商品价格：xxx，商品数量：xxx"。
    5. 退出购物车

结构：
shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""
from unittest import case

# 为什么要这个结构？因为名字作为关键字查询，因此不能{{"name":"Meta80", ... } ... }，这样子的查询就很费劲
# 因此使用名字作为key
shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {"price": 69, "num": 1}}
operate = 0
wrong = False
while operate != 5:
    print("########################\n###   1. 添加购物车   ###\n###   2. 修改购物车   ###\n###   3. 删除购物车   ###\n###   4. 查询购物车   ###\n###   5. 退出购物车   ###\n########################")
    if wrong:
        print("输入有误，请重新输入")
    wrong = False
    operate = input("请输入操作序号：")
    match operate:
        case "1":
            name = input("请输入商品名称：")
            if name not in shopping_cart.keys():
                price1 = input("请输入商品价格：")
                num1 = input("请输入商品数量：")
                shopping_cart[name] = {"price": price1, "num": num1}
            else:
                print("该商品已存在！")

        case "2":
            name = input("请输入商品名称：")
            if name  in shopping_cart.keys():
                price1 = input("请输入商品价格：")
                num1 = input("请输入商品数量：")
                shopping_cart[name] = {"price": price1, "num": num1}
            else:
                print("该商品不存在！")
        case "3":
            name = input("请输入商品名称：")
            if name  in shopping_cart.keys():
                shopping_cart.pop(name)
                print(f"{name}已删除！")
            else:
                print("该商品不存在！")
        case "4":
            "商品名称：xxx，商品价格：xxx，商品数量：xxx"
            i = 1
            for u,v in shopping_cart.items():
                print(f"商品{i}：",end = "")
                i += 1
                print(f"商品名称：{u}，商品价格：{v["price"]}，商品数量：{v["num"]}")
        case "5":
            break
        case _:
            wrong = True
