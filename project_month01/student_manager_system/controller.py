"""

bll 业务逻辑层

"""
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
