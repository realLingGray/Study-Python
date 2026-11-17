#将两个list合并并且去除重复部分
list1 = {1, 2, 3, 4, 5, 6}
list2 = {5, 6, 7 , 8, 9, 10}
print(list1)
print(list2)
#方法一：for循环遍历
# for item in list1:
#     list1.append(item)
#方法二：用 * 来解包，解包好后放到新的数组内
list3 = [*list1, *list2]
#方法三和四：list1 + list2可以合并，或者list1.extend(list2)，这样1后面
#就有2了
print(list3)
#此时去重，py里面可以直接使用a in list来判断，因此是个好方法
#就不用两次for循环
new_list = []
for item in list3:
    if item not in new_list:
        new_list.append(item)
print(new_list)
