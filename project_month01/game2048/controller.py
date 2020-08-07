"""

逻辑处理

"""

import random
from game2048.model import Location


class GameCoreController:

    def __init__(self):
        self.__map = [[2, 0, 4, 4],
                      [2, 2, 2, 2],
                      [4, 0, 2, 2],
                      [4, 0, 0, 0]]

        self.__list_merge = []

        self.__list_empty_location = []

    # 只读
    @property
    def map(self):
        return self.__map

    #  将0元素移动至末尾
    def zero_to_end(self):
        zerocount = self.__list_merge.count(0)
        # 1.删除0元素 从末尾开始删除
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]

                # 2.末尾加0
                self.__list_merge += [0] * zerocount

    # 合并函数
    def merge(self):
        self.zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] *= 2
                self.__list_merge[i + 1] = 0
                self.zero_to_end()

    # 定义移动函数
    # 左移
    def move_left(self):
        for i in range(len(self.__map)):
            self.__list_merge[:] = self.__map[i]
            self.merge()
            self.__map[i][:] = self.__list_merge

    # 右移
    def move_right(self):
        for i in range(len(self.__map)):
            # 切片生成一个新的列表
            self.__list_merge[:] = self.__map[i][::-1]

            self.merge()
            # 赋值
            self.__map[i][::-1] = self.__list_merge

    # 上移
    def move_up(self):
        for i in range(4):
            self.__list_merge.clear()
            for j in range(4):
                self.__list_merge.append(self.__map[j][i])
            self.merge()
            for j in range(4):
                self.__map[j][i] = self.__list_merge[j]

    # 下移
    def move_down(self):
        for i in range(4):
            self.__list_merge.clear()
            for j in range(3, -1, -1):
                self.__list_merge.append(self.__map[j][i])
            self.merge()
            for j in range(3, -1, -1):
                self.__map[j][i] = self.__list_merge[3 - j]

    def generate_new_num(self):
        # 10%概率生成4  90%概率生成2
        random_rate = random.randint(0, 9)
        if random_rate == 0:
            random_num = 4
        else:
            random_num = 2

        # 获取生成随机数的随机位置
        self.__list_empty_location.clear()
        for i in range(4):
            for j in range(4):
                if self.__map[i][j] == 0:
                    loc = Location(i, j)
                    self.__list_empty_location.append(loc)

        if len(self.__list_empty_location) == 0:
            return

        # 从空位置列表随机选取一个元素
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(0, 9) == 0 else 2

        self.__list_empty_location.remove(loc)

    # 二维列表 以表格格式显示在控制台
    def print_map(self):
        for i in range(len(self.__map)):
            for j in range(len(self.__map[i])):
                print(self.__map[i][j], end=" ")
            print()
