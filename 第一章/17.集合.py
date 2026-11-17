#集合用{}来表示
#集合的特征：无序、不可重复、可修改
s1 = {1,1,1,1,1,2,3,4}
print(s1)
print(type(s1))
#定义空集合不能用{}，因为这样是空字典，要用构造函数set()
s2 = set()
print(type(s2))
d = {}
print(type(d))

#--------------------------------------------------------------
#集合的一些方法：
# add()：添加元素
s1.add(98)
print(s1)
# 删除指定元素：
#若删除没有的元素会报错：
# s1.remove(666)
s1.remove(1)
print(s1)
# pop()：随机删除元素，而且删除的元素会返回
val = s1.pop()
print(val)
print(s1)
# clear()：清空集合
s1.clear()
print(s1)
# 此时输出的是set()
# 接下来是交并补
s1 = {'C','H','I','N','A'}
s2 = {'U','S','A'}
# difference()：求差集（存在于第一个集合但不存在于第二个集合）
print(s1.difference(s2))
# union()：求并集
print(s1.union(s2))
# intersection()：求交集
print(s1.intersection(s2))
# ----------------------------------------------------------------
# 交集：intersection()，也可以用 & 符号
# 并集：union()，也可以用 | 符合
# 差集：difference()，也可以用 - 符号