# 创建学生数据模型类
# 创建逻辑控制类

class Student:
    def __init__(self, name, age, score, id = 0):
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

    def __generator_id(self, stu):
        # id 自增长
        if len(self.__list_stu) > 0:
            stu.id = self.__list_stu[-1].id + 1
        else:
            stu.id = 1


s01 = Student("zs", 18, 100)
s02 = Student("ls", 18, 100)

c = StudentController()
c.add_student(s01)
c.add_student(s02)

print(c.list_stu[0].__dict__)
print(c.list_stu[1].__dict__)
