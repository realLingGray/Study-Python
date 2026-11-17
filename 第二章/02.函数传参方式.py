def reg_stu(name, age, gender, city = "深圳"):
    # 此时 深圳就是默认值，可以不传参，用于默认构造
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"性别：{gender}")
    print(f"城市：{city}")

# 传参方式一：位置传参 按照位置去传参，严格按照位置
reg_stu("张三",22,"男", "北京")

# 传参方式二：关键字传参 按照索引去传参，可以不严格按照位置
reg_stu(name="李四", city = "南京", age = 26, gender = "男")

# 传参方式三：混合 --->  位置在前，关键字在后
reg_stu("小红", 19, city = "上海", gender="女")