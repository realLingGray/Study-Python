# csv操作 - 方式一： 文件操作的原始方式
# 写：
"""
with open("./csv_data/02.csv", "w", encoding="utf-8") as f:
    f.write("姓名,年龄,性别,爱好\n")# 写入表头
    f.write("小红, 20, 女, '跑步,游泳'\n") #写入数据
    f.write("小明, 30, 男, 健身\n")
    f.write("小刚, 18, 男, C++\n")


with open("./csv_data/02.csv", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip("\n"))
"""

# 方式二：csv标准库（推荐）
import csv

# 注意这里要加一个newline = ""，否则会多一个换行
with open("csv_data/02.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()
    # 参数是字典：key = value
    writer.writerow({"姓名":"小红", "年龄":20, "性别":"女", "爱好":"跑步,游泳"})
    writer.writerow({"姓名":"小明", "年龄":30, "性别":"男","爱好":"健身"})

# 读
with open("csv_data/02.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # 此时返回值为字典dict
    for row in reader:
        print(row)