"""

    若干个图形
    计算面积
    定义图形管理器 记录所有图形 提供计算总面积方法


"""


class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("圆形面积", str(3.14 * self.radius ** 2))
        return 3.14 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("长方形面积", str(self.length * self.width))
        return self.length * self.width


class ShapeAreaManager:

    def __init__(self):
        self.__shape_list = []

    def add_shape(self, s):
        if not isinstance(s, Shape):
            return
        self.__shape_list.append(s)

    def calculate(self):
        total_area = 0
        for shape in self.__shape_list:
            total_area += shape.area()
        print("总面积", str(total_area))


s01 = Circle(10)
s02 = Rectangle(10, 20)

manager = ShapeAreaManager()
manager.add_shape(s01)
manager.add_shape(s02)
manager.add_shape("12")
manager.calculate()
