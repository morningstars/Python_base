"""

函数式编程

"""

def fun01():
    print("fun01")


a = fun01
a()


def fun02(fun):
    print("fun02")
    fun()

fun02(fun01)














