#字符串有不可变性、有序性和可迭代行
#不可变
str = "ABCDEFG"
#此时会报错，故不可变
# str[0] = "O"
# print(str)
#有序性，可以索引
print(str[2])
print(str[0:])
print(str[-1:-7])
#此时没有内容，是因为步长没写默认是1，而start和end方向是倒着
#步长为1是正着，不对，因此步长应为-1
print(str[-1:-8:-1])
#此时 为倒叙
#迭代器，不用说了
for i in str:
    print(i)