students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕皑", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72),
)
#1、计算每个学生的总分、各科平均分
for s in students:
    summ = s[2] + s[3] + s[4]
    average = summ / 3
    print(f"{s[1]}的总分为{summ}，平均分为{average:.2f}")
#f-string格式化：变量:2f，保留两位小数
#2、统计各科的最低分、最高分、平均分并输出
table_max_min_sum_aver = [0,100,0,0,0,100,0,0,0,100,0,0]
for s in students:
    if s[2] > table_max_min_sum_aver[0]:
        table_max_min_sum_aver[0] = s[2]
    if s[2] < table_max_min_sum_aver[1]:
        table_max_min_sum_aver[1] = s[2]
    if s[3] > table_max_min_sum_aver[4]:
        table_max_min_sum_aver[4] = s[3]
    if s[3] < table_max_min_sum_aver[5]:
        table_max_min_sum_aver[5] = s[3]
    if s[4] > table_max_min_sum_aver[8]:
        table_max_min_sum_aver[8] = s[4]
    if s[4] < table_max_min_sum_aver[9]:
        table_max_min_sum_aver[9] = s[4]
    table_max_min_sum_aver[2] += s[2]
    table_max_min_sum_aver[6] += s[3]
    table_max_min_sum_aver[10] += s[4]
for i in range(3, len(table_max_min_sum_aver),4):
    table_max_min_sum_aver[i] = table_max_min_sum_aver[i-1] / 10.0
print(f"语文的最高分是{table_max_min_sum_aver[0]},最低分是{table_max_min_sum_aver[1]}，平均分是{table_max_min_sum_aver[3]}。\n"
      f"数学的最高分是{table_max_min_sum_aver[4]},最低分是{table_max_min_sum_aver[5]}，平均分是{table_max_min_sum_aver[7]}。\n"
      f"英语的最高分是{table_max_min_sum_aver[8]},最低分是{table_max_min_sum_aver[9]}，平均分是{table_max_min_sum_aver[11]}。")
#当然，可以用之前学的知识
chinese_source = [s[2]for s in students]
math_source = [s[3] for s in students]
english_source = [s[4] for s in students]
print(f"{chinese_source}\n{math_source}\n{english_source}")
print(f"语文的最高分是{max(chinese_source)}，最低分是{min(chinese_source)}，平均分是{sum(chinese_source)/10.0}\n"
      f"数学的最高分是{max(math_source)}，最低分是{min(math_source)}，平均分是{sum(math_source)/10.0}\n"
      f"英语的最高分是{max(english_source)}，最低分是{min(english_source)}，平均分是{sum(english_source)/10.0}")
#3、查找优秀学生
good = []
for s in students:
    summ = s[2] + s[3] + s[4]
    average = summ / 3
    if(average >= 90):
        good.append(s[1])
for s in good:
    if s == good[-2]:
        print(s + "和", end = "")
    elif s == good[-1]:
        print(s, end = "")
    else:
        print(s + "、", end="")
print("是优秀学生")

#------------------------------------------------------------
#优化一下第一个需求的代码：
#可以利用元组的解包，将五个选项解包为变量
# for s in students:
# 此时，s就是元组，因此可以
for id,name,chinese,math,english in students:
    summ = chinese + math + english
    avg = summ / 3
    print(f"学号：{id}\t名字：{name}\t数学成绩：{math}\t语文成绩：{chinese}\t英语成绩：{english}")