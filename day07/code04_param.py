"""

    参数

"""


def fun02(a, b, c):
    print(a)
    print(b)
    print(c)


# 位置传参
fun02(1, 2, 3)

# 列表传参 用*将列表分割 与位置对应
fun02(*[2, 3, 4])

# 关键字传参
fun02(b=11, a=1, c=111)

# 字典传参 用**将字典分割 与关键字对应
fun02(**{"a": "2", "c": "3", "b": "4"})


# 默认（缺省）参数

def fun03(a, b=5, c=10):
    print(a)
    print(b)
    print(c)


fun03(11, 22)


# 星号元组形参
def fun04(*args):
    for item in args:
        print(item)


# 可以传无限制位置实参
fun04(1, 2, "as", 45, "c")


def fun05(*args, b):
    print(args)
    print(b)


fun05(2, 3, 1, b=2)


# 双星号字典形参
def fun06(**kwargs):
    print(kwargs)


# 调用 关键字传参 无限制关键字传参
fun06(a=1, b=2, c=33333)

print("------------")


def fun07(*args, **kwargs):
    print(args)
    print(kwargs)


fun07(1, 2, 3, 4, a=11, b=22, c=33)

print("------------")


def fun08(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


fun08(1, 2, 3, 4, 5, c=6, d=7, e=1, f="f")
fun08(1,2,d="d",c="c")

print()
