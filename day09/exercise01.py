"""
    用方法封装变量
 定义 敌人类（姓名、攻击力、攻击速度（0-10）、血量（0-100））

"""


class Enemy:
    def __init__(self, name, attack, speed, hp):
        self.set_name(name)
        self.set_attack(attack)
        self.set_speed(speed)
        self.set_hp(hp)

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_attack(self, value):
        self.__attack = value

    def get_attack(self):
        return self.__attack

    def set_speed(self, value):
        if 0 <= value <= 10:
            self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value

    def get_hp(self):
        return self.__hp


e01 = Enemy("zs", 100, 5, 80)
e01 = Enemy("zs", 100, 50, 80)
e01 = Enemy("zs", 100, 50, 800)
print(e01.__dict__)
print(e01.get_name(),e01.get_attack())
