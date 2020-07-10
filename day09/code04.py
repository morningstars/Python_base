"""

静态方法

"""


class Vector2:
    """
    二维坐标系
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


"""
取出二维数组坐标  方向上的 几个数据

[0][0]  [0][1]  [0][2]  [0][3]
[1][0]  [1][1]  [1][2]  [1][3]
[2][0]  [2][1]  [2][2]  [2][3]
[3][0]  [3][1]  [3][2]  [3][3]

"""


class Vector2Helper:

    @staticmethod
    def get_elements(map, v_positoin, v_direction, buffer):
        new_list = []
        for i in range(buffer):
            v_positoin.x += v_direction.x
            v_positoin.y += v_direction.y
            new_list.append(map[v_positoin.x][v_positoin.y])
        return new_list


map01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"],
]

Vector2Helper.get_elements(map01, Vector2(1, 1), Vector2.right(), 2)











