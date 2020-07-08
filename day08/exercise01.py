"""
练习
"""


class Enemy:
    def __init__(self, name="", hp=0, atk=0, speed=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.speed = speed

    def print_self(self):
        print(self.name, self.hp, self.atk, self.speed)


# 1. 控制台输入3个敌人 存入列表
# 2. 敌人列表输出到控制台


# list_enemy = []
# for i in range(3):
#     e = Enemy()
#     e.name = input("姓名：")
#     e.hp = input("血量：")
#     e.atk = input("攻击：")
#     e.speed = input("攻速：")
#     list_enemy.append(e)
#
# for item in list_enemy:
#     item.print_self()


# 定义函数 在敌人列表中 根据姓名查找敌人对象


list_enemy = [
    Enemy('zs', 10, 10, 10),
    Enemy('ls', 10, 20, 10),
    Enemy('ww', 10, 10, 30)
]


def find_enemy(name):
    for e in list_enemy:
        if e.name == name:
            return e


re = find_enemy("ss")
if re:
    re.print_self()
else:
    print("找不到")
