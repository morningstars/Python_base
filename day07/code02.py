
"""
内存图
    不可变对象传参
    类型：基础数据类型 ，元组，固定集合
    函数内部不会改变原数据的值
"""


def fun01(num01):
    num01 = 2
    print("num01:" + str(num01))  # 2


number01 = 1

# 调用方法  内存中开辟空间（栈帧）
# 栈帧中定义该方法内部创建的变量

fun01(number01)
print("number01:" + str(number01)) # 1



