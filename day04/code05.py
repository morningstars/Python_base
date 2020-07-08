# 列表推导式

list01 = [1, 2, 3, 4, 5]
list02 = []
for item in list01:
    list02.append(item ** 2)
print(list02)

list03 = [item ** 2 for item in list01 if item % 2 == 0]
print(list03)

# 练习  range生成1-10数字 存入list
list = []
for item in range(1, 11, 1):
    list.append(item)
print(list)

list = [item for item in range(1, 11)]
print(list)
# 将奇数存入 list02  偶数存入list03
list02 = [item for item in list if item % 2 == 1]
list03 = [item for item in list if item % 2 == 0]
print(list02)
print(list03)
