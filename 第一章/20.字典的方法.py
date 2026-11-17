dict1 = {"小智":675,"李思":608,"李琪":478,"小黑":545,"温韬":429}
# 添加：字典名称["key"] = value
# 修改：字典名称["key"] = value
# 用[]来添加/修改，若有对应的key则为修改，若没有对应的key为添加
dict1["小明"] = 700
print(dict1)
dict1["小智"] = 500
print(dict1)
# 查询：[] / 字典名.get(key) -> value
print(dict1["李思"])
print(dict1.get("小黑"))
# keys()、values()和items()：获取所有的key、value和key-value
print(dict1.keys())
print(dict1.values())
print(dict1.items())
# pop()：根据key删除键值对，此时会返回当前key的value
print(dict1.pop("小智"))
print(dict1)

# 也可以用del
del dict1["小黑"]
print(dict1)
# 推荐使用get()，因为无报错
print(dict1.get("888","没有这个数值"))
print(dict1)
# 遍历的时候，用for遍历keys/items，遍历items时，因为给的是元组，可以用
# [0] / [1]来获取，也可以解包
for item in dict1.items():
    print(item)
for m,v in dict1.items():
    print(f"{m}：{v}")