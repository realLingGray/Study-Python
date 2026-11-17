# Python可以使用变量: 类型，来进行注解这个变量是什么类型，但是只是注解
# 只是做语法提示，如果要真正运行依然能够通过
a: int = 60
print(a)
a = 66.66
# 此时编辑器会提示有问题，但仅仅只是提示，如果真正运行，依然能够运行
print(a)

# list:
names: list[str] = ['A', 'B', 'C', 'D']
print(names)
names.append(99.66)
# 依旧只是做语法提示
print(names)
# tuple:
name1: tuple[str,int] = ('A', 666)
print(name1)
# dict:
name2: dict[str, int] = {'A': 100, 'B': 200, 'C': 300}
print(name2)
# set:
name3: set[str | int] = {'A', 100, 'B', 200, 'C'}
# 可以使用 | 来进行两个都可以的运算
print(name3)

b = 88.66
b = 5
# 其实当你不写的时候，python解释器也会自动加上: float的字样做推断
# 此时和写了: float的结果一样，都只是做语法提示，真正编译运行依旧可以
print(b)

c: int | str | float = 6
print(c)
c = "哈哈啊哈"
print(c)
c = 996.6