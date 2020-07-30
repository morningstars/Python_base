list = [2, 3, 4, 5, 6]

# 使用列表推导式和生成器表达式 获取list中大于3的数据

result = [item for item in list if item > 3]
print(result)

result2 = (item for item in list if item > 3)
for item in result2:
    print(item)
