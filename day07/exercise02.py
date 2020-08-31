"""

    统计一个函数的调用次数

"""

num = 0


def fun01():
    print("调用了")
    global num
    num += 1


for i in range(10):
    fun01()

print("一共调用了" + str(num) + "次")
