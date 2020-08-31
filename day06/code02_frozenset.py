"""

固定集合
frozenset


"""

f01 = frozenset([1, 2, 3, 3, 4])
print(type(f01))

# 随意输入字符串 按q退出 显示不重复字符串

# s01 = set()
# while True:
#     str = input("请输入字符串")
#     if str == "q":
#         break
#     else:
#         s01.add(str)
# print(s01)

print("===================")

managers = frozenset(["c", "l", "s"])
techs = frozenset(["c", "l", "z", "g"])

# 1
print(managers & techs)  # {'l', 'c'}

# 2
print(managers - techs)  # {'s'}

# 3
print(techs - managers)  # {'g', 'z'}

# 4
print("z" in managers)  # False

# 5
print(managers ^ techs)  # {'g', 's', 'z'}

# 6
print(len(managers | techs))  # 5
