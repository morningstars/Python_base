"""

    手雷爆炸 可能伤害敌人 玩家 位置事物

"""


class Bomb:

    def explode(self, *args):
        for obj in args:
            obj.damage()


class Obj:
    def __init__(self, hp):
        self.hp = hp

    def damage(self):
        raise NotImplementedError


class Player(Obj):
    def damage(self):
        self.hp -= 10
        print("受伤", str(self.hp))


class Enemy(Obj):
    def damage(self):
        self.hp -= 100
        print("受伤", str(self.hp))


b01 = Bomb()
e01 = Enemy(100)
e02 = Enemy(200)
b01.explode(e01,e02)
