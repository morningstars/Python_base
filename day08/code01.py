"""

面向对象
类
对象

"""


class Wife:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cooking(self):
        print("做饭")


w01 = Wife("hello", 12)
w01.cooking()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("study")

    def work(self):
        print("work")


st01 = Student("wk", 12)
st01.study()
st01.work()
st02 = st01
st01.name = "swk"
print(st02.name)  # swk
