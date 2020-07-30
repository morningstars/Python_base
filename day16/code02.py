"""

生成器表达式

"""

list = [1, 2, 3, 4, 5]
result = []
for item in list:
    result.append(item ** 2)


#列表推导式 []   字典推导式{:}  集合推导式{}
result = [item ** 2 for item in list]
print(result)


#生成器表达式
def fun01(target):
    for item in target:
        yield item ** 2

for item in fun01(list):
    print(item)

result = (item ** 2 for item in list)

for item in result:
    print(item)
