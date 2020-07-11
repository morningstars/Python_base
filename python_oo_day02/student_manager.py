# 创建学生数据模型类
# 创建逻辑控制类

class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


class StudentController:

    def __init__(self):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def add_student(self, stu):
        self.__generator_id(stu)
        self.__list_stu.append(stu)

        print(stu.__dict__)

    def __generator_id(self, stu):
        # id 自增长
        if len(self.__list_stu) > 0:
            stu.id = self.__list_stu[-1].id + 1
        else:
            stu.id = 1


# s01 = Student("zs", 18, 100)
# s02 = Student("ls", 18, 100)
#
# controller = StudentController()
# controller.add_student(s01)
# controller.add_student(s02)
#
# print(controller.list_stu[0].__dict__)
# print(controller.list_stu[1].__dict__)


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
        stu.age = int(input("年龄："))
        stu.score = int(input("成绩："))

        # 2. 调用控制器add_student
        self.__controller.add_student(stu)

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


view = StudentManagerView()
view.main()
