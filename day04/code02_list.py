"""
list 列表
"""

# 1.创建空列表

list01 = []
list01 = list()

# 2.带默认值
list02 = [1, True, 1.2]
list02 = list("abcd")
list02 = list(range(5))

# 3.添加元素
list02.append(88)
print(list02)

# insert(索引， 元素)
list02.insert(2, "x")
print(list02)

# 4.删除元素
list02.remove(2)
print(list02)

# 删除指定索引的元素
del list02[1]
print(list02)

# 5.获取元素（索引 切片）
print(list02[:3])
list02[:3] = ["a","b","c"]
print(list02)

list02[:3] = ["a","b","c","d","e"]
print(list02)

# 6.遍历元素
# for item in list02:
    # print(item)

for i in range(len(list02)):
    print(list02[i])
















