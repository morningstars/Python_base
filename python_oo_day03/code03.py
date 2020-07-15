"""

    继承 -- 设计思想

        设计原则
            1.开闭原则
                开放      关闭
                对扩展     对修改
                允许增加新功能 不允许改变以前的代码

            2.依赖倒置
                使用父类

"""

"""  
    
    老张开车去东北
    
"""


class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, v, place):
        v.transport(place)


class Vehicle:

    def transport(self, pos):
        raise NotImplementedError


class Car(Vehicle):
    def transport(self, pos):
        print("行驶到" + pos)


class Plane(Vehicle):
    def transport(self, pos):
        print("飞到" + pos)


p01 = Person("zs")
p01.go_to(Plane(), "bj")
