"""

页面

"""
from model import *
from controller import *

class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        self.__controller = StudentController()

    def __input_students(self):
        # 1. 录入信息 生成学生对象
        stu = StudentModel()
        stu.name = input("姓名：")
        stu.age = self.input_int_value("年龄：")
        stu.score = self.input_int_value("成绩：")

        # 2. 调用控制器add_student
        self.__controller.add_student(stu)

    def input_int_value(self, holder):
        while True:
            try:
                score = int(input(holder))
                return score
            except ValueError:
                print("输入有误")
                continue


    def __show_students(self):
        if len(self.__controller.list_stu) == 0:
            print("空")
            return

        for stu in self.__controller.list_stu:
            print(stu.__dict__)

    def __display_menu(self):
        """
        显示菜单
        :return:
        """
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩降序排列")

    def __select_menu(self):
        number = input("输入选项：")

        if number == "1":
            self.__input_students()
        elif number == "2":
            self.__show_students()
        elif number == "3":
            pass
        elif number == "4":
            pass
        elif number == "5":
            pass

    def main(self):
        """
            界面入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()


