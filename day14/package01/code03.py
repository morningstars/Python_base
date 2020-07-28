"""
raise语句 主动抛出异常
自定义异常
"""


class AgeError(Exception):
    """
    封装错误信息
    """
    def __init__(self, msg, line, age_value):
        super().__init__(msg)
        self.msg = msg
        self.line = line
        self.age_value = age_value


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 < value < 80:
            self.__age = value
        else:
            raise AgeError("年龄不符", 26, value)


try:
    w01 = Wife(99)
    print(w01.age)
except AgeError as e:
    print(e.msg)
    print(e.age_value)
    print(e.line)
