# 输入一整数  判断素数
# 只能被1和本身整除
num = int(input("请输入整数"))
div = 2
while div < num:
    if num % div == 0:
        print("不是素数")
        break
    else:
        print("是素数")
    div += 1
