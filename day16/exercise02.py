""""""


class Skill:
    def __init__(self, id, name, time, duration, distance):
        self.id = id
        self.name = name
        self.time = time
        self.duration = duration
        self.distance = distance


list_skills = [
    Skill(101, "降龙十八掌", 10, 20, 300),
    Skill(102, "降龙十掌", 3, 5, 130),
    Skill(103, "降龙八掌", 10, 50, 30),
    Skill(104, "降龙二十八掌", 10, 80, 730)
]

# 练习：
# 查找编号是101的（单个）技能对象
# 查找名称是降龙十八掌的技能对象
# 查找cd > 10的（单个）技能对象

from common.custom_list_tools import ListHelper

item = ListHelper.first(list_skills, lambda item: item.id == 101)
print(item.name)


# 练习
# 筛选对象
# 技能列表 --> 编号列表  【101，102，103，104】
list_ids = ListHelper.select(list_skills, lambda item: item.id)

for item in list_ids:
    print(item)

for item in ListHelper.select(list_skills, lambda item: item.name):
    print(item)

for item in ListHelper.select(list_skills, lambda item: (item.name, item.id)):
    print(item)


#练习
# 技能列表 --> 所有技能编号的和
print(ListHelper.sum(list_skills, lambda item: item.id))
print(ListHelper.sum(list_skills, lambda item: item.time))





