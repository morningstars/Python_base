"""

限制对象的数据

"""


class Skill:
    __slots__ = ("__name")

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


s01 = Skill("hello")
# s01.time = 5
print(s01.name)

# print(s01.time)
