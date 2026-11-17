# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1、找出同时选修了防法语和艺术的学生
print(french_set.intersection(art_set))

# 2、找出同时选了四门课的学生
print(football_set.intersection(basketball_set).intersection(french_set).intersection(art_set))

# 3、找出选修了足球、但是没选修篮球的学生
print(football_set.difference(basketball_set))

# 4、统计每一个学生选修的课程数量
fourclass_set = football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)
threeclass_set = basketball_set.intersection(french_set).intersection(art_set).union(football_set.intersection(french_set).intersection(art_set)).union(football_set.intersection(art_set).intersection(basketball_set)).union(football_set.intersection(basketball_set).intersection(french_set)).difference(fourclass_set)
print(f"选择了四门课程的同学有{fourclass_set}")
print(f"选择了三门课程的同学有{threeclass_set}")
twoclass_set = football_set.intersection(basketball_set).union(football_set.intersection(french_set)).union(football_set.intersection(art_set)).union(basketball_set.intersection(french_set)).union(basketball_set.intersection(art_set)).union(french_set.intersection(art_set)).difference(threeclass_set).difference(fourclass_set)
print(f"选择了两门课程的同学有{twoclass_set}")
oneclass_set = football_set.union(basketball_set).union(french_set).union(art_set).difference(fourclass_set).difference(twoclass_set).difference(threeclass_set)
print(f"选择了一门课程的同学有{oneclass_set}")

# -----------------------------------------------------
# 方法二：利用list，但是时间复杂度提升
all_set = football_set.union(basketball_set).union(french_set).union(art_set)
class_list = [*football_set, *basketball_set, *french_set, *art_set]
for student in all_set:
    print(f"{student}同学选修了{class_list.count(student)}门课程")
