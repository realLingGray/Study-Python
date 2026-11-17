# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.math + self.english + self.chinese}"
    # 修改学生成绩
    def update_score(self, chinese = None, math = None, english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
# 教务管理系统
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] # 列表，记录在校学生信息
    # 添加学生成绩
    def add_student(self):
        name=input("输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("输入学生有误（已存在当前学生）！")
                return
        chinese=int(input("输入学生语文成绩："))
        math=int(input("输入学生数学成绩："))
        english=int(input("输入学生英语："))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            self.student_list.append(Student(name, chinese, math, english))
            print(f"成绩合法，学生{name}创建成功！")
        else:
            print(f"成绩非法！学生{name}创建失败！")

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前学生{name}查询成功，信息：\n{s}")
                chinese = int(input("输入学生语文成绩："))
                math = int(input("输入学生数学成绩："))
                english = int(input("输入学生英语："))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_sorce(chinese, math, english)
                    print(f"成绩合法，学生{name}修改成功！")
                    print(f"当前学生信息为\n“{s}")
                    return
                else:
                    print(f"成绩非法！学生{name}修改失败！")
                    return
        print(f"未查询到学生{name}，输入非法！")
    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前学生{name}查询成功，信息：\n{s}")
                ope = input("请确认是否删除？ Y/y：").upper()
                if ope == "Y":
                    self.student_list.remove(s)
                    print(f"已删除学生{name}")
                    return
                else:
                    print(f"已取消对学生{name}的删除操作")
                    return
        print(f"未查询到学生{name}，输入非法！")
    # 查询学生成绩
    def find_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前学生{name}查询成功，信息：\n{s}")
                return
        print(f"未查询到学生{name}，输入非法！")
    # 展示全部学生的成绩
    def show_student(self):
        for s in self.student_list:
            print(s)
if __name__ == '__main__':
    mag = EduManagement()
    print(f"当前系统为：{mag.system_name}    当前版本为：{mag.system_version}",end = "")
    oper = "0"
    intro = """
    ################################
    #     1、添加学生成绩           #
    #     2、修改学生成绩           #
    #     3、删除学生成绩           #
    #     4、查询学生成绩           #
    #     5、展示全部学生的成绩      #
    #     6、退出系统               #
    ################################
"""
    while oper!= "6":
        print(intro,end = "")
        oper = input("请输入操作序号：")
        try:
            match oper:
                case "1":
                    mag.add_student()
                case "2":
                    mag.update_student()
                case "3":
                    mag.delete_student()
                case "4":
                    mag.find_student()
                case "5":
                    mag.show_student()
                case "6":
                    print("欢迎下次使用")
                case _:
                    print("输入操作序号非法！！")
        except ValueError:
            print(f"输入的值出现错误！！重新输入！")
