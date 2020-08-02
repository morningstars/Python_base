"""

lambda表达式
定义：变量 = lambda 形参： 方法体
调用：变量（实参）

方法体只能有一条语句 且不支持赋值语句

1.一种匿名的函数
2.

"""


def fun01():
    print("我是普通方法")


def fun02(a):
    print("我是普通方法，参数是", a)


def fun03():
    return True


fun01()
fun02(10)
print(fun03())

a01 = lambda: print("我是lambda方法")
a02 = lambda a: print("我是lambda方法，参数是", a)
a03 = lambda: True
a01()
a02(10)
print(a03())

# ----------------------------

list01 = [1, 23, 21, 432, 543, 65]

from common.custom_list_tools import ListHelper

for item in ListHelper.find_all(list01, lambda item: item > 40):
    print(item)
