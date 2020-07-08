# 100米往下掉 弹起一半 弹多少次 走多少米

sum = 0.0
time = 0
height = 100.0

while height >= 0.01:
    time += 1
    sum += (height + height / 2)
    height = height / 2
print("一共弹了" + str(time) + "次")
print("一共走了" + str(sum) + "米")