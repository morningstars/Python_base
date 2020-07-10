"""

1. 描述一下场景
zs 教 ls 学习python
ls 教 zs 玩游戏
zs 工作 挣了8000元
ls 工作 挣了3000元

"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def help(self, p_other, work):
        print(self.name + "教" + p_other.name + work)

    def work(self, reward):
        print(self.name + "工作挣了" + reward)


# class Action:
#     def __init__(self, action):
#         self.action = action
#
#     @property
#     def action(self):
#         return self.__action
#
#     @action.setter
#     def action(self, value):
#         self.__action = value


p1 = Person("zs")
p2 = Person("ls")

p1.help(p2, "学习python")
p2.help(p1, "玩游戏")

p1.work("3000元")
p2.work("8000元")
