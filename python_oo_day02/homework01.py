# 玩家攻击敌人 敌人受伤掉血 可能死亡
# 敌人攻击玩家，玩家掉血 可能死亡


class Person:
    def __init__(self, hp=0, attack=0):
        self.hp = hp
        self.attack = attack

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack = value

    def attack_person(self, p_enemy):
        p_enemy.hp -= self.__attack
        if p_enemy.hp <= 0:
            print("死亡")


p_player = Person(100, 50)
p_enemy = Person(100, 50)

p_player.attack_person(p_enemy)
p_player.attack_person(p_enemy)