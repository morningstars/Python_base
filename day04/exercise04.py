# 输入字符串  统计字符出现的次数


str = input("输入")
dict = {}
for c in str:
    if c in dict:
        dict[c] = dict[c] + 1
    else:
        dict[c] = 1
print(dict)
