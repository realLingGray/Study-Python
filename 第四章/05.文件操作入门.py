def read_test():
    # 1、打开文件
    f = open("resource/China.txt", "r", encoding="utf-8")

    # 2、文件操作

    # content1 = f.read() # 读取所有内容
    # content2 = f.read(10) # 读取前10个字符
    # content3 =  f.readline() # 读取一行
    content4 =  f.readlines() # 读取所有行，返回一个列表

    for line in content4:
        # 因为读取进去每一行后面会多一个\n，因此需要strip()
        print(line.strip())

    # 3、关闭文件

    f.close()
def write_test():
    # 1、打开文件
    f = open("resource/USA.txt", "w", encoding="utf-8")

    # 2、文件操作

    # content1 = f.read() # 读取所有内容
    # content2 = f.read(10) # 读取前10个字符
    # content3 =  f.readline() # 读取一行
    # content4 = f.readlines()  # 读取所有行，返回一个列表
    # 可以通过\n来写入换行
    try:

        content = "The United States of America (USA), also known as the United States (U.S.) or America, is a country primarily located in North America. It is a federal republic consisting of 50 states and a federal capital district, Washington, D.C. The 48 contiguous states border Canada to the north and Mexico to the south, with the semi-exclave of Alaska in the northwest and the archipelago of Hawaii in the Pacific Ocean. The United States also asserts sovereignty over five major island territories and various uninhabited islands in Oceania and the Caribbean.[k] It is a megadiverse country, with the world's fourth-largest total area[l] and third-largest population, exceeding 341 million.[m]"
        f.write(content)
        # 1 / 0

    # 3、关闭文件
    finally:
        f.close()
        print("closed")

def better_write_test():
    # 真正项目开发中的写法
    # 是使用with关键字来打开文件，这样可以自动关闭文件，也确保正确释放资源
    with open("resource/USA.txt", "w", encoding="utf-8") as f:
        content = "The United States of America (USA), also known as the United States (U.S.) or America, is a country primarily located in North America. It is a federal republic consisting of 50 states and a federal capital district, Washington, D.C. The 48 contiguous states border Canada to the north and Mexico to the south, with the semi-exclave of Alaska in the northwest and the archipelago of Hawaii in the Pacific Ocean. The United States also asserts sovereignty over five major island territories and various uninhabited islands in Oceania and the Caribbean.[k] It is a megadiverse country, with the world's fourth-largest total area[l] and third-largest population, exceeding 341 million.[m]"
        f.write(content)


if __name__ == '__main__':
    better_write_test()