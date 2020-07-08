"""

2048 核心算法

"""


#  方法1、将0元素移动至末尾
# 【2，0，2，0】 -》 【2，2，0，0】

#  方案一
def zero_to_end(list_target):
    # 1.取出非0元素 放入新列表
    list_new = [item for item in list_target if item != 0]
    # 2.末尾追加0
    list_new += [0] * list_target.count(0)
    # 3.将新列表的值赋值给原列表
    list_target[:] = list_new

#  方案二
def zero_to_end2(list_target):
    zerocount = list_target.count(0)
    # 1.删除0元素 从末尾开始删除
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]

    # 2.末尾加0
    list_target += [0] * zerocount


# list01 = [0, 0, 4, 2]
# zero_to_end2(list01)
# print(list01)


# 方法2、合并函数
# 【2，2，0，0】 -》 【4，0，0，0】
# 【2，2，0，2】 -》 【4，2，0，0】
# 【4，0，2，2】 -》 【8，0，0，0】

def merge(list_target):
    zero_to_end2(list_target)

    for i in range(len(list_target) - 1):
        if list_target[i] == list_target[i + 1]:
            list_target[i] *= 2
            list_target[i + 1] = 0
        zero_to_end2(list_target)


list01 = [4, 0, 2, 2]
merge([2, 4, 4, 0])
merge(list01)
print(list01)

print("-------------")

# 方法3、二维列表 以表格格式显示在控制台

map01 = [
    [2, 0, 2, 0],
    [2, 2, 2, 0],
    [2, 0, 4, 4],
    [4, 0, 2, 2],
]


def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=" ")
        print()


# print_map(map01)


# 方法4、定义移动函数
"""
    [2, 0, 2, 0]                 [4, 0, 0, 0]
    [2, 2, 2, 0]                 [4, 2, 0, 0]
    [2, 0, 4, 4]                 [2, 8, 0, 0]
    [4, 0, 2, 2]                 [8, 0, 0, 0]      
"""


# 左移
def move_left(map):
    for i in range(len(map)):
        merge(map[i])
    print_map(map)


# 右移
def move_right(map):
    for i in range(len(map)):
        # 切片生成一个新的列表
        list_merge = map[i][::-1]
        merge(list_merge)
        # 赋值
        map[i][::-1] = list_merge


# 上移
def move_top(map):
    new_map = [4 * [0] for _ in range(4)]
    for i in range(len(map01)):
        for j in range(len(map01[i])):
            new_map[j][i] = map01[i][j]

    move_left(new_map)

    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            map[j][i] = new_map[i][j]


# 下移
def move_bottom(map):
    new_map = [4 * [0] for _ in range(4)]
    for i in range(len(map01)):
        for j in range(len(map01[i])):
            new_map[j][i] = map01[i][j]

    move_right(new_map)

    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            map[j][i] = new_map[i][j]


# move_left(map01)
# move_right(map01)
print_map(map01)

print("-------")
# move_top(map01)
move_bottom(map01)
print_map(map01)
