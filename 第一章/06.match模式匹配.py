day = input("输入星期几：")
match day:
    case "1":
        print("周一")
    case "2":
        print("周二")
    case "3":
        print("周三")
    case "4":
        print("周四")
    case "5":
        print("周五")
    case "6":
        print("周六")
    case "7":
        print("周日")
    case _:
        print("错误")