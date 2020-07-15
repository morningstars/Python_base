"""

继承语法 -- 方法

"""


class Person:
    def say(self):
        print("说")


class Student(Person):
    def study(self):
        print("学习")


class Teacher(Person):
    def teach(self):
        print("教")


s01 = Student()
s01.study()
s01.say()

print(isinstance(s01, Person))  # True
print(isinstance(s01, Teacher))  # False
print(isinstance(s01, Student))  # True

print(issubclass(Student, Person))  # True
print(issubclass(Student, Teacher))  # False
print(issubclass(Student, Student))  # True


