"""

迭代器
可迭代对象

"""

list01 = [12, 23, 432, 123]

# for item in list01:
#     print(item)

# for循环等同于下面的代码

# 1.获取迭代器
iterator = list01.__iter__()
while True:
    try:
        # 2.调用迭代器的__next__()方法
        item = iterator.__next__()
        print(item)
        # 3.结束迭代
    except StopIteration:
        break


# 自定义可迭代对象

class Skill:
    def __init__(self):
        pass


class SkillManager:
    def __init__(self, skills):
        self.skills = skills

    def __iter__(self):
        # 创建迭代器对象 传递迭代数据
        return SkillIterator(self.skills)


class SkillIterator:
    def __init__(self, targets):
        self.targets = targets
        self.index = 0

    def __next__(self):
        # 索引越界 抛出异常
        if self.index > len(self.targets) - 1:
            raise StopIteration()

        item = self.targets[self.index]
        self.index += 1
        return item


list02 = SkillManager([Skill(), Skill()])

for item in list02:
    print(item)
