"""
    字典
"""

d01 = {}
d02 = dict()

d01 = {"a": "A", "b": "B", "c": "C"}
d02 = dict([("a", "A"), ("b", "B")])
print(d01)
print(d02)

# 读取  赋值
d01["a"] = "AA"
print(d01)


# 删除
del d01["a"]
print(d01)

del d01
# print(d01)

# 获取所有元素
for key in d02:
    print(key)
    print(d02[key])
    print("----------")

# 获取所有键值对 （元组）
for item in d02.items():
    print(item)
    print(item[0])
    print(item[1])

print("----------")

for k,v in d02.items():
    print(k)
    print(v)

print("----------")

for k in d02.keys():
    print(k)

print("----------")
for v in d02.values():
    print(v)







