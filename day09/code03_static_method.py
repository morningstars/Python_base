"""

静态方法

"""


class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 实例方法
    def instance_print(self):
        print("instance")

    # 类方法
    @classmethod
    def class_print(cls):
        print("class")

    # 静态方法  得不到对象地址  得不到类名
    @staticmethod
    def static_print():
        print("static")


v01 = Vector2()
v01.instance_print()
v01.static_print()
v01.class_print()

Vector2.static_print()
Vector2.class_print()




