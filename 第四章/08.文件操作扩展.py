"""
相对路径和绝对路径：
相对路径：是相对于当前文件的路径（推荐）
    ./ 表示当前目录
    ../ 表示上一级目录

绝对路径：是相对于根目录的路径
    1、要写完整路径（注：\在py中是转义字符，因此要加一个\，来转义）
    "E:\\文件\\Study\\Python\\basic-code\\第四章\\resource\\China.txt"
    2、或者是一个正斜线，也是可以的：/
    E:/文件/Study/Python/basic-code/第四章/resource/China.txt
    3、或者写成：
"""
#    r"E:\文件\Study\Python\basic-code\第四章\resource\China.txt"
#   也是可以的




# 读文件
with open(r"E:\文件\Study\Python\basic-code\第四章\resource\China.txt", "r", encoding = "utf-8") as f:
    content = f.read()
    print(content)


# 除了w是写入内容，a是追加内容，w会覆盖掉原来的内容，而a会在后面追加内容，不会覆盖
# 原来的内容
# 写文件
with open(r"E:\文件\Study\Python\basic-code\第四章\resource\China.txt", "a", encoding = "utf-8") as f:
    f.write("Hello, World!")
