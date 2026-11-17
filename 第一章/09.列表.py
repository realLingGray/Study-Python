#列表用[]来写，有顺序，可更改
thelist = ["apple","banana","cherry"]
#索引：0：第一个，-1：最后一个。[2:5]：指的是3到5项,依旧左闭右开。负数指的是从尾巴索引
print(thelist)
print(thelist[0])
#python的列表可以支持不同类型
b = [6, 59, 80, 100, "A","This is Mr. Lee",["sad", 89],True ]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#切片操作：[开始，结束，步长]
print(thislist[2:5])
list1 = [1,2,3,5,6]
list1[2] = 10
for i in list1:
    print(i,end = "")
print()
#注意：遍历用for，for没有括号！！还要用冒号
#列表长度：len()
print(len(list1))
#append()：在末尾加入
#insert()：在某处插入：(位置,内容)
#remove()：移除指定内容
#pop()：按照位置去删，若没有参数，则是最后一个
list1.pop(0)
for i in list1:
    print(i,end = "")
print()
#del()：通用，可以删除内容也可以删除列表
#clear()：清空
#copy()：复制列表
#list()：强制转化为list，比如从tuple转到list
#合并列表：+，比如：list1 + list 2
list1 = ["I", "am"]
list2 = ["a", "Chinese"]
list3 = list1 + list2
for i in list3:
    print(i,end = " ")
print()
#当然，可以用extend()函数讲一个列表加入另一个列表末尾，用法：列表1.extend(列表2)
#注意：这是将2合并到1，而不返回结果
del list3
list1.extend(list2)
print(list1)
#sort()：排序
#reverse()：倒叙
list1 = [1,-100,50,-60,999,45,78,111111]
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)

#获取list（int型）的总和：sum()函数：
list111 = [0,1,2,3,4,5,6,7,8,9]
sum = sum(list111)
jun = sum / len(list111)
print(sum)
print(jun)
