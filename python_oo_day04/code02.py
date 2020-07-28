"""

运算符重载

"""


class Vector:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "Vector(%d)" % self.x

    def __add__(self, other):
        return Vector(self.x + other)

    def __sub__(self, other):
        return

    def __mul__(self, other):
        return

    def __truediv__(self, other):
        return

    def __floordiv__(self, other):
        return

    def __mod__(self, other):
        return

    def __pow__(self, power, modulo=None):
        return


    def __radd__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rpow__(self, other):
        pass





v01 = Vector(14)
v02 = v01 + 5
print(v02)
