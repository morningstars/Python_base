"""

    可变对象传参
    类型：列表，字典，集合
    函数内部可以改变原数据的值

"""


def fun01(list):
    list[0] = 11
    print("list[0]:" + str(list[0]))  # 11


# 可变对象传参  可直接改变对象
list_num = [1, 2]
fun01(list_num)
print("list_num[0]:" + str(list_num[0]))  # 11
