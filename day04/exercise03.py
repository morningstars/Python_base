#输入一个整数 打印一个矩形
"""
        ****
        *  *
        *  *
        ****
"""

num = int(input("输入整数"))
for index in range(0,num):
    if(index == 0 or index == num-1):
        print("*" * num)
    else:
        print("*" + " "*(num-2) + "*")
