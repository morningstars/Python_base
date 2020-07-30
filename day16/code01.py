"""
内置生成器
枚举函数 enumerate


"""

list01 = ["a", "b", "c"]

for item in enumerate(list01):
    print(item)

for index, element in enumerate(list01):
    print(index, element)

"""自定义enumerate"""


def my_enumerate(target):
    for i in range(len(target)):
        yield (i, target[i])


for item in my_enumerate(list01):
    print(item)

for index, element in my_enumerate(list01):
    print(index, element)

"""zip函数"""
list02 = [101, 102, 103]
list03 = ["A", "B", "C"]
for item in zip(list02, list03):
    print(item)

"""自定义zip函数"""


def my_zip(target1, target2):
    for i in range(len(target1)):
        yield (target1[i], target2[i])


for item in my_zip(list02, list03):
    print(item)
