"""
    集合 Set
"""

# 创建

s01 = set()
print(s01)

s02 = {1, 2, 3, 4, 1}
print(s02)

# 容器转换
s01 = set([1, 2, 3, 1])
l01 = list(s01)
t01 = tuple(s01)
print(l01)
print(t01)

# 添加
s01.add(5)
s01.add("a")
s01.add("c")
print(s01)

# 删除
# s01.remove("x") # 不存在会报错
print(s01)

# 删除元素
s01.discard("c")  # 不存在不会报错
print(s01)

# 获取所有元素
for item in s01:
    print(item)

#  计算

print("++++++++++++++")
s03 = {2, 3, 4}
s04 = {3, 4, 5}
print(s03 & s04)  # 交集 {3, 4}
print(s03 | s04)  # 并集 {2, 3, 4, 5}
print(s03 ^ s04)  # 对称补集 {2, 5}
print(s03 - s04)  # 补集 {2}

print(s03 > s04)  # 子集
