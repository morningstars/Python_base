"""
封装
继承：重用现有类的概念 并在此基础上进行扩展
    作用：隔离客户端代码与实现方式


多态：子类指针赋值给父类，父类调用子类的方法


"""

"""
技能
"""


class ImpactEffect:
    def impact(self):
        raise NotImplementedError


class Damage(ImpactEffect):
    """
    伤害
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("受到%.0f伤害" % self.value)


class SpeedCut(ImpactEffect):
    """
    减速
    """

    def __init__(self, ratio, duration):
        self.ratio = ratio
        self.duration = duration

    def impact(self):
        print("减速%.1f,持续%.1f秒" % (self.ratio, self.duration))


class SkillActor:
    list_skill_effect = []

    def __init__(self, skill_name):
        self.skill_name = skill_name
        self.__list_skill_effect = self.load_skill()

    def load_skill(self):
        dict_skill = {"wg1": ["Damage(100)"],
                      "wg2": ["Damage(200)", "SpeedCut(0.4,5)"]}

        # list_impact = []
        # for item in dict_skill[self.skill_name]:
        #     # eval(item)
        #     list_impact.append(eval(item))

        return [eval(item) for item in dict_skill[self.skill_name]]

    def perform_skill(self):
        for item in self.__list_skill_effect:
            # print(item[self.skill_name])
            item.impact()


jn1 = SkillActor("wg1")
jn1.perform_skill()

jn2 = SkillActor("wg2")
jn2.perform_skill()
