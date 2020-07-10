"""
    用属性封装变量
 定义 敌人类（姓名、攻击力、攻击速度（0-10）、血量（0-100））

"""


class Enemy:
    def __init__(self, name, attack, speed, hp):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 10:
            self.__speed = value
        else:
            self.__speed = 0

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            self.__hp = 0


#
e01 = Enemy("zs", 100, 5, 80)
e01 = Enemy("zs", 100, 50, 80)
e01 = Enemy("zs", 100, 50, 8200)
print(e01.__dict__)
print(e01.name, e01.attack, e01.speed, e01.hp)
