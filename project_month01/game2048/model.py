"""

数据类

"""


class Location:
    def __init__(self, r, c):
        self.__r_index = r
        self.__c_index = c

    @property
    def r_index(self):
        return self.__r_index

    @r_index.setter
    def r_index(self, value):
        self.__r_index = value

    @property
    def c_index(self):
        return self.__c_index

    @c_index.setter
    def c_index(self, value):
        self.__c_index = value
