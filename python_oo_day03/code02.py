"""

继承语法 -- 数据

"""


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, score):
        super().__init__(name)  # 调用父类构造函数 super().__init__()
        self.score = score


class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


s01 = Student("zs", 100)
t01 = Teacher("ls", 1000)

print(s01.score)
print(t01.salary)

p02 = Person("ww")
