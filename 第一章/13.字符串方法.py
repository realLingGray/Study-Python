s = "Hello-Python-Hello-World"
#find()：查找字符串第一次出现参数的位置
index = s.find("-")
print(index)
#count()：统计参数出现的次数
c = s.count("o")
print(c)
#upper()：转大写，因为string不可更改，故会返回一直string
d = s.upper()
print(d)
#lower():转小写
e = s.lower()
print(e)
#split()：切割字符串，按照参数切割
f = s.split("-")
print(f)
#strip()：删除首尾的参数，没有就是空格
str = "    " + s + "------"
print(str)
print(str.strip())
print(str.strip("-"))
#replace(old, new)：更换旧值为新值
g = s.replace("Python","Java")
print(g)
#startwith()、endwith()：是否以参数为开始/结尾
print(s.startswith("Python"))
print(s.endswith("World"))
#一般来讲，如果for i in k意思是i在k里过一遍
#但是如果是i in 容器：返回值bool，意思是 i 是否在容器内
print("----------------------------------------------------")
print("-" in s)
print("Python" in s)
print("China" in s)