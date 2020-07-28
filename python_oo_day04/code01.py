"""

类和类的三大关系
泛化：继承
关联：作为变量
依赖：作为参数

"""

"""
重写类的 __str__  __repr__ 方法
__str__  返回给人看  类似于oc的description
__repr__ 返回给机器看
"""


class StudentModel:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名：%s, 年龄：%d" % (self.name, self.age)
        # return "hello"

    def __repr__(self):
        return "StudentModel('%s', %d)" % (self.name, self.age)


s01 = StudentModel("zs", 12)
s02 = eval(s01.__repr__())

print(s01)
print(s02)

list01 = [s01,s02]
print(list01)



