"""
    创建技能类(技能名称，冷却时间，持续时间，攻击距离......)
    要求：使用属性封装变量
   创建技能列表(技能对象的列表)
   -- 查找名称是"降龙十八掌"的技能对象
   -- 查找名称是持续时间大于１０秒的的所有技能对象
   -- 查找攻击距离最远的技能对象
   -- 按照持续时间，对列表升序排列．

"""


class Skill:
    def __init__(self, name, time, duration, distance):
        self.name = name
        self.time = time
        self.duration = duration
        self.distance = distance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value


s01 = Skill("降龙十八掌", 10, 20, 300)
s02 = Skill("降龙十掌", 3, 5, 130)
s03 = Skill("降龙八掌", 10, 50, 30)
s04 = Skill("降龙二十八掌", 10, 80, 730)

list01 = [s01, s02, s03, s04]


# - 查找名称是"降龙十八掌"的技能对象
def get_skill_from_name(list_target, name):
    for item in list_target:
        if item.name == name:
            print(item.__dict__)
            return item


get_skill_from_name(list01, "降龙十八掌")


# - 查找名称是持续时间大于１０秒的的所有技能对象
def get_skill_duration(list_target, duration):
    for item in list_target:
        if item.duration > duration:
            print(item.__dict__)


get_skill_duration(list01, 10)

print("-----------")


# - 查找攻击距离最远的技能对象
def get_skill_max_distance(list_target):
    max_distance_skill = Skill("", 0, 0, 0)

    for item in list_target:
        if item.distance > max_distance_skill.distance:
            max_distance_skill = item

    print(max_distance_skill.__dict__)


get_skill_max_distance(list01)

print("-----------")


# - 按照持续时间，对列表升序排列．
def order_skill_with_duration(list_target):
    for i in range(len(list_target) - 1):
        for j in range(i + 1, len(list_target)):
            if list_target[i].duration > list_target[j].duration:
                list_target[i], list_target[j] = list_target[j], list_target[i]

    for item in list_target:
        print(item.__dict__)


order_skill_with_duration(list01)
