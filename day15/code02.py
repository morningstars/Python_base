"""

生成器函数
带有yield关键字的函数

"""


def foo():
    while True:
        yield 4


g = foo()

list01 = [123, 12234, 234, 234, 23, 4, 234, 23, 4]


# 在list01中挑出所有偶数 要求使用生成器函数实现

def get_ou(list):
    for item in list:
        if item % 2 == 0:
            yield item


iter01 = get_ou(list01)
for item in iter01:
    print(item)