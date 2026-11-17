#将多个元素放进tuple就是组包操作：
t1 = (45,89,56,10)
#不加括号 也可以
t2 = 45,56,9,8
print(type(t2))
#解包操作：操作一：
a,b,c,d = t2
print(a,b,c,d)
#如果元素太少是会报错的，是不可以的：
# e,f,g = t2
#操作二：要首尾，其余放进list中：
first, *other, last = t1
print(first, other, last)
#当然你也可以取消first/last
first, *other = t1
print(first, other)
#*会收集所有的剩余元素，封装在list方便后续操作
#有了组包和解包，可以方便数值交换
a = 10
b = 20
c = 30
b,a = a,b
print(a,b,c)
#因为a,b相当于组包，而b,a相当于解包，因为第一个是b而包中第一个是a故交换了
c, b, a = a,b,c
print(a,b,c)