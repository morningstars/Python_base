"""

类成员

"""


class ICBC:
    # 类变量
    moneys = 9999

    def __init__(self, name, money):
        # 实例变量
        self.name = name
        self.money = money
        ICBC.moneys -= money

# 类方法
    @classmethod
    def cla(cls):
        print(cls.moneys)
        print(cls.name)


i01 = ICBC("ha", 1000)
print(ICBC.moneys)
i02 = ICBC("he", 2000)
print(ICBC.moneys)

ICBC.cla()
